# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_esa20240910 import models as esa20240910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models


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
        self._endpoint = self.get_endpoint('esa', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_client_certificate_with_options(
        self,
        request: esa20240910_models.ActivateClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ActivateClientCertificateResponse:
        """
        @summary 激活客户端证书
        
        @param request: ActivateClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateClientCertificate',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ActivateClientCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_client_certificate_with_options_async(
        self,
        request: esa20240910_models.ActivateClientCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ActivateClientCertificateResponse:
        """
        @summary 激活客户端证书
        
        @param request: ActivateClientCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateClientCertificateResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivateClientCertificate',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ActivateClientCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_client_certificate(
        self,
        request: esa20240910_models.ActivateClientCertificateRequest,
    ) -> esa20240910_models.ActivateClientCertificateResponse:
        """
        @summary 激活客户端证书
        
        @param request: ActivateClientCertificateRequest
        @return: ActivateClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_client_certificate_with_options(request, runtime)

    async def activate_client_certificate_async(
        self,
        request: esa20240910_models.ActivateClientCertificateRequest,
    ) -> esa20240910_models.ActivateClientCertificateResponse:
        """
        @summary 激活客户端证书
        
        @param request: ActivateClientCertificateRequest
        @return: ActivateClientCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_client_certificate_with_options_async(request, runtime)

    def batch_create_records_with_options(
        self,
        tmp_req: esa20240910_models.BatchCreateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchCreateRecordsResponse:
        """
        @summary 创建记录
        
        @param tmp_req: BatchCreateRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchCreateRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_list):
            request.record_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_list, 'RecordList', 'json')
        query = {}
        if not UtilClient.is_unset(request.record_list_shrink):
            query['RecordList'] = request.record_list_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchCreateRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_records_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchCreateRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchCreateRecordsResponse:
        """
        @summary 创建记录
        
        @param tmp_req: BatchCreateRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateRecordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchCreateRecordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_list):
            request.record_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_list, 'RecordList', 'json')
        query = {}
        if not UtilClient.is_unset(request.record_list_shrink):
            query['RecordList'] = request.record_list_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCreateRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchCreateRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_records(
        self,
        request: esa20240910_models.BatchCreateRecordsRequest,
    ) -> esa20240910_models.BatchCreateRecordsResponse:
        """
        @summary 创建记录
        
        @param request: BatchCreateRecordsRequest
        @return: BatchCreateRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_records_with_options(request, runtime)

    async def batch_create_records_async(
        self,
        request: esa20240910_models.BatchCreateRecordsRequest,
    ) -> esa20240910_models.BatchCreateRecordsResponse:
        """
        @summary 创建记录
        
        @param request: BatchCreateRecordsRequest
        @return: BatchCreateRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_records_with_options_async(request, runtime)

    def batch_create_waf_rules_with_options(
        self,
        tmp_req: esa20240910_models.BatchCreateWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchCreateWafRulesResponse:
        """
        @summary 批量创建WAF规则
        
        @param tmp_req: BatchCreateWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchCreateWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.shared):
            request.shared_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared, 'Shared', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        if not UtilClient.is_unset(request.shared_shrink):
            body['Shared'] = request.shared_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchCreateWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_waf_rules_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchCreateWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchCreateWafRulesResponse:
        """
        @summary 批量创建WAF规则
        
        @param tmp_req: BatchCreateWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchCreateWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchCreateWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.shared):
            request.shared_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared, 'Shared', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        if not UtilClient.is_unset(request.shared_shrink):
            body['Shared'] = request.shared_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchCreateWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_waf_rules(
        self,
        request: esa20240910_models.BatchCreateWafRulesRequest,
    ) -> esa20240910_models.BatchCreateWafRulesResponse:
        """
        @summary 批量创建WAF规则
        
        @param request: BatchCreateWafRulesRequest
        @return: BatchCreateWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_create_waf_rules_with_options(request, runtime)

    async def batch_create_waf_rules_async(
        self,
        request: esa20240910_models.BatchCreateWafRulesRequest,
    ) -> esa20240910_models.BatchCreateWafRulesResponse:
        """
        @summary 批量创建WAF规则
        
        @param request: BatchCreateWafRulesRequest
        @return: BatchCreateWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_create_waf_rules_with_options_async(request, runtime)

    def batch_delete_kv_with_options(
        self,
        tmp_req: esa20240910_models.BatchDeleteKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvResponse:
        """
        @summary 批量删除Namespace的key-value对
        
        @param tmp_req: BatchDeleteKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteKvResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchDeleteKvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.keys_shrink):
            body['Keys'] = request.keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchDeleteKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_kv_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchDeleteKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvResponse:
        """
        @summary 批量删除Namespace的key-value对
        
        @param tmp_req: BatchDeleteKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteKvResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchDeleteKvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.keys):
            request.keys_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.keys, 'Keys', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.keys_shrink):
            body['Keys'] = request.keys_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchDeleteKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_kv(
        self,
        request: esa20240910_models.BatchDeleteKvRequest,
    ) -> esa20240910_models.BatchDeleteKvResponse:
        """
        @summary 批量删除Namespace的key-value对
        
        @param request: BatchDeleteKvRequest
        @return: BatchDeleteKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_kv_with_options(request, runtime)

    async def batch_delete_kv_async(
        self,
        request: esa20240910_models.BatchDeleteKvRequest,
    ) -> esa20240910_models.BatchDeleteKvResponse:
        """
        @summary 批量删除Namespace的key-value对
        
        @param request: BatchDeleteKvRequest
        @return: BatchDeleteKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_kv_with_options_async(request, runtime)

    def batch_delete_kv_with_high_capacity_with_options(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        """
        @summary 批量删除Namespace下的KV队，支持大body的上传，上限100M
        
        @param request: BatchDeleteKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchDeleteKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_kv_with_high_capacity_with_options_async(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        """
        @summary 批量删除Namespace下的KV队，支持大body的上传，上限100M
        
        @param request: BatchDeleteKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchDeleteKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_kv_with_high_capacity(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityRequest,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        """
        @summary 批量删除Namespace下的KV队，支持大body的上传，上限100M
        
        @param request: BatchDeleteKvWithHighCapacityRequest
        @return: BatchDeleteKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_kv_with_high_capacity_with_options(request, runtime)

    async def batch_delete_kv_with_high_capacity_async(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityRequest,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        """
        @summary 批量删除Namespace下的KV队，支持大body的上传，上限100M
        
        @param request: BatchDeleteKvWithHighCapacityRequest
        @return: BatchDeleteKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_kv_with_high_capacity_with_options_async(request, runtime)

    def batch_delete_kv_with_high_capacity_advance(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        batch_delete_kv_with_high_capacity_req = esa20240910_models.BatchDeleteKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, batch_delete_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            batch_delete_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        batch_delete_kv_with_high_capacity_resp = self.batch_delete_kv_with_high_capacity_with_options(batch_delete_kv_with_high_capacity_req, runtime)
        return batch_delete_kv_with_high_capacity_resp

    async def batch_delete_kv_with_high_capacity_advance_async(
        self,
        request: esa20240910_models.BatchDeleteKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchDeleteKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        batch_delete_kv_with_high_capacity_req = esa20240910_models.BatchDeleteKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, batch_delete_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            batch_delete_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        batch_delete_kv_with_high_capacity_resp = await self.batch_delete_kv_with_high_capacity_with_options_async(batch_delete_kv_with_high_capacity_req, runtime)
        return batch_delete_kv_with_high_capacity_resp

    def batch_get_expression_fields_with_options(
        self,
        tmp_req: esa20240910_models.BatchGetExpressionFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchGetExpressionFieldsResponse:
        """
        @summary 批量获取表达式的匹配项
        
        @param tmp_req: BatchGetExpressionFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetExpressionFieldsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchGetExpressionFieldsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.expressions):
            request.expressions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.expressions, 'Expressions', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        body = {}
        if not UtilClient.is_unset(request.expressions_shrink):
            body['Expressions'] = request.expressions_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetExpressionFields',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchGetExpressionFieldsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_expression_fields_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchGetExpressionFieldsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchGetExpressionFieldsResponse:
        """
        @summary 批量获取表达式的匹配项
        
        @param tmp_req: BatchGetExpressionFieldsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetExpressionFieldsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchGetExpressionFieldsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.expressions):
            request.expressions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.expressions, 'Expressions', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        body = {}
        if not UtilClient.is_unset(request.expressions_shrink):
            body['Expressions'] = request.expressions_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchGetExpressionFields',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchGetExpressionFieldsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_expression_fields(
        self,
        request: esa20240910_models.BatchGetExpressionFieldsRequest,
    ) -> esa20240910_models.BatchGetExpressionFieldsResponse:
        """
        @summary 批量获取表达式的匹配项
        
        @param request: BatchGetExpressionFieldsRequest
        @return: BatchGetExpressionFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_expression_fields_with_options(request, runtime)

    async def batch_get_expression_fields_async(
        self,
        request: esa20240910_models.BatchGetExpressionFieldsRequest,
    ) -> esa20240910_models.BatchGetExpressionFieldsResponse:
        """
        @summary 批量获取表达式的匹配项
        
        @param request: BatchGetExpressionFieldsRequest
        @return: BatchGetExpressionFieldsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_expression_fields_with_options_async(request, runtime)

    def batch_put_kv_with_options(
        self,
        tmp_req: esa20240910_models.BatchPutKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvResponse:
        """
        @summary 批量设置Namespace的key-value对
        
        @param tmp_req: BatchPutKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchPutKvResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchPutKvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.kv_list):
            request.kv_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kv_list, 'KvList', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.kv_list_shrink):
            body['KvList'] = request.kv_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchPutKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchPutKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_put_kv_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchPutKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvResponse:
        """
        @summary 批量设置Namespace的key-value对
        
        @param tmp_req: BatchPutKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchPutKvResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchPutKvShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.kv_list):
            request.kv_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kv_list, 'KvList', 'json')
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.kv_list_shrink):
            body['KvList'] = request.kv_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchPutKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchPutKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_put_kv(
        self,
        request: esa20240910_models.BatchPutKvRequest,
    ) -> esa20240910_models.BatchPutKvResponse:
        """
        @summary 批量设置Namespace的key-value对
        
        @param request: BatchPutKvRequest
        @return: BatchPutKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_put_kv_with_options(request, runtime)

    async def batch_put_kv_async(
        self,
        request: esa20240910_models.BatchPutKvRequest,
    ) -> esa20240910_models.BatchPutKvResponse:
        """
        @summary 批量设置Namespace的key-value对
        
        @param request: BatchPutKvRequest
        @return: BatchPutKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_put_kv_with_options_async(request, runtime)

    def batch_put_kv_with_high_capacity_with_options(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        """
        @summary 批量设置Namespace的key-value对，支持最大100M的请求体
        
        @param request: BatchPutKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchPutKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchPutKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchPutKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_put_kv_with_high_capacity_with_options_async(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        """
        @summary 批量设置Namespace的key-value对，支持最大100M的请求体
        
        @param request: BatchPutKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchPutKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchPutKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchPutKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_put_kv_with_high_capacity(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityRequest,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        """
        @summary 批量设置Namespace的key-value对，支持最大100M的请求体
        
        @param request: BatchPutKvWithHighCapacityRequest
        @return: BatchPutKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_put_kv_with_high_capacity_with_options(request, runtime)

    async def batch_put_kv_with_high_capacity_async(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityRequest,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        """
        @summary 批量设置Namespace的key-value对，支持最大100M的请求体
        
        @param request: BatchPutKvWithHighCapacityRequest
        @return: BatchPutKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_put_kv_with_high_capacity_with_options_async(request, runtime)

    def batch_put_kv_with_high_capacity_advance(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        batch_put_kv_with_high_capacity_req = esa20240910_models.BatchPutKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, batch_put_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            batch_put_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        batch_put_kv_with_high_capacity_resp = self.batch_put_kv_with_high_capacity_with_options(batch_put_kv_with_high_capacity_req, runtime)
        return batch_put_kv_with_high_capacity_resp

    async def batch_put_kv_with_high_capacity_advance_async(
        self,
        request: esa20240910_models.BatchPutKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchPutKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        batch_put_kv_with_high_capacity_req = esa20240910_models.BatchPutKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, batch_put_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            batch_put_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        batch_put_kv_with_high_capacity_resp = await self.batch_put_kv_with_high_capacity_with_options_async(batch_put_kv_with_high_capacity_req, runtime)
        return batch_put_kv_with_high_capacity_resp

    def batch_update_waf_rules_with_options(
        self,
        tmp_req: esa20240910_models.BatchUpdateWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchUpdateWafRulesResponse:
        """
        @summary 批量修改WAF规则
        
        @param tmp_req: BatchUpdateWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchUpdateWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.shared):
            request.shared_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared, 'Shared', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        if not UtilClient.is_unset(request.ruleset_id):
            body['RulesetId'] = request.ruleset_id
        if not UtilClient.is_unset(request.shared_shrink):
            body['Shared'] = request.shared_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchUpdateWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_waf_rules_with_options_async(
        self,
        tmp_req: esa20240910_models.BatchUpdateWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BatchUpdateWafRulesResponse:
        """
        @summary 批量修改WAF规则
        
        @param tmp_req: BatchUpdateWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BatchUpdateWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.configs):
            request.configs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.configs, 'Configs', 'json')
        if not UtilClient.is_unset(tmp_req.shared):
            request.shared_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.shared, 'Shared', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.configs_shrink):
            body['Configs'] = request.configs_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        if not UtilClient.is_unset(request.ruleset_id):
            body['RulesetId'] = request.ruleset_id
        if not UtilClient.is_unset(request.shared_shrink):
            body['Shared'] = request.shared_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUpdateWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BatchUpdateWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_waf_rules(
        self,
        request: esa20240910_models.BatchUpdateWafRulesRequest,
    ) -> esa20240910_models.BatchUpdateWafRulesResponse:
        """
        @summary 批量修改WAF规则
        
        @param request: BatchUpdateWafRulesRequest
        @return: BatchUpdateWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_update_waf_rules_with_options(request, runtime)

    async def batch_update_waf_rules_async(
        self,
        request: esa20240910_models.BatchUpdateWafRulesRequest,
    ) -> esa20240910_models.BatchUpdateWafRulesResponse:
        """
        @summary 批量修改WAF规则
        
        @param request: BatchUpdateWafRulesRequest
        @return: BatchUpdateWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_waf_rules_with_options_async(request, runtime)

    def block_object_with_options(
        self,
        tmp_req: esa20240910_models.BlockObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BlockObjectResponse:
        """
        @summary URL封禁
        
        @param tmp_req: BlockObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlockObjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BlockObjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.maxage):
            query['Maxage'] = request.maxage
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlockObject',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BlockObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def block_object_with_options_async(
        self,
        tmp_req: esa20240910_models.BlockObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.BlockObjectResponse:
        """
        @summary URL封禁
        
        @param tmp_req: BlockObjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BlockObjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.BlockObjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.extension):
            query['Extension'] = request.extension
        if not UtilClient.is_unset(request.maxage):
            query['Maxage'] = request.maxage
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlockObject',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.BlockObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def block_object(
        self,
        request: esa20240910_models.BlockObjectRequest,
    ) -> esa20240910_models.BlockObjectResponse:
        """
        @summary URL封禁
        
        @param request: BlockObjectRequest
        @return: BlockObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.block_object_with_options(request, runtime)

    async def block_object_async(
        self,
        request: esa20240910_models.BlockObjectRequest,
    ) -> esa20240910_models.BlockObjectResponse:
        """
        @summary URL封禁
        
        @param request: BlockObjectRequest
        @return: BlockObjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.block_object_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: esa20240910_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ChangeResourceGroupResponse:
        """
        @summary 修改站点的企业资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: esa20240910_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ChangeResourceGroupResponse:
        """
        @summary 修改站点的企业资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: esa20240910_models.ChangeResourceGroupRequest,
    ) -> esa20240910_models.ChangeResourceGroupResponse:
        """
        @summary 修改站点的企业资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: esa20240910_models.ChangeResourceGroupRequest,
    ) -> esa20240910_models.ChangeResourceGroupResponse:
        """
        @summary 修改站点的企业资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_site_name_with_options(
        self,
        request: esa20240910_models.CheckSiteNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckSiteNameResponse:
        """
        @summary 校验站点名称是否可用
        
        @param request: CheckSiteNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSiteNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_name):
            query['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSiteName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckSiteNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_site_name_with_options_async(
        self,
        request: esa20240910_models.CheckSiteNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckSiteNameResponse:
        """
        @summary 校验站点名称是否可用
        
        @param request: CheckSiteNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSiteNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_name):
            query['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSiteName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckSiteNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_site_name(
        self,
        request: esa20240910_models.CheckSiteNameRequest,
    ) -> esa20240910_models.CheckSiteNameResponse:
        """
        @summary 校验站点名称是否可用
        
        @param request: CheckSiteNameRequest
        @return: CheckSiteNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_site_name_with_options(request, runtime)

    async def check_site_name_async(
        self,
        request: esa20240910_models.CheckSiteNameRequest,
    ) -> esa20240910_models.CheckSiteNameResponse:
        """
        @summary 校验站点名称是否可用
        
        @param request: CheckSiteNameRequest
        @return: CheckSiteNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_site_name_with_options_async(request, runtime)

    def check_site_project_name_with_options(
        self,
        request: esa20240910_models.CheckSiteProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckSiteProjectNameResponse:
        """
        @summary 实时日志任务投递名检查
        
        @param request: CheckSiteProjectNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSiteProjectNameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSiteProjectName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckSiteProjectNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_site_project_name_with_options_async(
        self,
        request: esa20240910_models.CheckSiteProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckSiteProjectNameResponse:
        """
        @summary 实时日志任务投递名检查
        
        @param request: CheckSiteProjectNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckSiteProjectNameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSiteProjectName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckSiteProjectNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_site_project_name(
        self,
        request: esa20240910_models.CheckSiteProjectNameRequest,
    ) -> esa20240910_models.CheckSiteProjectNameResponse:
        """
        @summary 实时日志任务投递名检查
        
        @param request: CheckSiteProjectNameRequest
        @return: CheckSiteProjectNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_site_project_name_with_options(request, runtime)

    async def check_site_project_name_async(
        self,
        request: esa20240910_models.CheckSiteProjectNameRequest,
    ) -> esa20240910_models.CheckSiteProjectNameResponse:
        """
        @summary 实时日志任务投递名检查
        
        @param request: CheckSiteProjectNameRequest
        @return: CheckSiteProjectNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_site_project_name_with_options_async(request, runtime)

    def check_user_project_name_with_options(
        self,
        request: esa20240910_models.CheckUserProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckUserProjectNameResponse:
        """
        @summary 实时日志用户任务投递名检查
        
        @param request: CheckUserProjectNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUserProjectNameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserProjectName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckUserProjectNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_project_name_with_options_async(
        self,
        request: esa20240910_models.CheckUserProjectNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CheckUserProjectNameResponse:
        """
        @summary 实时日志用户任务投递名检查
        
        @param request: CheckUserProjectNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckUserProjectNameResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUserProjectName',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CheckUserProjectNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_project_name(
        self,
        request: esa20240910_models.CheckUserProjectNameRequest,
    ) -> esa20240910_models.CheckUserProjectNameResponse:
        """
        @summary 实时日志用户任务投递名检查
        
        @param request: CheckUserProjectNameRequest
        @return: CheckUserProjectNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_user_project_name_with_options(request, runtime)

    async def check_user_project_name_async(
        self,
        request: esa20240910_models.CheckUserProjectNameRequest,
    ) -> esa20240910_models.CheckUserProjectNameResponse:
        """
        @summary 实时日志用户任务投递名检查
        
        @param request: CheckUserProjectNameRequest
        @return: CheckUserProjectNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_user_project_name_with_options_async(request, runtime)

    def commit_routine_staging_code_with_options(
        self,
        request: esa20240910_models.CommitRoutineStagingCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CommitRoutineStagingCodeResponse:
        """
        @summary 提交Routine测试版本代码
        
        @param request: CommitRoutineStagingCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitRoutineStagingCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitRoutineStagingCode',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CommitRoutineStagingCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_routine_staging_code_with_options_async(
        self,
        request: esa20240910_models.CommitRoutineStagingCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CommitRoutineStagingCodeResponse:
        """
        @summary 提交Routine测试版本代码
        
        @param request: CommitRoutineStagingCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CommitRoutineStagingCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CommitRoutineStagingCode',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CommitRoutineStagingCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def commit_routine_staging_code(
        self,
        request: esa20240910_models.CommitRoutineStagingCodeRequest,
    ) -> esa20240910_models.CommitRoutineStagingCodeResponse:
        """
        @summary 提交Routine测试版本代码
        
        @param request: CommitRoutineStagingCodeRequest
        @return: CommitRoutineStagingCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.commit_routine_staging_code_with_options(request, runtime)

    async def commit_routine_staging_code_async(
        self,
        request: esa20240910_models.CommitRoutineStagingCodeRequest,
    ) -> esa20240910_models.CommitRoutineStagingCodeResponse:
        """
        @summary 提交Routine测试版本代码
        
        @param request: CommitRoutineStagingCodeRequest
        @return: CommitRoutineStagingCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.commit_routine_staging_code_with_options_async(request, runtime)

    def create_custom_scene_policy_with_options(
        self,
        request: esa20240910_models.CreateCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateCustomScenePolicyResponse:
        """
        @summary 创建定制场景策略
        
        @param request: CreateCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateCustomScenePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_scene_policy_with_options_async(
        self,
        request: esa20240910_models.CreateCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateCustomScenePolicyResponse:
        """
        @summary 创建定制场景策略
        
        @param request: CreateCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateCustomScenePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_scene_policy(
        self,
        request: esa20240910_models.CreateCustomScenePolicyRequest,
    ) -> esa20240910_models.CreateCustomScenePolicyResponse:
        """
        @summary 创建定制场景策略
        
        @param request: CreateCustomScenePolicyRequest
        @return: CreateCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_custom_scene_policy_with_options(request, runtime)

    async def create_custom_scene_policy_async(
        self,
        request: esa20240910_models.CreateCustomScenePolicyRequest,
    ) -> esa20240910_models.CreateCustomScenePolicyResponse:
        """
        @summary 创建定制场景策略
        
        @param request: CreateCustomScenePolicyRequest
        @return: CreateCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_scene_policy_with_options_async(request, runtime)

    def create_edge_container_app_with_options(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppResponse:
        """
        @summary 创建边缘容器的应用
        
        @param request: CreateEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.health_check_fail_times):
            body['HealthCheckFailTimes'] = request.health_check_fail_times
        if not UtilClient.is_unset(request.health_check_host):
            body['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_code):
            body['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            body['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            body['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_port):
            body['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.health_check_succ_times):
            body['HealthCheckSuccTimes'] = request.health_check_succ_times
        if not UtilClient.is_unset(request.health_check_timeout):
            body['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_type):
            body['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            body['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.service_port):
            body['ServicePort'] = request.service_port
        if not UtilClient.is_unset(request.target_port):
            body['TargetPort'] = request.target_port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edge_container_app_with_options_async(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppResponse:
        """
        @summary 创建边缘容器的应用
        
        @param request: CreateEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.health_check_fail_times):
            body['HealthCheckFailTimes'] = request.health_check_fail_times
        if not UtilClient.is_unset(request.health_check_host):
            body['HealthCheckHost'] = request.health_check_host
        if not UtilClient.is_unset(request.health_check_http_code):
            body['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            body['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            body['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_port):
            body['HealthCheckPort'] = request.health_check_port
        if not UtilClient.is_unset(request.health_check_succ_times):
            body['HealthCheckSuccTimes'] = request.health_check_succ_times
        if not UtilClient.is_unset(request.health_check_timeout):
            body['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_type):
            body['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            body['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.service_port):
            body['ServicePort'] = request.service_port
        if not UtilClient.is_unset(request.target_port):
            body['TargetPort'] = request.target_port
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edge_container_app(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppResponse:
        """
        @summary 创建边缘容器的应用
        
        @param request: CreateEdgeContainerAppRequest
        @return: CreateEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_edge_container_app_with_options(request, runtime)

    async def create_edge_container_app_async(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppResponse:
        """
        @summary 创建边缘容器的应用
        
        @param request: CreateEdgeContainerAppRequest
        @return: CreateEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_container_app_with_options_async(request, runtime)

    def create_edge_container_app_record_with_options(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppRecordResponse:
        """
        @summary 创建一个边缘容器应用的域名记录
        
        @param request: CreateEdgeContainerAppRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerAppRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edge_container_app_record_with_options_async(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppRecordResponse:
        """
        @summary 创建一个边缘容器应用的域名记录
        
        @param request: CreateEdgeContainerAppRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerAppRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edge_container_app_record(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRecordRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppRecordResponse:
        """
        @summary 创建一个边缘容器应用的域名记录
        
        @param request: CreateEdgeContainerAppRecordRequest
        @return: CreateEdgeContainerAppRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_edge_container_app_record_with_options(request, runtime)

    async def create_edge_container_app_record_async(
        self,
        request: esa20240910_models.CreateEdgeContainerAppRecordRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppRecordResponse:
        """
        @summary 创建一个边缘容器应用的域名记录
        
        @param request: CreateEdgeContainerAppRecordRequest
        @return: CreateEdgeContainerAppRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_container_app_record_with_options_async(request, runtime)

    def create_edge_container_app_version_with_options(
        self,
        tmp_req: esa20240910_models.CreateEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppVersionResponse:
        """
        @summary 创建边缘容器应用的版本
        
        @param tmp_req: CreateEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateEdgeContainerAppVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.containers):
            request.containers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.containers, 'Containers', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.containers_shrink):
            body['Containers'] = request.containers_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_edge_container_app_version_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateEdgeContainerAppVersionResponse:
        """
        @summary 创建边缘容器应用的版本
        
        @param tmp_req: CreateEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateEdgeContainerAppVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.containers):
            request.containers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.containers, 'Containers', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.containers_shrink):
            body['Containers'] = request.containers_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateEdgeContainerAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_edge_container_app_version(
        self,
        request: esa20240910_models.CreateEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppVersionResponse:
        """
        @summary 创建边缘容器应用的版本
        
        @param request: CreateEdgeContainerAppVersionRequest
        @return: CreateEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_edge_container_app_version_with_options(request, runtime)

    async def create_edge_container_app_version_async(
        self,
        request: esa20240910_models.CreateEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.CreateEdgeContainerAppVersionResponse:
        """
        @summary 创建边缘容器应用的版本
        
        @param request: CreateEdgeContainerAppVersionRequest
        @return: CreateEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_edge_container_app_version_with_options_async(request, runtime)

    def create_kv_namespace_with_options(
        self,
        request: esa20240910_models.CreateKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateKvNamespaceResponse:
        """
        @summary 添加Namespace
        
        @param request: CreateKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kv_namespace_with_options_async(
        self,
        request: esa20240910_models.CreateKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateKvNamespaceResponse:
        """
        @summary 添加Namespace
        
        @param request: CreateKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kv_namespace(
        self,
        request: esa20240910_models.CreateKvNamespaceRequest,
    ) -> esa20240910_models.CreateKvNamespaceResponse:
        """
        @summary 添加Namespace
        
        @param request: CreateKvNamespaceRequest
        @return: CreateKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_kv_namespace_with_options(request, runtime)

    async def create_kv_namespace_async(
        self,
        request: esa20240910_models.CreateKvNamespaceRequest,
    ) -> esa20240910_models.CreateKvNamespaceResponse:
        """
        @summary 添加Namespace
        
        @param request: CreateKvNamespaceRequest
        @return: CreateKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_kv_namespace_with_options_async(request, runtime)

    def create_list_with_options(
        self,
        tmp_req: esa20240910_models.CreateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateListResponse:
        """
        @summary 创建自定义列表
        
        @param tmp_req: CreateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.items):
            request.items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.items_shrink):
            body['Items'] = request.items_shrink
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_list_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateListResponse:
        """
        @summary 创建自定义列表
        
        @param tmp_req: CreateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.items):
            request.items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.items_shrink):
            body['Items'] = request.items_shrink
        if not UtilClient.is_unset(request.kind):
            body['Kind'] = request.kind
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_list(
        self,
        request: esa20240910_models.CreateListRequest,
    ) -> esa20240910_models.CreateListResponse:
        """
        @summary 创建自定义列表
        
        @param request: CreateListRequest
        @return: CreateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_list_with_options(request, runtime)

    async def create_list_async(
        self,
        request: esa20240910_models.CreateListRequest,
    ) -> esa20240910_models.CreateListResponse:
        """
        @summary 创建自定义列表
        
        @param request: CreateListRequest
        @return: CreateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_list_with_options_async(request, runtime)

    def create_page_with_options(
        self,
        request: esa20240910_models.CreatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreatePageResponse:
        """
        @summary 调用CreatePage创建自定义响应页面
        
        @param request: CreatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreatePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_page_with_options_async(
        self,
        request: esa20240910_models.CreatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreatePageResponse:
        """
        @summary 调用CreatePage创建自定义响应页面
        
        @param request: CreatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreatePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_page(
        self,
        request: esa20240910_models.CreatePageRequest,
    ) -> esa20240910_models.CreatePageResponse:
        """
        @summary 调用CreatePage创建自定义响应页面
        
        @param request: CreatePageRequest
        @return: CreatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_page_with_options(request, runtime)

    async def create_page_async(
        self,
        request: esa20240910_models.CreatePageRequest,
    ) -> esa20240910_models.CreatePageResponse:
        """
        @summary 调用CreatePage创建自定义响应页面
        
        @param request: CreatePageRequest
        @return: CreatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_page_with_options_async(request, runtime)

    def create_record_with_options(
        self,
        tmp_req: esa20240910_models.CreateRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRecordResponse:
        """
        @summary 创建记录
        
        @param tmp_req: CreateRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_conf):
            request.auth_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_conf, 'AuthConf', 'json')
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_conf_shrink):
            query['AuthConf'] = request.auth_conf_shrink
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.host_policy):
            query['HostPolicy'] = request.host_policy
        if not UtilClient.is_unset(request.proxied):
            query['Proxied'] = request.proxied
        if not UtilClient.is_unset(request.record_name):
            query['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_record_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRecordResponse:
        """
        @summary 创建记录
        
        @param tmp_req: CreateRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_conf):
            request.auth_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_conf, 'AuthConf', 'json')
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_conf_shrink):
            query['AuthConf'] = request.auth_conf_shrink
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.host_policy):
            query['HostPolicy'] = request.host_policy
        if not UtilClient.is_unset(request.proxied):
            query['Proxied'] = request.proxied
        if not UtilClient.is_unset(request.record_name):
            query['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_record(
        self,
        request: esa20240910_models.CreateRecordRequest,
    ) -> esa20240910_models.CreateRecordResponse:
        """
        @summary 创建记录
        
        @param request: CreateRecordRequest
        @return: CreateRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_record_with_options(request, runtime)

    async def create_record_async(
        self,
        request: esa20240910_models.CreateRecordRequest,
    ) -> esa20240910_models.CreateRecordResponse:
        """
        @summary 创建记录
        
        @param request: CreateRecordRequest
        @return: CreateRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_record_with_options_async(request, runtime)

    def create_routine_with_options(
        self,
        request: esa20240910_models.CreateRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineResponse:
        """
        @summary 创建routine
        
        @param request: CreateRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_routine_with_options_async(
        self,
        request: esa20240910_models.CreateRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineResponse:
        """
        @summary 创建routine
        
        @param request: CreateRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.spec_name):
            body['SpecName'] = request.spec_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_routine(
        self,
        request: esa20240910_models.CreateRoutineRequest,
    ) -> esa20240910_models.CreateRoutineResponse:
        """
        @summary 创建routine
        
        @param request: CreateRoutineRequest
        @return: CreateRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_routine_with_options(request, runtime)

    async def create_routine_async(
        self,
        request: esa20240910_models.CreateRoutineRequest,
    ) -> esa20240910_models.CreateRoutineResponse:
        """
        @summary 创建routine
        
        @param request: CreateRoutineRequest
        @return: CreateRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_routine_with_options_async(request, runtime)

    def create_routine_related_record_with_options(
        self,
        request: esa20240910_models.CreateRoutineRelatedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineRelatedRecordResponse:
        """
        @summary 添加Routine关联域名
        
        @param request: CreateRoutineRelatedRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineRelatedRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutineRelatedRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineRelatedRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_routine_related_record_with_options_async(
        self,
        request: esa20240910_models.CreateRoutineRelatedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineRelatedRecordResponse:
        """
        @summary 添加Routine关联域名
        
        @param request: CreateRoutineRelatedRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineRelatedRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutineRelatedRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineRelatedRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_routine_related_record(
        self,
        request: esa20240910_models.CreateRoutineRelatedRecordRequest,
    ) -> esa20240910_models.CreateRoutineRelatedRecordResponse:
        """
        @summary 添加Routine关联域名
        
        @param request: CreateRoutineRelatedRecordRequest
        @return: CreateRoutineRelatedRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_routine_related_record_with_options(request, runtime)

    async def create_routine_related_record_async(
        self,
        request: esa20240910_models.CreateRoutineRelatedRecordRequest,
    ) -> esa20240910_models.CreateRoutineRelatedRecordResponse:
        """
        @summary 添加Routine关联域名
        
        @param request: CreateRoutineRelatedRecordRequest
        @return: CreateRoutineRelatedRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_routine_related_record_with_options_async(request, runtime)

    def create_routine_related_route_with_options(
        self,
        request: esa20240910_models.CreateRoutineRelatedRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineRelatedRouteResponse:
        """
        @summary 添加Routine关联路由
        
        @param request: CreateRoutineRelatedRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineRelatedRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.route):
            body['Route'] = request.route
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutineRelatedRoute',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineRelatedRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_routine_related_route_with_options_async(
        self,
        request: esa20240910_models.CreateRoutineRelatedRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateRoutineRelatedRouteResponse:
        """
        @summary 添加Routine关联路由
        
        @param request: CreateRoutineRelatedRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRoutineRelatedRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.route):
            body['Route'] = request.route
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRoutineRelatedRoute',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateRoutineRelatedRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_routine_related_route(
        self,
        request: esa20240910_models.CreateRoutineRelatedRouteRequest,
    ) -> esa20240910_models.CreateRoutineRelatedRouteResponse:
        """
        @summary 添加Routine关联路由
        
        @param request: CreateRoutineRelatedRouteRequest
        @return: CreateRoutineRelatedRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_routine_related_route_with_options(request, runtime)

    async def create_routine_related_route_async(
        self,
        request: esa20240910_models.CreateRoutineRelatedRouteRequest,
    ) -> esa20240910_models.CreateRoutineRelatedRouteResponse:
        """
        @summary 添加Routine关联路由
        
        @param request: CreateRoutineRelatedRouteRequest
        @return: CreateRoutineRelatedRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_routine_related_route_with_options_async(request, runtime)

    def create_scheduled_preload_executions_with_options(
        self,
        tmp_req: esa20240910_models.CreateScheduledPreloadExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateScheduledPreloadExecutionsResponse:
        """
        @summary 批量新增定时预热任务的计划
        
        @param tmp_req: CreateScheduledPreloadExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPreloadExecutionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateScheduledPreloadExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.executions):
            request.executions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executions, 'Executions', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.executions_shrink):
            body['Executions'] = request.executions_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPreloadExecutions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateScheduledPreloadExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_preload_executions_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateScheduledPreloadExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateScheduledPreloadExecutionsResponse:
        """
        @summary 批量新增定时预热任务的计划
        
        @param tmp_req: CreateScheduledPreloadExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPreloadExecutionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateScheduledPreloadExecutionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.executions):
            request.executions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.executions, 'Executions', 'json')
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.executions_shrink):
            body['Executions'] = request.executions_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPreloadExecutions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateScheduledPreloadExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_preload_executions(
        self,
        request: esa20240910_models.CreateScheduledPreloadExecutionsRequest,
    ) -> esa20240910_models.CreateScheduledPreloadExecutionsResponse:
        """
        @summary 批量新增定时预热任务的计划
        
        @param request: CreateScheduledPreloadExecutionsRequest
        @return: CreateScheduledPreloadExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_preload_executions_with_options(request, runtime)

    async def create_scheduled_preload_executions_async(
        self,
        request: esa20240910_models.CreateScheduledPreloadExecutionsRequest,
    ) -> esa20240910_models.CreateScheduledPreloadExecutionsResponse:
        """
        @summary 批量新增定时预热任务的计划
        
        @param request: CreateScheduledPreloadExecutionsRequest
        @return: CreateScheduledPreloadExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_preload_executions_with_options_async(request, runtime)

    def create_scheduled_preload_job_with_options(
        self,
        request: esa20240910_models.CreateScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponse:
        """
        @summary 新增定时预热任务
        
        @param request: CreateScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.insert_way):
            body['InsertWay'] = request.insert_way
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.url_list):
            body['UrlList'] = request.url_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateScheduledPreloadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheduled_preload_job_with_options_async(
        self,
        request: esa20240910_models.CreateScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponse:
        """
        @summary 新增定时预热任务
        
        @param request: CreateScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.insert_way):
            body['InsertWay'] = request.insert_way
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.url_list):
            body['UrlList'] = request.url_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateScheduledPreloadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheduled_preload_job(
        self,
        request: esa20240910_models.CreateScheduledPreloadJobRequest,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponse:
        """
        @summary 新增定时预热任务
        
        @param request: CreateScheduledPreloadJobRequest
        @return: CreateScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheduled_preload_job_with_options(request, runtime)

    async def create_scheduled_preload_job_async(
        self,
        request: esa20240910_models.CreateScheduledPreloadJobRequest,
    ) -> esa20240910_models.CreateScheduledPreloadJobResponse:
        """
        @summary 新增定时预热任务
        
        @param request: CreateScheduledPreloadJobRequest
        @return: CreateScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheduled_preload_job_with_options_async(request, runtime)

    def create_site_with_options(
        self,
        request: esa20240910_models.CreateSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteResponse:
        """
        @summary 创建站点
        
        @param request: CreateSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site_name):
            query['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_site_with_options_async(
        self,
        request: esa20240910_models.CreateSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteResponse:
        """
        @summary 创建站点
        
        @param request: CreateSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.site_name):
            query['SiteName'] = request.site_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_site(
        self,
        request: esa20240910_models.CreateSiteRequest,
    ) -> esa20240910_models.CreateSiteResponse:
        """
        @summary 创建站点
        
        @param request: CreateSiteRequest
        @return: CreateSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_site_with_options(request, runtime)

    async def create_site_async(
        self,
        request: esa20240910_models.CreateSiteRequest,
    ) -> esa20240910_models.CreateSiteResponse:
        """
        @summary 创建站点
        
        @param request: CreateSiteRequest
        @return: CreateSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_site_with_options_async(request, runtime)

    def create_site_custom_log_with_options(
        self,
        tmp_req: esa20240910_models.CreateSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteCustomLogResponse:
        """
        @summary 新建自定义字段
        
        @param tmp_req: CreateSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteCustomLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateSiteCustomLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cookies):
            request.cookies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cookies, 'Cookies', 'json')
        if not UtilClient.is_unset(tmp_req.request_headers):
            request.request_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_headers, 'RequestHeaders', 'json')
        if not UtilClient.is_unset(tmp_req.response_headers):
            request.response_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.response_headers, 'ResponseHeaders', 'json')
        body = {}
        if not UtilClient.is_unset(request.cookies_shrink):
            body['Cookies'] = request.cookies_shrink
        if not UtilClient.is_unset(request.request_headers_shrink):
            body['RequestHeaders'] = request.request_headers_shrink
        if not UtilClient.is_unset(request.response_headers_shrink):
            body['ResponseHeaders'] = request.response_headers_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteCustomLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_site_custom_log_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteCustomLogResponse:
        """
        @summary 新建自定义字段
        
        @param tmp_req: CreateSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteCustomLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateSiteCustomLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cookies):
            request.cookies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cookies, 'Cookies', 'json')
        if not UtilClient.is_unset(tmp_req.request_headers):
            request.request_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_headers, 'RequestHeaders', 'json')
        if not UtilClient.is_unset(tmp_req.response_headers):
            request.response_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.response_headers, 'ResponseHeaders', 'json')
        body = {}
        if not UtilClient.is_unset(request.cookies_shrink):
            body['Cookies'] = request.cookies_shrink
        if not UtilClient.is_unset(request.request_headers_shrink):
            body['RequestHeaders'] = request.request_headers_shrink
        if not UtilClient.is_unset(request.response_headers_shrink):
            body['ResponseHeaders'] = request.response_headers_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteCustomLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_site_custom_log(
        self,
        request: esa20240910_models.CreateSiteCustomLogRequest,
    ) -> esa20240910_models.CreateSiteCustomLogResponse:
        """
        @summary 新建自定义字段
        
        @param request: CreateSiteCustomLogRequest
        @return: CreateSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_site_custom_log_with_options(request, runtime)

    async def create_site_custom_log_async(
        self,
        request: esa20240910_models.CreateSiteCustomLogRequest,
    ) -> esa20240910_models.CreateSiteCustomLogResponse:
        """
        @summary 新建自定义字段
        
        @param request: CreateSiteCustomLogRequest
        @return: CreateSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_site_custom_log_with_options_async(request, runtime)

    def create_site_delivery_task_with_options(
        self,
        tmp_req: esa20240910_models.CreateSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteDeliveryTaskResponse:
        """
        @summary 新建一个任务投递
        
        @param tmp_req: CreateSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateSiteDeliveryTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_delivery):
            request.http_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_delivery, 'HttpDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.kafka_delivery):
            request.kafka_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kafka_delivery, 'KafkaDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.oss_delivery):
            request.oss_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.oss_delivery, 'OssDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.s_3delivery):
            request.s_3delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.s_3delivery, 'S3Delivery', 'json')
        if not UtilClient.is_unset(tmp_req.sls_delivery):
            request.sls_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sls_delivery, 'SlsDelivery', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.http_delivery_shrink):
            body['HttpDelivery'] = request.http_delivery_shrink
        if not UtilClient.is_unset(request.kafka_delivery_shrink):
            body['KafkaDelivery'] = request.kafka_delivery_shrink
        if not UtilClient.is_unset(request.oss_delivery_shrink):
            body['OssDelivery'] = request.oss_delivery_shrink
        if not UtilClient.is_unset(request.s_3delivery_shrink):
            body['S3Delivery'] = request.s_3delivery_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.sls_delivery_shrink):
            body['SlsDelivery'] = request.sls_delivery_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_site_delivery_task_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateSiteDeliveryTaskResponse:
        """
        @summary 新建一个任务投递
        
        @param tmp_req: CreateSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateSiteDeliveryTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_delivery):
            request.http_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_delivery, 'HttpDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.kafka_delivery):
            request.kafka_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kafka_delivery, 'KafkaDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.oss_delivery):
            request.oss_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.oss_delivery, 'OssDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.s_3delivery):
            request.s_3delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.s_3delivery, 'S3Delivery', 'json')
        if not UtilClient.is_unset(tmp_req.sls_delivery):
            request.sls_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sls_delivery, 'SlsDelivery', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.http_delivery_shrink):
            body['HttpDelivery'] = request.http_delivery_shrink
        if not UtilClient.is_unset(request.kafka_delivery_shrink):
            body['KafkaDelivery'] = request.kafka_delivery_shrink
        if not UtilClient.is_unset(request.oss_delivery_shrink):
            body['OssDelivery'] = request.oss_delivery_shrink
        if not UtilClient.is_unset(request.s_3delivery_shrink):
            body['S3Delivery'] = request.s_3delivery_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.sls_delivery_shrink):
            body['SlsDelivery'] = request.sls_delivery_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateSiteDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_site_delivery_task(
        self,
        request: esa20240910_models.CreateSiteDeliveryTaskRequest,
    ) -> esa20240910_models.CreateSiteDeliveryTaskResponse:
        """
        @summary 新建一个任务投递
        
        @param request: CreateSiteDeliveryTaskRequest
        @return: CreateSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_site_delivery_task_with_options(request, runtime)

    async def create_site_delivery_task_async(
        self,
        request: esa20240910_models.CreateSiteDeliveryTaskRequest,
    ) -> esa20240910_models.CreateSiteDeliveryTaskResponse:
        """
        @summary 新建一个任务投递
        
        @param request: CreateSiteDeliveryTaskRequest
        @return: CreateSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_site_delivery_task_with_options_async(request, runtime)

    def create_user_delivery_task_with_options(
        self,
        tmp_req: esa20240910_models.CreateUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateUserDeliveryTaskResponse:
        """
        @summary 新建一个用户粒度任务投递
        
        @param tmp_req: CreateUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserDeliveryTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateUserDeliveryTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_delivery):
            request.http_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_delivery, 'HttpDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.kafka_delivery):
            request.kafka_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kafka_delivery, 'KafkaDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.oss_delivery):
            request.oss_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.oss_delivery, 'OssDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.s_3delivery):
            request.s_3delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.s_3delivery, 'S3Delivery', 'json')
        if not UtilClient.is_unset(tmp_req.sls_delivery):
            request.sls_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sls_delivery, 'SlsDelivery', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.http_delivery_shrink):
            body['HttpDelivery'] = request.http_delivery_shrink
        if not UtilClient.is_unset(request.kafka_delivery_shrink):
            body['KafkaDelivery'] = request.kafka_delivery_shrink
        if not UtilClient.is_unset(request.oss_delivery_shrink):
            body['OssDelivery'] = request.oss_delivery_shrink
        if not UtilClient.is_unset(request.s_3delivery_shrink):
            body['S3Delivery'] = request.s_3delivery_shrink
        if not UtilClient.is_unset(request.sls_delivery_shrink):
            body['SlsDelivery'] = request.sls_delivery_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateUserDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_delivery_task_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateUserDeliveryTaskResponse:
        """
        @summary 新建一个用户粒度任务投递
        
        @param tmp_req: CreateUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateUserDeliveryTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateUserDeliveryTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.http_delivery):
            request.http_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_delivery, 'HttpDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.kafka_delivery):
            request.kafka_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kafka_delivery, 'KafkaDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.oss_delivery):
            request.oss_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.oss_delivery, 'OssDelivery', 'json')
        if not UtilClient.is_unset(tmp_req.s_3delivery):
            request.s_3delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.s_3delivery, 'S3Delivery', 'json')
        if not UtilClient.is_unset(tmp_req.sls_delivery):
            request.sls_delivery_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sls_delivery, 'SlsDelivery', 'json')
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.data_center):
            body['DataCenter'] = request.data_center
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.http_delivery_shrink):
            body['HttpDelivery'] = request.http_delivery_shrink
        if not UtilClient.is_unset(request.kafka_delivery_shrink):
            body['KafkaDelivery'] = request.kafka_delivery_shrink
        if not UtilClient.is_unset(request.oss_delivery_shrink):
            body['OssDelivery'] = request.oss_delivery_shrink
        if not UtilClient.is_unset(request.s_3delivery_shrink):
            body['S3Delivery'] = request.s_3delivery_shrink
        if not UtilClient.is_unset(request.sls_delivery_shrink):
            body['SlsDelivery'] = request.sls_delivery_shrink
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateUserDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user_delivery_task(
        self,
        request: esa20240910_models.CreateUserDeliveryTaskRequest,
    ) -> esa20240910_models.CreateUserDeliveryTaskResponse:
        """
        @summary 新建一个用户粒度任务投递
        
        @param request: CreateUserDeliveryTaskRequest
        @return: CreateUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_user_delivery_task_with_options(request, runtime)

    async def create_user_delivery_task_async(
        self,
        request: esa20240910_models.CreateUserDeliveryTaskRequest,
    ) -> esa20240910_models.CreateUserDeliveryTaskResponse:
        """
        @summary 新建一个用户粒度任务投递
        
        @param request: CreateUserDeliveryTaskRequest
        @return: CreateUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_user_delivery_task_with_options_async(request, runtime)

    def create_waf_rule_with_options(
        self,
        tmp_req: esa20240910_models.CreateWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWafRuleResponse:
        """
        @summary 创建WAF规则
        
        @param tmp_req: CreateWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWafRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateWafRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waf_rule_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWafRuleResponse:
        """
        @summary 创建WAF规则
        
        @param tmp_req: CreateWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWafRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateWafRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.phase):
            body['Phase'] = request.phase
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waf_rule(
        self,
        request: esa20240910_models.CreateWafRuleRequest,
    ) -> esa20240910_models.CreateWafRuleResponse:
        """
        @summary 创建WAF规则
        
        @param request: CreateWafRuleRequest
        @return: CreateWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_waf_rule_with_options(request, runtime)

    async def create_waf_rule_async(
        self,
        request: esa20240910_models.CreateWafRuleRequest,
    ) -> esa20240910_models.CreateWafRuleResponse:
        """
        @summary 创建WAF规则
        
        @param request: CreateWafRuleRequest
        @return: CreateWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_waf_rule_with_options_async(request, runtime)

    def create_waiting_room_with_options(
        self,
        tmp_req: esa20240910_models.CreateWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomResponse:
        """
        @summary 创建等候室
        
        @param tmp_req: CreateWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateWaitingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.host_name_and_path):
            request.host_name_and_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name_and_path, 'HostNameAndPath', 'json')
        query = {}
        if not UtilClient.is_unset(request.cookie_name):
            query['CookieName'] = request.cookie_name
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.host_name_and_path_shrink):
            query['HostNameAndPath'] = request.host_name_and_path_shrink
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.queue_all_enable):
            query['QueueAllEnable'] = request.queue_all_enable
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waiting_room_with_options_async(
        self,
        tmp_req: esa20240910_models.CreateWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomResponse:
        """
        @summary 创建等候室
        
        @param tmp_req: CreateWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.CreateWaitingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.host_name_and_path):
            request.host_name_and_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name_and_path, 'HostNameAndPath', 'json')
        query = {}
        if not UtilClient.is_unset(request.cookie_name):
            query['CookieName'] = request.cookie_name
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.host_name_and_path_shrink):
            query['HostNameAndPath'] = request.host_name_and_path_shrink
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.queue_all_enable):
            query['QueueAllEnable'] = request.queue_all_enable
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waiting_room(
        self,
        request: esa20240910_models.CreateWaitingRoomRequest,
    ) -> esa20240910_models.CreateWaitingRoomResponse:
        """
        @summary 创建等候室
        
        @param request: CreateWaitingRoomRequest
        @return: CreateWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_waiting_room_with_options(request, runtime)

    async def create_waiting_room_async(
        self,
        request: esa20240910_models.CreateWaitingRoomRequest,
    ) -> esa20240910_models.CreateWaitingRoomResponse:
        """
        @summary 创建等候室
        
        @param request: CreateWaitingRoomRequest
        @return: CreateWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_waiting_room_with_options_async(request, runtime)

    def create_waiting_room_event_with_options(
        self,
        request: esa20240910_models.CreateWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomEventResponse:
        """
        @summary 创建等候室事件
        
        @param request: CreateWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.pre_queue_enable):
            query['PreQueueEnable'] = request.pre_queue_enable
        if not UtilClient.is_unset(request.pre_queue_start_time):
            query['PreQueueStartTime'] = request.pre_queue_start_time
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.random_pre_queue_enable):
            query['RandomPreQueueEnable'] = request.random_pre_queue_enable
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waiting_room_event_with_options_async(
        self,
        request: esa20240910_models.CreateWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomEventResponse:
        """
        @summary 创建等候室事件
        
        @param request: CreateWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.pre_queue_enable):
            query['PreQueueEnable'] = request.pre_queue_enable
        if not UtilClient.is_unset(request.pre_queue_start_time):
            query['PreQueueStartTime'] = request.pre_queue_start_time
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.random_pre_queue_enable):
            query['RandomPreQueueEnable'] = request.random_pre_queue_enable
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waiting_room_event(
        self,
        request: esa20240910_models.CreateWaitingRoomEventRequest,
    ) -> esa20240910_models.CreateWaitingRoomEventResponse:
        """
        @summary 创建等候室事件
        
        @param request: CreateWaitingRoomEventRequest
        @return: CreateWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_waiting_room_event_with_options(request, runtime)

    async def create_waiting_room_event_async(
        self,
        request: esa20240910_models.CreateWaitingRoomEventRequest,
    ) -> esa20240910_models.CreateWaitingRoomEventResponse:
        """
        @summary 创建等候室事件
        
        @param request: CreateWaitingRoomEventRequest
        @return: CreateWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_waiting_room_event_with_options_async(request, runtime)

    def create_waiting_room_rule_with_options(
        self,
        request: esa20240910_models.CreateWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomRuleResponse:
        """
        @summary 创建等候室规则
        
        @param request: CreateWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_enable):
            query['RuleEnable'] = request.rule_enable
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_waiting_room_rule_with_options_async(
        self,
        request: esa20240910_models.CreateWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.CreateWaitingRoomRuleResponse:
        """
        @summary 创建等候室规则
        
        @param request: CreateWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_enable):
            query['RuleEnable'] = request.rule_enable
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.CreateWaitingRoomRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_waiting_room_rule(
        self,
        request: esa20240910_models.CreateWaitingRoomRuleRequest,
    ) -> esa20240910_models.CreateWaitingRoomRuleResponse:
        """
        @summary 创建等候室规则
        
        @param request: CreateWaitingRoomRuleRequest
        @return: CreateWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_waiting_room_rule_with_options(request, runtime)

    async def create_waiting_room_rule_async(
        self,
        request: esa20240910_models.CreateWaitingRoomRuleRequest,
    ) -> esa20240910_models.CreateWaitingRoomRuleResponse:
        """
        @summary 创建等候室规则
        
        @param request: CreateWaitingRoomRuleRequest
        @return: CreateWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_waiting_room_rule_with_options_async(request, runtime)

    def delete_custom_scene_policy_with_options(
        self,
        request: esa20240910_models.DeleteCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteCustomScenePolicyResponse:
        """
        @summary 删除定制场景策略
        
        @param request: DeleteCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteCustomScenePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_scene_policy_with_options_async(
        self,
        request: esa20240910_models.DeleteCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteCustomScenePolicyResponse:
        """
        @summary 删除定制场景策略
        
        @param request: DeleteCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteCustomScenePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_scene_policy(
        self,
        request: esa20240910_models.DeleteCustomScenePolicyRequest,
    ) -> esa20240910_models.DeleteCustomScenePolicyResponse:
        """
        @summary 删除定制场景策略
        
        @param request: DeleteCustomScenePolicyRequest
        @return: DeleteCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_scene_policy_with_options(request, runtime)

    async def delete_custom_scene_policy_async(
        self,
        request: esa20240910_models.DeleteCustomScenePolicyRequest,
    ) -> esa20240910_models.DeleteCustomScenePolicyResponse:
        """
        @summary 删除定制场景策略
        
        @param request: DeleteCustomScenePolicyRequest
        @return: DeleteCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_scene_policy_with_options_async(request, runtime)

    def delete_edge_container_app_with_options(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppResponse:
        """
        @summary 删除边缘容器的应用
        
        @param request: DeleteEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_edge_container_app_with_options_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppResponse:
        """
        @summary 删除边缘容器的应用
        
        @param request: DeleteEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_edge_container_app(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppResponse:
        """
        @summary 删除边缘容器的应用
        
        @param request: DeleteEdgeContainerAppRequest
        @return: DeleteEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_container_app_with_options(request, runtime)

    async def delete_edge_container_app_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppResponse:
        """
        @summary 删除边缘容器的应用
        
        @param request: DeleteEdgeContainerAppRequest
        @return: DeleteEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_container_app_with_options_async(request, runtime)

    def delete_edge_container_app_record_with_options(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppRecordResponse:
        """
        @summary 删除一个边缘容器应用的域名记录
        
        @param request: DeleteEdgeContainerAppRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerAppRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_edge_container_app_record_with_options_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppRecordResponse:
        """
        @summary 删除一个边缘容器应用的域名记录
        
        @param request: DeleteEdgeContainerAppRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppRecordResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerAppRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_edge_container_app_record(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRecordRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppRecordResponse:
        """
        @summary 删除一个边缘容器应用的域名记录
        
        @param request: DeleteEdgeContainerAppRecordRequest
        @return: DeleteEdgeContainerAppRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_container_app_record_with_options(request, runtime)

    async def delete_edge_container_app_record_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppRecordRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppRecordResponse:
        """
        @summary 删除一个边缘容器应用的域名记录
        
        @param request: DeleteEdgeContainerAppRecordRequest
        @return: DeleteEdgeContainerAppRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_container_app_record_with_options_async(request, runtime)

    def delete_edge_container_app_version_with_options(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppVersionResponse:
        """
        @summary 删除边缘容器应用的版本
        
        @param request: DeleteEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_edge_container_app_version_with_options_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteEdgeContainerAppVersionResponse:
        """
        @summary 删除边缘容器应用的版本
        
        @param request: DeleteEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteEdgeContainerAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_edge_container_app_version(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppVersionResponse:
        """
        @summary 删除边缘容器应用的版本
        
        @param request: DeleteEdgeContainerAppVersionRequest
        @return: DeleteEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_container_app_version_with_options(request, runtime)

    async def delete_edge_container_app_version_async(
        self,
        request: esa20240910_models.DeleteEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.DeleteEdgeContainerAppVersionResponse:
        """
        @summary 删除边缘容器应用的版本
        
        @param request: DeleteEdgeContainerAppVersionRequest
        @return: DeleteEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_edge_container_app_version_with_options_async(request, runtime)

    def delete_kv_with_options(
        self,
        request: esa20240910_models.DeleteKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteKvResponse:
        """
        @summary 删除Namespace的Key-Value对
        
        @param request: DeleteKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKvResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kv_with_options_async(
        self,
        request: esa20240910_models.DeleteKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteKvResponse:
        """
        @summary 删除Namespace的Key-Value对
        
        @param request: DeleteKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKvResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kv(
        self,
        request: esa20240910_models.DeleteKvRequest,
    ) -> esa20240910_models.DeleteKvResponse:
        """
        @summary 删除Namespace的Key-Value对
        
        @param request: DeleteKvRequest
        @return: DeleteKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_kv_with_options(request, runtime)

    async def delete_kv_async(
        self,
        request: esa20240910_models.DeleteKvRequest,
    ) -> esa20240910_models.DeleteKvResponse:
        """
        @summary 删除Namespace的Key-Value对
        
        @param request: DeleteKvRequest
        @return: DeleteKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_kv_with_options_async(request, runtime)

    def delete_kv_namespace_with_options(
        self,
        request: esa20240910_models.DeleteKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteKvNamespaceResponse:
        """
        @summary 删除Namespace
        
        @param request: DeleteKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kv_namespace_with_options_async(
        self,
        request: esa20240910_models.DeleteKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteKvNamespaceResponse:
        """
        @summary 删除Namespace
        
        @param request: DeleteKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kv_namespace(
        self,
        request: esa20240910_models.DeleteKvNamespaceRequest,
    ) -> esa20240910_models.DeleteKvNamespaceResponse:
        """
        @summary 删除Namespace
        
        @param request: DeleteKvNamespaceRequest
        @return: DeleteKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_kv_namespace_with_options(request, runtime)

    async def delete_kv_namespace_async(
        self,
        request: esa20240910_models.DeleteKvNamespaceRequest,
    ) -> esa20240910_models.DeleteKvNamespaceResponse:
        """
        @summary 删除Namespace
        
        @param request: DeleteKvNamespaceRequest
        @return: DeleteKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_kv_namespace_with_options_async(request, runtime)

    def delete_list_with_options(
        self,
        request: esa20240910_models.DeleteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteListResponse:
        """
        @summary 删除自定义列表
        
        @param request: DeleteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_list_with_options_async(
        self,
        request: esa20240910_models.DeleteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteListResponse:
        """
        @summary 删除自定义列表
        
        @param request: DeleteListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteListResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_list(
        self,
        request: esa20240910_models.DeleteListRequest,
    ) -> esa20240910_models.DeleteListResponse:
        """
        @summary 删除自定义列表
        
        @param request: DeleteListRequest
        @return: DeleteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_list_with_options(request, runtime)

    async def delete_list_async(
        self,
        request: esa20240910_models.DeleteListRequest,
    ) -> esa20240910_models.DeleteListResponse:
        """
        @summary 删除自定义列表
        
        @param request: DeleteListRequest
        @return: DeleteListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_list_with_options_async(request, runtime)

    def delete_page_with_options(
        self,
        request: esa20240910_models.DeletePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeletePageResponse:
        """
        @summary 删除自定义响应页面
        
        @param request: DeletePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeletePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_page_with_options_async(
        self,
        request: esa20240910_models.DeletePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeletePageResponse:
        """
        @summary 删除自定义响应页面
        
        @param request: DeletePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeletePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_page(
        self,
        request: esa20240910_models.DeletePageRequest,
    ) -> esa20240910_models.DeletePageResponse:
        """
        @summary 删除自定义响应页面
        
        @param request: DeletePageRequest
        @return: DeletePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_page_with_options(request, runtime)

    async def delete_page_async(
        self,
        request: esa20240910_models.DeletePageRequest,
    ) -> esa20240910_models.DeletePageResponse:
        """
        @summary 删除自定义响应页面
        
        @param request: DeletePageRequest
        @return: DeletePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_page_with_options_async(request, runtime)

    def delete_record_with_options(
        self,
        request: esa20240910_models.DeleteRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRecordResponse:
        """
        @summary 删除记录
        
        @param request: DeleteRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_record_with_options_async(
        self,
        request: esa20240910_models.DeleteRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRecordResponse:
        """
        @summary 删除记录
        
        @param request: DeleteRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_record(
        self,
        request: esa20240910_models.DeleteRecordRequest,
    ) -> esa20240910_models.DeleteRecordResponse:
        """
        @summary 删除记录
        
        @param request: DeleteRecordRequest
        @return: DeleteRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_record_with_options(request, runtime)

    async def delete_record_async(
        self,
        request: esa20240910_models.DeleteRecordRequest,
    ) -> esa20240910_models.DeleteRecordResponse:
        """
        @summary 删除记录
        
        @param request: DeleteRecordRequest
        @return: DeleteRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_record_with_options_async(request, runtime)

    def delete_routine_with_options(
        self,
        request: esa20240910_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineResponse:
        """
        @summary 删除Routine
        
        @param request: DeleteRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_with_options_async(
        self,
        request: esa20240910_models.DeleteRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineResponse:
        """
        @summary 删除Routine
        
        @param request: DeleteRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine(
        self,
        request: esa20240910_models.DeleteRoutineRequest,
    ) -> esa20240910_models.DeleteRoutineResponse:
        """
        @summary 删除Routine
        
        @param request: DeleteRoutineRequest
        @return: DeleteRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_with_options(request, runtime)

    async def delete_routine_async(
        self,
        request: esa20240910_models.DeleteRoutineRequest,
    ) -> esa20240910_models.DeleteRoutineResponse:
        """
        @summary 删除Routine
        
        @param request: DeleteRoutineRequest
        @return: DeleteRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_with_options_async(request, runtime)

    def delete_routine_code_version_with_options(
        self,
        request: esa20240910_models.DeleteRoutineCodeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineCodeVersionResponse:
        """
        @summary 删除Routine某版本代码
        
        @param request: DeleteRoutineCodeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineCodeVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineCodeVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineCodeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_code_version_with_options_async(
        self,
        request: esa20240910_models.DeleteRoutineCodeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineCodeVersionResponse:
        """
        @summary 删除Routine某版本代码
        
        @param request: DeleteRoutineCodeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineCodeVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineCodeVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineCodeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_code_version(
        self,
        request: esa20240910_models.DeleteRoutineCodeVersionRequest,
    ) -> esa20240910_models.DeleteRoutineCodeVersionResponse:
        """
        @summary 删除Routine某版本代码
        
        @param request: DeleteRoutineCodeVersionRequest
        @return: DeleteRoutineCodeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_code_version_with_options(request, runtime)

    async def delete_routine_code_version_async(
        self,
        request: esa20240910_models.DeleteRoutineCodeVersionRequest,
    ) -> esa20240910_models.DeleteRoutineCodeVersionResponse:
        """
        @summary 删除Routine某版本代码
        
        @param request: DeleteRoutineCodeVersionRequest
        @return: DeleteRoutineCodeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_code_version_with_options_async(request, runtime)

    def delete_routine_related_record_with_options(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineRelatedRecordResponse:
        """
        @summary 删除Routine关联域名
        
        @param request: DeleteRoutineRelatedRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineRelatedRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_id):
            body['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineRelatedRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineRelatedRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_related_record_with_options_async(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineRelatedRecordResponse:
        """
        @summary 删除Routine关联域名
        
        @param request: DeleteRoutineRelatedRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineRelatedRecordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_id):
            body['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.record_name):
            body['RecordName'] = request.record_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineRelatedRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineRelatedRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_related_record(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRecordRequest,
    ) -> esa20240910_models.DeleteRoutineRelatedRecordResponse:
        """
        @summary 删除Routine关联域名
        
        @param request: DeleteRoutineRelatedRecordRequest
        @return: DeleteRoutineRelatedRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_related_record_with_options(request, runtime)

    async def delete_routine_related_record_async(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRecordRequest,
    ) -> esa20240910_models.DeleteRoutineRelatedRecordResponse:
        """
        @summary 删除Routine关联域名
        
        @param request: DeleteRoutineRelatedRecordRequest
        @return: DeleteRoutineRelatedRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_related_record_with_options_async(request, runtime)

    def delete_routine_related_route_with_options(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineRelatedRouteResponse:
        """
        @summary 删除Routine关联路由
        
        @param request: DeleteRoutineRelatedRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineRelatedRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.route):
            body['Route'] = request.route
        if not UtilClient.is_unset(request.route_id):
            body['RouteId'] = request.route_id
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineRelatedRoute',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineRelatedRouteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_routine_related_route_with_options_async(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRouteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteRoutineRelatedRouteResponse:
        """
        @summary 删除Routine关联路由
        
        @param request: DeleteRoutineRelatedRouteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRoutineRelatedRouteResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.route):
            body['Route'] = request.route
        if not UtilClient.is_unset(request.route_id):
            body['RouteId'] = request.route_id
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRoutineRelatedRoute',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteRoutineRelatedRouteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_routine_related_route(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRouteRequest,
    ) -> esa20240910_models.DeleteRoutineRelatedRouteResponse:
        """
        @summary 删除Routine关联路由
        
        @param request: DeleteRoutineRelatedRouteRequest
        @return: DeleteRoutineRelatedRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_routine_related_route_with_options(request, runtime)

    async def delete_routine_related_route_async(
        self,
        request: esa20240910_models.DeleteRoutineRelatedRouteRequest,
    ) -> esa20240910_models.DeleteRoutineRelatedRouteResponse:
        """
        @summary 删除Routine关联路由
        
        @param request: DeleteRoutineRelatedRouteRequest
        @return: DeleteRoutineRelatedRouteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_routine_related_route_with_options_async(request, runtime)

    def delete_scheduled_preload_execution_with_options(
        self,
        request: esa20240910_models.DeleteScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteScheduledPreloadExecutionResponse:
        """
        @summary 删除单个定时预热计划
        
        @param request: DeleteScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteScheduledPreloadExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_preload_execution_with_options_async(
        self,
        request: esa20240910_models.DeleteScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteScheduledPreloadExecutionResponse:
        """
        @summary 删除单个定时预热计划
        
        @param request: DeleteScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteScheduledPreloadExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_preload_execution(
        self,
        request: esa20240910_models.DeleteScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.DeleteScheduledPreloadExecutionResponse:
        """
        @summary 删除单个定时预热计划
        
        @param request: DeleteScheduledPreloadExecutionRequest
        @return: DeleteScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_preload_execution_with_options(request, runtime)

    async def delete_scheduled_preload_execution_async(
        self,
        request: esa20240910_models.DeleteScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.DeleteScheduledPreloadExecutionResponse:
        """
        @summary 删除单个定时预热计划
        
        @param request: DeleteScheduledPreloadExecutionRequest
        @return: DeleteScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_preload_execution_with_options_async(request, runtime)

    def delete_scheduled_preload_job_with_options(
        self,
        request: esa20240910_models.DeleteScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteScheduledPreloadJobResponse:
        """
        @summary 删除指定定时预热任务
        
        @param request: DeleteScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteScheduledPreloadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheduled_preload_job_with_options_async(
        self,
        request: esa20240910_models.DeleteScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteScheduledPreloadJobResponse:
        """
        @summary 删除指定定时预热任务
        
        @param request: DeleteScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteScheduledPreloadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheduled_preload_job(
        self,
        request: esa20240910_models.DeleteScheduledPreloadJobRequest,
    ) -> esa20240910_models.DeleteScheduledPreloadJobResponse:
        """
        @summary 删除指定定时预热任务
        
        @param request: DeleteScheduledPreloadJobRequest
        @return: DeleteScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheduled_preload_job_with_options(request, runtime)

    async def delete_scheduled_preload_job_async(
        self,
        request: esa20240910_models.DeleteScheduledPreloadJobRequest,
    ) -> esa20240910_models.DeleteScheduledPreloadJobResponse:
        """
        @summary 删除指定定时预热任务
        
        @param request: DeleteScheduledPreloadJobRequest
        @return: DeleteScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheduled_preload_job_with_options_async(request, runtime)

    def delete_site_with_options(
        self,
        request: esa20240910_models.DeleteSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteSiteResponse:
        """
        @summary 删除站点
        
        @param request: DeleteSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_site_with_options_async(
        self,
        request: esa20240910_models.DeleteSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteSiteResponse:
        """
        @summary 删除站点
        
        @param request: DeleteSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_site(
        self,
        request: esa20240910_models.DeleteSiteRequest,
    ) -> esa20240910_models.DeleteSiteResponse:
        """
        @summary 删除站点
        
        @param request: DeleteSiteRequest
        @return: DeleteSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_site_with_options(request, runtime)

    async def delete_site_async(
        self,
        request: esa20240910_models.DeleteSiteRequest,
    ) -> esa20240910_models.DeleteSiteResponse:
        """
        @summary 删除站点
        
        @param request: DeleteSiteRequest
        @return: DeleteSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_site_with_options_async(request, runtime)

    def delete_site_delivery_task_with_options(
        self,
        request: esa20240910_models.DeleteSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteSiteDeliveryTaskResponse:
        """
        @summary 删除一个任务投递
        
        @param request: DeleteSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteSiteDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_site_delivery_task_with_options_async(
        self,
        request: esa20240910_models.DeleteSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteSiteDeliveryTaskResponse:
        """
        @summary 删除一个任务投递
        
        @param request: DeleteSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteSiteDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_site_delivery_task(
        self,
        request: esa20240910_models.DeleteSiteDeliveryTaskRequest,
    ) -> esa20240910_models.DeleteSiteDeliveryTaskResponse:
        """
        @summary 删除一个任务投递
        
        @param request: DeleteSiteDeliveryTaskRequest
        @return: DeleteSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_site_delivery_task_with_options(request, runtime)

    async def delete_site_delivery_task_async(
        self,
        request: esa20240910_models.DeleteSiteDeliveryTaskRequest,
    ) -> esa20240910_models.DeleteSiteDeliveryTaskResponse:
        """
        @summary 删除一个任务投递
        
        @param request: DeleteSiteDeliveryTaskRequest
        @return: DeleteSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_site_delivery_task_with_options_async(request, runtime)

    def delete_user_delivery_task_with_options(
        self,
        request: esa20240910_models.DeleteUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteUserDeliveryTaskResponse:
        """
        @summary 删除一个用户任务投递
        
        @param request: DeleteUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteUserDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_delivery_task_with_options_async(
        self,
        request: esa20240910_models.DeleteUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteUserDeliveryTaskResponse:
        """
        @summary 删除一个用户任务投递
        
        @param request: DeleteUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteUserDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_delivery_task(
        self,
        request: esa20240910_models.DeleteUserDeliveryTaskRequest,
    ) -> esa20240910_models.DeleteUserDeliveryTaskResponse:
        """
        @summary 删除一个用户任务投递
        
        @param request: DeleteUserDeliveryTaskRequest
        @return: DeleteUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_delivery_task_with_options(request, runtime)

    async def delete_user_delivery_task_async(
        self,
        request: esa20240910_models.DeleteUserDeliveryTaskRequest,
    ) -> esa20240910_models.DeleteUserDeliveryTaskResponse:
        """
        @summary 删除一个用户任务投递
        
        @param request: DeleteUserDeliveryTaskRequest
        @return: DeleteUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_delivery_task_with_options_async(request, runtime)

    def delete_waf_rule_with_options(
        self,
        request: esa20240910_models.DeleteWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWafRuleResponse:
        """
        @summary 删除WAF规则
        
        @param request: DeleteWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waf_rule_with_options_async(
        self,
        request: esa20240910_models.DeleteWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWafRuleResponse:
        """
        @summary 删除WAF规则
        
        @param request: DeleteWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waf_rule(
        self,
        request: esa20240910_models.DeleteWafRuleRequest,
    ) -> esa20240910_models.DeleteWafRuleResponse:
        """
        @summary 删除WAF规则
        
        @param request: DeleteWafRuleRequest
        @return: DeleteWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waf_rule_with_options(request, runtime)

    async def delete_waf_rule_async(
        self,
        request: esa20240910_models.DeleteWafRuleRequest,
    ) -> esa20240910_models.DeleteWafRuleResponse:
        """
        @summary 删除WAF规则
        
        @param request: DeleteWafRuleRequest
        @return: DeleteWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waf_rule_with_options_async(request, runtime)

    def delete_waf_ruleset_with_options(
        self,
        request: esa20240910_models.DeleteWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWafRulesetResponse:
        """
        @summary 删除WAF规则集
        
        @param request: DeleteWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWafRulesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waf_ruleset_with_options_async(
        self,
        request: esa20240910_models.DeleteWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWafRulesetResponse:
        """
        @summary 删除WAF规则集
        
        @param request: DeleteWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWafRulesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waf_ruleset(
        self,
        request: esa20240910_models.DeleteWafRulesetRequest,
    ) -> esa20240910_models.DeleteWafRulesetResponse:
        """
        @summary 删除WAF规则集
        
        @param request: DeleteWafRulesetRequest
        @return: DeleteWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waf_ruleset_with_options(request, runtime)

    async def delete_waf_ruleset_async(
        self,
        request: esa20240910_models.DeleteWafRulesetRequest,
    ) -> esa20240910_models.DeleteWafRulesetResponse:
        """
        @summary 删除WAF规则集
        
        @param request: DeleteWafRulesetRequest
        @return: DeleteWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waf_ruleset_with_options_async(request, runtime)

    def delete_waiting_room_with_options(
        self,
        request: esa20240910_models.DeleteWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomResponse:
        """
        @summary 删除等候室
        
        @param request: DeleteWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waiting_room_with_options_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomResponse:
        """
        @summary 删除等候室
        
        @param request: DeleteWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waiting_room(
        self,
        request: esa20240910_models.DeleteWaitingRoomRequest,
    ) -> esa20240910_models.DeleteWaitingRoomResponse:
        """
        @summary 删除等候室
        
        @param request: DeleteWaitingRoomRequest
        @return: DeleteWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waiting_room_with_options(request, runtime)

    async def delete_waiting_room_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomRequest,
    ) -> esa20240910_models.DeleteWaitingRoomResponse:
        """
        @summary 删除等候室
        
        @param request: DeleteWaitingRoomRequest
        @return: DeleteWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waiting_room_with_options_async(request, runtime)

    def delete_waiting_room_event_with_options(
        self,
        request: esa20240910_models.DeleteWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomEventResponse:
        """
        @summary 删除等候室事件
        
        @param request: DeleteWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_event_id):
            query['WaitingRoomEventId'] = request.waiting_room_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waiting_room_event_with_options_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomEventResponse:
        """
        @summary 删除等候室事件
        
        @param request: DeleteWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_event_id):
            query['WaitingRoomEventId'] = request.waiting_room_event_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waiting_room_event(
        self,
        request: esa20240910_models.DeleteWaitingRoomEventRequest,
    ) -> esa20240910_models.DeleteWaitingRoomEventResponse:
        """
        @summary 删除等候室事件
        
        @param request: DeleteWaitingRoomEventRequest
        @return: DeleteWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waiting_room_event_with_options(request, runtime)

    async def delete_waiting_room_event_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomEventRequest,
    ) -> esa20240910_models.DeleteWaitingRoomEventResponse:
        """
        @summary 删除等候室事件
        
        @param request: DeleteWaitingRoomEventRequest
        @return: DeleteWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waiting_room_event_with_options_async(request, runtime)

    def delete_waiting_room_rule_with_options(
        self,
        request: esa20240910_models.DeleteWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomRuleResponse:
        """
        @summary 删除等候室规则
        
        @param request: DeleteWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_rule_id):
            query['WaitingRoomRuleId'] = request.waiting_room_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_waiting_room_rule_with_options_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DeleteWaitingRoomRuleResponse:
        """
        @summary 删除等候室规则
        
        @param request: DeleteWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_rule_id):
            query['WaitingRoomRuleId'] = request.waiting_room_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DeleteWaitingRoomRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_waiting_room_rule(
        self,
        request: esa20240910_models.DeleteWaitingRoomRuleRequest,
    ) -> esa20240910_models.DeleteWaitingRoomRuleResponse:
        """
        @summary 删除等候室规则
        
        @param request: DeleteWaitingRoomRuleRequest
        @return: DeleteWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_waiting_room_rule_with_options(request, runtime)

    async def delete_waiting_room_rule_async(
        self,
        request: esa20240910_models.DeleteWaitingRoomRuleRequest,
    ) -> esa20240910_models.DeleteWaitingRoomRuleResponse:
        """
        @summary 删除等候室规则
        
        @param request: DeleteWaitingRoomRuleRequest
        @return: DeleteWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_waiting_room_rule_with_options_async(request, runtime)

    def describe_custom_scene_policies_with_options(
        self,
        request: esa20240910_models.DescribeCustomScenePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeCustomScenePoliciesResponse:
        """
        @summary 查询定制场景策略配置
        
        @param request: DescribeCustomScenePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomScenePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomScenePolicies',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeCustomScenePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_scene_policies_with_options_async(
        self,
        request: esa20240910_models.DescribeCustomScenePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeCustomScenePoliciesResponse:
        """
        @summary 查询定制场景策略配置
        
        @param request: DescribeCustomScenePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCustomScenePoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCustomScenePolicies',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeCustomScenePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_scene_policies(
        self,
        request: esa20240910_models.DescribeCustomScenePoliciesRequest,
    ) -> esa20240910_models.DescribeCustomScenePoliciesResponse:
        """
        @summary 查询定制场景策略配置
        
        @param request: DescribeCustomScenePoliciesRequest
        @return: DescribeCustomScenePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_scene_policies_with_options(request, runtime)

    async def describe_custom_scene_policies_async(
        self,
        request: esa20240910_models.DescribeCustomScenePoliciesRequest,
    ) -> esa20240910_models.DescribeCustomScenePoliciesResponse:
        """
        @summary 查询定制场景策略配置
        
        @param request: DescribeCustomScenePoliciesRequest
        @return: DescribeCustomScenePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_scene_policies_with_options_async(request, runtime)

    def describe_ddo_sall_event_list_with_options(
        self,
        request: esa20240910_models.DescribeDDoSAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeDDoSAllEventListResponse:
        """
        @summary 攻击分析-查询攻击事件列表
        
        @param request: DescribeDDoSAllEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSAllEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSAllEventList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeDDoSAllEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ddo_sall_event_list_with_options_async(
        self,
        request: esa20240910_models.DescribeDDoSAllEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeDDoSAllEventListResponse:
        """
        @summary 攻击分析-查询攻击事件列表
        
        @param request: DescribeDDoSAllEventListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDDoSAllEventListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDDoSAllEventList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeDDoSAllEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ddo_sall_event_list(
        self,
        request: esa20240910_models.DescribeDDoSAllEventListRequest,
    ) -> esa20240910_models.DescribeDDoSAllEventListResponse:
        """
        @summary 攻击分析-查询攻击事件列表
        
        @param request: DescribeDDoSAllEventListRequest
        @return: DescribeDDoSAllEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_ddo_sall_event_list_with_options(request, runtime)

    async def describe_ddo_sall_event_list_async(
        self,
        request: esa20240910_models.DescribeDDoSAllEventListRequest,
    ) -> esa20240910_models.DescribeDDoSAllEventListResponse:
        """
        @summary 攻击分析-查询攻击事件列表
        
        @param request: DescribeDDoSAllEventListRequest
        @return: DescribeDDoSAllEventListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_ddo_sall_event_list_with_options_async(request, runtime)

    def describe_http_ddo_sattack_intelligent_protection_with_options(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 查询HTTP DDoS智能防护配置信息
        
        @param request: DescribeHttpDDoSAttackIntelligentProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHttpDDoSAttackIntelligentProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpDDoSAttackIntelligentProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_http_ddo_sattack_intelligent_protection_with_options_async(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 查询HTTP DDoS智能防护配置信息
        
        @param request: DescribeHttpDDoSAttackIntelligentProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHttpDDoSAttackIntelligentProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpDDoSAttackIntelligentProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_http_ddo_sattack_intelligent_protection(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionRequest,
    ) -> esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 查询HTTP DDoS智能防护配置信息
        
        @param request: DescribeHttpDDoSAttackIntelligentProtectionRequest
        @return: DescribeHttpDDoSAttackIntelligentProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_http_ddo_sattack_intelligent_protection_with_options(request, runtime)

    async def describe_http_ddo_sattack_intelligent_protection_async(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionRequest,
    ) -> esa20240910_models.DescribeHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 查询HTTP DDoS智能防护配置信息
        
        @param request: DescribeHttpDDoSAttackIntelligentProtectionRequest
        @return: DescribeHttpDDoSAttackIntelligentProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_http_ddo_sattack_intelligent_protection_with_options_async(request, runtime)

    def describe_http_ddo_sattack_protection_with_options(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeHttpDDoSAttackProtectionResponse:
        """
        @summary 查询HTTP DDoS攻击防护配置信息
        
        @param request: DescribeHttpDDoSAttackProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHttpDDoSAttackProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpDDoSAttackProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeHttpDDoSAttackProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_http_ddo_sattack_protection_with_options_async(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeHttpDDoSAttackProtectionResponse:
        """
        @summary 查询HTTP DDoS攻击防护配置信息
        
        @param request: DescribeHttpDDoSAttackProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHttpDDoSAttackProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHttpDDoSAttackProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeHttpDDoSAttackProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_http_ddo_sattack_protection(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackProtectionRequest,
    ) -> esa20240910_models.DescribeHttpDDoSAttackProtectionResponse:
        """
        @summary 查询HTTP DDoS攻击防护配置信息
        
        @param request: DescribeHttpDDoSAttackProtectionRequest
        @return: DescribeHttpDDoSAttackProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_http_ddo_sattack_protection_with_options(request, runtime)

    async def describe_http_ddo_sattack_protection_async(
        self,
        request: esa20240910_models.DescribeHttpDDoSAttackProtectionRequest,
    ) -> esa20240910_models.DescribeHttpDDoSAttackProtectionResponse:
        """
        @summary 查询HTTP DDoS攻击防护配置信息
        
        @param request: DescribeHttpDDoSAttackProtectionRequest
        @return: DescribeHttpDDoSAttackProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_http_ddo_sattack_protection_with_options_async(request, runtime)

    def describe_iprange_list_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeIPRangeListResponse:
        """
        @summary 查询加速服务节点IP段列表
        
        @param request: DescribeIPRangeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIPRangeListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeIPRangeList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeIPRangeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_iprange_list_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeIPRangeListResponse:
        """
        @summary 查询加速服务节点IP段列表
        
        @param request: DescribeIPRangeListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIPRangeListResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeIPRangeList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeIPRangeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_iprange_list(self) -> esa20240910_models.DescribeIPRangeListResponse:
        """
        @summary 查询加速服务节点IP段列表
        
        @return: DescribeIPRangeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_iprange_list_with_options(runtime)

    async def describe_iprange_list_async(self) -> esa20240910_models.DescribeIPRangeListResponse:
        """
        @summary 查询加速服务节点IP段列表
        
        @return: DescribeIPRangeListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_iprange_list_with_options_async(runtime)

    def describe_kv_account_status_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeKvAccountStatusResponse:
        """
        @summary 查询账户的KV状态信
        
        @param request: DescribeKvAccountStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKvAccountStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeKvAccountStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeKvAccountStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_kv_account_status_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribeKvAccountStatusResponse:
        """
        @summary 查询账户的KV状态信
        
        @param request: DescribeKvAccountStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeKvAccountStatusResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeKvAccountStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribeKvAccountStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_kv_account_status(self) -> esa20240910_models.DescribeKvAccountStatusResponse:
        """
        @summary 查询账户的KV状态信
        
        @return: DescribeKvAccountStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_kv_account_status_with_options(runtime)

    async def describe_kv_account_status_async(self) -> esa20240910_models.DescribeKvAccountStatusResponse:
        """
        @summary 查询账户的KV状态信
        
        @return: DescribeKvAccountStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_kv_account_status_with_options_async(runtime)

    def describe_preload_tasks_with_options(
        self,
        request: esa20240910_models.DescribePreloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribePreloadTasksResponse:
        """
        @summary 预热任务查询接口
        
        @param request: DescribePreloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreloadTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribePreloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_preload_tasks_with_options_async(
        self,
        request: esa20240910_models.DescribePreloadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribePreloadTasksResponse:
        """
        @summary 预热任务查询接口
        
        @param request: DescribePreloadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreloadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreloadTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribePreloadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_preload_tasks(
        self,
        request: esa20240910_models.DescribePreloadTasksRequest,
    ) -> esa20240910_models.DescribePreloadTasksResponse:
        """
        @summary 预热任务查询接口
        
        @param request: DescribePreloadTasksRequest
        @return: DescribePreloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_preload_tasks_with_options(request, runtime)

    async def describe_preload_tasks_async(
        self,
        request: esa20240910_models.DescribePreloadTasksRequest,
    ) -> esa20240910_models.DescribePreloadTasksResponse:
        """
        @summary 预热任务查询接口
        
        @param request: DescribePreloadTasksRequest
        @return: DescribePreloadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_preload_tasks_with_options_async(request, runtime)

    def describe_purge_tasks_with_options(
        self,
        request: esa20240910_models.DescribePurgeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribePurgeTasksResponse:
        """
        @summary 刷新任务查询接口
        
        @param request: DescribePurgeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurgeTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurgeTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribePurgeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_purge_tasks_with_options_async(
        self,
        request: esa20240910_models.DescribePurgeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DescribePurgeTasksResponse:
        """
        @summary 刷新任务查询接口
        
        @param request: DescribePurgeTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePurgeTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurgeTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DescribePurgeTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_purge_tasks(
        self,
        request: esa20240910_models.DescribePurgeTasksRequest,
    ) -> esa20240910_models.DescribePurgeTasksResponse:
        """
        @summary 刷新任务查询接口
        
        @param request: DescribePurgeTasksRequest
        @return: DescribePurgeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_purge_tasks_with_options(request, runtime)

    async def describe_purge_tasks_async(
        self,
        request: esa20240910_models.DescribePurgeTasksRequest,
    ) -> esa20240910_models.DescribePurgeTasksResponse:
        """
        @summary 刷新任务查询接口
        
        @param request: DescribePurgeTasksRequest
        @return: DescribePurgeTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_purge_tasks_with_options_async(request, runtime)

    def disable_custom_scene_policy_with_options(
        self,
        request: esa20240910_models.DisableCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DisableCustomScenePolicyResponse:
        """
        @summary 禁用定制场景策略
        
        @param request: DisableCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DisableCustomScenePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_custom_scene_policy_with_options_async(
        self,
        request: esa20240910_models.DisableCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.DisableCustomScenePolicyResponse:
        """
        @summary 禁用定制场景策略
        
        @param request: DisableCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.DisableCustomScenePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_custom_scene_policy(
        self,
        request: esa20240910_models.DisableCustomScenePolicyRequest,
    ) -> esa20240910_models.DisableCustomScenePolicyResponse:
        """
        @summary 禁用定制场景策略
        
        @param request: DisableCustomScenePolicyRequest
        @return: DisableCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_custom_scene_policy_with_options(request, runtime)

    async def disable_custom_scene_policy_async(
        self,
        request: esa20240910_models.DisableCustomScenePolicyRequest,
    ) -> esa20240910_models.DisableCustomScenePolicyResponse:
        """
        @summary 禁用定制场景策略
        
        @param request: DisableCustomScenePolicyRequest
        @return: DisableCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_custom_scene_policy_with_options_async(request, runtime)

    def edit_site_waf_settings_with_options(
        self,
        tmp_req: esa20240910_models.EditSiteWafSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.EditSiteWafSettingsResponse:
        """
        @summary 编辑站点WAF配置
        
        @param tmp_req: EditSiteWafSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditSiteWafSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.EditSiteWafSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.settings):
            request.settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditSiteWafSettings',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.EditSiteWafSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_site_waf_settings_with_options_async(
        self,
        tmp_req: esa20240910_models.EditSiteWafSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.EditSiteWafSettingsResponse:
        """
        @summary 编辑站点WAF配置
        
        @param tmp_req: EditSiteWafSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EditSiteWafSettingsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.EditSiteWafSettingsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.settings):
            request.settings_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.settings, 'Settings', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.settings_shrink):
            body['Settings'] = request.settings_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EditSiteWafSettings',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.EditSiteWafSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_site_waf_settings(
        self,
        request: esa20240910_models.EditSiteWafSettingsRequest,
    ) -> esa20240910_models.EditSiteWafSettingsResponse:
        """
        @summary 编辑站点WAF配置
        
        @param request: EditSiteWafSettingsRequest
        @return: EditSiteWafSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.edit_site_waf_settings_with_options(request, runtime)

    async def edit_site_waf_settings_async(
        self,
        request: esa20240910_models.EditSiteWafSettingsRequest,
    ) -> esa20240910_models.EditSiteWafSettingsResponse:
        """
        @summary 编辑站点WAF配置
        
        @param request: EditSiteWafSettingsRequest
        @return: EditSiteWafSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.edit_site_waf_settings_with_options_async(request, runtime)

    def enable_custom_scene_policy_with_options(
        self,
        request: esa20240910_models.EnableCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.EnableCustomScenePolicyResponse:
        """
        @summary 启动定制场景策略
        
        @param request: EnableCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.EnableCustomScenePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_custom_scene_policy_with_options_async(
        self,
        request: esa20240910_models.EnableCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.EnableCustomScenePolicyResponse:
        """
        @summary 启动定制场景策略
        
        @param request: EnableCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.EnableCustomScenePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_custom_scene_policy(
        self,
        request: esa20240910_models.EnableCustomScenePolicyRequest,
    ) -> esa20240910_models.EnableCustomScenePolicyResponse:
        """
        @summary 启动定制场景策略
        
        @param request: EnableCustomScenePolicyRequest
        @return: EnableCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_custom_scene_policy_with_options(request, runtime)

    async def enable_custom_scene_policy_async(
        self,
        request: esa20240910_models.EnableCustomScenePolicyRequest,
    ) -> esa20240910_models.EnableCustomScenePolicyResponse:
        """
        @summary 启动定制场景策略
        
        @param request: EnableCustomScenePolicyRequest
        @return: EnableCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_custom_scene_policy_with_options_async(request, runtime)

    def export_records_with_options(
        self,
        request: esa20240910_models.ExportRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ExportRecordsResponse:
        """
        @summary 导出记录
        
        @param request: ExportRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ExportRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_records_with_options_async(
        self,
        request: esa20240910_models.ExportRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ExportRecordsResponse:
        """
        @summary 导出记录
        
        @param request: ExportRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ExportRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_records(
        self,
        request: esa20240910_models.ExportRecordsRequest,
    ) -> esa20240910_models.ExportRecordsResponse:
        """
        @summary 导出记录
        
        @param request: ExportRecordsRequest
        @return: ExportRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_records_with_options(request, runtime)

    async def export_records_async(
        self,
        request: esa20240910_models.ExportRecordsRequest,
    ) -> esa20240910_models.ExportRecordsResponse:
        """
        @summary 导出记录
        
        @param request: ExportRecordsRequest
        @return: ExportRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_records_with_options_async(request, runtime)

    def get_cache_reserve_specification_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetCacheReserveSpecificationResponse:
        """
        @summary 查询缓存保持实例规格
        
        @param request: GetCacheReserveSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCacheReserveSpecificationResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCacheReserveSpecification',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetCacheReserveSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cache_reserve_specification_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetCacheReserveSpecificationResponse:
        """
        @summary 查询缓存保持实例规格
        
        @param request: GetCacheReserveSpecificationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCacheReserveSpecificationResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCacheReserveSpecification',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetCacheReserveSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cache_reserve_specification(self) -> esa20240910_models.GetCacheReserveSpecificationResponse:
        """
        @summary 查询缓存保持实例规格
        
        @return: GetCacheReserveSpecificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cache_reserve_specification_with_options(runtime)

    async def get_cache_reserve_specification_async(self) -> esa20240910_models.GetCacheReserveSpecificationResponse:
        """
        @summary 查询缓存保持实例规格
        
        @return: GetCacheReserveSpecificationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cache_reserve_specification_with_options_async(runtime)

    def get_edge_container_app_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppResponse:
        """
        @summary 获取边缘容器应用信息
        
        @param request: GetEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_app_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppResponse:
        """
        @summary 获取边缘容器应用信息
        
        @param request: GetEdgeContainerAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerApp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_app(
        self,
        request: esa20240910_models.GetEdgeContainerAppRequest,
    ) -> esa20240910_models.GetEdgeContainerAppResponse:
        """
        @summary 获取边缘容器应用信息
        
        @param request: GetEdgeContainerAppRequest
        @return: GetEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_app_with_options(request, runtime)

    async def get_edge_container_app_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppRequest,
    ) -> esa20240910_models.GetEdgeContainerAppResponse:
        """
        @summary 获取边缘容器应用信息
        
        @param request: GetEdgeContainerAppRequest
        @return: GetEdgeContainerAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_app_with_options_async(request, runtime)

    def get_edge_container_app_status_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppStatusResponse:
        """
        @summary 获取边缘容器应用的状态信息
        
        @param request: GetEdgeContainerAppStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_env):
            query['PublishEnv'] = request.publish_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerAppStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_app_status_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppStatusResponse:
        """
        @summary 获取边缘容器应用的状态信息
        
        @param request: GetEdgeContainerAppStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.publish_env):
            query['PublishEnv'] = request.publish_env
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerAppStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_app_status(
        self,
        request: esa20240910_models.GetEdgeContainerAppStatusRequest,
    ) -> esa20240910_models.GetEdgeContainerAppStatusResponse:
        """
        @summary 获取边缘容器应用的状态信息
        
        @param request: GetEdgeContainerAppStatusRequest
        @return: GetEdgeContainerAppStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_app_status_with_options(request, runtime)

    async def get_edge_container_app_status_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppStatusRequest,
    ) -> esa20240910_models.GetEdgeContainerAppStatusResponse:
        """
        @summary 获取边缘容器应用的状态信息
        
        @param request: GetEdgeContainerAppStatusRequest
        @return: GetEdgeContainerAppStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_app_status_with_options_async(request, runtime)

    def get_edge_container_app_version_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppVersionResponse:
        """
        @summary 获取边缘容器应用的某个版本信息
        
        @param request: GetEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_app_version_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerAppVersionResponse:
        """
        @summary 获取边缘容器应用的某个版本信息
        
        @param request: GetEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_app_version(
        self,
        request: esa20240910_models.GetEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.GetEdgeContainerAppVersionResponse:
        """
        @summary 获取边缘容器应用的某个版本信息
        
        @param request: GetEdgeContainerAppVersionRequest
        @return: GetEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_app_version_with_options(request, runtime)

    async def get_edge_container_app_version_async(
        self,
        request: esa20240910_models.GetEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.GetEdgeContainerAppVersionResponse:
        """
        @summary 获取边缘容器应用的某个版本信息
        
        @param request: GetEdgeContainerAppVersionRequest
        @return: GetEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_app_version_with_options_async(request, runtime)

    def get_edge_container_deploy_regions_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerDeployRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerDeployRegionsResponse:
        """
        @summary 获取边缘容器应用部署区域
        
        @param request: GetEdgeContainerDeployRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerDeployRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerDeployRegions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerDeployRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_deploy_regions_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerDeployRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerDeployRegionsResponse:
        """
        @summary 获取边缘容器应用部署区域
        
        @param request: GetEdgeContainerDeployRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerDeployRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerDeployRegions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerDeployRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_deploy_regions(
        self,
        request: esa20240910_models.GetEdgeContainerDeployRegionsRequest,
    ) -> esa20240910_models.GetEdgeContainerDeployRegionsResponse:
        """
        @summary 获取边缘容器应用部署区域
        
        @param request: GetEdgeContainerDeployRegionsRequest
        @return: GetEdgeContainerDeployRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_deploy_regions_with_options(request, runtime)

    async def get_edge_container_deploy_regions_async(
        self,
        request: esa20240910_models.GetEdgeContainerDeployRegionsRequest,
    ) -> esa20240910_models.GetEdgeContainerDeployRegionsResponse:
        """
        @summary 获取边缘容器应用部署区域
        
        @param request: GetEdgeContainerDeployRegionsRequest
        @return: GetEdgeContainerDeployRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_deploy_regions_with_options_async(request, runtime)

    def get_edge_container_logs_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerLogsResponse:
        """
        @summary 获取边缘容器日志信息
        
        @param request: GetEdgeContainerLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerLogs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_logs_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerLogsResponse:
        """
        @summary 获取边缘容器日志信息
        
        @param request: GetEdgeContainerLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerLogsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerLogs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_logs(
        self,
        request: esa20240910_models.GetEdgeContainerLogsRequest,
    ) -> esa20240910_models.GetEdgeContainerLogsResponse:
        """
        @summary 获取边缘容器日志信息
        
        @param request: GetEdgeContainerLogsRequest
        @return: GetEdgeContainerLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_logs_with_options(request, runtime)

    async def get_edge_container_logs_async(
        self,
        request: esa20240910_models.GetEdgeContainerLogsRequest,
    ) -> esa20240910_models.GetEdgeContainerLogsResponse:
        """
        @summary 获取边缘容器日志信息
        
        @param request: GetEdgeContainerLogsRequest
        @return: GetEdgeContainerLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_logs_with_options_async(request, runtime)

    def get_edge_container_staging_deploy_status_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerStagingDeployStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerStagingDeployStatusResponse:
        """
        @summary 获取应用测试环境部署状态
        
        @param request: GetEdgeContainerStagingDeployStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerStagingDeployStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerStagingDeployStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerStagingDeployStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_staging_deploy_status_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerStagingDeployStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerStagingDeployStatusResponse:
        """
        @summary 获取应用测试环境部署状态
        
        @param request: GetEdgeContainerStagingDeployStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerStagingDeployStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerStagingDeployStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerStagingDeployStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_staging_deploy_status(
        self,
        request: esa20240910_models.GetEdgeContainerStagingDeployStatusRequest,
    ) -> esa20240910_models.GetEdgeContainerStagingDeployStatusResponse:
        """
        @summary 获取应用测试环境部署状态
        
        @param request: GetEdgeContainerStagingDeployStatusRequest
        @return: GetEdgeContainerStagingDeployStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_staging_deploy_status_with_options(request, runtime)

    async def get_edge_container_staging_deploy_status_async(
        self,
        request: esa20240910_models.GetEdgeContainerStagingDeployStatusRequest,
    ) -> esa20240910_models.GetEdgeContainerStagingDeployStatusResponse:
        """
        @summary 获取应用测试环境部署状态
        
        @param request: GetEdgeContainerStagingDeployStatusRequest
        @return: GetEdgeContainerStagingDeployStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_staging_deploy_status_with_options_async(request, runtime)

    def get_edge_container_terminal_with_options(
        self,
        request: esa20240910_models.GetEdgeContainerTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerTerminalResponse:
        """
        @summary 获取边缘容器应用终端信息
        
        @param request: GetEdgeContainerTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerTerminal',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerTerminalResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_edge_container_terminal_with_options_async(
        self,
        request: esa20240910_models.GetEdgeContainerTerminalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetEdgeContainerTerminalResponse:
        """
        @summary 获取边缘容器应用终端信息
        
        @param request: GetEdgeContainerTerminalRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetEdgeContainerTerminalResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeContainerTerminal',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetEdgeContainerTerminalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_edge_container_terminal(
        self,
        request: esa20240910_models.GetEdgeContainerTerminalRequest,
    ) -> esa20240910_models.GetEdgeContainerTerminalResponse:
        """
        @summary 获取边缘容器应用终端信息
        
        @param request: GetEdgeContainerTerminalRequest
        @return: GetEdgeContainerTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_edge_container_terminal_with_options(request, runtime)

    async def get_edge_container_terminal_async(
        self,
        request: esa20240910_models.GetEdgeContainerTerminalRequest,
    ) -> esa20240910_models.GetEdgeContainerTerminalResponse:
        """
        @summary 获取边缘容器应用终端信息
        
        @param request: GetEdgeContainerTerminalRequest
        @return: GetEdgeContainerTerminalResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_edge_container_terminal_with_options_async(request, runtime)

    def get_er_service_with_options(
        self,
        request: esa20240910_models.GetErServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetErServiceResponse:
        """
        @summary GetErService
        
        @param request: GetErServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErService',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetErServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_er_service_with_options_async(
        self,
        request: esa20240910_models.GetErServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetErServiceResponse:
        """
        @summary GetErService
        
        @param request: GetErServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetErServiceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetErService',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetErServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_er_service(
        self,
        request: esa20240910_models.GetErServiceRequest,
    ) -> esa20240910_models.GetErServiceResponse:
        """
        @summary GetErService
        
        @param request: GetErServiceRequest
        @return: GetErServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_er_service_with_options(request, runtime)

    async def get_er_service_async(
        self,
        request: esa20240910_models.GetErServiceRequest,
    ) -> esa20240910_models.GetErServiceResponse:
        """
        @summary GetErService
        
        @param request: GetErServiceRequest
        @return: GetErServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_er_service_with_options_async(request, runtime)

    def get_kv_with_options(
        self,
        request: esa20240910_models.GetKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvResponse:
        """
        @summary 查询Key-Value对的某个Key值
        
        @param request: GetKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kv_with_options_async(
        self,
        request: esa20240910_models.GetKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvResponse:
        """
        @summary 查询Key-Value对的某个Key值
        
        @param request: GetKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kv(
        self,
        request: esa20240910_models.GetKvRequest,
    ) -> esa20240910_models.GetKvResponse:
        """
        @summary 查询Key-Value对的某个Key值
        
        @param request: GetKvRequest
        @return: GetKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_kv_with_options(request, runtime)

    async def get_kv_async(
        self,
        request: esa20240910_models.GetKvRequest,
    ) -> esa20240910_models.GetKvResponse:
        """
        @summary 查询Key-Value对的某个Key值
        
        @param request: GetKvRequest
        @return: GetKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_kv_with_options_async(request, runtime)

    def get_kv_account_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvAccountResponse:
        """
        @summary 列出账号下的NS
        
        @param request: GetKvAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvAccountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetKvAccount',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kv_account_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvAccountResponse:
        """
        @summary 列出账号下的NS
        
        @param request: GetKvAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvAccountResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetKvAccount',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kv_account(self) -> esa20240910_models.GetKvAccountResponse:
        """
        @summary 列出账号下的NS
        
        @return: GetKvAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_kv_account_with_options(runtime)

    async def get_kv_account_async(self) -> esa20240910_models.GetKvAccountResponse:
        """
        @summary 列出账号下的NS
        
        @return: GetKvAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_kv_account_with_options_async(runtime)

    def get_kv_namespace_with_options(
        self,
        request: esa20240910_models.GetKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvNamespaceResponse:
        """
        @summary 查询Namespace信息
        
        @param request: GetKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kv_namespace_with_options_async(
        self,
        request: esa20240910_models.GetKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetKvNamespaceResponse:
        """
        @summary 查询Namespace信息
        
        @param request: GetKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kv_namespace(
        self,
        request: esa20240910_models.GetKvNamespaceRequest,
    ) -> esa20240910_models.GetKvNamespaceResponse:
        """
        @summary 查询Namespace信息
        
        @param request: GetKvNamespaceRequest
        @return: GetKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_kv_namespace_with_options(request, runtime)

    async def get_kv_namespace_async(
        self,
        request: esa20240910_models.GetKvNamespaceRequest,
    ) -> esa20240910_models.GetKvNamespaceResponse:
        """
        @summary 查询Namespace信息
        
        @param request: GetKvNamespaceRequest
        @return: GetKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_kv_namespace_with_options_async(request, runtime)

    def get_list_with_options(
        self,
        request: esa20240910_models.GetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetListResponse:
        """
        @summary 获取单个自定义列表
        
        @param request: GetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_list_with_options_async(
        self,
        request: esa20240910_models.GetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetListResponse:
        """
        @summary 获取单个自定义列表
        
        @param request: GetListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_list(
        self,
        request: esa20240910_models.GetListRequest,
    ) -> esa20240910_models.GetListResponse:
        """
        @summary 获取单个自定义列表
        
        @param request: GetListRequest
        @return: GetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_list_with_options(request, runtime)

    async def get_list_async(
        self,
        request: esa20240910_models.GetListRequest,
    ) -> esa20240910_models.GetListResponse:
        """
        @summary 获取单个自定义列表
        
        @param request: GetListRequest
        @return: GetListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_list_with_options_async(request, runtime)

    def get_page_with_options(
        self,
        request: esa20240910_models.GetPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetPageResponse:
        """
        @summary 获取单个自定义响应页面详情
        
        @param request: GetPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_page_with_options_async(
        self,
        request: esa20240910_models.GetPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetPageResponse:
        """
        @summary 获取单个自定义响应页面详情
        
        @param request: GetPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_page(
        self,
        request: esa20240910_models.GetPageRequest,
    ) -> esa20240910_models.GetPageResponse:
        """
        @summary 获取单个自定义响应页面详情
        
        @param request: GetPageRequest
        @return: GetPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_page_with_options(request, runtime)

    async def get_page_async(
        self,
        request: esa20240910_models.GetPageRequest,
    ) -> esa20240910_models.GetPageResponse:
        """
        @summary 获取单个自定义响应页面详情
        
        @param request: GetPageRequest
        @return: GetPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_page_with_options_async(request, runtime)

    def get_purge_quota_with_options(
        self,
        request: esa20240910_models.GetPurgeQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetPurgeQuotaResponse:
        """
        @summary 获取刷新Quota
        
        @param request: GetPurgeQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurgeQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPurgeQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetPurgeQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_purge_quota_with_options_async(
        self,
        request: esa20240910_models.GetPurgeQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetPurgeQuotaResponse:
        """
        @summary 获取刷新Quota
        
        @param request: GetPurgeQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPurgeQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPurgeQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetPurgeQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_purge_quota(
        self,
        request: esa20240910_models.GetPurgeQuotaRequest,
    ) -> esa20240910_models.GetPurgeQuotaResponse:
        """
        @summary 获取刷新Quota
        
        @param request: GetPurgeQuotaRequest
        @return: GetPurgeQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_purge_quota_with_options(request, runtime)

    async def get_purge_quota_async(
        self,
        request: esa20240910_models.GetPurgeQuotaRequest,
    ) -> esa20240910_models.GetPurgeQuotaResponse:
        """
        @summary 获取刷新Quota
        
        @param request: GetPurgeQuotaRequest
        @return: GetPurgeQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_purge_quota_with_options_async(request, runtime)

    def get_realtime_delivery_field_with_options(
        self,
        request: esa20240910_models.GetRealtimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRealtimeDeliveryFieldResponse:
        """
        @summary ub日志字段列表接口
        
        @param request: GetRealtimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeDeliveryField',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRealtimeDeliveryFieldResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_realtime_delivery_field_with_options_async(
        self,
        request: esa20240910_models.GetRealtimeDeliveryFieldRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRealtimeDeliveryFieldResponse:
        """
        @summary ub日志字段列表接口
        
        @param request: GetRealtimeDeliveryFieldRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealtimeDeliveryFieldResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealtimeDeliveryField',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRealtimeDeliveryFieldResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_realtime_delivery_field(
        self,
        request: esa20240910_models.GetRealtimeDeliveryFieldRequest,
    ) -> esa20240910_models.GetRealtimeDeliveryFieldResponse:
        """
        @summary ub日志字段列表接口
        
        @param request: GetRealtimeDeliveryFieldRequest
        @return: GetRealtimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_realtime_delivery_field_with_options(request, runtime)

    async def get_realtime_delivery_field_async(
        self,
        request: esa20240910_models.GetRealtimeDeliveryFieldRequest,
    ) -> esa20240910_models.GetRealtimeDeliveryFieldResponse:
        """
        @summary ub日志字段列表接口
        
        @param request: GetRealtimeDeliveryFieldRequest
        @return: GetRealtimeDeliveryFieldResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_realtime_delivery_field_with_options_async(request, runtime)

    def get_record_with_options(
        self,
        request: esa20240910_models.GetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRecordResponse:
        """
        @summary 查询单个记录信息
        
        @param request: GetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_record_with_options_async(
        self,
        request: esa20240910_models.GetRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRecordResponse:
        """
        @summary 查询单个记录信息
        
        @param request: GetRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRecordResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_record(
        self,
        request: esa20240910_models.GetRecordRequest,
    ) -> esa20240910_models.GetRecordResponse:
        """
        @summary 查询单个记录信息
        
        @param request: GetRecordRequest
        @return: GetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_record_with_options(request, runtime)

    async def get_record_async(
        self,
        request: esa20240910_models.GetRecordRequest,
    ) -> esa20240910_models.GetRecordResponse:
        """
        @summary 查询单个记录信息
        
        @param request: GetRecordRequest
        @return: GetRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_record_with_options_async(request, runtime)

    def get_routine_with_options(
        self,
        request: esa20240910_models.GetRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineResponse:
        """
        @summary 查询Routine配置信息
        
        @param request: GetRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_routine_with_options_async(
        self,
        request: esa20240910_models.GetRoutineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineResponse:
        """
        @summary 查询Routine配置信息
        
        @param request: GetRoutineRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoutine',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_routine(
        self,
        request: esa20240910_models.GetRoutineRequest,
    ) -> esa20240910_models.GetRoutineResponse:
        """
        @summary 查询Routine配置信息
        
        @param request: GetRoutineRequest
        @return: GetRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_routine_with_options(request, runtime)

    async def get_routine_async(
        self,
        request: esa20240910_models.GetRoutineRequest,
    ) -> esa20240910_models.GetRoutineResponse:
        """
        @summary 查询Routine配置信息
        
        @param request: GetRoutineRequest
        @return: GetRoutineResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_routine_with_options_async(request, runtime)

    def get_routine_staging_code_upload_info_with_options(
        self,
        request: esa20240910_models.GetRoutineStagingCodeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineStagingCodeUploadInfoResponse:
        """
        @summary 上传Routine的测试版本代码, 返回上传代码到OSS的参数
        
        @param request: GetRoutineStagingCodeUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineStagingCodeUploadInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoutineStagingCodeUploadInfo',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineStagingCodeUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_routine_staging_code_upload_info_with_options_async(
        self,
        request: esa20240910_models.GetRoutineStagingCodeUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineStagingCodeUploadInfoResponse:
        """
        @summary 上传Routine的测试版本代码, 返回上传代码到OSS的参数
        
        @param request: GetRoutineStagingCodeUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineStagingCodeUploadInfoResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.code_description):
            body['CodeDescription'] = request.code_description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRoutineStagingCodeUploadInfo',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineStagingCodeUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_routine_staging_code_upload_info(
        self,
        request: esa20240910_models.GetRoutineStagingCodeUploadInfoRequest,
    ) -> esa20240910_models.GetRoutineStagingCodeUploadInfoResponse:
        """
        @summary 上传Routine的测试版本代码, 返回上传代码到OSS的参数
        
        @param request: GetRoutineStagingCodeUploadInfoRequest
        @return: GetRoutineStagingCodeUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_routine_staging_code_upload_info_with_options(request, runtime)

    async def get_routine_staging_code_upload_info_async(
        self,
        request: esa20240910_models.GetRoutineStagingCodeUploadInfoRequest,
    ) -> esa20240910_models.GetRoutineStagingCodeUploadInfoResponse:
        """
        @summary 上传Routine的测试版本代码, 返回上传代码到OSS的参数
        
        @param request: GetRoutineStagingCodeUploadInfoRequest
        @return: GetRoutineStagingCodeUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_routine_staging_code_upload_info_with_options_async(request, runtime)

    def get_routine_staging_env_ip_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineStagingEnvIpResponse:
        """
        @summary 查询边缘函数测试环境IP
        
        @param request: GetRoutineStagingEnvIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineStagingEnvIpResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRoutineStagingEnvIp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineStagingEnvIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_routine_staging_env_ip_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineStagingEnvIpResponse:
        """
        @summary 查询边缘函数测试环境IP
        
        @param request: GetRoutineStagingEnvIpRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineStagingEnvIpResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRoutineStagingEnvIp',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineStagingEnvIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_routine_staging_env_ip(self) -> esa20240910_models.GetRoutineStagingEnvIpResponse:
        """
        @summary 查询边缘函数测试环境IP
        
        @return: GetRoutineStagingEnvIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_routine_staging_env_ip_with_options(runtime)

    async def get_routine_staging_env_ip_async(self) -> esa20240910_models.GetRoutineStagingEnvIpResponse:
        """
        @summary 查询边缘函数测试环境IP
        
        @return: GetRoutineStagingEnvIpResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_routine_staging_env_ip_with_options_async(runtime)

    def get_routine_user_info_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineUserInfoResponse:
        """
        @summary 查询用户的Routine列表
        
        @param request: GetRoutineUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineUserInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRoutineUserInfo',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_routine_user_info_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetRoutineUserInfoResponse:
        """
        @summary 查询用户的Routine列表
        
        @param request: GetRoutineUserInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRoutineUserInfoResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetRoutineUserInfo',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetRoutineUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_routine_user_info(self) -> esa20240910_models.GetRoutineUserInfoResponse:
        """
        @summary 查询用户的Routine列表
        
        @return: GetRoutineUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_routine_user_info_with_options(runtime)

    async def get_routine_user_info_async(self) -> esa20240910_models.GetRoutineUserInfoResponse:
        """
        @summary 查询用户的Routine列表
        
        @return: GetRoutineUserInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_routine_user_info_with_options_async(runtime)

    def get_scheduled_preload_job_with_options(
        self,
        request: esa20240910_models.GetScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetScheduledPreloadJobResponse:
        """
        @summary 查询单个定时预热任务
        
        @param request: GetScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetScheduledPreloadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheduled_preload_job_with_options_async(
        self,
        request: esa20240910_models.GetScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetScheduledPreloadJobResponse:
        """
        @summary 查询单个定时预热任务
        
        @param request: GetScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetScheduledPreloadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheduled_preload_job(
        self,
        request: esa20240910_models.GetScheduledPreloadJobRequest,
    ) -> esa20240910_models.GetScheduledPreloadJobResponse:
        """
        @summary 查询单个定时预热任务
        
        @param request: GetScheduledPreloadJobRequest
        @return: GetScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_scheduled_preload_job_with_options(request, runtime)

    async def get_scheduled_preload_job_async(
        self,
        request: esa20240910_models.GetScheduledPreloadJobRequest,
    ) -> esa20240910_models.GetScheduledPreloadJobResponse:
        """
        @summary 查询单个定时预热任务
        
        @param request: GetScheduledPreloadJobRequest
        @return: GetScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_scheduled_preload_job_with_options_async(request, runtime)

    def get_site_with_options(
        self,
        request: esa20240910_models.GetSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteResponse:
        """
        @summary 查询单个站点信息
        
        @param request: GetSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_with_options_async(
        self,
        request: esa20240910_models.GetSiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteResponse:
        """
        @summary 查询单个站点信息
        
        @param request: GetSiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site(
        self,
        request: esa20240910_models.GetSiteRequest,
    ) -> esa20240910_models.GetSiteResponse:
        """
        @summary 查询单个站点信息
        
        @param request: GetSiteRequest
        @return: GetSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_with_options(request, runtime)

    async def get_site_async(
        self,
        request: esa20240910_models.GetSiteRequest,
    ) -> esa20240910_models.GetSiteResponse:
        """
        @summary 查询单个站点信息
        
        @param request: GetSiteRequest
        @return: GetSiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_with_options_async(request, runtime)

    def get_site_current_nswith_options(
        self,
        request: esa20240910_models.GetSiteCurrentNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteCurrentNSResponse:
        """
        @summary 查询当前NS列表
        
        @param request: GetSiteCurrentNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteCurrentNSResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteCurrentNS',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteCurrentNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_current_nswith_options_async(
        self,
        request: esa20240910_models.GetSiteCurrentNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteCurrentNSResponse:
        """
        @summary 查询当前NS列表
        
        @param request: GetSiteCurrentNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteCurrentNSResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteCurrentNS',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteCurrentNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site_current_ns(
        self,
        request: esa20240910_models.GetSiteCurrentNSRequest,
    ) -> esa20240910_models.GetSiteCurrentNSResponse:
        """
        @summary 查询当前NS列表
        
        @param request: GetSiteCurrentNSRequest
        @return: GetSiteCurrentNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_current_nswith_options(request, runtime)

    async def get_site_current_ns_async(
        self,
        request: esa20240910_models.GetSiteCurrentNSRequest,
    ) -> esa20240910_models.GetSiteCurrentNSResponse:
        """
        @summary 查询当前NS列表
        
        @param request: GetSiteCurrentNSRequest
        @return: GetSiteCurrentNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_current_nswith_options_async(request, runtime)

    def get_site_custom_log_with_options(
        self,
        request: esa20240910_models.GetSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteCustomLogResponse:
        """
        @summary 获取自定义字段
        
        @param request: GetSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteCustomLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteCustomLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_custom_log_with_options_async(
        self,
        request: esa20240910_models.GetSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteCustomLogResponse:
        """
        @summary 获取自定义字段
        
        @param request: GetSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteCustomLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteCustomLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site_custom_log(
        self,
        request: esa20240910_models.GetSiteCustomLogRequest,
    ) -> esa20240910_models.GetSiteCustomLogResponse:
        """
        @summary 获取自定义字段
        
        @param request: GetSiteCustomLogRequest
        @return: GetSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_custom_log_with_options(request, runtime)

    async def get_site_custom_log_async(
        self,
        request: esa20240910_models.GetSiteCustomLogRequest,
    ) -> esa20240910_models.GetSiteCustomLogResponse:
        """
        @summary 获取自定义字段
        
        @param request: GetSiteCustomLogRequest
        @return: GetSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_custom_log_with_options_async(request, runtime)

    def get_site_delivery_task_with_options(
        self,
        request: esa20240910_models.GetSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteDeliveryTaskResponse:
        """
        @summary 获取一个实时日志任务投递
        
        @param request: GetSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_delivery_task_with_options_async(
        self,
        request: esa20240910_models.GetSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteDeliveryTaskResponse:
        """
        @summary 获取一个实时日志任务投递
        
        @param request: GetSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site_delivery_task(
        self,
        request: esa20240910_models.GetSiteDeliveryTaskRequest,
    ) -> esa20240910_models.GetSiteDeliveryTaskResponse:
        """
        @summary 获取一个实时日志任务投递
        
        @param request: GetSiteDeliveryTaskRequest
        @return: GetSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_delivery_task_with_options(request, runtime)

    async def get_site_delivery_task_async(
        self,
        request: esa20240910_models.GetSiteDeliveryTaskRequest,
    ) -> esa20240910_models.GetSiteDeliveryTaskResponse:
        """
        @summary 获取一个实时日志任务投递
        
        @param request: GetSiteDeliveryTaskRequest
        @return: GetSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_delivery_task_with_options_async(request, runtime)

    def get_site_log_delivery_quota_with_options(
        self,
        request: esa20240910_models.GetSiteLogDeliveryQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务quota数
        
        @param request: GetSiteLogDeliveryQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteLogDeliveryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteLogDeliveryQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteLogDeliveryQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_log_delivery_quota_with_options_async(
        self,
        request: esa20240910_models.GetSiteLogDeliveryQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务quota数
        
        @param request: GetSiteLogDeliveryQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteLogDeliveryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteLogDeliveryQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteLogDeliveryQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site_log_delivery_quota(
        self,
        request: esa20240910_models.GetSiteLogDeliveryQuotaRequest,
    ) -> esa20240910_models.GetSiteLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务quota数
        
        @param request: GetSiteLogDeliveryQuotaRequest
        @return: GetSiteLogDeliveryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_log_delivery_quota_with_options(request, runtime)

    async def get_site_log_delivery_quota_async(
        self,
        request: esa20240910_models.GetSiteLogDeliveryQuotaRequest,
    ) -> esa20240910_models.GetSiteLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务quota数
        
        @param request: GetSiteLogDeliveryQuotaRequest
        @return: GetSiteLogDeliveryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_log_delivery_quota_with_options_async(request, runtime)

    def get_site_waf_settings_with_options(
        self,
        request: esa20240910_models.GetSiteWafSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteWafSettingsResponse:
        """
        @summary 获取站点WAF配置
        
        @param request: GetSiteWafSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteWafSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteWafSettings',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteWafSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_site_waf_settings_with_options_async(
        self,
        request: esa20240910_models.GetSiteWafSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetSiteWafSettingsResponse:
        """
        @summary 获取站点WAF配置
        
        @param request: GetSiteWafSettingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSiteWafSettingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSiteWafSettings',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetSiteWafSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_site_waf_settings(
        self,
        request: esa20240910_models.GetSiteWafSettingsRequest,
    ) -> esa20240910_models.GetSiteWafSettingsResponse:
        """
        @summary 获取站点WAF配置
        
        @param request: GetSiteWafSettingsRequest
        @return: GetSiteWafSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_site_waf_settings_with_options(request, runtime)

    async def get_site_waf_settings_async(
        self,
        request: esa20240910_models.GetSiteWafSettingsRequest,
    ) -> esa20240910_models.GetSiteWafSettingsResponse:
        """
        @summary 获取站点WAF配置
        
        @param request: GetSiteWafSettingsRequest
        @return: GetSiteWafSettingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_site_waf_settings_with_options_async(request, runtime)

    def get_upload_task_with_options(
        self,
        request: esa20240910_models.GetUploadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUploadTaskResponse:
        """
        @summary 文件上传任务查询接口
        
        @param request: GetUploadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUploadTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_task_with_options_async(
        self,
        request: esa20240910_models.GetUploadTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUploadTaskResponse:
        """
        @summary 文件上传任务查询接口
        
        @param request: GetUploadTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUploadTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_task(
        self,
        request: esa20240910_models.GetUploadTaskRequest,
    ) -> esa20240910_models.GetUploadTaskResponse:
        """
        @summary 文件上传任务查询接口
        
        @param request: GetUploadTaskRequest
        @return: GetUploadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_task_with_options(request, runtime)

    async def get_upload_task_async(
        self,
        request: esa20240910_models.GetUploadTaskRequest,
    ) -> esa20240910_models.GetUploadTaskResponse:
        """
        @summary 文件上传任务查询接口
        
        @param request: GetUploadTaskRequest
        @return: GetUploadTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_task_with_options_async(request, runtime)

    def get_user_delivery_task_with_options(
        self,
        request: esa20240910_models.GetUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUserDeliveryTaskResponse:
        """
        @summary 获取一个用户粒度任务投递
        
        @param request: GetUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUserDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_delivery_task_with_options_async(
        self,
        request: esa20240910_models.GetUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUserDeliveryTaskResponse:
        """
        @summary 获取一个用户粒度任务投递
        
        @param request: GetUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUserDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_delivery_task(
        self,
        request: esa20240910_models.GetUserDeliveryTaskRequest,
    ) -> esa20240910_models.GetUserDeliveryTaskResponse:
        """
        @summary 获取一个用户粒度任务投递
        
        @param request: GetUserDeliveryTaskRequest
        @return: GetUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_delivery_task_with_options(request, runtime)

    async def get_user_delivery_task_async(
        self,
        request: esa20240910_models.GetUserDeliveryTaskRequest,
    ) -> esa20240910_models.GetUserDeliveryTaskResponse:
        """
        @summary 获取一个用户粒度任务投递
        
        @param request: GetUserDeliveryTaskRequest
        @return: GetUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_delivery_task_with_options_async(request, runtime)

    def get_user_log_delivery_quota_with_options(
        self,
        request: esa20240910_models.GetUserLogDeliveryQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUserLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务用户quota数
        
        @param request: GetUserLogDeliveryQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserLogDeliveryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserLogDeliveryQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUserLogDeliveryQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_log_delivery_quota_with_options_async(
        self,
        request: esa20240910_models.GetUserLogDeliveryQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetUserLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务用户quota数
        
        @param request: GetUserLogDeliveryQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserLogDeliveryQuotaResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserLogDeliveryQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetUserLogDeliveryQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_log_delivery_quota(
        self,
        request: esa20240910_models.GetUserLogDeliveryQuotaRequest,
    ) -> esa20240910_models.GetUserLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务用户quota数
        
        @param request: GetUserLogDeliveryQuotaRequest
        @return: GetUserLogDeliveryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_log_delivery_quota_with_options(request, runtime)

    async def get_user_log_delivery_quota_async(
        self,
        request: esa20240910_models.GetUserLogDeliveryQuotaRequest,
    ) -> esa20240910_models.GetUserLogDeliveryQuotaResponse:
        """
        @summary 获取日志投递任务用户quota数
        
        @param request: GetUserLogDeliveryQuotaRequest
        @return: GetUserLogDeliveryQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_log_delivery_quota_with_options_async(request, runtime)

    def get_waf_bot_app_key_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafBotAppKeyResponse:
        """
        @param request: GetWafBotAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafBotAppKeyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetWafBotAppKey',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafBotAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_waf_bot_app_key_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafBotAppKeyResponse:
        """
        @param request: GetWafBotAppKeyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafBotAppKeyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetWafBotAppKey',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafBotAppKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_waf_bot_app_key(self) -> esa20240910_models.GetWafBotAppKeyResponse:
        """
        @return: GetWafBotAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_waf_bot_app_key_with_options(runtime)

    async def get_waf_bot_app_key_async(self) -> esa20240910_models.GetWafBotAppKeyResponse:
        """
        @return: GetWafBotAppKeyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_waf_bot_app_key_with_options_async(runtime)

    def get_waf_filter_with_options(
        self,
        request: esa20240910_models.GetWafFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafFilterResponse:
        """
        @summary 将匹配项转换为表达式
        
        @param request: GetWafFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafFilter',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_waf_filter_with_options_async(
        self,
        request: esa20240910_models.GetWafFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafFilterResponse:
        """
        @summary 将匹配项转换为表达式
        
        @param request: GetWafFilterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafFilterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafFilter',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_waf_filter(
        self,
        request: esa20240910_models.GetWafFilterRequest,
    ) -> esa20240910_models.GetWafFilterResponse:
        """
        @summary 将匹配项转换为表达式
        
        @param request: GetWafFilterRequest
        @return: GetWafFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_waf_filter_with_options(request, runtime)

    async def get_waf_filter_async(
        self,
        request: esa20240910_models.GetWafFilterRequest,
    ) -> esa20240910_models.GetWafFilterResponse:
        """
        @summary 将匹配项转换为表达式
        
        @param request: GetWafFilterRequest
        @return: GetWafFilterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_waf_filter_with_options_async(request, runtime)

    def get_waf_quota_with_options(
        self,
        request: esa20240910_models.GetWafQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafQuotaResponse:
        """
        @summary 获取WAF配额详情
        
        @param request: GetWafQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_waf_quota_with_options_async(
        self,
        request: esa20240910_models.GetWafQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafQuotaResponse:
        """
        @summary 获取WAF配额详情
        
        @param request: GetWafQuotaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafQuotaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.paths):
            query['Paths'] = request.paths
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafQuota',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_waf_quota(
        self,
        request: esa20240910_models.GetWafQuotaRequest,
    ) -> esa20240910_models.GetWafQuotaResponse:
        """
        @summary 获取WAF配额详情
        
        @param request: GetWafQuotaRequest
        @return: GetWafQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_waf_quota_with_options(request, runtime)

    async def get_waf_quota_async(
        self,
        request: esa20240910_models.GetWafQuotaRequest,
    ) -> esa20240910_models.GetWafQuotaResponse:
        """
        @summary 获取WAF配额详情
        
        @param request: GetWafQuotaRequest
        @return: GetWafQuotaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_waf_quota_with_options_async(request, runtime)

    def get_waf_rule_with_options(
        self,
        request: esa20240910_models.GetWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafRuleResponse:
        """
        @summary 获取单个WAF规则详情
        
        @param request: GetWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_waf_rule_with_options_async(
        self,
        request: esa20240910_models.GetWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafRuleResponse:
        """
        @summary 获取单个WAF规则详情
        
        @param request: GetWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_waf_rule(
        self,
        request: esa20240910_models.GetWafRuleRequest,
    ) -> esa20240910_models.GetWafRuleResponse:
        """
        @summary 获取单个WAF规则详情
        
        @param request: GetWafRuleRequest
        @return: GetWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_waf_rule_with_options(request, runtime)

    async def get_waf_rule_async(
        self,
        request: esa20240910_models.GetWafRuleRequest,
    ) -> esa20240910_models.GetWafRuleResponse:
        """
        @summary 获取单个WAF规则详情
        
        @param request: GetWafRuleRequest
        @return: GetWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_waf_rule_with_options_async(request, runtime)

    def get_waf_ruleset_with_options(
        self,
        request: esa20240910_models.GetWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafRulesetResponse:
        """
        @summary 获取WAF规则集详情
        
        @param request: GetWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafRulesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_waf_ruleset_with_options_async(
        self,
        request: esa20240910_models.GetWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.GetWafRulesetResponse:
        """
        @summary 获取WAF规则集详情
        
        @param request: GetWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.GetWafRulesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_waf_ruleset(
        self,
        request: esa20240910_models.GetWafRulesetRequest,
    ) -> esa20240910_models.GetWafRulesetResponse:
        """
        @summary 获取WAF规则集详情
        
        @param request: GetWafRulesetRequest
        @return: GetWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_waf_ruleset_with_options(request, runtime)

    async def get_waf_ruleset_async(
        self,
        request: esa20240910_models.GetWafRulesetRequest,
    ) -> esa20240910_models.GetWafRulesetResponse:
        """
        @summary 获取WAF规则集详情
        
        @param request: GetWafRulesetRequest
        @return: GetWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_waf_ruleset_with_options_async(request, runtime)

    def list_cache_reserve_instances_with_options(
        self,
        request: esa20240910_models.ListCacheReserveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListCacheReserveInstancesResponse:
        """
        @summary 查询缓存保持实例列表
        
        @param request: ListCacheReserveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCacheReserveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCacheReserveInstances',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListCacheReserveInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cache_reserve_instances_with_options_async(
        self,
        request: esa20240910_models.ListCacheReserveInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListCacheReserveInstancesResponse:
        """
        @summary 查询缓存保持实例列表
        
        @param request: ListCacheReserveInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCacheReserveInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCacheReserveInstances',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListCacheReserveInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cache_reserve_instances(
        self,
        request: esa20240910_models.ListCacheReserveInstancesRequest,
    ) -> esa20240910_models.ListCacheReserveInstancesResponse:
        """
        @summary 查询缓存保持实例列表
        
        @param request: ListCacheReserveInstancesRequest
        @return: ListCacheReserveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cache_reserve_instances_with_options(request, runtime)

    async def list_cache_reserve_instances_async(
        self,
        request: esa20240910_models.ListCacheReserveInstancesRequest,
    ) -> esa20240910_models.ListCacheReserveInstancesResponse:
        """
        @summary 查询缓存保持实例列表
        
        @param request: ListCacheReserveInstancesRequest
        @return: ListCacheReserveInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cache_reserve_instances_with_options_async(request, runtime)

    def list_client_certificates_with_options(
        self,
        request: esa20240910_models.ListClientCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListClientCertificatesResponse:
        """
        @summary 查询站点下客户端证书列表
        
        @param request: ListClientCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientCertificates',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListClientCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_client_certificates_with_options_async(
        self,
        request: esa20240910_models.ListClientCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListClientCertificatesResponse:
        """
        @summary 查询站点下客户端证书列表
        
        @param request: ListClientCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClientCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClientCertificates',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListClientCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_client_certificates(
        self,
        request: esa20240910_models.ListClientCertificatesRequest,
    ) -> esa20240910_models.ListClientCertificatesResponse:
        """
        @summary 查询站点下客户端证书列表
        
        @param request: ListClientCertificatesRequest
        @return: ListClientCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_client_certificates_with_options(request, runtime)

    async def list_client_certificates_async(
        self,
        request: esa20240910_models.ListClientCertificatesRequest,
    ) -> esa20240910_models.ListClientCertificatesResponse:
        """
        @summary 查询站点下客户端证书列表
        
        @param request: ListClientCertificatesRequest
        @return: ListClientCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_client_certificates_with_options_async(request, runtime)

    def list_edge_container_app_records_with_options(
        self,
        request: esa20240910_models.ListEdgeContainerAppRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppRecordsResponse:
        """
        @summary 获取一个边缘容器应用的全部域名记录
        
        @param request: ListEdgeContainerAppRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerAppRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_container_app_records_with_options_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppRecordsResponse:
        """
        @summary 获取一个边缘容器应用的全部域名记录
        
        @param request: ListEdgeContainerAppRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerAppRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_container_app_records(
        self,
        request: esa20240910_models.ListEdgeContainerAppRecordsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppRecordsResponse:
        """
        @summary 获取一个边缘容器应用的全部域名记录
        
        @param request: ListEdgeContainerAppRecordsRequest
        @return: ListEdgeContainerAppRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_container_app_records_with_options(request, runtime)

    async def list_edge_container_app_records_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppRecordsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppRecordsResponse:
        """
        @summary 获取一个边缘容器应用的全部域名记录
        
        @param request: ListEdgeContainerAppRecordsRequest
        @return: ListEdgeContainerAppRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_container_app_records_with_options_async(request, runtime)

    def list_edge_container_app_versions_with_options(
        self,
        request: esa20240910_models.ListEdgeContainerAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppVersionsResponse:
        """
        @summary 获取边缘容器应用的全部版本信息
        
        @param request: ListEdgeContainerAppVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerAppVersions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_container_app_versions_with_options_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppVersionsResponse:
        """
        @summary 获取边缘容器应用的全部版本信息
        
        @param request: ListEdgeContainerAppVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppVersionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerAppVersions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_container_app_versions(
        self,
        request: esa20240910_models.ListEdgeContainerAppVersionsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppVersionsResponse:
        """
        @summary 获取边缘容器应用的全部版本信息
        
        @param request: ListEdgeContainerAppVersionsRequest
        @return: ListEdgeContainerAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_container_app_versions_with_options(request, runtime)

    async def list_edge_container_app_versions_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppVersionsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppVersionsResponse:
        """
        @summary 获取边缘容器应用的全部版本信息
        
        @param request: ListEdgeContainerAppVersionsRequest
        @return: ListEdgeContainerAppVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_container_app_versions_with_options_async(request, runtime)

    def list_edge_container_apps_with_options(
        self,
        request: esa20240910_models.ListEdgeContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppsResponse:
        """
        @summary 获取用户全部边缘容器应用
        
        @param request: ListEdgeContainerAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_key):
            query['OrderKey'] = request.order_key
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerApps',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_container_apps_with_options_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerAppsResponse:
        """
        @summary 获取用户全部边缘容器应用
        
        @param request: ListEdgeContainerAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order_key):
            query['OrderKey'] = request.order_key
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_key):
            query['SearchKey'] = request.search_key
        if not UtilClient.is_unset(request.search_type):
            query['SearchType'] = request.search_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerApps',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_container_apps(
        self,
        request: esa20240910_models.ListEdgeContainerAppsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppsResponse:
        """
        @summary 获取用户全部边缘容器应用
        
        @param request: ListEdgeContainerAppsRequest
        @return: ListEdgeContainerAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_container_apps_with_options(request, runtime)

    async def list_edge_container_apps_async(
        self,
        request: esa20240910_models.ListEdgeContainerAppsRequest,
    ) -> esa20240910_models.ListEdgeContainerAppsResponse:
        """
        @summary 获取用户全部边缘容器应用
        
        @param request: ListEdgeContainerAppsRequest
        @return: ListEdgeContainerAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_container_apps_with_options_async(request, runtime)

    def list_edge_container_records_with_options(
        self,
        request: esa20240910_models.ListEdgeContainerRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerRecordsResponse:
        """
        @summary 查询站点的边缘容器记录
        
        @param request: ListEdgeContainerRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_container_records_with_options_async(
        self,
        request: esa20240910_models.ListEdgeContainerRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeContainerRecordsResponse:
        """
        @summary 查询站点的边缘容器记录
        
        @param request: ListEdgeContainerRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeContainerRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeContainerRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeContainerRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_container_records(
        self,
        request: esa20240910_models.ListEdgeContainerRecordsRequest,
    ) -> esa20240910_models.ListEdgeContainerRecordsResponse:
        """
        @summary 查询站点的边缘容器记录
        
        @param request: ListEdgeContainerRecordsRequest
        @return: ListEdgeContainerRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_container_records_with_options(request, runtime)

    async def list_edge_container_records_async(
        self,
        request: esa20240910_models.ListEdgeContainerRecordsRequest,
    ) -> esa20240910_models.ListEdgeContainerRecordsResponse:
        """
        @summary 查询站点的边缘容器记录
        
        @param request: ListEdgeContainerRecordsRequest
        @return: ListEdgeContainerRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_container_records_with_options_async(request, runtime)

    def list_edge_routine_plans_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeRoutinePlansResponse:
        """
        @summary 查询用户可购买的边缘函数的套餐
        
        @param request: ListEdgeRoutinePlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeRoutinePlansResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEdgeRoutinePlans',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeRoutinePlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_routine_plans_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeRoutinePlansResponse:
        """
        @summary 查询用户可购买的边缘函数的套餐
        
        @param request: ListEdgeRoutinePlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeRoutinePlansResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListEdgeRoutinePlans',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeRoutinePlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_routine_plans(self) -> esa20240910_models.ListEdgeRoutinePlansResponse:
        """
        @summary 查询用户可购买的边缘函数的套餐
        
        @return: ListEdgeRoutinePlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_routine_plans_with_options(runtime)

    async def list_edge_routine_plans_async(self) -> esa20240910_models.ListEdgeRoutinePlansResponse:
        """
        @summary 查询用户可购买的边缘函数的套餐
        
        @return: ListEdgeRoutinePlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_routine_plans_with_options_async(runtime)

    def list_edge_routine_records_with_options(
        self,
        request: esa20240910_models.ListEdgeRoutineRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeRoutineRecordsResponse:
        """
        @summary 查询站点的边缘路由记录
        
        @param request: ListEdgeRoutineRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeRoutineRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeRoutineRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeRoutineRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_edge_routine_records_with_options_async(
        self,
        request: esa20240910_models.ListEdgeRoutineRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListEdgeRoutineRecordsResponse:
        """
        @summary 查询站点的边缘路由记录
        
        @param request: ListEdgeRoutineRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListEdgeRoutineRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEdgeRoutineRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListEdgeRoutineRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_edge_routine_records(
        self,
        request: esa20240910_models.ListEdgeRoutineRecordsRequest,
    ) -> esa20240910_models.ListEdgeRoutineRecordsResponse:
        """
        @summary 查询站点的边缘路由记录
        
        @param request: ListEdgeRoutineRecordsRequest
        @return: ListEdgeRoutineRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_edge_routine_records_with_options(request, runtime)

    async def list_edge_routine_records_async(
        self,
        request: esa20240910_models.ListEdgeRoutineRecordsRequest,
    ) -> esa20240910_models.ListEdgeRoutineRecordsResponse:
        """
        @summary 查询站点的边缘路由记录
        
        @param request: ListEdgeRoutineRecordsRequest
        @return: ListEdgeRoutineRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_edge_routine_records_with_options_async(request, runtime)

    def list_instance_quotas_with_options(
        self,
        request: esa20240910_models.ListInstanceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListInstanceQuotasResponse:
        """
        @summary 查询实例或者站点的quota值
        
        @param request: ListInstanceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceQuotasResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceQuotas',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListInstanceQuotasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_quotas_with_options_async(
        self,
        request: esa20240910_models.ListInstanceQuotasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListInstanceQuotasResponse:
        """
        @summary 查询实例或者站点的quota值
        
        @param request: ListInstanceQuotasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceQuotasResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceQuotas',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListInstanceQuotasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_quotas(
        self,
        request: esa20240910_models.ListInstanceQuotasRequest,
    ) -> esa20240910_models.ListInstanceQuotasResponse:
        """
        @summary 查询实例或者站点的quota值
        
        @param request: ListInstanceQuotasRequest
        @return: ListInstanceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_quotas_with_options(request, runtime)

    async def list_instance_quotas_async(
        self,
        request: esa20240910_models.ListInstanceQuotasRequest,
    ) -> esa20240910_models.ListInstanceQuotasResponse:
        """
        @summary 查询实例或者站点的quota值
        
        @param request: ListInstanceQuotasRequest
        @return: ListInstanceQuotasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_quotas_with_options_async(request, runtime)

    def list_instance_quotas_with_usage_with_options(
        self,
        request: esa20240910_models.ListInstanceQuotasWithUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListInstanceQuotasWithUsageResponse:
        """
        @summary 查询功能quota和用量
        
        @param request: ListInstanceQuotasWithUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceQuotasWithUsageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceQuotasWithUsage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListInstanceQuotasWithUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_quotas_with_usage_with_options_async(
        self,
        request: esa20240910_models.ListInstanceQuotasWithUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListInstanceQuotasWithUsageResponse:
        """
        @summary 查询功能quota和用量
        
        @param request: ListInstanceQuotasWithUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceQuotasWithUsageResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceQuotasWithUsage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListInstanceQuotasWithUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_quotas_with_usage(
        self,
        request: esa20240910_models.ListInstanceQuotasWithUsageRequest,
    ) -> esa20240910_models.ListInstanceQuotasWithUsageResponse:
        """
        @summary 查询功能quota和用量
        
        @param request: ListInstanceQuotasWithUsageRequest
        @return: ListInstanceQuotasWithUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_quotas_with_usage_with_options(request, runtime)

    async def list_instance_quotas_with_usage_async(
        self,
        request: esa20240910_models.ListInstanceQuotasWithUsageRequest,
    ) -> esa20240910_models.ListInstanceQuotasWithUsageResponse:
        """
        @summary 查询功能quota和用量
        
        @param request: ListInstanceQuotasWithUsageRequest
        @return: ListInstanceQuotasWithUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_quotas_with_usage_with_options_async(request, runtime)

    def list_kvs_with_options(
        self,
        request: esa20240910_models.ListKvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListKvsResponse:
        """
        @summary 遍历Namespace的Key值
        
        @param request: ListKvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKvsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKvs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListKvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kvs_with_options_async(
        self,
        request: esa20240910_models.ListKvsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListKvsResponse:
        """
        @summary 遍历Namespace的Key值
        
        @param request: ListKvsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKvsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKvs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListKvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kvs(
        self,
        request: esa20240910_models.ListKvsRequest,
    ) -> esa20240910_models.ListKvsResponse:
        """
        @summary 遍历Namespace的Key值
        
        @param request: ListKvsRequest
        @return: ListKvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_kvs_with_options(request, runtime)

    async def list_kvs_async(
        self,
        request: esa20240910_models.ListKvsRequest,
    ) -> esa20240910_models.ListKvsResponse:
        """
        @summary 遍历Namespace的Key值
        
        @param request: ListKvsRequest
        @return: ListKvsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_kvs_with_options_async(request, runtime)

    def list_lists_with_options(
        self,
        tmp_req: esa20240910_models.ListListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListListsResponse:
        """
        @summary 列举自定义列表
        
        @param tmp_req: ListListsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListListsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLists',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListListsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_lists_with_options_async(
        self,
        tmp_req: esa20240910_models.ListListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListListsResponse:
        """
        @summary 列举自定义列表
        
        @param tmp_req: ListListsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListListsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListListsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLists',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListListsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_lists(
        self,
        request: esa20240910_models.ListListsRequest,
    ) -> esa20240910_models.ListListsResponse:
        """
        @summary 列举自定义列表
        
        @param request: ListListsRequest
        @return: ListListsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_lists_with_options(request, runtime)

    async def list_lists_async(
        self,
        request: esa20240910_models.ListListsRequest,
    ) -> esa20240910_models.ListListsResponse:
        """
        @summary 列举自定义列表
        
        @param request: ListListsRequest
        @return: ListListsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_lists_with_options_async(request, runtime)

    def list_load_balancer_regions_with_options(
        self,
        request: esa20240910_models.ListLoadBalancerRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListLoadBalancerRegionsResponse:
        """
        @summary 查询负载均衡区域列表
        
        @param request: ListLoadBalancerRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancerRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancerRegions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListLoadBalancerRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_load_balancer_regions_with_options_async(
        self,
        request: esa20240910_models.ListLoadBalancerRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListLoadBalancerRegionsResponse:
        """
        @summary 查询负载均衡区域列表
        
        @param request: ListLoadBalancerRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLoadBalancerRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLoadBalancerRegions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListLoadBalancerRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_load_balancer_regions(
        self,
        request: esa20240910_models.ListLoadBalancerRegionsRequest,
    ) -> esa20240910_models.ListLoadBalancerRegionsResponse:
        """
        @summary 查询负载均衡区域列表
        
        @param request: ListLoadBalancerRegionsRequest
        @return: ListLoadBalancerRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_load_balancer_regions_with_options(request, runtime)

    async def list_load_balancer_regions_async(
        self,
        request: esa20240910_models.ListLoadBalancerRegionsRequest,
    ) -> esa20240910_models.ListLoadBalancerRegionsResponse:
        """
        @summary 查询负载均衡区域列表
        
        @param request: ListLoadBalancerRegionsRequest
        @return: ListLoadBalancerRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_load_balancer_regions_with_options_async(request, runtime)

    def list_managed_rules_groups_with_options(
        self,
        request: esa20240910_models.ListManagedRulesGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListManagedRulesGroupsResponse:
        """
        @summary 列举自定义托管规则组
        
        @param request: ListManagedRulesGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManagedRulesGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManagedRulesGroups',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListManagedRulesGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_managed_rules_groups_with_options_async(
        self,
        request: esa20240910_models.ListManagedRulesGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListManagedRulesGroupsResponse:
        """
        @summary 列举自定义托管规则组
        
        @param request: ListManagedRulesGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManagedRulesGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManagedRulesGroups',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListManagedRulesGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_managed_rules_groups(
        self,
        request: esa20240910_models.ListManagedRulesGroupsRequest,
    ) -> esa20240910_models.ListManagedRulesGroupsResponse:
        """
        @summary 列举自定义托管规则组
        
        @param request: ListManagedRulesGroupsRequest
        @return: ListManagedRulesGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_managed_rules_groups_with_options(request, runtime)

    async def list_managed_rules_groups_async(
        self,
        request: esa20240910_models.ListManagedRulesGroupsRequest,
    ) -> esa20240910_models.ListManagedRulesGroupsResponse:
        """
        @summary 列举自定义托管规则组
        
        @param request: ListManagedRulesGroupsRequest
        @return: ListManagedRulesGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_managed_rules_groups_with_options_async(request, runtime)

    def list_pages_with_options(
        self,
        request: esa20240910_models.ListPagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListPagesResponse:
        """
        @summary 列举自定义响应页面
        
        @param request: ListPagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPages',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListPagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pages_with_options_async(
        self,
        request: esa20240910_models.ListPagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListPagesResponse:
        """
        @summary 列举自定义响应页面
        
        @param request: ListPagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPages',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListPagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pages(
        self,
        request: esa20240910_models.ListPagesRequest,
    ) -> esa20240910_models.ListPagesResponse:
        """
        @summary 列举自定义响应页面
        
        @param request: ListPagesRequest
        @return: ListPagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_pages_with_options(request, runtime)

    async def list_pages_async(
        self,
        request: esa20240910_models.ListPagesRequest,
    ) -> esa20240910_models.ListPagesResponse:
        """
        @summary 列举自定义响应页面
        
        @param request: ListPagesRequest
        @return: ListPagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_pages_with_options_async(request, runtime)

    def list_records_with_options(
        self,
        request: esa20240910_models.ListRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRecordsResponse:
        """
        @summary 查询站点下的记录列表
        
        @param request: ListRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_records_with_options_async(
        self,
        request: esa20240910_models.ListRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRecordsResponse:
        """
        @summary 查询站点下的记录列表
        
        @param request: ListRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRecordsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRecords',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_records(
        self,
        request: esa20240910_models.ListRecordsRequest,
    ) -> esa20240910_models.ListRecordsResponse:
        """
        @summary 查询站点下的记录列表
        
        @param request: ListRecordsRequest
        @return: ListRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_records_with_options(request, runtime)

    async def list_records_async(
        self,
        request: esa20240910_models.ListRecordsRequest,
    ) -> esa20240910_models.ListRecordsResponse:
        """
        @summary 查询站点下的记录列表
        
        @param request: ListRecordsRequest
        @return: ListRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_records_with_options_async(request, runtime)

    def list_routine_canary_areas_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRoutineCanaryAreasResponse:
        """
        @summary 查询Routine灰度环境列表
        
        @param request: ListRoutineCanaryAreasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutineCanaryAreasResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRoutineCanaryAreas',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRoutineCanaryAreasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_routine_canary_areas_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRoutineCanaryAreasResponse:
        """
        @summary 查询Routine灰度环境列表
        
        @param request: ListRoutineCanaryAreasRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutineCanaryAreasResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRoutineCanaryAreas',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRoutineCanaryAreasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_routine_canary_areas(self) -> esa20240910_models.ListRoutineCanaryAreasResponse:
        """
        @summary 查询Routine灰度环境列表
        
        @return: ListRoutineCanaryAreasResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_routine_canary_areas_with_options(runtime)

    async def list_routine_canary_areas_async(self) -> esa20240910_models.ListRoutineCanaryAreasResponse:
        """
        @summary 查询Routine灰度环境列表
        
        @return: ListRoutineCanaryAreasResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_routine_canary_areas_with_options_async(runtime)

    def list_routine_optional_specs_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRoutineOptionalSpecsResponse:
        """
        @summary 查询Routine可选择规格列表
        
        @param request: ListRoutineOptionalSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutineOptionalSpecsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRoutineOptionalSpecs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRoutineOptionalSpecsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_routine_optional_specs_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListRoutineOptionalSpecsResponse:
        """
        @summary 查询Routine可选择规格列表
        
        @param request: ListRoutineOptionalSpecsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRoutineOptionalSpecsResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListRoutineOptionalSpecs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListRoutineOptionalSpecsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_routine_optional_specs(self) -> esa20240910_models.ListRoutineOptionalSpecsResponse:
        """
        @summary 查询Routine可选择规格列表
        
        @return: ListRoutineOptionalSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_routine_optional_specs_with_options(runtime)

    async def list_routine_optional_specs_async(self) -> esa20240910_models.ListRoutineOptionalSpecsResponse:
        """
        @summary 查询Routine可选择规格列表
        
        @return: ListRoutineOptionalSpecsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_routine_optional_specs_with_options_async(runtime)

    def list_scheduled_preload_executions_with_options(
        self,
        request: esa20240910_models.ListScheduledPreloadExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListScheduledPreloadExecutionsResponse:
        """
        @summary 列出指定任务下的执行计划
        
        @param request: ListScheduledPreloadExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPreloadExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPreloadExecutions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListScheduledPreloadExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_preload_executions_with_options_async(
        self,
        request: esa20240910_models.ListScheduledPreloadExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListScheduledPreloadExecutionsResponse:
        """
        @summary 列出指定任务下的执行计划
        
        @param request: ListScheduledPreloadExecutionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPreloadExecutionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPreloadExecutions',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListScheduledPreloadExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_preload_executions(
        self,
        request: esa20240910_models.ListScheduledPreloadExecutionsRequest,
    ) -> esa20240910_models.ListScheduledPreloadExecutionsResponse:
        """
        @summary 列出指定任务下的执行计划
        
        @param request: ListScheduledPreloadExecutionsRequest
        @return: ListScheduledPreloadExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scheduled_preload_executions_with_options(request, runtime)

    async def list_scheduled_preload_executions_async(
        self,
        request: esa20240910_models.ListScheduledPreloadExecutionsRequest,
    ) -> esa20240910_models.ListScheduledPreloadExecutionsResponse:
        """
        @summary 列出指定任务下的执行计划
        
        @param request: ListScheduledPreloadExecutionsRequest
        @return: ListScheduledPreloadExecutionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scheduled_preload_executions_with_options_async(request, runtime)

    def list_scheduled_preload_jobs_with_options(
        self,
        request: esa20240910_models.ListScheduledPreloadJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListScheduledPreloadJobsResponse:
        """
        @summary 列出定时预热任务列表
        
        @param request: ListScheduledPreloadJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPreloadJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPreloadJobs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListScheduledPreloadJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheduled_preload_jobs_with_options_async(
        self,
        request: esa20240910_models.ListScheduledPreloadJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListScheduledPreloadJobsResponse:
        """
        @summary 列出定时预热任务列表
        
        @param request: ListScheduledPreloadJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScheduledPreloadJobsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScheduledPreloadJobs',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListScheduledPreloadJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheduled_preload_jobs(
        self,
        request: esa20240910_models.ListScheduledPreloadJobsRequest,
    ) -> esa20240910_models.ListScheduledPreloadJobsResponse:
        """
        @summary 列出定时预热任务列表
        
        @param request: ListScheduledPreloadJobsRequest
        @return: ListScheduledPreloadJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scheduled_preload_jobs_with_options(request, runtime)

    async def list_scheduled_preload_jobs_async(
        self,
        request: esa20240910_models.ListScheduledPreloadJobsRequest,
    ) -> esa20240910_models.ListScheduledPreloadJobsResponse:
        """
        @summary 列出定时预热任务列表
        
        @param request: ListScheduledPreloadJobsRequest
        @return: ListScheduledPreloadJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scheduled_preload_jobs_with_options_async(request, runtime)

    def list_site_delivery_tasks_with_options(
        self,
        request: esa20240910_models.ListSiteDeliveryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListSiteDeliveryTasksResponse:
        """
        @summary 列出全部任务投递
        
        @param request: ListSiteDeliveryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSiteDeliveryTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSiteDeliveryTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListSiteDeliveryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_site_delivery_tasks_with_options_async(
        self,
        request: esa20240910_models.ListSiteDeliveryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListSiteDeliveryTasksResponse:
        """
        @summary 列出全部任务投递
        
        @param request: ListSiteDeliveryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSiteDeliveryTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSiteDeliveryTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListSiteDeliveryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_site_delivery_tasks(
        self,
        request: esa20240910_models.ListSiteDeliveryTasksRequest,
    ) -> esa20240910_models.ListSiteDeliveryTasksResponse:
        """
        @summary 列出全部任务投递
        
        @param request: ListSiteDeliveryTasksRequest
        @return: ListSiteDeliveryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_site_delivery_tasks_with_options(request, runtime)

    async def list_site_delivery_tasks_async(
        self,
        request: esa20240910_models.ListSiteDeliveryTasksRequest,
    ) -> esa20240910_models.ListSiteDeliveryTasksResponse:
        """
        @summary 列出全部任务投递
        
        @param request: ListSiteDeliveryTasksRequest
        @return: ListSiteDeliveryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_site_delivery_tasks_with_options_async(request, runtime)

    def list_sites_with_options(
        self,
        tmp_req: esa20240910_models.ListSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListSitesResponse:
        """
        @summary 查询站点列表
        
        @param tmp_req: ListSitesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSitesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListSitesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_filter):
            request.tag_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_filter, 'TagFilter', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSites',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListSitesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sites_with_options_async(
        self,
        tmp_req: esa20240910_models.ListSitesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListSitesResponse:
        """
        @summary 查询站点列表
        
        @param tmp_req: ListSitesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSitesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListSitesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag_filter):
            request.tag_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_filter, 'TagFilter', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSites',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListSitesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sites(
        self,
        request: esa20240910_models.ListSitesRequest,
    ) -> esa20240910_models.ListSitesResponse:
        """
        @summary 查询站点列表
        
        @param request: ListSitesRequest
        @return: ListSitesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_sites_with_options(request, runtime)

    async def list_sites_async(
        self,
        request: esa20240910_models.ListSitesRequest,
    ) -> esa20240910_models.ListSitesResponse:
        """
        @summary 查询站点列表
        
        @param request: ListSitesRequest
        @return: ListSitesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_sites_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: esa20240910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListTagResourcesResponse:
        """
        @summary 查询云资源已经绑定的标签列表
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_item):
            query['MaxItem'] = request.max_item
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: esa20240910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListTagResourcesResponse:
        """
        @summary 查询云资源已经绑定的标签列表
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_item):
            query['MaxItem'] = request.max_item
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: esa20240910_models.ListTagResourcesRequest,
    ) -> esa20240910_models.ListTagResourcesResponse:
        """
        @summary 查询云资源已经绑定的标签列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: esa20240910_models.ListTagResourcesRequest,
    ) -> esa20240910_models.ListTagResourcesResponse:
        """
        @summary 查询云资源已经绑定的标签列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_upload_tasks_with_options(
        self,
        request: esa20240910_models.ListUploadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUploadTasksResponse:
        """
        @summary 获取文件上传任务
        
        @param request: ListUploadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUploadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUploadTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUploadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upload_tasks_with_options_async(
        self,
        request: esa20240910_models.ListUploadTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUploadTasksResponse:
        """
        @summary 获取文件上传任务
        
        @param request: ListUploadTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUploadTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUploadTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUploadTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upload_tasks(
        self,
        request: esa20240910_models.ListUploadTasksRequest,
    ) -> esa20240910_models.ListUploadTasksResponse:
        """
        @summary 获取文件上传任务
        
        @param request: ListUploadTasksRequest
        @return: ListUploadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_upload_tasks_with_options(request, runtime)

    async def list_upload_tasks_async(
        self,
        request: esa20240910_models.ListUploadTasksRequest,
    ) -> esa20240910_models.ListUploadTasksResponse:
        """
        @summary 获取文件上传任务
        
        @param request: ListUploadTasksRequest
        @return: ListUploadTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_upload_tasks_with_options_async(request, runtime)

    def list_user_delivery_tasks_with_options(
        self,
        request: esa20240910_models.ListUserDeliveryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUserDeliveryTasksResponse:
        """
        @summary 列出用户全部任务投递
        
        @param request: ListUserDeliveryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDeliveryTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDeliveryTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUserDeliveryTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_delivery_tasks_with_options_async(
        self,
        request: esa20240910_models.ListUserDeliveryTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUserDeliveryTasksResponse:
        """
        @summary 列出用户全部任务投递
        
        @param request: ListUserDeliveryTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserDeliveryTasksResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserDeliveryTasks',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUserDeliveryTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_delivery_tasks(
        self,
        request: esa20240910_models.ListUserDeliveryTasksRequest,
    ) -> esa20240910_models.ListUserDeliveryTasksResponse:
        """
        @summary 列出用户全部任务投递
        
        @param request: ListUserDeliveryTasksRequest
        @return: ListUserDeliveryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_delivery_tasks_with_options(request, runtime)

    async def list_user_delivery_tasks_async(
        self,
        request: esa20240910_models.ListUserDeliveryTasksRequest,
    ) -> esa20240910_models.ListUserDeliveryTasksResponse:
        """
        @summary 列出用户全部任务投递
        
        @param request: ListUserDeliveryTasksRequest
        @return: ListUserDeliveryTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_delivery_tasks_with_options_async(request, runtime)

    def list_user_rate_plan_instances_with_options(
        self,
        request: esa20240910_models.ListUserRatePlanInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUserRatePlanInstancesResponse:
        """
        @summary 查询该用户下可用的已购套餐实例
        
        @param request: ListUserRatePlanInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserRatePlanInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRatePlanInstances',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUserRatePlanInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_rate_plan_instances_with_options_async(
        self,
        request: esa20240910_models.ListUserRatePlanInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListUserRatePlanInstancesResponse:
        """
        @summary 查询该用户下可用的已购套餐实例
        
        @param request: ListUserRatePlanInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserRatePlanInstancesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserRatePlanInstances',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListUserRatePlanInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_rate_plan_instances(
        self,
        request: esa20240910_models.ListUserRatePlanInstancesRequest,
    ) -> esa20240910_models.ListUserRatePlanInstancesResponse:
        """
        @summary 查询该用户下可用的已购套餐实例
        
        @param request: ListUserRatePlanInstancesRequest
        @return: ListUserRatePlanInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_rate_plan_instances_with_options(request, runtime)

    async def list_user_rate_plan_instances_async(
        self,
        request: esa20240910_models.ListUserRatePlanInstancesRequest,
    ) -> esa20240910_models.ListUserRatePlanInstancesResponse:
        """
        @summary 查询该用户下可用的已购套餐实例
        
        @param request: ListUserRatePlanInstancesRequest
        @return: ListUserRatePlanInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_rate_plan_instances_with_options_async(request, runtime)

    def list_waf_managed_rules_with_options(
        self,
        tmp_req: esa20240910_models.ListWafManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafManagedRulesResponse:
        """
        @summary 列举WAF托管规则
        
        @param tmp_req: ListWafManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafManagedRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafManagedRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafManagedRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafManagedRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_managed_rules_with_options_async(
        self,
        tmp_req: esa20240910_models.ListWafManagedRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafManagedRulesResponse:
        """
        @summary 列举WAF托管规则
        
        @param tmp_req: ListWafManagedRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafManagedRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafManagedRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.attack_type):
            query['AttackType'] = request.attack_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protection_level):
            query['ProtectionLevel'] = request.protection_level
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafManagedRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafManagedRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_managed_rules(
        self,
        request: esa20240910_models.ListWafManagedRulesRequest,
    ) -> esa20240910_models.ListWafManagedRulesResponse:
        """
        @summary 列举WAF托管规则
        
        @param request: ListWafManagedRulesRequest
        @return: ListWafManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_managed_rules_with_options(request, runtime)

    async def list_waf_managed_rules_async(
        self,
        request: esa20240910_models.ListWafManagedRulesRequest,
    ) -> esa20240910_models.ListWafManagedRulesResponse:
        """
        @summary 列举WAF托管规则
        
        @param request: ListWafManagedRulesRequest
        @return: ListWafManagedRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_managed_rules_with_options_async(request, runtime)

    def list_waf_phases_with_options(
        self,
        request: esa20240910_models.ListWafPhasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafPhasesResponse:
        """
        @summary 列举WAF阶段
        
        @param request: ListWafPhasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafPhasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafPhases',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafPhasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_phases_with_options_async(
        self,
        request: esa20240910_models.ListWafPhasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafPhasesResponse:
        """
        @summary 列举WAF阶段
        
        @param request: ListWafPhasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafPhasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafPhases',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafPhasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_phases(
        self,
        request: esa20240910_models.ListWafPhasesRequest,
    ) -> esa20240910_models.ListWafPhasesResponse:
        """
        @summary 列举WAF阶段
        
        @param request: ListWafPhasesRequest
        @return: ListWafPhasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_phases_with_options(request, runtime)

    async def list_waf_phases_async(
        self,
        request: esa20240910_models.ListWafPhasesRequest,
    ) -> esa20240910_models.ListWafPhasesResponse:
        """
        @summary 列举WAF阶段
        
        @param request: ListWafPhasesRequest
        @return: ListWafPhasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_phases_with_options_async(request, runtime)

    def list_waf_rules_with_options(
        self,
        tmp_req: esa20240910_models.ListWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafRulesResponse:
        """
        @summary 列举WAF规则
        
        @param tmp_req: ListWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_rules_with_options_async(
        self,
        tmp_req: esa20240910_models.ListWafRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafRulesResponse:
        """
        @summary 列举WAF规则
        
        @param tmp_req: ListWafRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_rules(
        self,
        request: esa20240910_models.ListWafRulesRequest,
    ) -> esa20240910_models.ListWafRulesResponse:
        """
        @summary 列举WAF规则
        
        @param request: ListWafRulesRequest
        @return: ListWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_rules_with_options(request, runtime)

    async def list_waf_rules_async(
        self,
        request: esa20240910_models.ListWafRulesRequest,
    ) -> esa20240910_models.ListWafRulesResponse:
        """
        @summary 列举WAF规则
        
        @param request: ListWafRulesRequest
        @return: ListWafRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_rules_with_options_async(request, runtime)

    def list_waf_rulesets_with_options(
        self,
        tmp_req: esa20240910_models.ListWafRulesetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafRulesetsResponse:
        """
        @summary 列举WAF规则集
        
        @param tmp_req: ListWafRulesetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafRulesetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafRulesetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafRulesets',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafRulesetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_rulesets_with_options_async(
        self,
        tmp_req: esa20240910_models.ListWafRulesetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafRulesetsResponse:
        """
        @summary 列举WAF规则集
        
        @param tmp_req: ListWafRulesetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafRulesetsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafRulesetsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafRulesets',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafRulesetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_rulesets(
        self,
        request: esa20240910_models.ListWafRulesetsRequest,
    ) -> esa20240910_models.ListWafRulesetsResponse:
        """
        @summary 列举WAF规则集
        
        @param request: ListWafRulesetsRequest
        @return: ListWafRulesetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_rulesets_with_options(request, runtime)

    async def list_waf_rulesets_async(
        self,
        request: esa20240910_models.ListWafRulesetsRequest,
    ) -> esa20240910_models.ListWafRulesetsResponse:
        """
        @summary 列举WAF规则集
        
        @param request: ListWafRulesetsRequest
        @return: ListWafRulesetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_rulesets_with_options_async(request, runtime)

    def list_waf_template_rules_with_options(
        self,
        tmp_req: esa20240910_models.ListWafTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafTemplateRulesResponse:
        """
        @summary 列举WAF模板规则
        
        @param tmp_req: ListWafTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafTemplateRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafTemplateRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafTemplateRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafTemplateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_template_rules_with_options_async(
        self,
        tmp_req: esa20240910_models.ListWafTemplateRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafTemplateRulesResponse:
        """
        @summary 列举WAF模板规则
        
        @param tmp_req: ListWafTemplateRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafTemplateRulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.ListWafTemplateRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query_args):
            request.query_args_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query_args, 'QueryArgs', 'json')
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.query_args_shrink):
            query['QueryArgs'] = request.query_args_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafTemplateRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafTemplateRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_template_rules(
        self,
        request: esa20240910_models.ListWafTemplateRulesRequest,
    ) -> esa20240910_models.ListWafTemplateRulesResponse:
        """
        @summary 列举WAF模板规则
        
        @param request: ListWafTemplateRulesRequest
        @return: ListWafTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_template_rules_with_options(request, runtime)

    async def list_waf_template_rules_async(
        self,
        request: esa20240910_models.ListWafTemplateRulesRequest,
    ) -> esa20240910_models.ListWafTemplateRulesResponse:
        """
        @summary 列举WAF模板规则
        
        @param request: ListWafTemplateRulesRequest
        @return: ListWafTemplateRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_template_rules_with_options_async(request, runtime)

    def list_waf_usage_of_rules_with_options(
        self,
        request: esa20240910_models.ListWafUsageOfRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafUsageOfRulesResponse:
        """
        @summary 列举WAF规则使用情况
        
        @param request: ListWafUsageOfRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafUsageOfRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafUsageOfRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafUsageOfRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waf_usage_of_rules_with_options_async(
        self,
        request: esa20240910_models.ListWafUsageOfRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWafUsageOfRulesResponse:
        """
        @summary 列举WAF规则使用情况
        
        @param request: ListWafUsageOfRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWafUsageOfRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.phase):
            query['Phase'] = request.phase
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWafUsageOfRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWafUsageOfRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waf_usage_of_rules(
        self,
        request: esa20240910_models.ListWafUsageOfRulesRequest,
    ) -> esa20240910_models.ListWafUsageOfRulesResponse:
        """
        @summary 列举WAF规则使用情况
        
        @param request: ListWafUsageOfRulesRequest
        @return: ListWafUsageOfRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waf_usage_of_rules_with_options(request, runtime)

    async def list_waf_usage_of_rules_async(
        self,
        request: esa20240910_models.ListWafUsageOfRulesRequest,
    ) -> esa20240910_models.ListWafUsageOfRulesResponse:
        """
        @summary 列举WAF规则使用情况
        
        @param request: ListWafUsageOfRulesRequest
        @return: ListWafUsageOfRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waf_usage_of_rules_with_options_async(request, runtime)

    def list_waiting_room_events_with_options(
        self,
        request: esa20240910_models.ListWaitingRoomEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomEventsResponse:
        """
        @summary 查询等候室事件
        
        @param request: ListWaitingRoomEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRoomEvents',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waiting_room_events_with_options_async(
        self,
        request: esa20240910_models.ListWaitingRoomEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomEventsResponse:
        """
        @summary 查询等候室事件
        
        @param request: ListWaitingRoomEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomEventsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRoomEvents',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waiting_room_events(
        self,
        request: esa20240910_models.ListWaitingRoomEventsRequest,
    ) -> esa20240910_models.ListWaitingRoomEventsResponse:
        """
        @summary 查询等候室事件
        
        @param request: ListWaitingRoomEventsRequest
        @return: ListWaitingRoomEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waiting_room_events_with_options(request, runtime)

    async def list_waiting_room_events_async(
        self,
        request: esa20240910_models.ListWaitingRoomEventsRequest,
    ) -> esa20240910_models.ListWaitingRoomEventsResponse:
        """
        @summary 查询等候室事件
        
        @param request: ListWaitingRoomEventsRequest
        @return: ListWaitingRoomEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waiting_room_events_with_options_async(request, runtime)

    def list_waiting_room_rules_with_options(
        self,
        request: esa20240910_models.ListWaitingRoomRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomRulesResponse:
        """
        @summary 查询等候室绕过规则
        
        @param request: ListWaitingRoomRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRoomRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waiting_room_rules_with_options_async(
        self,
        request: esa20240910_models.ListWaitingRoomRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomRulesResponse:
        """
        @summary 查询等候室绕过规则
        
        @param request: ListWaitingRoomRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomRulesResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRoomRules',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waiting_room_rules(
        self,
        request: esa20240910_models.ListWaitingRoomRulesRequest,
    ) -> esa20240910_models.ListWaitingRoomRulesResponse:
        """
        @summary 查询等候室绕过规则
        
        @param request: ListWaitingRoomRulesRequest
        @return: ListWaitingRoomRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waiting_room_rules_with_options(request, runtime)

    async def list_waiting_room_rules_async(
        self,
        request: esa20240910_models.ListWaitingRoomRulesRequest,
    ) -> esa20240910_models.ListWaitingRoomRulesResponse:
        """
        @summary 查询等候室绕过规则
        
        @param request: ListWaitingRoomRulesRequest
        @return: ListWaitingRoomRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waiting_room_rules_with_options_async(request, runtime)

    def list_waiting_rooms_with_options(
        self,
        request: esa20240910_models.ListWaitingRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomsResponse:
        """
        @summary 查询等候室
        
        @param request: ListWaitingRoomsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRooms',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_waiting_rooms_with_options_async(
        self,
        request: esa20240910_models.ListWaitingRoomsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ListWaitingRoomsResponse:
        """
        @summary 查询等候室
        
        @param request: ListWaitingRoomsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWaitingRoomsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWaitingRooms',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ListWaitingRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_waiting_rooms(
        self,
        request: esa20240910_models.ListWaitingRoomsRequest,
    ) -> esa20240910_models.ListWaitingRoomsResponse:
        """
        @summary 查询等候室
        
        @param request: ListWaitingRoomsRequest
        @return: ListWaitingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_waiting_rooms_with_options(request, runtime)

    async def list_waiting_rooms_async(
        self,
        request: esa20240910_models.ListWaitingRoomsRequest,
    ) -> esa20240910_models.ListWaitingRoomsResponse:
        """
        @summary 查询等候室
        
        @param request: ListWaitingRoomsRequest
        @return: ListWaitingRoomsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_waiting_rooms_with_options_async(request, runtime)

    def preload_caches_with_options(
        self,
        tmp_req: esa20240910_models.PreloadCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PreloadCachesResponse:
        """
        @summary 缓存预热
        
        @param tmp_req: PreloadCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadCachesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PreloadCachesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.headers):
            request.headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreloadCaches',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PreloadCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def preload_caches_with_options_async(
        self,
        tmp_req: esa20240910_models.PreloadCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PreloadCachesResponse:
        """
        @summary 缓存预热
        
        @param tmp_req: PreloadCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreloadCachesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PreloadCachesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        if not UtilClient.is_unset(tmp_req.headers):
            request.headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.headers, 'Headers', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.headers_shrink):
            query['Headers'] = request.headers_shrink
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreloadCaches',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PreloadCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preload_caches(
        self,
        request: esa20240910_models.PreloadCachesRequest,
    ) -> esa20240910_models.PreloadCachesResponse:
        """
        @summary 缓存预热
        
        @param request: PreloadCachesRequest
        @return: PreloadCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preload_caches_with_options(request, runtime)

    async def preload_caches_async(
        self,
        request: esa20240910_models.PreloadCachesRequest,
    ) -> esa20240910_models.PreloadCachesResponse:
        """
        @summary 缓存预热
        
        @param request: PreloadCachesRequest
        @return: PreloadCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preload_caches_with_options_async(request, runtime)

    def publish_edge_container_app_version_with_options(
        self,
        tmp_req: esa20240910_models.PublishEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PublishEdgeContainerAppVersionResponse:
        """
        @summary 发布边缘容器应用的某个版本
        
        @param tmp_req: PublishEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PublishEdgeContainerAppVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.regions):
            request.regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        query = {}
        if not UtilClient.is_unset(request.full_release):
            query['FullRelease'] = request.full_release
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.percentage):
            body['Percentage'] = request.percentage
        if not UtilClient.is_unset(request.publish_env):
            body['PublishEnv'] = request.publish_env
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PublishEdgeContainerAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_edge_container_app_version_with_options_async(
        self,
        tmp_req: esa20240910_models.PublishEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PublishEdgeContainerAppVersionResponse:
        """
        @summary 发布边缘容器应用的某个版本
        
        @param tmp_req: PublishEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PublishEdgeContainerAppVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.regions):
            request.regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regions, 'Regions', 'json')
        query = {}
        if not UtilClient.is_unset(request.full_release):
            query['FullRelease'] = request.full_release
        if not UtilClient.is_unset(request.publish_type):
            query['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.regions_shrink):
            query['Regions'] = request.regions_shrink
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.percentage):
            body['Percentage'] = request.percentage
        if not UtilClient.is_unset(request.publish_env):
            body['PublishEnv'] = request.publish_env
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PublishEdgeContainerAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_edge_container_app_version(
        self,
        request: esa20240910_models.PublishEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.PublishEdgeContainerAppVersionResponse:
        """
        @summary 发布边缘容器应用的某个版本
        
        @param request: PublishEdgeContainerAppVersionRequest
        @return: PublishEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_edge_container_app_version_with_options(request, runtime)

    async def publish_edge_container_app_version_async(
        self,
        request: esa20240910_models.PublishEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.PublishEdgeContainerAppVersionResponse:
        """
        @summary 发布边缘容器应用的某个版本
        
        @param request: PublishEdgeContainerAppVersionRequest
        @return: PublishEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_edge_container_app_version_with_options_async(request, runtime)

    def publish_routine_code_version_with_options(
        self,
        tmp_req: esa20240910_models.PublishRoutineCodeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PublishRoutineCodeVersionResponse:
        """
        @summary 发布Routine某版本代码
        
        @param tmp_req: PublishRoutineCodeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRoutineCodeVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PublishRoutineCodeVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.canary_area_list):
            request.canary_area_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.canary_area_list, 'CanaryAreaList', 'json')
        body = {}
        if not UtilClient.is_unset(request.canary_area_list_shrink):
            body['CanaryAreaList'] = request.canary_area_list_shrink
        if not UtilClient.is_unset(request.canary_code_version):
            body['CanaryCodeVersion'] = request.canary_code_version
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRoutineCodeVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PublishRoutineCodeVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_routine_code_version_with_options_async(
        self,
        tmp_req: esa20240910_models.PublishRoutineCodeVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PublishRoutineCodeVersionResponse:
        """
        @summary 发布Routine某版本代码
        
        @param tmp_req: PublishRoutineCodeVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRoutineCodeVersionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PublishRoutineCodeVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.canary_area_list):
            request.canary_area_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.canary_area_list, 'CanaryAreaList', 'json')
        body = {}
        if not UtilClient.is_unset(request.canary_area_list_shrink):
            body['CanaryAreaList'] = request.canary_area_list_shrink
        if not UtilClient.is_unset(request.canary_code_version):
            body['CanaryCodeVersion'] = request.canary_code_version
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.env):
            body['Env'] = request.env
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRoutineCodeVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PublishRoutineCodeVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_routine_code_version(
        self,
        request: esa20240910_models.PublishRoutineCodeVersionRequest,
    ) -> esa20240910_models.PublishRoutineCodeVersionResponse:
        """
        @summary 发布Routine某版本代码
        
        @param request: PublishRoutineCodeVersionRequest
        @return: PublishRoutineCodeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.publish_routine_code_version_with_options(request, runtime)

    async def publish_routine_code_version_async(
        self,
        request: esa20240910_models.PublishRoutineCodeVersionRequest,
    ) -> esa20240910_models.PublishRoutineCodeVersionResponse:
        """
        @summary 发布Routine某版本代码
        
        @param request: PublishRoutineCodeVersionRequest
        @return: PublishRoutineCodeVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.publish_routine_code_version_with_options_async(request, runtime)

    def purge_caches_with_options(
        self,
        tmp_req: esa20240910_models.PurgeCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PurgeCachesResponse:
        """
        @summary 缓存刷新
        
        @param tmp_req: PurgeCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PurgeCachesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PurgeCachesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.edge_compute_purge):
            query['EdgeComputePurge'] = request.edge_compute_purge
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeCaches',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PurgeCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def purge_caches_with_options_async(
        self,
        tmp_req: esa20240910_models.PurgeCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PurgeCachesResponse:
        """
        @summary 缓存刷新
        
        @param tmp_req: PurgeCachesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PurgeCachesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.PurgeCachesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content):
            request.content_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content, 'Content', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_shrink):
            query['Content'] = request.content_shrink
        if not UtilClient.is_unset(request.edge_compute_purge):
            query['EdgeComputePurge'] = request.edge_compute_purge
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PurgeCaches',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PurgeCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def purge_caches(
        self,
        request: esa20240910_models.PurgeCachesRequest,
    ) -> esa20240910_models.PurgeCachesResponse:
        """
        @summary 缓存刷新
        
        @param request: PurgeCachesRequest
        @return: PurgeCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.purge_caches_with_options(request, runtime)

    async def purge_caches_async(
        self,
        request: esa20240910_models.PurgeCachesRequest,
    ) -> esa20240910_models.PurgeCachesResponse:
        """
        @summary 缓存刷新
        
        @param request: PurgeCachesRequest
        @return: PurgeCachesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.purge_caches_with_options_async(request, runtime)

    def put_kv_with_options(
        self,
        request: esa20240910_models.PutKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvResponse:
        """
        @summary 设置Namespace的Key-Value对
        
        @param request: PutKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutKvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_64):
            query['Base64'] = request.base_64
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PutKvResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_kv_with_options_async(
        self,
        request: esa20240910_models.PutKvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvResponse:
        """
        @summary 设置Namespace的Key-Value对
        
        @param request: PutKvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutKvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_64):
            query['Base64'] = request.base_64
        if not UtilClient.is_unset(request.expiration):
            query['Expiration'] = request.expiration
        if not UtilClient.is_unset(request.expiration_ttl):
            query['ExpirationTtl'] = request.expiration_ttl
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        body = {}
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PutKv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PutKvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_kv(
        self,
        request: esa20240910_models.PutKvRequest,
    ) -> esa20240910_models.PutKvResponse:
        """
        @summary 设置Namespace的Key-Value对
        
        @param request: PutKvRequest
        @return: PutKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_kv_with_options(request, runtime)

    async def put_kv_async(
        self,
        request: esa20240910_models.PutKvRequest,
    ) -> esa20240910_models.PutKvResponse:
        """
        @summary 设置Namespace的Key-Value对
        
        @param request: PutKvRequest
        @return: PutKvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_kv_with_options_async(request, runtime)

    def put_kv_with_high_capacity_with_options(
        self,
        request: esa20240910_models.PutKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        """
        @summary 设置Namespace的Key-Value对，支持最大25M的Body
        
        @param request: PutKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PutKvWithHighCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_kv_with_high_capacity_with_options_async(
        self,
        request: esa20240910_models.PutKvWithHighCapacityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        """
        @summary 设置Namespace的Key-Value对，支持最大25M的Body
        
        @param request: PutKvWithHighCapacityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutKvWithHighCapacityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutKvWithHighCapacity',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.PutKvWithHighCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_kv_with_high_capacity(
        self,
        request: esa20240910_models.PutKvWithHighCapacityRequest,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        """
        @summary 设置Namespace的Key-Value对，支持最大25M的Body
        
        @param request: PutKvWithHighCapacityRequest
        @return: PutKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_kv_with_high_capacity_with_options(request, runtime)

    async def put_kv_with_high_capacity_async(
        self,
        request: esa20240910_models.PutKvWithHighCapacityRequest,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        """
        @summary 设置Namespace的Key-Value对，支持最大25M的Body
        
        @param request: PutKvWithHighCapacityRequest
        @return: PutKvWithHighCapacityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_kv_with_high_capacity_with_options_async(request, runtime)

    def put_kv_with_high_capacity_advance(
        self,
        request: esa20240910_models.PutKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        put_kv_with_high_capacity_req = esa20240910_models.PutKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, put_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            put_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        put_kv_with_high_capacity_resp = self.put_kv_with_high_capacity_with_options(put_kv_with_high_capacity_req, runtime)
        return put_kv_with_high_capacity_resp

    async def put_kv_with_high_capacity_advance_async(
        self,
        request: esa20240910_models.PutKvWithHighCapacityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.PutKvWithHighCapacityResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        put_kv_with_high_capacity_req = esa20240910_models.PutKvWithHighCapacityRequest()
        OpenApiUtilClient.convert(request, put_kv_with_high_capacity_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            put_kv_with_high_capacity_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        put_kv_with_high_capacity_resp = await self.put_kv_with_high_capacity_with_options_async(put_kv_with_high_capacity_req, runtime)
        return put_kv_with_high_capacity_resp

    def rebuild_edge_container_app_staging_env_with_options(
        self,
        request: esa20240910_models.RebuildEdgeContainerAppStagingEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse:
        """
        @summary 重建边缘容器应用的测试环境
        
        @param request: RebuildEdgeContainerAppStagingEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildEdgeContainerAppStagingEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildEdgeContainerAppStagingEnv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_edge_container_app_staging_env_with_options_async(
        self,
        request: esa20240910_models.RebuildEdgeContainerAppStagingEnvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse:
        """
        @summary 重建边缘容器应用的测试环境
        
        @param request: RebuildEdgeContainerAppStagingEnvRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebuildEdgeContainerAppStagingEnvResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildEdgeContainerAppStagingEnv',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_edge_container_app_staging_env(
        self,
        request: esa20240910_models.RebuildEdgeContainerAppStagingEnvRequest,
    ) -> esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse:
        """
        @summary 重建边缘容器应用的测试环境
        
        @param request: RebuildEdgeContainerAppStagingEnvRequest
        @return: RebuildEdgeContainerAppStagingEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rebuild_edge_container_app_staging_env_with_options(request, runtime)

    async def rebuild_edge_container_app_staging_env_async(
        self,
        request: esa20240910_models.RebuildEdgeContainerAppStagingEnvRequest,
    ) -> esa20240910_models.RebuildEdgeContainerAppStagingEnvResponse:
        """
        @summary 重建边缘容器应用的测试环境
        
        @param request: RebuildEdgeContainerAppStagingEnvRequest
        @return: RebuildEdgeContainerAppStagingEnvResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_edge_container_app_staging_env_with_options_async(request, runtime)

    def reset_scheduled_preload_job_with_options(
        self,
        request: esa20240910_models.ResetScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ResetScheduledPreloadJobResponse:
        """
        @summary 重置定时预热任务的进度，从头开始预热
        
        @param request: ResetScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ResetScheduledPreloadJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_scheduled_preload_job_with_options_async(
        self,
        request: esa20240910_models.ResetScheduledPreloadJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.ResetScheduledPreloadJobResponse:
        """
        @summary 重置定时预热任务的进度，从头开始预热
        
        @param request: ResetScheduledPreloadJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetScheduledPreloadJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetScheduledPreloadJob',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.ResetScheduledPreloadJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_scheduled_preload_job(
        self,
        request: esa20240910_models.ResetScheduledPreloadJobRequest,
    ) -> esa20240910_models.ResetScheduledPreloadJobResponse:
        """
        @summary 重置定时预热任务的进度，从头开始预热
        
        @param request: ResetScheduledPreloadJobRequest
        @return: ResetScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_scheduled_preload_job_with_options(request, runtime)

    async def reset_scheduled_preload_job_async(
        self,
        request: esa20240910_models.ResetScheduledPreloadJobRequest,
    ) -> esa20240910_models.ResetScheduledPreloadJobResponse:
        """
        @summary 重置定时预热任务的进度，从头开始预热
        
        @param request: ResetScheduledPreloadJobRequest
        @return: ResetScheduledPreloadJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_scheduled_preload_job_with_options_async(request, runtime)

    def rollback_edge_container_app_version_with_options(
        self,
        request: esa20240910_models.RollbackEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.RollbackEdgeContainerAppVersionResponse:
        """
        @summary 回滚边缘容器应用的某个版本
        
        @param request: RollbackEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.RollbackEdgeContainerAppVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_edge_container_app_version_with_options_async(
        self,
        request: esa20240910_models.RollbackEdgeContainerAppVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.RollbackEdgeContainerAppVersionResponse:
        """
        @summary 回滚边缘容器应用的某个版本
        
        @param request: RollbackEdgeContainerAppVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackEdgeContainerAppVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.remarks):
            body['Remarks'] = request.remarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackEdgeContainerAppVersion',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.RollbackEdgeContainerAppVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_edge_container_app_version(
        self,
        request: esa20240910_models.RollbackEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.RollbackEdgeContainerAppVersionResponse:
        """
        @summary 回滚边缘容器应用的某个版本
        
        @param request: RollbackEdgeContainerAppVersionRequest
        @return: RollbackEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_edge_container_app_version_with_options(request, runtime)

    async def rollback_edge_container_app_version_async(
        self,
        request: esa20240910_models.RollbackEdgeContainerAppVersionRequest,
    ) -> esa20240910_models.RollbackEdgeContainerAppVersionResponse:
        """
        @summary 回滚边缘容器应用的某个版本
        
        @param request: RollbackEdgeContainerAppVersionRequest
        @return: RollbackEdgeContainerAppVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_edge_container_app_version_with_options_async(request, runtime)

    def set_certificate_with_options(
        self,
        request: esa20240910_models.SetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetCertificateResponse:
        """
        @summary 设置证书
        
        @param request: SetCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not UtilClient.is_unset(request.cas_id):
            body['CasId'] = request.cas_id
        if not UtilClient.is_unset(request.certificate):
            body['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.private_key):
            body['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.update):
            body['Update'] = request.update
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetCertificate',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_certificate_with_options_async(
        self,
        request: esa20240910_models.SetCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetCertificateResponse:
        """
        @summary 设置证书
        
        @param request: SetCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        body = {}
        if not UtilClient.is_unset(request.cas_id):
            body['CasId'] = request.cas_id
        if not UtilClient.is_unset(request.certificate):
            body['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.private_key):
            body['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region):
            body['Region'] = request.region
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.update):
            body['Update'] = request.update
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetCertificate',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_certificate(
        self,
        request: esa20240910_models.SetCertificateRequest,
    ) -> esa20240910_models.SetCertificateResponse:
        """
        @summary 设置证书
        
        @param request: SetCertificateRequest
        @return: SetCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_certificate_with_options(request, runtime)

    async def set_certificate_async(
        self,
        request: esa20240910_models.SetCertificateRequest,
    ) -> esa20240910_models.SetCertificateResponse:
        """
        @summary 设置证书
        
        @param request: SetCertificateRequest
        @return: SetCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_certificate_with_options_async(request, runtime)

    def set_http_ddo_sattack_intelligent_protection_with_options(
        self,
        request: esa20240910_models.SetHttpDDoSAttackIntelligentProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 设置HTTP DDoS智能防护配置信息
        
        @param request: SetHttpDDoSAttackIntelligentProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHttpDDoSAttackIntelligentProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ai_mode):
            query['AiMode'] = request.ai_mode
        if not UtilClient.is_unset(request.ai_template):
            query['AiTemplate'] = request.ai_template
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpDDoSAttackIntelligentProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_http_ddo_sattack_intelligent_protection_with_options_async(
        self,
        request: esa20240910_models.SetHttpDDoSAttackIntelligentProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 设置HTTP DDoS智能防护配置信息
        
        @param request: SetHttpDDoSAttackIntelligentProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHttpDDoSAttackIntelligentProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ai_mode):
            query['AiMode'] = request.ai_mode
        if not UtilClient.is_unset(request.ai_template):
            query['AiTemplate'] = request.ai_template
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpDDoSAttackIntelligentProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_http_ddo_sattack_intelligent_protection(
        self,
        request: esa20240910_models.SetHttpDDoSAttackIntelligentProtectionRequest,
    ) -> esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 设置HTTP DDoS智能防护配置信息
        
        @param request: SetHttpDDoSAttackIntelligentProtectionRequest
        @return: SetHttpDDoSAttackIntelligentProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_http_ddo_sattack_intelligent_protection_with_options(request, runtime)

    async def set_http_ddo_sattack_intelligent_protection_async(
        self,
        request: esa20240910_models.SetHttpDDoSAttackIntelligentProtectionRequest,
    ) -> esa20240910_models.SetHttpDDoSAttackIntelligentProtectionResponse:
        """
        @summary 设置HTTP DDoS智能防护配置信息
        
        @param request: SetHttpDDoSAttackIntelligentProtectionRequest
        @return: SetHttpDDoSAttackIntelligentProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_http_ddo_sattack_intelligent_protection_with_options_async(request, runtime)

    def set_http_ddo_sattack_protection_with_options(
        self,
        request: esa20240910_models.SetHttpDDoSAttackProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetHttpDDoSAttackProtectionResponse:
        """
        @summary 设置HTTP DDoS攻击防护配置信息
        
        @param request: SetHttpDDoSAttackProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHttpDDoSAttackProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_mode):
            query['GlobalMode'] = request.global_mode
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpDDoSAttackProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetHttpDDoSAttackProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_http_ddo_sattack_protection_with_options_async(
        self,
        request: esa20240910_models.SetHttpDDoSAttackProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.SetHttpDDoSAttackProtectionResponse:
        """
        @summary 设置HTTP DDoS攻击防护配置信息
        
        @param request: SetHttpDDoSAttackProtectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetHttpDDoSAttackProtectionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_mode):
            query['GlobalMode'] = request.global_mode
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetHttpDDoSAttackProtection',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.SetHttpDDoSAttackProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_http_ddo_sattack_protection(
        self,
        request: esa20240910_models.SetHttpDDoSAttackProtectionRequest,
    ) -> esa20240910_models.SetHttpDDoSAttackProtectionResponse:
        """
        @summary 设置HTTP DDoS攻击防护配置信息
        
        @param request: SetHttpDDoSAttackProtectionRequest
        @return: SetHttpDDoSAttackProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_http_ddo_sattack_protection_with_options(request, runtime)

    async def set_http_ddo_sattack_protection_async(
        self,
        request: esa20240910_models.SetHttpDDoSAttackProtectionRequest,
    ) -> esa20240910_models.SetHttpDDoSAttackProtectionResponse:
        """
        @summary 设置HTTP DDoS攻击防护配置信息
        
        @param request: SetHttpDDoSAttackProtectionRequest
        @return: SetHttpDDoSAttackProtectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_http_ddo_sattack_protection_with_options_async(request, runtime)

    def start_scheduled_preload_execution_with_options(
        self,
        request: esa20240910_models.StartScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.StartScheduledPreloadExecutionResponse:
        """
        @summary 开始单个定时预热计划
        
        @param request: StartScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.StartScheduledPreloadExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_scheduled_preload_execution_with_options_async(
        self,
        request: esa20240910_models.StartScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.StartScheduledPreloadExecutionResponse:
        """
        @summary 开始单个定时预热计划
        
        @param request: StartScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.StartScheduledPreloadExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_scheduled_preload_execution(
        self,
        request: esa20240910_models.StartScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.StartScheduledPreloadExecutionResponse:
        """
        @summary 开始单个定时预热计划
        
        @param request: StartScheduledPreloadExecutionRequest
        @return: StartScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_scheduled_preload_execution_with_options(request, runtime)

    async def start_scheduled_preload_execution_async(
        self,
        request: esa20240910_models.StartScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.StartScheduledPreloadExecutionResponse:
        """
        @summary 开始单个定时预热计划
        
        @param request: StartScheduledPreloadExecutionRequest
        @return: StartScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_scheduled_preload_execution_with_options_async(request, runtime)

    def stop_scheduled_preload_execution_with_options(
        self,
        request: esa20240910_models.StopScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.StopScheduledPreloadExecutionResponse:
        """
        @summary 停止单个定时预热计划
        
        @param request: StopScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.StopScheduledPreloadExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_scheduled_preload_execution_with_options_async(
        self,
        request: esa20240910_models.StopScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.StopScheduledPreloadExecutionResponse:
        """
        @summary 停止单个定时预热计划
        
        @param request: StopScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.StopScheduledPreloadExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_scheduled_preload_execution(
        self,
        request: esa20240910_models.StopScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.StopScheduledPreloadExecutionResponse:
        """
        @summary 停止单个定时预热计划
        
        @param request: StopScheduledPreloadExecutionRequest
        @return: StopScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_scheduled_preload_execution_with_options(request, runtime)

    async def stop_scheduled_preload_execution_async(
        self,
        request: esa20240910_models.StopScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.StopScheduledPreloadExecutionResponse:
        """
        @summary 停止单个定时预热计划
        
        @param request: StopScheduledPreloadExecutionRequest
        @return: StopScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_scheduled_preload_execution_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: esa20240910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UntagResourcesResponse:
        """
        @summary 为资源列表统一解绑标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: esa20240910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UntagResourcesResponse:
        """
        @summary 为资源列表统一解绑标签
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: esa20240910_models.UntagResourcesRequest,
    ) -> esa20240910_models.UntagResourcesResponse:
        """
        @summary 为资源列表统一解绑标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: esa20240910_models.UntagResourcesRequest,
    ) -> esa20240910_models.UntagResourcesResponse:
        """
        @summary 为资源列表统一解绑标签
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_custom_scene_policy_with_options(
        self,
        request: esa20240910_models.UpdateCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateCustomScenePolicyResponse:
        """
        @summary 修改定制场景策略
        
        @param request: UpdateCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateCustomScenePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_scene_policy_with_options_async(
        self,
        request: esa20240910_models.UpdateCustomScenePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateCustomScenePolicyResponse:
        """
        @summary 修改定制场景策略
        
        @param request: UpdateCustomScenePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCustomScenePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.objects):
            query['Objects'] = request.objects
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomScenePolicy',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateCustomScenePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_scene_policy(
        self,
        request: esa20240910_models.UpdateCustomScenePolicyRequest,
    ) -> esa20240910_models.UpdateCustomScenePolicyResponse:
        """
        @summary 修改定制场景策略
        
        @param request: UpdateCustomScenePolicyRequest
        @return: UpdateCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_custom_scene_policy_with_options(request, runtime)

    async def update_custom_scene_policy_async(
        self,
        request: esa20240910_models.UpdateCustomScenePolicyRequest,
    ) -> esa20240910_models.UpdateCustomScenePolicyResponse:
        """
        @summary 修改定制场景策略
        
        @param request: UpdateCustomScenePolicyRequest
        @return: UpdateCustomScenePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_scene_policy_with_options_async(request, runtime)

    def update_kv_namespace_with_options(
        self,
        request: esa20240910_models.UpdateKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateKvNamespaceResponse:
        """
        @summary 重命名账号下的Namespace
        
        @param request: UpdateKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateKvNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kv_namespace_with_options_async(
        self,
        request: esa20240910_models.UpdateKvNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateKvNamespaceResponse:
        """
        @summary 重命名账号下的Namespace
        
        @param request: UpdateKvNamespaceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKvNamespaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateKvNamespace',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateKvNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kv_namespace(
        self,
        request: esa20240910_models.UpdateKvNamespaceRequest,
    ) -> esa20240910_models.UpdateKvNamespaceResponse:
        """
        @summary 重命名账号下的Namespace
        
        @param request: UpdateKvNamespaceRequest
        @return: UpdateKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_kv_namespace_with_options(request, runtime)

    async def update_kv_namespace_async(
        self,
        request: esa20240910_models.UpdateKvNamespaceRequest,
    ) -> esa20240910_models.UpdateKvNamespaceResponse:
        """
        @summary 重命名账号下的Namespace
        
        @param request: UpdateKvNamespaceRequest
        @return: UpdateKvNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_kv_namespace_with_options_async(request, runtime)

    def update_list_with_options(
        self,
        tmp_req: esa20240910_models.UpdateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateListResponse:
        """
        @summary 更新自定义列表
        
        @param tmp_req: UpdateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.items):
            request.items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.items_shrink):
            body['Items'] = request.items_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_list_with_options_async(
        self,
        tmp_req: esa20240910_models.UpdateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateListResponse:
        """
        @summary 更新自定义列表
        
        @param tmp_req: UpdateListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.items):
            request.items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.items, 'Items', 'json')
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.items_shrink):
            body['Items'] = request.items_shrink
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateList',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_list(
        self,
        request: esa20240910_models.UpdateListRequest,
    ) -> esa20240910_models.UpdateListResponse:
        """
        @summary 更新自定义列表
        
        @param request: UpdateListRequest
        @return: UpdateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_list_with_options(request, runtime)

    async def update_list_async(
        self,
        request: esa20240910_models.UpdateListRequest,
    ) -> esa20240910_models.UpdateListResponse:
        """
        @summary 更新自定义列表
        
        @param request: UpdateListRequest
        @return: UpdateListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_list_with_options_async(request, runtime)

    def update_page_with_options(
        self,
        request: esa20240910_models.UpdatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdatePageResponse:
        """
        @summary 更新自定义响应页面
        
        @param request: UpdatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdatePageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_page_with_options_async(
        self,
        request: esa20240910_models.UpdatePageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdatePageResponse:
        """
        @summary 更新自定义响应页面
        
        @param request: UpdatePageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePageResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdatePageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_page(
        self,
        request: esa20240910_models.UpdatePageRequest,
    ) -> esa20240910_models.UpdatePageResponse:
        """
        @summary 更新自定义响应页面
        
        @param request: UpdatePageRequest
        @return: UpdatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_page_with_options(request, runtime)

    async def update_page_async(
        self,
        request: esa20240910_models.UpdatePageRequest,
    ) -> esa20240910_models.UpdatePageResponse:
        """
        @summary 更新自定义响应页面
        
        @param request: UpdatePageRequest
        @return: UpdatePageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_page_with_options_async(request, runtime)

    def update_record_with_options(
        self,
        tmp_req: esa20240910_models.UpdateRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateRecordResponse:
        """
        @summary 更新记录
        
        @param tmp_req: UpdateRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_conf):
            request.auth_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_conf, 'AuthConf', 'json')
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_conf_shrink):
            query['AuthConf'] = request.auth_conf_shrink
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.host_policy):
            query['HostPolicy'] = request.host_policy
        if not UtilClient.is_unset(request.proxied):
            query['Proxied'] = request.proxied
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_record_with_options_async(
        self,
        tmp_req: esa20240910_models.UpdateRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateRecordResponse:
        """
        @summary 更新记录
        
        @param tmp_req: UpdateRecordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRecordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateRecordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auth_conf):
            request.auth_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auth_conf, 'AuthConf', 'json')
        if not UtilClient.is_unset(tmp_req.data):
            request.data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data, 'Data', 'json')
        query = {}
        if not UtilClient.is_unset(request.auth_conf_shrink):
            query['AuthConf'] = request.auth_conf_shrink
        if not UtilClient.is_unset(request.biz_name):
            query['BizName'] = request.biz_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.data_shrink):
            query['Data'] = request.data_shrink
        if not UtilClient.is_unset(request.host_policy):
            query['HostPolicy'] = request.host_policy
        if not UtilClient.is_unset(request.proxied):
            query['Proxied'] = request.proxied
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.ttl):
            query['Ttl'] = request.ttl
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecord',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_record(
        self,
        request: esa20240910_models.UpdateRecordRequest,
    ) -> esa20240910_models.UpdateRecordResponse:
        """
        @summary 更新记录
        
        @param request: UpdateRecordRequest
        @return: UpdateRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_record_with_options(request, runtime)

    async def update_record_async(
        self,
        request: esa20240910_models.UpdateRecordRequest,
    ) -> esa20240910_models.UpdateRecordResponse:
        """
        @summary 更新记录
        
        @param request: UpdateRecordRequest
        @return: UpdateRecordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_record_with_options_async(request, runtime)

    def update_scheduled_preload_execution_with_options(
        self,
        request: esa20240910_models.UpdateScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateScheduledPreloadExecutionResponse:
        """
        @summary 更新单个定时预热计划
        
        @param request: UpdateScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            body['Interval'] = request.interval
        if not UtilClient.is_unset(request.slice_len):
            body['SliceLen'] = request.slice_len
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateScheduledPreloadExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheduled_preload_execution_with_options_async(
        self,
        request: esa20240910_models.UpdateScheduledPreloadExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateScheduledPreloadExecutionResponse:
        """
        @summary 更新单个定时预热计划
        
        @param request: UpdateScheduledPreloadExecutionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScheduledPreloadExecutionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            body['Interval'] = request.interval
        if not UtilClient.is_unset(request.slice_len):
            body['SliceLen'] = request.slice_len
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScheduledPreloadExecution',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateScheduledPreloadExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheduled_preload_execution(
        self,
        request: esa20240910_models.UpdateScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.UpdateScheduledPreloadExecutionResponse:
        """
        @summary 更新单个定时预热计划
        
        @param request: UpdateScheduledPreloadExecutionRequest
        @return: UpdateScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_scheduled_preload_execution_with_options(request, runtime)

    async def update_scheduled_preload_execution_async(
        self,
        request: esa20240910_models.UpdateScheduledPreloadExecutionRequest,
    ) -> esa20240910_models.UpdateScheduledPreloadExecutionResponse:
        """
        @summary 更新单个定时预热计划
        
        @param request: UpdateScheduledPreloadExecutionRequest
        @return: UpdateScheduledPreloadExecutionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_scheduled_preload_execution_with_options_async(request, runtime)

    def update_site_access_type_with_options(
        self,
        request: esa20240910_models.UpdateSiteAccessTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteAccessTypeResponse:
        """
        @summary 修改站点接入方式
        
        @param request: UpdateSiteAccessTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteAccessTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteAccessType',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteAccessTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_access_type_with_options_async(
        self,
        request: esa20240910_models.UpdateSiteAccessTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteAccessTypeResponse:
        """
        @summary 修改站点接入方式
        
        @param request: UpdateSiteAccessTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteAccessTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteAccessType',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteAccessTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_access_type(
        self,
        request: esa20240910_models.UpdateSiteAccessTypeRequest,
    ) -> esa20240910_models.UpdateSiteAccessTypeResponse:
        """
        @summary 修改站点接入方式
        
        @param request: UpdateSiteAccessTypeRequest
        @return: UpdateSiteAccessTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_access_type_with_options(request, runtime)

    async def update_site_access_type_async(
        self,
        request: esa20240910_models.UpdateSiteAccessTypeRequest,
    ) -> esa20240910_models.UpdateSiteAccessTypeResponse:
        """
        @summary 修改站点接入方式
        
        @param request: UpdateSiteAccessTypeRequest
        @return: UpdateSiteAccessTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_access_type_with_options_async(request, runtime)

    def update_site_coverage_with_options(
        self,
        request: esa20240910_models.UpdateSiteCoverageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteCoverageResponse:
        """
        @summary 更新站点加速区域
        
        @param request: UpdateSiteCoverageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteCoverageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteCoverage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteCoverageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_coverage_with_options_async(
        self,
        request: esa20240910_models.UpdateSiteCoverageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteCoverageResponse:
        """
        @summary 更新站点加速区域
        
        @param request: UpdateSiteCoverageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteCoverageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.coverage):
            query['Coverage'] = request.coverage
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteCoverage',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteCoverageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_coverage(
        self,
        request: esa20240910_models.UpdateSiteCoverageRequest,
    ) -> esa20240910_models.UpdateSiteCoverageResponse:
        """
        @summary 更新站点加速区域
        
        @param request: UpdateSiteCoverageRequest
        @return: UpdateSiteCoverageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_coverage_with_options(request, runtime)

    async def update_site_coverage_async(
        self,
        request: esa20240910_models.UpdateSiteCoverageRequest,
    ) -> esa20240910_models.UpdateSiteCoverageResponse:
        """
        @summary 更新站点加速区域
        
        @param request: UpdateSiteCoverageRequest
        @return: UpdateSiteCoverageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_coverage_with_options_async(request, runtime)

    def update_site_custom_log_with_options(
        self,
        tmp_req: esa20240910_models.UpdateSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteCustomLogResponse:
        """
        @summary 修改自定义字段
        
        @param tmp_req: UpdateSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteCustomLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateSiteCustomLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cookies):
            request.cookies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cookies, 'Cookies', 'json')
        if not UtilClient.is_unset(tmp_req.request_headers):
            request.request_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_headers, 'RequestHeaders', 'json')
        if not UtilClient.is_unset(tmp_req.response_headers):
            request.response_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.response_headers, 'ResponseHeaders', 'json')
        body = {}
        if not UtilClient.is_unset(request.cookies_shrink):
            body['Cookies'] = request.cookies_shrink
        if not UtilClient.is_unset(request.request_headers_shrink):
            body['RequestHeaders'] = request.request_headers_shrink
        if not UtilClient.is_unset(request.response_headers_shrink):
            body['ResponseHeaders'] = request.response_headers_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteCustomLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_custom_log_with_options_async(
        self,
        tmp_req: esa20240910_models.UpdateSiteCustomLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteCustomLogResponse:
        """
        @summary 修改自定义字段
        
        @param tmp_req: UpdateSiteCustomLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteCustomLogResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateSiteCustomLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cookies):
            request.cookies_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cookies, 'Cookies', 'json')
        if not UtilClient.is_unset(tmp_req.request_headers):
            request.request_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.request_headers, 'RequestHeaders', 'json')
        if not UtilClient.is_unset(tmp_req.response_headers):
            request.response_headers_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.response_headers, 'ResponseHeaders', 'json')
        body = {}
        if not UtilClient.is_unset(request.cookies_shrink):
            body['Cookies'] = request.cookies_shrink
        if not UtilClient.is_unset(request.request_headers_shrink):
            body['RequestHeaders'] = request.request_headers_shrink
        if not UtilClient.is_unset(request.response_headers_shrink):
            body['ResponseHeaders'] = request.response_headers_shrink
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSiteCustomLog',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteCustomLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_custom_log(
        self,
        request: esa20240910_models.UpdateSiteCustomLogRequest,
    ) -> esa20240910_models.UpdateSiteCustomLogResponse:
        """
        @summary 修改自定义字段
        
        @param request: UpdateSiteCustomLogRequest
        @return: UpdateSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_custom_log_with_options(request, runtime)

    async def update_site_custom_log_async(
        self,
        request: esa20240910_models.UpdateSiteCustomLogRequest,
    ) -> esa20240910_models.UpdateSiteCustomLogResponse:
        """
        @summary 修改自定义字段
        
        @param request: UpdateSiteCustomLogRequest
        @return: UpdateSiteCustomLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_custom_log_with_options_async(request, runtime)

    def update_site_delivery_task_with_options(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskResponse:
        """
        @summary 修改一个任务投递
        
        @param request: UpdateSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_delivery_task_with_options_async(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskResponse:
        """
        @summary 修改一个任务投递
        
        @param request: UpdateSiteDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.site_id):
            body['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSiteDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_delivery_task(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskRequest,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskResponse:
        """
        @summary 修改一个任务投递
        
        @param request: UpdateSiteDeliveryTaskRequest
        @return: UpdateSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_delivery_task_with_options(request, runtime)

    async def update_site_delivery_task_async(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskRequest,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskResponse:
        """
        @summary 修改一个任务投递
        
        @param request: UpdateSiteDeliveryTaskRequest
        @return: UpdateSiteDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_delivery_task_with_options_async(request, runtime)

    def update_site_delivery_task_status_with_options(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskStatusResponse:
        """
        @summary 上下线一个任务投递
        
        @param request: UpdateSiteDeliveryTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteDeliveryTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteDeliveryTaskStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteDeliveryTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_delivery_task_status_with_options_async(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskStatusResponse:
        """
        @summary 上下线一个任务投递
        
        @param request: UpdateSiteDeliveryTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteDeliveryTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteDeliveryTaskStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteDeliveryTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_delivery_task_status(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskStatusRequest,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskStatusResponse:
        """
        @summary 上下线一个任务投递
        
        @param request: UpdateSiteDeliveryTaskStatusRequest
        @return: UpdateSiteDeliveryTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_delivery_task_status_with_options(request, runtime)

    async def update_site_delivery_task_status_async(
        self,
        request: esa20240910_models.UpdateSiteDeliveryTaskStatusRequest,
    ) -> esa20240910_models.UpdateSiteDeliveryTaskStatusResponse:
        """
        @summary 上下线一个任务投递
        
        @param request: UpdateSiteDeliveryTaskStatusRequest
        @return: UpdateSiteDeliveryTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_delivery_task_status_with_options_async(request, runtime)

    def update_site_vanity_nswith_options(
        self,
        request: esa20240910_models.UpdateSiteVanityNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteVanityNSResponse:
        """
        @summary 修改站点自定义NS
        
        @param request: UpdateSiteVanityNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteVanityNSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.vanity_nslist):
            query['VanityNSList'] = request.vanity_nslist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteVanityNS',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteVanityNSResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_site_vanity_nswith_options_async(
        self,
        request: esa20240910_models.UpdateSiteVanityNSRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateSiteVanityNSResponse:
        """
        @summary 修改站点自定义NS
        
        @param request: UpdateSiteVanityNSRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSiteVanityNSResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.vanity_nslist):
            query['VanityNSList'] = request.vanity_nslist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSiteVanityNS',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateSiteVanityNSResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_site_vanity_ns(
        self,
        request: esa20240910_models.UpdateSiteVanityNSRequest,
    ) -> esa20240910_models.UpdateSiteVanityNSResponse:
        """
        @summary 修改站点自定义NS
        
        @param request: UpdateSiteVanityNSRequest
        @return: UpdateSiteVanityNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_site_vanity_nswith_options(request, runtime)

    async def update_site_vanity_ns_async(
        self,
        request: esa20240910_models.UpdateSiteVanityNSRequest,
    ) -> esa20240910_models.UpdateSiteVanityNSResponse:
        """
        @summary 修改站点自定义NS
        
        @param request: UpdateSiteVanityNSRequest
        @return: UpdateSiteVanityNSResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_site_vanity_nswith_options_async(request, runtime)

    def update_user_delivery_task_with_options(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateUserDeliveryTaskResponse:
        """
        @summary 修改一个用户粒度任务投递
        
        @param request: UpdateUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateUserDeliveryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_delivery_task_with_options_async(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateUserDeliveryTaskResponse:
        """
        @summary 修改一个用户粒度任务投递
        
        @param request: UpdateUserDeliveryTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDeliveryTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.business_type):
            body['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.discard_rate):
            body['DiscardRate'] = request.discard_rate
        if not UtilClient.is_unset(request.field_name):
            body['FieldName'] = request.field_name
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserDeliveryTask',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateUserDeliveryTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_delivery_task(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskRequest,
    ) -> esa20240910_models.UpdateUserDeliveryTaskResponse:
        """
        @summary 修改一个用户粒度任务投递
        
        @param request: UpdateUserDeliveryTaskRequest
        @return: UpdateUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_delivery_task_with_options(request, runtime)

    async def update_user_delivery_task_async(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskRequest,
    ) -> esa20240910_models.UpdateUserDeliveryTaskResponse:
        """
        @summary 修改一个用户粒度任务投递
        
        @param request: UpdateUserDeliveryTaskRequest
        @return: UpdateUserDeliveryTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_delivery_task_with_options_async(request, runtime)

    def update_user_delivery_task_status_with_options(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateUserDeliveryTaskStatusResponse:
        """
        @summary 上下线一个用户任务投递
        
        @param request: UpdateUserDeliveryTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDeliveryTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserDeliveryTaskStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateUserDeliveryTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_delivery_task_status_with_options_async(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateUserDeliveryTaskStatusResponse:
        """
        @summary 上下线一个用户任务投递
        
        @param request: UpdateUserDeliveryTaskStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserDeliveryTaskStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserDeliveryTaskStatus',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateUserDeliveryTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_delivery_task_status(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskStatusRequest,
    ) -> esa20240910_models.UpdateUserDeliveryTaskStatusResponse:
        """
        @summary 上下线一个用户任务投递
        
        @param request: UpdateUserDeliveryTaskStatusRequest
        @return: UpdateUserDeliveryTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_delivery_task_status_with_options(request, runtime)

    async def update_user_delivery_task_status_async(
        self,
        request: esa20240910_models.UpdateUserDeliveryTaskStatusRequest,
    ) -> esa20240910_models.UpdateUserDeliveryTaskStatusResponse:
        """
        @summary 上下线一个用户任务投递
        
        @param request: UpdateUserDeliveryTaskStatusRequest
        @return: UpdateUserDeliveryTaskStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_delivery_task_status_with_options_async(request, runtime)

    def update_waf_rule_with_options(
        self,
        tmp_req: esa20240910_models.UpdateWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWafRuleResponse:
        """
        @summary 更新WAF规则页面
        
        @param tmp_req: UpdateWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWafRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateWafRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.position):
            body['Position'] = request.position
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWafRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waf_rule_with_options_async(
        self,
        tmp_req: esa20240910_models.UpdateWafRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWafRuleResponse:
        """
        @summary 更新WAF规则页面
        
        @param tmp_req: UpdateWafRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWafRuleResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateWafRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.position):
            body['Position'] = request.position
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWafRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWafRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waf_rule(
        self,
        request: esa20240910_models.UpdateWafRuleRequest,
    ) -> esa20240910_models.UpdateWafRuleResponse:
        """
        @summary 更新WAF规则页面
        
        @param request: UpdateWafRuleRequest
        @return: UpdateWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waf_rule_with_options(request, runtime)

    async def update_waf_rule_async(
        self,
        request: esa20240910_models.UpdateWafRuleRequest,
    ) -> esa20240910_models.UpdateWafRuleResponse:
        """
        @summary 更新WAF规则页面
        
        @param request: UpdateWafRuleRequest
        @return: UpdateWafRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waf_rule_with_options_async(request, runtime)

    def update_waf_ruleset_with_options(
        self,
        request: esa20240910_models.UpdateWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWafRulesetResponse:
        """
        @summary 更新WAF规则集
        
        @param request: UpdateWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWafRulesetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waf_ruleset_with_options_async(
        self,
        request: esa20240910_models.UpdateWafRulesetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWafRulesetResponse:
        """
        @summary 更新WAF规则集
        
        @param request: UpdateWafRulesetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWafRulesetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.site_version):
            query['SiteVersion'] = request.site_version
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWafRuleset',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWafRulesetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waf_ruleset(
        self,
        request: esa20240910_models.UpdateWafRulesetRequest,
    ) -> esa20240910_models.UpdateWafRulesetResponse:
        """
        @summary 更新WAF规则集
        
        @param request: UpdateWafRulesetRequest
        @return: UpdateWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waf_ruleset_with_options(request, runtime)

    async def update_waf_ruleset_async(
        self,
        request: esa20240910_models.UpdateWafRulesetRequest,
    ) -> esa20240910_models.UpdateWafRulesetResponse:
        """
        @summary 更新WAF规则集
        
        @param request: UpdateWafRulesetRequest
        @return: UpdateWafRulesetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waf_ruleset_with_options_async(request, runtime)

    def update_waiting_room_with_options(
        self,
        tmp_req: esa20240910_models.UpdateWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomResponse:
        """
        @summary 修改等候室
        
        @param tmp_req: UpdateWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateWaitingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.host_name_and_path):
            request.host_name_and_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name_and_path, 'HostNameAndPath', 'json')
        query = {}
        if not UtilClient.is_unset(request.cookie_name):
            query['CookieName'] = request.cookie_name
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.host_name_and_path_shrink):
            query['HostNameAndPath'] = request.host_name_and_path_shrink
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.queue_all_enable):
            query['QueueAllEnable'] = request.queue_all_enable
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waiting_room_with_options_async(
        self,
        tmp_req: esa20240910_models.UpdateWaitingRoomRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomResponse:
        """
        @summary 修改等候室
        
        @param tmp_req: UpdateWaitingRoomRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomResponse
        """
        UtilClient.validate_model(tmp_req)
        request = esa20240910_models.UpdateWaitingRoomShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.host_name_and_path):
            request.host_name_and_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.host_name_and_path, 'HostNameAndPath', 'json')
        query = {}
        if not UtilClient.is_unset(request.cookie_name):
            query['CookieName'] = request.cookie_name
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.host_name_and_path_shrink):
            query['HostNameAndPath'] = request.host_name_and_path_shrink
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.queue_all_enable):
            query['QueueAllEnable'] = request.queue_all_enable
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_id):
            query['WaitingRoomId'] = request.waiting_room_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoom',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waiting_room(
        self,
        request: esa20240910_models.UpdateWaitingRoomRequest,
    ) -> esa20240910_models.UpdateWaitingRoomResponse:
        """
        @summary 修改等候室
        
        @param request: UpdateWaitingRoomRequest
        @return: UpdateWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waiting_room_with_options(request, runtime)

    async def update_waiting_room_async(
        self,
        request: esa20240910_models.UpdateWaitingRoomRequest,
    ) -> esa20240910_models.UpdateWaitingRoomResponse:
        """
        @summary 修改等候室
        
        @param request: UpdateWaitingRoomRequest
        @return: UpdateWaitingRoomResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waiting_room_with_options_async(request, runtime)

    def update_waiting_room_event_with_options(
        self,
        request: esa20240910_models.UpdateWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomEventResponse:
        """
        @summary 修改等候室事件
        
        @param request: UpdateWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.pre_queue_enable):
            query['PreQueueEnable'] = request.pre_queue_enable
        if not UtilClient.is_unset(request.pre_queue_start_time):
            query['PreQueueStartTime'] = request.pre_queue_start_time
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.random_pre_queue_enable):
            query['RandomPreQueueEnable'] = request.random_pre_queue_enable
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_event_id):
            query['WaitingRoomEventId'] = request.waiting_room_event_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waiting_room_event_with_options_async(
        self,
        request: esa20240910_models.UpdateWaitingRoomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomEventResponse:
        """
        @summary 修改等候室事件
        
        @param request: UpdateWaitingRoomEventRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomEventResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_page_html):
            query['CustomPageHtml'] = request.custom_page_html
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_session_renewal_enable):
            query['DisableSessionRenewalEnable'] = request.disable_session_renewal_enable
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.json_response_enable):
            query['JsonResponseEnable'] = request.json_response_enable
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.new_users_per_minute):
            query['NewUsersPerMinute'] = request.new_users_per_minute
        if not UtilClient.is_unset(request.pre_queue_enable):
            query['PreQueueEnable'] = request.pre_queue_enable
        if not UtilClient.is_unset(request.pre_queue_start_time):
            query['PreQueueStartTime'] = request.pre_queue_start_time
        if not UtilClient.is_unset(request.queuing_method):
            query['QueuingMethod'] = request.queuing_method
        if not UtilClient.is_unset(request.queuing_status_code):
            query['QueuingStatusCode'] = request.queuing_status_code
        if not UtilClient.is_unset(request.random_pre_queue_enable):
            query['RandomPreQueueEnable'] = request.random_pre_queue_enable
        if not UtilClient.is_unset(request.session_duration):
            query['SessionDuration'] = request.session_duration
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.total_active_users):
            query['TotalActiveUsers'] = request.total_active_users
        if not UtilClient.is_unset(request.waiting_room_event_id):
            query['WaitingRoomEventId'] = request.waiting_room_event_id
        if not UtilClient.is_unset(request.waiting_room_type):
            query['WaitingRoomType'] = request.waiting_room_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoomEvent',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waiting_room_event(
        self,
        request: esa20240910_models.UpdateWaitingRoomEventRequest,
    ) -> esa20240910_models.UpdateWaitingRoomEventResponse:
        """
        @summary 修改等候室事件
        
        @param request: UpdateWaitingRoomEventRequest
        @return: UpdateWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waiting_room_event_with_options(request, runtime)

    async def update_waiting_room_event_async(
        self,
        request: esa20240910_models.UpdateWaitingRoomEventRequest,
    ) -> esa20240910_models.UpdateWaitingRoomEventResponse:
        """
        @summary 修改等候室事件
        
        @param request: UpdateWaitingRoomEventRequest
        @return: UpdateWaitingRoomEventResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waiting_room_event_with_options_async(request, runtime)

    def update_waiting_room_rule_with_options(
        self,
        request: esa20240910_models.UpdateWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomRuleResponse:
        """
        @summary 修改等候室规则
        
        @param request: UpdateWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_enable):
            query['RuleEnable'] = request.rule_enable
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_rule_id):
            query['WaitingRoomRuleId'] = request.waiting_room_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_waiting_room_rule_with_options_async(
        self,
        request: esa20240910_models.UpdateWaitingRoomRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UpdateWaitingRoomRuleResponse:
        """
        @summary 修改等候室规则
        
        @param request: UpdateWaitingRoomRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWaitingRoomRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_enable):
            query['RuleEnable'] = request.rule_enable
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.waiting_room_rule_id):
            query['WaitingRoomRuleId'] = request.waiting_room_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWaitingRoomRule',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UpdateWaitingRoomRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_waiting_room_rule(
        self,
        request: esa20240910_models.UpdateWaitingRoomRuleRequest,
    ) -> esa20240910_models.UpdateWaitingRoomRuleResponse:
        """
        @summary 修改等候室规则
        
        @param request: UpdateWaitingRoomRuleRequest
        @return: UpdateWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_waiting_room_rule_with_options(request, runtime)

    async def update_waiting_room_rule_async(
        self,
        request: esa20240910_models.UpdateWaitingRoomRuleRequest,
    ) -> esa20240910_models.UpdateWaitingRoomRuleResponse:
        """
        @summary 修改等候室规则
        
        @param request: UpdateWaitingRoomRuleRequest
        @return: UpdateWaitingRoomRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_waiting_room_rule_with_options_async(request, runtime)

    def upload_file_with_options(
        self,
        request: esa20240910_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UploadFileResponse:
        """
        @summary 缓存刷新文件上传
        
        @param request: UploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.upload_task_name):
            query['UploadTaskName'] = request.upload_task_name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFile',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_file_with_options_async(
        self,
        request: esa20240910_models.UploadFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UploadFileResponse:
        """
        @summary 缓存刷新文件上传
        
        @param request: UploadFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.upload_task_name):
            query['UploadTaskName'] = request.upload_task_name
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadFile',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.UploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_file(
        self,
        request: esa20240910_models.UploadFileRequest,
    ) -> esa20240910_models.UploadFileResponse:
        """
        @summary 缓存刷新文件上传
        
        @param request: UploadFileRequest
        @return: UploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    async def upload_file_async(
        self,
        request: esa20240910_models.UploadFileRequest,
    ) -> esa20240910_models.UploadFileResponse:
        """
        @summary 缓存刷新文件上传
        
        @param request: UploadFileRequest
        @return: UploadFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_file_with_options_async(request, runtime)

    def upload_file_advance(
        self,
        request: esa20240910_models.UploadFileAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UploadFileResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_file_req = esa20240910_models.UploadFileRequest()
        OpenApiUtilClient.convert(request, upload_file_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            upload_file_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_file_resp = self.upload_file_with_options(upload_file_req, runtime)
        return upload_file_resp

    async def upload_file_advance_async(
        self,
        request: esa20240910_models.UploadFileAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.UploadFileResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.empty(open_platform_endpoint):
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
            product='ESA',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_file_req = esa20240910_models.UploadFileRequest()
        OpenApiUtilClient.convert(request, upload_file_req)
        if not UtilClient.is_unset(request.url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.url_object,
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
            upload_file_req.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_file_resp = await self.upload_file_with_options_async(upload_file_req, runtime)
        return upload_file_resp

    def verify_site_with_options(
        self,
        request: esa20240910_models.VerifySiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.VerifySiteResponse:
        """
        @summary 校验站点的归属
        
        @param request: VerifySiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.VerifySiteResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_site_with_options_async(
        self,
        request: esa20240910_models.VerifySiteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> esa20240910_models.VerifySiteResponse:
        """
        @summary 校验站点的归属
        
        @param request: VerifySiteRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySiteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.site_id):
            query['SiteId'] = request.site_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySite',
            version='2024-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            esa20240910_models.VerifySiteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_site(
        self,
        request: esa20240910_models.VerifySiteRequest,
    ) -> esa20240910_models.VerifySiteResponse:
        """
        @summary 校验站点的归属
        
        @param request: VerifySiteRequest
        @return: VerifySiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_site_with_options(request, runtime)

    async def verify_site_async(
        self,
        request: esa20240910_models.VerifySiteRequest,
    ) -> esa20240910_models.VerifySiteResponse:
        """
        @summary 校验站点的归属
        
        @param request: VerifySiteRequest
        @return: VerifySiteResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_site_with_options_async(request, runtime)
