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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUriA'] = request.image_uri_a
        query['ImageUriB'] = request.image_uri_b
        query['FaceIdA'] = request.face_id_a
        query['FaceIdB'] = request.face_id_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUriA'] = request.image_uri_a
        query['ImageUriB'] = request.image_uri_b
        query['FaceIdA'] = request.face_id_a
        query['FaceIdB'] = request.face_id_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['TgtType'] = request.tgt_type
        query['TgtUri'] = request.tgt_uri
        query['SrcType'] = request.src_type
        query['StartPage'] = request.start_page
        query['EndPage'] = request.end_page
        query['MaxSheetRow'] = request.max_sheet_row
        query['MaxSheetCol'] = request.max_sheet_col
        query['MaxSheetCount'] = request.max_sheet_count
        query['SheetOnePage'] = request.sheet_one_page
        query['ModelId'] = request.model_id
        query['Password'] = request.password
        query['TgtFilePrefix'] = request.tgt_file_prefix
        query['TgtFileSuffix'] = request.tgt_file_suffix
        query['TgtFilePages'] = request.tgt_file_pages
        query['FitToPagesTall'] = request.fit_to_pages_tall
        query['FitToPagesWide'] = request.fit_to_pages_wide
        query['PdfVector'] = request.pdf_vector
        query['Hidecomments'] = request.hidecomments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConvertOfficeFormat',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['TgtType'] = request.tgt_type
        query['TgtUri'] = request.tgt_uri
        query['SrcType'] = request.src_type
        query['StartPage'] = request.start_page
        query['EndPage'] = request.end_page
        query['MaxSheetRow'] = request.max_sheet_row
        query['MaxSheetCol'] = request.max_sheet_col
        query['MaxSheetCount'] = request.max_sheet_count
        query['SheetOnePage'] = request.sheet_one_page
        query['ModelId'] = request.model_id
        query['Password'] = request.password
        query['TgtFilePrefix'] = request.tgt_file_prefix
        query['TgtFileSuffix'] = request.tgt_file_suffix
        query['TgtFilePages'] = request.tgt_file_pages
        query['FitToPagesTall'] = request.fit_to_pages_tall
        query['FitToPagesWide'] = request.fit_to_pages_wide
        query['PdfVector'] = request.pdf_vector
        query['Hidecomments'] = request.hidecomments
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ConvertOfficeFormat',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        query['CustomMessage'] = request.custom_message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGrabFrameTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        query['CustomMessage'] = request.custom_message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGrabFrameTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroupFacesJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGroupFacesJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_image_process_task_with_options(
        self,
        request: imm_20170906_models.CreateImageProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateImageProcessTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageProcessTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateImageProcessTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_process_task_with_options_async(
        self,
        request: imm_20170906_models.CreateImageProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateImageProcessTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageProcessTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateImageProcessTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_process_task(
        self,
        request: imm_20170906_models.CreateImageProcessTaskRequest,
    ) -> imm_20170906_models.CreateImageProcessTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_process_task_with_options(request, runtime)

    async def create_image_process_task_async(
        self,
        request: imm_20170906_models.CreateImageProcessTaskRequest,
    ) -> imm_20170906_models.CreateImageProcessTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_process_task_with_options_async(request, runtime)

    def create_media_complex_task_with_options(
        self,
        request: imm_20170906_models.CreateMediaComplexTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMediaComplexTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Parameters'] = request.parameters
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMediaComplexTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMediaComplexTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_media_complex_task_with_options_async(
        self,
        request: imm_20170906_models.CreateMediaComplexTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMediaComplexTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Parameters'] = request.parameters
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMediaComplexTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateMediaComplexTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_media_complex_task(
        self,
        request: imm_20170906_models.CreateMediaComplexTaskRequest,
    ) -> imm_20170906_models.CreateMediaComplexTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_media_complex_task_with_options(request, runtime)

    async def create_media_complex_task_async(
        self,
        request: imm_20170906_models.CreateMediaComplexTaskRequest,
    ) -> imm_20170906_models.CreateMediaComplexTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_media_complex_task_with_options_async(request, runtime)

    def create_merge_face_groups_job_with_options(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['GroupIdFrom'] = request.group_id_from
        query['GroupIdTo'] = request.group_id_to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMergeFaceGroupsJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['GroupIdFrom'] = request.group_id_from
        query['GroupIdTo'] = request.group_id_to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMergeFaceGroupsJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['TgtType'] = request.tgt_type
        query['TgtUri'] = request.tgt_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['SrcType'] = request.src_type
        query['StartPage'] = request.start_page
        query['EndPage'] = request.end_page
        query['MaxSheetRow'] = request.max_sheet_row
        query['MaxSheetCol'] = request.max_sheet_col
        query['MaxSheetCount'] = request.max_sheet_count
        query['SheetOnePage'] = request.sheet_one_page
        query['ModelId'] = request.model_id
        query['Password'] = request.password
        query['TgtFilePrefix'] = request.tgt_file_prefix
        query['TgtFileSuffix'] = request.tgt_file_suffix
        query['TgtFilePages'] = request.tgt_file_pages
        query['FitToPagesTall'] = request.fit_to_pages_tall
        query['FitToPagesWide'] = request.fit_to_pages_wide
        query['IdempotentToken'] = request.idempotent_token
        query['PdfVector'] = request.pdf_vector
        query['Hidecomments'] = request.hidecomments
        query['DisplayDpi'] = request.display_dpi
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['TgtType'] = request.tgt_type
        query['TgtUri'] = request.tgt_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['SrcType'] = request.src_type
        query['StartPage'] = request.start_page
        query['EndPage'] = request.end_page
        query['MaxSheetRow'] = request.max_sheet_row
        query['MaxSheetCol'] = request.max_sheet_col
        query['MaxSheetCount'] = request.max_sheet_count
        query['SheetOnePage'] = request.sheet_one_page
        query['ModelId'] = request.model_id
        query['Password'] = request.password
        query['TgtFilePrefix'] = request.tgt_file_prefix
        query['TgtFileSuffix'] = request.tgt_file_suffix
        query['TgtFilePages'] = request.tgt_file_pages
        query['FitToPagesTall'] = request.fit_to_pages_tall
        query['FitToPagesWide'] = request.fit_to_pages_wide
        query['IdempotentToken'] = request.idempotent_token
        query['PdfVector'] = request.pdf_vector
        query['Hidecomments'] = request.hidecomments
        query['DisplayDpi'] = request.display_dpi
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_video_abstract_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetVideoUri'] = request.target_video_uri
        query['TargetClipsUri'] = request.target_clips_uri
        query['AbstractLength'] = request.abstract_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoAbstractTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAbstractTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_abstract_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetVideoUri'] = request.target_video_uri
        query['TargetClipsUri'] = request.target_clips_uri
        query['AbstractLength'] = request.abstract_length
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoAbstractTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAbstractTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_abstract_task(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_abstract_task_with_options(request, runtime)

    async def create_video_abstract_task_async(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_abstract_task_with_options_async(request, runtime)

    def create_video_analyse_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoAnalyseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAnalyseTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['TgtUri'] = request.tgt_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoAnalyseTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAnalyseTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_analyse_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoAnalyseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAnalyseTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['TgtUri'] = request.tgt_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoAnalyseTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoAnalyseTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_analyse_task(
        self,
        request: imm_20170906_models.CreateVideoAnalyseTaskRequest,
    ) -> imm_20170906_models.CreateVideoAnalyseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_analyse_task_with_options(request, runtime)

    async def create_video_analyse_task_async(
        self,
        request: imm_20170906_models.CreateVideoAnalyseTaskRequest,
    ) -> imm_20170906_models.CreateVideoAnalyseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_analyse_task_with_options_async(request, runtime)

    def create_video_compress_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        query['CustomMessage'] = request.custom_message
        query['TargetContainer'] = request.target_container
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoCompressTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['VideoUri'] = request.video_uri
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetList'] = request.target_list
        query['CustomMessage'] = request.custom_message
        query['TargetContainer'] = request.target_container
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoCompressTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_video_produce_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoProduceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoProduceTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Images'] = request.images
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetUri'] = request.target_uri
        query['CustomMessage'] = request.custom_message
        query['Music'] = request.music
        query['Width'] = request.width
        query['Height'] = request.height
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoProduceTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoProduceTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_produce_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoProduceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoProduceTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Images'] = request.images
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['TargetUri'] = request.target_uri
        query['CustomMessage'] = request.custom_message
        query['Music'] = request.music
        query['Width'] = request.width
        query['Height'] = request.height
        query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateVideoProduceTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.CreateVideoProduceTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_produce_task(
        self,
        request: imm_20170906_models.CreateVideoProduceTaskRequest,
    ) -> imm_20170906_models.CreateVideoProduceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_video_produce_task_with_options(request, runtime)

    async def create_video_produce_task_async(
        self,
        request: imm_20170906_models.CreateVideoProduceTaskRequest,
    ) -> imm_20170906_models.CreateVideoProduceTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_produce_task_with_options_async(request, runtime)

    def decode_blind_watermark_with_options(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['OriginalImageUri'] = request.original_image_uri
        query['TargetUri'] = request.target_uri
        query['ImageQuality'] = request.image_quality
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['OriginalImageUri'] = request.original_image_uri
        query['TargetUri'] = request.target_uri
        query['ImageQuality'] = request.image_quality
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_image_job_with_options(
        self,
        request: imm_20170906_models.DeleteImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['JobType'] = request.job_type
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImageJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_job_with_options_async(
        self,
        request: imm_20170906_models.DeleteImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['JobType'] = request.job_type
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImageJob',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DeleteImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_job(
        self,
        request: imm_20170906_models.DeleteImageJobRequest,
    ) -> imm_20170906_models.DeleteImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_job_with_options(request, runtime)

    async def delete_image_job_async(
        self,
        request: imm_20170906_models.DeleteImageJobRequest,
    ) -> imm_20170906_models.DeleteImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_job_with_options_async(request, runtime)

    def delete_office_conversion_task_with_options(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskType'] = request.task_type
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskType'] = request.task_type
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def describe_regions_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> imm_20170906_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    async def describe_regions_async(self) -> imm_20170906_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(runtime)

    def detect_image_bodies_with_options(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def detect_image_logos_with_options(
        self,
        request: imm_20170906_models.DetectImageLogosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageLogosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageLogos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageLogosResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_logos_with_options_async(
        self,
        request: imm_20170906_models.DetectImageLogosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageLogosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageLogos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.DetectImageLogosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_logos(
        self,
        request: imm_20170906_models.DetectImageLogosRequest,
    ) -> imm_20170906_models.DetectImageLogosResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_logos_with_options(request, runtime)

    async def detect_image_logos_async(
        self,
        request: imm_20170906_models.DetectImageLogosRequest,
    ) -> imm_20170906_models.DetectImageLogosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_logos_with_options_async(request, runtime)

    def detect_image_qrcodes_with_options(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUris'] = request.src_uris
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUris'] = request.src_uris
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectQRCodes',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['WatermarkUri'] = request.watermark_uri
        query['TargetUri'] = request.target_uri
        query['ImageQuality'] = request.image_quality
        query['Content'] = request.content
        query['TargetImageType'] = request.target_image_type
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['WatermarkUri'] = request.watermark_uri
        query['TargetUri'] = request.target_uri
        query['ImageQuality'] = request.image_quality
        query['Content'] = request.content
        query['TargetImageType'] = request.target_image_type
        query['Model'] = request.model
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageSizeRange'] = request.image_size_range
        query['ImageTimeRange'] = request.image_time_range
        query['CreateTimeRange'] = request.create_time_range
        query['ModifyTimeRange'] = request.modify_time_range
        query['SourceType'] = request.source_type
        query['SourceUriPrefix'] = request.source_uri_prefix
        query['RemarksAPrefix'] = request.remarks_aprefix
        query['RemarksBPrefix'] = request.remarks_bprefix
        query['TagNames'] = request.tag_names
        query['OCRContentsMatch'] = request.ocrcontents_match
        query['AgeRange'] = request.age_range
        query['Gender'] = request.gender
        query['Emotion'] = request.emotion
        query['OrderBy'] = request.order_by
        query['Order'] = request.order
        query['Marker'] = request.marker
        query['LocationBoundary'] = request.location_boundary
        query['RemarksCPrefix'] = request.remarks_cprefix
        query['RemarksDPrefix'] = request.remarks_dprefix
        query['ExternalId'] = request.external_id
        query['GroupId'] = request.group_id
        query['Limit'] = request.limit
        query['FacesModifyTimeRange'] = request.faces_modify_time_range
        query['TagsModifyTimeRange'] = request.tags_modify_time_range
        query['AddressLineContentsMatch'] = request.address_line_contents_match
        query['RemarksArrayAIn'] = request.remarks_array_ain
        query['RemarksArrayBIn'] = request.remarks_array_bin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FindImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageSizeRange'] = request.image_size_range
        query['ImageTimeRange'] = request.image_time_range
        query['CreateTimeRange'] = request.create_time_range
        query['ModifyTimeRange'] = request.modify_time_range
        query['SourceType'] = request.source_type
        query['SourceUriPrefix'] = request.source_uri_prefix
        query['RemarksAPrefix'] = request.remarks_aprefix
        query['RemarksBPrefix'] = request.remarks_bprefix
        query['TagNames'] = request.tag_names
        query['OCRContentsMatch'] = request.ocrcontents_match
        query['AgeRange'] = request.age_range
        query['Gender'] = request.gender
        query['Emotion'] = request.emotion
        query['OrderBy'] = request.order_by
        query['Order'] = request.order
        query['Marker'] = request.marker
        query['LocationBoundary'] = request.location_boundary
        query['RemarksCPrefix'] = request.remarks_cprefix
        query['RemarksDPrefix'] = request.remarks_dprefix
        query['ExternalId'] = request.external_id
        query['GroupId'] = request.group_id
        query['Limit'] = request.limit
        query['FacesModifyTimeRange'] = request.faces_modify_time_range
        query['TagsModifyTimeRange'] = request.tags_modify_time_range
        query['AddressLineContentsMatch'] = request.address_line_contents_match
        query['RemarksArrayAIn'] = request.remarks_array_ain
        query['RemarksArrayBIn'] = request.remarks_array_bin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FindImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['FaceId'] = request.face_id
        query['Limit'] = request.limit
        query['MinSimilarity'] = request.min_similarity
        query['ResponseFormat'] = request.response_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FindSimilarFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['FaceId'] = request.face_id
        query['Limit'] = request.limit
        query['MinSimilarity'] = request.min_similarity
        query['ResponseFormat'] = request.response_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FindSimilarFaces',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_content_key_with_options(
        self,
        request: imm_20170906_models.GetContentKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetContentKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VersionId'] = request.version_id
        query['DRMServerId'] = request.drmserver_id
        query['KeyIds'] = request.key_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetContentKey',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetContentKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_content_key_with_options_async(
        self,
        request: imm_20170906_models.GetContentKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetContentKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['VersionId'] = request.version_id
        query['DRMServerId'] = request.drmserver_id
        query['KeyIds'] = request.key_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetContentKey',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetContentKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_content_key(
        self,
        request: imm_20170906_models.GetContentKeyRequest,
    ) -> imm_20170906_models.GetContentKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_content_key_with_options(request, runtime)

    async def get_content_key_async(
        self,
        request: imm_20170906_models.GetContentKeyRequest,
    ) -> imm_20170906_models.GetContentKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_content_key_with_options_async(request, runtime)

    def get_drmlicense_with_options(
        self,
        request: imm_20170906_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetDRMLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['DRMType'] = request.drmtype
        query['DRMLicense'] = request.drmlicense
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetDRMLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_drmlicense_with_options_async(
        self,
        request: imm_20170906_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetDRMLicenseResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['DRMType'] = request.drmtype
        query['DRMLicense'] = request.drmlicense
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetDRMLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_drmlicense(
        self,
        request: imm_20170906_models.GetDRMLicenseRequest,
    ) -> imm_20170906_models.GetDRMLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_drmlicense_with_options(request, runtime)

    async def get_drmlicense_async(
        self,
        request: imm_20170906_models.GetDRMLicenseRequest,
    ) -> imm_20170906_models.GetDRMLicenseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_drmlicense_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        request: imm_20170906_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['AspectRatios'] = request.aspect_ratios
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImageCroppingSuggestions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        query['AspectRatios'] = request.aspect_ratios
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImageCroppingSuggestions',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImageQuality',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ImageUri'] = request.image_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImageQuality',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['MediaUri'] = request.media_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMediaMeta',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['MediaUri'] = request.media_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMediaMeta',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_office_edit_urlwith_options(
        self,
        request: imm_20170906_models.GetOfficeEditURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeEditURLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['SrcType'] = request.src_type
        query['FileID'] = request.file_id
        query['TgtUri'] = request.tgt_uri
        query['UserID'] = request.user_id
        query['UserName'] = request.user_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeEditURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeEditURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_office_edit_urlwith_options_async(
        self,
        request: imm_20170906_models.GetOfficeEditURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeEditURLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['SrcType'] = request.src_type
        query['FileID'] = request.file_id
        query['TgtUri'] = request.tgt_uri
        query['UserID'] = request.user_id
        query['UserName'] = request.user_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['FileName'] = request.file_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeEditURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.GetOfficeEditURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_office_edit_url(
        self,
        request: imm_20170906_models.GetOfficeEditURLRequest,
    ) -> imm_20170906_models.GetOfficeEditURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_edit_urlwith_options(request, runtime)

    async def get_office_edit_url_async(
        self,
        request: imm_20170906_models.GetOfficeEditURLRequest,
    ) -> imm_20170906_models.GetOfficeEditURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_edit_urlwith_options_async(request, runtime)

    def get_office_preview_urlwith_options(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['SrcType'] = request.src_type
        query['WatermarkType'] = request.watermark_type
        query['WatermarkValue'] = request.watermark_value
        query['WatermarkFillStyle'] = request.watermark_fill_style
        query['WatermarkFont'] = request.watermark_font
        query['WatermarkRotate'] = request.watermark_rotate
        query['WatermarkHorizontal'] = request.watermark_horizontal
        query['WatermarkVertical'] = request.watermark_vertical
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficePreviewURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcUri'] = request.src_uri
        query['SrcType'] = request.src_type
        query['WatermarkType'] = request.watermark_type
        query['WatermarkValue'] = request.watermark_value
        query['WatermarkFillStyle'] = request.watermark_fill_style
        query['WatermarkFont'] = request.watermark_font
        query['WatermarkRotate'] = request.watermark_rotate
        query['WatermarkHorizontal'] = request.watermark_horizontal
        query['WatermarkVertical'] = request.watermark_vertical
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficePreviewURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskType'] = request.task_type
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['TaskType'] = request.task_type
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetVideoTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcType'] = request.src_type
        query['FileID'] = request.file_id
        query['User'] = request.user
        query['Permission'] = request.permission
        query['File'] = request.file
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['Watermark'] = request.watermark
        query['Hidecmb'] = request.hidecmb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SrcType'] = request.src_type
        query['FileID'] = request.file_id
        query['User'] = request.user
        query['Permission'] = request.permission
        query['File'] = request.file
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['Watermark'] = request.watermark
        query['Hidecmb'] = request.hidecmb
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['SourcePosition'] = request.source_position
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['SourcePosition'] = request.source_position
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['TgtUri'] = request.tgt_uri
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['TgtUri'] = request.tgt_uri
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['NotifyTopicName'] = request.notify_topic_name
        query['NotifyEndpoint'] = request.notify_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexVideo',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['Marker'] = request.marker
        query['Limit'] = request.limit
        query['Order'] = request.order
        query['OrderBy'] = request.order_by
        query['RemarksAQuery'] = request.remarks_aquery
        query['RemarksBQuery'] = request.remarks_bquery
        query['RemarksCQuery'] = request.remarks_cquery
        query['RemarksDQuery'] = request.remarks_dquery
        query['RemarksArrayAQuery'] = request.remarks_array_aquery
        query['RemarksArrayBQuery'] = request.remarks_array_bquery
        query['ExternalId'] = request.external_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFaceGroups',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['Marker'] = request.marker
        query['Limit'] = request.limit
        query['Order'] = request.order
        query['OrderBy'] = request.order_by
        query['RemarksAQuery'] = request.remarks_aquery
        query['RemarksBQuery'] = request.remarks_bquery
        query['RemarksCQuery'] = request.remarks_cquery
        query['RemarksDQuery'] = request.remarks_dquery
        query['RemarksArrayAQuery'] = request.remarks_array_aquery
        query['RemarksArrayBQuery'] = request.remarks_array_bquery
        query['ExternalId'] = request.external_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFaceGroups',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['CreateTimeStart'] = request.create_time_start
        query['Marker'] = request.marker
        query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['CreateTimeStart'] = request.create_time_start
        query['Marker'] = request.marker
        query['Limit'] = request.limit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_project_apis_with_options(
        self,
        request: imm_20170906_models.ListProjectAPIsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectAPIsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjectAPIs',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectAPIsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_apis_with_options_async(
        self,
        request: imm_20170906_models.ListProjectAPIsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectAPIsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjectAPIs',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.ListProjectAPIsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project_apis(
        self,
        request: imm_20170906_models.ListProjectAPIsRequest,
    ) -> imm_20170906_models.ListProjectAPIsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_apis_with_options(request, runtime)

    async def list_project_apis_async(
        self,
        request: imm_20170906_models.ListProjectAPIsRequest,
    ) -> imm_20170906_models.ListProjectAPIsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_apis_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: imm_20170906_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_sets_with_options(
        self,
        request: imm_20170906_models.ListSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSets',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSets',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_set_tags_with_options(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSetTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSetTags',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_video_audios_with_options(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoAudios',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoAudios',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoFrames',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['VideoUri'] = request.video_uri
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoFrames',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_videos_with_options(
        self,
        request: imm_20170906_models.ListVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['CreateTimeStart'] = request.create_time_start
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['CreateTimeStart'] = request.create_time_start
        query['Marker'] = request.marker
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideos',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_video_tasks_with_options(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoTasks',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['Marker'] = request.marker
        query['MaxKeys'] = request.max_keys
        query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVideoTasks',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def open_imm_service_with_options(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenImmService',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='OpenImmService',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ServiceRole'] = request.service_role
        query['CU'] = request.cu
        query['Type'] = request.type
        query['BillingType'] = request.billing_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['ServiceRole'] = request.service_role
        query['CU'] = request.cu
        query['Type'] = request.type
        query['BillingType'] = request.billing_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def refresh_office_edit_token_with_options(
        self,
        request: imm_20170906_models.RefreshOfficeEditTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficeEditTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshOfficeEditToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficeEditTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_office_edit_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshOfficeEditTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficeEditTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshOfficeEditToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.RefreshOfficeEditTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_office_edit_token(
        self,
        request: imm_20170906_models.RefreshOfficeEditTokenRequest,
    ) -> imm_20170906_models.RefreshOfficeEditTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_office_edit_token_with_options(request, runtime)

    async def refresh_office_edit_token_async(
        self,
        request: imm_20170906_models.RefreshOfficeEditTokenRequest,
    ) -> imm_20170906_models.RefreshOfficeEditTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_office_edit_token_with_options_async(request, runtime)

    def refresh_office_preview_token_with_options(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshOfficePreviewToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshOfficePreviewToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['AccessToken'] = request.access_token
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['GroupCoverFaceId'] = request.group_cover_face_id
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        query['ExternalId'] = request.external_id
        query['ResetItems'] = request.reset_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceGroup',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['GroupId'] = request.group_id
        query['GroupName'] = request.group_name
        query['GroupCoverFaceId'] = request.group_cover_face_id
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        query['ExternalId'] = request.external_id
        query['ResetItems'] = request.reset_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFaceGroup',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        request: imm_20170906_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['SourcePosition'] = request.source_position
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20170906_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: imm_20170906_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['ImageUri'] = request.image_uri
        query['RemarksA'] = request.remarks_a
        query['RemarksB'] = request.remarks_b
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['SourcePosition'] = request.source_position
        query['RemarksC'] = request.remarks_c
        query['RemarksD'] = request.remarks_d
        query['ExternalId'] = request.external_id
        query['RemarksArrayA'] = request.remarks_array_a
        query['RemarksArrayB'] = request.remarks_array_b
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['NewCU'] = request.new_cu
        query['NewServiceRole'] = request.new_service_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['NewCU'] = request.new_cu
        query['NewServiceRole'] = request.new_service_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['Project'] = request.project
        query['SetId'] = request.set_id
        query['SetName'] = request.set_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateSet',
            version='2017-09-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
