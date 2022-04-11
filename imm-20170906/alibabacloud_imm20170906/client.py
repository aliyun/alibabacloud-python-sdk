# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20170906 import models as imm_20170906_models
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
        self._endpoint_map = {
            'cn-beijing-gov-1': 'imm-vpc.cn-beijing-gov-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('imm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def compare_image_faces_with_options(
        self,
        request: imm_20170906_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CompareImageFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id_a):
            query['FaceIdA'] = request.face_id_a
        if not UtilClient.is_unset(request.face_id_b):
            query['FaceIdB'] = request.face_id_b
        if not UtilClient.is_unset(request.image_uri_a):
            query['ImageUriA'] = request.image_uri_a
        if not UtilClient.is_unset(request.image_uri_b):
            query['ImageUriB'] = request.image_uri_b
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CompareImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_image_faces_with_options_async(
        self,
        request: imm_20170906_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CompareImageFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id_a):
            query['FaceIdA'] = request.face_id_a
        if not UtilClient.is_unset(request.face_id_b):
            query['FaceIdB'] = request.face_id_b
        if not UtilClient.is_unset(request.image_uri_a):
            query['ImageUriA'] = request.image_uri_a
        if not UtilClient.is_unset(request.image_uri_b):
            query['ImageUriB'] = request.image_uri_b
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CompareImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_image_faces(
        self,
        request: imm_20170906_models.CompareImageFacesRequest,
    ) -> imm_20170906_models.CompareImageFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    async def compare_image_faces_async(
        self,
        request: imm_20170906_models.CompareImageFacesRequest,
    ) -> imm_20170906_models.CompareImageFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.compare_image_faces_with_options_async(request, runtime)

    def convert_office_format_with_options(
        self,
        request: imm_20170906_models.ConvertOfficeFormatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ConvertOfficeFormatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.fit_to_pages_tall):
            query['FitToPagesTall'] = request.fit_to_pages_tall
        if not UtilClient.is_unset(request.fit_to_pages_wide):
            query['FitToPagesWide'] = request.fit_to_pages_wide
        if not UtilClient.is_unset(request.hidecomments):
            query['Hidecomments'] = request.hidecomments
        if not UtilClient.is_unset(request.max_sheet_col):
            query['MaxSheetCol'] = request.max_sheet_col
        if not UtilClient.is_unset(request.max_sheet_count):
            query['MaxSheetCount'] = request.max_sheet_count
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pdf_vector):
            query['PdfVector'] = request.pdf_vector
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.sheet_one_page):
            query['SheetOnePage'] = request.sheet_one_page
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tgt_file_pages):
            query['TgtFilePages'] = request.tgt_file_pages
        if not UtilClient.is_unset(request.tgt_file_prefix):
            query['TgtFilePrefix'] = request.tgt_file_prefix
        if not UtilClient.is_unset(request.tgt_file_suffix):
            query['TgtFileSuffix'] = request.tgt_file_suffix
        if not UtilClient.is_unset(request.tgt_type):
            query['TgtType'] = request.tgt_type
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertOfficeFormat',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ConvertOfficeFormatResponse(),
            self.call_api(params, req, runtime)
        )

    async def convert_office_format_with_options_async(
        self,
        request: imm_20170906_models.ConvertOfficeFormatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ConvertOfficeFormatResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.fit_to_pages_tall):
            query['FitToPagesTall'] = request.fit_to_pages_tall
        if not UtilClient.is_unset(request.fit_to_pages_wide):
            query['FitToPagesWide'] = request.fit_to_pages_wide
        if not UtilClient.is_unset(request.hidecomments):
            query['Hidecomments'] = request.hidecomments
        if not UtilClient.is_unset(request.max_sheet_col):
            query['MaxSheetCol'] = request.max_sheet_col
        if not UtilClient.is_unset(request.max_sheet_count):
            query['MaxSheetCount'] = request.max_sheet_count
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pdf_vector):
            query['PdfVector'] = request.pdf_vector
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.sheet_one_page):
            query['SheetOnePage'] = request.sheet_one_page
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tgt_file_pages):
            query['TgtFilePages'] = request.tgt_file_pages
        if not UtilClient.is_unset(request.tgt_file_prefix):
            query['TgtFilePrefix'] = request.tgt_file_prefix
        if not UtilClient.is_unset(request.tgt_file_suffix):
            query['TgtFileSuffix'] = request.tgt_file_suffix
        if not UtilClient.is_unset(request.tgt_type):
            query['TgtType'] = request.tgt_type
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertOfficeFormat',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ConvertOfficeFormatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def convert_office_format(
        self,
        request: imm_20170906_models.ConvertOfficeFormatRequest,
    ) -> imm_20170906_models.ConvertOfficeFormatResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_office_format_with_options(request, runtime)

    async def convert_office_format_async(
        self,
        request: imm_20170906_models.ConvertOfficeFormatRequest,
    ) -> imm_20170906_models.ConvertOfficeFormatResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_office_format_with_options_async(request, runtime)

    def create_grab_frame_task_with_options(
        self,
        request: imm_20170906_models.CreateGrabFrameTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGrabFrameTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_list):
            query['TargetList'] = request.target_list
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGrabFrameTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGrabFrameTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grab_frame_task_with_options_async(
        self,
        request: imm_20170906_models.CreateGrabFrameTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGrabFrameTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_list):
            query['TargetList'] = request.target_list
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGrabFrameTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGrabFrameTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grab_frame_task(
        self,
        request: imm_20170906_models.CreateGrabFrameTaskRequest,
    ) -> imm_20170906_models.CreateGrabFrameTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_grab_frame_task_with_options(request, runtime)

    async def create_grab_frame_task_async(
        self,
        request: imm_20170906_models.CreateGrabFrameTaskRequest,
    ) -> imm_20170906_models.CreateGrabFrameTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_grab_frame_task_with_options_async(request, runtime)

    def create_group_faces_job_with_options(
        self,
        request: imm_20170906_models.CreateGroupFacesJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGroupFacesJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupFacesJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGroupFacesJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_faces_job_with_options_async(
        self,
        request: imm_20170906_models.CreateGroupFacesJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGroupFacesJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroupFacesJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateGroupFacesJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_faces_job(
        self,
        request: imm_20170906_models.CreateGroupFacesJobRequest,
    ) -> imm_20170906_models.CreateGroupFacesJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_faces_job_with_options(request, runtime)

    async def create_group_faces_job_async(
        self,
        request: imm_20170906_models.CreateGroupFacesJobRequest,
    ) -> imm_20170906_models.CreateGroupFacesJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_faces_job_with_options_async(request, runtime)

    def create_merge_face_groups_job_with_options(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.group_id_from):
            query['GroupIdFrom'] = request.group_id_from
        if not UtilClient.is_unset(request.group_id_to):
            query['GroupIdTo'] = request.group_id_to
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMergeFaceGroupsJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMergeFaceGroupsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_merge_face_groups_job_with_options_async(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.group_id_from):
            query['GroupIdFrom'] = request.group_id_from
        if not UtilClient.is_unset(request.group_id_to):
            query['GroupIdTo'] = request.group_id_to
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMergeFaceGroupsJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMergeFaceGroupsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_merge_face_groups_job(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_merge_face_groups_job_with_options(request, runtime)

    async def create_merge_face_groups_job_async(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_merge_face_groups_job_with_options_async(request, runtime)

    def create_office_conversion_task_with_options(
        self,
        request: imm_20170906_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_dpi):
            query['DisplayDpi'] = request.display_dpi
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.fit_to_pages_tall):
            query['FitToPagesTall'] = request.fit_to_pages_tall
        if not UtilClient.is_unset(request.fit_to_pages_wide):
            query['FitToPagesWide'] = request.fit_to_pages_wide
        if not UtilClient.is_unset(request.hidecomments):
            query['Hidecomments'] = request.hidecomments
        if not UtilClient.is_unset(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not UtilClient.is_unset(request.max_sheet_col):
            query['MaxSheetCol'] = request.max_sheet_col
        if not UtilClient.is_unset(request.max_sheet_count):
            query['MaxSheetCount'] = request.max_sheet_count
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pdf_vector):
            query['PdfVector'] = request.pdf_vector
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.sheet_one_page):
            query['SheetOnePage'] = request.sheet_one_page
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tgt_file_pages):
            query['TgtFilePages'] = request.tgt_file_pages
        if not UtilClient.is_unset(request.tgt_file_prefix):
            query['TgtFilePrefix'] = request.tgt_file_prefix
        if not UtilClient.is_unset(request.tgt_file_suffix):
            query['TgtFileSuffix'] = request.tgt_file_suffix
        if not UtilClient.is_unset(request.tgt_type):
            query['TgtType'] = request.tgt_type
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_dpi):
            query['DisplayDpi'] = request.display_dpi
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.fit_to_pages_tall):
            query['FitToPagesTall'] = request.fit_to_pages_tall
        if not UtilClient.is_unset(request.fit_to_pages_wide):
            query['FitToPagesWide'] = request.fit_to_pages_wide
        if not UtilClient.is_unset(request.hidecomments):
            query['Hidecomments'] = request.hidecomments
        if not UtilClient.is_unset(request.idempotent_token):
            query['IdempotentToken'] = request.idempotent_token
        if not UtilClient.is_unset(request.max_sheet_col):
            query['MaxSheetCol'] = request.max_sheet_col
        if not UtilClient.is_unset(request.max_sheet_count):
            query['MaxSheetCount'] = request.max_sheet_count
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pdf_vector):
            query['PdfVector'] = request.pdf_vector
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.sheet_one_page):
            query['SheetOnePage'] = request.sheet_one_page
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tgt_file_pages):
            query['TgtFilePages'] = request.tgt_file_pages
        if not UtilClient.is_unset(request.tgt_file_prefix):
            query['TgtFilePrefix'] = request.tgt_file_prefix
        if not UtilClient.is_unset(request.tgt_file_suffix):
            query['TgtFileSuffix'] = request.tgt_file_suffix
        if not UtilClient.is_unset(request.tgt_type):
            query['TgtType'] = request.tgt_type
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_office_conversion_task(
        self,
        request: imm_20170906_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20170906_models.CreateOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    async def create_office_conversion_task_async(
        self,
        request: imm_20170906_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20170906_models.CreateOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_office_conversion_task_with_options_async(request, runtime)

    def create_set_with_options(
        self,
        request: imm_20170906_models.CreateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.set_name):
            query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_set_with_options_async(
        self,
        request: imm_20170906_models.CreateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.set_name):
            query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_set(
        self,
        request: imm_20170906_models.CreateSetRequest,
    ) -> imm_20170906_models.CreateSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_set_with_options(request, runtime)

    async def create_set_async(
        self,
        request: imm_20170906_models.CreateSetRequest,
    ) -> imm_20170906_models.CreateSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_set_with_options_async(request, runtime)

    def create_video_compress_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_list):
            query['TargetList'] = request.target_list
        if not UtilClient.is_unset(request.target_segment):
            query['TargetSegment'] = request.target_segment
        if not UtilClient.is_unset(request.target_subtitle):
            query['TargetSubtitle'] = request.target_subtitle
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoCompressTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoCompressTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_compress_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_list):
            query['TargetList'] = request.target_list
        if not UtilClient.is_unset(request.target_segment):
            query['TargetSegment'] = request.target_segment
        if not UtilClient.is_unset(request.target_subtitle):
            query['TargetSubtitle'] = request.target_subtitle
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoCompressTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoCompressTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_compress_task(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_compress_task_with_options(request, runtime)

    async def create_video_compress_task_async(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_compress_task_with_options_async(request, runtime)

    def decode_blind_watermark_with_options(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageUri'] = request.original_image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_uri):
            query['TargetUri'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DecodeBlindWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def decode_blind_watermark_with_options_async(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageUri'] = request.original_image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_uri):
            query['TargetUri'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DecodeBlindWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decode_blind_watermark(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.decode_blind_watermark_with_options(request, runtime)

    async def decode_blind_watermark_async(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decode_blind_watermark_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: imm_20170906_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: imm_20170906_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image(
        self,
        request: imm_20170906_models.DeleteImageRequest,
    ) -> imm_20170906_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: imm_20170906_models.DeleteImageRequest,
    ) -> imm_20170906_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_office_conversion_task_with_options(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_office_conversion_task(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_office_conversion_task_with_options(request, runtime)

    async def delete_office_conversion_task_async(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_office_conversion_task_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: imm_20170906_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: imm_20170906_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: imm_20170906_models.DeleteProjectRequest,
    ) -> imm_20170906_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: imm_20170906_models.DeleteProjectRequest,
    ) -> imm_20170906_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_set_with_options(
        self,
        request: imm_20170906_models.DeleteSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_set_with_options_async(
        self,
        request: imm_20170906_models.DeleteSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_set(
        self,
        request: imm_20170906_models.DeleteSetRequest,
    ) -> imm_20170906_models.DeleteSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_set_with_options(request, runtime)

    async def delete_set_async(
        self,
        request: imm_20170906_models.DeleteSetRequest,
    ) -> imm_20170906_models.DeleteSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_set_with_options_async(request, runtime)

    def delete_video_with_options(
        self,
        request: imm_20170906_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_video_with_options_async(
        self,
        request: imm_20170906_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_video(
        self,
        request: imm_20170906_models.DeleteVideoRequest,
    ) -> imm_20170906_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_video_with_options(request, runtime)

    async def delete_video_async(
        self,
        request: imm_20170906_models.DeleteVideoRequest,
    ) -> imm_20170906_models.DeleteVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_video_with_options_async(request, runtime)

    def delete_video_task_with_options(
        self,
        request: imm_20170906_models.DeleteVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_video_task_with_options_async(
        self,
        request: imm_20170906_models.DeleteVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_video_task(
        self,
        request: imm_20170906_models.DeleteVideoTaskRequest,
    ) -> imm_20170906_models.DeleteVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_video_task_with_options(request, runtime)

    async def delete_video_task_async(
        self,
        request: imm_20170906_models.DeleteVideoTaskRequest,
    ) -> imm_20170906_models.DeleteVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_video_task_with_options_async(request, runtime)

    def detect_image_bodies_with_options(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageBodiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_bodies_with_options_async(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageBodiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_bodies(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    async def detect_image_bodies_async(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_bodies_with_options_async(request, runtime)

    def detect_image_faces_with_options(
        self,
        request: imm_20170906_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_faces_with_options_async(
        self,
        request: imm_20170906_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_faces(
        self,
        request: imm_20170906_models.DetectImageFacesRequest,
    ) -> imm_20170906_models.DetectImageFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    async def detect_image_faces_async(
        self,
        request: imm_20170906_models.DetectImageFacesRequest,
    ) -> imm_20170906_models.DetectImageFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_faces_with_options_async(request, runtime)

    def detect_image_qrcodes_with_options(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageQRCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_qrcodes_with_options_async(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageQRCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_qrcodes(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_qrcodes_with_options(request, runtime)

    async def detect_image_qrcodes_async(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_qrcodes_with_options_async(request, runtime)

    def detect_image_tags_with_options(
        self,
        request: imm_20170906_models.DetectImageTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_tags_with_options_async(
        self,
        request: imm_20170906_models.DetectImageTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_tags(
        self,
        request: imm_20170906_models.DetectImageTagsRequest,
    ) -> imm_20170906_models.DetectImageTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_tags_with_options(request, runtime)

    async def detect_image_tags_async(
        self,
        request: imm_20170906_models.DetectImageTagsRequest,
    ) -> imm_20170906_models.DetectImageTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_tags_with_options_async(request, runtime)

    def detect_qrcodes_with_options(
        self,
        request: imm_20170906_models.DetectQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectQRCodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_uris):
            query['SrcUris'] = request.src_uris
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectQRCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_qrcodes_with_options_async(
        self,
        request: imm_20170906_models.DetectQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectQRCodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_uris):
            query['SrcUris'] = request.src_uris
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectQRCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_qrcodes(
        self,
        request: imm_20170906_models.DetectQRCodesRequest,
    ) -> imm_20170906_models.DetectQRCodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_qrcodes_with_options(request, runtime)

    async def detect_qrcodes_async(
        self,
        request: imm_20170906_models.DetectQRCodesRequest,
    ) -> imm_20170906_models.DetectQRCodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_qrcodes_with_options_async(request, runtime)

    def encode_blind_watermark_with_options(
        self,
        request: imm_20170906_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.EncodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_image_type):
            query['TargetImageType'] = request.target_image_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetUri'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_uri):
            query['WatermarkUri'] = request.watermark_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.EncodeBlindWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def encode_blind_watermark_with_options_async(
        self,
        request: imm_20170906_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.EncodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.target_image_type):
            query['TargetImageType'] = request.target_image_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetUri'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_uri):
            query['WatermarkUri'] = request.watermark_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.EncodeBlindWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encode_blind_watermark(
        self,
        request: imm_20170906_models.EncodeBlindWatermarkRequest,
    ) -> imm_20170906_models.EncodeBlindWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return self.encode_blind_watermark_with_options(request, runtime)

    async def encode_blind_watermark_async(
        self,
        request: imm_20170906_models.EncodeBlindWatermarkRequest,
    ) -> imm_20170906_models.EncodeBlindWatermarkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.encode_blind_watermark_with_options_async(request, runtime)

    def find_images_with_options(
        self,
        request: imm_20170906_models.FindImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_line_contents_match):
            query['AddressLineContentsMatch'] = request.address_line_contents_match
        if not UtilClient.is_unset(request.age_range):
            query['AgeRange'] = request.age_range
        if not UtilClient.is_unset(request.create_time_range):
            query['CreateTimeRange'] = request.create_time_range
        if not UtilClient.is_unset(request.emotion):
            query['Emotion'] = request.emotion
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.faces_modify_time_range):
            query['FacesModifyTimeRange'] = request.faces_modify_time_range
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_size_range):
            query['ImageSizeRange'] = request.image_size_range
        if not UtilClient.is_unset(request.image_time_range):
            query['ImageTimeRange'] = request.image_time_range
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.location_boundary):
            query['LocationBoundary'] = request.location_boundary
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.modify_time_range):
            query['ModifyTimeRange'] = request.modify_time_range
        if not UtilClient.is_unset(request.ocrcontents_match):
            query['OCRContentsMatch'] = request.ocrcontents_match
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_aprefix):
            query['RemarksAPrefix'] = request.remarks_aprefix
        if not UtilClient.is_unset(request.remarks_array_ain):
            query['RemarksArrayAIn'] = request.remarks_array_ain
        if not UtilClient.is_unset(request.remarks_array_bin):
            query['RemarksArrayBIn'] = request.remarks_array_bin
        if not UtilClient.is_unset(request.remarks_bprefix):
            query['RemarksBPrefix'] = request.remarks_bprefix
        if not UtilClient.is_unset(request.remarks_cprefix):
            query['RemarksCPrefix'] = request.remarks_cprefix
        if not UtilClient.is_unset(request.remarks_dprefix):
            query['RemarksDPrefix'] = request.remarks_dprefix
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri_prefix):
            query['SourceUriPrefix'] = request.source_uri_prefix
        if not UtilClient.is_unset(request.tag_names):
            query['TagNames'] = request.tag_names
        if not UtilClient.is_unset(request.tags_modify_time_range):
            query['TagsModifyTimeRange'] = request.tags_modify_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.FindImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_images_with_options_async(
        self,
        request: imm_20170906_models.FindImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_line_contents_match):
            query['AddressLineContentsMatch'] = request.address_line_contents_match
        if not UtilClient.is_unset(request.age_range):
            query['AgeRange'] = request.age_range
        if not UtilClient.is_unset(request.create_time_range):
            query['CreateTimeRange'] = request.create_time_range
        if not UtilClient.is_unset(request.emotion):
            query['Emotion'] = request.emotion
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.faces_modify_time_range):
            query['FacesModifyTimeRange'] = request.faces_modify_time_range
        if not UtilClient.is_unset(request.gender):
            query['Gender'] = request.gender
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.image_size_range):
            query['ImageSizeRange'] = request.image_size_range
        if not UtilClient.is_unset(request.image_time_range):
            query['ImageTimeRange'] = request.image_time_range
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.location_boundary):
            query['LocationBoundary'] = request.location_boundary
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.modify_time_range):
            query['ModifyTimeRange'] = request.modify_time_range
        if not UtilClient.is_unset(request.ocrcontents_match):
            query['OCRContentsMatch'] = request.ocrcontents_match
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_aprefix):
            query['RemarksAPrefix'] = request.remarks_aprefix
        if not UtilClient.is_unset(request.remarks_array_ain):
            query['RemarksArrayAIn'] = request.remarks_array_ain
        if not UtilClient.is_unset(request.remarks_array_bin):
            query['RemarksArrayBIn'] = request.remarks_array_bin
        if not UtilClient.is_unset(request.remarks_bprefix):
            query['RemarksBPrefix'] = request.remarks_bprefix
        if not UtilClient.is_unset(request.remarks_cprefix):
            query['RemarksCPrefix'] = request.remarks_cprefix
        if not UtilClient.is_unset(request.remarks_dprefix):
            query['RemarksDPrefix'] = request.remarks_dprefix
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri_prefix):
            query['SourceUriPrefix'] = request.source_uri_prefix
        if not UtilClient.is_unset(request.tag_names):
            query['TagNames'] = request.tag_names
        if not UtilClient.is_unset(request.tags_modify_time_range):
            query['TagsModifyTimeRange'] = request.tags_modify_time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.FindImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_images(
        self,
        request: imm_20170906_models.FindImagesRequest,
    ) -> imm_20170906_models.FindImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_images_with_options(request, runtime)

    async def find_images_async(
        self,
        request: imm_20170906_models.FindImagesRequest,
    ) -> imm_20170906_models.FindImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_images_with_options_async(request, runtime)

    def find_similar_faces_with_options(
        self,
        request: imm_20170906_models.FindSimilarFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindSimilarFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.min_similarity):
            query['MinSimilarity'] = request.min_similarity
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.response_format):
            query['ResponseFormat'] = request.response_format
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindSimilarFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.FindSimilarFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def find_similar_faces_with_options_async(
        self,
        request: imm_20170906_models.FindSimilarFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindSimilarFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_id):
            query['FaceId'] = request.face_id
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.min_similarity):
            query['MinSimilarity'] = request.min_similarity
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.response_format):
            query['ResponseFormat'] = request.response_format
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FindSimilarFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.FindSimilarFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def find_similar_faces(
        self,
        request: imm_20170906_models.FindSimilarFacesRequest,
    ) -> imm_20170906_models.FindSimilarFacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.find_similar_faces_with_options(request, runtime)

    async def find_similar_faces_async(
        self,
        request: imm_20170906_models.FindSimilarFacesRequest,
    ) -> imm_20170906_models.FindSimilarFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.find_similar_faces_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        request: imm_20170906_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: imm_20170906_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: imm_20170906_models.GetImageRequest,
    ) -> imm_20170906_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: imm_20170906_models.GetImageRequest,
    ) -> imm_20170906_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_image_cropping_suggestions_with_options(
        self,
        request: imm_20170906_models.GetImageCroppingSuggestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageCroppingSuggestionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageCroppingSuggestions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageCroppingSuggestionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_cropping_suggestions_with_options_async(
        self,
        request: imm_20170906_models.GetImageCroppingSuggestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageCroppingSuggestionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageCroppingSuggestions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageCroppingSuggestionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_cropping_suggestions(
        self,
        request: imm_20170906_models.GetImageCroppingSuggestionsRequest,
    ) -> imm_20170906_models.GetImageCroppingSuggestionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_cropping_suggestions_with_options(request, runtime)

    async def get_image_cropping_suggestions_async(
        self,
        request: imm_20170906_models.GetImageCroppingSuggestionsRequest,
    ) -> imm_20170906_models.GetImageCroppingSuggestionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_cropping_suggestions_with_options_async(request, runtime)

    def get_image_quality_with_options(
        self,
        request: imm_20170906_models.GetImageQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageQualityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageQuality',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageQualityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_quality_with_options_async(
        self,
        request: imm_20170906_models.GetImageQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageQualityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageQuality',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetImageQualityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_quality(
        self,
        request: imm_20170906_models.GetImageQualityRequest,
    ) -> imm_20170906_models.GetImageQualityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_quality_with_options(request, runtime)

    async def get_image_quality_async(
        self,
        request: imm_20170906_models.GetImageQualityRequest,
    ) -> imm_20170906_models.GetImageQualityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_quality_with_options_async(request, runtime)

    def get_media_meta_with_options(
        self,
        request: imm_20170906_models.GetMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetMediaMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_uri):
            query['MediaUri'] = request.media_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaMeta',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_meta_with_options_async(
        self,
        request: imm_20170906_models.GetMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetMediaMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_uri):
            query['MediaUri'] = request.media_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaMeta',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetMediaMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_meta(
        self,
        request: imm_20170906_models.GetMediaMetaRequest,
    ) -> imm_20170906_models.GetMediaMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_meta_with_options(request, runtime)

    async def get_media_meta_async(
        self,
        request: imm_20170906_models.GetMediaMetaRequest,
    ) -> imm_20170906_models.GetMediaMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_meta_with_options_async(request, runtime)

    def get_office_conversion_task_with_options(
        self,
        request: imm_20170906_models.GetOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.GetOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_office_conversion_task(
        self,
        request: imm_20170906_models.GetOfficeConversionTaskRequest,
    ) -> imm_20170906_models.GetOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_conversion_task_with_options(request, runtime)

    async def get_office_conversion_task_async(
        self,
        request: imm_20170906_models.GetOfficeConversionTaskRequest,
    ) -> imm_20170906_models.GetOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_conversion_task_with_options_async(request, runtime)

    def get_office_preview_urlwith_options(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.watermark_fill_style):
            query['WatermarkFillStyle'] = request.watermark_fill_style
        if not UtilClient.is_unset(request.watermark_font):
            query['WatermarkFont'] = request.watermark_font
        if not UtilClient.is_unset(request.watermark_horizontal):
            query['WatermarkHorizontal'] = request.watermark_horizontal
        if not UtilClient.is_unset(request.watermark_rotate):
            query['WatermarkRotate'] = request.watermark_rotate
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        if not UtilClient.is_unset(request.watermark_value):
            query['WatermarkValue'] = request.watermark_value
        if not UtilClient.is_unset(request.watermark_vertical):
            query['WatermarkVertical'] = request.watermark_vertical
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficePreviewURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficePreviewURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_office_preview_urlwith_options_async(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.src_uri):
            query['SrcUri'] = request.src_uri
        if not UtilClient.is_unset(request.watermark_fill_style):
            query['WatermarkFillStyle'] = request.watermark_fill_style
        if not UtilClient.is_unset(request.watermark_font):
            query['WatermarkFont'] = request.watermark_font
        if not UtilClient.is_unset(request.watermark_horizontal):
            query['WatermarkHorizontal'] = request.watermark_horizontal
        if not UtilClient.is_unset(request.watermark_rotate):
            query['WatermarkRotate'] = request.watermark_rotate
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        if not UtilClient.is_unset(request.watermark_value):
            query['WatermarkValue'] = request.watermark_value
        if not UtilClient.is_unset(request.watermark_vertical):
            query['WatermarkVertical'] = request.watermark_vertical
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOfficePreviewURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficePreviewURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_office_preview_url(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_preview_urlwith_options(request, runtime)

    async def get_office_preview_url_async(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_preview_urlwith_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: imm_20170906_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: imm_20170906_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: imm_20170906_models.GetProjectRequest,
    ) -> imm_20170906_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: imm_20170906_models.GetProjectRequest,
    ) -> imm_20170906_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_set_with_options(
        self,
        request: imm_20170906_models.GetSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_set_with_options_async(
        self,
        request: imm_20170906_models.GetSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_set(
        self,
        request: imm_20170906_models.GetSetRequest,
    ) -> imm_20170906_models.GetSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_set_with_options(request, runtime)

    async def get_set_async(
        self,
        request: imm_20170906_models.GetSetRequest,
    ) -> imm_20170906_models.GetSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_set_with_options_async(request, runtime)

    def get_video_with_options(
        self,
        request: imm_20170906_models.GetVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_with_options_async(
        self,
        request: imm_20170906_models.GetVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video(
        self,
        request: imm_20170906_models.GetVideoRequest,
    ) -> imm_20170906_models.GetVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_with_options(request, runtime)

    async def get_video_async(
        self,
        request: imm_20170906_models.GetVideoRequest,
    ) -> imm_20170906_models.GetVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_with_options_async(request, runtime)

    def get_video_task_with_options(
        self,
        request: imm_20170906_models.GetVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_task_with_options_async(
        self,
        request: imm_20170906_models.GetVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetVideoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_task(
        self,
        request: imm_20170906_models.GetVideoTaskRequest,
    ) -> imm_20170906_models.GetVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_video_task_with_options(request, runtime)

    async def get_video_task_async(
        self,
        request: imm_20170906_models.GetVideoTaskRequest,
    ) -> imm_20170906_models.GetVideoTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_video_task_with_options_async(request, runtime)

    def get_weboffice_urlwith_options(
        self,
        request: imm_20170906_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetWebofficeURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file):
            query['File'] = request.file
        if not UtilClient.is_unset(request.file_id):
            query['FileID'] = request.file_id
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetWebofficeURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_weboffice_urlwith_options_async(
        self,
        request: imm_20170906_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetWebofficeURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file):
            query['File'] = request.file
        if not UtilClient.is_unset(request.file_id):
            query['FileID'] = request.file_id
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.src_type):
            query['SrcType'] = request.src_type
        if not UtilClient.is_unset(request.user):
            query['User'] = request.user
        if not UtilClient.is_unset(request.watermark):
            query['Watermark'] = request.watermark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetWebofficeURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_weboffice_url(
        self,
        request: imm_20170906_models.GetWebofficeURLRequest,
    ) -> imm_20170906_models.GetWebofficeURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_weboffice_urlwith_options(request, runtime)

    async def get_weboffice_url_async(
        self,
        request: imm_20170906_models.GetWebofficeURLRequest,
    ) -> imm_20170906_models.GetWebofficeURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_weboffice_urlwith_options_async(request, runtime)

    def index_image_with_options(
        self,
        request: imm_20170906_models.IndexImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_position):
            query['SourcePosition'] = request.source_position
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceUri'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_image_with_options_async(
        self,
        request: imm_20170906_models.IndexImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_position):
            query['SourcePosition'] = request.source_position
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceUri'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_image(
        self,
        request: imm_20170906_models.IndexImageRequest,
    ) -> imm_20170906_models.IndexImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.index_image_with_options(request, runtime)

    async def index_image_async(
        self,
        request: imm_20170906_models.IndexImageRequest,
    ) -> imm_20170906_models.IndexImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.index_image_with_options_async(request, runtime)

    def index_video_with_options(
        self,
        request: imm_20170906_models.IndexVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_video_with_options_async(
        self,
        request: imm_20170906_models.IndexVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexVideoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.tgt_uri):
            query['TgtUri'] = request.tgt_uri
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.IndexVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_video(
        self,
        request: imm_20170906_models.IndexVideoRequest,
    ) -> imm_20170906_models.IndexVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.index_video_with_options(request, runtime)

    async def index_video_async(
        self,
        request: imm_20170906_models.IndexVideoRequest,
    ) -> imm_20170906_models.IndexVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.index_video_with_options_async(request, runtime)

    def list_face_groups_with_options(
        self,
        request: imm_20170906_models.ListFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListFaceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_aquery):
            query['RemarksAQuery'] = request.remarks_aquery
        if not UtilClient.is_unset(request.remarks_array_aquery):
            query['RemarksArrayAQuery'] = request.remarks_array_aquery
        if not UtilClient.is_unset(request.remarks_array_bquery):
            query['RemarksArrayBQuery'] = request.remarks_array_bquery
        if not UtilClient.is_unset(request.remarks_bquery):
            query['RemarksBQuery'] = request.remarks_bquery
        if not UtilClient.is_unset(request.remarks_cquery):
            query['RemarksCQuery'] = request.remarks_cquery
        if not UtilClient.is_unset(request.remarks_dquery):
            query['RemarksDQuery'] = request.remarks_dquery
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFaceGroups',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListFaceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_face_groups_with_options_async(
        self,
        request: imm_20170906_models.ListFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListFaceGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_aquery):
            query['RemarksAQuery'] = request.remarks_aquery
        if not UtilClient.is_unset(request.remarks_array_aquery):
            query['RemarksArrayAQuery'] = request.remarks_array_aquery
        if not UtilClient.is_unset(request.remarks_array_bquery):
            query['RemarksArrayBQuery'] = request.remarks_array_bquery
        if not UtilClient.is_unset(request.remarks_bquery):
            query['RemarksBQuery'] = request.remarks_bquery
        if not UtilClient.is_unset(request.remarks_cquery):
            query['RemarksCQuery'] = request.remarks_cquery
        if not UtilClient.is_unset(request.remarks_dquery):
            query['RemarksDQuery'] = request.remarks_dquery
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFaceGroups',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListFaceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_face_groups(
        self,
        request: imm_20170906_models.ListFaceGroupsRequest,
    ) -> imm_20170906_models.ListFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_groups_with_options(request, runtime)

    async def list_face_groups_async(
        self,
        request: imm_20170906_models.ListFaceGroupsRequest,
    ) -> imm_20170906_models.ListFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_groups_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: imm_20170906_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: imm_20170906_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: imm_20170906_models.ListImagesRequest,
    ) -> imm_20170906_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: imm_20170906_models.ListImagesRequest,
    ) -> imm_20170906_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_office_conversion_task_with_options(
        self,
        request: imm_20170906_models.ListOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.ListOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_office_conversion_task(
        self,
        request: imm_20170906_models.ListOfficeConversionTaskRequest,
    ) -> imm_20170906_models.ListOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_conversion_task_with_options(request, runtime)

    async def list_office_conversion_task_async(
        self,
        request: imm_20170906_models.ListOfficeConversionTaskRequest,
    ) -> imm_20170906_models.ListOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_conversion_task_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: imm_20170906_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: imm_20170906_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: imm_20170906_models.ListProjectsRequest,
    ) -> imm_20170906_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: imm_20170906_models.ListProjectsRequest,
    ) -> imm_20170906_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_set_tags_with_options(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSetTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_set_tags_with_options_async(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSetTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_set_tags(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
    ) -> imm_20170906_models.ListSetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_set_tags_with_options(request, runtime)

    async def list_set_tags_async(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
    ) -> imm_20170906_models.ListSetTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_set_tags_with_options_async(request, runtime)

    def list_sets_with_options(
        self,
        request: imm_20170906_models.ListSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSets',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sets_with_options_async(
        self,
        request: imm_20170906_models.ListSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSets',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sets(
        self,
        request: imm_20170906_models.ListSetsRequest,
    ) -> imm_20170906_models.ListSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sets_with_options(request, runtime)

    async def list_sets_async(
        self,
        request: imm_20170906_models.ListSetsRequest,
    ) -> imm_20170906_models.ListSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sets_with_options_async(request, runtime)

    def list_video_audios_with_options(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoAudios',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoAudiosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_video_audios_with_options_async(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoAudios',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoAudiosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_video_audios(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_video_audios_with_options(request, runtime)

    async def list_video_audios_async(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_video_audios_with_options_async(request, runtime)

    def list_video_frames_with_options(
        self,
        request: imm_20170906_models.ListVideoFramesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoFramesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoFrames',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoFramesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_video_frames_with_options_async(
        self,
        request: imm_20170906_models.ListVideoFramesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoFramesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.video_uri):
            query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoFrames',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoFramesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_video_frames(
        self,
        request: imm_20170906_models.ListVideoFramesRequest,
    ) -> imm_20170906_models.ListVideoFramesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_video_frames_with_options(request, runtime)

    async def list_video_frames_async(
        self,
        request: imm_20170906_models.ListVideoFramesRequest,
    ) -> imm_20170906_models.ListVideoFramesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_video_frames_with_options_async(request, runtime)

    def list_video_tasks_with_options(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoTasks',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_video_tasks_with_options_async(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideoTasks',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideoTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_video_tasks(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_video_tasks_with_options(request, runtime)

    async def list_video_tasks_async(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_video_tasks_with_options_async(request, runtime)

    def list_videos_with_options(
        self,
        request: imm_20170906_models.ListVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_videos_with_options_async(
        self,
        request: imm_20170906_models.ListVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_time_start):
            query['CreateTimeStart'] = request.create_time_start
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListVideos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListVideosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_videos(
        self,
        request: imm_20170906_models.ListVideosRequest,
    ) -> imm_20170906_models.ListVideosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_videos_with_options(request, runtime)

    async def list_videos_async(
        self,
        request: imm_20170906_models.ListVideosRequest,
    ) -> imm_20170906_models.ListVideosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_videos_with_options_async(request, runtime)

    def open_imm_service_with_options(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenImmService',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.OpenImmServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_imm_service_with_options_async(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenImmService',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.OpenImmServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_imm_service(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_imm_service_with_options(request, runtime)

    async def open_imm_service_async(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_imm_service_with_options_async(request, runtime)

    def put_project_with_options(
        self,
        request: imm_20170906_models.PutProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.PutProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.PutProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_project_with_options_async(
        self,
        request: imm_20170906_models.PutProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.PutProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.PutProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_project(
        self,
        request: imm_20170906_models.PutProjectRequest,
    ) -> imm_20170906_models.PutProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_project_with_options(request, runtime)

    async def put_project_async(
        self,
        request: imm_20170906_models.PutProjectRequest,
    ) -> imm_20170906_models.PutProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_project_with_options_async(request, runtime)

    def refresh_office_preview_token_with_options(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshOfficePreviewToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficePreviewTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_office_preview_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshOfficePreviewToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficePreviewTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_office_preview_token(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_office_preview_token_with_options(request, runtime)

    async def refresh_office_preview_token_async(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_office_preview_token_with_options_async(request, runtime)

    def refresh_weboffice_token_with_options(
        self,
        request: imm_20170906_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshWebofficeTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_weboffice_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshWebofficeTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_weboffice_token(
        self,
        request: imm_20170906_models.RefreshWebofficeTokenRequest,
    ) -> imm_20170906_models.RefreshWebofficeTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    async def refresh_weboffice_token_async(
        self,
        request: imm_20170906_models.RefreshWebofficeTokenRequest,
    ) -> imm_20170906_models.RefreshWebofficeTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_weboffice_token_with_options_async(request, runtime)

    def update_face_group_with_options(
        self,
        request: imm_20170906_models.UpdateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateFaceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            query['GroupCoverFaceId'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.reset_items):
            query['ResetItems'] = request.reset_items
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceGroup',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateFaceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_face_group_with_options_async(
        self,
        request: imm_20170906_models.UpdateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateFaceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.group_cover_face_id):
            query['GroupCoverFaceId'] = request.group_cover_face_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.reset_items):
            query['ResetItems'] = request.reset_items
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceGroup',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateFaceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_face_group(
        self,
        request: imm_20170906_models.UpdateFaceGroupRequest,
    ) -> imm_20170906_models.UpdateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_face_group_with_options(request, runtime)

    async def update_face_group_async(
        self,
        request: imm_20170906_models.UpdateFaceGroupRequest,
    ) -> imm_20170906_models.UpdateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_face_group_with_options_async(request, runtime)

    def update_image_with_options(
        self,
        tmp_req: imm_20170906_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateImageResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20170906_models.UpdateImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.faces_shrink):
            query['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_position):
            query['SourcePosition'] = request.source_position
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceUri'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        tmp_req: imm_20170906_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateImageResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20170906_models.UpdateImageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.faces):
            request.faces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.faces, 'Faces', 'json')
        query = {}
        if not UtilClient.is_unset(request.external_id):
            query['ExternalId'] = request.external_id
        if not UtilClient.is_unset(request.faces_shrink):
            query['Faces'] = request.faces_shrink
        if not UtilClient.is_unset(request.image_uri):
            query['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.remarks_a):
            query['RemarksA'] = request.remarks_a
        if not UtilClient.is_unset(request.remarks_array_a):
            query['RemarksArrayA'] = request.remarks_array_a
        if not UtilClient.is_unset(request.remarks_array_b):
            query['RemarksArrayB'] = request.remarks_array_b
        if not UtilClient.is_unset(request.remarks_b):
            query['RemarksB'] = request.remarks_b
        if not UtilClient.is_unset(request.remarks_c):
            query['RemarksC'] = request.remarks_c
        if not UtilClient.is_unset(request.remarks_d):
            query['RemarksD'] = request.remarks_d
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.source_position):
            query['SourcePosition'] = request.source_position
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceUri'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        request: imm_20170906_models.UpdateImageRequest,
    ) -> imm_20170906_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    async def update_image_async(
        self,
        request: imm_20170906_models.UpdateImageRequest,
    ) -> imm_20170906_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_image_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: imm_20170906_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_cu):
            query['NewCU'] = request.new_cu
        if not UtilClient.is_unset(request.new_service_role):
            query['NewServiceRole'] = request.new_service_role
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: imm_20170906_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_cu):
            query['NewCU'] = request.new_cu
        if not UtilClient.is_unset(request.new_service_role):
            query['NewServiceRole'] = request.new_service_role
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: imm_20170906_models.UpdateProjectRequest,
    ) -> imm_20170906_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: imm_20170906_models.UpdateProjectRequest,
    ) -> imm_20170906_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_set_with_options(
        self,
        request: imm_20170906_models.UpdateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.set_name):
            query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_set_with_options_async(
        self,
        request: imm_20170906_models.UpdateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateSetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.set_id):
            query['SetId'] = request.set_id
        if not UtilClient.is_unset(request.set_name):
            query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_set(
        self,
        request: imm_20170906_models.UpdateSetRequest,
    ) -> imm_20170906_models.UpdateSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_set_with_options(request, runtime)

    async def update_set_async(
        self,
        request: imm_20170906_models.UpdateSetRequest,
    ) -> imm_20170906_models.UpdateSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_set_with_options_async(request, runtime)
