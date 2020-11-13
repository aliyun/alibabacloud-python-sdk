# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_facebody20191230 import models as facebody_20191230_models
from alibabacloud_tea_util.client import Client as UtilClient
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
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("facebody", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def count_crowd(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.CountCrowdResponse().from_map(self.do_request("CountCrowd", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def count_crowd_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        count_crowdreq = facebody_20191230_models.CountCrowdRequest()
        RPCUtilClient.convert(request, count_crowdreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        count_crowdreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        count_crowd_resp = self.count_crowd(count_crowdreq, runtime)
        return count_crowd_resp

    def generate_human_anime_style(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.GenerateHumanAnimeStyleResponse().from_map(self.do_request("GenerateHumanAnimeStyle", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def generate_human_anime_style_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        generate_human_anime_stylereq = facebody_20191230_models.GenerateHumanAnimeStyleRequest()
        RPCUtilClient.convert(request, generate_human_anime_stylereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        generate_human_anime_stylereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        generate_human_anime_style_resp = self.generate_human_anime_style(generate_human_anime_stylereq, runtime)
        return generate_human_anime_style_resp

    def pedestrian_detect_attribute(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.PedestrianDetectAttributeResponse().from_map(self.do_request("PedestrianDetectAttribute", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def pedestrian_detect_attribute_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        pedestrian_detect_attributereq = facebody_20191230_models.PedestrianDetectAttributeRequest()
        RPCUtilClient.convert(request, pedestrian_detect_attributereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        pedestrian_detect_attributereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        pedestrian_detect_attribute_resp = self.pedestrian_detect_attribute(pedestrian_detect_attributereq, runtime)
        return pedestrian_detect_attribute_resp

    def detect_chef_cap(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectChefCapResponse().from_map(self.do_request("DetectChefCap", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_chef_cap_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_chef_capreq = facebody_20191230_models.DetectChefCapRequest()
        RPCUtilClient.convert(request, detect_chef_capreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_chef_capreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_chef_cap_resp = self.detect_chef_cap(detect_chef_capreq, runtime)
        return detect_chef_cap_resp

    def extract_pedestrian_feature_attr(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.ExtractPedestrianFeatureAttrResponse().from_map(self.do_request("ExtractPedestrianFeatureAttr", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def extract_pedestrian_feature_attr_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        extract_pedestrian_feature_attrreq = facebody_20191230_models.ExtractPedestrianFeatureAttrRequest()
        RPCUtilClient.convert(request, extract_pedestrian_feature_attrreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        extract_pedestrian_feature_attrreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        extract_pedestrian_feature_attr_resp = self.extract_pedestrian_feature_attr(extract_pedestrian_feature_attrreq, runtime)
        return extract_pedestrian_feature_attr_resp

    def detect_ipcpedestrian(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectIPCPedestrianResponse().from_map(self.do_request("DetectIPCPedestrian", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def blur_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.BlurFaceResponse().from_map(self.do_request("BlurFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def blur_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        blur_facereq = facebody_20191230_models.BlurFaceRequest()
        RPCUtilClient.convert(request, blur_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        blur_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        blur_face_resp = self.blur_face(blur_facereq, runtime)
        return blur_face_resp

    def extract_pedestrian_feature_attribute(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.ExtractPedestrianFeatureAttributeResponse().from_map(self.do_request("ExtractPedestrianFeatureAttribute", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_celebrity(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectCelebrityResponse().from_map(self.do_request("DetectCelebrity", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_celebrity_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_celebrityreq = facebody_20191230_models.DetectCelebrityRequest()
        RPCUtilClient.convert(request, detect_celebrityreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_celebrityreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_celebrity_resp = self.detect_celebrity(detect_celebrityreq, runtime)
        return detect_celebrity_resp

    def verify_face_mask(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.VerifyFaceMaskResponse().from_map(self.do_request("VerifyFaceMask", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def verify_face_mask_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        verify_face_maskreq = facebody_20191230_models.VerifyFaceMaskRequest()
        RPCUtilClient.convert(request, verify_face_maskreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        verify_face_maskreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        verify_face_mask_resp = self.verify_face_mask(verify_face_maskreq, runtime)
        return verify_face_mask_resp

    def recognize_action(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.RecognizeActionResponse().from_map(self.do_request("RecognizeAction", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_video_living_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectVideoLivingFaceResponse().from_map(self.do_request("DetectVideoLivingFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_video_living_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_video_living_facereq = facebody_20191230_models.DetectVideoLivingFaceRequest()
        RPCUtilClient.convert(request, detect_video_living_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_url_object,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_video_living_facereq.video_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_video_living_face_resp = self.detect_video_living_face(detect_video_living_facereq, runtime)
        return detect_video_living_face_resp

    def swap_facial_features(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.SwapFacialFeaturesResponse().from_map(self.do_request("SwapFacialFeatures", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def swap_facial_features_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        swap_facial_featuresreq = facebody_20191230_models.SwapFacialFeaturesRequest()
        RPCUtilClient.convert(request, swap_facial_featuresreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.source_image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        swap_facial_featuresreq.source_image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        swap_facial_features_resp = self.swap_facial_features(swap_facial_featuresreq, runtime)
        return swap_facial_features_resp

    def add_face_entity(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.AddFaceEntityResponse().from_map(self.do_request("AddFaceEntity", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def delete_face_entity(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DeleteFaceEntityResponse().from_map(self.do_request("DeleteFaceEntity", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def list_face_entities(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.ListFaceEntitiesResponse().from_map(self.do_request("ListFaceEntities", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def get_face_entity(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.GetFaceEntityResponse().from_map(self.do_request("GetFaceEntity", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def update_face_entity(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.UpdateFaceEntityResponse().from_map(self.do_request("UpdateFaceEntity", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def face_makeup(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.FaceMakeupResponse().from_map(self.do_request("FaceMakeup", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def face_makeup_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        face_makeupreq = facebody_20191230_models.FaceMakeupRequest()
        RPCUtilClient.convert(request, face_makeupreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_makeupreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        face_makeup_resp = self.face_makeup(face_makeupreq, runtime)
        return face_makeup_resp

    def hand_posture(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.HandPostureResponse().from_map(self.do_request("HandPosture", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def hand_posture_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        hand_posturereq = facebody_20191230_models.HandPostureRequest()
        RPCUtilClient.convert(request, hand_posturereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        hand_posturereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        hand_posture_resp = self.hand_posture(hand_posturereq, runtime)
        return hand_posture_resp

    def body_posture(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.BodyPostureResponse().from_map(self.do_request("BodyPosture", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def body_posture_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        body_posturereq = facebody_20191230_models.BodyPostureRequest()
        RPCUtilClient.convert(request, body_posturereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        body_posturereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        body_posture_resp = self.body_posture(body_posturereq, runtime)
        return body_posture_resp

    def detect_pedestrian(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectPedestrianResponse().from_map(self.do_request("DetectPedestrian", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_pedestrian_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_pedestrianreq = facebody_20191230_models.DetectPedestrianRequest()
        RPCUtilClient.convert(request, detect_pedestrianreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_pedestrianreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_pedestrian_resp = self.detect_pedestrian(detect_pedestrianreq, runtime)
        return detect_pedestrian_resp

    def face_beauty(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.FaceBeautyResponse().from_map(self.do_request("FaceBeauty", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def face_beauty_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        face_beautyreq = facebody_20191230_models.FaceBeautyRequest()
        RPCUtilClient.convert(request, face_beautyreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_beautyreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        face_beauty_resp = self.face_beauty(face_beautyreq, runtime)
        return face_beauty_resp

    def face_filter(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.FaceFilterResponse().from_map(self.do_request("FaceFilter", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def face_filter_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        face_filterreq = facebody_20191230_models.FaceFilterRequest()
        RPCUtilClient.convert(request, face_filterreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_filterreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        face_filter_resp = self.face_filter(face_filterreq, runtime)
        return face_filter_resp

    def enhance_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.EnhanceFaceResponse().from_map(self.do_request("EnhanceFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def enhance_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        enhance_facereq = facebody_20191230_models.EnhanceFaceRequest()
        RPCUtilClient.convert(request, enhance_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        enhance_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        enhance_face_resp = self.enhance_face(enhance_facereq, runtime)
        return enhance_face_resp

    def face_tidyup(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.FaceTidyupResponse().from_map(self.do_request("FaceTidyup", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def face_tidyup_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        face_tidyupreq = facebody_20191230_models.FaceTidyupRequest()
        RPCUtilClient.convert(request, face_tidyupreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        face_tidyupreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        face_tidyup_resp = self.face_tidyup(face_tidyupreq, runtime)
        return face_tidyup_resp

    def search_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.SearchFaceResponse().from_map(self.do_request("SearchFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def search_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        search_facereq = facebody_20191230_models.SearchFaceRequest()
        RPCUtilClient.convert(request, search_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        search_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        search_face_resp = self.search_face(search_facereq, runtime)
        return search_face_resp

    def list_face_dbs(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.ListFaceDbsResponse().from_map(self.do_request("ListFaceDbs", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def create_face_db(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.CreateFaceDbResponse().from_map(self.do_request("CreateFaceDb", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def delete_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DeleteFaceResponse().from_map(self.do_request("DeleteFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def delete_face_db(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DeleteFaceDbResponse().from_map(self.do_request("DeleteFaceDb", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def add_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.AddFaceResponse().from_map(self.do_request("AddFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def add_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        add_facereq = facebody_20191230_models.AddFaceRequest()
        RPCUtilClient.convert(request, add_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_url_object,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        add_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        add_face_resp = self.add_face(add_facereq, runtime)
        return add_face_resp

    def recognize_expression(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.RecognizeExpressionResponse().from_map(self.do_request("RecognizeExpression", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def recognize_expression_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        recognize_expressionreq = facebody_20191230_models.RecognizeExpressionRequest()
        RPCUtilClient.convert(request, recognize_expressionreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        recognize_expressionreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        recognize_expression_resp = self.recognize_expression(recognize_expressionreq, runtime)
        return recognize_expression_resp

    def recognize_public_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.RecognizePublicFaceResponse().from_map(self.do_request("RecognizePublicFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_living_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectLivingFaceResponse().from_map(self.do_request("DetectLivingFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_body_count(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectBodyCountResponse().from_map(self.do_request("DetectBodyCount", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_body_count_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_body_countreq = facebody_20191230_models.DetectBodyCountRequest()
        RPCUtilClient.convert(request, detect_body_countreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_body_countreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_body_count_resp = self.detect_body_count(detect_body_countreq, runtime)
        return detect_body_count_resp

    def detect_mask(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectMaskResponse().from_map(self.do_request("DetectMask", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_mask_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_maskreq = facebody_20191230_models.DetectMaskRequest()
        RPCUtilClient.convert(request, detect_maskreq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_maskreq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_mask_resp = self.detect_mask(detect_maskreq, runtime)
        return detect_mask_resp

    def recognize_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.RecognizeFaceResponse().from_map(self.do_request("RecognizeFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def recognize_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        recognize_facereq = facebody_20191230_models.RecognizeFaceRequest()
        RPCUtilClient.convert(request, recognize_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        recognize_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        recognize_face_resp = self.recognize_face(recognize_facereq, runtime)
        return recognize_face_resp

    def compare_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.CompareFaceResponse().from_map(self.do_request("CompareFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_face(self, request, runtime):
        UtilClient.validate_model(request)
        return facebody_20191230_models.DetectFaceResponse().from_map(self.do_request("DetectFace", "HTTPS", "POST", "2019-12-30", "AK", None, request.to_map(), runtime))

    def detect_face_advance(self, request, runtime):
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        auth_config = rpc_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            type="access_key",
            endpoint="openplatform.aliyuncs.com",
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product="facebody",
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type="access_key",
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        RPCUtilClient.convert(runtime, oss_runtime)
        detect_facereq = facebody_20191230_models.DetectFaceRequest()
        RPCUtilClient.convert(request, detect_facereq)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = RPCUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.image_urlobject,
            content_type=""
        )
        oss_header = oss_models.PostObjectRequestHeader(
            access_key_id=auth_response.access_key_id,
            policy=auth_response.encoded_policy,
            signature=auth_response.signature,
            key=auth_response.object_key,
            file=file_obj,
            success_action_status="201"
        )
        upload_request = oss_models.PostObjectRequest(
            bucket_name=auth_response.bucket,
            header=oss_header
        )
        oss_client.post_object(upload_request, oss_runtime)
        detect_facereq.image_url = 'http://%s.%s/%s' % (auth_response.bucket, auth_response.endpoint, auth_response.object_key)
        detect_face_resp = self.detect_face(detect_facereq, runtime)
        return detect_face_resp

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
