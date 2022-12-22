# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_facebody20191230 import models as facebody_20191230_models
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
        self._endpoint = self.get_endpoint('facebody', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_face_with_options(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFace',
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
            facebody_20191230_models.AddFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.extra_data):
            body['ExtraData'] = request.extra_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFace',
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
            facebody_20191230_models.AddFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_with_options(request, runtime)

    async def add_face_async(
        self,
        request: facebody_20191230_models.AddFaceRequest,
    ) -> facebody_20191230_models.AddFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_with_options_async(request, runtime)

    def add_face_advance(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
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
            product='facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            add_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_resp = self.add_face_with_options(add_face_req, runtime)
        return add_face_resp

    async def add_face_advance_async(
        self,
        request: facebody_20191230_models.AddFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceResponse:
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
            product='facebody',
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
        add_face_req = facebody_20191230_models.AddFaceRequest()
        OpenApiUtilClient.convert(request, add_face_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            add_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_resp = await self.add_face_with_options_async(add_face_req, runtime)
        return add_face_resp

    def add_face_entity_with_options(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceEntity',
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
            facebody_20191230_models.AddFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceEntity',
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
            facebody_20191230_models.AddFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_entity(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_entity_with_options(request, runtime)

    async def add_face_entity_async(
        self,
        request: facebody_20191230_models.AddFaceEntityRequest,
    ) -> facebody_20191230_models.AddFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_entity_with_options_async(request, runtime)

    def add_face_image_template_with_options(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceImageTemplate',
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
            facebody_20191230_models.AddFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddFaceImageTemplate',
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
            facebody_20191230_models.AddFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_face_image_template(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_face_image_template_with_options(request, runtime)

    async def add_face_image_template_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateRequest,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_face_image_template_with_options_async(request, runtime)

    def add_face_image_template_advance(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
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
            product='facebody',
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
        add_face_image_template_req = facebody_20191230_models.AddFaceImageTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_image_template_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            add_face_image_template_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_image_template_resp = self.add_face_image_template_with_options(add_face_image_template_req, runtime)
        return add_face_image_template_resp

    async def add_face_image_template_advance_async(
        self,
        request: facebody_20191230_models.AddFaceImageTemplateAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.AddFaceImageTemplateResponse:
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
            product='facebody',
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
        add_face_image_template_req = facebody_20191230_models.AddFaceImageTemplateRequest()
        OpenApiUtilClient.convert(request, add_face_image_template_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            add_face_image_template_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        add_face_image_template_resp = await self.add_face_image_template_with_options_async(add_face_image_template_req, runtime)
        return add_face_image_template_resp

    def batch_add_faces_with_options(
        self,
        tmp_req: facebody_20191230_models.BatchAddFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BatchAddFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.faces_shrink):
            body['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddFaces',
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
            facebody_20191230_models.BatchAddFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_faces_with_options_async(
        self,
        tmp_req: facebody_20191230_models.BatchAddFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BatchAddFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.faces_shrink):
            body['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        if not UtilClient.is_unset(request.similarity_score_threshold_between_entity):
            body['SimilarityScoreThresholdBetweenEntity'] = request.similarity_score_threshold_between_entity
        if not UtilClient.is_unset(request.similarity_score_threshold_in_entity):
            body['SimilarityScoreThresholdInEntity'] = request.similarity_score_threshold_in_entity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchAddFaces',
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
            facebody_20191230_models.BatchAddFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_faces(
        self,
        request: facebody_20191230_models.BatchAddFacesRequest,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_faces_with_options(request, runtime)

    async def batch_add_faces_async(
        self,
        request: facebody_20191230_models.BatchAddFacesRequest,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_faces_with_options_async(request, runtime)

    def batch_add_faces_advance(
        self,
        request: facebody_20191230_models.BatchAddFacesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
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
            product='facebody',
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
        batch_add_faces_req = facebody_20191230_models.BatchAddFacesRequest()
        OpenApiUtilClient.convert(request, batch_add_faces_req)
        if not UtilClient.is_unset(request.faces):
            i_0 = 0
            for item_0 in request.faces:
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
                    tmp = batch_add_faces_req.faces[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        batch_add_faces_resp = self.batch_add_faces_with_options(batch_add_faces_req, runtime)
        return batch_add_faces_resp

    async def batch_add_faces_advance_async(
        self,
        request: facebody_20191230_models.BatchAddFacesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BatchAddFacesResponse:
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
            product='facebody',
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
        batch_add_faces_req = facebody_20191230_models.BatchAddFacesRequest()
        OpenApiUtilClient.convert(request, batch_add_faces_req)
        if not UtilClient.is_unset(request.faces):
            i_0 = 0
            for item_0 in request.faces:
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
                    tmp = batch_add_faces_req.faces[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        batch_add_faces_resp = await self.batch_add_faces_with_options_async(batch_add_faces_req, runtime)
        return batch_add_faces_resp

    def beautify_body_with_options(
        self,
        tmp_req: facebody_20191230_models.BeautifyBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BeautifyBodyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.age_range):
            request.age_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.age_range, 'AgeRange', 'json')
        if not UtilClient.is_unset(tmp_req.body_boxes):
            request.body_boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_boxes, 'BodyBoxes', 'json')
        if not UtilClient.is_unset(tmp_req.face_list):
            request.face_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_list, 'FaceList', 'json')
        if not UtilClient.is_unset(tmp_req.pose_list):
            request.pose_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pose_list, 'PoseList', 'json')
        body = {}
        if not UtilClient.is_unset(request.age_range_shrink):
            body['AgeRange'] = request.age_range_shrink
        if not UtilClient.is_unset(request.body_boxes_shrink):
            body['BodyBoxes'] = request.body_boxes_shrink
        if not UtilClient.is_unset(request.custom):
            body['Custom'] = request.custom
        if not UtilClient.is_unset(request.face_list_shrink):
            body['FaceList'] = request.face_list_shrink
        if not UtilClient.is_unset(request.female_liquify_degree):
            body['FemaleLiquifyDegree'] = request.female_liquify_degree
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.is_pregnant):
            body['IsPregnant'] = request.is_pregnant
        if not UtilClient.is_unset(request.lengthen_degree):
            body['LengthenDegree'] = request.lengthen_degree
        if not UtilClient.is_unset(request.male_liquify_degree):
            body['MaleLiquifyDegree'] = request.male_liquify_degree
        if not UtilClient.is_unset(request.original_height):
            body['OriginalHeight'] = request.original_height
        if not UtilClient.is_unset(request.original_width):
            body['OriginalWidth'] = request.original_width
        if not UtilClient.is_unset(request.pose_list_shrink):
            body['PoseList'] = request.pose_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeautifyBody',
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
            facebody_20191230_models.BeautifyBodyResponse(),
            self.call_api(params, req, runtime)
        )

    async def beautify_body_with_options_async(
        self,
        tmp_req: facebody_20191230_models.BeautifyBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.BeautifyBodyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.age_range):
            request.age_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.age_range, 'AgeRange', 'json')
        if not UtilClient.is_unset(tmp_req.body_boxes):
            request.body_boxes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_boxes, 'BodyBoxes', 'json')
        if not UtilClient.is_unset(tmp_req.face_list):
            request.face_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.face_list, 'FaceList', 'json')
        if not UtilClient.is_unset(tmp_req.pose_list):
            request.pose_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pose_list, 'PoseList', 'json')
        body = {}
        if not UtilClient.is_unset(request.age_range_shrink):
            body['AgeRange'] = request.age_range_shrink
        if not UtilClient.is_unset(request.body_boxes_shrink):
            body['BodyBoxes'] = request.body_boxes_shrink
        if not UtilClient.is_unset(request.custom):
            body['Custom'] = request.custom
        if not UtilClient.is_unset(request.face_list_shrink):
            body['FaceList'] = request.face_list_shrink
        if not UtilClient.is_unset(request.female_liquify_degree):
            body['FemaleLiquifyDegree'] = request.female_liquify_degree
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.is_pregnant):
            body['IsPregnant'] = request.is_pregnant
        if not UtilClient.is_unset(request.lengthen_degree):
            body['LengthenDegree'] = request.lengthen_degree
        if not UtilClient.is_unset(request.male_liquify_degree):
            body['MaleLiquifyDegree'] = request.male_liquify_degree
        if not UtilClient.is_unset(request.original_height):
            body['OriginalHeight'] = request.original_height
        if not UtilClient.is_unset(request.original_width):
            body['OriginalWidth'] = request.original_width
        if not UtilClient.is_unset(request.pose_list_shrink):
            body['PoseList'] = request.pose_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeautifyBody',
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
            facebody_20191230_models.BeautifyBodyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def beautify_body(
        self,
        request: facebody_20191230_models.BeautifyBodyRequest,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.beautify_body_with_options(request, runtime)

    async def beautify_body_async(
        self,
        request: facebody_20191230_models.BeautifyBodyRequest,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.beautify_body_with_options_async(request, runtime)

    def beautify_body_advance(
        self,
        request: facebody_20191230_models.BeautifyBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
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
            product='facebody',
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
        beautify_body_req = facebody_20191230_models.BeautifyBodyRequest()
        OpenApiUtilClient.convert(request, beautify_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            beautify_body_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        beautify_body_resp = self.beautify_body_with_options(beautify_body_req, runtime)
        return beautify_body_resp

    async def beautify_body_advance_async(
        self,
        request: facebody_20191230_models.BeautifyBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BeautifyBodyResponse:
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
            product='facebody',
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
        beautify_body_req = facebody_20191230_models.BeautifyBodyRequest()
        OpenApiUtilClient.convert(request, beautify_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            beautify_body_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        beautify_body_resp = await self.beautify_body_with_options_async(beautify_body_req, runtime)
        return beautify_body_resp

    def blur_face_with_options(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BlurFace',
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
            facebody_20191230_models.BlurFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def blur_face_with_options_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BlurFace',
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
            facebody_20191230_models.BlurFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def blur_face(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.blur_face_with_options(request, runtime)

    async def blur_face_async(
        self,
        request: facebody_20191230_models.BlurFaceRequest,
    ) -> facebody_20191230_models.BlurFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.blur_face_with_options_async(request, runtime)

    def blur_face_advance(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
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
            product='facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            blur_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        blur_face_resp = self.blur_face_with_options(blur_face_req, runtime)
        return blur_face_resp

    async def blur_face_advance_async(
        self,
        request: facebody_20191230_models.BlurFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BlurFaceResponse:
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
            product='facebody',
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
        blur_face_req = facebody_20191230_models.BlurFaceRequest()
        OpenApiUtilClient.convert(request, blur_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            blur_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        blur_face_resp = await self.blur_face_with_options_async(blur_face_req, runtime)
        return blur_face_resp

    def body_posture_with_options(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BodyPosture',
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
            facebody_20191230_models.BodyPostureResponse(),
            self.call_api(params, req, runtime)
        )

    async def body_posture_with_options_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BodyPosture',
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
            facebody_20191230_models.BodyPostureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def body_posture(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        runtime = util_models.RuntimeOptions()
        return self.body_posture_with_options(request, runtime)

    async def body_posture_async(
        self,
        request: facebody_20191230_models.BodyPostureRequest,
    ) -> facebody_20191230_models.BodyPostureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.body_posture_with_options_async(request, runtime)

    def body_posture_advance(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
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
            product='facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            body_posture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        body_posture_resp = self.body_posture_with_options(body_posture_req, runtime)
        return body_posture_resp

    async def body_posture_advance_async(
        self,
        request: facebody_20191230_models.BodyPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.BodyPostureResponse:
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
            product='facebody',
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
        body_posture_req = facebody_20191230_models.BodyPostureRequest()
        OpenApiUtilClient.convert(request, body_posture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            body_posture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        body_posture_resp = await self.body_posture_with_options_async(body_posture_req, runtime)
        return body_posture_resp

    def compare_face_with_options(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data_a):
            body['ImageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['ImageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFace',
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
            facebody_20191230_models.CompareFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_face_with_options_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data_a):
            body['ImageDataA'] = request.image_data_a
        if not UtilClient.is_unset(request.image_data_b):
            body['ImageDataB'] = request.image_data_b
        if not UtilClient.is_unset(request.image_urla):
            body['ImageURLA'] = request.image_urla
        if not UtilClient.is_unset(request.image_urlb):
            body['ImageURLB'] = request.image_urlb
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CompareFace',
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
            facebody_20191230_models.CompareFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_face(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_face_with_options(request, runtime)

    async def compare_face_async(
        self,
        request: facebody_20191230_models.CompareFaceRequest,
    ) -> facebody_20191230_models.CompareFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_face_with_options_async(request, runtime)

    def compare_face_advance(
        self,
        request: facebody_20191230_models.CompareFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
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
            product='facebody',
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
        compare_face_req = facebody_20191230_models.CompareFaceRequest()
        OpenApiUtilClient.convert(request, compare_face_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlaobject,
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
            compare_face_req.image_urla = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.image_urlbobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlbobject,
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
            compare_face_req.image_urlb = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        compare_face_resp = self.compare_face_with_options(compare_face_req, runtime)
        return compare_face_resp

    async def compare_face_advance_async(
        self,
        request: facebody_20191230_models.CompareFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CompareFaceResponse:
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
            product='facebody',
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
        compare_face_req = facebody_20191230_models.CompareFaceRequest()
        OpenApiUtilClient.convert(request, compare_face_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlaobject,
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
            compare_face_req.image_urla = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.image_urlbobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlbobject,
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
            compare_face_req.image_urlb = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        compare_face_resp = await self.compare_face_with_options_async(compare_face_req, runtime)
        return compare_face_resp

    def count_crowd_with_options(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.is_show):
            body['IsShow'] = request.is_show
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CountCrowd',
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
            facebody_20191230_models.CountCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_crowd_with_options_async(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.is_show):
            body['IsShow'] = request.is_show
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CountCrowd',
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
            facebody_20191230_models.CountCrowdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_crowd(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
    ) -> facebody_20191230_models.CountCrowdResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_crowd_with_options(request, runtime)

    async def count_crowd_async(
        self,
        request: facebody_20191230_models.CountCrowdRequest,
    ) -> facebody_20191230_models.CountCrowdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_crowd_with_options_async(request, runtime)

    def count_crowd_advance(
        self,
        request: facebody_20191230_models.CountCrowdAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
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
            product='facebody',
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
        count_crowd_req = facebody_20191230_models.CountCrowdRequest()
        OpenApiUtilClient.convert(request, count_crowd_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            count_crowd_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        count_crowd_resp = self.count_crowd_with_options(count_crowd_req, runtime)
        return count_crowd_resp

    async def count_crowd_advance_async(
        self,
        request: facebody_20191230_models.CountCrowdAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CountCrowdResponse:
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
            product='facebody',
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
        count_crowd_req = facebody_20191230_models.CountCrowdRequest()
        OpenApiUtilClient.convert(request, count_crowd_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            count_crowd_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        count_crowd_resp = await self.count_crowd_with_options_async(count_crowd_req, runtime)
        return count_crowd_resp

    def create_face_db_with_options(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaceDb',
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
            facebody_20191230_models.CreateFaceDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_face_db_with_options_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFaceDb',
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
            facebody_20191230_models.CreateFaceDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_face_db(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_db_with_options(request, runtime)

    async def create_face_db_async(
        self,
        request: facebody_20191230_models.CreateFaceDbRequest,
    ) -> facebody_20191230_models.CreateFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_db_with_options_async(request, runtime)

    def delete_face_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.face_id):
            body['FaceId'] = request.face_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
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
            facebody_20191230_models.DeleteFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.face_id):
            body['FaceId'] = request.face_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFace',
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
            facebody_20191230_models.DeleteFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_with_options(request, runtime)

    async def delete_face_async(
        self,
        request: facebody_20191230_models.DeleteFaceRequest,
    ) -> facebody_20191230_models.DeleteFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_with_options_async(request, runtime)

    def delete_face_db_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceDb',
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
            facebody_20191230_models.DeleteFaceDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_db_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceDb',
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
            facebody_20191230_models.DeleteFaceDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_db(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_db_with_options(request, runtime)

    async def delete_face_db_async(
        self,
        request: facebody_20191230_models.DeleteFaceDbRequest,
    ) -> facebody_20191230_models.DeleteFaceDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_db_with_options_async(request, runtime)

    def delete_face_entity_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceEntity',
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
            facebody_20191230_models.DeleteFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceEntity',
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
            facebody_20191230_models.DeleteFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_entity(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_entity_with_options(request, runtime)

    async def delete_face_entity_async(
        self,
        request: facebody_20191230_models.DeleteFaceEntityRequest,
    ) -> facebody_20191230_models.DeleteFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_entity_with_options_async(request, runtime)

    def delete_face_image_template_with_options(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceImageTemplate',
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
            facebody_20191230_models.DeleteFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFaceImageTemplate',
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
            facebody_20191230_models.DeleteFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_face_image_template(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_image_template_with_options(request, runtime)

    async def delete_face_image_template_async(
        self,
        request: facebody_20191230_models.DeleteFaceImageTemplateRequest,
    ) -> facebody_20191230_models.DeleteFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_image_template_with_options_async(request, runtime)

    def detect_body_count_with_options(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectBodyCount',
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
            facebody_20191230_models.DetectBodyCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_body_count_with_options_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectBodyCount',
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
            facebody_20191230_models.DetectBodyCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_body_count(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_body_count_with_options(request, runtime)

    async def detect_body_count_async(
        self,
        request: facebody_20191230_models.DetectBodyCountRequest,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_body_count_with_options_async(request, runtime)

    def detect_body_count_advance(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
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
            product='facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_body_count_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_body_count_resp = self.detect_body_count_with_options(detect_body_count_req, runtime)
        return detect_body_count_resp

    async def detect_body_count_advance_async(
        self,
        request: facebody_20191230_models.DetectBodyCountAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectBodyCountResponse:
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
            product='facebody',
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
        detect_body_count_req = facebody_20191230_models.DetectBodyCountRequest()
        OpenApiUtilClient.convert(request, detect_body_count_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_body_count_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_body_count_resp = await self.detect_body_count_with_options_async(detect_body_count_req, runtime)
        return detect_body_count_resp

    def detect_celebrity_with_options(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCelebrity',
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
            facebody_20191230_models.DetectCelebrityResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_celebrity_with_options_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectCelebrity',
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
            facebody_20191230_models.DetectCelebrityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_celebrity(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_celebrity_with_options(request, runtime)

    async def detect_celebrity_async(
        self,
        request: facebody_20191230_models.DetectCelebrityRequest,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_celebrity_with_options_async(request, runtime)

    def detect_celebrity_advance(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
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
            product='facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_celebrity_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_celebrity_resp = self.detect_celebrity_with_options(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    async def detect_celebrity_advance_async(
        self,
        request: facebody_20191230_models.DetectCelebrityAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectCelebrityResponse:
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
            product='facebody',
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
        detect_celebrity_req = facebody_20191230_models.DetectCelebrityRequest()
        OpenApiUtilClient.convert(request, detect_celebrity_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_celebrity_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_celebrity_resp = await self.detect_celebrity_with_options_async(detect_celebrity_req, runtime)
        return detect_celebrity_resp

    def detect_chef_cap_with_options(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectChefCap',
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
            facebody_20191230_models.DetectChefCapResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_chef_cap_with_options_async(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectChefCap',
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
            facebody_20191230_models.DetectChefCapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_chef_cap(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_chef_cap_with_options(request, runtime)

    async def detect_chef_cap_async(
        self,
        request: facebody_20191230_models.DetectChefCapRequest,
    ) -> facebody_20191230_models.DetectChefCapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_chef_cap_with_options_async(request, runtime)

    def detect_chef_cap_advance(
        self,
        request: facebody_20191230_models.DetectChefCapAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
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
            product='facebody',
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
        detect_chef_cap_req = facebody_20191230_models.DetectChefCapRequest()
        OpenApiUtilClient.convert(request, detect_chef_cap_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_chef_cap_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_chef_cap_resp = self.detect_chef_cap_with_options(detect_chef_cap_req, runtime)
        return detect_chef_cap_resp

    async def detect_chef_cap_advance_async(
        self,
        request: facebody_20191230_models.DetectChefCapAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectChefCapResponse:
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
            product='facebody',
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
        detect_chef_cap_req = facebody_20191230_models.DetectChefCapRequest()
        OpenApiUtilClient.convert(request, detect_chef_cap_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_chef_cap_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_chef_cap_resp = await self.detect_chef_cap_with_options_async(detect_chef_cap_req, runtime)
        return detect_chef_cap_resp

    def detect_face_with_options(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.landmark):
            body['Landmark'] = request.landmark
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.pose):
            body['Pose'] = request.pose
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFace',
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
            facebody_20191230_models.DetectFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.landmark):
            body['Landmark'] = request.landmark
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.pose):
            body['Pose'] = request.pose
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectFace',
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
            facebody_20191230_models.DetectFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_face(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_face_with_options(request, runtime)

    async def detect_face_async(
        self,
        request: facebody_20191230_models.DetectFaceRequest,
    ) -> facebody_20191230_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_face_with_options_async(request, runtime)

    def detect_face_advance(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
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
            product='facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_face_resp = self.detect_face_with_options(detect_face_req, runtime)
        return detect_face_resp

    async def detect_face_advance_async(
        self,
        request: facebody_20191230_models.DetectFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectFaceResponse:
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
            product='facebody',
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
        detect_face_req = facebody_20191230_models.DetectFaceRequest()
        OpenApiUtilClient.convert(request, detect_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_face_resp = await self.detect_face_with_options_async(detect_face_req, runtime)
        return detect_face_resp

    def detect_ipcpedestrian_with_options(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCPedestrian',
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
            facebody_20191230_models.DetectIPCPedestrianResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_ipcpedestrian_with_options_async(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.height):
            body['Height'] = request.height
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.width):
            body['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectIPCPedestrian',
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
            facebody_20191230_models.DetectIPCPedestrianResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_ipcpedestrian(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_ipcpedestrian_with_options(request, runtime)

    async def detect_ipcpedestrian_async(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianRequest,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_ipcpedestrian_with_options_async(request, runtime)

    def detect_ipcpedestrian_advance(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
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
            product='facebody',
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
        detect_ipcpedestrian_req = facebody_20191230_models.DetectIPCPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_ipcpedestrian_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_ipcpedestrian_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_ipcpedestrian_resp = self.detect_ipcpedestrian_with_options(detect_ipcpedestrian_req, runtime)
        return detect_ipcpedestrian_resp

    async def detect_ipcpedestrian_advance_async(
        self,
        request: facebody_20191230_models.DetectIPCPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectIPCPedestrianResponse:
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
            product='facebody',
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
        detect_ipcpedestrian_req = facebody_20191230_models.DetectIPCPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_ipcpedestrian_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_ipcpedestrian_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_ipcpedestrian_resp = await self.detect_ipcpedestrian_with_options_async(detect_ipcpedestrian_req, runtime)
        return detect_ipcpedestrian_resp

    def detect_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLivingFace',
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
            facebody_20191230_models.DetectLivingFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tasks):
            body['Tasks'] = request.tasks
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectLivingFace',
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
            facebody_20191230_models.DetectLivingFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_living_face(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_living_face_with_options(request, runtime)

    async def detect_living_face_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceRequest,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_living_face_with_options_async(request, runtime)

    def detect_living_face_advance(
        self,
        request: facebody_20191230_models.DetectLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
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
            product='facebody',
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
        detect_living_face_req = facebody_20191230_models.DetectLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
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
                    tmp = detect_living_face_req.tasks[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_living_face_resp = self.detect_living_face_with_options(detect_living_face_req, runtime)
        return detect_living_face_resp

    async def detect_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectLivingFaceResponse:
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
            product='facebody',
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
        detect_living_face_req = facebody_20191230_models.DetectLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_living_face_req)
        if not UtilClient.is_unset(request.tasks):
            i_0 = 0
            for item_0 in request.tasks:
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
                    tmp = detect_living_face_req.tasks[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        detect_living_face_resp = await self.detect_living_face_with_options_async(detect_living_face_req, runtime)
        return detect_living_face_resp

    def detect_pedestrian_with_options(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrian',
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
            facebody_20191230_models.DetectPedestrianResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_pedestrian_with_options_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrian',
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
            facebody_20191230_models.DetectPedestrianResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_pedestrian(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_pedestrian_with_options(request, runtime)

    async def detect_pedestrian_async(
        self,
        request: facebody_20191230_models.DetectPedestrianRequest,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_pedestrian_with_options_async(request, runtime)

    def detect_pedestrian_advance(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
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
            product='facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_pedestrian_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_pedestrian_resp = self.detect_pedestrian_with_options(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    async def detect_pedestrian_advance_async(
        self,
        request: facebody_20191230_models.DetectPedestrianAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianResponse:
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
            product='facebody',
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
        detect_pedestrian_req = facebody_20191230_models.DetectPedestrianRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_pedestrian_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_pedestrian_resp = await self.detect_pedestrian_with_options_async(detect_pedestrian_req, runtime)
        return detect_pedestrian_resp

    def detect_pedestrian_intrusion_with_options(
        self,
        tmp_req: facebody_20191230_models.DetectPedestrianIntrusionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.DetectPedestrianIntrusionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detect_region):
            request.detect_region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detect_region, 'DetectRegion', 'json')
        body = {}
        if not UtilClient.is_unset(request.detect_region_shrink):
            body['DetectRegion'] = request.detect_region_shrink
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.region_type):
            body['RegionType'] = request.region_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrianIntrusion',
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
            facebody_20191230_models.DetectPedestrianIntrusionResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_pedestrian_intrusion_with_options_async(
        self,
        tmp_req: facebody_20191230_models.DetectPedestrianIntrusionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        UtilClient.validate_model(tmp_req)
        request = facebody_20191230_models.DetectPedestrianIntrusionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.detect_region):
            request.detect_region_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.detect_region, 'DetectRegion', 'json')
        body = {}
        if not UtilClient.is_unset(request.detect_region_shrink):
            body['DetectRegion'] = request.detect_region_shrink
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.region_type):
            body['RegionType'] = request.region_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectPedestrianIntrusion',
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
            facebody_20191230_models.DetectPedestrianIntrusionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_pedestrian_intrusion(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionRequest,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_pedestrian_intrusion_with_options(request, runtime)

    async def detect_pedestrian_intrusion_async(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionRequest,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_pedestrian_intrusion_with_options_async(request, runtime)

    def detect_pedestrian_intrusion_advance(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
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
            product='facebody',
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
        detect_pedestrian_intrusion_req = facebody_20191230_models.DetectPedestrianIntrusionRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_intrusion_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_pedestrian_intrusion_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_pedestrian_intrusion_resp = self.detect_pedestrian_intrusion_with_options(detect_pedestrian_intrusion_req, runtime)
        return detect_pedestrian_intrusion_resp

    async def detect_pedestrian_intrusion_advance_async(
        self,
        request: facebody_20191230_models.DetectPedestrianIntrusionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectPedestrianIntrusionResponse:
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
            product='facebody',
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
        detect_pedestrian_intrusion_req = facebody_20191230_models.DetectPedestrianIntrusionRequest()
        OpenApiUtilClient.convert(request, detect_pedestrian_intrusion_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            detect_pedestrian_intrusion_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_pedestrian_intrusion_resp = await self.detect_pedestrian_intrusion_with_options_async(detect_pedestrian_intrusion_req, runtime)
        return detect_pedestrian_intrusion_resp

    def detect_video_living_face_with_options(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoLivingFace',
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
            facebody_20191230_models.DetectVideoLivingFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_video_living_face_with_options_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetectVideoLivingFace',
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
            facebody_20191230_models.DetectVideoLivingFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_video_living_face(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_video_living_face_with_options(request, runtime)

    async def detect_video_living_face_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceRequest,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_living_face_with_options_async(request, runtime)

    def detect_video_living_face_advance(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
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
            product='facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            detect_video_living_face_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_video_living_face_resp = self.detect_video_living_face_with_options(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    async def detect_video_living_face_advance_async(
        self,
        request: facebody_20191230_models.DetectVideoLivingFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.DetectVideoLivingFaceResponse:
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
            product='facebody',
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
        detect_video_living_face_req = facebody_20191230_models.DetectVideoLivingFaceRequest()
        OpenApiUtilClient.convert(request, detect_video_living_face_req)
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            detect_video_living_face_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        detect_video_living_face_resp = await self.detect_video_living_face_with_options_async(detect_video_living_face_req, runtime)
        return detect_video_living_face_resp

    def enhance_face_with_options(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceFace',
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
            facebody_20191230_models.EnhanceFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def enhance_face_with_options_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnhanceFace',
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
            facebody_20191230_models.EnhanceFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enhance_face(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enhance_face_with_options(request, runtime)

    async def enhance_face_async(
        self,
        request: facebody_20191230_models.EnhanceFaceRequest,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enhance_face_with_options_async(request, runtime)

    def enhance_face_advance(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
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
            product='facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            enhance_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        enhance_face_resp = self.enhance_face_with_options(enhance_face_req, runtime)
        return enhance_face_resp

    async def enhance_face_advance_async(
        self,
        request: facebody_20191230_models.EnhanceFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.EnhanceFaceResponse:
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
            product='facebody',
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
        enhance_face_req = facebody_20191230_models.EnhanceFaceRequest()
        OpenApiUtilClient.convert(request, enhance_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            enhance_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        enhance_face_resp = await self.enhance_face_with_options_async(enhance_face_req, runtime)
        return enhance_face_resp

    def extract_finger_print_with_options(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractFingerPrint',
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
            facebody_20191230_models.ExtractFingerPrintResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_finger_print_with_options_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractFingerPrint',
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
            facebody_20191230_models.ExtractFingerPrintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_finger_print(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_finger_print_with_options(request, runtime)

    async def extract_finger_print_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintRequest,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_finger_print_with_options_async(request, runtime)

    def extract_finger_print_advance(
        self,
        request: facebody_20191230_models.ExtractFingerPrintAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
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
            product='facebody',
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
        extract_finger_print_req = facebody_20191230_models.ExtractFingerPrintRequest()
        OpenApiUtilClient.convert(request, extract_finger_print_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            extract_finger_print_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_finger_print_resp = self.extract_finger_print_with_options(extract_finger_print_req, runtime)
        return extract_finger_print_resp

    async def extract_finger_print_advance_async(
        self,
        request: facebody_20191230_models.ExtractFingerPrintAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractFingerPrintResponse:
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
            product='facebody',
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
        extract_finger_print_req = facebody_20191230_models.ExtractFingerPrintRequest()
        OpenApiUtilClient.convert(request, extract_finger_print_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            extract_finger_print_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_finger_print_resp = await self.extract_finger_print_with_options_async(extract_finger_print_req, runtime)
        return extract_finger_print_resp

    def extract_pedestrian_feature_attr_with_options(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractPedestrianFeatureAttr',
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
            facebody_20191230_models.ExtractPedestrianFeatureAttrResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_pedestrian_feature_attr_with_options_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mode):
            body['Mode'] = request.mode
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtractPedestrianFeatureAttr',
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
            facebody_20191230_models.ExtractPedestrianFeatureAttrResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_pedestrian_feature_attr(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        runtime = util_models.RuntimeOptions()
        return self.extract_pedestrian_feature_attr_with_options(request, runtime)

    async def extract_pedestrian_feature_attr_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrRequest,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extract_pedestrian_feature_attr_with_options_async(request, runtime)

    def extract_pedestrian_feature_attr_advance(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
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
            product='facebody',
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
        extract_pedestrian_feature_attr_req = facebody_20191230_models.ExtractPedestrianFeatureAttrRequest()
        OpenApiUtilClient.convert(request, extract_pedestrian_feature_attr_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            extract_pedestrian_feature_attr_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_pedestrian_feature_attr_resp = self.extract_pedestrian_feature_attr_with_options(extract_pedestrian_feature_attr_req, runtime)
        return extract_pedestrian_feature_attr_resp

    async def extract_pedestrian_feature_attr_advance_async(
        self,
        request: facebody_20191230_models.ExtractPedestrianFeatureAttrAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ExtractPedestrianFeatureAttrResponse:
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
            product='facebody',
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
        extract_pedestrian_feature_attr_req = facebody_20191230_models.ExtractPedestrianFeatureAttrRequest()
        OpenApiUtilClient.convert(request, extract_pedestrian_feature_attr_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            extract_pedestrian_feature_attr_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        extract_pedestrian_feature_attr_resp = await self.extract_pedestrian_feature_attr_with_options_async(extract_pedestrian_feature_attr_req, runtime)
        return extract_pedestrian_feature_attr_resp

    def face_beauty_with_options(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.sharp):
            body['Sharp'] = request.sharp
        if not UtilClient.is_unset(request.smooth):
            body['Smooth'] = request.smooth
        if not UtilClient.is_unset(request.white):
            body['White'] = request.white
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceBeauty',
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
            facebody_20191230_models.FaceBeautyResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_beauty_with_options_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.sharp):
            body['Sharp'] = request.sharp
        if not UtilClient.is_unset(request.smooth):
            body['Smooth'] = request.smooth
        if not UtilClient.is_unset(request.white):
            body['White'] = request.white
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceBeauty',
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
            facebody_20191230_models.FaceBeautyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_beauty(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_beauty_with_options(request, runtime)

    async def face_beauty_async(
        self,
        request: facebody_20191230_models.FaceBeautyRequest,
    ) -> facebody_20191230_models.FaceBeautyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_beauty_with_options_async(request, runtime)

    def face_beauty_advance(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
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
            product='facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_beauty_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_beauty_resp = self.face_beauty_with_options(face_beauty_req, runtime)
        return face_beauty_resp

    async def face_beauty_advance_async(
        self,
        request: facebody_20191230_models.FaceBeautyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceBeautyResponse:
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
            product='facebody',
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
        face_beauty_req = facebody_20191230_models.FaceBeautyRequest()
        OpenApiUtilClient.convert(request, face_beauty_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_beauty_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_beauty_resp = await self.face_beauty_with_options_async(face_beauty_req, runtime)
        return face_beauty_resp

    def face_filter_with_options(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceFilter',
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
            facebody_20191230_models.FaceFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_filter_with_options_async(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceFilter',
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
            facebody_20191230_models.FaceFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_filter(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
    ) -> facebody_20191230_models.FaceFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_filter_with_options(request, runtime)

    async def face_filter_async(
        self,
        request: facebody_20191230_models.FaceFilterRequest,
    ) -> facebody_20191230_models.FaceFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_filter_with_options_async(request, runtime)

    def face_filter_advance(
        self,
        request: facebody_20191230_models.FaceFilterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
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
            product='facebody',
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
        face_filter_req = facebody_20191230_models.FaceFilterRequest()
        OpenApiUtilClient.convert(request, face_filter_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_filter_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_filter_resp = self.face_filter_with_options(face_filter_req, runtime)
        return face_filter_resp

    async def face_filter_advance_async(
        self,
        request: facebody_20191230_models.FaceFilterAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceFilterResponse:
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
            product='facebody',
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
        face_filter_req = facebody_20191230_models.FaceFilterRequest()
        OpenApiUtilClient.convert(request, face_filter_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_filter_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_filter_resp = await self.face_filter_with_options_async(face_filter_req, runtime)
        return face_filter_resp

    def face_makeup_with_options(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.makeup_type):
            body['MakeupType'] = request.makeup_type
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceMakeup',
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
            facebody_20191230_models.FaceMakeupResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_makeup_with_options_async(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.makeup_type):
            body['MakeupType'] = request.makeup_type
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceMakeup',
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
            facebody_20191230_models.FaceMakeupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_makeup(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_makeup_with_options(request, runtime)

    async def face_makeup_async(
        self,
        request: facebody_20191230_models.FaceMakeupRequest,
    ) -> facebody_20191230_models.FaceMakeupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_makeup_with_options_async(request, runtime)

    def face_makeup_advance(
        self,
        request: facebody_20191230_models.FaceMakeupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
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
            product='facebody',
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
        face_makeup_req = facebody_20191230_models.FaceMakeupRequest()
        OpenApiUtilClient.convert(request, face_makeup_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_makeup_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_makeup_resp = self.face_makeup_with_options(face_makeup_req, runtime)
        return face_makeup_resp

    async def face_makeup_advance_async(
        self,
        request: facebody_20191230_models.FaceMakeupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceMakeupResponse:
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
            product='facebody',
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
        face_makeup_req = facebody_20191230_models.FaceMakeupRequest()
        OpenApiUtilClient.convert(request, face_makeup_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_makeup_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_makeup_resp = await self.face_makeup_with_options_async(face_makeup_req, runtime)
        return face_makeup_resp

    def face_tidyup_with_options(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.shape_type):
            body['ShapeType'] = request.shape_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceTidyup',
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
            facebody_20191230_models.FaceTidyupResponse(),
            self.call_api(params, req, runtime)
        )

    async def face_tidyup_with_options_async(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.shape_type):
            body['ShapeType'] = request.shape_type
        if not UtilClient.is_unset(request.strength):
            body['Strength'] = request.strength
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FaceTidyup',
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
            facebody_20191230_models.FaceTidyupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def face_tidyup(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        runtime = util_models.RuntimeOptions()
        return self.face_tidyup_with_options(request, runtime)

    async def face_tidyup_async(
        self,
        request: facebody_20191230_models.FaceTidyupRequest,
    ) -> facebody_20191230_models.FaceTidyupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.face_tidyup_with_options_async(request, runtime)

    def face_tidyup_advance(
        self,
        request: facebody_20191230_models.FaceTidyupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
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
            product='facebody',
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
        face_tidyup_req = facebody_20191230_models.FaceTidyupRequest()
        OpenApiUtilClient.convert(request, face_tidyup_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_tidyup_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_tidyup_resp = self.face_tidyup_with_options(face_tidyup_req, runtime)
        return face_tidyup_resp

    async def face_tidyup_advance_async(
        self,
        request: facebody_20191230_models.FaceTidyupAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.FaceTidyupResponse:
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
            product='facebody',
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
        face_tidyup_req = facebody_20191230_models.FaceTidyupRequest()
        OpenApiUtilClient.convert(request, face_tidyup_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            face_tidyup_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        face_tidyup_resp = await self.face_tidyup_with_options_async(face_tidyup_req, runtime)
        return face_tidyup_resp

    def gen_real_person_verification_token_with_options(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['CertificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenRealPersonVerificationToken',
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
            facebody_20191230_models.GenRealPersonVerificationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def gen_real_person_verification_token_with_options_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.certificate_name):
            body['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.certificate_number):
            body['CertificateNumber'] = request.certificate_number
        if not UtilClient.is_unset(request.meta_info):
            body['MetaInfo'] = request.meta_info
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenRealPersonVerificationToken',
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
            facebody_20191230_models.GenRealPersonVerificationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def gen_real_person_verification_token(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.gen_real_person_verification_token_with_options(request, runtime)

    async def gen_real_person_verification_token_async(
        self,
        request: facebody_20191230_models.GenRealPersonVerificationTokenRequest,
    ) -> facebody_20191230_models.GenRealPersonVerificationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.gen_real_person_verification_token_with_options_async(request, runtime)

    def generate_human_anime_style_with_options(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_type):
            query['AlgoType'] = request.algo_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyle',
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
            facebody_20191230_models.GenerateHumanAnimeStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_human_anime_style_with_options_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.algo_type):
            query['AlgoType'] = request.algo_type
        if not UtilClient.is_unset(request.image_url):
            query['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateHumanAnimeStyle',
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
            facebody_20191230_models.GenerateHumanAnimeStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_human_anime_style(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_human_anime_style_with_options(request, runtime)

    async def generate_human_anime_style_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_anime_style_with_options_async(request, runtime)

    def generate_human_anime_style_advance(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
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
            product='facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            generate_human_anime_style_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        generate_human_anime_style_resp = self.generate_human_anime_style_with_options(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    async def generate_human_anime_style_advance_async(
        self,
        request: facebody_20191230_models.GenerateHumanAnimeStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanAnimeStyleResponse:
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
            product='facebody',
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
        generate_human_anime_style_req = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_anime_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            generate_human_anime_style_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        generate_human_anime_style_resp = await self.generate_human_anime_style_with_options_async(generate_human_anime_style_req, runtime)
        return generate_human_anime_style_resp

    def generate_human_sketch_style_with_options(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.return_type):
            body['ReturnType'] = request.return_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanSketchStyle',
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
            facebody_20191230_models.GenerateHumanSketchStyleResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_human_sketch_style_with_options_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.return_type):
            body['ReturnType'] = request.return_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateHumanSketchStyle',
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
            facebody_20191230_models.GenerateHumanSketchStyleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_human_sketch_style(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_human_sketch_style_with_options(request, runtime)

    async def generate_human_sketch_style_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleRequest,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_human_sketch_style_with_options_async(request, runtime)

    def generate_human_sketch_style_advance(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
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
            product='facebody',
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
        generate_human_sketch_style_req = facebody_20191230_models.GenerateHumanSketchStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_sketch_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            generate_human_sketch_style_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        generate_human_sketch_style_resp = self.generate_human_sketch_style_with_options(generate_human_sketch_style_req, runtime)
        return generate_human_sketch_style_resp

    async def generate_human_sketch_style_advance_async(
        self,
        request: facebody_20191230_models.GenerateHumanSketchStyleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GenerateHumanSketchStyleResponse:
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
            product='facebody',
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
        generate_human_sketch_style_req = facebody_20191230_models.GenerateHumanSketchStyleRequest()
        OpenApiUtilClient.convert(request, generate_human_sketch_style_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            generate_human_sketch_style_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        generate_human_sketch_style_resp = await self.generate_human_sketch_style_with_options_async(generate_human_sketch_style_req, runtime)
        return generate_human_sketch_style_resp

    def get_face_entity_with_options(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceEntity',
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
            facebody_20191230_models.GetFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceEntity',
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
            facebody_20191230_models.GetFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_face_entity(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_face_entity_with_options(request, runtime)

    async def get_face_entity_async(
        self,
        request: facebody_20191230_models.GetFaceEntityRequest,
    ) -> facebody_20191230_models.GetFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_face_entity_with_options_async(request, runtime)

    def get_real_person_verification_result_with_options(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.verification_token):
            body['VerificationToken'] = request.verification_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRealPersonVerificationResult',
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
            facebody_20191230_models.GetRealPersonVerificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_person_verification_result_with_options_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.verification_token):
            body['VerificationToken'] = request.verification_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRealPersonVerificationResult',
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
            facebody_20191230_models.GetRealPersonVerificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_person_verification_result(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_real_person_verification_result_with_options(request, runtime)

    async def get_real_person_verification_result_async(
        self,
        request: facebody_20191230_models.GetRealPersonVerificationResultRequest,
    ) -> facebody_20191230_models.GetRealPersonVerificationResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_real_person_verification_result_with_options_async(request, runtime)

    def hand_posture_with_options(
        self,
        request: facebody_20191230_models.HandPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HandPosture',
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
            facebody_20191230_models.HandPostureResponse(),
            self.call_api(params, req, runtime)
        )

    async def hand_posture_with_options_async(
        self,
        request: facebody_20191230_models.HandPostureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='HandPosture',
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
            facebody_20191230_models.HandPostureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hand_posture(
        self,
        request: facebody_20191230_models.HandPostureRequest,
    ) -> facebody_20191230_models.HandPostureResponse:
        runtime = util_models.RuntimeOptions()
        return self.hand_posture_with_options(request, runtime)

    async def hand_posture_async(
        self,
        request: facebody_20191230_models.HandPostureRequest,
    ) -> facebody_20191230_models.HandPostureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.hand_posture_with_options_async(request, runtime)

    def hand_posture_advance(
        self,
        request: facebody_20191230_models.HandPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
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
            product='facebody',
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
        hand_posture_req = facebody_20191230_models.HandPostureRequest()
        OpenApiUtilClient.convert(request, hand_posture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            hand_posture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        hand_posture_resp = self.hand_posture_with_options(hand_posture_req, runtime)
        return hand_posture_resp

    async def hand_posture_advance_async(
        self,
        request: facebody_20191230_models.HandPostureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.HandPostureResponse:
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
            product='facebody',
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
        hand_posture_req = facebody_20191230_models.HandPostureRequest()
        OpenApiUtilClient.convert(request, hand_posture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            hand_posture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        hand_posture_resp = await self.hand_posture_with_options_async(hand_posture_req, runtime)
        return hand_posture_resp

    def liquify_face_with_options(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LiquifyFace',
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
            facebody_20191230_models.LiquifyFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def liquify_face_with_options_async(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LiquifyFace',
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
            facebody_20191230_models.LiquifyFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def liquify_face(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.liquify_face_with_options(request, runtime)

    async def liquify_face_async(
        self,
        request: facebody_20191230_models.LiquifyFaceRequest,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.liquify_face_with_options_async(request, runtime)

    def liquify_face_advance(
        self,
        request: facebody_20191230_models.LiquifyFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
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
            product='facebody',
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
        liquify_face_req = facebody_20191230_models.LiquifyFaceRequest()
        OpenApiUtilClient.convert(request, liquify_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            liquify_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        liquify_face_resp = self.liquify_face_with_options(liquify_face_req, runtime)
        return liquify_face_resp

    async def liquify_face_advance_async(
        self,
        request: facebody_20191230_models.LiquifyFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.LiquifyFaceResponse:
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
            product='facebody',
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
        liquify_face_req = facebody_20191230_models.LiquifyFaceRequest()
        OpenApiUtilClient.convert(request, liquify_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            liquify_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        liquify_face_resp = await self.liquify_face_with_options_async(liquify_face_req, runtime)
        return liquify_face_resp

    def list_face_dbs_with_options(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceDbs',
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
            facebody_20191230_models.ListFaceDbsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_face_dbs_with_options_async(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceDbs',
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
            facebody_20191230_models.ListFaceDbsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_face_dbs(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_dbs_with_options(request, runtime)

    async def list_face_dbs_async(
        self,
        request: facebody_20191230_models.ListFaceDbsRequest,
    ) -> facebody_20191230_models.ListFaceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_dbs_with_options_async(request, runtime)

    def list_face_entities_with_options(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceEntities',
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
            facebody_20191230_models.ListFaceEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_face_entities_with_options_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id_prefix):
            body['EntityIdPrefix'] = request.entity_id_prefix
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.offset):
            body['Offset'] = request.offset
        if not UtilClient.is_unset(request.order):
            body['Order'] = request.order
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceEntities',
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
            facebody_20191230_models.ListFaceEntitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_face_entities(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_entities_with_options(request, runtime)

    async def list_face_entities_async(
        self,
        request: facebody_20191230_models.ListFaceEntitiesRequest,
    ) -> facebody_20191230_models.ListFaceEntitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_entities_with_options_async(request, runtime)

    def merge_image_face_with_options(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeImageFace',
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
            facebody_20191230_models.MergeImageFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_image_face_with_options_async(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MergeImageFace',
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
            facebody_20191230_models.MergeImageFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_image_face(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.merge_image_face_with_options(request, runtime)

    async def merge_image_face_async(
        self,
        request: facebody_20191230_models.MergeImageFaceRequest,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_image_face_with_options_async(request, runtime)

    def merge_image_face_advance(
        self,
        request: facebody_20191230_models.MergeImageFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
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
            product='facebody',
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
        merge_image_face_req = facebody_20191230_models.MergeImageFaceRequest()
        OpenApiUtilClient.convert(request, merge_image_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            merge_image_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_image_face_resp = self.merge_image_face_with_options(merge_image_face_req, runtime)
        return merge_image_face_resp

    async def merge_image_face_advance_async(
        self,
        request: facebody_20191230_models.MergeImageFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MergeImageFaceResponse:
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
            product='facebody',
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
        merge_image_face_req = facebody_20191230_models.MergeImageFaceRequest()
        OpenApiUtilClient.convert(request, merge_image_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            merge_image_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        merge_image_face_resp = await self.merge_image_face_with_options_async(merge_image_face_req, runtime)
        return merge_image_face_resp

    def monitor_examination_with_options(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonitorExamination',
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
            facebody_20191230_models.MonitorExaminationResponse(),
            self.call_api(params, req, runtime)
        )

    async def monitor_examination_with_options_async(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MonitorExamination',
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
            facebody_20191230_models.MonitorExaminationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def monitor_examination(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        runtime = util_models.RuntimeOptions()
        return self.monitor_examination_with_options(request, runtime)

    async def monitor_examination_async(
        self,
        request: facebody_20191230_models.MonitorExaminationRequest,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.monitor_examination_with_options_async(request, runtime)

    def monitor_examination_advance(
        self,
        request: facebody_20191230_models.MonitorExaminationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
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
            product='facebody',
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
        monitor_examination_req = facebody_20191230_models.MonitorExaminationRequest()
        OpenApiUtilClient.convert(request, monitor_examination_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            monitor_examination_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        monitor_examination_resp = self.monitor_examination_with_options(monitor_examination_req, runtime)
        return monitor_examination_resp

    async def monitor_examination_advance_async(
        self,
        request: facebody_20191230_models.MonitorExaminationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.MonitorExaminationResponse:
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
            product='facebody',
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
        monitor_examination_req = facebody_20191230_models.MonitorExaminationRequest()
        OpenApiUtilClient.convert(request, monitor_examination_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            monitor_examination_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        monitor_examination_resp = await self.monitor_examination_with_options_async(monitor_examination_req, runtime)
        return monitor_examination_resp

    def pedestrian_detect_attribute_with_options(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PedestrianDetectAttribute',
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
            facebody_20191230_models.PedestrianDetectAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def pedestrian_detect_attribute_with_options_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PedestrianDetectAttribute',
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
            facebody_20191230_models.PedestrianDetectAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pedestrian_detect_attribute(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.pedestrian_detect_attribute_with_options(request, runtime)

    async def pedestrian_detect_attribute_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeRequest,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pedestrian_detect_attribute_with_options_async(request, runtime)

    def pedestrian_detect_attribute_advance(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
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
            product='facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            pedestrian_detect_attribute_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        pedestrian_detect_attribute_resp = self.pedestrian_detect_attribute_with_options(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    async def pedestrian_detect_attribute_advance_async(
        self,
        request: facebody_20191230_models.PedestrianDetectAttributeAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.PedestrianDetectAttributeResponse:
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
            product='facebody',
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
        pedestrian_detect_attribute_req = facebody_20191230_models.PedestrianDetectAttributeRequest()
        OpenApiUtilClient.convert(request, pedestrian_detect_attribute_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            pedestrian_detect_attribute_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        pedestrian_detect_attribute_resp = await self.pedestrian_detect_attribute_with_options_async(pedestrian_detect_attribute_req, runtime)
        return pedestrian_detect_attribute_resp

    def query_face_image_template_with_options(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.QueryFaceImageTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_face_image_template_with_options_async(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceImageTemplate',
            version='2019-12-30',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            facebody_20191230_models.QueryFaceImageTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_face_image_template(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_face_image_template_with_options(request, runtime)

    async def query_face_image_template_async(
        self,
        request: facebody_20191230_models.QueryFaceImageTemplateRequest,
    ) -> facebody_20191230_models.QueryFaceImageTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_face_image_template_with_options_async(request, runtime)

    def recognize_action_with_options(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.video_data):
            body['VideoData'] = request.video_data
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAction',
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
            facebody_20191230_models.RecognizeActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_action_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.urllist):
            body['URLList'] = request.urllist
        if not UtilClient.is_unset(request.video_data):
            body['VideoData'] = request.video_data
        if not UtilClient.is_unset(request.video_url):
            body['VideoUrl'] = request.video_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeAction',
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
            facebody_20191230_models.RecognizeActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_action(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_action_with_options(request, runtime)

    async def recognize_action_async(
        self,
        request: facebody_20191230_models.RecognizeActionRequest,
    ) -> facebody_20191230_models.RecognizeActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_action_with_options_async(request, runtime)

    def recognize_action_advance(
        self,
        request: facebody_20191230_models.RecognizeActionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
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
            product='facebody',
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
        recognize_action_req = facebody_20191230_models.RecognizeActionRequest()
        OpenApiUtilClient.convert(request, recognize_action_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
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
                    tmp = recognize_action_req.urllist[i0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            recognize_action_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_action_resp = self.recognize_action_with_options(recognize_action_req, runtime)
        return recognize_action_resp

    async def recognize_action_advance_async(
        self,
        request: facebody_20191230_models.RecognizeActionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeActionResponse:
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
            product='facebody',
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
        recognize_action_req = facebody_20191230_models.RecognizeActionRequest()
        OpenApiUtilClient.convert(request, recognize_action_req)
        if not UtilClient.is_unset(request.urllist):
            i_0 = 0
            for item_0 in request.urllist:
                if not UtilClient.is_unset(item_0.urlobject):
                    auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
                    oss_config.access_key_id = auth_response.body.access_key_id
                    oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
                    oss_client = OSSClient(oss_config)
                    file_obj = file_form_models.FileField(
                        filename=auth_response.body.object_key,
                        content=item_0.urlobject,
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
                    tmp = recognize_action_req.urllist[i0]
                    tmp.url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        if not UtilClient.is_unset(request.video_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.video_url_object,
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
            recognize_action_req.video_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_action_resp = await self.recognize_action_with_options_async(recognize_action_req, runtime)
        return recognize_action_resp

    def recognize_expression_with_options(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeExpression',
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
            facebody_20191230_models.RecognizeExpressionResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_expression_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeExpression',
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
            facebody_20191230_models.RecognizeExpressionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_expression(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_expression_with_options(request, runtime)

    async def recognize_expression_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionRequest,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_expression_with_options_async(request, runtime)

    def recognize_expression_advance(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
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
            product='facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_expression_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_expression_resp = self.recognize_expression_with_options(recognize_expression_req, runtime)
        return recognize_expression_resp

    async def recognize_expression_advance_async(
        self,
        request: facebody_20191230_models.RecognizeExpressionAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeExpressionResponse:
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
            product='facebody',
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
        recognize_expression_req = facebody_20191230_models.RecognizeExpressionRequest()
        OpenApiUtilClient.convert(request, recognize_expression_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_expression_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_expression_resp = await self.recognize_expression_with_options_async(recognize_expression_req, runtime)
        return recognize_expression_resp

    def recognize_face_with_options(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.beauty):
            body['Beauty'] = request.beauty
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.glass):
            body['Glass'] = request.glass
        if not UtilClient.is_unset(request.hat):
            body['Hat'] = request.hat
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeFace',
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
            facebody_20191230_models.RecognizeFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.beauty):
            body['Beauty'] = request.beauty
        if not UtilClient.is_unset(request.expression):
            body['Expression'] = request.expression
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.glass):
            body['Glass'] = request.glass
        if not UtilClient.is_unset(request.hat):
            body['Hat'] = request.hat
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.max_face_number):
            body['MaxFaceNumber'] = request.max_face_number
        if not UtilClient.is_unset(request.quality):
            body['Quality'] = request.quality
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeFace',
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
            facebody_20191230_models.RecognizeFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_face(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_with_options(request, runtime)

    async def recognize_face_async(
        self,
        request: facebody_20191230_models.RecognizeFaceRequest,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_face_with_options_async(request, runtime)

    def recognize_face_advance(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
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
            product='facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_face_resp = self.recognize_face_with_options(recognize_face_req, runtime)
        return recognize_face_resp

    async def recognize_face_advance_async(
        self,
        request: facebody_20191230_models.RecognizeFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeFaceResponse:
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
            product='facebody',
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
        recognize_face_req = facebody_20191230_models.RecognizeFaceRequest()
        OpenApiUtilClient.convert(request, recognize_face_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_face_resp = await self.recognize_face_with_options_async(recognize_face_req, runtime)
        return recognize_face_resp

    def recognize_hand_gesture_with_options(
        self,
        request: facebody_20191230_models.RecognizeHandGestureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.gesture_type):
            body['GestureType'] = request.gesture_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeHandGesture',
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
            facebody_20191230_models.RecognizeHandGestureResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_hand_gesture_with_options_async(
        self,
        request: facebody_20191230_models.RecognizeHandGestureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.gesture_type):
            body['GestureType'] = request.gesture_type
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeHandGesture',
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
            facebody_20191230_models.RecognizeHandGestureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_hand_gesture(
        self,
        request: facebody_20191230_models.RecognizeHandGestureRequest,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_hand_gesture_with_options(request, runtime)

    async def recognize_hand_gesture_async(
        self,
        request: facebody_20191230_models.RecognizeHandGestureRequest,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_hand_gesture_with_options_async(request, runtime)

    def recognize_hand_gesture_advance(
        self,
        request: facebody_20191230_models.RecognizeHandGestureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
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
            product='facebody',
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
        recognize_hand_gesture_req = facebody_20191230_models.RecognizeHandGestureRequest()
        OpenApiUtilClient.convert(request, recognize_hand_gesture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_hand_gesture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_hand_gesture_resp = self.recognize_hand_gesture_with_options(recognize_hand_gesture_req, runtime)
        return recognize_hand_gesture_resp

    async def recognize_hand_gesture_advance_async(
        self,
        request: facebody_20191230_models.RecognizeHandGestureAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizeHandGestureResponse:
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
            product='facebody',
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
        recognize_hand_gesture_req = facebody_20191230_models.RecognizeHandGestureRequest()
        OpenApiUtilClient.convert(request, recognize_hand_gesture_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            recognize_hand_gesture_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        recognize_hand_gesture_resp = await self.recognize_hand_gesture_with_options_async(recognize_hand_gesture_req, runtime)
        return recognize_hand_gesture_resp

    def recognize_public_face_with_options(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePublicFace',
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
            facebody_20191230_models.RecognizePublicFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def recognize_public_face_with_options_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task):
            body['Task'] = request.task
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizePublicFace',
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
            facebody_20191230_models.RecognizePublicFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recognize_public_face(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_public_face_with_options(request, runtime)

    async def recognize_public_face_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceRequest,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_public_face_with_options_async(request, runtime)

    def recognize_public_face_advance(
        self,
        request: facebody_20191230_models.RecognizePublicFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
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
            product='facebody',
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
        recognize_public_face_req = facebody_20191230_models.RecognizePublicFaceRequest()
        OpenApiUtilClient.convert(request, recognize_public_face_req)
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
                    tmp = recognize_public_face_req.task[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_public_face_resp = self.recognize_public_face_with_options(recognize_public_face_req, runtime)
        return recognize_public_face_resp

    async def recognize_public_face_advance_async(
        self,
        request: facebody_20191230_models.RecognizePublicFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RecognizePublicFaceResponse:
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
            product='facebody',
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
        recognize_public_face_req = facebody_20191230_models.RecognizePublicFaceRequest()
        OpenApiUtilClient.convert(request, recognize_public_face_req)
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
                    tmp = recognize_public_face_req.task[i0]
                    tmp.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
                    i_0 = NumberClient.ltoi(NumberClient.add(NumberClient.itol(i_0), NumberClient.itol(1)))
        recognize_public_face_resp = await self.recognize_public_face_with_options_async(recognize_public_face_req, runtime)
        return recognize_public_face_resp

    def retouch_body_with_options(
        self,
        request: facebody_20191230_models.RetouchBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.lengthen_degree):
            body['LengthenDegree'] = request.lengthen_degree
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchBody',
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
            facebody_20191230_models.RetouchBodyResponse(),
            self.call_api(params, req, runtime)
        )

    async def retouch_body_with_options_async(
        self,
        request: facebody_20191230_models.RetouchBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchBodyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.lengthen_degree):
            body['LengthenDegree'] = request.lengthen_degree
        if not UtilClient.is_unset(request.slim_degree):
            body['SlimDegree'] = request.slim_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchBody',
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
            facebody_20191230_models.RetouchBodyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retouch_body(
        self,
        request: facebody_20191230_models.RetouchBodyRequest,
    ) -> facebody_20191230_models.RetouchBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.retouch_body_with_options(request, runtime)

    async def retouch_body_async(
        self,
        request: facebody_20191230_models.RetouchBodyRequest,
    ) -> facebody_20191230_models.RetouchBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retouch_body_with_options_async(request, runtime)

    def retouch_body_advance(
        self,
        request: facebody_20191230_models.RetouchBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchBodyResponse:
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
            product='facebody',
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
        retouch_body_req = facebody_20191230_models.RetouchBodyRequest()
        OpenApiUtilClient.convert(request, retouch_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            retouch_body_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        retouch_body_resp = self.retouch_body_with_options(retouch_body_req, runtime)
        return retouch_body_resp

    async def retouch_body_advance_async(
        self,
        request: facebody_20191230_models.RetouchBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchBodyResponse:
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
            product='facebody',
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
        retouch_body_req = facebody_20191230_models.RetouchBodyRequest()
        OpenApiUtilClient.convert(request, retouch_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            retouch_body_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        retouch_body_resp = await self.retouch_body_with_options_async(retouch_body_req, runtime)
        return retouch_body_resp

    def retouch_skin_with_options(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.retouch_degree):
            body['RetouchDegree'] = request.retouch_degree
        if not UtilClient.is_unset(request.whitening_degree):
            body['WhiteningDegree'] = request.whitening_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchSkin',
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
            facebody_20191230_models.RetouchSkinResponse(),
            self.call_api(params, req, runtime)
        )

    async def retouch_skin_with_options_async(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.retouch_degree):
            body['RetouchDegree'] = request.retouch_degree
        if not UtilClient.is_unset(request.whitening_degree):
            body['WhiteningDegree'] = request.whitening_degree
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetouchSkin',
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
            facebody_20191230_models.RetouchSkinResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retouch_skin(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        runtime = util_models.RuntimeOptions()
        return self.retouch_skin_with_options(request, runtime)

    async def retouch_skin_async(
        self,
        request: facebody_20191230_models.RetouchSkinRequest,
    ) -> facebody_20191230_models.RetouchSkinResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retouch_skin_with_options_async(request, runtime)

    def retouch_skin_advance(
        self,
        request: facebody_20191230_models.RetouchSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
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
            product='facebody',
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
        retouch_skin_req = facebody_20191230_models.RetouchSkinRequest()
        OpenApiUtilClient.convert(request, retouch_skin_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            retouch_skin_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        retouch_skin_resp = self.retouch_skin_with_options(retouch_skin_req, runtime)
        return retouch_skin_resp

    async def retouch_skin_advance_async(
        self,
        request: facebody_20191230_models.RetouchSkinAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.RetouchSkinResponse:
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
            product='facebody',
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
        retouch_skin_req = facebody_20191230_models.RetouchSkinRequest()
        OpenApiUtilClient.convert(request, retouch_skin_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            retouch_skin_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        retouch_skin_resp = await self.retouch_skin_with_options_async(retouch_skin_req, runtime)
        return retouch_skin_resp

    def search_face_with_options(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_names):
            body['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_face_num):
            body['MaxFaceNum'] = request.max_face_num
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
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
            facebody_20191230_models.SearchFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_face_with_options_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.db_names):
            body['DbNames'] = request.db_names
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.limit):
            body['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_face_num):
            body['MaxFaceNum'] = request.max_face_num
        if not UtilClient.is_unset(request.quality_score_threshold):
            body['QualityScoreThreshold'] = request.quality_score_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
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
            facebody_20191230_models.SearchFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_face(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    async def search_face_async(
        self,
        request: facebody_20191230_models.SearchFaceRequest,
    ) -> facebody_20191230_models.SearchFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_face_with_options_async(request, runtime)

    def search_face_advance(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
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
            product='facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            search_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_face_resp = self.search_face_with_options(search_face_req, runtime)
        return search_face_resp

    async def search_face_advance_async(
        self,
        request: facebody_20191230_models.SearchFaceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SearchFaceResponse:
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
            product='facebody',
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
        search_face_req = facebody_20191230_models.SearchFaceRequest()
        OpenApiUtilClient.convert(request, search_face_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
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
            search_face_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        search_face_resp = await self.search_face_with_options_async(search_face_req, runtime)
        return search_face_resp

    def swap_facial_features_with_options(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.edit_part):
            body['EditPart'] = request.edit_part
        if not UtilClient.is_unset(request.source_image_data):
            body['SourceImageData'] = request.source_image_data
        if not UtilClient.is_unset(request.source_image_url):
            body['SourceImageURL'] = request.source_image_url
        if not UtilClient.is_unset(request.target_image_data):
            body['TargetImageData'] = request.target_image_data
        if not UtilClient.is_unset(request.target_image_url):
            body['TargetImageURL'] = request.target_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwapFacialFeatures',
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
            facebody_20191230_models.SwapFacialFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def swap_facial_features_with_options_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.edit_part):
            body['EditPart'] = request.edit_part
        if not UtilClient.is_unset(request.source_image_data):
            body['SourceImageData'] = request.source_image_data
        if not UtilClient.is_unset(request.source_image_url):
            body['SourceImageURL'] = request.source_image_url
        if not UtilClient.is_unset(request.target_image_data):
            body['TargetImageData'] = request.target_image_data
        if not UtilClient.is_unset(request.target_image_url):
            body['TargetImageURL'] = request.target_image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SwapFacialFeatures',
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
            facebody_20191230_models.SwapFacialFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def swap_facial_features(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.swap_facial_features_with_options(request, runtime)

    async def swap_facial_features_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesRequest,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.swap_facial_features_with_options_async(request, runtime)

    def swap_facial_features_advance(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
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
            product='facebody',
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
        swap_facial_features_req = facebody_20191230_models.SwapFacialFeaturesRequest()
        OpenApiUtilClient.convert(request, swap_facial_features_req)
        if not UtilClient.is_unset(request.source_image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.source_image_urlobject,
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
            swap_facial_features_req.source_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.target_image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.target_image_urlobject,
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
            swap_facial_features_req.target_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        swap_facial_features_resp = self.swap_facial_features_with_options(swap_facial_features_req, runtime)
        return swap_facial_features_resp

    async def swap_facial_features_advance_async(
        self,
        request: facebody_20191230_models.SwapFacialFeaturesAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.SwapFacialFeaturesResponse:
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
            product='facebody',
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
        swap_facial_features_req = facebody_20191230_models.SwapFacialFeaturesRequest()
        OpenApiUtilClient.convert(request, swap_facial_features_req)
        if not UtilClient.is_unset(request.source_image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.source_image_urlobject,
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
            swap_facial_features_req.source_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.target_image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.target_image_urlobject,
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
            swap_facial_features_req.target_image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        swap_facial_features_resp = await self.swap_facial_features_with_options_async(swap_facial_features_req, runtime)
        return swap_facial_features_resp

    def update_face_entity_with_options(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaceEntity',
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
            facebody_20191230_models.UpdateFaceEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_entity_with_options_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        if not UtilClient.is_unset(request.entity_id):
            body['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateFaceEntity',
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
            facebody_20191230_models.UpdateFaceEntityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_face_entity(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_entity_with_options(request, runtime)

    async def update_face_entity_async(
        self,
        request: facebody_20191230_models.UpdateFaceEntityRequest,
    ) -> facebody_20191230_models.UpdateFaceEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_entity_with_options_async(request, runtime)

    def verify_face_mask_with_options(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.ref_data):
            body['RefData'] = request.ref_data
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyFaceMask',
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
            facebody_20191230_models.VerifyFaceMaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_face_mask_with_options_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_data):
            body['ImageData'] = request.image_data
        if not UtilClient.is_unset(request.image_url):
            body['ImageURL'] = request.image_url
        if not UtilClient.is_unset(request.ref_data):
            body['RefData'] = request.ref_data
        if not UtilClient.is_unset(request.ref_url):
            body['RefUrl'] = request.ref_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyFaceMask',
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
            facebody_20191230_models.VerifyFaceMaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_face_mask(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.verify_face_mask_with_options(request, runtime)

    async def verify_face_mask_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskRequest,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_face_mask_with_options_async(request, runtime)

    def verify_face_mask_advance(
        self,
        request: facebody_20191230_models.VerifyFaceMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
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
            product='facebody',
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
        verify_face_mask_req = facebody_20191230_models.VerifyFaceMaskRequest()
        OpenApiUtilClient.convert(request, verify_face_mask_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            verify_face_mask_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.ref_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.ref_url_object,
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
            verify_face_mask_req.ref_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        verify_face_mask_resp = self.verify_face_mask_with_options(verify_face_mask_req, runtime)
        return verify_face_mask_resp

    async def verify_face_mask_advance_async(
        self,
        request: facebody_20191230_models.VerifyFaceMaskAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> facebody_20191230_models.VerifyFaceMaskResponse:
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
            product='facebody',
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
        verify_face_mask_req = facebody_20191230_models.VerifyFaceMaskRequest()
        OpenApiUtilClient.convert(request, verify_face_mask_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_urlobject,
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
            verify_face_mask_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        if not UtilClient.is_unset(request.ref_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.ref_url_object,
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
            verify_face_mask_req.ref_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        verify_face_mask_resp = await self.verify_face_mask_with_options_async(verify_face_mask_req, runtime)
        return verify_face_mask_resp
