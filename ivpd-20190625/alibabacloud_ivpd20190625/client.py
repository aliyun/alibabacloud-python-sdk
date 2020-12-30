# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ivpd20190625 import models as ivpd_20190625_models
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
        self._endpoint = self.get_endpoint('ivpd', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def assess_composition_with_options(
        self,
        request: ivpd_20190625_models.AssessCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessCompositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessCompositionResponse().from_map(
            self.do_rpcrequest('AssessComposition', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assess_composition_with_options_async(
        self,
        request: ivpd_20190625_models.AssessCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessCompositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessCompositionResponse().from_map(
            await self.do_rpcrequest_async('AssessComposition', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assess_composition(
        self,
        request: ivpd_20190625_models.AssessCompositionRequest,
    ) -> ivpd_20190625_models.AssessCompositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.assess_composition_with_options(request, runtime)

    async def assess_composition_async(
        self,
        request: ivpd_20190625_models.AssessCompositionRequest,
    ) -> ivpd_20190625_models.AssessCompositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assess_composition_with_options_async(request, runtime)

    def assess_exposure_with_options(
        self,
        request: ivpd_20190625_models.AssessExposureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessExposureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessExposureResponse().from_map(
            self.do_rpcrequest('AssessExposure', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assess_exposure_with_options_async(
        self,
        request: ivpd_20190625_models.AssessExposureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessExposureResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessExposureResponse().from_map(
            await self.do_rpcrequest_async('AssessExposure', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assess_exposure(
        self,
        request: ivpd_20190625_models.AssessExposureRequest,
    ) -> ivpd_20190625_models.AssessExposureResponse:
        runtime = util_models.RuntimeOptions()
        return self.assess_exposure_with_options(request, runtime)

    async def assess_exposure_async(
        self,
        request: ivpd_20190625_models.AssessExposureRequest,
    ) -> ivpd_20190625_models.AssessExposureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assess_exposure_with_options_async(request, runtime)

    def assess_sharpness_with_options(
        self,
        request: ivpd_20190625_models.AssessSharpnessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessSharpnessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessSharpnessResponse().from_map(
            self.do_rpcrequest('AssessSharpness', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assess_sharpness_with_options_async(
        self,
        request: ivpd_20190625_models.AssessSharpnessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.AssessSharpnessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.AssessSharpnessResponse().from_map(
            await self.do_rpcrequest_async('AssessSharpness', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assess_sharpness(
        self,
        request: ivpd_20190625_models.AssessSharpnessRequest,
    ) -> ivpd_20190625_models.AssessSharpnessResponse:
        runtime = util_models.RuntimeOptions()
        return self.assess_sharpness_with_options(request, runtime)

    async def assess_sharpness_async(
        self,
        request: ivpd_20190625_models.AssessSharpnessRequest,
    ) -> ivpd_20190625_models.AssessSharpnessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assess_sharpness_with_options_async(request, runtime)

    def change_image_size_with_options(
        self,
        request: ivpd_20190625_models.ChangeImageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ChangeImageSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ChangeImageSizeResponse().from_map(
            self.do_rpcrequest('ChangeImageSize', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_image_size_with_options_async(
        self,
        request: ivpd_20190625_models.ChangeImageSizeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ChangeImageSizeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ChangeImageSizeResponse().from_map(
            await self.do_rpcrequest_async('ChangeImageSize', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_image_size(
        self,
        request: ivpd_20190625_models.ChangeImageSizeRequest,
    ) -> ivpd_20190625_models.ChangeImageSizeResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_image_size_with_options(request, runtime)

    async def change_image_size_async(
        self,
        request: ivpd_20190625_models.ChangeImageSizeRequest,
    ) -> ivpd_20190625_models.ChangeImageSizeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_image_size_with_options_async(request, runtime)

    def create_segment_body_job_with_options(
        self,
        request: ivpd_20190625_models.CreateSegmentBodyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.CreateSegmentBodyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.CreateSegmentBodyJobResponse().from_map(
            self.do_rpcrequest('CreateSegmentBodyJob', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_segment_body_job_with_options_async(
        self,
        request: ivpd_20190625_models.CreateSegmentBodyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.CreateSegmentBodyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.CreateSegmentBodyJobResponse().from_map(
            await self.do_rpcrequest_async('CreateSegmentBodyJob', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_segment_body_job(
        self,
        request: ivpd_20190625_models.CreateSegmentBodyJobRequest,
    ) -> ivpd_20190625_models.CreateSegmentBodyJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_segment_body_job_with_options(request, runtime)

    async def create_segment_body_job_async(
        self,
        request: ivpd_20190625_models.CreateSegmentBodyJobRequest,
    ) -> ivpd_20190625_models.CreateSegmentBodyJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_segment_body_job_with_options_async(request, runtime)

    def detect_image_elements_with_options(
        self,
        request: ivpd_20190625_models.DetectImageElementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.DetectImageElementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.DetectImageElementsResponse().from_map(
            self.do_rpcrequest('DetectImageElements', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_image_elements_with_options_async(
        self,
        request: ivpd_20190625_models.DetectImageElementsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.DetectImageElementsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.DetectImageElementsResponse().from_map(
            await self.do_rpcrequest_async('DetectImageElements', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_image_elements(
        self,
        request: ivpd_20190625_models.DetectImageElementsRequest,
    ) -> ivpd_20190625_models.DetectImageElementsResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_image_elements_with_options(request, runtime)

    async def detect_image_elements_async(
        self,
        request: ivpd_20190625_models.DetectImageElementsRequest,
    ) -> ivpd_20190625_models.DetectImageElementsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_elements_with_options_async(request, runtime)

    def detect_main_body_with_options(
        self,
        request: ivpd_20190625_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.DetectMainBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.DetectMainBodyResponse().from_map(
            self.do_rpcrequest('DetectMainBody', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detect_main_body_with_options_async(
        self,
        request: ivpd_20190625_models.DetectMainBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.DetectMainBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.DetectMainBodyResponse().from_map(
            await self.do_rpcrequest_async('DetectMainBody', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detect_main_body(
        self,
        request: ivpd_20190625_models.DetectMainBodyRequest,
    ) -> ivpd_20190625_models.DetectMainBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_main_body_with_options(request, runtime)

    async def detect_main_body_async(
        self,
        request: ivpd_20190625_models.DetectMainBodyRequest,
    ) -> ivpd_20190625_models.DetectMainBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_main_body_with_options_async(request, runtime)

    def enhance_face_with_options(
        self,
        request: ivpd_20190625_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.EnhanceFaceResponse().from_map(
            self.do_rpcrequest('EnhanceFace', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enhance_face_with_options_async(
        self,
        request: ivpd_20190625_models.EnhanceFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.EnhanceFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.EnhanceFaceResponse().from_map(
            await self.do_rpcrequest_async('EnhanceFace', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enhance_face(
        self,
        request: ivpd_20190625_models.EnhanceFaceRequest,
    ) -> ivpd_20190625_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.enhance_face_with_options(request, runtime)

    async def enhance_face_async(
        self,
        request: ivpd_20190625_models.EnhanceFaceRequest,
    ) -> ivpd_20190625_models.EnhanceFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enhance_face_with_options_async(request, runtime)

    def erase_logo_in_video_with_options(
        self,
        request: ivpd_20190625_models.EraseLogoInVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.EraseLogoInVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.EraseLogoInVideoResponse().from_map(
            self.do_rpcrequest('EraseLogoInVideo', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def erase_logo_in_video_with_options_async(
        self,
        request: ivpd_20190625_models.EraseLogoInVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.EraseLogoInVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.EraseLogoInVideoResponse().from_map(
            await self.do_rpcrequest_async('EraseLogoInVideo', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def erase_logo_in_video(
        self,
        request: ivpd_20190625_models.EraseLogoInVideoRequest,
    ) -> ivpd_20190625_models.EraseLogoInVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.erase_logo_in_video_with_options(request, runtime)

    async def erase_logo_in_video_async(
        self,
        request: ivpd_20190625_models.EraseLogoInVideoRequest,
    ) -> ivpd_20190625_models.EraseLogoInVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.erase_logo_in_video_with_options_async(request, runtime)

    def extend_image_style_with_options(
        self,
        request: ivpd_20190625_models.ExtendImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ExtendImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ExtendImageStyleResponse().from_map(
            self.do_rpcrequest('ExtendImageStyle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def extend_image_style_with_options_async(
        self,
        request: ivpd_20190625_models.ExtendImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ExtendImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ExtendImageStyleResponse().from_map(
            await self.do_rpcrequest_async('ExtendImageStyle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def extend_image_style(
        self,
        request: ivpd_20190625_models.ExtendImageStyleRequest,
    ) -> ivpd_20190625_models.ExtendImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.extend_image_style_with_options(request, runtime)

    async def extend_image_style_async(
        self,
        request: ivpd_20190625_models.ExtendImageStyleRequest,
    ) -> ivpd_20190625_models.ExtendImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extend_image_style_with_options_async(request, runtime)

    def get_async_job_result_with_options(
        self,
        request: ivpd_20190625_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetAsyncJobResultResponse().from_map(
            self.do_rpcrequest('GetAsyncJobResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_job_result_with_options_async(
        self,
        request: ivpd_20190625_models.GetAsyncJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetAsyncJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetAsyncJobResultResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncJobResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_job_result(
        self,
        request: ivpd_20190625_models.GetAsyncJobResultRequest,
    ) -> ivpd_20190625_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_job_result_with_options(request, runtime)

    async def get_async_job_result_async(
        self,
        request: ivpd_20190625_models.GetAsyncJobResultRequest,
    ) -> ivpd_20190625_models.GetAsyncJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_job_result_with_options_async(request, runtime)

    def get_async_result_with_options(
        self,
        request: ivpd_20190625_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetAsyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetAsyncResultResponse().from_map(
            self.do_rpcrequest('GetAsyncResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_async_result_with_options_async(
        self,
        request: ivpd_20190625_models.GetAsyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetAsyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetAsyncResultResponse().from_map(
            await self.do_rpcrequest_async('GetAsyncResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_result(
        self,
        request: ivpd_20190625_models.GetAsyncResultRequest,
    ) -> ivpd_20190625_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    async def get_async_result_async(
        self,
        request: ivpd_20190625_models.GetAsyncResultRequest,
    ) -> ivpd_20190625_models.GetAsyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_result_with_options_async(request, runtime)

    def get_job_result_with_options(
        self,
        request: ivpd_20190625_models.GetJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetJobResultResponse().from_map(
            self.do_rpcrequest('GetJobResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_result_with_options_async(
        self,
        request: ivpd_20190625_models.GetJobResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetJobResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetJobResultResponse().from_map(
            await self.do_rpcrequest_async('GetJobResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_result(
        self,
        request: ivpd_20190625_models.GetJobResultRequest,
    ) -> ivpd_20190625_models.GetJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_result_with_options(request, runtime)

    async def get_job_result_async(
        self,
        request: ivpd_20190625_models.GetJobResultRequest,
    ) -> ivpd_20190625_models.GetJobResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_result_with_options_async(request, runtime)

    def get_job_status_with_options(
        self,
        request: ivpd_20190625_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetJobStatusResponse().from_map(
            self.do_rpcrequest('GetJobStatus', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_status_with_options_async(
        self,
        request: ivpd_20190625_models.GetJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetJobStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetJobStatusResponse().from_map(
            await self.do_rpcrequest_async('GetJobStatus', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_status(
        self,
        request: ivpd_20190625_models.GetJobStatusRequest,
    ) -> ivpd_20190625_models.GetJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_status_with_options(request, runtime)

    async def get_job_status_async(
        self,
        request: ivpd_20190625_models.GetJobStatusRequest,
    ) -> ivpd_20190625_models.GetJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_status_with_options_async(request, runtime)

    def get_render_result_with_options(
        self,
        request: ivpd_20190625_models.GetRenderResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetRenderResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetRenderResultResponse().from_map(
            self.do_rpcrequest('GetRenderResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_render_result_with_options_async(
        self,
        request: ivpd_20190625_models.GetRenderResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetRenderResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.GetRenderResultResponse().from_map(
            await self.do_rpcrequest_async('GetRenderResult', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_render_result(
        self,
        request: ivpd_20190625_models.GetRenderResultRequest,
    ) -> ivpd_20190625_models.GetRenderResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_render_result_with_options(request, runtime)

    async def get_render_result_async(
        self,
        request: ivpd_20190625_models.GetRenderResultRequest,
    ) -> ivpd_20190625_models.GetRenderResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_render_result_with_options_async(request, runtime)

    def get_user_bucket_config_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetUserBucketConfigResponse:
        req = open_api_models.OpenApiRequest()
        return ivpd_20190625_models.GetUserBucketConfigResponse().from_map(
            self.do_rpcrequest('GetUserBucketConfig', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_bucket_config_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.GetUserBucketConfigResponse:
        req = open_api_models.OpenApiRequest()
        return ivpd_20190625_models.GetUserBucketConfigResponse().from_map(
            await self.do_rpcrequest_async('GetUserBucketConfig', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_bucket_config(self) -> ivpd_20190625_models.GetUserBucketConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_bucket_config_with_options(runtime)

    async def get_user_bucket_config_async(self) -> ivpd_20190625_models.GetUserBucketConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_bucket_config_with_options_async(runtime)

    def highlight_game_video_with_options(
        self,
        request: ivpd_20190625_models.HighlightGameVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.HighlightGameVideoResponse().from_map(
            self.do_rpcrequest('HighlightGameVideo', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def highlight_game_video_with_options_async(
        self,
        request: ivpd_20190625_models.HighlightGameVideoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.HighlightGameVideoResponse().from_map(
            await self.do_rpcrequest_async('HighlightGameVideo', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def highlight_game_video(
        self,
        request: ivpd_20190625_models.HighlightGameVideoRequest,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
        runtime = util_models.RuntimeOptions()
        return self.highlight_game_video_with_options(request, runtime)

    async def highlight_game_video_async(
        self,
        request: ivpd_20190625_models.HighlightGameVideoRequest,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.highlight_game_video_with_options_async(request, runtime)

    def highlight_game_video_advance(
        self,
        request: ivpd_20190625_models.HighlightGameVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
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
            product='ivpd',
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
        highlight_game_video_req = ivpd_20190625_models.HighlightGameVideoRequest()
        OpenApiUtilClient.convert(request, highlight_game_video_req)
        auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_url_object,
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
        highlight_game_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        highlight_game_video_resp = self.highlight_game_video_with_options(highlight_game_video_req, runtime)
        return highlight_game_video_resp

    async def highlight_game_video_advance_async(
        self,
        request: ivpd_20190625_models.HighlightGameVideoAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.HighlightGameVideoResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
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
            product='ivpd',
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
        highlight_game_video_req = ivpd_20190625_models.HighlightGameVideoRequest()
        OpenApiUtilClient.convert(request, highlight_game_video_req)
        auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
        oss_config.access_key_id = auth_response.access_key_id
        oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
        oss_client = OSSClient(oss_config)
        file_obj = file_form_models.FileField(
            filename=auth_response.object_key,
            content=request.video_url_object,
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
        highlight_game_video_req.video_url = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        highlight_game_video_resp = await self.highlight_game_video_with_options_async(highlight_game_video_req, runtime)
        return highlight_game_video_resp

    def intelligent_composition_with_options(
        self,
        request: ivpd_20190625_models.IntelligentCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.IntelligentCompositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.IntelligentCompositionResponse().from_map(
            self.do_rpcrequest('IntelligentComposition', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def intelligent_composition_with_options_async(
        self,
        request: ivpd_20190625_models.IntelligentCompositionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.IntelligentCompositionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.IntelligentCompositionResponse().from_map(
            await self.do_rpcrequest_async('IntelligentComposition', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def intelligent_composition(
        self,
        request: ivpd_20190625_models.IntelligentCompositionRequest,
    ) -> ivpd_20190625_models.IntelligentCompositionResponse:
        runtime = util_models.RuntimeOptions()
        return self.intelligent_composition_with_options(request, runtime)

    async def intelligent_composition_async(
        self,
        request: ivpd_20190625_models.IntelligentCompositionRequest,
    ) -> ivpd_20190625_models.IntelligentCompositionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.intelligent_composition_with_options_async(request, runtime)

    def list_package_design_model_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ListPackageDesignModelTypesResponse:
        req = open_api_models.OpenApiRequest()
        return ivpd_20190625_models.ListPackageDesignModelTypesResponse().from_map(
            self.do_rpcrequest('ListPackageDesignModelTypes', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_package_design_model_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ListPackageDesignModelTypesResponse:
        req = open_api_models.OpenApiRequest()
        return ivpd_20190625_models.ListPackageDesignModelTypesResponse().from_map(
            await self.do_rpcrequest_async('ListPackageDesignModelTypes', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_package_design_model_types(self) -> ivpd_20190625_models.ListPackageDesignModelTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_package_design_model_types_with_options(runtime)

    async def list_package_design_model_types_async(self) -> ivpd_20190625_models.ListPackageDesignModelTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_package_design_model_types_with_options_async(runtime)

    def list_user_buckets_with_options(
        self,
        request: ivpd_20190625_models.ListUserBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ListUserBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ListUserBucketsResponse().from_map(
            self.do_rpcrequest('ListUserBuckets', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_buckets_with_options_async(
        self,
        request: ivpd_20190625_models.ListUserBucketsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ListUserBucketsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ListUserBucketsResponse().from_map(
            await self.do_rpcrequest_async('ListUserBuckets', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_buckets(
        self,
        request: ivpd_20190625_models.ListUserBucketsRequest,
    ) -> ivpd_20190625_models.ListUserBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_buckets_with_options(request, runtime)

    async def list_user_buckets_async(
        self,
        request: ivpd_20190625_models.ListUserBucketsRequest,
    ) -> ivpd_20190625_models.ListUserBucketsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_buckets_with_options_async(request, runtime)

    def make_super_resolution_image_with_options(
        self,
        request: ivpd_20190625_models.MakeSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.MakeSuperResolutionImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.MakeSuperResolutionImageResponse().from_map(
            self.do_rpcrequest('MakeSuperResolutionImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def make_super_resolution_image_with_options_async(
        self,
        request: ivpd_20190625_models.MakeSuperResolutionImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.MakeSuperResolutionImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.MakeSuperResolutionImageResponse().from_map(
            await self.do_rpcrequest_async('MakeSuperResolutionImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def make_super_resolution_image(
        self,
        request: ivpd_20190625_models.MakeSuperResolutionImageRequest,
    ) -> ivpd_20190625_models.MakeSuperResolutionImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.make_super_resolution_image_with_options(request, runtime)

    async def make_super_resolution_image_async(
        self,
        request: ivpd_20190625_models.MakeSuperResolutionImageRequest,
    ) -> ivpd_20190625_models.MakeSuperResolutionImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.make_super_resolution_image_with_options_async(request, runtime)

    def parse_face_with_options(
        self,
        request: ivpd_20190625_models.ParseFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ParseFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ParseFaceResponse().from_map(
            self.do_rpcrequest('ParseFace', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def parse_face_with_options_async(
        self,
        request: ivpd_20190625_models.ParseFaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.ParseFaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.ParseFaceResponse().from_map(
            await self.do_rpcrequest_async('ParseFace', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def parse_face(
        self,
        request: ivpd_20190625_models.ParseFaceRequest,
    ) -> ivpd_20190625_models.ParseFaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.parse_face_with_options(request, runtime)

    async def parse_face_async(
        self,
        request: ivpd_20190625_models.ParseFaceRequest,
    ) -> ivpd_20190625_models.ParseFaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.parse_face_with_options_async(request, runtime)

    def preview_model_for_package_design_with_options(
        self,
        request: ivpd_20190625_models.PreviewModelForPackageDesignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.PreviewModelForPackageDesignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.PreviewModelForPackageDesignResponse().from_map(
            self.do_rpcrequest('PreviewModelForPackageDesign', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def preview_model_for_package_design_with_options_async(
        self,
        request: ivpd_20190625_models.PreviewModelForPackageDesignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.PreviewModelForPackageDesignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.PreviewModelForPackageDesignResponse().from_map(
            await self.do_rpcrequest_async('PreviewModelForPackageDesign', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def preview_model_for_package_design(
        self,
        request: ivpd_20190625_models.PreviewModelForPackageDesignRequest,
    ) -> ivpd_20190625_models.PreviewModelForPackageDesignResponse:
        runtime = util_models.RuntimeOptions()
        return self.preview_model_for_package_design_with_options(request, runtime)

    async def preview_model_for_package_design_async(
        self,
        request: ivpd_20190625_models.PreviewModelForPackageDesignRequest,
    ) -> ivpd_20190625_models.PreviewModelForPackageDesignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.preview_model_for_package_design_with_options_async(request, runtime)

    def recognize_image_color_with_options(
        self,
        request: ivpd_20190625_models.RecognizeImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecognizeImageColorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecognizeImageColorResponse().from_map(
            self.do_rpcrequest('RecognizeImageColor', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_color_with_options_async(
        self,
        request: ivpd_20190625_models.RecognizeImageColorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecognizeImageColorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecognizeImageColorResponse().from_map(
            await self.do_rpcrequest_async('RecognizeImageColor', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image_color(
        self,
        request: ivpd_20190625_models.RecognizeImageColorRequest,
    ) -> ivpd_20190625_models.RecognizeImageColorResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_color_with_options(request, runtime)

    async def recognize_image_color_async(
        self,
        request: ivpd_20190625_models.RecognizeImageColorRequest,
    ) -> ivpd_20190625_models.RecognizeImageColorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_color_with_options_async(request, runtime)

    def recognize_image_style_with_options(
        self,
        request: ivpd_20190625_models.RecognizeImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecognizeImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecognizeImageStyleResponse().from_map(
            self.do_rpcrequest('RecognizeImageStyle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recognize_image_style_with_options_async(
        self,
        request: ivpd_20190625_models.RecognizeImageStyleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecognizeImageStyleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecognizeImageStyleResponse().from_map(
            await self.do_rpcrequest_async('RecognizeImageStyle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recognize_image_style(
        self,
        request: ivpd_20190625_models.RecognizeImageStyleRequest,
    ) -> ivpd_20190625_models.RecognizeImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_style_with_options(request, runtime)

    async def recognize_image_style_async(
        self,
        request: ivpd_20190625_models.RecognizeImageStyleRequest,
    ) -> ivpd_20190625_models.RecognizeImageStyleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recognize_image_style_with_options_async(request, runtime)

    def recolor_image_with_options(
        self,
        request: ivpd_20190625_models.RecolorImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecolorImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecolorImageResponse().from_map(
            self.do_rpcrequest('RecolorImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recolor_image_with_options_async(
        self,
        request: ivpd_20190625_models.RecolorImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RecolorImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RecolorImageResponse().from_map(
            await self.do_rpcrequest_async('RecolorImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recolor_image(
        self,
        request: ivpd_20190625_models.RecolorImageRequest,
    ) -> ivpd_20190625_models.RecolorImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.recolor_image_with_options(request, runtime)

    async def recolor_image_async(
        self,
        request: ivpd_20190625_models.RecolorImageRequest,
    ) -> ivpd_20190625_models.RecolorImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recolor_image_with_options_async(request, runtime)

    def render_image_for_package_design_with_options(
        self,
        request: ivpd_20190625_models.RenderImageForPackageDesignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RenderImageForPackageDesignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RenderImageForPackageDesignResponse().from_map(
            self.do_rpcrequest('RenderImageForPackageDesign', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def render_image_for_package_design_with_options_async(
        self,
        request: ivpd_20190625_models.RenderImageForPackageDesignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.RenderImageForPackageDesignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.RenderImageForPackageDesignResponse().from_map(
            await self.do_rpcrequest_async('RenderImageForPackageDesign', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def render_image_for_package_design(
        self,
        request: ivpd_20190625_models.RenderImageForPackageDesignRequest,
    ) -> ivpd_20190625_models.RenderImageForPackageDesignResponse:
        runtime = util_models.RuntimeOptions()
        return self.render_image_for_package_design_with_options(request, runtime)

    async def render_image_for_package_design_async(
        self,
        request: ivpd_20190625_models.RenderImageForPackageDesignRequest,
    ) -> ivpd_20190625_models.RenderImageForPackageDesignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.render_image_for_package_design_with_options_async(request, runtime)

    def segment_animal_with_options(
        self,
        request: ivpd_20190625_models.SegmentAnimalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentAnimalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentAnimalResponse().from_map(
            self.do_rpcrequest('SegmentAnimal', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_animal_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentAnimalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentAnimalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentAnimalResponse().from_map(
            await self.do_rpcrequest_async('SegmentAnimal', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_animal(
        self,
        request: ivpd_20190625_models.SegmentAnimalRequest,
    ) -> ivpd_20190625_models.SegmentAnimalResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_animal_with_options(request, runtime)

    async def segment_animal_async(
        self,
        request: ivpd_20190625_models.SegmentAnimalRequest,
    ) -> ivpd_20190625_models.SegmentAnimalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_animal_with_options_async(request, runtime)

    def segment_body_with_options(
        self,
        request: ivpd_20190625_models.SegmentBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentBodyResponse().from_map(
            self.do_rpcrequest('SegmentBody', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_body_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentBodyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentBodyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentBodyResponse().from_map(
            await self.do_rpcrequest_async('SegmentBody', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_body(
        self,
        request: ivpd_20190625_models.SegmentBodyRequest,
    ) -> ivpd_20190625_models.SegmentBodyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_body_with_options(request, runtime)

    async def segment_body_async(
        self,
        request: ivpd_20190625_models.SegmentBodyRequest,
    ) -> ivpd_20190625_models.SegmentBodyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_body_with_options_async(request, runtime)

    def segment_cloth_with_options(
        self,
        request: ivpd_20190625_models.SegmentClothRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentClothResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentClothResponse().from_map(
            self.do_rpcrequest('SegmentCloth', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_cloth_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentClothRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentClothResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentClothResponse().from_map(
            await self.do_rpcrequest_async('SegmentCloth', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_cloth(
        self,
        request: ivpd_20190625_models.SegmentClothRequest,
    ) -> ivpd_20190625_models.SegmentClothResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_cloth_with_options(request, runtime)

    async def segment_cloth_async(
        self,
        request: ivpd_20190625_models.SegmentClothRequest,
    ) -> ivpd_20190625_models.SegmentClothResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_cloth_with_options_async(request, runtime)

    def segment_commodity_with_options(
        self,
        request: ivpd_20190625_models.SegmentCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentCommodityResponse().from_map(
            self.do_rpcrequest('SegmentCommodity', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_commodity_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentCommodityResponse().from_map(
            await self.do_rpcrequest_async('SegmentCommodity', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_commodity(
        self,
        request: ivpd_20190625_models.SegmentCommodityRequest,
    ) -> ivpd_20190625_models.SegmentCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_commodity_with_options(request, runtime)

    async def segment_commodity_async(
        self,
        request: ivpd_20190625_models.SegmentCommodityRequest,
    ) -> ivpd_20190625_models.SegmentCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_commodity_with_options_async(request, runtime)

    def segment_hair_with_options(
        self,
        request: ivpd_20190625_models.SegmentHairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentHairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentHairResponse().from_map(
            self.do_rpcrequest('SegmentHair', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_hair_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentHairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentHairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentHairResponse().from_map(
            await self.do_rpcrequest_async('SegmentHair', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_hair(
        self,
        request: ivpd_20190625_models.SegmentHairRequest,
    ) -> ivpd_20190625_models.SegmentHairResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_hair_with_options(request, runtime)

    async def segment_hair_async(
        self,
        request: ivpd_20190625_models.SegmentHairRequest,
    ) -> ivpd_20190625_models.SegmentHairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_hair_with_options_async(request, runtime)

    def segment_head_with_options(
        self,
        request: ivpd_20190625_models.SegmentHeadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentHeadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentHeadResponse().from_map(
            self.do_rpcrequest('SegmentHead', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_head_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentHeadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentHeadResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentHeadResponse().from_map(
            await self.do_rpcrequest_async('SegmentHead', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_head(
        self,
        request: ivpd_20190625_models.SegmentHeadRequest,
    ) -> ivpd_20190625_models.SegmentHeadResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_head_with_options(request, runtime)

    async def segment_head_async(
        self,
        request: ivpd_20190625_models.SegmentHeadRequest,
    ) -> ivpd_20190625_models.SegmentHeadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_head_with_options_async(request, runtime)

    def segment_image_with_options(
        self,
        request: ivpd_20190625_models.SegmentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentImageResponse().from_map(
            self.do_rpcrequest('SegmentImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_image_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentImageResponse().from_map(
            await self.do_rpcrequest_async('SegmentImage', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_image(
        self,
        request: ivpd_20190625_models.SegmentImageRequest,
    ) -> ivpd_20190625_models.SegmentImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_image_with_options(request, runtime)

    async def segment_image_async(
        self,
        request: ivpd_20190625_models.SegmentImageRequest,
    ) -> ivpd_20190625_models.SegmentImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_image_with_options_async(request, runtime)

    def segment_sky_with_options(
        self,
        request: ivpd_20190625_models.SegmentSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentSkyResponse().from_map(
            self.do_rpcrequest('SegmentSky', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_sky_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentSkyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentSkyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentSkyResponse().from_map(
            await self.do_rpcrequest_async('SegmentSky', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_sky(
        self,
        request: ivpd_20190625_models.SegmentSkyRequest,
    ) -> ivpd_20190625_models.SegmentSkyResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_sky_with_options(request, runtime)

    async def segment_sky_async(
        self,
        request: ivpd_20190625_models.SegmentSkyRequest,
    ) -> ivpd_20190625_models.SegmentSkyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_sky_with_options_async(request, runtime)

    def segment_vehicle_with_options(
        self,
        request: ivpd_20190625_models.SegmentVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentVehicleResponse().from_map(
            self.do_rpcrequest('SegmentVehicle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def segment_vehicle_with_options_async(
        self,
        request: ivpd_20190625_models.SegmentVehicleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.SegmentVehicleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.SegmentVehicleResponse().from_map(
            await self.do_rpcrequest_async('SegmentVehicle', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def segment_vehicle(
        self,
        request: ivpd_20190625_models.SegmentVehicleRequest,
    ) -> ivpd_20190625_models.SegmentVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return self.segment_vehicle_with_options(request, runtime)

    async def segment_vehicle_async(
        self,
        request: ivpd_20190625_models.SegmentVehicleRequest,
    ) -> ivpd_20190625_models.SegmentVehicleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.segment_vehicle_with_options_async(request, runtime)

    def update_user_bucket_config_with_options(
        self,
        request: ivpd_20190625_models.UpdateUserBucketConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.UpdateUserBucketConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.UpdateUserBucketConfigResponse().from_map(
            self.do_rpcrequest('UpdateUserBucketConfig', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_bucket_config_with_options_async(
        self,
        request: ivpd_20190625_models.UpdateUserBucketConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ivpd_20190625_models.UpdateUserBucketConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ivpd_20190625_models.UpdateUserBucketConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateUserBucketConfig', '2019-06-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user_bucket_config(
        self,
        request: ivpd_20190625_models.UpdateUserBucketConfigRequest,
    ) -> ivpd_20190625_models.UpdateUserBucketConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_bucket_config_with_options(request, runtime)

    async def update_user_bucket_config_async(
        self,
        request: ivpd_20190625_models.UpdateUserBucketConfigRequest,
    ) -> ivpd_20190625_models.UpdateUserBucketConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_bucket_config_with_options_async(request, runtime)
