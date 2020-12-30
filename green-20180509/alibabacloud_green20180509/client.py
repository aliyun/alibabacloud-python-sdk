# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20180509 import models as green_20180509_models
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
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_faces(
        self,
        request: green_20180509_models.AddFacesRequest,
    ) -> green_20180509_models.AddFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_faces_with_options(request, headers, runtime)

    async def add_faces_async(
        self,
        request: green_20180509_models.AddFacesRequest,
    ) -> green_20180509_models.AddFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_faces_with_options_async(request, headers, runtime)

    def add_faces_with_options(
        self,
        request: green_20180509_models.AddFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddFacesResponse().from_map(
            self.do_roarequest('AddFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/face/add', 'none', req, runtime)
        )

    async def add_faces_with_options_async(
        self,
        request: green_20180509_models.AddFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddFacesResponse().from_map(
            await self.do_roarequest_async('AddFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/face/add', 'none', req, runtime)
        )

    def add_groups(
        self,
        request: green_20180509_models.AddGroupsRequest,
    ) -> green_20180509_models.AddGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_groups_with_options(request, headers, runtime)

    async def add_groups_async(
        self,
        request: green_20180509_models.AddGroupsRequest,
    ) -> green_20180509_models.AddGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_groups_with_options_async(request, headers, runtime)

    def add_groups_with_options(
        self,
        request: green_20180509_models.AddGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddGroupsResponse().from_map(
            self.do_roarequest('AddGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/groups/add', 'none', req, runtime)
        )

    async def add_groups_with_options_async(
        self,
        request: green_20180509_models.AddGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddGroupsResponse().from_map(
            await self.do_roarequest_async('AddGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/groups/add', 'none', req, runtime)
        )

    def add_person(
        self,
        request: green_20180509_models.AddPersonRequest,
    ) -> green_20180509_models.AddPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_person_with_options(request, headers, runtime)

    async def add_person_async(
        self,
        request: green_20180509_models.AddPersonRequest,
    ) -> green_20180509_models.AddPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_person_with_options_async(request, headers, runtime)

    def add_person_with_options(
        self,
        request: green_20180509_models.AddPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddPersonResponse().from_map(
            self.do_roarequest('AddPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/add', 'none', req, runtime)
        )

    async def add_person_with_options_async(
        self,
        request: green_20180509_models.AddPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddPersonResponse().from_map(
            await self.do_roarequest_async('AddPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/add', 'none', req, runtime)
        )

    def add_similarity_image(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_similarity_image_with_options(request, headers, runtime)

    async def add_similarity_image_async(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_similarity_image_with_options_async(request, headers, runtime)

    def add_similarity_image_with_options(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddSimilarityImageResponse().from_map(
            self.do_roarequest('AddSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/add', 'none', req, runtime)
        )

    async def add_similarity_image_with_options_async(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddSimilarityImageResponse().from_map(
            await self.do_roarequest_async('AddSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/add', 'none', req, runtime)
        )

    def add_similarity_library(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_similarity_library_with_options(request, headers, runtime)

    async def add_similarity_library_async(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_similarity_library_with_options_async(request, headers, runtime)

    def add_similarity_library_with_options(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddSimilarityLibraryResponse().from_map(
            self.do_roarequest('AddSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/add', 'none', req, runtime)
        )

    async def add_similarity_library_with_options_async(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddSimilarityLibraryResponse().from_map(
            await self.do_roarequest_async('AddSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/add', 'none', req, runtime)
        )

    def add_video_dna(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
    ) -> green_20180509_models.AddVideoDnaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_video_dna_with_options(request, headers, runtime)

    async def add_video_dna_async(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
    ) -> green_20180509_models.AddVideoDnaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_video_dna_with_options_async(request, headers, runtime)

    def add_video_dna_with_options(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddVideoDnaResponse().from_map(
            self.do_roarequest('AddVideoDna', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/add', 'none', req, runtime)
        )

    async def add_video_dna_with_options_async(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddVideoDnaResponse().from_map(
            await self.do_roarequest_async('AddVideoDna', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/add', 'none', req, runtime)
        )

    def add_video_dna_group(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_video_dna_group_with_options(request, headers, runtime)

    async def add_video_dna_group_async(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_video_dna_group_with_options_async(request, headers, runtime)

    def add_video_dna_group_with_options(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddVideoDnaGroupResponse().from_map(
            self.do_roarequest('AddVideoDnaGroup', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/group/add', 'none', req, runtime)
        )

    async def add_video_dna_group_with_options_async(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.AddVideoDnaGroupResponse().from_map(
            await self.do_roarequest_async('AddVideoDnaGroup', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/group/add', 'none', req, runtime)
        )

    def delete_faces(
        self,
        request: green_20180509_models.DeleteFacesRequest,
    ) -> green_20180509_models.DeleteFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_faces_with_options(request, headers, runtime)

    async def delete_faces_async(
        self,
        request: green_20180509_models.DeleteFacesRequest,
    ) -> green_20180509_models.DeleteFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_faces_with_options_async(request, headers, runtime)

    def delete_faces_with_options(
        self,
        request: green_20180509_models.DeleteFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteFacesResponse().from_map(
            self.do_roarequest('DeleteFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/face/delete', 'none', req, runtime)
        )

    async def delete_faces_with_options_async(
        self,
        request: green_20180509_models.DeleteFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteFacesResponse().from_map(
            await self.do_roarequest_async('DeleteFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/face/delete', 'none', req, runtime)
        )

    def delete_groups(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
    ) -> green_20180509_models.DeleteGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_groups_with_options(request, headers, runtime)

    async def delete_groups_async(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
    ) -> green_20180509_models.DeleteGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_groups_with_options_async(request, headers, runtime)

    def delete_groups_with_options(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteGroupsResponse().from_map(
            self.do_roarequest('DeleteGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/groups/delete', 'none', req, runtime)
        )

    async def delete_groups_with_options_async(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteGroupsResponse().from_map(
            await self.do_roarequest_async('DeleteGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/groups/delete', 'none', req, runtime)
        )

    def delete_person(
        self,
        request: green_20180509_models.DeletePersonRequest,
    ) -> green_20180509_models.DeletePersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_person_with_options(request, headers, runtime)

    async def delete_person_async(
        self,
        request: green_20180509_models.DeletePersonRequest,
    ) -> green_20180509_models.DeletePersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_person_with_options_async(request, headers, runtime)

    def delete_person_with_options(
        self,
        request: green_20180509_models.DeletePersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeletePersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeletePersonResponse().from_map(
            self.do_roarequest('DeletePerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/delete', 'none', req, runtime)
        )

    async def delete_person_with_options_async(
        self,
        request: green_20180509_models.DeletePersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeletePersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeletePersonResponse().from_map(
            await self.do_roarequest_async('DeletePerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/delete', 'none', req, runtime)
        )

    def delete_similarity_image(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_similarity_image_with_options(request, headers, runtime)

    async def delete_similarity_image_async(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_similarity_image_with_options_async(request, headers, runtime)

    def delete_similarity_image_with_options(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteSimilarityImageResponse().from_map(
            self.do_roarequest('DeleteSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/delete', 'none', req, runtime)
        )

    async def delete_similarity_image_with_options_async(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteSimilarityImageResponse().from_map(
            await self.do_roarequest_async('DeleteSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/delete', 'none', req, runtime)
        )

    def delete_similarity_library(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_similarity_library_with_options(request, headers, runtime)

    async def delete_similarity_library_async(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_similarity_library_with_options_async(request, headers, runtime)

    def delete_similarity_library_with_options(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteSimilarityLibraryResponse().from_map(
            self.do_roarequest('DeleteSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/delete', 'none', req, runtime)
        )

    async def delete_similarity_library_with_options_async(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteSimilarityLibraryResponse().from_map(
            await self.do_roarequest_async('DeleteSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/delete', 'none', req, runtime)
        )

    def delete_video_dna(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_video_dna_with_options(request, headers, runtime)

    async def delete_video_dna_async(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_video_dna_with_options_async(request, headers, runtime)

    def delete_video_dna_with_options(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteVideoDnaResponse().from_map(
            self.do_roarequest('DeleteVideoDna', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/delete', 'none', req, runtime)
        )

    async def delete_video_dna_with_options_async(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteVideoDnaResponse().from_map(
            await self.do_roarequest_async('DeleteVideoDna', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/delete', 'none', req, runtime)
        )

    def delete_video_dna_group(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_video_dna_group_with_options(request, headers, runtime)

    async def delete_video_dna_group_async(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_video_dna_group_with_options_async(request, headers, runtime)

    def delete_video_dna_group_with_options(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteVideoDnaGroupResponse().from_map(
            self.do_roarequest('DeleteVideoDnaGroup', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/group/delete', 'none', req, runtime)
        )

    async def delete_video_dna_group_with_options_async(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DeleteVideoDnaGroupResponse().from_map(
            await self.do_roarequest_async('DeleteVideoDnaGroup', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/group/delete', 'none', req, runtime)
        )

    def detect_face(
        self,
        request: green_20180509_models.DetectFaceRequest,
    ) -> green_20180509_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detect_face_with_options(request, headers, runtime)

    async def detect_face_async(
        self,
        request: green_20180509_models.DetectFaceRequest,
    ) -> green_20180509_models.DetectFaceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detect_face_with_options_async(request, headers, runtime)

    def detect_face_with_options(
        self,
        request: green_20180509_models.DetectFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DetectFaceResponse().from_map(
            self.do_roarequest('DetectFace', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/face/detect', 'none', req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: green_20180509_models.DetectFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DetectFaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.DetectFaceResponse().from_map(
            await self.do_roarequest_async('DetectFace', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/face/detect', 'none', req, runtime)
        )

    def file_async_scan(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
    ) -> green_20180509_models.FileAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_async_scan_with_options(request, headers, runtime)

    async def file_async_scan_async(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
    ) -> green_20180509_models.FileAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_async_scan_with_options_async(request, headers, runtime)

    def file_async_scan_with_options(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.FileAsyncScanResponse().from_map(
            self.do_roarequest('FileAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/file/asyncscan', 'none', req, runtime)
        )

    async def file_async_scan_with_options_async(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.FileAsyncScanResponse().from_map(
            await self.do_roarequest_async('FileAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/file/asyncscan', 'none', req, runtime)
        )

    def file_async_scan_results(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_async_scan_results_with_options(request, headers, runtime)

    async def file_async_scan_results_async(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_async_scan_results_with_options_async(request, headers, runtime)

    def file_async_scan_results_with_options(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.FileAsyncScanResultsResponse().from_map(
            self.do_roarequest('FileAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/file/results', 'none', req, runtime)
        )

    async def file_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.FileAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('FileAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/file/results', 'none', req, runtime)
        )

    def get_add_video_dna_results(
        self,
        request: green_20180509_models.GetAddVideoDnaResultsRequest,
    ) -> green_20180509_models.GetAddVideoDnaResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_add_video_dna_results_with_options(request, headers, runtime)

    async def get_add_video_dna_results_async(
        self,
        request: green_20180509_models.GetAddVideoDnaResultsRequest,
    ) -> green_20180509_models.GetAddVideoDnaResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_add_video_dna_results_with_options_async(request, headers, runtime)

    def get_add_video_dna_results_with_options(
        self,
        request: green_20180509_models.GetAddVideoDnaResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetAddVideoDnaResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetAddVideoDnaResultsResponse().from_map(
            self.do_roarequest('GetAddVideoDnaResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/add/results', 'none', req, runtime)
        )

    async def get_add_video_dna_results_with_options_async(
        self,
        request: green_20180509_models.GetAddVideoDnaResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetAddVideoDnaResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetAddVideoDnaResultsResponse().from_map(
            await self.do_roarequest_async('GetAddVideoDnaResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/dna/add/results', 'none', req, runtime)
        )

    def get_faces(
        self,
        request: green_20180509_models.GetFacesRequest,
    ) -> green_20180509_models.GetFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_faces_with_options(request, headers, runtime)

    async def get_faces_async(
        self,
        request: green_20180509_models.GetFacesRequest,
    ) -> green_20180509_models.GetFacesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_faces_with_options_async(request, headers, runtime)

    def get_faces_with_options(
        self,
        request: green_20180509_models.GetFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetFacesResponse().from_map(
            self.do_roarequest('GetFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/faces', 'json', req, runtime)
        )

    async def get_faces_with_options_async(
        self,
        request: green_20180509_models.GetFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetFacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetFacesResponse().from_map(
            await self.do_roarequest_async('GetFaces', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/faces', 'json', req, runtime)
        )

    def get_groups(
        self,
        request: green_20180509_models.GetGroupsRequest,
    ) -> green_20180509_models.GetGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_groups_with_options(request, headers, runtime)

    async def get_groups_async(
        self,
        request: green_20180509_models.GetGroupsRequest,
    ) -> green_20180509_models.GetGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_groups_with_options_async(request, headers, runtime)

    def get_groups_with_options(
        self,
        request: green_20180509_models.GetGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetGroupsResponse().from_map(
            self.do_roarequest('GetGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/groups', 'none', req, runtime)
        )

    async def get_groups_with_options_async(
        self,
        request: green_20180509_models.GetGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetGroupsResponse().from_map(
            await self.do_roarequest_async('GetGroups', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/groups', 'none', req, runtime)
        )

    def get_person(
        self,
        request: green_20180509_models.GetPersonRequest,
    ) -> green_20180509_models.GetPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_person_with_options(request, headers, runtime)

    async def get_person_async(
        self,
        request: green_20180509_models.GetPersonRequest,
    ) -> green_20180509_models.GetPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_person_with_options_async(request, headers, runtime)

    def get_person_with_options(
        self,
        request: green_20180509_models.GetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetPersonResponse().from_map(
            self.do_roarequest('GetPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person', 'none', req, runtime)
        )

    async def get_person_with_options_async(
        self,
        request: green_20180509_models.GetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetPersonResponse().from_map(
            await self.do_roarequest_async('GetPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person', 'none', req, runtime)
        )

    def get_persons(
        self,
        request: green_20180509_models.GetPersonsRequest,
    ) -> green_20180509_models.GetPersonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_persons_with_options(request, headers, runtime)

    async def get_persons_async(
        self,
        request: green_20180509_models.GetPersonsRequest,
    ) -> green_20180509_models.GetPersonsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_persons_with_options_async(request, headers, runtime)

    def get_persons_with_options(
        self,
        request: green_20180509_models.GetPersonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetPersonsResponse().from_map(
            self.do_roarequest('GetPersons', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/group/persons', 'none', req, runtime)
        )

    async def get_persons_with_options_async(
        self,
        request: green_20180509_models.GetPersonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetPersonsResponse().from_map(
            await self.do_roarequest_async('GetPersons', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/group/persons', 'none', req, runtime)
        )

    def get_similarity_image(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similarity_image_with_options(request, headers, runtime)

    async def get_similarity_image_async(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_similarity_image_with_options_async(request, headers, runtime)

    def get_similarity_image_with_options(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetSimilarityImageResponse().from_map(
            self.do_roarequest('GetSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/get', 'none', req, runtime)
        )

    async def get_similarity_image_with_options_async(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetSimilarityImageResponse().from_map(
            await self.do_roarequest_async('GetSimilarityImage', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/get', 'none', req, runtime)
        )

    def get_similarity_library(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similarity_library_with_options(request, headers, runtime)

    async def get_similarity_library_async(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_similarity_library_with_options_async(request, headers, runtime)

    def get_similarity_library_with_options(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetSimilarityLibraryResponse().from_map(
            self.do_roarequest('GetSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/get', 'none', req, runtime)
        )

    async def get_similarity_library_with_options_async(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.GetSimilarityLibraryResponse().from_map(
            await self.do_roarequest_async('GetSimilarityLibrary', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/get', 'none', req, runtime)
        )

    def image_async_manual_scan(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_manual_scan_with_options(request, headers, runtime)

    async def image_async_manual_scan_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_manual_scan_with_options_async(request, headers, runtime)

    def image_async_manual_scan_with_options(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncManualScanResponse().from_map(
            self.do_roarequest('ImageAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/manual/asyncScan', 'none', req, runtime)
        )

    async def image_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncManualScanResponse().from_map(
            await self.do_roarequest_async('ImageAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/manual/asyncScan', 'none', req, runtime)
        )

    def image_async_manual_scan_results(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_manual_scan_results_with_options(request, headers, runtime)

    async def image_async_manual_scan_results_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_manual_scan_results_with_options_async(request, headers, runtime)

    def image_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncManualScanResultsResponse().from_map(
            self.do_roarequest('ImageAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/manual/scan/results', 'none', req, runtime)
        )

    async def image_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncManualScanResultsResponse().from_map(
            await self.do_roarequest_async('ImageAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/manual/scan/results', 'none', req, runtime)
        )

    def image_async_scan(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_scan_with_options(request, headers, runtime)

    async def image_async_scan_async(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_scan_with_options_async(request, headers, runtime)

    def image_async_scan_with_options(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncScanResponse().from_map(
            self.do_roarequest('ImageAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/asyncscan', 'none', req, runtime)
        )

    async def image_async_scan_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncScanResponse().from_map(
            await self.do_roarequest_async('ImageAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/asyncscan', 'none', req, runtime)
        )

    def image_async_scan_results(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_scan_results_with_options(request, headers, runtime)

    async def image_async_scan_results_async(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_scan_results_with_options_async(request, headers, runtime)

    def image_async_scan_results_with_options(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncScanResultsResponse().from_map(
            self.do_roarequest('ImageAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/results', 'none', req, runtime)
        )

    async def image_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('ImageAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/results', 'none', req, runtime)
        )

    def image_scan_feedback(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_scan_feedback_with_options(request, headers, runtime)

    async def image_scan_feedback_async(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_scan_feedback_with_options_async(request, headers, runtime)

    def image_scan_feedback_with_options(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageScanFeedbackResponse().from_map(
            self.do_roarequest('ImageScanFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/feedback', 'none', req, runtime)
        )

    async def image_scan_feedback_with_options_async(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageScanFeedbackResponse().from_map(
            await self.do_roarequest_async('ImageScanFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/feedback', 'none', req, runtime)
        )

    def image_sync_scan(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
    ) -> green_20180509_models.ImageSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_sync_scan_with_options(request, headers, runtime)

    async def image_sync_scan_async(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
    ) -> green_20180509_models.ImageSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_sync_scan_with_options_async(request, headers, runtime)

    def image_sync_scan_with_options(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageSyncScanResponse().from_map(
            self.do_roarequest('ImageSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/scan', 'none', req, runtime)
        )

    async def image_sync_scan_with_options_async(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ImageSyncScanResponse().from_map(
            await self.do_roarequest_async('ImageSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/image/scan', 'none', req, runtime)
        )

    def list_similarity_images(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_similarity_images_with_options(request, headers, runtime)

    async def list_similarity_images_async(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_similarity_images_with_options_async(request, headers, runtime)

    def list_similarity_images_with_options(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ListSimilarityImagesResponse().from_map(
            self.do_roarequest('ListSimilarityImages', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/list', 'none', req, runtime)
        )

    async def list_similarity_images_with_options_async(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ListSimilarityImagesResponse().from_map(
            await self.do_roarequest_async('ListSimilarityImages', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/image/list', 'none', req, runtime)
        )

    def list_similarity_libraries(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_similarity_libraries_with_options(request, headers, runtime)

    async def list_similarity_libraries_async(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_similarity_libraries_with_options_async(request, headers, runtime)

    def list_similarity_libraries_with_options(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ListSimilarityLibrariesResponse().from_map(
            self.do_roarequest('ListSimilarityLibraries', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/list', 'none', req, runtime)
        )

    async def list_similarity_libraries_with_options_async(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.ListSimilarityLibrariesResponse().from_map(
            await self.do_roarequest_async('ListSimilarityLibraries', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/similarity/library/list', 'none', req, runtime)
        )

    def live_stream_async_scan(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_async_scan_with_options(request, headers, runtime)

    async def live_stream_async_scan_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_async_scan_with_options_async(request, headers, runtime)

    def live_stream_async_scan_with_options(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamAsyncScanResponse().from_map(
            self.do_roarequest('LiveStreamAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/asyncscan', 'none', req, runtime)
        )

    async def live_stream_async_scan_with_options_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamAsyncScanResponse().from_map(
            await self.do_roarequest_async('LiveStreamAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/asyncscan', 'none', req, runtime)
        )

    def live_stream_async_scan_results(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_async_scan_results_with_options(request, headers, runtime)

    async def live_stream_async_scan_results_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_async_scan_results_with_options_async(request, headers, runtime)

    def live_stream_async_scan_results_with_options(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamAsyncScanResultsResponse().from_map(
            self.do_roarequest('LiveStreamAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/results', 'none', req, runtime)
        )

    async def live_stream_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('LiveStreamAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/results', 'none', req, runtime)
        )

    def live_stream_cancel_scan(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_cancel_scan_with_options(request, headers, runtime)

    async def live_stream_cancel_scan_async(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_cancel_scan_with_options_async(request, headers, runtime)

    def live_stream_cancel_scan_with_options(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamCancelScanResponse().from_map(
            self.do_roarequest('LiveStreamCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/cancelscan', 'none', req, runtime)
        )

    async def live_stream_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.LiveStreamCancelScanResponse().from_map(
            await self.do_roarequest_async('LiveStreamCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/livestream/cancelscan', 'none', req, runtime)
        )

    def search_person(
        self,
        request: green_20180509_models.SearchPersonRequest,
    ) -> green_20180509_models.SearchPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_person_with_options(request, headers, runtime)

    async def search_person_async(
        self,
        request: green_20180509_models.SearchPersonRequest,
    ) -> green_20180509_models.SearchPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_person_with_options_async(request, headers, runtime)

    def search_person_with_options(
        self,
        request: green_20180509_models.SearchPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SearchPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.SearchPersonResponse().from_map(
            self.do_roarequest('SearchPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/search', 'none', req, runtime)
        )

    async def search_person_with_options_async(
        self,
        request: green_20180509_models.SearchPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SearchPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.SearchPersonResponse().from_map(
            await self.do_roarequest_async('SearchPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/search', 'none', req, runtime)
        )

    def set_person(
        self,
        request: green_20180509_models.SetPersonRequest,
    ) -> green_20180509_models.SetPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_person_with_options(request, headers, runtime)

    async def set_person_async(
        self,
        request: green_20180509_models.SetPersonRequest,
    ) -> green_20180509_models.SetPersonResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_person_with_options_async(request, headers, runtime)

    def set_person_with_options(
        self,
        request: green_20180509_models.SetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SetPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.SetPersonResponse().from_map(
            self.do_roarequest('SetPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/update', 'none', req, runtime)
        )

    async def set_person_with_options_async(
        self,
        request: green_20180509_models.SetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SetPersonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.SetPersonResponse().from_map(
            await self.do_roarequest_async('SetPerson', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/sface/person/update', 'none', req, runtime)
        )

    def text_async_manual_scan(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_async_manual_scan_with_options(request, headers, runtime)

    async def text_async_manual_scan_async(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_async_manual_scan_with_options_async(request, headers, runtime)

    def text_async_manual_scan_with_options(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextAsyncManualScanResponse().from_map(
            self.do_roarequest('TextAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/manual/asyncScan', 'none', req, runtime)
        )

    async def text_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextAsyncManualScanResponse().from_map(
            await self.do_roarequest_async('TextAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/manual/asyncScan', 'none', req, runtime)
        )

    def text_async_manual_scan_results(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_async_manual_scan_results_with_options(request, headers, runtime)

    async def text_async_manual_scan_results_async(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_async_manual_scan_results_with_options_async(request, headers, runtime)

    def text_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextAsyncManualScanResultsResponse().from_map(
            self.do_roarequest('TextAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/manual/scan/results', 'none', req, runtime)
        )

    async def text_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextAsyncManualScanResultsResponse().from_map(
            await self.do_roarequest_async('TextAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/manual/scan/results', 'none', req, runtime)
        )

    def text_feedback(
        self,
        request: green_20180509_models.TextFeedbackRequest,
    ) -> green_20180509_models.TextFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_feedback_with_options(request, headers, runtime)

    async def text_feedback_async(
        self,
        request: green_20180509_models.TextFeedbackRequest,
    ) -> green_20180509_models.TextFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_feedback_with_options_async(request, headers, runtime)

    def text_feedback_with_options(
        self,
        request: green_20180509_models.TextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextFeedbackResponse().from_map(
            self.do_roarequest('TextFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/feedback', 'none', req, runtime)
        )

    async def text_feedback_with_options_async(
        self,
        request: green_20180509_models.TextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextFeedbackResponse().from_map(
            await self.do_roarequest_async('TextFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/feedback', 'none', req, runtime)
        )

    def text_scan(
        self,
        request: green_20180509_models.TextScanRequest,
    ) -> green_20180509_models.TextScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_scan_with_options(request, headers, runtime)

    async def text_scan_async(
        self,
        request: green_20180509_models.TextScanRequest,
    ) -> green_20180509_models.TextScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_scan_with_options_async(request, headers, runtime)

    def text_scan_with_options(
        self,
        request: green_20180509_models.TextScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextScanResponse().from_map(
            self.do_roarequest('TextScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/scan', 'none', req, runtime)
        )

    async def text_scan_with_options_async(
        self,
        request: green_20180509_models.TextScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.TextScanResponse().from_map(
            await self.do_roarequest_async('TextScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/text/scan', 'none', req, runtime)
        )

    def upload_credentials(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
    ) -> green_20180509_models.UploadCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_credentials_with_options(request, headers, runtime)

    async def upload_credentials_async(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
    ) -> green_20180509_models.UploadCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_credentials_with_options_async(request, headers, runtime)

    def upload_credentials_with_options(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.UploadCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.UploadCredentialsResponse().from_map(
            self.do_roarequest('UploadCredentials', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/credentials/uploadcredentials', 'none', req, runtime)
        )

    async def upload_credentials_with_options_async(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.UploadCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.UploadCredentialsResponse().from_map(
            await self.do_roarequest_async('UploadCredentials', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/credentials/uploadcredentials', 'none', req, runtime)
        )

    def video_async_manual_scan(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_manual_scan_with_options(request, headers, runtime)

    async def video_async_manual_scan_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_manual_scan_with_options_async(request, headers, runtime)

    def video_async_manual_scan_with_options(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncManualScanResponse().from_map(
            self.do_roarequest('VideoAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/manual/asyncScan', 'none', req, runtime)
        )

    async def video_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncManualScanResponse().from_map(
            await self.do_roarequest_async('VideoAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/manual/asyncScan', 'none', req, runtime)
        )

    def video_async_manual_scan_results(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_manual_scan_results_with_options(request, headers, runtime)

    async def video_async_manual_scan_results_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_manual_scan_results_with_options_async(request, headers, runtime)

    def video_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncManualScanResultsResponse().from_map(
            self.do_roarequest('VideoAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/manual/scan/results', 'none', req, runtime)
        )

    async def video_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncManualScanResultsResponse().from_map(
            await self.do_roarequest_async('VideoAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/manual/scan/results', 'none', req, runtime)
        )

    def video_async_scan(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_scan_with_options(request, headers, runtime)

    async def video_async_scan_async(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_scan_with_options_async(request, headers, runtime)

    def video_async_scan_with_options(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncScanResponse().from_map(
            self.do_roarequest('VideoAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/asyncscan', 'none', req, runtime)
        )

    async def video_async_scan_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncScanResponse().from_map(
            await self.do_roarequest_async('VideoAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/asyncscan', 'none', req, runtime)
        )

    def video_async_scan_results(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_scan_results_with_options(request, headers, runtime)

    async def video_async_scan_results_async(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_scan_results_with_options_async(request, headers, runtime)

    def video_async_scan_results_with_options(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncScanResultsResponse().from_map(
            self.do_roarequest('VideoAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/results', 'none', req, runtime)
        )

    async def video_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('VideoAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/results', 'none', req, runtime)
        )

    def video_cancel_scan(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
    ) -> green_20180509_models.VideoCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_cancel_scan_with_options(request, headers, runtime)

    async def video_cancel_scan_async(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
    ) -> green_20180509_models.VideoCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_cancel_scan_with_options_async(request, headers, runtime)

    def video_cancel_scan_with_options(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoCancelScanResponse().from_map(
            self.do_roarequest('VideoCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/cancelscan', 'none', req, runtime)
        )

    async def video_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoCancelScanResponse().from_map(
            await self.do_roarequest_async('VideoCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/cancelscan', 'none', req, runtime)
        )

    def video_feedback(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
    ) -> green_20180509_models.VideoFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_feedback_with_options(request, headers, runtime)

    async def video_feedback_async(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
    ) -> green_20180509_models.VideoFeedbackResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_feedback_with_options_async(request, headers, runtime)

    def video_feedback_with_options(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoFeedbackResponse().from_map(
            self.do_roarequest('VideoFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/feedback', 'none', req, runtime)
        )

    async def video_feedback_with_options_async(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoFeedbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoFeedbackResponse().from_map(
            await self.do_roarequest_async('VideoFeedback', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/feedback', 'none', req, runtime)
        )

    def video_sync_scan(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
    ) -> green_20180509_models.VideoSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_sync_scan_with_options(request, headers, runtime)

    async def video_sync_scan_async(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
    ) -> green_20180509_models.VideoSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_sync_scan_with_options_async(request, headers, runtime)

    def video_sync_scan_with_options(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoSyncScanResponse().from_map(
            self.do_roarequest('VideoSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/syncscan', 'none', req, runtime)
        )

    async def video_sync_scan_with_options_async(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VideoSyncScanResponse().from_map(
            await self.do_roarequest_async('VideoSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/video/syncscan', 'none', req, runtime)
        )

    def vod_async_scan(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
    ) -> green_20180509_models.VodAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.vod_async_scan_with_options(request, headers, runtime)

    async def vod_async_scan_async(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
    ) -> green_20180509_models.VodAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.vod_async_scan_with_options_async(request, headers, runtime)

    def vod_async_scan_with_options(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VodAsyncScanResponse().from_map(
            self.do_roarequest('VodAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/vod/asyncscan', 'none', req, runtime)
        )

    async def vod_async_scan_with_options_async(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VodAsyncScanResponse().from_map(
            await self.do_roarequest_async('VodAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/vod/asyncscan', 'none', req, runtime)
        )

    def vod_async_scan_results(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.vod_async_scan_results_with_options(request, headers, runtime)

    async def vod_async_scan_results_async(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.vod_async_scan_results_with_options_async(request, headers, runtime)

    def vod_async_scan_results_with_options(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VodAsyncScanResultsResponse().from_map(
            self.do_roarequest('VodAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/vod/results', 'none', req, runtime)
        )

    async def vod_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VodAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('VodAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/vod/results', 'none', req, runtime)
        )

    def voice_async_manual_scan(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_manual_scan_with_options(request, headers, runtime)

    async def voice_async_manual_scan_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_manual_scan_with_options_async(request, headers, runtime)

    def voice_async_manual_scan_with_options(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncManualScanResponse().from_map(
            self.do_roarequest('VoiceAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/manual/asyncScan', 'none', req, runtime)
        )

    async def voice_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncManualScanResponse().from_map(
            await self.do_roarequest_async('VoiceAsyncManualScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/manual/asyncScan', 'none', req, runtime)
        )

    def voice_async_manual_scan_results(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_manual_scan_results_with_options(request, headers, runtime)

    async def voice_async_manual_scan_results_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_manual_scan_results_with_options_async(request, headers, runtime)

    def voice_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncManualScanResultsResponse().from_map(
            self.do_roarequest('VoiceAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/manual/scan/results', 'none', req, runtime)
        )

    async def voice_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncManualScanResultsResponse().from_map(
            await self.do_roarequest_async('VoiceAsyncManualScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/manual/scan/results', 'none', req, runtime)
        )

    def voice_async_scan(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_scan_with_options(request, headers, runtime)

    async def voice_async_scan_async(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_scan_with_options_async(request, headers, runtime)

    def voice_async_scan_with_options(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncScanResponse().from_map(
            self.do_roarequest('VoiceAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/asyncscan', 'none', req, runtime)
        )

    async def voice_async_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncScanResponse().from_map(
            await self.do_roarequest_async('VoiceAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/asyncscan', 'none', req, runtime)
        )

    def voice_async_scan_results(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_scan_results_with_options(request, headers, runtime)

    async def voice_async_scan_results_async(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_scan_results_with_options_async(request, headers, runtime)

    def voice_async_scan_results_with_options(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncScanResultsResponse().from_map(
            self.do_roarequest('VoiceAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/results', 'none', req, runtime)
        )

    async def voice_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('VoiceAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/results', 'none', req, runtime)
        )

    def voice_cancel_scan(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_cancel_scan_with_options(request, headers, runtime)

    async def voice_cancel_scan_async(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_cancel_scan_with_options_async(request, headers, runtime)

    def voice_cancel_scan_with_options(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceCancelScanResponse().from_map(
            self.do_roarequest('VoiceCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/cancelscan', 'none', req, runtime)
        )

    async def voice_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceCancelScanResponse().from_map(
            await self.do_roarequest_async('VoiceCancelScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/cancelscan', 'none', req, runtime)
        )

    def voice_identity_check(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_check_with_options(request, headers, runtime)

    async def voice_identity_check_async(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_check_with_options_async(request, headers, runtime)

    def voice_identity_check_with_options(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityCheckResponse().from_map(
            self.do_roarequest('VoiceIdentityCheck', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/check', 'none', req, runtime)
        )

    async def voice_identity_check_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityCheckResponse().from_map(
            await self.do_roarequest_async('VoiceIdentityCheck', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/check', 'none', req, runtime)
        )

    def voice_identity_register(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_register_with_options(request, headers, runtime)

    async def voice_identity_register_async(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_register_with_options_async(request, headers, runtime)

    def voice_identity_register_with_options(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityRegisterResponse().from_map(
            self.do_roarequest('VoiceIdentityRegister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/register', 'none', req, runtime)
        )

    async def voice_identity_register_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityRegisterResponse().from_map(
            await self.do_roarequest_async('VoiceIdentityRegister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/register', 'none', req, runtime)
        )

    def voice_identity_start_check(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_start_check_with_options(request, headers, runtime)

    async def voice_identity_start_check_async(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_start_check_with_options_async(request, headers, runtime)

    def voice_identity_start_check_with_options(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityStartCheckResponse().from_map(
            self.do_roarequest('VoiceIdentityStartCheck', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/start/check', 'none', req, runtime)
        )

    async def voice_identity_start_check_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityStartCheckResponse().from_map(
            await self.do_roarequest_async('VoiceIdentityStartCheck', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/start/check', 'none', req, runtime)
        )

    def voice_identity_start_register(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_start_register_with_options(request, headers, runtime)

    async def voice_identity_start_register_async(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_start_register_with_options_async(request, headers, runtime)

    def voice_identity_start_register_with_options(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityStartRegisterResponse().from_map(
            self.do_roarequest('VoiceIdentityStartRegister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/start/register', 'none', req, runtime)
        )

    async def voice_identity_start_register_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityStartRegisterResponse().from_map(
            await self.do_roarequest_async('VoiceIdentityStartRegister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/start/register', 'none', req, runtime)
        )

    def voice_identity_unregister(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_unregister_with_options(request, headers, runtime)

    async def voice_identity_unregister_async(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_unregister_with_options_async(request, headers, runtime)

    def voice_identity_unregister_with_options(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityUnregisterResponse().from_map(
            self.do_roarequest('VoiceIdentityUnregister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/unregister', 'none', req, runtime)
        )

    async def voice_identity_unregister_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceIdentityUnregisterResponse().from_map(
            await self.do_roarequest_async('VoiceIdentityUnregister', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/auth/unregister', 'none', req, runtime)
        )

    def voice_sync_scan(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_sync_scan_with_options(request, headers, runtime)

    async def voice_sync_scan_async(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_sync_scan_with_options_async(request, headers, runtime)

    def voice_sync_scan_with_options(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceSyncScanResponse().from_map(
            self.do_roarequest('VoiceSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/syncscan', 'none', req, runtime)
        )

    async def voice_sync_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.VoiceSyncScanResponse().from_map(
            await self.do_roarequest_async('VoiceSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/voice/syncscan', 'none', req, runtime)
        )

    def webpage_async_scan(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_async_scan_with_options(request, headers, runtime)

    async def webpage_async_scan_async(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_async_scan_with_options_async(request, headers, runtime)

    def webpage_async_scan_with_options(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageAsyncScanResponse().from_map(
            self.do_roarequest('WebpageAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/asyncscan', 'none', req, runtime)
        )

    async def webpage_async_scan_with_options_async(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageAsyncScanResponse().from_map(
            await self.do_roarequest_async('WebpageAsyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/asyncscan', 'none', req, runtime)
        )

    def webpage_async_scan_results(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_async_scan_results_with_options(request, headers, runtime)

    async def webpage_async_scan_results_async(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_async_scan_results_with_options_async(request, headers, runtime)

    def webpage_async_scan_results_with_options(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageAsyncScanResultsResponse().from_map(
            self.do_roarequest('WebpageAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/results', 'none', req, runtime)
        )

    async def webpage_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageAsyncScanResultsResponse().from_map(
            await self.do_roarequest_async('WebpageAsyncScanResults', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/results', 'none', req, runtime)
        )

    def webpage_sync_scan(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_sync_scan_with_options(request, headers, runtime)

    async def webpage_sync_scan_async(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_sync_scan_with_options_async(request, headers, runtime)

    def webpage_sync_scan_with_options(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageSyncScanResponse().from_map(
            self.do_roarequest('WebpageSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/scan', 'none', req, runtime)
        )

    async def webpage_sync_scan_with_options_async(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return green_20180509_models.WebpageSyncScanResponse().from_map(
            await self.do_roarequest_async('WebpageSyncScan', '2018-05-09', 'HTTPS', 'POST', 'AK', f'/green/webpage/scan', 'none', req, runtime)
        )
