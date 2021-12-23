# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ice20201109 import models as ice20201109_models
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
            'ap-northeast-1': 'ice.aliyuncs.com',
            'ap-northeast-2-pop': 'ice.aliyuncs.com',
            'ap-south-1': 'ice.aliyuncs.com',
            'ap-southeast-1': 'ice.aliyuncs.com',
            'ap-southeast-2': 'ice.aliyuncs.com',
            'ap-southeast-3': 'ice.aliyuncs.com',
            'ap-southeast-5': 'ice.aliyuncs.com',
            'cn-beijing': 'ice.aliyuncs.com',
            'cn-beijing-finance-1': 'ice.aliyuncs.com',
            'cn-beijing-finance-pop': 'ice.aliyuncs.com',
            'cn-beijing-gov-1': 'ice.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ice.aliyuncs.com',
            'cn-chengdu': 'ice.aliyuncs.com',
            'cn-edge-1': 'ice.aliyuncs.com',
            'cn-fujian': 'ice.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ice.aliyuncs.com',
            'cn-hangzhou': 'ice.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ice.aliyuncs.com',
            'cn-hangzhou-finance': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ice.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ice.aliyuncs.com',
            'cn-hangzhou-test-306': 'ice.aliyuncs.com',
            'cn-hongkong': 'ice.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ice.aliyuncs.com',
            'cn-huhehaote': 'ice.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'ice.aliyuncs.com',
            'cn-north-2-gov-1': 'ice.aliyuncs.com',
            'cn-qingdao': 'ice.aliyuncs.com',
            'cn-qingdao-nebula': 'ice.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ice.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ice.aliyuncs.com',
            'cn-shanghai-finance-1': 'ice.aliyuncs.com',
            'cn-shanghai-inner': 'ice.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ice.aliyuncs.com',
            'cn-shenzhen': 'ice.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ice.aliyuncs.com',
            'cn-shenzhen-inner': 'ice.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ice.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ice.aliyuncs.com',
            'cn-wuhan': 'ice.aliyuncs.com',
            'cn-wulanchabu': 'ice.aliyuncs.com',
            'cn-yushanfang': 'ice.aliyuncs.com',
            'cn-zhangbei': 'ice.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ice.aliyuncs.com',
            'cn-zhangjiakou': 'ice.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ice.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ice.aliyuncs.com',
            'eu-central-1': 'ice.aliyuncs.com',
            'eu-west-1': 'ice.aliyuncs.com',
            'eu-west-1-oxs': 'ice.aliyuncs.com',
            'me-east-1': 'ice.aliyuncs.com',
            'rus-west-1-pop': 'ice.aliyuncs.com',
            'us-east-1': 'ice.aliyuncs.com',
            'us-west-1': 'ice.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_editing_project_materials_with_options(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialMaps'] = request.material_maps
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialMaps'] = request.material_maps
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_editing_project_materials(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_editing_project_materials_with_options(request, runtime)

    async def add_editing_project_materials_async(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_editing_project_materials_with_options_async(request, runtime)

    def add_favorite_public_media_with_options(
        self,
        request: ice20201109_models.AddFavoritePublicMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddFavoritePublicMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddFavoritePublicMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_favorite_public_media_with_options_async(
        self,
        request: ice20201109_models.AddFavoritePublicMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddFavoritePublicMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddFavoritePublicMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_favorite_public_media(
        self,
        request: ice20201109_models.AddFavoritePublicMediaRequest,
    ) -> ice20201109_models.AddFavoritePublicMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_favorite_public_media_with_options(request, runtime)

    async def add_favorite_public_media_async(
        self,
        request: ice20201109_models.AddFavoritePublicMediaRequest,
    ) -> ice20201109_models.AddFavoritePublicMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_favorite_public_media_with_options_async(request, runtime)

    def add_template_with_options(
        self,
        request: ice20201109_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['CoverUrl'] = request.cover_url
        query['Name'] = request.name
        query['PreviewMedia'] = request.preview_media
        query['RelatedMediaids'] = request.related_mediaids
        query['Source'] = request.source
        query['Status'] = request.status
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_template_with_options_async(
        self,
        request: ice20201109_models.AddTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['CoverUrl'] = request.cover_url
        query['Name'] = request.name
        query['PreviewMedia'] = request.preview_media
        query['RelatedMediaids'] = request.related_mediaids
        query['Source'] = request.source
        query['Status'] = request.status
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.AddTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_template(
        self,
        request: ice20201109_models.AddTemplateRequest,
    ) -> ice20201109_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_template_with_options(request, runtime)

    async def add_template_async(
        self,
        request: ice20201109_models.AddTemplateRequest,
    ) -> ice20201109_models.AddTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_template_with_options_async(request, runtime)

    def batch_get_media_infos_with_options(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdditionType'] = request.addition_type
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_media_infos_with_options_async(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AdditionType'] = request.addition_type
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.BatchGetMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_media_infos(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_get_media_infos_with_options(request, runtime)

    async def batch_get_media_infos_async(
        self,
        request: ice20201109_models.BatchGetMediaInfosRequest,
    ) -> ice20201109_models.BatchGetMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_media_infos_with_options_async(request, runtime)

    def cancel_favorite_public_media_with_options(
        self,
        request: ice20201109_models.CancelFavoritePublicMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CancelFavoritePublicMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CancelFavoritePublicMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_favorite_public_media_with_options_async(
        self,
        request: ice20201109_models.CancelFavoritePublicMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CancelFavoritePublicMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelFavoritePublicMedia',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CancelFavoritePublicMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_favorite_public_media(
        self,
        request: ice20201109_models.CancelFavoritePublicMediaRequest,
    ) -> ice20201109_models.CancelFavoritePublicMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_favorite_public_media_with_options(request, runtime)

    async def cancel_favorite_public_media_async(
        self,
        request: ice20201109_models.CancelFavoritePublicMediaRequest,
    ) -> ice20201109_models.CancelFavoritePublicMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_favorite_public_media_with_options_async(request, runtime)

    def create_editing_project_with_options(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessConfig'] = request.business_config
        query['ClipsParam'] = request.clips_param
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['MaterialMaps'] = request.material_maps
        query['ProjectType'] = request.project_type
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_editing_project_with_options_async(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessConfig'] = request.business_config
        query['ClipsParam'] = request.clips_param
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['MaterialMaps'] = request.material_maps
        query['ProjectType'] = request.project_type
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.CreateEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_editing_project(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_editing_project_with_options(request, runtime)

    async def create_editing_project_async(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_editing_project_with_options_async(request, runtime)

    def delete_editing_project_materials_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialIds'] = request.material_ids
        query['MaterialType'] = request.material_type
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialIds'] = request.material_ids
        query['MaterialType'] = request.material_type
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_editing_project_materials(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_project_materials_with_options(request, runtime)

    async def delete_editing_project_materials_async(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_project_materials_with_options_async(request, runtime)

    def delete_editing_projects_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjects',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_editing_projects_with_options_async(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEditingProjects',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteEditingProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_editing_projects(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_editing_projects_with_options(request, runtime)

    async def delete_editing_projects_async(
        self,
        request: ice20201109_models.DeleteEditingProjectsRequest,
    ) -> ice20201109_models.DeleteEditingProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_editing_projects_with_options_async(request, runtime)

    def delete_media_infos_with_options(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputURLs'] = request.input_urls
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_media_infos_with_options_async(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputURLs'] = request.input_urls
        query['MediaIds'] = request.media_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMediaInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteMediaInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_media_infos(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_media_infos_with_options(request, runtime)

    async def delete_media_infos_async(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_media_infos_with_options_async(request, runtime)

    def delete_smart_job_with_options(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_smart_job_with_options_async(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSmartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteSmartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_smart_job(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_smart_job_with_options(request, runtime)

    async def delete_smart_job_async(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_smart_job_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
    ) -> ice20201109_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: ice20201109_models.DeleteTemplateRequest,
    ) -> ice20201109_models.DeleteTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def describe_ice_product_status_with_options(
        self,
        request: ice20201109_models.DescribeIceProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIceProductStatus',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeIceProductStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_ice_product_status_with_options_async(
        self,
        request: ice20201109_models.DescribeIceProductStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIceProductStatus',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeIceProductStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_ice_product_status(
        self,
        request: ice20201109_models.DescribeIceProductStatusRequest,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ice_product_status_with_options(request, runtime)

    async def describe_ice_product_status_async(
        self,
        request: ice20201109_models.DescribeIceProductStatusRequest,
    ) -> ice20201109_models.DescribeIceProductStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ice_product_status_with_options_async(request, runtime)

    def describe_material_package_info_with_options(
        self,
        request: ice20201109_models.DescribeMaterialPackageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMaterialPackageInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialPackageId'] = request.material_package_id
        query['MaterialPackageType'] = request.material_package_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaterialPackageInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMaterialPackageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_material_package_info_with_options_async(
        self,
        request: ice20201109_models.DescribeMaterialPackageInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMaterialPackageInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaterialPackageId'] = request.material_package_id
        query['MaterialPackageType'] = request.material_package_type
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMaterialPackageInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeMaterialPackageInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_material_package_info(
        self,
        request: ice20201109_models.DescribeMaterialPackageInfoRequest,
    ) -> ice20201109_models.DescribeMaterialPackageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_material_package_info_with_options(request, runtime)

    async def describe_material_package_info_async(
        self,
        request: ice20201109_models.DescribeMaterialPackageInfoRequest,
    ) -> ice20201109_models.DescribeMaterialPackageInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_material_package_info_with_options_async(request, runtime)

    def describe_related_authorization_status_with_options(
        self,
        request: ice20201109_models.DescribeRelatedAuthorizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRelatedAuthorizationStatus',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeRelatedAuthorizationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_related_authorization_status_with_options_async(
        self,
        request: ice20201109_models.DescribeRelatedAuthorizationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRelatedAuthorizationStatus',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.DescribeRelatedAuthorizationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_related_authorization_status(
        self,
        request: ice20201109_models.DescribeRelatedAuthorizationStatusRequest,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_related_authorization_status_with_options(request, runtime)

    async def describe_related_authorization_status_async(
        self,
        request: ice20201109_models.DescribeRelatedAuthorizationStatusRequest,
    ) -> ice20201109_models.DescribeRelatedAuthorizationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_related_authorization_status_with_options_async(request, runtime)

    def get_default_storage_location_with_options(
        self,
        request: ice20201109_models.GetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_default_storage_location_with_options_async(
        self,
        request: ice20201109_models.GetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetDefaultStorageLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_default_storage_location(
        self,
        request: ice20201109_models.GetDefaultStorageLocationRequest,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_storage_location_with_options(request, runtime)

    async def get_default_storage_location_async(
        self,
        request: ice20201109_models.GetDefaultStorageLocationRequest,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_storage_location_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_editing_project_with_options_async(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_editing_project(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
    ) -> ice20201109_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_with_options(request, runtime)

    async def get_editing_project_async(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
    ) -> ice20201109_models.GetEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_with_options_async(request, runtime)

    def get_editing_project_materials_with_options(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_editing_project_materials_with_options_async(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingProjectMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEditingProjectMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_editing_project_materials(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_editing_project_materials_with_options(request, runtime)

    async def get_editing_project_materials_async(
        self,
        request: ice20201109_models.GetEditingProjectMaterialsRequest,
    ) -> ice20201109_models.GetEditingProjectMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_editing_project_materials_with_options_async(request, runtime)

    def get_event_callback_with_options(
        self,
        request: ice20201109_models.GetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_callback_with_options_async(
        self,
        request: ice20201109_models.GetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetEventCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event_callback(
        self,
        request: ice20201109_models.GetEventCallbackRequest,
    ) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_callback_with_options(request, runtime)

    async def get_event_callback_async(
        self,
        request: ice20201109_models.GetEventCallbackRequest,
    ) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_callback_with_options_async(request, runtime)

    def get_live_editing_index_file_with_options(
        self,
        request: ice20201109_models.GetLiveEditingIndexFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveEditingIndexFileResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingIndexFile',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingIndexFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_editing_index_file_with_options_async(
        self,
        request: ice20201109_models.GetLiveEditingIndexFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveEditingIndexFileResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingIndexFile',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingIndexFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_editing_index_file(
        self,
        request: ice20201109_models.GetLiveEditingIndexFileRequest,
    ) -> ice20201109_models.GetLiveEditingIndexFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_editing_index_file_with_options(request, runtime)

    async def get_live_editing_index_file_async(
        self,
        request: ice20201109_models.GetLiveEditingIndexFileRequest,
    ) -> ice20201109_models.GetLiveEditingIndexFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_editing_index_file_with_options_async(request, runtime)

    def get_live_editing_job_with_options(
        self,
        request: ice20201109_models.GetLiveEditingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveEditingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_editing_job_with_options_async(
        self,
        request: ice20201109_models.GetLiveEditingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveEditingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetLiveEditingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_editing_job(
        self,
        request: ice20201109_models.GetLiveEditingJobRequest,
    ) -> ice20201109_models.GetLiveEditingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_editing_job_with_options(request, runtime)

    async def get_live_editing_job_async(
        self,
        request: ice20201109_models.GetLiveEditingJobRequest,
    ) -> ice20201109_models.GetLiveEditingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_editing_job_with_options_async(request, runtime)

    def get_media_info_with_options(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputURL'] = request.input_url
        query['MediaId'] = request.media_id
        query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_info_with_options_async(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InputURL'] = request.input_url
        query['MediaId'] = request.media_id
        query['OutputType'] = request.output_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_info(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
    ) -> ice20201109_models.GetMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_with_options(request, runtime)

    async def get_media_info_async(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
    ) -> ice20201109_models.GetMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_info_with_options_async(request, runtime)

    def get_media_producing_job_with_options(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_producing_job_with_options_async(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetMediaProducingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_producing_job(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_producing_job_with_options(request, runtime)

    async def get_media_producing_job_async(
        self,
        request: ice20201109_models.GetMediaProducingJobRequest,
    ) -> ice20201109_models.GetMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_producing_job_with_options_async(request, runtime)

    def get_public_media_info_with_options(
        self,
        request: ice20201109_models.GetPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPublicMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_public_media_info_with_options_async(
        self,
        request: ice20201109_models.GetPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetPublicMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_public_media_info(
        self,
        request: ice20201109_models.GetPublicMediaInfoRequest,
    ) -> ice20201109_models.GetPublicMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_public_media_info_with_options(request, runtime)

    async def get_public_media_info_async(
        self,
        request: ice20201109_models.GetPublicMediaInfoRequest,
    ) -> ice20201109_models.GetPublicMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_public_media_info_with_options_async(request, runtime)

    def get_smart_handle_job_with_options(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartHandleJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_smart_handle_job_with_options_async(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSmartHandleJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetSmartHandleJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_smart_handle_job(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_smart_handle_job_with_options(request, runtime)

    async def get_smart_handle_job_async(
        self,
        request: ice20201109_models.GetSmartHandleJobRequest,
    ) -> ice20201109_models.GetSmartHandleJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_smart_handle_job_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: ice20201109_models.GetTemplateRequest,
    ) -> ice20201109_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: ice20201109_models.GetTemplateRequest,
    ) -> ice20201109_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_materials_with_options(
        self,
        request: ice20201109_models.GetTemplateMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_materials_with_options_async(
        self,
        request: ice20201109_models.GetTemplateMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateMaterialsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateMaterials',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.GetTemplateMaterialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_materials(
        self,
        request: ice20201109_models.GetTemplateMaterialsRequest,
    ) -> ice20201109_models.GetTemplateMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_materials_with_options(request, runtime)

    async def get_template_materials_async(
        self,
        request: ice20201109_models.GetTemplateMaterialsRequest,
    ) -> ice20201109_models.GetTemplateMaterialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_materials_with_options_async(request, runtime)

    def list_all_public_media_tags_with_options(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPublicMediaTags',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_all_public_media_tags_with_options_async(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAllPublicMediaTags',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListAllPublicMediaTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_all_public_media_tags(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_all_public_media_tags_with_options(request, runtime)

    async def list_all_public_media_tags_async(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_all_public_media_tags_with_options_async(request, runtime)

    def list_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['EndTime'] = request.end_time
        query['IncludeFileBasicInfo'] = request.include_file_basic_info
        query['MaxResults'] = request.max_results
        query['MediaType'] = request.media_type
        query['NextToken'] = request.next_token
        query['SortBy'] = request.sort_by
        query['Source'] = request.source
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_basic_infos_with_options_async(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['EndTime'] = request.end_time
        query['IncludeFileBasicInfo'] = request.include_file_basic_info
        query['MaxResults'] = request.max_results
        query['MediaType'] = request.media_type
        query['NextToken'] = request.next_token
        query['SortBy'] = request.sort_by
        query['Source'] = request.source
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaBasicInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_media_basic_infos(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_basic_infos_with_options(request, runtime)

    async def list_media_basic_infos_async(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_basic_infos_with_options_async(request, runtime)

    def list_media_producing_jobs_with_options(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaProducingJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaProducingJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_producing_jobs_with_options_async(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaProducingJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListMediaProducingJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_media_producing_jobs(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_producing_jobs_with_options(request, runtime)

    async def list_media_producing_jobs_async(
        self,
        request: ice20201109_models.ListMediaProducingJobsRequest,
    ) -> ice20201109_models.ListMediaProducingJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_producing_jobs_with_options_async(request, runtime)

    def list_public_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IncludeFileBasicInfo'] = request.include_file_basic_info
        query['MaxResults'] = request.max_results
        query['MediaTagId'] = request.media_tag_id
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_public_media_basic_infos_with_options_async(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        query['IncludeFileBasicInfo'] = request.include_file_basic_info
        query['MaxResults'] = request.max_results
        query['MediaTagId'] = request.media_tag_id
        query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListPublicMediaBasicInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_public_media_basic_infos(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_public_media_basic_infos_with_options(request, runtime)

    async def list_public_media_basic_infos_async(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_public_media_basic_infos_with_options_async(request, runtime)

    def list_smart_jobs_with_options(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSmartJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_smart_jobs_with_options_async(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSmartJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSmartJobs',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSmartJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_smart_jobs(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
    ) -> ice20201109_models.ListSmartJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_smart_jobs_with_options(request, runtime)

    async def list_smart_jobs_async(
        self,
        request: ice20201109_models.ListSmartJobsRequest,
    ) -> ice20201109_models.ListSmartJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_smart_jobs_with_options_async(request, runtime)

    def list_sys_templates_with_options(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSysTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSysTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sys_templates_with_options_async(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSysTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListSysTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sys_templates(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_sys_templates_with_options(request, runtime)

    async def list_sys_templates_async(
        self,
        request: ice20201109_models.ListSysTemplatesRequest,
    ) -> ice20201109_models.ListSysTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_sys_templates_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ice20201109_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateSource'] = request.create_source
        query['Keyword'] = request.keyword
        query['SortType'] = request.sort_type
        query['Status'] = request.status
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: ice20201109_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateSource'] = request.create_source
        query['Keyword'] = request.keyword
        query['SortType'] = request.sort_type
        query['Status'] = request.status
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: ice20201109_models.ListTemplatesRequest,
    ) -> ice20201109_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: ice20201109_models.ListTemplatesRequest,
    ) -> ice20201109_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def register_media_info_with_options(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['ClientToken'] = request.client_token
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['DynamicMetaDataList'] = request.dynamic_meta_data_list
        query['InputURL'] = request.input_url
        query['MediaTags'] = request.media_tags
        query['MediaType'] = request.media_type
        query['Overwrite'] = request.overwrite
        query['RegisterConfig'] = request.register_config
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_media_info_with_options_async(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['ClientToken'] = request.client_token
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['DynamicMetaDataList'] = request.dynamic_meta_data_list
        query['InputURL'] = request.input_url
        query['MediaTags'] = request.media_tags
        query['MediaType'] = request.media_type
        query['Overwrite'] = request.overwrite
        query['RegisterConfig'] = request.register_config
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.RegisterMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_media_info(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_info_with_options(request, runtime)

    async def register_media_info_async(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_info_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateSource'] = request.create_source
        query['EndTime'] = request.end_time
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectType'] = request.project_type
        query['SortBy'] = request.sort_by
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_editing_project_with_options_async(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CreateSource'] = request.create_source
        query['EndTime'] = request.end_time
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectType'] = request.project_type
        query['SortBy'] = request.sort_by
        query['StartTime'] = request.start_time
        query['Status'] = request.status
        query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_editing_project(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_editing_project_with_options(request, runtime)

    async def search_editing_project_async(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_editing_project_with_options_async(request, runtime)

    def search_public_media_info_with_options(
        self,
        request: ice20201109_models.SearchPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Authorized'] = request.authorized
        query['DynamicMetaDataMatchFields'] = request.dynamic_meta_data_match_fields
        query['EntityId'] = request.entity_id
        query['Favorite'] = request.favorite
        query['MediaIds'] = request.media_ids
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchPublicMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_public_media_info_with_options_async(
        self,
        request: ice20201109_models.SearchPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Authorized'] = request.authorized
        query['DynamicMetaDataMatchFields'] = request.dynamic_meta_data_match_fields
        query['EntityId'] = request.entity_id
        query['Favorite'] = request.favorite
        query['MediaIds'] = request.media_ids
        query['PageNo'] = request.page_no
        query['PageSize'] = request.page_size
        query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchPublicMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SearchPublicMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_public_media_info(
        self,
        request: ice20201109_models.SearchPublicMediaInfoRequest,
    ) -> ice20201109_models.SearchPublicMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_public_media_info_with_options(request, runtime)

    async def search_public_media_info_async(
        self,
        request: ice20201109_models.SearchPublicMediaInfoRequest,
    ) -> ice20201109_models.SearchPublicMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_public_media_info_with_options_async(request, runtime)

    def set_default_storage_location_with_options(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['Path'] = request.path
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_storage_location_with_options_async(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Bucket'] = request.bucket
        query['Path'] = request.path
        query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultStorageLocation',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetDefaultStorageLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_storage_location(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_storage_location_with_options(request, runtime)

    async def set_default_storage_location_async(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_storage_location_with_options_async(request, runtime)

    def set_event_callback_with_options(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetEventCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallbackQueueName'] = request.callback_queue_name
        query['EventTypeList'] = request.event_type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_event_callback_with_options_async(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetEventCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallbackQueueName'] = request.callback_queue_name
        query['EventTypeList'] = request.event_type_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEventCallback',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SetEventCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_event_callback(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
    ) -> ice20201109_models.SetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_event_callback_with_options(request, runtime)

    async def set_event_callback_async(
        self,
        request: ice20201109_models.SetEventCallbackRequest,
    ) -> ice20201109_models.SetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_event_callback_with_options_async(request, runtime)

    def submit_asrjob_with_options(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitASRJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['Duration'] = request.duration
        query['InputFile'] = request.input_file
        query['StartTime'] = request.start_time
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitASRJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_asrjob_with_options_async(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitASRJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['Duration'] = request.duration
        query['InputFile'] = request.input_file
        query['StartTime'] = request.start_time
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitASRJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitASRJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_asrjob(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
    ) -> ice20201109_models.SubmitASRJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_asrjob_with_options(request, runtime)

    async def submit_asrjob_async(
        self,
        request: ice20201109_models.SubmitASRJobRequest,
    ) -> ice20201109_models.SubmitASRJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_asrjob_with_options_async(request, runtime)

    def submit_audio_produce_job_with_options(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['EditingConfig'] = request.editing_config
        query['InputConfig'] = request.input_config
        query['OutputConfig'] = request.output_config
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_audio_produce_job_with_options_async(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['EditingConfig'] = request.editing_config
        query['InputConfig'] = request.input_config
        query['OutputConfig'] = request.output_config
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitAudioProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitAudioProduceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_audio_produce_job(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_audio_produce_job_with_options(request, runtime)

    async def submit_audio_produce_job_async(
        self,
        request: ice20201109_models.SubmitAudioProduceJobRequest,
    ) -> ice20201109_models.SubmitAudioProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_audio_produce_job_with_options_async(request, runtime)

    def submit_delogo_job_with_options(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDelogoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDelogoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_delogo_job_with_options_async(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDelogoJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDelogoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_delogo_job(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_delogo_job_with_options(request, runtime)

    async def submit_delogo_job_async(
        self,
        request: ice20201109_models.SubmitDelogoJobRequest,
    ) -> ice20201109_models.SubmitDelogoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_delogo_job_with_options_async(request, runtime)

    def submit_dynamic_chart_job_with_options(
        self,
        request: ice20201109_models.SubmitDynamicChartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDynamicChartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AxisParams'] = request.axis_params
        query['Background'] = request.background
        query['ChartConfig'] = request.chart_config
        query['ChartTitle'] = request.chart_title
        query['ChartType'] = request.chart_type
        query['DataSource'] = request.data_source
        query['Description'] = request.description
        query['Input'] = request.input
        query['OutputConfig'] = request.output_config
        query['Subtitle'] = request.subtitle
        query['Title'] = request.title
        query['Unit'] = request.unit
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicChartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDynamicChartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_dynamic_chart_job_with_options_async(
        self,
        request: ice20201109_models.SubmitDynamicChartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDynamicChartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AxisParams'] = request.axis_params
        query['Background'] = request.background
        query['ChartConfig'] = request.chart_config
        query['ChartTitle'] = request.chart_title
        query['ChartType'] = request.chart_type
        query['DataSource'] = request.data_source
        query['Description'] = request.description
        query['Input'] = request.input
        query['OutputConfig'] = request.output_config
        query['Subtitle'] = request.subtitle
        query['Title'] = request.title
        query['Unit'] = request.unit
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicChartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitDynamicChartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_dynamic_chart_job(
        self,
        request: ice20201109_models.SubmitDynamicChartJobRequest,
    ) -> ice20201109_models.SubmitDynamicChartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_chart_job_with_options(request, runtime)

    async def submit_dynamic_chart_job_async(
        self,
        request: ice20201109_models.SubmitDynamicChartJobRequest,
    ) -> ice20201109_models.SubmitDynamicChartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_dynamic_chart_job_with_options_async(request, runtime)

    def submit_h2vjob_with_options(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitH2VJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitH2VJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_h2vjob_with_options_async(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitH2VJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitH2VJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_h2vjob(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_h2vjob_with_options(request, runtime)

    async def submit_h2vjob_async(
        self,
        request: ice20201109_models.SubmitH2VJobRequest,
    ) -> ice20201109_models.SubmitH2VJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_h2vjob_with_options_async(request, runtime)

    def submit_key_word_cut_job_with_options(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitKeyWordCutJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitKeyWordCutJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_key_word_cut_job_with_options_async(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitKeyWordCutJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitKeyWordCutJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_key_word_cut_job(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_key_word_cut_job_with_options(request, runtime)

    async def submit_key_word_cut_job_async(
        self,
        request: ice20201109_models.SubmitKeyWordCutJobRequest,
    ) -> ice20201109_models.SubmitKeyWordCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_key_word_cut_job_with_options_async(request, runtime)

    def submit_live_editing_job_with_options(
        self,
        request: ice20201109_models.SubmitLiveEditingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveEditingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Clips'] = request.clips
        query['LiveStreamConfig'] = request.live_stream_config
        query['MediaProduceConfig'] = request.media_produce_config
        query['OutputMediaConfig'] = request.output_media_config
        query['OutputMediaTarget'] = request.output_media_target
        query['ProjectId'] = request.project_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveEditingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_live_editing_job_with_options_async(
        self,
        request: ice20201109_models.SubmitLiveEditingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveEditingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Clips'] = request.clips
        query['LiveStreamConfig'] = request.live_stream_config
        query['MediaProduceConfig'] = request.media_produce_config
        query['OutputMediaConfig'] = request.output_media_config
        query['OutputMediaTarget'] = request.output_media_target
        query['ProjectId'] = request.project_id
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveEditingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitLiveEditingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_live_editing_job(
        self,
        request: ice20201109_models.SubmitLiveEditingJobRequest,
    ) -> ice20201109_models.SubmitLiveEditingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_live_editing_job_with_options(request, runtime)

    async def submit_live_editing_job_async(
        self,
        request: ice20201109_models.SubmitLiveEditingJobRequest,
    ) -> ice20201109_models.SubmitLiveEditingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_live_editing_job_with_options_async(request, runtime)

    def submit_matting_job_with_options(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMattingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMattingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_matting_job_with_options_async(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['InputFile'] = request.input_file
        query['InputType'] = request.input_type
        query['OutputConfig'] = request.output_config
        query['OutputMediaTarget'] = request.output_media_target
        query['Overwrite'] = request.overwrite
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMattingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMattingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_matting_job(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_matting_job_with_options(request, runtime)

    async def submit_matting_job_async(
        self,
        request: ice20201109_models.SubmitMattingJobRequest,
    ) -> ice20201109_models.SubmitMattingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_matting_job_with_options_async(request, runtime)

    def submit_media_producing_job_with_options(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ClipsParam'] = request.clips_param
        query['EditingProduceConfig'] = request.editing_produce_config
        query['OutputMediaConfig'] = request.output_media_config
        query['OutputMediaTarget'] = request.output_media_target
        query['ProjectId'] = request.project_id
        query['ProjectMetadata'] = request.project_metadata
        query['Source'] = request.source
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_producing_job_with_options_async(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ClipsParam'] = request.clips_param
        query['EditingProduceConfig'] = request.editing_produce_config
        query['OutputMediaConfig'] = request.output_media_config
        query['OutputMediaTarget'] = request.output_media_target
        query['ProjectId'] = request.project_id
        query['ProjectMetadata'] = request.project_metadata
        query['Source'] = request.source
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaProducingJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitMediaProducingJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_producing_job(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_producing_job_with_options(request, runtime)

    async def submit_media_producing_job_async(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_producing_job_with_options_async(request, runtime)

    def submit_pptcut_job_with_options(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPPTCutJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPPTCutJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_pptcut_job_with_options_async(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPPTCutJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitPPTCutJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_pptcut_job(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_pptcut_job_with_options(request, runtime)

    async def submit_pptcut_job_async(
        self,
        request: ice20201109_models.SubmitPPTCutJobRequest,
    ) -> ice20201109_models.SubmitPPTCutJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_pptcut_job_with_options_async(request, runtime)

    def submit_subtitle_produce_job_with_options(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['EditingConfig'] = request.editing_config
        query['InputConfig'] = request.input_config
        query['IsAsync'] = request.is_async
        query['OutputConfig'] = request.output_config
        query['Title'] = request.title
        query['Type'] = request.type
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSubtitleProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_subtitle_produce_job_with_options_async(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['EditingConfig'] = request.editing_config
        query['InputConfig'] = request.input_config
        query['IsAsync'] = request.is_async
        query['OutputConfig'] = request.output_config
        query['Title'] = request.title
        query['Type'] = request.type
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSubtitleProduceJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.SubmitSubtitleProduceJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_subtitle_produce_job(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_subtitle_produce_job_with_options(request, runtime)

    async def submit_subtitle_produce_job_async(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_subtitle_produce_job_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessStatus'] = request.business_status
        query['ClipsParam'] = request.clips_param
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['ProjectId'] = request.project_id
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_editing_project_with_options_async(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessStatus'] = request.business_status
        query['ClipsParam'] = request.clips_param
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['ProjectId'] = request.project_id
        query['TemplateId'] = request.template_id
        query['Timeline'] = request.timeline
        query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEditingProject',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateEditingProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_editing_project(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_editing_project_with_options(request, runtime)

    async def update_editing_project_async(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_editing_project_with_options_async(request, runtime)

    def update_media_info_with_options(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppendDynamicMeta'] = request.append_dynamic_meta
        query['AppendTags'] = request.append_tags
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['DynamicMetaDataList'] = request.dynamic_meta_data_list
        query['InputURL'] = request.input_url
        query['MediaId'] = request.media_id
        query['MediaTags'] = request.media_tags
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_media_info_with_options_async(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppendDynamicMeta'] = request.append_dynamic_meta
        query['AppendTags'] = request.append_tags
        query['BusinessType'] = request.business_type
        query['Category'] = request.category
        query['CoverURL'] = request.cover_url
        query['Description'] = request.description
        query['DynamicMetaDataList'] = request.dynamic_meta_data_list
        query['InputURL'] = request.input_url
        query['MediaId'] = request.media_id
        query['MediaTags'] = request.media_tags
        query['Title'] = request.title
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMediaInfo',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateMediaInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_media_info(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_media_info_with_options(request, runtime)

    async def update_media_info_async(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_media_info_with_options_async(request, runtime)

    def update_smart_job_with_options(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FEExtend'] = request.feextend
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateSmartJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_smart_job_with_options_async(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FEExtend'] = request.feextend
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSmartJob',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateSmartJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_smart_job(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_smart_job_with_options(request, runtime)

    async def update_smart_job_async(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_smart_job_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['CoverUrl'] = request.cover_url
        query['Name'] = request.name
        query['PreviewMedia'] = request.preview_media
        query['RelatedMediaids'] = request.related_mediaids
        query['Source'] = request.source
        query['Status'] = request.status
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Config'] = request.config
        query['CoverUrl'] = request.cover_url
        query['Name'] = request.name
        query['PreviewMedia'] = request.preview_media
        query['RelatedMediaids'] = request.related_mediaids
        query['Source'] = request.source
        query['Status'] = request.status
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ice20201109_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
    ) -> ice20201109_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: ice20201109_models.UpdateTemplateRequest,
    ) -> ice20201109_models.UpdateTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)
