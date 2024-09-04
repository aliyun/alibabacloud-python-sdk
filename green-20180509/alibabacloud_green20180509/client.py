# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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

    def add_faces_with_options(
        self,
        request: green_20180509_models.AddFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddFacesResponse:
        """
        @summary 添加人脸
        
        @param request: AddFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/face/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_faces_with_options_async(
        self,
        request: green_20180509_models.AddFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddFacesResponse:
        """
        @summary 添加人脸
        
        @param request: AddFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/face/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_faces(
        self,
        request: green_20180509_models.AddFacesRequest,
    ) -> green_20180509_models.AddFacesResponse:
        """
        @summary 添加人脸
        
        @param request: AddFacesRequest
        @return: AddFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_faces_with_options(request, headers, runtime)

    async def add_faces_async(
        self,
        request: green_20180509_models.AddFacesRequest,
    ) -> green_20180509_models.AddFacesResponse:
        """
        @summary 添加人脸
        
        @param request: AddFacesRequest
        @return: AddFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_faces_with_options_async(request, headers, runtime)

    def add_groups_with_options(
        self,
        request: green_20180509_models.AddGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddGroupsResponse:
        """
        @summary 添加分组
        
        @param request: AddGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/groups/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_groups_with_options_async(
        self,
        request: green_20180509_models.AddGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddGroupsResponse:
        """
        @summary 添加分组
        
        @param request: AddGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/groups/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_groups(
        self,
        request: green_20180509_models.AddGroupsRequest,
    ) -> green_20180509_models.AddGroupsResponse:
        """
        @summary 添加分组
        
        @param request: AddGroupsRequest
        @return: AddGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_groups_with_options(request, headers, runtime)

    async def add_groups_async(
        self,
        request: green_20180509_models.AddGroupsRequest,
    ) -> green_20180509_models.AddGroupsResponse:
        """
        @summary 添加分组
        
        @param request: AddGroupsRequest
        @return: AddGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_groups_with_options_async(request, headers, runtime)

    def add_person_with_options(
        self,
        request: green_20180509_models.AddPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddPersonResponse:
        """
        @summary 添加个体
        
        @param request: AddPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_person_with_options_async(
        self,
        request: green_20180509_models.AddPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddPersonResponse:
        """
        @summary 添加个体
        
        @param request: AddPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddPersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_person(
        self,
        request: green_20180509_models.AddPersonRequest,
    ) -> green_20180509_models.AddPersonResponse:
        """
        @summary 添加个体
        
        @param request: AddPersonRequest
        @return: AddPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_person_with_options(request, headers, runtime)

    async def add_person_async(
        self,
        request: green_20180509_models.AddPersonRequest,
    ) -> green_20180509_models.AddPersonResponse:
        """
        @summary 添加个体
        
        @param request: AddPersonRequest
        @return: AddPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_person_with_options_async(request, headers, runtime)

    def add_similarity_image_with_options(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        """
        @summary 添加相似图
        
        @param request: AddSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddSimilarityImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_similarity_image_with_options_async(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        """
        @summary 添加相似图
        
        @param request: AddSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddSimilarityImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_similarity_image(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        """
        @summary 添加相似图
        
        @param request: AddSimilarityImageRequest
        @return: AddSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_similarity_image_with_options(request, headers, runtime)

    async def add_similarity_image_async(
        self,
        request: green_20180509_models.AddSimilarityImageRequest,
    ) -> green_20180509_models.AddSimilarityImageResponse:
        """
        @summary 添加相似图
        
        @param request: AddSimilarityImageRequest
        @return: AddSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_similarity_image_with_options_async(request, headers, runtime)

    def add_similarity_library_with_options(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        """
        @summary 添加相似图库
        
        @param request: AddSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddSimilarityLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_similarity_library_with_options_async(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        """
        @summary 添加相似图库
        
        @param request: AddSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddSimilarityLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_similarity_library(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        """
        @summary 添加相似图库
        
        @param request: AddSimilarityLibraryRequest
        @return: AddSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_similarity_library_with_options(request, headers, runtime)

    async def add_similarity_library_async(
        self,
        request: green_20180509_models.AddSimilarityLibraryRequest,
    ) -> green_20180509_models.AddSimilarityLibraryResponse:
        """
        @summary 添加相似图库
        
        @param request: AddSimilarityLibraryRequest
        @return: AddSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_similarity_library_with_options_async(request, headers, runtime)

    def add_video_dna_with_options(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaResponse:
        """
        @summary 添加视频Dna
        
        @param request: AddVideoDnaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVideoDnaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVideoDna',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddVideoDnaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_video_dna_with_options_async(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaResponse:
        """
        @summary 添加视频Dna
        
        @param request: AddVideoDnaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVideoDnaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVideoDna',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddVideoDnaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_video_dna(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
    ) -> green_20180509_models.AddVideoDnaResponse:
        """
        @summary 添加视频Dna
        
        @param request: AddVideoDnaRequest
        @return: AddVideoDnaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_video_dna_with_options(request, headers, runtime)

    async def add_video_dna_async(
        self,
        request: green_20180509_models.AddVideoDnaRequest,
    ) -> green_20180509_models.AddVideoDnaResponse:
        """
        @summary 添加视频Dna
        
        @param request: AddVideoDnaRequest
        @return: AddVideoDnaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_video_dna_with_options_async(request, headers, runtime)

    def add_video_dna_group_with_options(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        """
        @summary 添加视频Dna分组
        
        @param request: AddVideoDnaGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVideoDnaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVideoDnaGroup',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/group/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddVideoDnaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_video_dna_group_with_options_async(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        """
        @summary 添加视频Dna分组
        
        @param request: AddVideoDnaGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddVideoDnaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVideoDnaGroup',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/group/add',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.AddVideoDnaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_video_dna_group(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        """
        @summary 添加视频Dna分组
        
        @param request: AddVideoDnaGroupRequest
        @return: AddVideoDnaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_video_dna_group_with_options(request, headers, runtime)

    async def add_video_dna_group_async(
        self,
        request: green_20180509_models.AddVideoDnaGroupRequest,
    ) -> green_20180509_models.AddVideoDnaGroupResponse:
        """
        @summary 添加视频Dna分组
        
        @param request: AddVideoDnaGroupRequest
        @return: AddVideoDnaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_video_dna_group_with_options_async(request, headers, runtime)

    def delete_faces_with_options(
        self,
        request: green_20180509_models.DeleteFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteFacesResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/face/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_faces_with_options_async(
        self,
        request: green_20180509_models.DeleteFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteFacesResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/face/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_faces(
        self,
        request: green_20180509_models.DeleteFacesRequest,
    ) -> green_20180509_models.DeleteFacesResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFacesRequest
        @return: DeleteFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_faces_with_options(request, headers, runtime)

    async def delete_faces_async(
        self,
        request: green_20180509_models.DeleteFacesRequest,
    ) -> green_20180509_models.DeleteFacesResponse:
        """
        @summary 删除人脸
        
        @param request: DeleteFacesRequest
        @return: DeleteFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_faces_with_options_async(request, headers, runtime)

    def delete_groups_with_options(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteGroupsResponse:
        """
        @summary 删除分组
        
        @param request: DeleteGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/groups/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_groups_with_options_async(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteGroupsResponse:
        """
        @summary 删除分组
        
        @param request: DeleteGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/groups/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_groups(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
    ) -> green_20180509_models.DeleteGroupsResponse:
        """
        @summary 删除分组
        
        @param request: DeleteGroupsRequest
        @return: DeleteGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_groups_with_options(request, headers, runtime)

    async def delete_groups_async(
        self,
        request: green_20180509_models.DeleteGroupsRequest,
    ) -> green_20180509_models.DeleteGroupsResponse:
        """
        @summary 删除分组
        
        @param request: DeleteGroupsRequest
        @return: DeleteGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_groups_with_options_async(request, headers, runtime)

    def delete_person_with_options(
        self,
        request: green_20180509_models.DeletePersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeletePersonResponse:
        """
        @summary 删除个体
        
        @param request: DeletePersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeletePersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_person_with_options_async(
        self,
        request: green_20180509_models.DeletePersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeletePersonResponse:
        """
        @summary 删除个体
        
        @param request: DeletePersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeletePersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_person(
        self,
        request: green_20180509_models.DeletePersonRequest,
    ) -> green_20180509_models.DeletePersonResponse:
        """
        @summary 删除个体
        
        @param request: DeletePersonRequest
        @return: DeletePersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_person_with_options(request, headers, runtime)

    async def delete_person_async(
        self,
        request: green_20180509_models.DeletePersonRequest,
    ) -> green_20180509_models.DeletePersonResponse:
        """
        @summary 删除个体
        
        @param request: DeletePersonRequest
        @return: DeletePersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_person_with_options_async(request, headers, runtime)

    def delete_similarity_image_with_options(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        """
        @summary 删除相似图
        
        @param request: DeleteSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteSimilarityImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_similarity_image_with_options_async(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        """
        @summary 删除相似图
        
        @param request: DeleteSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteSimilarityImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_similarity_image(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        """
        @summary 删除相似图
        
        @param request: DeleteSimilarityImageRequest
        @return: DeleteSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_similarity_image_with_options(request, headers, runtime)

    async def delete_similarity_image_async(
        self,
        request: green_20180509_models.DeleteSimilarityImageRequest,
    ) -> green_20180509_models.DeleteSimilarityImageResponse:
        """
        @summary 删除相似图
        
        @param request: DeleteSimilarityImageRequest
        @return: DeleteSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_similarity_image_with_options_async(request, headers, runtime)

    def delete_similarity_library_with_options(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        """
        @summary 删除相似图库
        
        @param request: DeleteSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteSimilarityLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_similarity_library_with_options_async(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        """
        @summary 删除相似图库
        
        @param request: DeleteSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteSimilarityLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_similarity_library(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        """
        @summary 删除相似图库
        
        @param request: DeleteSimilarityLibraryRequest
        @return: DeleteSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_similarity_library_with_options(request, headers, runtime)

    async def delete_similarity_library_async(
        self,
        request: green_20180509_models.DeleteSimilarityLibraryRequest,
    ) -> green_20180509_models.DeleteSimilarityLibraryResponse:
        """
        @summary 删除相似图库
        
        @param request: DeleteSimilarityLibraryRequest
        @return: DeleteSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_similarity_library_with_options_async(request, headers, runtime)

    def delete_video_dna_with_options(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        """
        @summary 删除视频Dna
        
        @param request: DeleteVideoDnaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVideoDnaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoDna',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteVideoDnaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_video_dna_with_options_async(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        """
        @summary 删除视频Dna
        
        @param request: DeleteVideoDnaRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVideoDnaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoDna',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteVideoDnaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_video_dna(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        """
        @summary 删除视频Dna
        
        @param request: DeleteVideoDnaRequest
        @return: DeleteVideoDnaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_video_dna_with_options(request, headers, runtime)

    async def delete_video_dna_async(
        self,
        request: green_20180509_models.DeleteVideoDnaRequest,
    ) -> green_20180509_models.DeleteVideoDnaResponse:
        """
        @summary 删除视频Dna
        
        @param request: DeleteVideoDnaRequest
        @return: DeleteVideoDnaResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_video_dna_with_options_async(request, headers, runtime)

    def delete_video_dna_group_with_options(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        """
        @summary 删除视频Dna分组
        
        @param request: DeleteVideoDnaGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVideoDnaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoDnaGroup',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteVideoDnaGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_video_dna_group_with_options_async(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        """
        @summary 删除视频Dna分组
        
        @param request: DeleteVideoDnaGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVideoDnaGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVideoDnaGroup',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/dna/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DeleteVideoDnaGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_video_dna_group(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        """
        @summary 删除视频Dna分组
        
        @param request: DeleteVideoDnaGroupRequest
        @return: DeleteVideoDnaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_video_dna_group_with_options(request, headers, runtime)

    async def delete_video_dna_group_async(
        self,
        request: green_20180509_models.DeleteVideoDnaGroupRequest,
    ) -> green_20180509_models.DeleteVideoDnaGroupResponse:
        """
        @summary 删除视频Dna分组
        
        @param request: DeleteVideoDnaGroupRequest
        @return: DeleteVideoDnaGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_video_dna_group_with_options_async(request, headers, runtime)

    def detect_face_with_options(
        self,
        request: green_20180509_models.DetectFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DetectFaceResponse:
        """
        @summary 人脸属性检测
        
        @param request: DetectFaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectFace',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/face/detect',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DetectFaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_face_with_options_async(
        self,
        request: green_20180509_models.DetectFaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.DetectFaceResponse:
        """
        @summary 人脸属性检测
        
        @param request: DetectFaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectFaceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectFace',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/face/detect',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.DetectFaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_face(
        self,
        request: green_20180509_models.DetectFaceRequest,
    ) -> green_20180509_models.DetectFaceResponse:
        """
        @summary 人脸属性检测
        
        @param request: DetectFaceRequest
        @return: DetectFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.detect_face_with_options(request, headers, runtime)

    async def detect_face_async(
        self,
        request: green_20180509_models.DetectFaceRequest,
    ) -> green_20180509_models.DetectFaceResponse:
        """
        @summary 人脸属性检测
        
        @param request: DetectFaceRequest
        @return: DetectFaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.detect_face_with_options_async(request, headers, runtime)

    def file_async_scan_with_options(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResponse:
        """
        @summary 文件异步检测
        
        @param request: FileAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FileAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_async_scan_with_options_async(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResponse:
        """
        @summary 文件异步检测
        
        @param request: FileAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FileAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_async_scan(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
    ) -> green_20180509_models.FileAsyncScanResponse:
        """
        @summary 文件异步检测
        
        @param request: FileAsyncScanRequest
        @return: FileAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_async_scan_with_options(request, headers, runtime)

    async def file_async_scan_async(
        self,
        request: green_20180509_models.FileAsyncScanRequest,
    ) -> green_20180509_models.FileAsyncScanResponse:
        """
        @summary 文件异步检测
        
        @param request: FileAsyncScanRequest
        @return: FileAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_async_scan_with_options_async(request, headers, runtime)

    def file_async_scan_results_with_options(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        """
        @summary 文件异步检测结果
        
        @param request: FileAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FileAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def file_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        """
        @summary 文件异步检测结果
        
        @param request: FileAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FileAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def file_async_scan_results(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        """
        @summary 文件异步检测结果
        
        @param request: FileAsyncScanResultsRequest
        @return: FileAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_async_scan_results_with_options(request, headers, runtime)

    async def file_async_scan_results_async(
        self,
        request: green_20180509_models.FileAsyncScanResultsRequest,
    ) -> green_20180509_models.FileAsyncScanResultsResponse:
        """
        @summary 文件异步检测结果
        
        @param request: FileAsyncScanResultsRequest
        @return: FileAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_async_scan_results_with_options_async(request, headers, runtime)

    def file_async_scan_v2with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanV2Response:
        """
        @summary 文件检测新版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanV2Response
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FileAsyncScanV2',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/asyncscanv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanV2Response(),
            self.call_api(params, req, runtime)
        )

    async def file_async_scan_v2with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.FileAsyncScanV2Response:
        """
        @summary 文件检测新版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: FileAsyncScanV2Response
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='FileAsyncScanV2',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/file/asyncscanv2',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.FileAsyncScanV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def file_async_scan_v2(self) -> green_20180509_models.FileAsyncScanV2Response:
        """
        @summary 文件检测新版本
        
        @return: FileAsyncScanV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.file_async_scan_v2with_options(headers, runtime)

    async def file_async_scan_v2_async(self) -> green_20180509_models.FileAsyncScanV2Response:
        """
        @summary 文件检测新版本
        
        @return: FileAsyncScanV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.file_async_scan_v2with_options_async(headers, runtime)

    def get_faces_with_options(
        self,
        request: green_20180509_models.GetFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetFacesResponse:
        """
        @summary 获取人脸列表
        
        @param request: GetFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/faces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_faces_with_options_async(
        self,
        request: green_20180509_models.GetFacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetFacesResponse:
        """
        @summary 获取人脸列表
        
        @param request: GetFacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFaces',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/faces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_faces(
        self,
        request: green_20180509_models.GetFacesRequest,
    ) -> green_20180509_models.GetFacesResponse:
        """
        @summary 获取人脸列表
        
        @param request: GetFacesRequest
        @return: GetFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_faces_with_options(request, headers, runtime)

    async def get_faces_async(
        self,
        request: green_20180509_models.GetFacesRequest,
    ) -> green_20180509_models.GetFacesResponse:
        """
        @summary 获取人脸列表
        
        @param request: GetFacesRequest
        @return: GetFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_faces_with_options_async(request, headers, runtime)

    def get_groups_with_options(
        self,
        request: green_20180509_models.GetGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetGroupsResponse:
        """
        @summary 获取组列表
        
        @param request: GetGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_groups_with_options_async(
        self,
        request: green_20180509_models.GetGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetGroupsResponse:
        """
        @summary 获取组列表
        
        @param request: GetGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGroups',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/groups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_groups(
        self,
        request: green_20180509_models.GetGroupsRequest,
    ) -> green_20180509_models.GetGroupsResponse:
        """
        @summary 获取组列表
        
        @param request: GetGroupsRequest
        @return: GetGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_groups_with_options(request, headers, runtime)

    async def get_groups_async(
        self,
        request: green_20180509_models.GetGroupsRequest,
    ) -> green_20180509_models.GetGroupsResponse:
        """
        @summary 获取组列表
        
        @param request: GetGroupsRequest
        @return: GetGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_groups_with_options_async(request, headers, runtime)

    def get_person_with_options(
        self,
        request: green_20180509_models.GetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonResponse:
        """
        @summary 获取单个个体
        
        @param request: GetPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_person_with_options_async(
        self,
        request: green_20180509_models.GetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonResponse:
        """
        @summary 获取单个个体
        
        @param request: GetPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetPersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_person(
        self,
        request: green_20180509_models.GetPersonRequest,
    ) -> green_20180509_models.GetPersonResponse:
        """
        @summary 获取单个个体
        
        @param request: GetPersonRequest
        @return: GetPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_person_with_options(request, headers, runtime)

    async def get_person_async(
        self,
        request: green_20180509_models.GetPersonRequest,
    ) -> green_20180509_models.GetPersonResponse:
        """
        @summary 获取单个个体
        
        @param request: GetPersonRequest
        @return: GetPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_person_with_options_async(request, headers, runtime)

    def get_persons_with_options(
        self,
        request: green_20180509_models.GetPersonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonsResponse:
        """
        @summary 获取个体列表
        
        @param request: GetPersonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPersonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPersons',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/group/persons',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetPersonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_persons_with_options_async(
        self,
        request: green_20180509_models.GetPersonsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetPersonsResponse:
        """
        @summary 获取个体列表
        
        @param request: GetPersonsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPersonsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPersons',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/group/persons',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetPersonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_persons(
        self,
        request: green_20180509_models.GetPersonsRequest,
    ) -> green_20180509_models.GetPersonsResponse:
        """
        @summary 获取个体列表
        
        @param request: GetPersonsRequest
        @return: GetPersonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_persons_with_options(request, headers, runtime)

    async def get_persons_async(
        self,
        request: green_20180509_models.GetPersonsRequest,
    ) -> green_20180509_models.GetPersonsResponse:
        """
        @summary 获取个体列表
        
        @param request: GetPersonsRequest
        @return: GetPersonsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_persons_with_options_async(request, headers, runtime)

    def get_similarity_image_with_options(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        """
        @summary 获取相似图
        
        @param request: GetSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetSimilarityImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_similarity_image_with_options_async(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        """
        @summary 获取相似图
        
        @param request: GetSimilarityImageRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityImageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimilarityImage',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetSimilarityImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_similarity_image(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        """
        @summary 获取相似图
        
        @param request: GetSimilarityImageRequest
        @return: GetSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similarity_image_with_options(request, headers, runtime)

    async def get_similarity_image_async(
        self,
        request: green_20180509_models.GetSimilarityImageRequest,
    ) -> green_20180509_models.GetSimilarityImageResponse:
        """
        @summary 获取相似图
        
        @param request: GetSimilarityImageRequest
        @return: GetSimilarityImageResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_similarity_image_with_options_async(request, headers, runtime)

    def get_similarity_library_with_options(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        """
        @summary 获取相似图库
        
        @param request: GetSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetSimilarityLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_similarity_library_with_options_async(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        """
        @summary 获取相似图库
        
        @param request: GetSimilarityLibraryRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSimilarityLibraryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSimilarityLibrary',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/get',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.GetSimilarityLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_similarity_library(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        """
        @summary 获取相似图库
        
        @param request: GetSimilarityLibraryRequest
        @return: GetSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similarity_library_with_options(request, headers, runtime)

    async def get_similarity_library_async(
        self,
        request: green_20180509_models.GetSimilarityLibraryRequest,
    ) -> green_20180509_models.GetSimilarityLibraryResponse:
        """
        @summary 获取相似图库
        
        @param request: GetSimilarityLibraryRequest
        @return: GetSimilarityLibraryResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_similarity_library_with_options_async(request, headers, runtime)

    def image_async_manual_scan_with_options(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        """
        @summary 图片人工异步审核
        
        @param request: ImageAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncManualScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        """
        @summary 图片人工异步审核
        
        @param request: ImageAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncManualScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_manual_scan(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        """
        @summary 图片人工异步审核
        
        @param request: ImageAsyncManualScanRequest
        @return: ImageAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_manual_scan_with_options(request, headers, runtime)

    async def image_async_manual_scan_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResponse:
        """
        @summary 图片人工异步审核
        
        @param request: ImageAsyncManualScanRequest
        @return: ImageAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_manual_scan_with_options_async(request, headers, runtime)

    def image_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        """
        @summary 图片人工异步审核结果
        
        @param request: ImageAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncManualScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        """
        @summary 图片人工异步审核结果
        
        @param request: ImageAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncManualScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_manual_scan_results(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        """
        @summary 图片人工异步审核结果
        
        @param request: ImageAsyncManualScanResultsRequest
        @return: ImageAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_manual_scan_results_with_options(request, headers, runtime)

    async def image_async_manual_scan_results_async(
        self,
        request: green_20180509_models.ImageAsyncManualScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncManualScanResultsResponse:
        """
        @summary 图片人工异步审核结果
        
        @param request: ImageAsyncManualScanResultsRequest
        @return: ImageAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_manual_scan_results_with_options_async(request, headers, runtime)

    def image_async_scan_with_options(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_scan_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_scan(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncScanRequest
        @return: ImageAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_scan_with_options(request, headers, runtime)

    async def image_async_scan_async(
        self,
        request: green_20180509_models.ImageAsyncScanRequest,
    ) -> green_20180509_models.ImageAsyncScanResponse:
        """
        @summary 图片异步检测
        
        @param request: ImageAsyncScanRequest
        @return: ImageAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_scan_with_options_async(request, headers, runtime)

    def image_async_scan_results_with_options(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        """
        @summary 图片异步检测结果
        
        @param request: ImageAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        """
        @summary 图片异步检测结果
        
        @param request: ImageAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_async_scan_results(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        """
        @summary 图片异步检测结果
        
        @param request: ImageAsyncScanResultsRequest
        @return: ImageAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_async_scan_results_with_options(request, headers, runtime)

    async def image_async_scan_results_async(
        self,
        request: green_20180509_models.ImageAsyncScanResultsRequest,
    ) -> green_20180509_models.ImageAsyncScanResultsResponse:
        """
        @summary 图片异步检测结果
        
        @param request: ImageAsyncScanResultsRequest
        @return: ImageAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_async_scan_results_with_options_async(request, headers, runtime)

    def image_scan_feedback_with_options(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        """
        @summary 图片检测反馈
        
        @param request: ImageScanFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageScanFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageScanFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageScanFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_scan_feedback_with_options_async(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        """
        @summary 图片检测反馈
        
        @param request: ImageScanFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageScanFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageScanFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageScanFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_scan_feedback(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        """
        @summary 图片检测反馈
        
        @param request: ImageScanFeedbackRequest
        @return: ImageScanFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_scan_feedback_with_options(request, headers, runtime)

    async def image_scan_feedback_async(
        self,
        request: green_20180509_models.ImageScanFeedbackRequest,
    ) -> green_20180509_models.ImageScanFeedbackResponse:
        """
        @summary 图片检测反馈
        
        @param request: ImageScanFeedbackRequest
        @return: ImageScanFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_scan_feedback_with_options_async(request, headers, runtime)

    def image_sync_scan_with_options(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageSyncScanResponse:
        """
        @summary 图片同步检测
        
        @param request: ImageSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageSyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def image_sync_scan_with_options_async(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ImageSyncScanResponse:
        """
        @summary 图片同步检测
        
        @param request: ImageSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImageSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImageSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/image/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ImageSyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def image_sync_scan(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
    ) -> green_20180509_models.ImageSyncScanResponse:
        """
        @summary 图片同步检测
        
        @param request: ImageSyncScanRequest
        @return: ImageSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.image_sync_scan_with_options(request, headers, runtime)

    async def image_sync_scan_async(
        self,
        request: green_20180509_models.ImageSyncScanRequest,
    ) -> green_20180509_models.ImageSyncScanResponse:
        """
        @summary 图片同步检测
        
        @param request: ImageSyncScanRequest
        @return: ImageSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.image_sync_scan_with_options_async(request, headers, runtime)

    def list_similarity_images_with_options(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        """
        @summary 获取相似图
        
        @param request: ListSimilarityImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimilarityImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSimilarityImages',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ListSimilarityImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_similarity_images_with_options_async(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        """
        @summary 获取相似图
        
        @param request: ListSimilarityImagesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimilarityImagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSimilarityImages',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/image/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ListSimilarityImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_similarity_images(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        """
        @summary 获取相似图
        
        @param request: ListSimilarityImagesRequest
        @return: ListSimilarityImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_similarity_images_with_options(request, headers, runtime)

    async def list_similarity_images_async(
        self,
        request: green_20180509_models.ListSimilarityImagesRequest,
    ) -> green_20180509_models.ListSimilarityImagesResponse:
        """
        @summary 获取相似图
        
        @param request: ListSimilarityImagesRequest
        @return: ListSimilarityImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_similarity_images_with_options_async(request, headers, runtime)

    def list_similarity_libraries_with_options(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        """
        @summary 获取相似图库
        
        @param request: ListSimilarityLibrariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimilarityLibrariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSimilarityLibraries',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ListSimilarityLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_similarity_libraries_with_options_async(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        """
        @summary 获取相似图库
        
        @param request: ListSimilarityLibrariesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSimilarityLibrariesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSimilarityLibraries',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/similarity/library/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.ListSimilarityLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_similarity_libraries(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        """
        @summary 获取相似图库
        
        @param request: ListSimilarityLibrariesRequest
        @return: ListSimilarityLibrariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_similarity_libraries_with_options(request, headers, runtime)

    async def list_similarity_libraries_async(
        self,
        request: green_20180509_models.ListSimilarityLibrariesRequest,
    ) -> green_20180509_models.ListSimilarityLibrariesResponse:
        """
        @summary 获取相似图库
        
        @param request: ListSimilarityLibrariesRequest
        @return: ListSimilarityLibrariesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_similarity_libraries_with_options_async(request, headers, runtime)

    def live_stream_async_scan_with_options(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        """
        @summary 直播流异步检测
        
        @param request: LiveStreamAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def live_stream_async_scan_with_options_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        """
        @summary 直播流异步检测
        
        @param request: LiveStreamAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def live_stream_async_scan(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        """
        @summary 直播流异步检测
        
        @param request: LiveStreamAsyncScanRequest
        @return: LiveStreamAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_async_scan_with_options(request, headers, runtime)

    async def live_stream_async_scan_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResponse:
        """
        @summary 直播流异步检测
        
        @param request: LiveStreamAsyncScanRequest
        @return: LiveStreamAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_async_scan_with_options_async(request, headers, runtime)

    def live_stream_async_scan_results_with_options(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        """
        @summary 直播流异步检测结果
        
        @param request: LiveStreamAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def live_stream_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        """
        @summary 直播流异步检测结果
        
        @param request: LiveStreamAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def live_stream_async_scan_results(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        """
        @summary 直播流异步检测结果
        
        @param request: LiveStreamAsyncScanResultsRequest
        @return: LiveStreamAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_async_scan_results_with_options(request, headers, runtime)

    async def live_stream_async_scan_results_async(
        self,
        request: green_20180509_models.LiveStreamAsyncScanResultsRequest,
    ) -> green_20180509_models.LiveStreamAsyncScanResultsResponse:
        """
        @summary 直播流异步检测结果
        
        @param request: LiveStreamAsyncScanResultsRequest
        @return: LiveStreamAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_async_scan_results_with_options_async(request, headers, runtime)

    def live_stream_cancel_scan_with_options(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        """
        @summary 直播流取消检测
        
        @param request: LiveStreamCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamCancelScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def live_stream_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        """
        @summary 直播流取消检测
        
        @param request: LiveStreamCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: LiveStreamCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LiveStreamCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/livestream/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.LiveStreamCancelScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def live_stream_cancel_scan(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        """
        @summary 直播流取消检测
        
        @param request: LiveStreamCancelScanRequest
        @return: LiveStreamCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.live_stream_cancel_scan_with_options(request, headers, runtime)

    async def live_stream_cancel_scan_async(
        self,
        request: green_20180509_models.LiveStreamCancelScanRequest,
    ) -> green_20180509_models.LiveStreamCancelScanResponse:
        """
        @summary 直播流取消检测
        
        @param request: LiveStreamCancelScanRequest
        @return: LiveStreamCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.live_stream_cancel_scan_with_options_async(request, headers, runtime)

    def set_person_with_options(
        self,
        request: green_20180509_models.SetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SetPersonResponse:
        """
        @summary 设置个体
        
        @param request: SetPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.SetPersonResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_person_with_options_async(
        self,
        request: green_20180509_models.SetPersonRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.SetPersonResponse:
        """
        @summary 设置个体
        
        @param request: SetPersonRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetPersonResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPerson',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/sface/person/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.SetPersonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_person(
        self,
        request: green_20180509_models.SetPersonRequest,
    ) -> green_20180509_models.SetPersonResponse:
        """
        @summary 设置个体
        
        @param request: SetPersonRequest
        @return: SetPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.set_person_with_options(request, headers, runtime)

    async def set_person_async(
        self,
        request: green_20180509_models.SetPersonRequest,
    ) -> green_20180509_models.SetPersonResponse:
        """
        @summary 设置个体
        
        @param request: SetPersonRequest
        @return: SetPersonResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.set_person_with_options_async(request, headers, runtime)

    def text_async_manual_scan_with_options(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        """
        @summary 文本异步人工审核
        
        @param request: TextAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextAsyncManualScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        """
        @summary 文本异步人工审核
        
        @param request: TextAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextAsyncManualScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_async_manual_scan(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        """
        @summary 文本异步人工审核
        
        @param request: TextAsyncManualScanRequest
        @return: TextAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_async_manual_scan_with_options(request, headers, runtime)

    async def text_async_manual_scan_async(
        self,
        request: green_20180509_models.TextAsyncManualScanRequest,
    ) -> green_20180509_models.TextAsyncManualScanResponse:
        """
        @summary 文本异步人工审核
        
        @param request: TextAsyncManualScanRequest
        @return: TextAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_async_manual_scan_with_options_async(request, headers, runtime)

    def text_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        """
        @summary 文本异步人工审核结果
        
        @param request: TextAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextAsyncManualScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        """
        @summary 文本异步人工审核结果
        
        @param request: TextAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextAsyncManualScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_async_manual_scan_results(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        """
        @summary 文本异步人工审核结果
        
        @param request: TextAsyncManualScanResultsRequest
        @return: TextAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_async_manual_scan_results_with_options(request, headers, runtime)

    async def text_async_manual_scan_results_async(
        self,
        request: green_20180509_models.TextAsyncManualScanResultsRequest,
    ) -> green_20180509_models.TextAsyncManualScanResultsResponse:
        """
        @summary 文本异步人工审核结果
        
        @param request: TextAsyncManualScanResultsRequest
        @return: TextAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_async_manual_scan_results_with_options_async(request, headers, runtime)

    def text_feedback_with_options(
        self,
        request: green_20180509_models.TextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextFeedbackResponse:
        """
        @summary 文本结果反馈
        
        @param request: TextFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_feedback_with_options_async(
        self,
        request: green_20180509_models.TextFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextFeedbackResponse:
        """
        @summary 文本结果反馈
        
        @param request: TextFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_feedback(
        self,
        request: green_20180509_models.TextFeedbackRequest,
    ) -> green_20180509_models.TextFeedbackResponse:
        """
        @summary 文本结果反馈
        
        @param request: TextFeedbackRequest
        @return: TextFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_feedback_with_options(request, headers, runtime)

    async def text_feedback_async(
        self,
        request: green_20180509_models.TextFeedbackRequest,
    ) -> green_20180509_models.TextFeedbackResponse:
        """
        @summary 文本结果反馈
        
        @param request: TextFeedbackRequest
        @return: TextFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_feedback_with_options_async(request, headers, runtime)

    def text_scan_with_options(
        self,
        request: green_20180509_models.TextScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextScanResponse:
        """
        @param request: TextScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def text_scan_with_options_async(
        self,
        request: green_20180509_models.TextScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.TextScanResponse:
        """
        @param request: TextScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TextScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TextScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/text/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.TextScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def text_scan(
        self,
        request: green_20180509_models.TextScanRequest,
    ) -> green_20180509_models.TextScanResponse:
        """
        @param request: TextScanRequest
        @return: TextScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.text_scan_with_options(request, headers, runtime)

    async def text_scan_async(
        self,
        request: green_20180509_models.TextScanRequest,
    ) -> green_20180509_models.TextScanResponse:
        """
        @param request: TextScanRequest
        @return: TextScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.text_scan_with_options_async(request, headers, runtime)

    def upload_credentials_with_options(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.UploadCredentialsResponse:
        """
        @summary 获取上传证书
        
        @param request: UploadCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCredentials',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/credentials/uploadcredentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.UploadCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_credentials_with_options_async(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.UploadCredentialsResponse:
        """
        @summary 获取上传证书
        
        @param request: UploadCredentialsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCredentials',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/credentials/uploadcredentials',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.UploadCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_credentials(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
    ) -> green_20180509_models.UploadCredentialsResponse:
        """
        @summary 获取上传证书
        
        @param request: UploadCredentialsRequest
        @return: UploadCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_credentials_with_options(request, headers, runtime)

    async def upload_credentials_async(
        self,
        request: green_20180509_models.UploadCredentialsRequest,
    ) -> green_20180509_models.UploadCredentialsResponse:
        """
        @summary 获取上传证书
        
        @param request: UploadCredentialsRequest
        @return: UploadCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_credentials_with_options_async(request, headers, runtime)

    def video_async_manual_scan_with_options(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        """
        @summary 视频异步人工审核
        
        @param request: VideoAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncManualScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        """
        @summary 视频异步人工审核
        
        @param request: VideoAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncManualScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_async_manual_scan(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        """
        @summary 视频异步人工审核
        
        @param request: VideoAsyncManualScanRequest
        @return: VideoAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_manual_scan_with_options(request, headers, runtime)

    async def video_async_manual_scan_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResponse:
        """
        @summary 视频异步人工审核
        
        @param request: VideoAsyncManualScanRequest
        @return: VideoAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_manual_scan_with_options_async(request, headers, runtime)

    def video_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        """
        @summary 视频异步人工审核结果
        
        @param request: VideoAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncManualScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        """
        @summary 视频异步人工审核结果
        
        @param request: VideoAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncManualScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_async_manual_scan_results(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        """
        @summary 视频异步人工审核结果
        
        @param request: VideoAsyncManualScanResultsRequest
        @return: VideoAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_manual_scan_results_with_options(request, headers, runtime)

    async def video_async_manual_scan_results_async(
        self,
        request: green_20180509_models.VideoAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncManualScanResultsResponse:
        """
        @summary 视频异步人工审核结果
        
        @param request: VideoAsyncManualScanResultsRequest
        @return: VideoAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_manual_scan_results_with_options_async(request, headers, runtime)

    def video_async_scan_with_options(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        """
        @summary 视频异步检测
        
        @param request: VideoAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_async_scan_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        """
        @summary 视频异步检测
        
        @param request: VideoAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_async_scan(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        """
        @summary 视频异步检测
        
        @param request: VideoAsyncScanRequest
        @return: VideoAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_scan_with_options(request, headers, runtime)

    async def video_async_scan_async(
        self,
        request: green_20180509_models.VideoAsyncScanRequest,
    ) -> green_20180509_models.VideoAsyncScanResponse:
        """
        @summary 视频异步检测
        
        @param request: VideoAsyncScanRequest
        @return: VideoAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_scan_with_options_async(request, headers, runtime)

    def video_async_scan_results_with_options(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        """
        @summary 视频异步检测结果
        
        @param request: VideoAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        """
        @summary 视频异步检测结果
        
        @param request: VideoAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_async_scan_results(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        """
        @summary 视频异步检测结果
        
        @param request: VideoAsyncScanResultsRequest
        @return: VideoAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_async_scan_results_with_options(request, headers, runtime)

    async def video_async_scan_results_async(
        self,
        request: green_20180509_models.VideoAsyncScanResultsRequest,
    ) -> green_20180509_models.VideoAsyncScanResultsResponse:
        """
        @summary 视频异步检测结果
        
        @param request: VideoAsyncScanResultsRequest
        @return: VideoAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_async_scan_results_with_options_async(request, headers, runtime)

    def video_cancel_scan_with_options(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoCancelScanResponse:
        """
        @summary 视频取消检测
        
        @param request: VideoCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoCancelScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoCancelScanResponse:
        """
        @summary 视频取消检测
        
        @param request: VideoCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoCancelScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_cancel_scan(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
    ) -> green_20180509_models.VideoCancelScanResponse:
        """
        @summary 视频取消检测
        
        @param request: VideoCancelScanRequest
        @return: VideoCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_cancel_scan_with_options(request, headers, runtime)

    async def video_cancel_scan_async(
        self,
        request: green_20180509_models.VideoCancelScanRequest,
    ) -> green_20180509_models.VideoCancelScanResponse:
        """
        @summary 视频取消检测
        
        @param request: VideoCancelScanRequest
        @return: VideoCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_cancel_scan_with_options_async(request, headers, runtime)

    def video_feedback_with_options(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoFeedbackResponse:
        """
        @summary 视频结果反馈
        
        @param request: VideoFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_feedback_with_options_async(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoFeedbackResponse:
        """
        @summary 视频结果反馈
        
        @param request: VideoFeedbackRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoFeedback',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/feedback',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_feedback(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
    ) -> green_20180509_models.VideoFeedbackResponse:
        """
        @summary 视频结果反馈
        
        @param request: VideoFeedbackRequest
        @return: VideoFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_feedback_with_options(request, headers, runtime)

    async def video_feedback_async(
        self,
        request: green_20180509_models.VideoFeedbackRequest,
    ) -> green_20180509_models.VideoFeedbackResponse:
        """
        @summary 视频结果反馈
        
        @param request: VideoFeedbackRequest
        @return: VideoFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_feedback_with_options_async(request, headers, runtime)

    def video_sync_scan_with_options(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoSyncScanResponse:
        """
        @summary 视频同步检测
        
        @param request: VideoSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/syncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoSyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def video_sync_scan_with_options_async(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VideoSyncScanResponse:
        """
        @summary 视频同步检测
        
        @param request: VideoSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VideoSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VideoSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/video/syncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VideoSyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def video_sync_scan(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
    ) -> green_20180509_models.VideoSyncScanResponse:
        """
        @summary 视频同步检测
        
        @param request: VideoSyncScanRequest
        @return: VideoSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.video_sync_scan_with_options(request, headers, runtime)

    async def video_sync_scan_async(
        self,
        request: green_20180509_models.VideoSyncScanRequest,
    ) -> green_20180509_models.VideoSyncScanResponse:
        """
        @summary 视频同步检测
        
        @param request: VideoSyncScanRequest
        @return: VideoSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.video_sync_scan_with_options_async(request, headers, runtime)

    def vod_async_scan_with_options(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResponse:
        """
        @summary 视频点播异步检测
        
        @param request: VodAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VodAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VodAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/vod/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VodAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def vod_async_scan_with_options_async(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResponse:
        """
        @summary 视频点播异步检测
        
        @param request: VodAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VodAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VodAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/vod/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VodAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vod_async_scan(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
    ) -> green_20180509_models.VodAsyncScanResponse:
        """
        @summary 视频点播异步检测
        
        @param request: VodAsyncScanRequest
        @return: VodAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.vod_async_scan_with_options(request, headers, runtime)

    async def vod_async_scan_async(
        self,
        request: green_20180509_models.VodAsyncScanRequest,
    ) -> green_20180509_models.VodAsyncScanResponse:
        """
        @summary 视频点播异步检测
        
        @param request: VodAsyncScanRequest
        @return: VodAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.vod_async_scan_with_options_async(request, headers, runtime)

    def vod_async_scan_results_with_options(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        """
        @summary 视频点播异步检测结果
        
        @param request: VodAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VodAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VodAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/vod/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VodAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def vod_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        """
        @summary 视频点播异步检测结果
        
        @param request: VodAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VodAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VodAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/vod/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VodAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def vod_async_scan_results(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        """
        @summary 视频点播异步检测结果
        
        @param request: VodAsyncScanResultsRequest
        @return: VodAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.vod_async_scan_results_with_options(request, headers, runtime)

    async def vod_async_scan_results_async(
        self,
        request: green_20180509_models.VodAsyncScanResultsRequest,
    ) -> green_20180509_models.VodAsyncScanResultsResponse:
        """
        @summary 视频点播异步检测结果
        
        @param request: VodAsyncScanResultsRequest
        @return: VodAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.vod_async_scan_results_with_options_async(request, headers, runtime)

    def voice_async_manual_scan_with_options(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        """
        @summary 语音异步人工审核
        
        @param request: VoiceAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncManualScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_async_manual_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        """
        @summary 语音异步人工审核
        
        @param request: VoiceAsyncManualScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncManualScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncManualScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/manual/asyncScan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncManualScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_async_manual_scan(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        """
        @summary 语音异步人工审核
        
        @param request: VoiceAsyncManualScanRequest
        @return: VoiceAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_manual_scan_with_options(request, headers, runtime)

    async def voice_async_manual_scan_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResponse:
        """
        @summary 语音异步人工审核
        
        @param request: VoiceAsyncManualScanRequest
        @return: VoiceAsyncManualScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_manual_scan_with_options_async(request, headers, runtime)

    def voice_async_manual_scan_results_with_options(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        """
        @summary 语音异步人工审核结果
        
        @param request: VoiceAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncManualScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_async_manual_scan_results_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        """
        @summary 语音异步人工审核结果
        
        @param request: VoiceAsyncManualScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncManualScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncManualScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/manual/scan/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncManualScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_async_manual_scan_results(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        """
        @summary 语音异步人工审核结果
        
        @param request: VoiceAsyncManualScanResultsRequest
        @return: VoiceAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_manual_scan_results_with_options(request, headers, runtime)

    async def voice_async_manual_scan_results_async(
        self,
        request: green_20180509_models.VoiceAsyncManualScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncManualScanResultsResponse:
        """
        @summary 语音异步人工审核结果
        
        @param request: VoiceAsyncManualScanResultsRequest
        @return: VoiceAsyncManualScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_manual_scan_results_with_options_async(request, headers, runtime)

    def voice_async_scan_with_options(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        """
        @summary 语音异步检测
        
        @param request: VoiceAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_async_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        """
        @summary 语音异步检测
        
        @param request: VoiceAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_async_scan(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        """
        @summary 语音异步检测
        
        @param request: VoiceAsyncScanRequest
        @return: VoiceAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_scan_with_options(request, headers, runtime)

    async def voice_async_scan_async(
        self,
        request: green_20180509_models.VoiceAsyncScanRequest,
    ) -> green_20180509_models.VoiceAsyncScanResponse:
        """
        @summary 语音异步检测
        
        @param request: VoiceAsyncScanRequest
        @return: VoiceAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_scan_with_options_async(request, headers, runtime)

    def voice_async_scan_results_with_options(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        """
        @summary 语音异步检测结果
        
        @param request: VoiceAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        """
        @summary 语音异步检测结果
        
        @param request: VoiceAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_async_scan_results(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        """
        @summary 语音异步检测结果
        
        @param request: VoiceAsyncScanResultsRequest
        @return: VoiceAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_async_scan_results_with_options(request, headers, runtime)

    async def voice_async_scan_results_async(
        self,
        request: green_20180509_models.VoiceAsyncScanResultsRequest,
    ) -> green_20180509_models.VoiceAsyncScanResultsResponse:
        """
        @summary 语音异步检测结果
        
        @param request: VoiceAsyncScanResultsRequest
        @return: VoiceAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_async_scan_results_with_options_async(request, headers, runtime)

    def voice_cancel_scan_with_options(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        """
        @summary 语音取消检测
        
        @param request: VoiceCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceCancelScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_cancel_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        """
        @summary 语音取消检测
        
        @param request: VoiceCancelScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceCancelScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceCancelScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/cancelscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceCancelScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_cancel_scan(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        """
        @summary 语音取消检测
        
        @param request: VoiceCancelScanRequest
        @return: VoiceCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_cancel_scan_with_options(request, headers, runtime)

    async def voice_cancel_scan_async(
        self,
        request: green_20180509_models.VoiceCancelScanRequest,
    ) -> green_20180509_models.VoiceCancelScanResponse:
        """
        @summary 语音取消检测
        
        @param request: VoiceCancelScanRequest
        @return: VoiceCancelScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_cancel_scan_with_options_async(request, headers, runtime)

    def voice_identity_check_with_options(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        """
        @summary 声纹比对
        
        @param request: VoiceIdentityCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityCheck',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_identity_check_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        """
        @summary 声纹比对
        
        @param request: VoiceIdentityCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityCheck',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_identity_check(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        """
        @summary 声纹比对
        
        @param request: VoiceIdentityCheckRequest
        @return: VoiceIdentityCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_check_with_options(request, headers, runtime)

    async def voice_identity_check_async(
        self,
        request: green_20180509_models.VoiceIdentityCheckRequest,
    ) -> green_20180509_models.VoiceIdentityCheckResponse:
        """
        @summary 声纹比对
        
        @param request: VoiceIdentityCheckRequest
        @return: VoiceIdentityCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_check_with_options_async(request, headers, runtime)

    def voice_identity_register_with_options(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        """
        @summary 声纹注册
        
        @param request: VoiceIdentityRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityRegister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_identity_register_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        """
        @summary 声纹注册
        
        @param request: VoiceIdentityRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityRegister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_identity_register(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        """
        @summary 声纹注册
        
        @param request: VoiceIdentityRegisterRequest
        @return: VoiceIdentityRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_register_with_options(request, headers, runtime)

    async def voice_identity_register_async(
        self,
        request: green_20180509_models.VoiceIdentityRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityRegisterResponse:
        """
        @summary 声纹注册
        
        @param request: VoiceIdentityRegisterRequest
        @return: VoiceIdentityRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_register_with_options_async(request, headers, runtime)

    def voice_identity_start_check_with_options(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        """
        @summary 声纹开始比对
        
        @param request: VoiceIdentityStartCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityStartCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityStartCheck',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/start/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityStartCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_identity_start_check_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        """
        @summary 声纹开始比对
        
        @param request: VoiceIdentityStartCheckRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityStartCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityStartCheck',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/start/check',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityStartCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_identity_start_check(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        """
        @summary 声纹开始比对
        
        @param request: VoiceIdentityStartCheckRequest
        @return: VoiceIdentityStartCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_start_check_with_options(request, headers, runtime)

    async def voice_identity_start_check_async(
        self,
        request: green_20180509_models.VoiceIdentityStartCheckRequest,
    ) -> green_20180509_models.VoiceIdentityStartCheckResponse:
        """
        @summary 声纹开始比对
        
        @param request: VoiceIdentityStartCheckRequest
        @return: VoiceIdentityStartCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_start_check_with_options_async(request, headers, runtime)

    def voice_identity_start_register_with_options(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        """
        @summary 声纹开始注册
        
        @param request: VoiceIdentityStartRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityStartRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityStartRegister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/start/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityStartRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_identity_start_register_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        """
        @summary 声纹开始注册
        
        @param request: VoiceIdentityStartRegisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityStartRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityStartRegister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/start/register',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityStartRegisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_identity_start_register(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        """
        @summary 声纹开始注册
        
        @param request: VoiceIdentityStartRegisterRequest
        @return: VoiceIdentityStartRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_start_register_with_options(request, headers, runtime)

    async def voice_identity_start_register_async(
        self,
        request: green_20180509_models.VoiceIdentityStartRegisterRequest,
    ) -> green_20180509_models.VoiceIdentityStartRegisterResponse:
        """
        @summary 声纹开始注册
        
        @param request: VoiceIdentityStartRegisterRequest
        @return: VoiceIdentityStartRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_start_register_with_options_async(request, headers, runtime)

    def voice_identity_unregister_with_options(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        """
        @summary 声纹注销
        
        @param request: VoiceIdentityUnregisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityUnregisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityUnregister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/unregister',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityUnregisterResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_identity_unregister_with_options_async(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        """
        @summary 声纹注销
        
        @param request: VoiceIdentityUnregisterRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceIdentityUnregisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceIdentityUnregister',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/auth/unregister',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceIdentityUnregisterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_identity_unregister(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        """
        @summary 声纹注销
        
        @param request: VoiceIdentityUnregisterRequest
        @return: VoiceIdentityUnregisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_identity_unregister_with_options(request, headers, runtime)

    async def voice_identity_unregister_async(
        self,
        request: green_20180509_models.VoiceIdentityUnregisterRequest,
    ) -> green_20180509_models.VoiceIdentityUnregisterResponse:
        """
        @summary 声纹注销
        
        @param request: VoiceIdentityUnregisterRequest
        @return: VoiceIdentityUnregisterResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_identity_unregister_with_options_async(request, headers, runtime)

    def voice_sync_scan_with_options(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        """
        @summary 语音同步检测
        
        @param request: VoiceSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/syncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceSyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def voice_sync_scan_with_options_async(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        """
        @summary 语音同步检测
        
        @param request: VoiceSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: VoiceSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VoiceSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/voice/syncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.VoiceSyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def voice_sync_scan(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        """
        @summary 语音同步检测
        
        @param request: VoiceSyncScanRequest
        @return: VoiceSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.voice_sync_scan_with_options(request, headers, runtime)

    async def voice_sync_scan_async(
        self,
        request: green_20180509_models.VoiceSyncScanRequest,
    ) -> green_20180509_models.VoiceSyncScanResponse:
        """
        @summary 语音同步检测
        
        @param request: VoiceSyncScanRequest
        @return: VoiceSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.voice_sync_scan_with_options_async(request, headers, runtime)

    def webpage_async_scan_with_options(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        """
        @summary 站点异步检测
        
        @param request: WebpageAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageAsyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def webpage_async_scan_with_options_async(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        """
        @summary 站点异步检测
        
        @param request: WebpageAsyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageAsyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageAsyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/asyncscan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageAsyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def webpage_async_scan(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        """
        @summary 站点异步检测
        
        @param request: WebpageAsyncScanRequest
        @return: WebpageAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_async_scan_with_options(request, headers, runtime)

    async def webpage_async_scan_async(
        self,
        request: green_20180509_models.WebpageAsyncScanRequest,
    ) -> green_20180509_models.WebpageAsyncScanResponse:
        """
        @summary 站点异步检测
        
        @param request: WebpageAsyncScanRequest
        @return: WebpageAsyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_async_scan_with_options_async(request, headers, runtime)

    def webpage_async_scan_results_with_options(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        """
        @summary 站点异步检测结果
        
        @param request: WebpageAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageAsyncScanResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def webpage_async_scan_results_with_options_async(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        """
        @summary 站点异步检测结果
        
        @param request: WebpageAsyncScanResultsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageAsyncScanResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageAsyncScanResults',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/results',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageAsyncScanResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def webpage_async_scan_results(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        """
        @summary 站点异步检测结果
        
        @param request: WebpageAsyncScanResultsRequest
        @return: WebpageAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_async_scan_results_with_options(request, headers, runtime)

    async def webpage_async_scan_results_async(
        self,
        request: green_20180509_models.WebpageAsyncScanResultsRequest,
    ) -> green_20180509_models.WebpageAsyncScanResultsResponse:
        """
        @summary 站点异步检测结果
        
        @param request: WebpageAsyncScanResultsRequest
        @return: WebpageAsyncScanResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_async_scan_results_with_options_async(request, headers, runtime)

    def webpage_sync_scan_with_options(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        """
        @summary 站点同步检测
        
        @param request: WebpageSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageSyncScanResponse(),
            self.call_api(params, req, runtime)
        )

    async def webpage_sync_scan_with_options_async(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        """
        @summary 站点同步检测
        
        @param request: WebpageSyncScanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: WebpageSyncScanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_info):
            query['ClientInfo'] = request.client_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WebpageSyncScan',
            version='2018-05-09',
            protocol='HTTPS',
            pathname=f'/green/webpage/scan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20180509_models.WebpageSyncScanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def webpage_sync_scan(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        """
        @summary 站点同步检测
        
        @param request: WebpageSyncScanRequest
        @return: WebpageSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.webpage_sync_scan_with_options(request, headers, runtime)

    async def webpage_sync_scan_async(
        self,
        request: green_20180509_models.WebpageSyncScanRequest,
    ) -> green_20180509_models.WebpageSyncScanResponse:
        """
        @summary 站点同步检测
        
        @param request: WebpageSyncScanRequest
        @return: WebpageSyncScanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.webpage_sync_scan_with_options_async(request, headers, runtime)
