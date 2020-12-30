# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_multimediaai20190810 import models as multimediaai_20190810_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('multimediaai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_cover_task_with_options(
        self,
        request: multimediaai_20190810_models.CreateCoverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateCoverTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateCoverTaskResponse().from_map(
            self.do_rpcrequest('CreateCoverTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cover_task_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateCoverTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateCoverTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateCoverTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateCoverTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cover_task(
        self,
        request: multimediaai_20190810_models.CreateCoverTaskRequest,
    ) -> multimediaai_20190810_models.CreateCoverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cover_task_with_options(request, runtime)

    async def create_cover_task_async(
        self,
        request: multimediaai_20190810_models.CreateCoverTaskRequest,
    ) -> multimediaai_20190810_models.CreateCoverTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cover_task_with_options_async(request, runtime)

    def create_face_group_with_options(
        self,
        request: multimediaai_20190810_models.CreateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateFaceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateFaceGroupResponse().from_map(
            self.do_rpcrequest('CreateFaceGroup', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_face_group_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateFaceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateFaceGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateFaceGroup', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_face_group(
        self,
        request: multimediaai_20190810_models.CreateFaceGroupRequest,
    ) -> multimediaai_20190810_models.CreateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_group_with_options(request, runtime)

    async def create_face_group_async(
        self,
        request: multimediaai_20190810_models.CreateFaceGroupRequest,
    ) -> multimediaai_20190810_models.CreateFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_group_with_options_async(request, runtime)

    def create_face_person_with_options(
        self,
        request: multimediaai_20190810_models.CreateFacePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateFacePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateFacePersonResponse().from_map(
            self.do_rpcrequest('CreateFacePerson', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_face_person_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateFacePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateFacePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateFacePersonResponse().from_map(
            await self.do_rpcrequest_async('CreateFacePerson', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_face_person(
        self,
        request: multimediaai_20190810_models.CreateFacePersonRequest,
    ) -> multimediaai_20190810_models.CreateFacePersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_face_person_with_options(request, runtime)

    async def create_face_person_async(
        self,
        request: multimediaai_20190810_models.CreateFacePersonRequest,
    ) -> multimediaai_20190810_models.CreateFacePersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_face_person_with_options_async(request, runtime)

    def create_gif_task_with_options(
        self,
        request: multimediaai_20190810_models.CreateGifTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateGifTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateGifTaskResponse().from_map(
            self.do_rpcrequest('CreateGifTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_gif_task_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateGifTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateGifTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateGifTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateGifTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_gif_task(
        self,
        request: multimediaai_20190810_models.CreateGifTaskRequest,
    ) -> multimediaai_20190810_models.CreateGifTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_gif_task_with_options(request, runtime)

    async def create_gif_task_async(
        self,
        request: multimediaai_20190810_models.CreateGifTaskRequest,
    ) -> multimediaai_20190810_models.CreateGifTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_gif_task_with_options_async(request, runtime)

    def create_label_task_with_options(
        self,
        request: multimediaai_20190810_models.CreateLabelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateLabelTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateLabelTaskResponse().from_map(
            self.do_rpcrequest('CreateLabelTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_label_task_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateLabelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateLabelTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateLabelTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateLabelTask', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_label_task(
        self,
        request: multimediaai_20190810_models.CreateLabelTaskRequest,
    ) -> multimediaai_20190810_models.CreateLabelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_label_task_with_options(request, runtime)

    async def create_label_task_async(
        self,
        request: multimediaai_20190810_models.CreateLabelTaskRequest,
    ) -> multimediaai_20190810_models.CreateLabelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_label_task_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: multimediaai_20190810_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateTemplateResponse().from_map(
            self.do_rpcrequest('CreateTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: multimediaai_20190810_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.CreateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.CreateTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(
        self,
        request: multimediaai_20190810_models.CreateTemplateRequest,
    ) -> multimediaai_20190810_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: multimediaai_20190810_models.CreateTemplateRequest,
    ) -> multimediaai_20190810_models.CreateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_face_group_with_options(
        self,
        request: multimediaai_20190810_models.DeleteFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFaceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFaceGroupResponse().from_map(
            self.do_rpcrequest('DeleteFaceGroup', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_group_with_options_async(
        self,
        request: multimediaai_20190810_models.DeleteFaceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFaceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFaceGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceGroup', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_group(
        self,
        request: multimediaai_20190810_models.DeleteFaceGroupRequest,
    ) -> multimediaai_20190810_models.DeleteFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_group_with_options(request, runtime)

    async def delete_face_group_async(
        self,
        request: multimediaai_20190810_models.DeleteFaceGroupRequest,
    ) -> multimediaai_20190810_models.DeleteFaceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_group_with_options_async(request, runtime)

    def delete_face_image_with_options(
        self,
        request: multimediaai_20190810_models.DeleteFaceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFaceImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFaceImageResponse().from_map(
            self.do_rpcrequest('DeleteFaceImage', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_image_with_options_async(
        self,
        request: multimediaai_20190810_models.DeleteFaceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFaceImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFaceImageResponse().from_map(
            await self.do_rpcrequest_async('DeleteFaceImage', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_image(
        self,
        request: multimediaai_20190810_models.DeleteFaceImageRequest,
    ) -> multimediaai_20190810_models.DeleteFaceImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_image_with_options(request, runtime)

    async def delete_face_image_async(
        self,
        request: multimediaai_20190810_models.DeleteFaceImageRequest,
    ) -> multimediaai_20190810_models.DeleteFaceImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_image_with_options_async(request, runtime)

    def delete_face_person_with_options(
        self,
        request: multimediaai_20190810_models.DeleteFacePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFacePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFacePersonResponse().from_map(
            self.do_rpcrequest('DeleteFacePerson', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_face_person_with_options_async(
        self,
        request: multimediaai_20190810_models.DeleteFacePersonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.DeleteFacePersonResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.DeleteFacePersonResponse().from_map(
            await self.do_rpcrequest_async('DeleteFacePerson', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_face_person(
        self,
        request: multimediaai_20190810_models.DeleteFacePersonRequest,
    ) -> multimediaai_20190810_models.DeleteFacePersonResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_face_person_with_options(request, runtime)

    async def delete_face_person_async(
        self,
        request: multimediaai_20190810_models.DeleteFacePersonRequest,
    ) -> multimediaai_20190810_models.DeleteFacePersonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_face_person_with_options_async(request, runtime)

    def get_task_result_with_options(
        self,
        request: multimediaai_20190810_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTaskResultResponse().from_map(
            self.do_rpcrequest('GetTaskResult', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_result_with_options_async(
        self,
        request: multimediaai_20190810_models.GetTaskResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTaskResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTaskResultResponse().from_map(
            await self.do_rpcrequest_async('GetTaskResult', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_result(
        self,
        request: multimediaai_20190810_models.GetTaskResultRequest,
    ) -> multimediaai_20190810_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_result_with_options(request, runtime)

    async def get_task_result_async(
        self,
        request: multimediaai_20190810_models.GetTaskResultRequest,
    ) -> multimediaai_20190810_models.GetTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_result_with_options_async(request, runtime)

    def get_task_status_with_options(
        self,
        request: multimediaai_20190810_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTaskStatusResponse().from_map(
            self.do_rpcrequest('GetTaskStatus', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_status_with_options_async(
        self,
        request: multimediaai_20190810_models.GetTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTaskStatusResponse().from_map(
            await self.do_rpcrequest_async('GetTaskStatus', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_status(
        self,
        request: multimediaai_20190810_models.GetTaskStatusRequest,
    ) -> multimediaai_20190810_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_status_with_options(request, runtime)

    async def get_task_status_async(
        self,
        request: multimediaai_20190810_models.GetTaskStatusRequest,
    ) -> multimediaai_20190810_models.GetTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_status_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: multimediaai_20190810_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTemplateResponse().from_map(
            self.do_rpcrequest('GetTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: multimediaai_20190810_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.GetTemplateResponse().from_map(
            await self.do_rpcrequest_async('GetTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_template(
        self,
        request: multimediaai_20190810_models.GetTemplateRequest,
    ) -> multimediaai_20190810_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: multimediaai_20190810_models.GetTemplateRequest,
    ) -> multimediaai_20190810_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def list_face_groups_with_options(
        self,
        request: multimediaai_20190810_models.ListFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFaceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFaceGroupsResponse().from_map(
            self.do_rpcrequest('ListFaceGroups', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_groups_with_options_async(
        self,
        request: multimediaai_20190810_models.ListFaceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFaceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFaceGroupsResponse().from_map(
            await self.do_rpcrequest_async('ListFaceGroups', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_groups(
        self,
        request: multimediaai_20190810_models.ListFaceGroupsRequest,
    ) -> multimediaai_20190810_models.ListFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_groups_with_options(request, runtime)

    async def list_face_groups_async(
        self,
        request: multimediaai_20190810_models.ListFaceGroupsRequest,
    ) -> multimediaai_20190810_models.ListFaceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_groups_with_options_async(request, runtime)

    def list_face_images_with_options(
        self,
        request: multimediaai_20190810_models.ListFaceImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFaceImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFaceImagesResponse().from_map(
            self.do_rpcrequest('ListFaceImages', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_images_with_options_async(
        self,
        request: multimediaai_20190810_models.ListFaceImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFaceImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFaceImagesResponse().from_map(
            await self.do_rpcrequest_async('ListFaceImages', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_images(
        self,
        request: multimediaai_20190810_models.ListFaceImagesRequest,
    ) -> multimediaai_20190810_models.ListFaceImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_images_with_options(request, runtime)

    async def list_face_images_async(
        self,
        request: multimediaai_20190810_models.ListFaceImagesRequest,
    ) -> multimediaai_20190810_models.ListFaceImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_images_with_options_async(request, runtime)

    def list_face_persons_with_options(
        self,
        request: multimediaai_20190810_models.ListFacePersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFacePersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFacePersonsResponse().from_map(
            self.do_rpcrequest('ListFacePersons', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_face_persons_with_options_async(
        self,
        request: multimediaai_20190810_models.ListFacePersonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListFacePersonsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListFacePersonsResponse().from_map(
            await self.do_rpcrequest_async('ListFacePersons', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_face_persons(
        self,
        request: multimediaai_20190810_models.ListFacePersonsRequest,
    ) -> multimediaai_20190810_models.ListFacePersonsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_face_persons_with_options(request, runtime)

    async def list_face_persons_async(
        self,
        request: multimediaai_20190810_models.ListFacePersonsRequest,
    ) -> multimediaai_20190810_models.ListFacePersonsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_face_persons_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: multimediaai_20190810_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListTemplatesResponse().from_map(
            self.do_rpcrequest('ListTemplates', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: multimediaai_20190810_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ListTemplatesResponse().from_map(
            await self.do_rpcrequest_async('ListTemplates', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: multimediaai_20190810_models.ListTemplatesRequest,
    ) -> multimediaai_20190810_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: multimediaai_20190810_models.ListTemplatesRequest,
    ) -> multimediaai_20190810_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def process_face_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessFaceAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessFaceAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessFaceAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessFaceAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_face_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessFaceAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessFaceAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessFaceAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessFaceAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_face_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessFaceAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessFaceAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_face_algorithm_with_options(request, runtime)

    async def process_face_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessFaceAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessFaceAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_face_algorithm_with_options_async(request, runtime)

    def process_image_tag_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessImageTagAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessImageTagAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessImageTagAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessImageTagAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_image_tag_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessImageTagAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessImageTagAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessImageTagAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessImageTagAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_image_tag_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessImageTagAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessImageTagAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_image_tag_algorithm_with_options(request, runtime)

    async def process_image_tag_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessImageTagAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessImageTagAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_image_tag_algorithm_with_options_async(request, runtime)

    def process_landmark_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessLandmarkAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessLandmarkAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_landmark_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessLandmarkAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessLandmarkAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_landmark_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessLandmarkAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_landmark_algorithm_with_options(request, runtime)

    async def process_landmark_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessLandmarkAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessLandmarkAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_landmark_algorithm_with_options_async(request, runtime)

    def process_logo_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessLogoAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessLogoAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessLogoAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessLogoAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_logo_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessLogoAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessLogoAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessLogoAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessLogoAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_logo_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessLogoAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessLogoAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_logo_algorithm_with_options(request, runtime)

    async def process_logo_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessLogoAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessLogoAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_logo_algorithm_with_options_async(request, runtime)

    def process_news_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessNewsAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessNewsAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessNewsAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessNewsAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_news_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessNewsAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessNewsAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessNewsAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessNewsAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_news_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessNewsAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessNewsAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_news_algorithm_with_options(request, runtime)

    async def process_news_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessNewsAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessNewsAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_news_algorithm_with_options_async(request, runtime)

    def process_nlp_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessNlpAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessNlpAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessNlpAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessNlpAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_nlp_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessNlpAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessNlpAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessNlpAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessNlpAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_nlp_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessNlpAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessNlpAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_nlp_algorithm_with_options(request, runtime)

    async def process_nlp_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessNlpAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessNlpAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_nlp_algorithm_with_options_async(request, runtime)

    def process_ocr_algorithm_with_options(
        self,
        request: multimediaai_20190810_models.ProcessOcrAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessOcrAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessOcrAlgorithmResponse().from_map(
            self.do_rpcrequest('ProcessOcrAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def process_ocr_algorithm_with_options_async(
        self,
        request: multimediaai_20190810_models.ProcessOcrAlgorithmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.ProcessOcrAlgorithmResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.ProcessOcrAlgorithmResponse().from_map(
            await self.do_rpcrequest_async('ProcessOcrAlgorithm', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def process_ocr_algorithm(
        self,
        request: multimediaai_20190810_models.ProcessOcrAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessOcrAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return self.process_ocr_algorithm_with_options(request, runtime)

    async def process_ocr_algorithm_async(
        self,
        request: multimediaai_20190810_models.ProcessOcrAlgorithmRequest,
    ) -> multimediaai_20190810_models.ProcessOcrAlgorithmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.process_ocr_algorithm_with_options_async(request, runtime)

    def register_face_image_with_options(
        self,
        request: multimediaai_20190810_models.RegisterFaceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.RegisterFaceImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.RegisterFaceImageResponse().from_map(
            self.do_rpcrequest('RegisterFaceImage', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def register_face_image_with_options_async(
        self,
        request: multimediaai_20190810_models.RegisterFaceImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.RegisterFaceImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.RegisterFaceImageResponse().from_map(
            await self.do_rpcrequest_async('RegisterFaceImage', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_face_image(
        self,
        request: multimediaai_20190810_models.RegisterFaceImageRequest,
    ) -> multimediaai_20190810_models.RegisterFaceImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_face_image_with_options(request, runtime)

    async def register_face_image_async(
        self,
        request: multimediaai_20190810_models.RegisterFaceImageRequest,
    ) -> multimediaai_20190810_models.RegisterFaceImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_face_image_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: multimediaai_20190810_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.UpdateTemplateResponse().from_map(
            self.do_rpcrequest('UpdateTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: multimediaai_20190810_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> multimediaai_20190810_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return multimediaai_20190810_models.UpdateTemplateResponse().from_map(
            await self.do_rpcrequest_async('UpdateTemplate', '2019-08-10', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_template(
        self,
        request: multimediaai_20190810_models.UpdateTemplateRequest,
    ) -> multimediaai_20190810_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: multimediaai_20190810_models.UpdateTemplateRequest,
    ) -> multimediaai_20190810_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)
