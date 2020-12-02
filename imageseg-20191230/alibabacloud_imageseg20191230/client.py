# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_imageseg20191230 import models as imageseg_20191230_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_oss_sdk.client import Client as OSSClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('imageseg', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def segment_hdsky(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentHDSkyResponse().from_map(self.do_request('SegmentHDSky', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_hdsky_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_hdsky(request, runtime)

    def segment_hdsky_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_hdsky_req = imageseg_20191230_models.SegmentHDSkyRequest()
        RPCUtilClient.convert(request, segment_hdsky_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_hdsky_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_hdsky_resp = self.segment_hdsky(segment_hdsky_req, runtime)
        return segment_hdsky_resp

    def segment_hdcommon_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentHDCommonImageResponse().from_map(self.do_request('SegmentHDCommonImage', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_hdcommon_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_hdcommon_image(request, runtime)

    def segment_hdcommon_image_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_hdcommon_image_req = imageseg_20191230_models.SegmentHDCommonImageRequest()
        RPCUtilClient.convert(request, segment_hdcommon_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_hdcommon_image_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_hdcommon_image_resp = self.segment_hdcommon_image(segment_hdcommon_image_req, runtime)
        return segment_hdcommon_image_resp

    def segment_skin(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentSkinResponse().from_map(self.do_request('SegmentSkin', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_skin_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_skin(request, runtime)

    def segment_skin_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_skin_req = imageseg_20191230_models.SegmentSkinRequest()
        RPCUtilClient.convert(request, segment_skin_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.urlobject,
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
        segment_skin_req.url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_skin_resp = self.segment_skin(segment_skin_req, runtime)
        return segment_skin_resp

    def change_sky(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.ChangeSkyResponse().from_map(self.do_request('ChangeSky', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def change_sky_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_sky(request, runtime)

    def change_sky_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        change_sky_req = imageseg_20191230_models.ChangeSkyRequest()
        RPCUtilClient.convert(request, change_sky_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        change_sky_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        change_sky_resp = self.change_sky(change_sky_req, runtime)
        return change_sky_resp

    def segment_logo(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentLogoResponse().from_map(self.do_request('SegmentLogo', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_logo_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_logo(request, runtime)

    def segment_logo_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_logo_req = imageseg_20191230_models.SegmentLogoRequest()
        RPCUtilClient.convert(request, segment_logo_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_logo_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_logo_resp = self.segment_logo(segment_logo_req, runtime)
        return segment_logo_resp

    def segment_scene(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentSceneResponse().from_map(self.do_request('SegmentScene', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_scene_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_scene(request, runtime)

    def segment_scene_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_scene_req = imageseg_20191230_models.SegmentSceneRequest()
        RPCUtilClient.convert(request, segment_scene_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_scene_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_scene_resp = self.segment_scene(segment_scene_req, runtime)
        return segment_scene_resp

    def segment_food(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentFoodResponse().from_map(self.do_request('SegmentFood', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_food_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_food(request, runtime)

    def segment_food_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_food_req = imageseg_20191230_models.SegmentFoodRequest()
        RPCUtilClient.convert(request, segment_food_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_food_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_food_resp = self.segment_food(segment_food_req, runtime)
        return segment_food_resp

    def segment_cloth(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentClothResponse().from_map(self.do_request('SegmentCloth', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_cloth_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_cloth(request, runtime)

    def segment_cloth_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_cloth_req = imageseg_20191230_models.SegmentClothRequest()
        RPCUtilClient.convert(request, segment_cloth_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_cloth_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_cloth_resp = self.segment_cloth(segment_cloth_req, runtime)
        return segment_cloth_resp

    def segment_animal(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentAnimalResponse().from_map(self.do_request('SegmentAnimal', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_animal_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_animal(request, runtime)

    def segment_animal_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_animal_req = imageseg_20191230_models.SegmentAnimalRequest()
        RPCUtilClient.convert(request, segment_animal_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_animal_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_animal_resp = self.segment_animal(segment_animal_req, runtime)
        return segment_animal_resp

    def segment_hdbody(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentHDBodyResponse().from_map(self.do_request('SegmentHDBody', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_hdbody_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_hdbody(request, runtime)

    def segment_hdbody_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_hdbody_req = imageseg_20191230_models.SegmentHDBodyRequest()
        RPCUtilClient.convert(request, segment_hdbody_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_hdbody_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_hdbody_resp = self.segment_hdbody(segment_hdbody_req, runtime)
        return segment_hdbody_resp

    def segment_sky(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentSkyResponse().from_map(self.do_request('SegmentSky', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_sky_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_sky(request, runtime)

    def segment_sky_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_sky_req = imageseg_20191230_models.SegmentSkyRequest()
        RPCUtilClient.convert(request, segment_sky_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_sky_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_sky_resp = self.segment_sky(segment_sky_req, runtime)
        return segment_sky_resp

    def get_async_job_result(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.GetAsyncJobResultResponse().from_map(self.do_request('GetAsyncJobResult', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def get_async_job_result_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result(request, runtime)

    def segment_furniture(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentFurnitureResponse().from_map(self.do_request('SegmentFurniture', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_furniture_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_furniture(request, runtime)

    def segment_furniture_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_furniture_req = imageseg_20191230_models.SegmentFurnitureRequest()
        RPCUtilClient.convert(request, segment_furniture_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_furniture_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_furniture_resp = self.segment_furniture(segment_furniture_req, runtime)
        return segment_furniture_resp

    def refine_mask(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.RefineMaskResponse().from_map(self.do_request('RefineMask', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def refine_mask_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refine_mask(request, runtime)

    def refine_mask_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        refine_mask_req = imageseg_20191230_models.RefineMaskRequest()
        RPCUtilClient.convert(request, refine_mask_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        refine_mask_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        refine_mask_resp = self.refine_mask(refine_mask_req, runtime)
        return refine_mask_resp

    def parse_face(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.ParseFaceResponse().from_map(self.do_request('ParseFace', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def parse_face_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.parse_face(request, runtime)

    def parse_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        parse_face_req = imageseg_20191230_models.ParseFaceRequest()
        RPCUtilClient.convert(request, parse_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        parse_face_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        parse_face_resp = self.parse_face(parse_face_req, runtime)
        return parse_face_resp

    def segment_vehicle(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentVehicleResponse().from_map(self.do_request('SegmentVehicle', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_vehicle_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_vehicle(request, runtime)

    def segment_vehicle_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_vehicle_req = imageseg_20191230_models.SegmentVehicleRequest()
        RPCUtilClient.convert(request, segment_vehicle_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_vehicle_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_vehicle_resp = self.segment_vehicle(segment_vehicle_req, runtime)
        return segment_vehicle_resp

    def segment_hair(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentHairResponse().from_map(self.do_request('SegmentHair', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_hair_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_hair(request, runtime)

    def segment_hair_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_hair_req = imageseg_20191230_models.SegmentHairRequest()
        RPCUtilClient.convert(request, segment_hair_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_hair_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_hair_resp = self.segment_hair(segment_hair_req, runtime)
        return segment_hair_resp

    def segment_face(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentFaceResponse().from_map(self.do_request('SegmentFace', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_face_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_face(request, runtime)

    def segment_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_face_req = imageseg_20191230_models.SegmentFaceRequest()
        RPCUtilClient.convert(request, segment_face_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_face_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_face_resp = self.segment_face(segment_face_req, runtime)
        return segment_face_resp

    def segment_head(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentHeadResponse().from_map(self.do_request('SegmentHead', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_head_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_head(request, runtime)

    def segment_head_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_head_req = imageseg_20191230_models.SegmentHeadRequest()
        RPCUtilClient.convert(request, segment_head_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_head_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_head_resp = self.segment_head(segment_head_req, runtime)
        return segment_head_resp

    def segment_commodity(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentCommodityResponse().from_map(self.do_request('SegmentCommodity', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_commodity_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_commodity(request, runtime)

    def segment_commodity_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_commodity_req = imageseg_20191230_models.SegmentCommodityRequest()
        RPCUtilClient.convert(request, segment_commodity_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_commodity_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_commodity_resp = self.segment_commodity(segment_commodity_req, runtime)
        return segment_commodity_resp

    def segment_body(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentBodyResponse().from_map(self.do_request('SegmentBody', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_body_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_body(request, runtime)

    def segment_body_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_body_req = imageseg_20191230_models.SegmentBodyRequest()
        RPCUtilClient.convert(request, segment_body_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_body_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_body_resp = self.segment_body(segment_body_req, runtime)
        return segment_body_resp

    def segment_common_image(self, request, runtime):
        UtilClient.validate_model(request)
        return imageseg_20191230_models.SegmentCommonImageResponse().from_map(self.do_request('SegmentCommonImage', 'HTTPS', 'POST', '2019-12-30', 'AK', None, TeaCore.to_map(request), runtime))

    def segment_common_image_simply(self, request):
        runtime = util_models.RuntimeOptions()
        return self.segment_common_image(request, runtime)

    def segment_common_image_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type='access_key',
            endpoint='openplatform.aliyuncs.com',
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='imageseg',
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
        RPCUtilClient.convert(runtime, oss_runtime)
        segment_common_image_req = imageseg_20191230_models.SegmentCommonImageRequest()
        RPCUtilClient.convert(request, segment_common_image_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
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
        segment_common_image_req.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        segment_common_image_resp = self.segment_common_image(segment_common_image_req, runtime)
        return segment_common_image_resp

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
