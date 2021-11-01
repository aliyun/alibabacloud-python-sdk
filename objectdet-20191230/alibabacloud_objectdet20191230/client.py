# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_objectdet20191230 import models as objectdet_20191230_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('objectdet', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def classify_vehicle_insurance_with_options(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.ClassifyVehicleInsuranceResponse(),
            self.do_rpcrequest('ClassifyVehicleInsurance', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def classify_vehicle_insurance_with_options_async(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.ClassifyVehicleInsuranceResponse(),
            await self.do_rpcrequest_async('ClassifyVehicleInsurance', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def classify_vehicle_insurance(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceRequest,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.classify_vehicle_insurance_with_options(request, runtime)

    async def classify_vehicle_insurance_async(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceRequest,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.classify_vehicle_insurance_with_options_async(request, runtime)

    def classify_vehicle_insurance_advance(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        classify_vehicle_insurance_req = objectdet_20191230_models.ClassifyVehicleInsuranceRequest()
        OpenApiUtilClient.convert(request, classify_vehicle_insurance_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            classify_vehicle_insurance_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_vehicle_insurance_resp = self.classify_vehicle_insurance_with_options(classify_vehicle_insurance_req, runtime)
        return classify_vehicle_insurance_resp

    async def classify_vehicle_insurance_advance_async(
        self,
        request: objectdet_20191230_models.ClassifyVehicleInsuranceAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.ClassifyVehicleInsuranceResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        classify_vehicle_insurance_req = objectdet_20191230_models.ClassifyVehicleInsuranceRequest()
        OpenApiUtilClient.convert(request, classify_vehicle_insurance_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            classify_vehicle_insurance_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        classify_vehicle_insurance_resp = await self.classify_vehicle_insurance_with_options_async(classify_vehicle_insurance_req, runtime)
        return classify_vehicle_insurance_resp

    def detect_ipcobject_with_options(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectIPCObjectResponse(),
            self.do_rpcrequest('DetectIPCObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_ipcobject_with_options_async(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectIPCObjectResponse(),
            await self.do_rpcrequest_async('DetectIPCObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_ipcobject(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_ipcobject_with_options(request, runtime)

    async def detect_ipcobject_async(
        self,
        request: objectdet_20191230_models.DetectIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectIPCObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_ipcobject_with_options_async(request, runtime)

    def detect_kitchen_animals_with_options(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectKitchenAnimalsResponse(),
            self.do_rpcrequest('DetectKitchenAnimals', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_kitchen_animals_with_options_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectKitchenAnimalsResponse(),
            await self.do_rpcrequest_async('DetectKitchenAnimals', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_kitchen_animals(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_kitchen_animals_with_options(request, runtime)

    async def detect_kitchen_animals_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsRequest,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_kitchen_animals_with_options_async(request, runtime)

    def detect_kitchen_animals_advance(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_kitchen_animals_req = objectdet_20191230_models.DetectKitchenAnimalsRequest()
        OpenApiUtilClient.convert(request, detect_kitchen_animals_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlaobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_kitchen_animals_req.image_urla = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_kitchen_animals_resp = self.detect_kitchen_animals_with_options(detect_kitchen_animals_req, runtime)
        return detect_kitchen_animals_resp

    async def detect_kitchen_animals_advance_async(
        self,
        request: objectdet_20191230_models.DetectKitchenAnimalsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectKitchenAnimalsResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_kitchen_animals_req = objectdet_20191230_models.DetectKitchenAnimalsRequest()
        OpenApiUtilClient.convert(request, detect_kitchen_animals_req)
        if not UtilClient.is_unset(request.image_urlaobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlaobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_kitchen_animals_req.image_urla = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_kitchen_animals_resp = await self.detect_kitchen_animals_with_options_async(detect_kitchen_animals_req, runtime)
        return detect_kitchen_animals_resp

    def detect_main_body_with_options(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectMainBodyResponse(),
            self.do_rpcrequest('DetectMainBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_main_body_with_options_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectMainBodyResponse(),
            await self.do_rpcrequest_async('DetectMainBody', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_main_body(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_main_body_with_options(request, runtime)

    async def detect_main_body_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyRequest,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_main_body_with_options_async(request, runtime)

    def detect_main_body_advance(
        self,
        request: objectdet_20191230_models.DetectMainBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_main_body_req = objectdet_20191230_models.DetectMainBodyRequest()
        OpenApiUtilClient.convert(request, detect_main_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_main_body_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_main_body_resp = self.detect_main_body_with_options(detect_main_body_req, runtime)
        return detect_main_body_resp

    async def detect_main_body_advance_async(
        self,
        request: objectdet_20191230_models.DetectMainBodyAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectMainBodyResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_main_body_req = objectdet_20191230_models.DetectMainBodyRequest()
        OpenApiUtilClient.convert(request, detect_main_body_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_main_body_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_main_body_resp = await self.detect_main_body_with_options_async(detect_main_body_req, runtime)
        return detect_main_body_resp

    def detect_object_with_options(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectObjectResponse(),
            self.do_rpcrequest('DetectObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_object_with_options_async(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectObjectResponse(),
            await self.do_rpcrequest_async('DetectObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_object(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_object_with_options(request, runtime)

    async def detect_object_async(
        self,
        request: objectdet_20191230_models.DetectObjectRequest,
    ) -> objectdet_20191230_models.DetectObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_object_with_options_async(request, runtime)

    def detect_object_advance(
        self,
        request: objectdet_20191230_models.DetectObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_object_req = objectdet_20191230_models.DetectObjectRequest()
        OpenApiUtilClient.convert(request, detect_object_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_object_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_object_resp = self.detect_object_with_options(detect_object_req, runtime)
        return detect_object_resp

    async def detect_object_advance_async(
        self,
        request: objectdet_20191230_models.DetectObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectObjectResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_object_req = objectdet_20191230_models.DetectObjectRequest()
        OpenApiUtilClient.convert(request, detect_object_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_object_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_object_resp = await self.detect_object_with_options_async(detect_object_req, runtime)
        return detect_object_resp

    def detect_transparent_image_with_options(
        self,
        request: objectdet_20191230_models.DetectTransparentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectTransparentImageResponse(),
            self.do_rpcrequest('DetectTransparentImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_transparent_image_with_options_async(
        self,
        request: objectdet_20191230_models.DetectTransparentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectTransparentImageResponse(),
            await self.do_rpcrequest_async('DetectTransparentImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_transparent_image(
        self,
        request: objectdet_20191230_models.DetectTransparentImageRequest,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_transparent_image_with_options(request, runtime)

    async def detect_transparent_image_async(
        self,
        request: objectdet_20191230_models.DetectTransparentImageRequest,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_transparent_image_with_options_async(request, runtime)

    def detect_transparent_image_advance(
        self,
        request: objectdet_20191230_models.DetectTransparentImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_transparent_image_req = objectdet_20191230_models.DetectTransparentImageRequest()
        OpenApiUtilClient.convert(request, detect_transparent_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_transparent_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_transparent_image_resp = self.detect_transparent_image_with_options(detect_transparent_image_req, runtime)
        return detect_transparent_image_resp

    async def detect_transparent_image_advance_async(
        self,
        request: objectdet_20191230_models.DetectTransparentImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectTransparentImageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_transparent_image_req = objectdet_20191230_models.DetectTransparentImageRequest()
        OpenApiUtilClient.convert(request, detect_transparent_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_transparent_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_transparent_image_resp = await self.detect_transparent_image_with_options_async(detect_transparent_image_req, runtime)
        return detect_transparent_image_resp

    def detect_vehicle_with_options(
        self,
        request: objectdet_20191230_models.DetectVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleResponse(),
            self.do_rpcrequest('DetectVehicle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_vehicle_with_options_async(
        self,
        request: objectdet_20191230_models.DetectVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleResponse(),
            await self.do_rpcrequest_async('DetectVehicle', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_vehicle(
        self,
        request: objectdet_20191230_models.DetectVehicleRequest,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_vehicle_with_options(request, runtime)

    async def detect_vehicle_async(
        self,
        request: objectdet_20191230_models.DetectVehicleRequest,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_vehicle_with_options_async(request, runtime)

    def detect_vehicle_advance(
        self,
        request: objectdet_20191230_models.DetectVehicleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_vehicle_req = objectdet_20191230_models.DetectVehicleRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_vehicle_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_vehicle_resp = self.detect_vehicle_with_options(detect_vehicle_req, runtime)
        return detect_vehicle_resp

    async def detect_vehicle_advance_async(
        self,
        request: objectdet_20191230_models.DetectVehicleAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_vehicle_req = objectdet_20191230_models.DetectVehicleRequest()
        OpenApiUtilClient.convert(request, detect_vehicle_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_vehicle_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_vehicle_resp = await self.detect_vehicle_with_options_async(detect_vehicle_req, runtime)
        return detect_vehicle_resp

    def detect_vehicle_icongestion_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleICongestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleICongestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pre_region_intersect_features):
            request.pre_region_intersect_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pre_region_intersect_features, 'PreRegionIntersectFeatures', 'json')
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleICongestionResponse(),
            self.do_rpcrequest('DetectVehicleICongestion', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_vehicle_icongestion_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleICongestionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleICongestionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.pre_region_intersect_features):
            request.pre_region_intersect_features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.pre_region_intersect_features, 'PreRegionIntersectFeatures', 'json')
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleICongestionResponse(),
            await self.do_rpcrequest_async('DetectVehicleICongestion', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_vehicle_icongestion(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionRequest,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_vehicle_icongestion_with_options(request, runtime)

    async def detect_vehicle_icongestion_async(
        self,
        request: objectdet_20191230_models.DetectVehicleICongestionRequest,
    ) -> objectdet_20191230_models.DetectVehicleICongestionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_vehicle_icongestion_with_options_async(request, runtime)

    def detect_vehicle_illegal_parking_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleIllegalParkingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleIllegalParkingResponse(),
            self.do_rpcrequest('DetectVehicleIllegalParking', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_vehicle_illegal_parking_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVehicleIllegalParkingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.road_regions):
            request.road_regions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.road_regions, 'RoadRegions', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVehicleIllegalParkingResponse(),
            await self.do_rpcrequest_async('DetectVehicleIllegalParking', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_vehicle_illegal_parking(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_vehicle_illegal_parking_with_options(request, runtime)

    async def detect_vehicle_illegal_parking_async(
        self,
        request: objectdet_20191230_models.DetectVehicleIllegalParkingRequest,
    ) -> objectdet_20191230_models.DetectVehicleIllegalParkingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_vehicle_illegal_parking_with_options_async(request, runtime)

    def detect_video_frame_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoFrameResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVideoFrameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.features):
            request.features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.features, 'Features', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVideoFrameResponse(),
            self.do_rpcrequest('DetectVideoFrame', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_video_frame_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectVideoFrameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoFrameResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectVideoFrameShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.features):
            request.features_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.features, 'Features', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVideoFrameResponse(),
            await self.do_rpcrequest_async('DetectVideoFrame', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_video_frame(
        self,
        request: objectdet_20191230_models.DetectVideoFrameRequest,
    ) -> objectdet_20191230_models.DetectVideoFrameResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_video_frame_with_options(request, runtime)

    async def detect_video_frame_async(
        self,
        request: objectdet_20191230_models.DetectVideoFrameRequest,
    ) -> objectdet_20191230_models.DetectVideoFrameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_frame_with_options_async(request, runtime)

    def detect_video_ipcobject_with_options(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVideoIPCObjectResponse(),
            self.do_rpcrequest('DetectVideoIPCObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_video_ipcobject_with_options_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectVideoIPCObjectResponse(),
            await self.do_rpcrequest_async('DetectVideoIPCObject', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_video_ipcobject(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_video_ipcobject_with_options(request, runtime)

    async def detect_video_ipcobject_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectRequest,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_video_ipcobject_with_options_async(request, runtime)

    def detect_video_ipcobject_advance(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_video_ipcobject_req = objectdet_20191230_models.DetectVideoIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_video_ipcobject_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.video_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_video_ipcobject_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_video_ipcobject_resp = self.detect_video_ipcobject_with_options(detect_video_ipcobject_req, runtime)
        return detect_video_ipcobject_resp

    async def detect_video_ipcobject_advance_async(
        self,
        request: objectdet_20191230_models.DetectVideoIPCObjectAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectVideoIPCObjectResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_video_ipcobject_req = objectdet_20191230_models.DetectVideoIPCObjectRequest()
        OpenApiUtilClient.convert(request, detect_video_ipcobject_req)
        if not UtilClient.is_unset(request.video_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.video_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_video_ipcobject_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_video_ipcobject_resp = await self.detect_video_ipcobject_with_options_async(detect_video_ipcobject_req, runtime)
        return detect_video_ipcobject_resp

    def detect_white_base_image_with_options(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectWhiteBaseImageResponse(),
            self.do_rpcrequest('DetectWhiteBaseImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_white_base_image_with_options_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectWhiteBaseImageResponse(),
            await self.do_rpcrequest_async('DetectWhiteBaseImage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_white_base_image(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_white_base_image_with_options(request, runtime)

    async def detect_white_base_image_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageRequest,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_white_base_image_with_options_async(request, runtime)

    def detect_white_base_image_advance(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_white_base_image_req = objectdet_20191230_models.DetectWhiteBaseImageRequest()
        OpenApiUtilClient.convert(request, detect_white_base_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_white_base_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_white_base_image_resp = self.detect_white_base_image_with_options(detect_white_base_image_req, runtime)
        return detect_white_base_image_resp

    async def detect_white_base_image_advance_async(
        self,
        request: objectdet_20191230_models.DetectWhiteBaseImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWhiteBaseImageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_white_base_image_req = objectdet_20191230_models.DetectWhiteBaseImageRequest()
        OpenApiUtilClient.convert(request, detect_white_base_image_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_white_base_image_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_white_base_image_resp = await self.detect_white_base_image_with_options_async(detect_white_base_image_req, runtime)
        return detect_white_base_image_resp

    def detect_workwear_with_options(
        self,
        tmp_req: objectdet_20191230_models.DetectWorkwearRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectWorkwearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clothes):
            request.clothes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.clothes), 'Clothes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectWorkwearResponse(),
            self.do_rpcrequest('DetectWorkwear', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_workwear_with_options_async(
        self,
        tmp_req: objectdet_20191230_models.DetectWorkwearRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        UtilClient.validate_model(tmp_req)
        request = objectdet_20191230_models.DetectWorkwearShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.clothes):
            request.clothes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.clothes), 'Clothes', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.DetectWorkwearResponse(),
            await self.do_rpcrequest_async('DetectWorkwear', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_workwear(
        self,
        request: objectdet_20191230_models.DetectWorkwearRequest,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_workwear_with_options(request, runtime)

    async def detect_workwear_async(
        self,
        request: objectdet_20191230_models.DetectWorkwearRequest,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_workwear_with_options_async(request, runtime)

    def detect_workwear_advance(
        self,
        request: objectdet_20191230_models.DetectWorkwearAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_workwear_req = objectdet_20191230_models.DetectWorkwearRequest()
        OpenApiUtilClient.convert(request, detect_workwear_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            detect_workwear_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_workwear_resp = self.detect_workwear_with_options(detect_workwear_req, runtime)
        return detect_workwear_resp

    async def detect_workwear_advance_async(
        self,
        request: objectdet_20191230_models.DetectWorkwearAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.DetectWorkwearResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        detect_workwear_req = objectdet_20191230_models.DetectWorkwearRequest()
        OpenApiUtilClient.convert(request, detect_workwear_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            detect_workwear_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        detect_workwear_resp = await self.detect_workwear_with_options_async(detect_workwear_req, runtime)
        return detect_workwear_resp

    def generate_vehicle_repair_plan_with_options(
        self,
        request: objectdet_20191230_models.GenerateVehicleRepairPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GenerateVehicleRepairPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GenerateVehicleRepairPlanResponse(),
            self.do_rpcrequest('GenerateVehicleRepairPlan', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_vehicle_repair_plan_with_options_async(
        self,
        request: objectdet_20191230_models.GenerateVehicleRepairPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GenerateVehicleRepairPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GenerateVehicleRepairPlanResponse(),
            await self.do_rpcrequest_async('GenerateVehicleRepairPlan', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_vehicle_repair_plan(
        self,
        request: objectdet_20191230_models.GenerateVehicleRepairPlanRequest,
    ) -> objectdet_20191230_models.GenerateVehicleRepairPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_vehicle_repair_plan_with_options(request, runtime)

    async def generate_vehicle_repair_plan_async(
        self,
        request: objectdet_20191230_models.GenerateVehicleRepairPlanRequest,
    ) -> objectdet_20191230_models.GenerateVehicleRepairPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_vehicle_repair_plan_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GetAsyncJobResultResponse(),
            self.do_rpcrequest('GetAsyncJobResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GetAsyncJobResultResponse(),
            await self.do_rpcrequest_async('GetAsyncJobResult', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: objectdet_20191230_models.GetAsyncJobResultRequest,
    ) -> objectdet_20191230_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def get_vehicle_repair_plan_with_options(
        self,
        request: objectdet_20191230_models.GetVehicleRepairPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetVehicleRepairPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GetVehicleRepairPlanResponse(),
            self.do_rpcrequest('GetVehicleRepairPlan', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_vehicle_repair_plan_with_options_async(
        self,
        request: objectdet_20191230_models.GetVehicleRepairPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.GetVehicleRepairPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.GetVehicleRepairPlanResponse(),
            await self.do_rpcrequest_async('GetVehicleRepairPlan', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_vehicle_repair_plan(
        self,
        request: objectdet_20191230_models.GetVehicleRepairPlanRequest,
    ) -> objectdet_20191230_models.GetVehicleRepairPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vehicle_repair_plan_with_options(request, runtime)

    async def get_vehicle_repair_plan_async(
        self,
        request: objectdet_20191230_models.GetVehicleRepairPlanRequest,
    ) -> objectdet_20191230_models.GetVehicleRepairPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vehicle_repair_plan_with_options_async(request, runtime)

    def recognize_vehicle_damage_with_options(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehicleDamageResponse(),
            self.do_rpcrequest('RecognizeVehicleDamage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_vehicle_damage_with_options_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehicleDamageResponse(),
            await self.do_rpcrequest_async('RecognizeVehicleDamage', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_damage(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageRequest,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_damage_with_options(request, runtime)

    async def recognize_vehicle_damage_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageRequest,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_damage_with_options_async(request, runtime)

    def recognize_vehicle_damage_advance(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_damage_req = objectdet_20191230_models.RecognizeVehicleDamageRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_damage_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            recognize_vehicle_damage_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_damage_resp = self.recognize_vehicle_damage_with_options(recognize_vehicle_damage_req, runtime)
        return recognize_vehicle_damage_resp

    async def recognize_vehicle_damage_advance_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDamageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDamageResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_damage_req = objectdet_20191230_models.RecognizeVehicleDamageRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_damage_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            recognize_vehicle_damage_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_damage_resp = await self.recognize_vehicle_damage_with_options_async(recognize_vehicle_damage_req, runtime)
        return recognize_vehicle_damage_resp

    def recognize_vehicle_dashboard_with_options(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehicleDashboardResponse(),
            self.do_rpcrequest('RecognizeVehicleDashboard', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_vehicle_dashboard_with_options_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehicleDashboardResponse(),
            await self.do_rpcrequest_async('RecognizeVehicleDashboard', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_dashboard(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardRequest,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_dashboard_with_options(request, runtime)

    async def recognize_vehicle_dashboard_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardRequest,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_dashboard_with_options_async(request, runtime)

    def recognize_vehicle_dashboard_advance(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_dashboard_req = objectdet_20191230_models.RecognizeVehicleDashboardRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_dashboard_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            recognize_vehicle_dashboard_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_dashboard_resp = self.recognize_vehicle_dashboard_with_options(recognize_vehicle_dashboard_req, runtime)
        return recognize_vehicle_dashboard_resp

    async def recognize_vehicle_dashboard_advance_async(
        self,
        request: objectdet_20191230_models.RecognizeVehicleDashboardAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehicleDashboardResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_dashboard_req = objectdet_20191230_models.RecognizeVehicleDashboardRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_dashboard_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            recognize_vehicle_dashboard_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_dashboard_resp = await self.recognize_vehicle_dashboard_with_options_async(recognize_vehicle_dashboard_req, runtime)
        return recognize_vehicle_dashboard_resp

    def recognize_vehicle_parts_with_options(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehiclePartsResponse(),
            self.do_rpcrequest('RecognizeVehicleParts', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_vehicle_parts_with_options_async(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            objectdet_20191230_models.RecognizeVehiclePartsResponse(),
            await self.do_rpcrequest_async('RecognizeVehicleParts', '2019-12-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_vehicle_parts(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsRequest,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_vehicle_parts_with_options(request, runtime)

    async def recognize_vehicle_parts_async(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsRequest,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_vehicle_parts_with_options_async(request, runtime)

    def recognize_vehicle_parts_advance(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_parts_req = objectdet_20191230_models.RecognizeVehiclePartsRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_parts_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            recognize_vehicle_parts_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_parts_resp = self.recognize_vehicle_parts_with_options(recognize_vehicle_parts_req, runtime)
        return recognize_vehicle_parts_resp

    async def recognize_vehicle_parts_advance_async(
        self,
        request: objectdet_20191230_models.RecognizeVehiclePartsAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> objectdet_20191230_models.RecognizeVehiclePartsResponse:
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
        auth_config = rpc_models.Config(
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
            product='objectdet',
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
        recognize_vehicle_parts_req = objectdet_20191230_models.RecognizeVehiclePartsRequest()
        OpenApiUtilClient.convert(request, recognize_vehicle_parts_req)
        if not UtilClient.is_unset(request.image_urlobject):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.image_urlobject,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            recognize_vehicle_parts_req.image_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        recognize_vehicle_parts_resp = await self.recognize_vehicle_parts_with_options_async(recognize_vehicle_parts_req, runtime)
        return recognize_vehicle_parts_resp
