# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imageaudit20191230 import models as imageaudit_20191230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_darabonba_number.client import Client as NumberClient


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
        self._endpoint = self.get_endpoint('imageaudit', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def scan_image_with_options(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanImage',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageaudit_20191230_models.ScanImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_image_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanImage',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageaudit_20191230_models.ScanImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_image(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_image_with_options(request, runtime)

    async def scan_image_async(
        self,
        request: imageaudit_20191230_models.ScanImageRequest,
    ) -> imageaudit_20191230_models.ScanImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_image_with_options_async(request, runtime)

    def scan_image_advance(
        self,
        request: imageaudit_20191230_models.ScanImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
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
            product='imageaudit',
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
        scan_image_req = imageaudit_20191230_models.ScanImageRequest()
        OpenApiUtilClient.convert(request, scan_image_req)
        if not UtilClient.is_unset(request.task):
            i_0 = 0
            for item_0 in request.task:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.image_urlobject,
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
                    tmp = scan_image_req.task[i_0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        scan_image_resp = self.scan_image_with_options(scan_image_req, runtime)
        return scan_image_resp

    async def scan_image_advance_async(
        self,
        request: imageaudit_20191230_models.ScanImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanImageResponse:
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
            product='imageaudit',
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
        scan_image_req = imageaudit_20191230_models.ScanImageRequest()
        OpenApiUtilClient.convert(request, scan_image_req)
        if not UtilClient.is_unset(request.task):
            i_0 = 0
            for item_0 in request.task:
                if not UtilClient.is_unset(item_0.image_urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.image_urlobject,
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
                    tmp = scan_image_req.task[i_0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        scan_image_resp = await self.scan_image_with_options_async(scan_image_req, runtime)
        return scan_image_resp

    def scan_text_with_options(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanText',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageaudit_20191230_models.ScanTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def scan_text_with_options_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanText',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imageaudit_20191230_models.ScanTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scan_text(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_text_with_options(request, runtime)

    async def scan_text_async(
        self,
        request: imageaudit_20191230_models.ScanTextRequest,
    ) -> imageaudit_20191230_models.ScanTextResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_text_with_options_async(request, runtime)
