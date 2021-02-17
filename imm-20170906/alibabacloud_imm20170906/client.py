# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20170906 import models as imm_20170906_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CompareImageFacesResponse().from_map(
            self.do_rpcrequest('CompareImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def compare_image_faces_with_options_async(
        self,
        request: imm_20170906_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CompareImageFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CompareImageFacesResponse().from_map(
            await self.do_rpcrequest_async('CompareImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ConvertOfficeFormatResponse().from_map(
            self.do_rpcrequest('ConvertOfficeFormat', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_office_format_with_options_async(
        self,
        request: imm_20170906_models.ConvertOfficeFormatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ConvertOfficeFormatResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ConvertOfficeFormatResponse().from_map(
            await self.do_rpcrequest_async('ConvertOfficeFormat', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateGrabFrameTaskResponse().from_map(
            self.do_rpcrequest('CreateGrabFrameTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_grab_frame_task_with_options_async(
        self,
        request: imm_20170906_models.CreateGrabFrameTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGrabFrameTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateGrabFrameTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateGrabFrameTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateGroupFacesJobResponse().from_map(
            self.do_rpcrequest('CreateGroupFacesJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_faces_job_with_options_async(
        self,
        request: imm_20170906_models.CreateGroupFacesJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateGroupFacesJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateGroupFacesJobResponse().from_map(
            await self.do_rpcrequest_async('CreateGroupFacesJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateImageProcessTaskResponse().from_map(
            self.do_rpcrequest('CreateImageProcessTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_process_task_with_options_async(
        self,
        request: imm_20170906_models.CreateImageProcessTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateImageProcessTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateImageProcessTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateImageProcessTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateMediaComplexTaskResponse().from_map(
            self.do_rpcrequest('CreateMediaComplexTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_media_complex_task_with_options_async(
        self,
        request: imm_20170906_models.CreateMediaComplexTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMediaComplexTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateMediaComplexTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateMediaComplexTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateMergeFaceGroupsJobResponse().from_map(
            self.do_rpcrequest('CreateMergeFaceGroupsJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_merge_face_groups_job_with_options_async(
        self,
        request: imm_20170906_models.CreateMergeFaceGroupsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateMergeFaceGroupsJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateMergeFaceGroupsJobResponse().from_map(
            await self.do_rpcrequest_async('CreateMergeFaceGroupsJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateOfficeConversionTaskResponse().from_map(
            self.do_rpcrequest('CreateOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateOfficeConversionTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateSetResponse().from_map(
            self.do_rpcrequest('CreateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_set_with_options_async(
        self,
        request: imm_20170906_models.CreateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateSetResponse().from_map(
            await self.do_rpcrequest_async('CreateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_stream_analyse_task_with_options(
        self,
        request: imm_20170906_models.CreateStreamAnalyseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateStreamAnalyseTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateStreamAnalyseTaskResponse().from_map(
            self.do_rpcrequest('CreateStreamAnalyseTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_stream_analyse_task_with_options_async(
        self,
        request: imm_20170906_models.CreateStreamAnalyseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateStreamAnalyseTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateStreamAnalyseTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateStreamAnalyseTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stream_analyse_task(
        self,
        request: imm_20170906_models.CreateStreamAnalyseTaskRequest,
    ) -> imm_20170906_models.CreateStreamAnalyseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stream_analyse_task_with_options(request, runtime)

    async def create_stream_analyse_task_async(
        self,
        request: imm_20170906_models.CreateStreamAnalyseTaskRequest,
    ) -> imm_20170906_models.CreateStreamAnalyseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stream_analyse_task_with_options_async(request, runtime)

    def create_video_abstract_task_with_options(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoAbstractTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoAbstractTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_abstract_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoAbstractTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAbstractTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoAbstractTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoAbstractTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoAnalyseTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoAnalyseTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_analyse_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoAnalyseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoAnalyseTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoAnalyseTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoAnalyseTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoCompressTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoCompressTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_compress_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoCompressTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoCompressTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoCompressTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoCompressTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoProduceTaskResponse().from_map(
            self.do_rpcrequest('CreateVideoProduceTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_video_produce_task_with_options_async(
        self,
        request: imm_20170906_models.CreateVideoProduceTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.CreateVideoProduceTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.CreateVideoProduceTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateVideoProduceTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DecodeBlindWatermarkResponse().from_map(
            self.do_rpcrequest('DecodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def decode_blind_watermark_with_options_async(
        self,
        request: imm_20170906_models.DecodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DecodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DecodeBlindWatermarkResponse().from_map(
            await self.do_rpcrequest_async('DecodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteImageResponse().from_map(
            self.do_rpcrequest('DeleteImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: imm_20170906_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteImageResponse().from_map(
            await self.do_rpcrequest_async('DeleteImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteImageJobResponse().from_map(
            self.do_rpcrequest('DeleteImageJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_job_with_options_async(
        self,
        request: imm_20170906_models.DeleteImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteImageJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteImageJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteImageJob', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteOfficeConversionTaskResponse().from_map(
            self.do_rpcrequest('DeleteOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.DeleteOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteOfficeConversionTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteProjectResponse().from_map(
            self.do_rpcrequest('DeleteProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: imm_20170906_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteSetResponse().from_map(
            self.do_rpcrequest('DeleteSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_set_with_options_async(
        self,
        request: imm_20170906_models.DeleteSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteVideoResponse().from_map(
            self.do_rpcrequest('DeleteVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_video_with_options_async(
        self,
        request: imm_20170906_models.DeleteVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteVideoResponse().from_map(
            await self.do_rpcrequest_async('DeleteVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteVideoTaskResponse().from_map(
            self.do_rpcrequest('DeleteVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_video_task_with_options_async(
        self,
        request: imm_20170906_models.DeleteVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DeleteVideoTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DeleteVideoTaskResponse().from_map(
            await self.do_rpcrequest_async('DeleteVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return imm_20170906_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DescribeRegionsResponse:
        req = open_api_models.OpenApiRequest()
        return imm_20170906_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageBodiesResponse().from_map(
            self.do_rpcrequest('DetectImageBodies', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_bodies_with_options_async(
        self,
        request: imm_20170906_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageBodiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageBodiesResponse().from_map(
            await self.do_rpcrequest_async('DetectImageBodies', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageFacesResponse().from_map(
            self.do_rpcrequest('DetectImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_faces_with_options_async(
        self,
        request: imm_20170906_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageFacesResponse().from_map(
            await self.do_rpcrequest_async('DetectImageFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageLogosResponse().from_map(
            self.do_rpcrequest('DetectImageLogos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_logos_with_options_async(
        self,
        request: imm_20170906_models.DetectImageLogosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageLogosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageLogosResponse().from_map(
            await self.do_rpcrequest_async('DetectImageLogos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageQRCodesResponse().from_map(
            self.do_rpcrequest('DetectImageQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_qrcodes_with_options_async(
        self,
        request: imm_20170906_models.DetectImageQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageQRCodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageQRCodesResponse().from_map(
            await self.do_rpcrequest_async('DetectImageQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageTagsResponse().from_map(
            self.do_rpcrequest('DetectImageTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_tags_with_options_async(
        self,
        request: imm_20170906_models.DetectImageTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectImageTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectImageTagsResponse().from_map(
            await self.do_rpcrequest_async('DetectImageTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectQRCodesResponse().from_map(
            self.do_rpcrequest('DetectQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_qrcodes_with_options_async(
        self,
        request: imm_20170906_models.DetectQRCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.DetectQRCodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.DetectQRCodesResponse().from_map(
            await self.do_rpcrequest_async('DetectQRCodes', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.EncodeBlindWatermarkResponse().from_map(
            self.do_rpcrequest('EncodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def encode_blind_watermark_with_options_async(
        self,
        request: imm_20170906_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.EncodeBlindWatermarkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.EncodeBlindWatermarkResponse().from_map(
            await self.do_rpcrequest_async('EncodeBlindWatermark', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.FindImagesResponse().from_map(
            self.do_rpcrequest('FindImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_images_with_options_async(
        self,
        request: imm_20170906_models.FindImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.FindImagesResponse().from_map(
            await self.do_rpcrequest_async('FindImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.FindSimilarFacesResponse().from_map(
            self.do_rpcrequest('FindSimilarFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def find_similar_faces_with_options_async(
        self,
        request: imm_20170906_models.FindSimilarFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.FindSimilarFacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.FindSimilarFacesResponse().from_map(
            await self.do_rpcrequest_async('FindSimilarFaces', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetContentKeyResponse().from_map(
            self.do_rpcrequest('GetContentKey', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_content_key_with_options_async(
        self,
        request: imm_20170906_models.GetContentKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetContentKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetContentKeyResponse().from_map(
            await self.do_rpcrequest_async('GetContentKey', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetDRMLicenseResponse().from_map(
            self.do_rpcrequest('GetDRMLicense', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_drmlicense_with_options_async(
        self,
        request: imm_20170906_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetDRMLicenseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetDRMLicenseResponse().from_map(
            await self.do_rpcrequest_async('GetDRMLicense', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageResponse().from_map(
            self.do_rpcrequest('GetImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: imm_20170906_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageResponse().from_map(
            await self.do_rpcrequest_async('GetImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageCroppingSuggestionsResponse().from_map(
            self.do_rpcrequest('GetImageCroppingSuggestions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_cropping_suggestions_with_options_async(
        self,
        request: imm_20170906_models.GetImageCroppingSuggestionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageCroppingSuggestionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageCroppingSuggestionsResponse().from_map(
            await self.do_rpcrequest_async('GetImageCroppingSuggestions', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageQualityResponse().from_map(
            self.do_rpcrequest('GetImageQuality', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_quality_with_options_async(
        self,
        request: imm_20170906_models.GetImageQualityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetImageQualityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetImageQualityResponse().from_map(
            await self.do_rpcrequest_async('GetImageQuality', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetMediaMetaResponse().from_map(
            self.do_rpcrequest('GetMediaMeta', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_media_meta_with_options_async(
        self,
        request: imm_20170906_models.GetMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetMediaMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetMediaMetaResponse().from_map(
            await self.do_rpcrequest_async('GetMediaMeta', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficeConversionTaskResponse().from_map(
            self.do_rpcrequest('GetOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.GetOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficeConversionTaskResponse().from_map(
            await self.do_rpcrequest_async('GetOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficeEditURLResponse().from_map(
            self.do_rpcrequest('GetOfficeEditURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_office_edit_urlwith_options_async(
        self,
        request: imm_20170906_models.GetOfficeEditURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficeEditURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficeEditURLResponse().from_map(
            await self.do_rpcrequest_async('GetOfficeEditURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficePreviewURLResponse().from_map(
            self.do_rpcrequest('GetOfficePreviewURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_office_preview_urlwith_options_async(
        self,
        request: imm_20170906_models.GetOfficePreviewURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetOfficePreviewURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetOfficePreviewURLResponse().from_map(
            await self.do_rpcrequest_async('GetOfficePreviewURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetProjectResponse().from_map(
            self.do_rpcrequest('GetProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: imm_20170906_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetProjectResponse().from_map(
            await self.do_rpcrequest_async('GetProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetSetResponse().from_map(
            self.do_rpcrequest('GetSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_set_with_options_async(
        self,
        request: imm_20170906_models.GetSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetSetResponse().from_map(
            await self.do_rpcrequest_async('GetSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetVideoResponse().from_map(
            self.do_rpcrequest('GetVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_with_options_async(
        self,
        request: imm_20170906_models.GetVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetVideoResponse().from_map(
            await self.do_rpcrequest_async('GetVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetVideoTaskResponse().from_map(
            self.do_rpcrequest('GetVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_video_task_with_options_async(
        self,
        request: imm_20170906_models.GetVideoTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetVideoTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetVideoTaskResponse().from_map(
            await self.do_rpcrequest_async('GetVideoTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetWebofficeURLResponse().from_map(
            self.do_rpcrequest('GetWebofficeURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_weboffice_urlwith_options_async(
        self,
        request: imm_20170906_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.GetWebofficeURLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.GetWebofficeURLResponse().from_map(
            await self.do_rpcrequest_async('GetWebofficeURL', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.IndexImageResponse().from_map(
            self.do_rpcrequest('IndexImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def index_image_with_options_async(
        self,
        request: imm_20170906_models.IndexImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.IndexImageResponse().from_map(
            await self.do_rpcrequest_async('IndexImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.IndexVideoResponse().from_map(
            self.do_rpcrequest('IndexVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def index_video_with_options_async(
        self,
        request: imm_20170906_models.IndexVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.IndexVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.IndexVideoResponse().from_map(
            await self.do_rpcrequest_async('IndexVideo', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListFaceGroupsResponse().from_map(
            self.do_rpcrequest('ListFaceGroups', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_groups_with_options_async(
        self,
        request: imm_20170906_models.ListFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListFaceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListFaceGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListFaceGroups', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListImagesResponse().from_map(
            self.do_rpcrequest('ListImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: imm_20170906_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListImagesResponse().from_map(
            await self.do_rpcrequest_async('ListImages', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListOfficeConversionTaskResponse().from_map(
            self.do_rpcrequest('ListOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_office_conversion_task_with_options_async(
        self,
        request: imm_20170906_models.ListOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListOfficeConversionTaskResponse().from_map(
            await self.do_rpcrequest_async('ListOfficeConversionTask', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListProjectAPIsResponse().from_map(
            self.do_rpcrequest('ListProjectAPIs', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_apis_with_options_async(
        self,
        request: imm_20170906_models.ListProjectAPIsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectAPIsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListProjectAPIsResponse().from_map(
            await self.do_rpcrequest_async('ListProjectAPIs', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListProjectsResponse().from_map(
            self.do_rpcrequest('ListProjects', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: imm_20170906_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListProjectsResponse().from_map(
            await self.do_rpcrequest_async('ListProjects', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListSetsResponse().from_map(
            self.do_rpcrequest('ListSets', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_sets_with_options_async(
        self,
        request: imm_20170906_models.ListSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListSetsResponse().from_map(
            await self.do_rpcrequest_async('ListSets', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListSetTagsResponse().from_map(
            self.do_rpcrequest('ListSetTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_set_tags_with_options_async(
        self,
        request: imm_20170906_models.ListSetTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListSetTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListSetTagsResponse().from_map(
            await self.do_rpcrequest_async('ListSetTags', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoAudiosResponse().from_map(
            self.do_rpcrequest('ListVideoAudios', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_video_audios_with_options_async(
        self,
        request: imm_20170906_models.ListVideoAudiosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoAudiosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoAudiosResponse().from_map(
            await self.do_rpcrequest_async('ListVideoAudios', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoFramesResponse().from_map(
            self.do_rpcrequest('ListVideoFrames', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_video_frames_with_options_async(
        self,
        request: imm_20170906_models.ListVideoFramesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoFramesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoFramesResponse().from_map(
            await self.do_rpcrequest_async('ListVideoFrames', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideosResponse().from_map(
            self.do_rpcrequest('ListVideos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_videos_with_options_async(
        self,
        request: imm_20170906_models.ListVideosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideosResponse().from_map(
            await self.do_rpcrequest_async('ListVideos', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoTasksResponse().from_map(
            self.do_rpcrequest('ListVideoTasks', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_video_tasks_with_options_async(
        self,
        request: imm_20170906_models.ListVideoTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.ListVideoTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.ListVideoTasksResponse().from_map(
            await self.do_rpcrequest_async('ListVideoTasks', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.OpenImmServiceResponse().from_map(
            self.do_rpcrequest('OpenImmService', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_imm_service_with_options_async(
        self,
        request: imm_20170906_models.OpenImmServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.OpenImmServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.OpenImmServiceResponse().from_map(
            await self.do_rpcrequest_async('OpenImmService', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.PutProjectResponse().from_map(
            self.do_rpcrequest('PutProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_project_with_options_async(
        self,
        request: imm_20170906_models.PutProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.PutProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.PutProjectResponse().from_map(
            await self.do_rpcrequest_async('PutProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshOfficeEditTokenResponse().from_map(
            self.do_rpcrequest('RefreshOfficeEditToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_office_edit_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshOfficeEditTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficeEditTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshOfficeEditTokenResponse().from_map(
            await self.do_rpcrequest_async('RefreshOfficeEditToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshOfficePreviewTokenResponse().from_map(
            self.do_rpcrequest('RefreshOfficePreviewToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_office_preview_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshOfficePreviewTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshOfficePreviewTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshOfficePreviewTokenResponse().from_map(
            await self.do_rpcrequest_async('RefreshOfficePreviewToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshWebofficeTokenResponse().from_map(
            self.do_rpcrequest('RefreshWebofficeToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_weboffice_token_with_options_async(
        self,
        request: imm_20170906_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.RefreshWebofficeTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.RefreshWebofficeTokenResponse().from_map(
            await self.do_rpcrequest_async('RefreshWebofficeToken', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateFaceGroupResponse().from_map(
            self.do_rpcrequest('UpdateFaceGroup', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_face_group_with_options_async(
        self,
        request: imm_20170906_models.UpdateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateFaceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateFaceGroupResponse().from_map(
            await self.do_rpcrequest_async('UpdateFaceGroup', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateImageResponse().from_map(
            self.do_rpcrequest('UpdateImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: imm_20170906_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateImageResponse().from_map(
            await self.do_rpcrequest_async('UpdateImage', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateProjectResponse().from_map(
            self.do_rpcrequest('UpdateProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        request: imm_20170906_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateProjectResponse().from_map(
            await self.do_rpcrequest_async('UpdateProject', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateSetResponse().from_map(
            self.do_rpcrequest('UpdateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_set_with_options_async(
        self,
        request: imm_20170906_models.UpdateSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20170906_models.UpdateSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return imm_20170906_models.UpdateSetResponse().from_map(
            await self.do_rpcrequest_async('UpdateSet', '2017-09-06', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
