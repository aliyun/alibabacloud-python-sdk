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
        self._signature_algorithm = 'v2'
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

    def add_category_with_options(
        self,
        request: ice20201109_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCategory',
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
            ice20201109_models.AddCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_category_with_options_async(
        self,
        request: ice20201109_models.AddCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCategory',
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
            ice20201109_models.AddCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_category(
        self,
        request: ice20201109_models.AddCategoryRequest,
    ) -> ice20201109_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_category_with_options(request, runtime)

    async def add_category_async(
        self,
        request: ice20201109_models.AddCategoryRequest,
    ) -> ice20201109_models.AddCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_category_with_options_async(request, runtime)

    def add_editing_project_materials_with_options(
        self,
        request: ice20201109_models.AddEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.AddEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.addition_type):
            query['AdditionType'] = request.addition_type
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.media_ids):
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

    def create_audit_with_options(
        self,
        request: ice20201109_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audit_content):
            query['AuditContent'] = request.audit_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAudit',
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
            ice20201109_models.CreateAuditResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_audit_with_options_async(
        self,
        request: ice20201109_models.CreateAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateAuditResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audit_content):
            query['AuditContent'] = request.audit_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAudit',
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
            ice20201109_models.CreateAuditResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_audit(
        self,
        request: ice20201109_models.CreateAuditRequest,
    ) -> ice20201109_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_audit_with_options(request, runtime)

    async def create_audit_async(
        self,
        request: ice20201109_models.CreateAuditRequest,
    ) -> ice20201109_models.CreateAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_audit_with_options_async(request, runtime)

    def create_custom_template_with_options(
        self,
        request: ice20201109_models.CreateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
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
            ice20201109_models.CreateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_custom_template_with_options_async(
        self,
        request: ice20201109_models.CreateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
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
            ice20201109_models.CreateCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_custom_template(
        self,
        request: ice20201109_models.CreateCustomTemplateRequest,
    ) -> ice20201109_models.CreateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_template_with_options(request, runtime)

    async def create_custom_template_async(
        self,
        request: ice20201109_models.CreateCustomTemplateRequest,
    ) -> ice20201109_models.CreateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_template_with_options_async(request, runtime)

    def create_editing_project_with_options(
        self,
        request: ice20201109_models.CreateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_config):
            query['BusinessConfig'] = request.business_config
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
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
        if not UtilClient.is_unset(request.business_config):
            query['BusinessConfig'] = request.business_config
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.material_maps):
            query['MaterialMaps'] = request.material_maps
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
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

    def create_live_record_template_with_options(
        self,
        tmp_req: ice20201109_models.CreateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRecordTemplate',
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
            ice20201109_models.CreateLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_record_template_with_options_async(
        self,
        tmp_req: ice20201109_models.CreateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveRecordTemplate',
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
            ice20201109_models.CreateLiveRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_record_template(
        self,
        request: ice20201109_models.CreateLiveRecordTemplateRequest,
    ) -> ice20201109_models.CreateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_record_template_with_options(request, runtime)

    async def create_live_record_template_async(
        self,
        request: ice20201109_models.CreateLiveRecordTemplateRequest,
    ) -> ice20201109_models.CreateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_record_template_with_options_async(request, runtime)

    def create_live_snapshot_template_with_options(
        self,
        request: ice20201109_models.CreateLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveSnapshotTemplate',
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
            ice20201109_models.CreateLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_snapshot_template_with_options_async(
        self,
        request: ice20201109_models.CreateLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLiveSnapshotTemplate',
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
            ice20201109_models.CreateLiveSnapshotTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_snapshot_template(
        self,
        request: ice20201109_models.CreateLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.CreateLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_snapshot_template_with_options(request, runtime)

    async def create_live_snapshot_template_async(
        self,
        request: ice20201109_models.CreateLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.CreateLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_snapshot_template_with_options_async(request, runtime)

    def create_live_transcode_template_with_options(
        self,
        tmp_req: ice20201109_models.CreateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
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
            ice20201109_models.CreateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_transcode_template_with_options_async(
        self,
        tmp_req: ice20201109_models.CreateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.CreateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
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
            ice20201109_models.CreateLiveTranscodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live_transcode_template(
        self,
        request: ice20201109_models.CreateLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.CreateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_live_transcode_template_with_options(request, runtime)

    async def create_live_transcode_template_async(
        self,
        request: ice20201109_models.CreateLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.CreateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_live_transcode_template_with_options_async(request, runtime)

    def create_pipeline_with_options(
        self,
        request: ice20201109_models.CreatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
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
            ice20201109_models.CreatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pipeline_with_options_async(
        self,
        request: ice20201109_models.CreatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreatePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePipeline',
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
            ice20201109_models.CreatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pipeline(
        self,
        request: ice20201109_models.CreatePipelineRequest,
    ) -> ice20201109_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_pipeline_with_options(request, runtime)

    async def create_pipeline_async(
        self,
        request: ice20201109_models.CreatePipelineRequest,
    ) -> ice20201109_models.CreatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_pipeline_with_options_async(request, runtime)

    def create_upload_media_with_options(
        self,
        request: ice20201109_models.CreateUploadMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateUploadMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.file_info):
            query['FileInfo'] = request.file_info
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadMedia',
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
            ice20201109_models.CreateUploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_media_with_options_async(
        self,
        request: ice20201109_models.CreateUploadMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateUploadMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.file_info):
            query['FileInfo'] = request.file_info
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadMedia',
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
            ice20201109_models.CreateUploadMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_media(
        self,
        request: ice20201109_models.CreateUploadMediaRequest,
    ) -> ice20201109_models.CreateUploadMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_media_with_options(request, runtime)

    async def create_upload_media_async(
        self,
        request: ice20201109_models.CreateUploadMediaRequest,
    ) -> ice20201109_models.CreateUploadMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_media_with_options_async(request, runtime)

    def create_upload_stream_with_options(
        self,
        request: ice20201109_models.CreateUploadStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateUploadStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not UtilClient.is_unset(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadStream',
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
            ice20201109_models.CreateUploadStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_upload_stream_with_options_async(
        self,
        request: ice20201109_models.CreateUploadStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.CreateUploadStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not UtilClient.is_unset(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUploadStream',
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
            ice20201109_models.CreateUploadStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_upload_stream(
        self,
        request: ice20201109_models.CreateUploadStreamRequest,
    ) -> ice20201109_models.CreateUploadStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_upload_stream_with_options(request, runtime)

    async def create_upload_stream_async(
        self,
        request: ice20201109_models.CreateUploadStreamRequest,
    ) -> ice20201109_models.CreateUploadStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_upload_stream_with_options_async(request, runtime)

    def delete_category_with_options(
        self,
        request: ice20201109_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
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
            ice20201109_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_category_with_options_async(
        self,
        request: ice20201109_models.DeleteCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
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
            ice20201109_models.DeleteCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_category(
        self,
        request: ice20201109_models.DeleteCategoryRequest,
    ) -> ice20201109_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    async def delete_category_async(
        self,
        request: ice20201109_models.DeleteCategoryRequest,
    ) -> ice20201109_models.DeleteCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_category_with_options_async(request, runtime)

    def delete_custom_template_with_options(
        self,
        request: ice20201109_models.DeleteCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
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
            ice20201109_models.DeleteCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_template_with_options_async(
        self,
        request: ice20201109_models.DeleteCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
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
            ice20201109_models.DeleteCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_template(
        self,
        request: ice20201109_models.DeleteCustomTemplateRequest,
    ) -> ice20201109_models.DeleteCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_template_with_options(request, runtime)

    async def delete_custom_template_async(
        self,
        request: ice20201109_models.DeleteCustomTemplateRequest,
    ) -> ice20201109_models.DeleteCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_custom_template_with_options_async(request, runtime)

    def delete_editing_project_materials_with_options(
        self,
        request: ice20201109_models.DeleteEditingProjectMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteEditingProjectMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.material_ids):
            query['MaterialIds'] = request.material_ids
        if not UtilClient.is_unset(request.material_type):
            query['MaterialType'] = request.material_type
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.project_ids):
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
        if not UtilClient.is_unset(request.project_ids):
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

    def delete_live_record_files_with_options(
        self,
        request: ice20201109_models.DeleteLiveRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveRecordFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_ids):
            query['RecordIds'] = request.record_ids
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordFiles',
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
            ice20201109_models.DeleteLiveRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_record_files_with_options_async(
        self,
        request: ice20201109_models.DeleteLiveRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveRecordFilesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_ids):
            query['RecordIds'] = request.record_ids
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordFiles',
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
            ice20201109_models.DeleteLiveRecordFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_record_files(
        self,
        request: ice20201109_models.DeleteLiveRecordFilesRequest,
    ) -> ice20201109_models.DeleteLiveRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_files_with_options(request, runtime)

    async def delete_live_record_files_async(
        self,
        request: ice20201109_models.DeleteLiveRecordFilesRequest,
    ) -> ice20201109_models.DeleteLiveRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_record_files_with_options_async(request, runtime)

    def delete_live_record_template_with_options(
        self,
        request: ice20201109_models.DeleteLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordTemplate',
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
            ice20201109_models.DeleteLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_record_template_with_options_async(
        self,
        request: ice20201109_models.DeleteLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordTemplate',
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
            ice20201109_models.DeleteLiveRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_record_template(
        self,
        request: ice20201109_models.DeleteLiveRecordTemplateRequest,
    ) -> ice20201109_models.DeleteLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_template_with_options(request, runtime)

    async def delete_live_record_template_async(
        self,
        request: ice20201109_models.DeleteLiveRecordTemplateRequest,
    ) -> ice20201109_models.DeleteLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_record_template_with_options_async(request, runtime)

    def delete_live_snapshot_files_with_options(
        self,
        tmp_req: ice20201109_models.DeleteLiveSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveSnapshotFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DeleteLiveSnapshotFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_timestamp_list):
            request.create_timestamp_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_timestamp_list, 'CreateTimestampList', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_timestamp_list_shrink):
            query['CreateTimestampList'] = request.create_timestamp_list_shrink
        if not UtilClient.is_unset(request.delete_original_file):
            query['DeleteOriginalFile'] = request.delete_original_file
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotFiles',
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
            ice20201109_models.DeleteLiveSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_snapshot_files_with_options_async(
        self,
        tmp_req: ice20201109_models.DeleteLiveSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveSnapshotFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DeleteLiveSnapshotFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_timestamp_list):
            request.create_timestamp_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_timestamp_list, 'CreateTimestampList', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_timestamp_list_shrink):
            query['CreateTimestampList'] = request.create_timestamp_list_shrink
        if not UtilClient.is_unset(request.delete_original_file):
            query['DeleteOriginalFile'] = request.delete_original_file
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotFiles',
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
            ice20201109_models.DeleteLiveSnapshotFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_snapshot_files(
        self,
        request: ice20201109_models.DeleteLiveSnapshotFilesRequest,
    ) -> ice20201109_models.DeleteLiveSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_files_with_options(request, runtime)

    async def delete_live_snapshot_files_async(
        self,
        request: ice20201109_models.DeleteLiveSnapshotFilesRequest,
    ) -> ice20201109_models.DeleteLiveSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_snapshot_files_with_options_async(request, runtime)

    def delete_live_snapshot_template_with_options(
        self,
        request: ice20201109_models.DeleteLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotTemplate',
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
            ice20201109_models.DeleteLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_snapshot_template_with_options_async(
        self,
        request: ice20201109_models.DeleteLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotTemplate',
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
            ice20201109_models.DeleteLiveSnapshotTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_snapshot_template(
        self,
        request: ice20201109_models.DeleteLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.DeleteLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_template_with_options(request, runtime)

    async def delete_live_snapshot_template_async(
        self,
        request: ice20201109_models.DeleteLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.DeleteLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_snapshot_template_with_options_async(request, runtime)

    def delete_live_transcode_job_with_options(
        self,
        request: ice20201109_models.DeleteLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeJob',
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
            ice20201109_models.DeleteLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_transcode_job_with_options_async(
        self,
        request: ice20201109_models.DeleteLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeJob',
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
            ice20201109_models.DeleteLiveTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_transcode_job(
        self,
        request: ice20201109_models.DeleteLiveTranscodeJobRequest,
    ) -> ice20201109_models.DeleteLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_transcode_job_with_options(request, runtime)

    async def delete_live_transcode_job_async(
        self,
        request: ice20201109_models.DeleteLiveTranscodeJobRequest,
    ) -> ice20201109_models.DeleteLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_transcode_job_with_options_async(request, runtime)

    def delete_live_transcode_template_with_options(
        self,
        request: ice20201109_models.DeleteLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeTemplate',
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
            ice20201109_models.DeleteLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_transcode_template_with_options_async(
        self,
        request: ice20201109_models.DeleteLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveTranscodeTemplate',
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
            ice20201109_models.DeleteLiveTranscodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live_transcode_template(
        self,
        request: ice20201109_models.DeleteLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.DeleteLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_live_transcode_template_with_options(request, runtime)

    async def delete_live_transcode_template_async(
        self,
        request: ice20201109_models.DeleteLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.DeleteLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_live_transcode_template_with_options_async(request, runtime)

    def delete_media_infos_with_options(
        self,
        request: ice20201109_models.DeleteMediaInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteMediaInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not UtilClient.is_unset(request.media_ids):
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
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.input_urls):
            query['InputURLs'] = request.input_urls
        if not UtilClient.is_unset(request.media_ids):
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

    def delete_pipeline_with_options(
        self,
        request: ice20201109_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeletePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
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
            ice20201109_models.DeletePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pipeline_with_options_async(
        self,
        request: ice20201109_models.DeletePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeletePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePipeline',
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
            ice20201109_models.DeletePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pipeline(
        self,
        request: ice20201109_models.DeletePipelineRequest,
    ) -> ice20201109_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_pipeline_with_options(request, runtime)

    async def delete_pipeline_async(
        self,
        request: ice20201109_models.DeletePipelineRequest,
    ) -> ice20201109_models.DeletePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_pipeline_with_options_async(request, runtime)

    def delete_play_info_with_options(
        self,
        request: ice20201109_models.DeletePlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeletePlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlayInfo',
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
            ice20201109_models.DeletePlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_play_info_with_options_async(
        self,
        request: ice20201109_models.DeletePlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeletePlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_physical_files):
            query['DeletePhysicalFiles'] = request.delete_physical_files
        if not UtilClient.is_unset(request.file_urls):
            query['FileURLs'] = request.file_urls
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlayInfo',
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
            ice20201109_models.DeletePlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_play_info(
        self,
        request: ice20201109_models.DeletePlayInfoRequest,
    ) -> ice20201109_models.DeletePlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_play_info_with_options(request, runtime)

    async def delete_play_info_async(
        self,
        request: ice20201109_models.DeletePlayInfoRequest,
    ) -> ice20201109_models.DeletePlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_play_info_with_options_async(request, runtime)

    def delete_smart_job_with_options(
        self,
        request: ice20201109_models.DeleteSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DeleteSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
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
        if not UtilClient.is_unset(request.job_id):
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

    def describe_filter_configs_with_options(
        self,
        request: ice20201109_models.DescribeFilterConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeFilterConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFilterConfigs',
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
            ice20201109_models.DescribeFilterConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_filter_configs_with_options_async(
        self,
        request: ice20201109_models.DescribeFilterConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeFilterConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFilterConfigs',
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
            ice20201109_models.DescribeFilterConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_filter_configs(
        self,
        request: ice20201109_models.DescribeFilterConfigsRequest,
    ) -> ice20201109_models.DescribeFilterConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_filter_configs_with_options(request, runtime)

    async def describe_filter_configs_async(
        self,
        request: ice20201109_models.DescribeFilterConfigsRequest,
    ) -> ice20201109_models.DescribeFilterConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_filter_configs_with_options_async(request, runtime)

    def describe_meter_ice_edit_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterIceEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceEditUsage',
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
            ice20201109_models.DescribeMeterIceEditUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ice_edit_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterIceEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceEditUsage',
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
            ice20201109_models.DescribeMeterIceEditUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ice_edit_usage(
        self,
        request: ice20201109_models.DescribeMeterIceEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ice_edit_usage_with_options(request, runtime)

    async def describe_meter_ice_edit_usage_async(
        self,
        request: ice20201109_models.DescribeMeterIceEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ice_edit_usage_with_options_async(request, runtime)

    def describe_meter_ice_live_media_convert_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterIceLiveMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceLiveMediaConvertUsage',
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
            ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ice_live_media_convert_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterIceLiveMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceLiveMediaConvertUsage',
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
            ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ice_live_media_convert_usage(
        self,
        request: ice20201109_models.DescribeMeterIceLiveMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ice_live_media_convert_usage_with_options(request, runtime)

    async def describe_meter_ice_live_media_convert_usage_async(
        self,
        request: ice20201109_models.DescribeMeterIceLiveMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceLiveMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ice_live_media_convert_usage_with_options_async(request, runtime)

    def describe_meter_ice_media_convert_uhdusage_with_options(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUHDUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMediaConvertUHDUsage',
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
            ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ice_media_convert_uhdusage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUHDUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMediaConvertUHDUsage',
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
            ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ice_media_convert_uhdusage(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUHDUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ice_media_convert_uhdusage_with_options(request, runtime)

    async def describe_meter_ice_media_convert_uhdusage_async(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUHDUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUHDUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ice_media_convert_uhdusage_with_options_async(request, runtime)

    def describe_meter_ice_media_convert_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMediaConvertUsage',
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
            ice20201109_models.DescribeMeterIceMediaConvertUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ice_media_convert_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMediaConvertUsage',
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
            ice20201109_models.DescribeMeterIceMediaConvertUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ice_media_convert_usage(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ice_media_convert_usage_with_options(request, runtime)

    async def describe_meter_ice_media_convert_usage_async(
        self,
        request: ice20201109_models.DescribeMeterIceMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ice_media_convert_usage_with_options_async(request, runtime)

    def describe_meter_ice_mps_ai_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterIceMpsAiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMpsAiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMpsAiUsage',
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
            ice20201109_models.DescribeMeterIceMpsAiUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ice_mps_ai_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterIceMpsAiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterIceMpsAiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterIceMpsAiUsage',
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
            ice20201109_models.DescribeMeterIceMpsAiUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ice_mps_ai_usage(
        self,
        request: ice20201109_models.DescribeMeterIceMpsAiUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMpsAiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ice_mps_ai_usage_with_options(request, runtime)

    async def describe_meter_ice_mps_ai_usage_async(
        self,
        request: ice20201109_models.DescribeMeterIceMpsAiUsageRequest,
    ) -> ice20201109_models.DescribeMeterIceMpsAiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ice_mps_ai_usage_with_options_async(request, runtime)

    def describe_meter_ims_edit_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsEditUsage',
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
            ice20201109_models.DescribeMeterImsEditUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_edit_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsEditUsage',
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
            ice20201109_models.DescribeMeterImsEditUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_edit_usage(
        self,
        request: ice20201109_models.DescribeMeterImsEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_edit_usage_with_options(request, runtime)

    async def describe_meter_ims_edit_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_edit_usage_with_options_async(request, runtime)

    def describe_meter_ims_live_edit_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsLiveEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveEditUsage',
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
            ice20201109_models.DescribeMeterImsLiveEditUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_live_edit_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveEditUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveEditUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveEditUsage',
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
            ice20201109_models.DescribeMeterImsLiveEditUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_live_edit_usage(
        self,
        request: ice20201109_models.DescribeMeterImsLiveEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_live_edit_usage_with_options(request, runtime)

    async def describe_meter_ims_live_edit_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveEditUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveEditUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_live_edit_usage_with_options_async(request, runtime)

    def describe_meter_ims_live_media_convert_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsLiveMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveMediaConvertUsage',
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
            ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_live_media_convert_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveMediaConvertUsage',
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
            ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_live_media_convert_usage(
        self,
        request: ice20201109_models.DescribeMeterImsLiveMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_live_media_convert_usage_with_options(request, runtime)

    async def describe_meter_ims_live_media_convert_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_live_media_convert_usage_with_options_async(request, runtime)

    def describe_meter_ims_live_record_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsLiveRecordUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveRecordUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveRecordUsage',
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
            ice20201109_models.DescribeMeterImsLiveRecordUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_live_record_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveRecordUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveRecordUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveRecordUsage',
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
            ice20201109_models.DescribeMeterImsLiveRecordUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_live_record_usage(
        self,
        request: ice20201109_models.DescribeMeterImsLiveRecordUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveRecordUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_live_record_usage_with_options(request, runtime)

    async def describe_meter_ims_live_record_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveRecordUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveRecordUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_live_record_usage_with_options_async(request, runtime)

    def describe_meter_ims_live_snapshot_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsLiveSnapshotUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveSnapshotUsage',
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
            ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_live_snapshot_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveSnapshotUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsLiveSnapshotUsage',
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
            ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_live_snapshot_usage(
        self,
        request: ice20201109_models.DescribeMeterImsLiveSnapshotUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_live_snapshot_usage_with_options(request, runtime)

    async def describe_meter_ims_live_snapshot_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsLiveSnapshotUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsLiveSnapshotUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_live_snapshot_usage_with_options_async(request, runtime)

    def describe_meter_ims_media_convert_uhdusage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUHDUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUHDUsage',
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
            ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_media_convert_uhdusage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUHDUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUHDUsage',
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
            ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_media_convert_uhdusage(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUHDUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_media_convert_uhdusage_with_options(request, runtime)

    async def describe_meter_ims_media_convert_uhdusage_async(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUHDUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUHDUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_media_convert_uhdusage_with_options_async(request, runtime)

    def describe_meter_ims_media_convert_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUsage',
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
            ice20201109_models.DescribeMeterImsMediaConvertUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_media_convert_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMediaConvertUsage',
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
            ice20201109_models.DescribeMeterImsMediaConvertUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_media_convert_usage(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_media_convert_usage_with_options(request, runtime)

    async def describe_meter_ims_media_convert_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsMediaConvertUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMediaConvertUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_media_convert_usage_with_options_async(request, runtime)

    def describe_meter_ims_mps_ai_usage_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsMpsAiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMpsAiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMpsAiUsage',
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
            ice20201109_models.DescribeMeterImsMpsAiUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_mps_ai_usage_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsMpsAiUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsMpsAiUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsMpsAiUsage',
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
            ice20201109_models.DescribeMeterImsMpsAiUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_mps_ai_usage(
        self,
        request: ice20201109_models.DescribeMeterImsMpsAiUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMpsAiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_mps_ai_usage_with_options(request, runtime)

    async def describe_meter_ims_mps_ai_usage_async(
        self,
        request: ice20201109_models.DescribeMeterImsMpsAiUsageRequest,
    ) -> ice20201109_models.DescribeMeterImsMpsAiUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_mps_ai_usage_with_options_async(request, runtime)

    def describe_meter_ims_summary_with_options(
        self,
        request: ice20201109_models.DescribeMeterImsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsSummary',
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
            ice20201109_models.DescribeMeterImsSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meter_ims_summary_with_options_async(
        self,
        request: ice20201109_models.DescribeMeterImsSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeMeterImsSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterImsSummary',
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
            ice20201109_models.DescribeMeterImsSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_meter_ims_summary(
        self,
        request: ice20201109_models.DescribeMeterImsSummaryRequest,
    ) -> ice20201109_models.DescribeMeterImsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_ims_summary_with_options(request, runtime)

    async def describe_meter_ims_summary_async(
        self,
        request: ice20201109_models.DescribeMeterImsSummaryRequest,
    ) -> ice20201109_models.DescribeMeterImsSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meter_ims_summary_with_options_async(request, runtime)

    def describe_play_detail_with_options(
        self,
        request: ice20201109_models.DescribePlayDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.play_ts):
            query['PlayTs'] = request.play_ts
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayDetail',
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
            ice20201109_models.DescribePlayDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_detail_with_options_async(
        self,
        request: ice20201109_models.DescribePlayDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.play_ts):
            query['PlayTs'] = request.play_ts
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayDetail',
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
            ice20201109_models.DescribePlayDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_detail(
        self,
        request: ice20201109_models.DescribePlayDetailRequest,
    ) -> ice20201109_models.DescribePlayDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_detail_with_options(request, runtime)

    async def describe_play_detail_async(
        self,
        request: ice20201109_models.DescribePlayDetailRequest,
    ) -> ice20201109_models.DescribePlayDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_detail_with_options_async(request, runtime)

    def describe_play_event_list_with_options(
        self,
        request: ice20201109_models.DescribePlayEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_ts):
            query['PlayTs'] = request.play_ts
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayEventList',
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
            ice20201109_models.DescribePlayEventListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_event_list_with_options_async(
        self,
        request: ice20201109_models.DescribePlayEventListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayEventListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_ts):
            query['PlayTs'] = request.play_ts
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayEventList',
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
            ice20201109_models.DescribePlayEventListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_event_list(
        self,
        request: ice20201109_models.DescribePlayEventListRequest,
    ) -> ice20201109_models.DescribePlayEventListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_event_list_with_options(request, runtime)

    async def describe_play_event_list_async(
        self,
        request: ice20201109_models.DescribePlayEventListRequest,
    ) -> ice20201109_models.DescribePlayEventListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_event_list_with_options_async(request, runtime)

    def describe_play_first_frame_duration_metric_data_with_options(
        self,
        request: ice20201109_models.DescribePlayFirstFrameDurationMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayFirstFrameDurationMetricData',
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
            ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_first_frame_duration_metric_data_with_options_async(
        self,
        request: ice20201109_models.DescribePlayFirstFrameDurationMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayFirstFrameDurationMetricData',
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
            ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_first_frame_duration_metric_data(
        self,
        request: ice20201109_models.DescribePlayFirstFrameDurationMetricDataRequest,
    ) -> ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_first_frame_duration_metric_data_with_options(request, runtime)

    async def describe_play_first_frame_duration_metric_data_async(
        self,
        request: ice20201109_models.DescribePlayFirstFrameDurationMetricDataRequest,
    ) -> ice20201109_models.DescribePlayFirstFrameDurationMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_first_frame_duration_metric_data_with_options_async(request, runtime)

    def describe_play_list_with_options(
        self,
        request: ice20201109_models.DescribePlayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayList',
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
            ice20201109_models.DescribePlayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_list_with_options_async(
        self,
        request: ice20201109_models.DescribePlayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.play_type):
            query['PlayType'] = request.play_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayList',
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
            ice20201109_models.DescribePlayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_list(
        self,
        request: ice20201109_models.DescribePlayListRequest,
    ) -> ice20201109_models.DescribePlayListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_list_with_options(request, runtime)

    async def describe_play_list_async(
        self,
        request: ice20201109_models.DescribePlayListRequest,
    ) -> ice20201109_models.DescribePlayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_list_with_options_async(request, runtime)

    def describe_play_metric_data_with_options(
        self,
        request: ice20201109_models.DescribePlayMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.experience_level):
            query['ExperienceLevel'] = request.experience_level
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.sdk_version):
            query['SdkVersion'] = request.sdk_version
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayMetricData',
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
            ice20201109_models.DescribePlayMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_metric_data_with_options_async(
        self,
        request: ice20201109_models.DescribePlayMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayMetricDataResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.experience_level):
            query['ExperienceLevel'] = request.experience_level
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.sdk_version):
            query['SdkVersion'] = request.sdk_version
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayMetricData',
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
            ice20201109_models.DescribePlayMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_metric_data(
        self,
        request: ice20201109_models.DescribePlayMetricDataRequest,
    ) -> ice20201109_models.DescribePlayMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_metric_data_with_options(request, runtime)

    async def describe_play_metric_data_async(
        self,
        request: ice20201109_models.DescribePlayMetricDataRequest,
    ) -> ice20201109_models.DescribePlayMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_metric_data_with_options_async(request, runtime)

    def describe_play_qoe_list_with_options(
        self,
        tmp_req: ice20201109_models.DescribePlayQoeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayQoeListResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DescribePlayQoeListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_types):
            request.metric_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_types, 'MetricTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_types_shrink):
            query['MetricTypes'] = request.metric_types_shrink
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayQoeList',
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
            ice20201109_models.DescribePlayQoeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_qoe_list_with_options_async(
        self,
        tmp_req: ice20201109_models.DescribePlayQoeListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayQoeListResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DescribePlayQoeListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_types):
            request.metric_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_types, 'MetricTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_types_shrink):
            query['MetricTypes'] = request.metric_types_shrink
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayQoeList',
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
            ice20201109_models.DescribePlayQoeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_qoe_list(
        self,
        request: ice20201109_models.DescribePlayQoeListRequest,
    ) -> ice20201109_models.DescribePlayQoeListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_qoe_list_with_options(request, runtime)

    async def describe_play_qoe_list_async(
        self,
        request: ice20201109_models.DescribePlayQoeListRequest,
    ) -> ice20201109_models.DescribePlayQoeListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_qoe_list_with_options_async(request, runtime)

    def describe_play_qos_list_with_options(
        self,
        tmp_req: ice20201109_models.DescribePlayQosListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayQosListResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DescribePlayQosListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_types):
            request.metric_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_types, 'MetricTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_types_shrink):
            query['MetricTypes'] = request.metric_types_shrink
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayQosList',
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
            ice20201109_models.DescribePlayQosListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_play_qos_list_with_options_async(
        self,
        tmp_req: ice20201109_models.DescribePlayQosListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribePlayQosListResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.DescribePlayQosListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.metric_types):
            request.metric_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.metric_types, 'MetricTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.begin_ts):
            query['BeginTs'] = request.begin_ts
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.item_configs):
            query['ItemConfigs'] = request.item_configs
        if not UtilClient.is_unset(request.metric_types_shrink):
            query['MetricTypes'] = request.metric_types_shrink
        if not UtilClient.is_unset(request.network):
            query['Network'] = request.network
        if not UtilClient.is_unset(request.order_name):
            query['OrderName'] = request.order_name
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.os):
            query['Os'] = request.os
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.terminal_type):
            query['TerminalType'] = request.terminal_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePlayQosList',
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
            ice20201109_models.DescribePlayQosListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_play_qos_list(
        self,
        request: ice20201109_models.DescribePlayQosListRequest,
    ) -> ice20201109_models.DescribePlayQosListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_play_qos_list_with_options(request, runtime)

    async def describe_play_qos_list_async(
        self,
        request: ice20201109_models.DescribePlayQosListRequest,
    ) -> ice20201109_models.DescribePlayQosListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_play_qos_list_with_options_async(request, runtime)

    def describe_query_configs_with_options(
        self,
        request: ice20201109_models.DescribeQueryConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeQueryConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQueryConfigs',
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
            ice20201109_models.DescribeQueryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_query_configs_with_options_async(
        self,
        request: ice20201109_models.DescribeQueryConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.DescribeQueryConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQueryConfigs',
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
            ice20201109_models.DescribeQueryConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_query_configs(
        self,
        request: ice20201109_models.DescribeQueryConfigsRequest,
    ) -> ice20201109_models.DescribeQueryConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_query_configs_with_options(request, runtime)

    async def describe_query_configs_async(
        self,
        request: ice20201109_models.DescribeQueryConfigsRequest,
    ) -> ice20201109_models.DescribeQueryConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_query_configs_with_options_async(request, runtime)

    def get_categories_with_options(
        self,
        request: ice20201109_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategories',
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
            ice20201109_models.GetCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_categories_with_options_async(
        self,
        request: ice20201109_models.GetCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetCategoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCategories',
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
            ice20201109_models.GetCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_categories(
        self,
        request: ice20201109_models.GetCategoriesRequest,
    ) -> ice20201109_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_categories_with_options(request, runtime)

    async def get_categories_async(
        self,
        request: ice20201109_models.GetCategoriesRequest,
    ) -> ice20201109_models.GetCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_categories_with_options_async(request, runtime)

    def get_custom_template_with_options(
        self,
        request: ice20201109_models.GetCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
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
            ice20201109_models.GetCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_custom_template_with_options_async(
        self,
        request: ice20201109_models.GetCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
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
            ice20201109_models.GetCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_custom_template(
        self,
        request: ice20201109_models.GetCustomTemplateRequest,
    ) -> ice20201109_models.GetCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_custom_template_with_options(request, runtime)

    async def get_custom_template_async(
        self,
        request: ice20201109_models.GetCustomTemplateRequest,
    ) -> ice20201109_models.GetCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_custom_template_with_options_async(request, runtime)

    def get_default_storage_location_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
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
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDefaultStorageLocationResponse:
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

    def get_default_storage_location(self) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_default_storage_location_with_options(runtime)

    async def get_default_storage_location_async(self) -> ice20201109_models.GetDefaultStorageLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_default_storage_location_with_options_async(runtime)

    def get_dynamic_image_job_with_options(
        self,
        request: ice20201109_models.GetDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDynamicImageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicImageJob',
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
            ice20201109_models.GetDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dynamic_image_job_with_options_async(
        self,
        request: ice20201109_models.GetDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetDynamicImageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDynamicImageJob',
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
            ice20201109_models.GetDynamicImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dynamic_image_job(
        self,
        request: ice20201109_models.GetDynamicImageJobRequest,
    ) -> ice20201109_models.GetDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dynamic_image_job_with_options(request, runtime)

    async def get_dynamic_image_job_async(
        self,
        request: ice20201109_models.GetDynamicImageJobRequest,
    ) -> ice20201109_models.GetDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dynamic_image_job_with_options_async(request, runtime)

    def get_editing_project_with_options(
        self,
        request: ice20201109_models.GetEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.project_id):
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
        if not UtilClient.is_unset(request.project_id):
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
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
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
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetEventCallbackResponse:
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

    def get_event_callback(self) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_event_callback_with_options(runtime)

    async def get_event_callback_async(self) -> ice20201109_models.GetEventCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_event_callback_with_options_async(runtime)

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
        if not UtilClient.is_unset(request.job_id):
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
        if not UtilClient.is_unset(request.job_id):
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

    def get_live_record_job_with_options(
        self,
        request: ice20201109_models.GetLiveRecordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveRecordJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordJob',
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
            ice20201109_models.GetLiveRecordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_record_job_with_options_async(
        self,
        request: ice20201109_models.GetLiveRecordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveRecordJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordJob',
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
            ice20201109_models.GetLiveRecordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_record_job(
        self,
        request: ice20201109_models.GetLiveRecordJobRequest,
    ) -> ice20201109_models.GetLiveRecordJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_job_with_options(request, runtime)

    async def get_live_record_job_async(
        self,
        request: ice20201109_models.GetLiveRecordJobRequest,
    ) -> ice20201109_models.GetLiveRecordJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_record_job_with_options_async(request, runtime)

    def get_live_record_template_with_options(
        self,
        request: ice20201109_models.GetLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordTemplate',
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
            ice20201109_models.GetLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_record_template_with_options_async(
        self,
        request: ice20201109_models.GetLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveRecordTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveRecordTemplate',
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
            ice20201109_models.GetLiveRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_record_template(
        self,
        request: ice20201109_models.GetLiveRecordTemplateRequest,
    ) -> ice20201109_models.GetLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_record_template_with_options(request, runtime)

    async def get_live_record_template_async(
        self,
        request: ice20201109_models.GetLiveRecordTemplateRequest,
    ) -> ice20201109_models.GetLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_record_template_with_options_async(request, runtime)

    def get_live_snapshot_job_with_options(
        self,
        request: ice20201109_models.GetLiveSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotJob',
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
            ice20201109_models.GetLiveSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_snapshot_job_with_options_async(
        self,
        request: ice20201109_models.GetLiveSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotJob',
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
            ice20201109_models.GetLiveSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_snapshot_job(
        self,
        request: ice20201109_models.GetLiveSnapshotJobRequest,
    ) -> ice20201109_models.GetLiveSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_snapshot_job_with_options(request, runtime)

    async def get_live_snapshot_job_async(
        self,
        request: ice20201109_models.GetLiveSnapshotJobRequest,
    ) -> ice20201109_models.GetLiveSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_snapshot_job_with_options_async(request, runtime)

    def get_live_snapshot_template_with_options(
        self,
        request: ice20201109_models.GetLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotTemplate',
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
            ice20201109_models.GetLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_snapshot_template_with_options_async(
        self,
        request: ice20201109_models.GetLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveSnapshotTemplate',
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
            ice20201109_models.GetLiveSnapshotTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_snapshot_template(
        self,
        request: ice20201109_models.GetLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.GetLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_snapshot_template_with_options(request, runtime)

    async def get_live_snapshot_template_async(
        self,
        request: ice20201109_models.GetLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.GetLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_snapshot_template_with_options_async(request, runtime)

    def get_live_transcode_job_with_options(
        self,
        request: ice20201109_models.GetLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeJob',
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
            ice20201109_models.GetLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_transcode_job_with_options_async(
        self,
        request: ice20201109_models.GetLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeJob',
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
            ice20201109_models.GetLiveTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_transcode_job(
        self,
        request: ice20201109_models.GetLiveTranscodeJobRequest,
    ) -> ice20201109_models.GetLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_transcode_job_with_options(request, runtime)

    async def get_live_transcode_job_async(
        self,
        request: ice20201109_models.GetLiveTranscodeJobRequest,
    ) -> ice20201109_models.GetLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_transcode_job_with_options_async(request, runtime)

    def get_live_transcode_template_with_options(
        self,
        request: ice20201109_models.GetLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeTemplate',
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
            ice20201109_models.GetLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_transcode_template_with_options_async(
        self,
        request: ice20201109_models.GetLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetLiveTranscodeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLiveTranscodeTemplate',
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
            ice20201109_models.GetLiveTranscodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_transcode_template(
        self,
        request: ice20201109_models.GetLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.GetLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_live_transcode_template_with_options(request, runtime)

    async def get_live_transcode_template_async(
        self,
        request: ice20201109_models.GetLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.GetLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_live_transcode_template_with_options_async(request, runtime)

    def get_media_info_with_options(
        self,
        request: ice20201109_models.GetMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output_type):
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
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.output_type):
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

    def get_media_info_job_with_options(
        self,
        request: ice20201109_models.GetMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfoJob',
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
            ice20201109_models.GetMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_info_job_with_options_async(
        self,
        request: ice20201109_models.GetMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetMediaInfoJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMediaInfoJob',
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
            ice20201109_models.GetMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_info_job(
        self,
        request: ice20201109_models.GetMediaInfoJobRequest,
    ) -> ice20201109_models.GetMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_info_job_with_options(request, runtime)

    async def get_media_info_job_async(
        self,
        request: ice20201109_models.GetMediaInfoJobRequest,
    ) -> ice20201109_models.GetMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_info_job_with_options_async(request, runtime)

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

    def get_package_job_with_options(
        self,
        request: ice20201109_models.GetPackageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPackageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackageJob',
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
            ice20201109_models.GetPackageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_package_job_with_options_async(
        self,
        request: ice20201109_models.GetPackageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPackageJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPackageJob',
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
            ice20201109_models.GetPackageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_package_job(
        self,
        request: ice20201109_models.GetPackageJobRequest,
    ) -> ice20201109_models.GetPackageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_package_job_with_options(request, runtime)

    async def get_package_job_async(
        self,
        request: ice20201109_models.GetPackageJobRequest,
    ) -> ice20201109_models.GetPackageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_package_job_with_options_async(request, runtime)

    def get_pipeline_with_options(
        self,
        request: ice20201109_models.GetPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipeline',
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
            ice20201109_models.GetPipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pipeline_with_options_async(
        self,
        request: ice20201109_models.GetPipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPipeline',
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
            ice20201109_models.GetPipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pipeline(
        self,
        request: ice20201109_models.GetPipelineRequest,
    ) -> ice20201109_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_pipeline_with_options(request, runtime)

    async def get_pipeline_async(
        self,
        request: ice20201109_models.GetPipelineRequest,
    ) -> ice20201109_models.GetPipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_pipeline_with_options_async(request, runtime)

    def get_play_info_with_options(
        self,
        request: ice20201109_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPlayInfo',
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
            ice20201109_models.GetPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_play_info_with_options_async(
        self,
        request: ice20201109_models.GetPlayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPlayInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPlayInfo',
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
            ice20201109_models.GetPlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_play_info(
        self,
        request: ice20201109_models.GetPlayInfoRequest,
    ) -> ice20201109_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_play_info_with_options(request, runtime)

    async def get_play_info_async(
        self,
        request: ice20201109_models.GetPlayInfoRequest,
    ) -> ice20201109_models.GetPlayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_play_info_with_options_async(request, runtime)

    def get_public_media_info_with_options(
        self,
        request: ice20201109_models.GetPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
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
        if not UtilClient.is_unset(request.media_id):
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

    def get_snapshot_job_with_options(
        self,
        request: ice20201109_models.GetSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotJob',
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
            ice20201109_models.GetSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_snapshot_job_with_options_async(
        self,
        request: ice20201109_models.GetSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSnapshotJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotJob',
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
            ice20201109_models.GetSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_snapshot_job(
        self,
        request: ice20201109_models.GetSnapshotJobRequest,
    ) -> ice20201109_models.GetSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_snapshot_job_with_options(request, runtime)

    async def get_snapshot_job_async(
        self,
        request: ice20201109_models.GetSnapshotJobRequest,
    ) -> ice20201109_models.GetSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_snapshot_job_with_options_async(request, runtime)

    def get_snapshot_urls_with_options(
        self,
        request: ice20201109_models.GetSnapshotUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSnapshotUrlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotUrls',
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
            ice20201109_models.GetSnapshotUrlsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_snapshot_urls_with_options_async(
        self,
        request: ice20201109_models.GetSnapshotUrlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSnapshotUrlsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSnapshotUrls',
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
            ice20201109_models.GetSnapshotUrlsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_snapshot_urls(
        self,
        request: ice20201109_models.GetSnapshotUrlsRequest,
    ) -> ice20201109_models.GetSnapshotUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_snapshot_urls_with_options(request, runtime)

    async def get_snapshot_urls_async(
        self,
        request: ice20201109_models.GetSnapshotUrlsRequest,
    ) -> ice20201109_models.GetSnapshotUrlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_snapshot_urls_with_options_async(request, runtime)

    def get_system_template_with_options(
        self,
        request: ice20201109_models.GetSystemTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSystemTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSystemTemplate',
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
            ice20201109_models.GetSystemTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_system_template_with_options_async(
        self,
        request: ice20201109_models.GetSystemTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetSystemTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSystemTemplate',
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
            ice20201109_models.GetSystemTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_system_template(
        self,
        request: ice20201109_models.GetSystemTemplateRequest,
    ) -> ice20201109_models.GetSystemTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_system_template_with_options(request, runtime)

    async def get_system_template_async(
        self,
        request: ice20201109_models.GetSystemTemplateRequest,
    ) -> ice20201109_models.GetSystemTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_system_template_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.related_mediaid_flag):
            query['RelatedMediaidFlag'] = request.related_mediaid_flag
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
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
            ice20201109_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ice20201109_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.related_mediaid_flag):
            query['RelatedMediaidFlag'] = request.related_mediaid_flag
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
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
        query = {}
        if not UtilClient.is_unset(request.file_list):
            query['FileList'] = request.file_list
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateMaterials',
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
            ice20201109_models.GetTemplateMaterialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_materials_with_options_async(
        self,
        request: ice20201109_models.GetTemplateMaterialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTemplateMaterialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_list):
            query['FileList'] = request.file_list
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateMaterials',
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

    def get_transcode_job_with_options(
        self,
        request: ice20201109_models.GetTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeJob',
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
            ice20201109_models.GetTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_transcode_job_with_options_async(
        self,
        request: ice20201109_models.GetTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetTranscodeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTranscodeJob',
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
            ice20201109_models.GetTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_transcode_job(
        self,
        request: ice20201109_models.GetTranscodeJobRequest,
    ) -> ice20201109_models.GetTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_transcode_job_with_options(request, runtime)

    async def get_transcode_job_async(
        self,
        request: ice20201109_models.GetTranscodeJobRequest,
    ) -> ice20201109_models.GetTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_transcode_job_with_options_async(request, runtime)

    def get_url_upload_infos_with_options(
        self,
        request: ice20201109_models.GetUrlUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetUrlUploadInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUrlUploadInfos',
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
            ice20201109_models.GetUrlUploadInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_url_upload_infos_with_options_async(
        self,
        request: ice20201109_models.GetUrlUploadInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.GetUrlUploadInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUrlUploadInfos',
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
            ice20201109_models.GetUrlUploadInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_url_upload_infos(
        self,
        request: ice20201109_models.GetUrlUploadInfosRequest,
    ) -> ice20201109_models.GetUrlUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_url_upload_infos_with_options(request, runtime)

    async def get_url_upload_infos_async(
        self,
        request: ice20201109_models.GetUrlUploadInfosRequest,
    ) -> ice20201109_models.GetUrlUploadInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_url_upload_infos_with_options_async(request, runtime)

    def list_all_public_media_tags_with_options(
        self,
        request: ice20201109_models.ListAllPublicMediaTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListAllPublicMediaTagsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.entity_id):
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
            auth_type='Anonymous',
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
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.entity_id):
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
            auth_type='Anonymous',
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

    def list_custom_templates_with_options(
        self,
        request: ice20201109_models.ListCustomTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListCustomTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomTemplates',
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
            ice20201109_models.ListCustomTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_custom_templates_with_options_async(
        self,
        request: ice20201109_models.ListCustomTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListCustomTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCustomTemplates',
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
            ice20201109_models.ListCustomTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_custom_templates(
        self,
        request: ice20201109_models.ListCustomTemplatesRequest,
    ) -> ice20201109_models.ListCustomTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_custom_templates_with_options(request, runtime)

    async def list_custom_templates_async(
        self,
        request: ice20201109_models.ListCustomTemplatesRequest,
    ) -> ice20201109_models.ListCustomTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_custom_templates_with_options_async(request, runtime)

    def list_dynamic_image_jobs_with_options(
        self,
        request: ice20201109_models.ListDynamicImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListDynamicImageJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicImageJobs',
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
            ice20201109_models.ListDynamicImageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dynamic_image_jobs_with_options_async(
        self,
        request: ice20201109_models.ListDynamicImageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListDynamicImageJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDynamicImageJobs',
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
            ice20201109_models.ListDynamicImageJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dynamic_image_jobs(
        self,
        request: ice20201109_models.ListDynamicImageJobsRequest,
    ) -> ice20201109_models.ListDynamicImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dynamic_image_jobs_with_options(request, runtime)

    async def list_dynamic_image_jobs_async(
        self,
        request: ice20201109_models.ListDynamicImageJobsRequest,
    ) -> ice20201109_models.ListDynamicImageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dynamic_image_jobs_with_options_async(request, runtime)

    def list_live_record_files_with_options(
        self,
        request: ice20201109_models.ListLiveRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordFiles',
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
            ice20201109_models.ListLiveRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_record_files_with_options_async(
        self,
        request: ice20201109_models.ListLiveRecordFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordFiles',
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
            ice20201109_models.ListLiveRecordFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_record_files(
        self,
        request: ice20201109_models.ListLiveRecordFilesRequest,
    ) -> ice20201109_models.ListLiveRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_files_with_options(request, runtime)

    async def list_live_record_files_async(
        self,
        request: ice20201109_models.ListLiveRecordFilesRequest,
    ) -> ice20201109_models.ListLiveRecordFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_files_with_options_async(request, runtime)

    def list_live_record_jobs_with_options(
        self,
        request: ice20201109_models.ListLiveRecordJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordJobs',
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
            ice20201109_models.ListLiveRecordJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_record_jobs_with_options_async(
        self,
        request: ice20201109_models.ListLiveRecordJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordJobs',
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
            ice20201109_models.ListLiveRecordJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_record_jobs(
        self,
        request: ice20201109_models.ListLiveRecordJobsRequest,
    ) -> ice20201109_models.ListLiveRecordJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_jobs_with_options(request, runtime)

    async def list_live_record_jobs_async(
        self,
        request: ice20201109_models.ListLiveRecordJobsRequest,
    ) -> ice20201109_models.ListLiveRecordJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_jobs_with_options_async(request, runtime)

    def list_live_record_templates_with_options(
        self,
        request: ice20201109_models.ListLiveRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordTemplates',
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
            ice20201109_models.ListLiveRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_record_templates_with_options_async(
        self,
        request: ice20201109_models.ListLiveRecordTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveRecordTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRecordTemplates',
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
            ice20201109_models.ListLiveRecordTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_record_templates(
        self,
        request: ice20201109_models.ListLiveRecordTemplatesRequest,
    ) -> ice20201109_models.ListLiveRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_record_templates_with_options(request, runtime)

    async def list_live_record_templates_async(
        self,
        request: ice20201109_models.ListLiveRecordTemplatesRequest,
    ) -> ice20201109_models.ListLiveRecordTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_record_templates_with_options_async(request, runtime)

    def list_live_snapshot_files_with_options(
        self,
        request: ice20201109_models.ListLiveSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotFiles',
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
            ice20201109_models.ListLiveSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_snapshot_files_with_options_async(
        self,
        request: ice20201109_models.ListLiveSnapshotFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotFilesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotFiles',
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
            ice20201109_models.ListLiveSnapshotFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_snapshot_files(
        self,
        request: ice20201109_models.ListLiveSnapshotFilesRequest,
    ) -> ice20201109_models.ListLiveSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_files_with_options(request, runtime)

    async def list_live_snapshot_files_async(
        self,
        request: ice20201109_models.ListLiveSnapshotFilesRequest,
    ) -> ice20201109_models.ListLiveSnapshotFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_snapshot_files_with_options_async(request, runtime)

    def list_live_snapshot_jobs_with_options(
        self,
        request: ice20201109_models.ListLiveSnapshotJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotJobs',
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
            ice20201109_models.ListLiveSnapshotJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_snapshot_jobs_with_options_async(
        self,
        request: ice20201109_models.ListLiveSnapshotJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotJobsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotJobs',
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
            ice20201109_models.ListLiveSnapshotJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_snapshot_jobs(
        self,
        request: ice20201109_models.ListLiveSnapshotJobsRequest,
    ) -> ice20201109_models.ListLiveSnapshotJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_jobs_with_options(request, runtime)

    async def list_live_snapshot_jobs_async(
        self,
        request: ice20201109_models.ListLiveSnapshotJobsRequest,
    ) -> ice20201109_models.ListLiveSnapshotJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_snapshot_jobs_with_options_async(request, runtime)

    def list_live_snapshot_templates_with_options(
        self,
        request: ice20201109_models.ListLiveSnapshotTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotTemplates',
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
            ice20201109_models.ListLiveSnapshotTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_snapshot_templates_with_options_async(
        self,
        request: ice20201109_models.ListLiveSnapshotTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveSnapshotTemplatesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveSnapshotTemplates',
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
            ice20201109_models.ListLiveSnapshotTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_snapshot_templates(
        self,
        request: ice20201109_models.ListLiveSnapshotTemplatesRequest,
    ) -> ice20201109_models.ListLiveSnapshotTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_snapshot_templates_with_options(request, runtime)

    async def list_live_snapshot_templates_async(
        self,
        request: ice20201109_models.ListLiveSnapshotTemplatesRequest,
    ) -> ice20201109_models.ListLiveSnapshotTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_snapshot_templates_with_options_async(request, runtime)

    def list_live_transcode_jobs_with_options(
        self,
        request: ice20201109_models.ListLiveTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveTranscodeJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeJobs',
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
            ice20201109_models.ListLiveTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_transcode_jobs_with_options_async(
        self,
        request: ice20201109_models.ListLiveTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveTranscodeJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeJobs',
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
            ice20201109_models.ListLiveTranscodeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_transcode_jobs(
        self,
        request: ice20201109_models.ListLiveTranscodeJobsRequest,
    ) -> ice20201109_models.ListLiveTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_transcode_jobs_with_options(request, runtime)

    async def list_live_transcode_jobs_async(
        self,
        request: ice20201109_models.ListLiveTranscodeJobsRequest,
    ) -> ice20201109_models.ListLiveTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_transcode_jobs_with_options_async(request, runtime)

    def list_live_transcode_templates_with_options(
        self,
        request: ice20201109_models.ListLiveTranscodeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveTranscodeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.video_codec):
            query['VideoCodec'] = request.video_codec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeTemplates',
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
            ice20201109_models.ListLiveTranscodeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_live_transcode_templates_with_options_async(
        self,
        request: ice20201109_models.ListLiveTranscodeTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListLiveTranscodeTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key_word):
            query['KeyWord'] = request.key_word
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.video_codec):
            query['VideoCodec'] = request.video_codec
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveTranscodeTemplates',
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
            ice20201109_models.ListLiveTranscodeTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_live_transcode_templates(
        self,
        request: ice20201109_models.ListLiveTranscodeTemplatesRequest,
    ) -> ice20201109_models.ListLiveTranscodeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_live_transcode_templates_with_options(request, runtime)

    async def list_live_transcode_templates_async(
        self,
        request: ice20201109_models.ListLiveTranscodeTemplatesRequest,
    ) -> ice20201109_models.ListLiveTranscodeTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_live_transcode_templates_with_options_async(request, runtime)

    def list_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
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
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
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

    def list_media_info_jobs_with_options(
        self,
        request: ice20201109_models.ListMediaInfoJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaInfoJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaInfoJobs',
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
            ice20201109_models.ListMediaInfoJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_media_info_jobs_with_options_async(
        self,
        request: ice20201109_models.ListMediaInfoJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListMediaInfoJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMediaInfoJobs',
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
            ice20201109_models.ListMediaInfoJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_media_info_jobs(
        self,
        request: ice20201109_models.ListMediaInfoJobsRequest,
    ) -> ice20201109_models.ListMediaInfoJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_media_info_jobs_with_options(request, runtime)

    async def list_media_info_jobs_async(
        self,
        request: ice20201109_models.ListMediaInfoJobsRequest,
    ) -> ice20201109_models.ListMediaInfoJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_media_info_jobs_with_options_async(request, runtime)

    def list_package_jobs_with_options(
        self,
        request: ice20201109_models.ListPackageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPackageJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPackageJobs',
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
            ice20201109_models.ListPackageJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_package_jobs_with_options_async(
        self,
        request: ice20201109_models.ListPackageJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPackageJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPackageJobs',
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
            ice20201109_models.ListPackageJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_package_jobs(
        self,
        request: ice20201109_models.ListPackageJobsRequest,
    ) -> ice20201109_models.ListPackageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_package_jobs_with_options(request, runtime)

    async def list_package_jobs_async(
        self,
        request: ice20201109_models.ListPackageJobsRequest,
    ) -> ice20201109_models.ListPackageJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_package_jobs_with_options_async(request, runtime)

    def list_pipelines_with_options(
        self,
        request: ice20201109_models.ListPipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
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
            ice20201109_models.ListPipelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pipelines_with_options_async(
        self,
        request: ice20201109_models.ListPipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPipelinesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPipelines',
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
            ice20201109_models.ListPipelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pipelines(
        self,
        request: ice20201109_models.ListPipelinesRequest,
    ) -> ice20201109_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pipelines_with_options(request, runtime)

    async def list_pipelines_async(
        self,
        request: ice20201109_models.ListPipelinesRequest,
    ) -> ice20201109_models.ListPipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pipelines_with_options_async(request, runtime)

    def list_public_media_basic_infos_with_options(
        self,
        request: ice20201109_models.ListPublicMediaBasicInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListPublicMediaBasicInfosResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_tag_id):
            query['MediaTagId'] = request.media_tag_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
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
        if not UtilClient.is_unset(request.include_file_basic_info):
            query['IncludeFileBasicInfo'] = request.include_file_basic_info
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_tag_id):
            query['MediaTagId'] = request.media_tag_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPublicMediaBasicInfos',
            version='2020-11-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='Anonymous',
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

    def list_snapshot_jobs_with_options(
        self,
        request: ice20201109_models.ListSnapshotJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSnapshotJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshotJobs',
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
            ice20201109_models.ListSnapshotJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshot_jobs_with_options_async(
        self,
        request: ice20201109_models.ListSnapshotJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSnapshotJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSnapshotJobs',
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
            ice20201109_models.ListSnapshotJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshot_jobs(
        self,
        request: ice20201109_models.ListSnapshotJobsRequest,
    ) -> ice20201109_models.ListSnapshotJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_snapshot_jobs_with_options(request, runtime)

    async def list_snapshot_jobs_async(
        self,
        request: ice20201109_models.ListSnapshotJobsRequest,
    ) -> ice20201109_models.ListSnapshotJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_snapshot_jobs_with_options_async(request, runtime)

    def list_system_templates_with_options(
        self,
        request: ice20201109_models.ListSystemTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSystemTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemTemplates',
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
            ice20201109_models.ListSystemTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_system_templates_with_options_async(
        self,
        request: ice20201109_models.ListSystemTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListSystemTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.subtype):
            query['Subtype'] = request.subtype
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSystemTemplates',
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
            ice20201109_models.ListSystemTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_system_templates(
        self,
        request: ice20201109_models.ListSystemTemplatesRequest,
    ) -> ice20201109_models.ListSystemTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_system_templates_with_options(request, runtime)

    async def list_system_templates_async(
        self,
        request: ice20201109_models.ListSystemTemplatesRequest,
    ) -> ice20201109_models.ListSystemTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_system_templates_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ice20201109_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
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

    def list_transcode_jobs_with_options(
        self,
        request: ice20201109_models.ListTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTranscodeJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTranscodeJobs',
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
            ice20201109_models.ListTranscodeJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_transcode_jobs_with_options_async(
        self,
        request: ice20201109_models.ListTranscodeJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.ListTranscodeJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_create_time):
            query['EndOfCreateTime'] = request.end_of_create_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_job_id):
            query['ParentJobId'] = request.parent_job_id
        if not UtilClient.is_unset(request.start_of_create_time):
            query['StartOfCreateTime'] = request.start_of_create_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTranscodeJobs',
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
            ice20201109_models.ListTranscodeJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_transcode_jobs(
        self,
        request: ice20201109_models.ListTranscodeJobsRequest,
    ) -> ice20201109_models.ListTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_transcode_jobs_with_options(request, runtime)

    async def list_transcode_jobs_async(
        self,
        request: ice20201109_models.ListTranscodeJobsRequest,
    ) -> ice20201109_models.ListTranscodeJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_transcode_jobs_with_options_async(request, runtime)

    def query_iproduction_job_with_options(
        self,
        request: ice20201109_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
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
            ice20201109_models.QueryIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_iproduction_job_with_options_async(
        self,
        request: ice20201109_models.QueryIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryIProductionJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIProductionJob',
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
            ice20201109_models.QueryIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_iproduction_job(
        self,
        request: ice20201109_models.QueryIProductionJobRequest,
    ) -> ice20201109_models.QueryIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_iproduction_job_with_options(request, runtime)

    async def query_iproduction_job_async(
        self,
        request: ice20201109_models.QueryIProductionJobRequest,
    ) -> ice20201109_models.QueryIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_iproduction_job_with_options_async(request, runtime)

    def query_media_censor_job_detail_with_options(
        self,
        request: ice20201109_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
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
            ice20201109_models.QueryMediaCensorJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_detail_with_options_async(
        self,
        request: ice20201109_models.QueryMediaCensorJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryMediaCensorJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobDetail',
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
            ice20201109_models.QueryMediaCensorJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_detail(
        self,
        request: ice20201109_models.QueryMediaCensorJobDetailRequest,
    ) -> ice20201109_models.QueryMediaCensorJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_detail_with_options(request, runtime)

    async def query_media_censor_job_detail_async(
        self,
        request: ice20201109_models.QueryMediaCensorJobDetailRequest,
    ) -> ice20201109_models.QueryMediaCensorJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_detail_with_options_async(request, runtime)

    def query_media_censor_job_list_with_options(
        self,
        request: ice20201109_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryMediaCensorJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
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
            ice20201109_models.QueryMediaCensorJobListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_media_censor_job_list_with_options_async(
        self,
        request: ice20201109_models.QueryMediaCensorJobListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QueryMediaCensorJobListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_of_job_created_time_range):
            query['EndOfJobCreatedTimeRange'] = request.end_of_job_created_time_range
        if not UtilClient.is_unset(request.job_ids):
            query['JobIds'] = request.job_ids
        if not UtilClient.is_unset(request.maximum_page_size):
            query['MaximumPageSize'] = request.maximum_page_size
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.start_of_job_created_time_range):
            query['StartOfJobCreatedTimeRange'] = request.start_of_job_created_time_range
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMediaCensorJobList',
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
            ice20201109_models.QueryMediaCensorJobListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_media_censor_job_list(
        self,
        request: ice20201109_models.QueryMediaCensorJobListRequest,
    ) -> ice20201109_models.QueryMediaCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_media_censor_job_list_with_options(request, runtime)

    async def query_media_censor_job_list_async(
        self,
        request: ice20201109_models.QueryMediaCensorJobListRequest,
    ) -> ice20201109_models.QueryMediaCensorJobListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_media_censor_job_list_with_options_async(request, runtime)

    def query_smarttag_job_with_options(
        self,
        request: ice20201109_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
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
            ice20201109_models.QuerySmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_smarttag_job_with_options_async(
        self,
        request: ice20201109_models.QuerySmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.QuerySmarttagJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySmarttagJob',
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
            ice20201109_models.QuerySmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_smarttag_job(
        self,
        request: ice20201109_models.QuerySmarttagJobRequest,
    ) -> ice20201109_models.QuerySmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_smarttag_job_with_options(request, runtime)

    async def query_smarttag_job_async(
        self,
        request: ice20201109_models.QuerySmarttagJobRequest,
    ) -> ice20201109_models.QuerySmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_smarttag_job_with_options_async(request, runtime)

    def refresh_upload_media_with_options(
        self,
        request: ice20201109_models.RefreshUploadMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RefreshUploadMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshUploadMedia',
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
            ice20201109_models.RefreshUploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_upload_media_with_options_async(
        self,
        request: ice20201109_models.RefreshUploadMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RefreshUploadMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshUploadMedia',
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
            ice20201109_models.RefreshUploadMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_upload_media(
        self,
        request: ice20201109_models.RefreshUploadMediaRequest,
    ) -> ice20201109_models.RefreshUploadMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_upload_media_with_options(request, runtime)

    async def refresh_upload_media_async(
        self,
        request: ice20201109_models.RefreshUploadMediaRequest,
    ) -> ice20201109_models.RefreshUploadMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_upload_media_with_options_async(request, runtime)

    def register_media_info_with_options(
        self,
        request: ice20201109_models.RegisterMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
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
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.register_config):
            query['RegisterConfig'] = request.register_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.workflow_id):
            query['WorkflowId'] = request.workflow_id
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

    def register_media_stream_with_options(
        self,
        request: ice20201109_models.RegisterMediaStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMediaStream',
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
            ice20201109_models.RegisterMediaStreamResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_media_stream_with_options_async(
        self,
        request: ice20201109_models.RegisterMediaStreamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.RegisterMediaStreamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterMediaStream',
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
            ice20201109_models.RegisterMediaStreamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_media_stream(
        self,
        request: ice20201109_models.RegisterMediaStreamRequest,
    ) -> ice20201109_models.RegisterMediaStreamResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_media_stream_with_options(request, runtime)

    async def register_media_stream_async(
        self,
        request: ice20201109_models.RegisterMediaStreamRequest,
    ) -> ice20201109_models.RegisterMediaStreamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_media_stream_with_options_async(request, runtime)

    def search_editing_project_with_options(
        self,
        request: ice20201109_models.SearchEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_type):
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
        if not UtilClient.is_unset(request.create_source):
            query['CreateSource'] = request.create_source
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_type):
            query['ProjectType'] = request.project_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_type):
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

    def search_media_with_options(
        self,
        request: ice20201109_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.match):
            query['Match'] = request.match
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMedia',
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
            ice20201109_models.SearchMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_media_with_options_async(
        self,
        request: ice20201109_models.SearchMediaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchMediaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.match):
            query['Match'] = request.match
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchMedia',
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
            ice20201109_models.SearchMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_media(
        self,
        request: ice20201109_models.SearchMediaRequest,
    ) -> ice20201109_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_media_with_options(request, runtime)

    async def search_media_async(
        self,
        request: ice20201109_models.SearchMediaRequest,
    ) -> ice20201109_models.SearchMediaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_media_with_options_async(request, runtime)

    def search_public_media_info_with_options(
        self,
        request: ice20201109_models.SearchPublicMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SearchPublicMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized):
            query['Authorized'] = request.authorized
        if not UtilClient.is_unset(request.dynamic_meta_data_match_fields):
            query['DynamicMetaDataMatchFields'] = request.dynamic_meta_data_match_fields
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.favorite):
            query['Favorite'] = request.favorite
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
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
        if not UtilClient.is_unset(request.authorized):
            query['Authorized'] = request.authorized
        if not UtilClient.is_unset(request.dynamic_meta_data_match_fields):
            query['DynamicMetaDataMatchFields'] = request.dynamic_meta_data_match_fields
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.favorite):
            query['Favorite'] = request.favorite
        if not UtilClient.is_unset(request.media_ids):
            query['MediaIds'] = request.media_ids
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
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

    def send_live_snapshot_job_command_with_options(
        self,
        request: ice20201109_models.SendLiveSnapshotJobCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SendLiveSnapshotJobCommandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.command):
            body['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendLiveSnapshotJobCommand',
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
            ice20201109_models.SendLiveSnapshotJobCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_live_snapshot_job_command_with_options_async(
        self,
        request: ice20201109_models.SendLiveSnapshotJobCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SendLiveSnapshotJobCommandResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.command):
            body['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendLiveSnapshotJobCommand',
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
            ice20201109_models.SendLiveSnapshotJobCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_live_snapshot_job_command(
        self,
        request: ice20201109_models.SendLiveSnapshotJobCommandRequest,
    ) -> ice20201109_models.SendLiveSnapshotJobCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_live_snapshot_job_command_with_options(request, runtime)

    async def send_live_snapshot_job_command_async(
        self,
        request: ice20201109_models.SendLiveSnapshotJobCommandRequest,
    ) -> ice20201109_models.SendLiveSnapshotJobCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_live_snapshot_job_command_with_options_async(request, runtime)

    def send_live_transcode_job_command_with_options(
        self,
        request: ice20201109_models.SendLiveTranscodeJobCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SendLiveTranscodeJobCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendLiveTranscodeJobCommand',
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
            ice20201109_models.SendLiveTranscodeJobCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_live_transcode_job_command_with_options_async(
        self,
        request: ice20201109_models.SendLiveTranscodeJobCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SendLiveTranscodeJobCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendLiveTranscodeJobCommand',
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
            ice20201109_models.SendLiveTranscodeJobCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_live_transcode_job_command(
        self,
        request: ice20201109_models.SendLiveTranscodeJobCommandRequest,
    ) -> ice20201109_models.SendLiveTranscodeJobCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_live_transcode_job_command_with_options(request, runtime)

    async def send_live_transcode_job_command_async(
        self,
        request: ice20201109_models.SendLiveTranscodeJobCommandRequest,
    ) -> ice20201109_models.SendLiveTranscodeJobCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_live_transcode_job_command_with_options_async(request, runtime)

    def set_default_custom_template_with_options(
        self,
        request: ice20201109_models.SetDefaultCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultCustomTemplate',
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
            ice20201109_models.SetDefaultCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_default_custom_template_with_options_async(
        self,
        request: ice20201109_models.SetDefaultCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultCustomTemplate',
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
            ice20201109_models.SetDefaultCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_default_custom_template(
        self,
        request: ice20201109_models.SetDefaultCustomTemplateRequest,
    ) -> ice20201109_models.SetDefaultCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_default_custom_template_with_options(request, runtime)

    async def set_default_custom_template_async(
        self,
        request: ice20201109_models.SetDefaultCustomTemplateRequest,
    ) -> ice20201109_models.SetDefaultCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_default_custom_template_with_options_async(request, runtime)

    def set_default_storage_location_with_options(
        self,
        request: ice20201109_models.SetDefaultStorageLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SetDefaultStorageLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
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
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
        if not UtilClient.is_unset(request.path):
            query['Path'] = request.path
        if not UtilClient.is_unset(request.storage_type):
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
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not UtilClient.is_unset(request.callback_queue_name):
            query['CallbackQueueName'] = request.callback_queue_name
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not UtilClient.is_unset(request.event_type_list):
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
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_switch):
            query['AuthSwitch'] = request.auth_switch
        if not UtilClient.is_unset(request.callback_queue_name):
            query['CallbackQueueName'] = request.callback_queue_name
        if not UtilClient.is_unset(request.callback_type):
            query['CallbackType'] = request.callback_type
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackURL'] = request.callback_url
        if not UtilClient.is_unset(request.event_type_list):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.input_file):
            query['InputFile'] = request.input_file
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.input_file):
            query['InputFile'] = request.input_file
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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

    def submit_dynamic_chart_job_with_options(
        self,
        request: ice20201109_models.SubmitDynamicChartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDynamicChartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.axis_params):
            query['AxisParams'] = request.axis_params
        if not UtilClient.is_unset(request.background):
            query['Background'] = request.background
        if not UtilClient.is_unset(request.chart_config):
            query['ChartConfig'] = request.chart_config
        if not UtilClient.is_unset(request.chart_title):
            query['ChartTitle'] = request.chart_title
        if not UtilClient.is_unset(request.chart_type):
            query['ChartType'] = request.chart_type
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.subtitle):
            query['Subtitle'] = request.subtitle
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.axis_params):
            query['AxisParams'] = request.axis_params
        if not UtilClient.is_unset(request.background):
            query['Background'] = request.background
        if not UtilClient.is_unset(request.chart_config):
            query['ChartConfig'] = request.chart_config
        if not UtilClient.is_unset(request.chart_title):
            query['ChartTitle'] = request.chart_title
        if not UtilClient.is_unset(request.chart_type):
            query['ChartType'] = request.chart_type
        if not UtilClient.is_unset(request.data_source):
            query['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input):
            query['Input'] = request.input
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.subtitle):
            query['Subtitle'] = request.subtitle
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.unit):
            query['Unit'] = request.unit
        if not UtilClient.is_unset(request.user_data):
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

    def submit_dynamic_image_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitDynamicImageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicImageJob',
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
            ice20201109_models.SubmitDynamicImageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_dynamic_image_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitDynamicImageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitDynamicImageJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitDynamicImageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitDynamicImageJob',
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
            ice20201109_models.SubmitDynamicImageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_dynamic_image_job(
        self,
        request: ice20201109_models.SubmitDynamicImageJobRequest,
    ) -> ice20201109_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_dynamic_image_job_with_options(request, runtime)

    async def submit_dynamic_image_job_async(
        self,
        request: ice20201109_models.SubmitDynamicImageJobRequest,
    ) -> ice20201109_models.SubmitDynamicImageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_dynamic_image_job_with_options_async(request, runtime)

    def submit_iproduction_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitIProductionJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
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
            ice20201109_models.SubmitIProductionJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_iproduction_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitIProductionJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitIProductionJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitIProductionJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.job_params):
            query['JobParams'] = request.job_params
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIProductionJob',
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
            ice20201109_models.SubmitIProductionJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_iproduction_job(
        self,
        request: ice20201109_models.SubmitIProductionJobRequest,
    ) -> ice20201109_models.SubmitIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_iproduction_job_with_options(request, runtime)

    async def submit_iproduction_job_async(
        self,
        request: ice20201109_models.SubmitIProductionJobRequest,
    ) -> ice20201109_models.SubmitIProductionJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_iproduction_job_with_options_async(request, runtime)

    def submit_live_editing_job_with_options(
        self,
        request: ice20201109_models.SubmitLiveEditingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveEditingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clips):
            query['Clips'] = request.clips
        if not UtilClient.is_unset(request.live_stream_config):
            query['LiveStreamConfig'] = request.live_stream_config
        if not UtilClient.is_unset(request.media_produce_config):
            query['MediaProduceConfig'] = request.media_produce_config
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.clips):
            query['Clips'] = request.clips
        if not UtilClient.is_unset(request.live_stream_config):
            query['LiveStreamConfig'] = request.live_stream_config
        if not UtilClient.is_unset(request.media_produce_config):
            query['MediaProduceConfig'] = request.media_produce_config
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.user_data):
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

    def submit_live_record_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitLiveRecordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveRecordJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveRecordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_output):
            request.record_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_output, 'RecordOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_url):
            body['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.record_output_shrink):
            body['RecordOutput'] = request.record_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveRecordJob',
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
            ice20201109_models.SubmitLiveRecordJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_live_record_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitLiveRecordJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveRecordJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveRecordJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_output):
            request.record_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_output, 'RecordOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_url):
            body['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.record_output_shrink):
            body['RecordOutput'] = request.record_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveRecordJob',
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
            ice20201109_models.SubmitLiveRecordJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_live_record_job(
        self,
        request: ice20201109_models.SubmitLiveRecordJobRequest,
    ) -> ice20201109_models.SubmitLiveRecordJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_live_record_job_with_options(request, runtime)

    async def submit_live_record_job_async(
        self,
        request: ice20201109_models.SubmitLiveRecordJobRequest,
    ) -> ice20201109_models.SubmitLiveRecordJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_live_record_job_with_options_async(request, runtime)

    def submit_live_snapshot_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitLiveSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveSnapshotJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_output):
            request.snapshot_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_output, 'SnapshotOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.snapshot_output_shrink):
            body['SnapshotOutput'] = request.snapshot_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveSnapshotJob',
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
            ice20201109_models.SubmitLiveSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_live_snapshot_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitLiveSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveSnapshotJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.snapshot_output):
            request.snapshot_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.snapshot_output, 'SnapshotOutput', 'json')
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        body = {}
        if not UtilClient.is_unset(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.job_name):
            body['JobName'] = request.job_name
        if not UtilClient.is_unset(request.snapshot_output_shrink):
            body['SnapshotOutput'] = request.snapshot_output_shrink
        if not UtilClient.is_unset(request.stream_input_shrink):
            body['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitLiveSnapshotJob',
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
            ice20201109_models.SubmitLiveSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_live_snapshot_job(
        self,
        request: ice20201109_models.SubmitLiveSnapshotJobRequest,
    ) -> ice20201109_models.SubmitLiveSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_live_snapshot_job_with_options(request, runtime)

    async def submit_live_snapshot_job_async(
        self,
        request: ice20201109_models.SubmitLiveSnapshotJobRequest,
    ) -> ice20201109_models.SubmitLiveSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_live_snapshot_job_with_options_async(request, runtime)

    def submit_live_transcode_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveTranscodeJob',
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
            ice20201109_models.SubmitLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_live_transcode_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitLiveTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.start_mode):
            query['StartMode'] = request.start_mode
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitLiveTranscodeJob',
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
            ice20201109_models.SubmitLiveTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_live_transcode_job(
        self,
        request: ice20201109_models.SubmitLiveTranscodeJobRequest,
    ) -> ice20201109_models.SubmitLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_live_transcode_job_with_options(request, runtime)

    async def submit_live_transcode_job_async(
        self,
        request: ice20201109_models.SubmitLiveTranscodeJobRequest,
    ) -> ice20201109_models.SubmitLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_live_transcode_job_with_options_async(request, runtime)

    def submit_media_censor_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaCensorJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
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
            ice20201109_models.SubmitMediaCensorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_censor_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitMediaCensorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaCensorJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaCensorJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.barrages):
            query['Barrages'] = request.barrages
        if not UtilClient.is_unset(request.cover_images):
            query['CoverImages'] = request.cover_images
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.output):
            query['Output'] = request.output
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaCensorJob',
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
            ice20201109_models.SubmitMediaCensorJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_censor_job(
        self,
        request: ice20201109_models.SubmitMediaCensorJobRequest,
    ) -> ice20201109_models.SubmitMediaCensorJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_censor_job_with_options(request, runtime)

    async def submit_media_censor_job_async(
        self,
        request: ice20201109_models.SubmitMediaCensorJobRequest,
    ) -> ice20201109_models.SubmitMediaCensorJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_censor_job_with_options_async(request, runtime)

    def submit_media_info_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
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
            ice20201109_models.SubmitMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_media_info_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaInfoJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitMediaInfoJob',
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
            ice20201109_models.SubmitMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_media_info_job(
        self,
        request: ice20201109_models.SubmitMediaInfoJobRequest,
    ) -> ice20201109_models.SubmitMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_media_info_job_with_options(request, runtime)

    async def submit_media_info_job_async(
        self,
        request: ice20201109_models.SubmitMediaInfoJobRequest,
    ) -> ice20201109_models.SubmitMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_media_info_job_with_options_async(request, runtime)

    def submit_media_producing_job_with_options(
        self,
        request: ice20201109_models.SubmitMediaProducingJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitMediaProducingJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.editing_produce_config):
            query['EditingProduceConfig'] = request.editing_produce_config
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_metadata):
            query['ProjectMetadata'] = request.project_metadata
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.editing_produce_config):
            query['EditingProduceConfig'] = request.editing_produce_config
        if not UtilClient.is_unset(request.output_media_config):
            query['OutputMediaConfig'] = request.output_media_config
        if not UtilClient.is_unset(request.output_media_target):
            query['OutputMediaTarget'] = request.output_media_target
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.project_metadata):
            query['ProjectMetadata'] = request.project_metadata
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.user_data):
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

    def submit_package_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitPackageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPackageJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitPackageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPackageJob',
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
            ice20201109_models.SubmitPackageJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_package_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitPackageJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitPackageJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitPackageJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.inputs):
            request.inputs_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.inputs, 'Inputs', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.inputs_shrink):
            query['Inputs'] = request.inputs_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPackageJob',
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
            ice20201109_models.SubmitPackageJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_package_job(
        self,
        request: ice20201109_models.SubmitPackageJobRequest,
    ) -> ice20201109_models.SubmitPackageJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_package_job_with_options(request, runtime)

    async def submit_package_job_async(
        self,
        request: ice20201109_models.SubmitPackageJobRequest,
    ) -> ice20201109_models.SubmitPackageJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_package_job_with_options_async(request, runtime)

    def submit_smarttag_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSmarttagJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
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
            ice20201109_models.SubmitSmarttagJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_smarttag_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitSmarttagJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSmarttagJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSmarttagJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.content_addr):
            query['ContentAddr'] = request.content_addr
        if not UtilClient.is_unset(request.content_type):
            query['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSmarttagJob',
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
            ice20201109_models.SubmitSmarttagJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_smarttag_job(
        self,
        request: ice20201109_models.SubmitSmarttagJobRequest,
    ) -> ice20201109_models.SubmitSmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smarttag_job_with_options(request, runtime)

    async def submit_smarttag_job_async(
        self,
        request: ice20201109_models.SubmitSmarttagJobRequest,
    ) -> ice20201109_models.SubmitSmarttagJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smarttag_job_with_options_async(request, runtime)

    def submit_snapshot_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
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
            ice20201109_models.SubmitSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_snapshot_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitSnapshotJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSnapshotJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSnapshotJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.output):
            request.output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_shrink):
            query['Output'] = request.output_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSnapshotJob',
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
            ice20201109_models.SubmitSnapshotJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_snapshot_job(
        self,
        request: ice20201109_models.SubmitSnapshotJobRequest,
    ) -> ice20201109_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_snapshot_job_with_options(request, runtime)

    async def submit_snapshot_job_async(
        self,
        request: ice20201109_models.SubmitSnapshotJobRequest,
    ) -> ice20201109_models.SubmitSnapshotJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_snapshot_job_with_options_async(request, runtime)

    def submit_subtitle_produce_job_with_options(
        self,
        request: ice20201109_models.SubmitSubtitleProduceJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSubtitleProduceJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.editing_config):
            query['EditingConfig'] = request.editing_config
        if not UtilClient.is_unset(request.input_config):
            query['InputConfig'] = request.input_config
        if not UtilClient.is_unset(request.is_async):
            query['IsAsync'] = request.is_async
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_data):
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

    def submit_sync_media_info_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitSyncMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSyncMediaInfoJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSyncMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSyncMediaInfoJob',
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
            ice20201109_models.SubmitSyncMediaInfoJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_sync_media_info_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitSyncMediaInfoJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitSyncMediaInfoJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitSyncMediaInfoJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_shrink):
            query['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitSyncMediaInfoJob',
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
            ice20201109_models.SubmitSyncMediaInfoJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_sync_media_info_job(
        self,
        request: ice20201109_models.SubmitSyncMediaInfoJobRequest,
    ) -> ice20201109_models.SubmitSyncMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sync_media_info_job_with_options(request, runtime)

    async def submit_sync_media_info_job_async(
        self,
        request: ice20201109_models.SubmitSyncMediaInfoJobRequest,
    ) -> ice20201109_models.SubmitSyncMediaInfoJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sync_media_info_job_with_options_async(request, runtime)

    def submit_transcode_job_with_options(
        self,
        tmp_req: ice20201109_models.SubmitTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_group):
            request.input_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_group, 'InputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.output_group):
            request.output_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output_group, 'OutputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_group_shrink):
            query['InputGroup'] = request.input_group_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_group_shrink):
            query['OutputGroup'] = request.output_group_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTranscodeJob',
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
            ice20201109_models.SubmitTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_transcode_job_with_options_async(
        self,
        tmp_req: ice20201109_models.SubmitTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.SubmitTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.SubmitTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.input_group):
            request.input_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input_group, 'InputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.output_group):
            request.output_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.output_group, 'OutputGroup', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_config):
            request.schedule_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_config, 'ScheduleConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.input_group_shrink):
            query['InputGroup'] = request.input_group_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.output_group_shrink):
            query['OutputGroup'] = request.output_group_shrink
        if not UtilClient.is_unset(request.schedule_config_shrink):
            query['ScheduleConfig'] = request.schedule_config_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitTranscodeJob',
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
            ice20201109_models.SubmitTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_transcode_job(
        self,
        request: ice20201109_models.SubmitTranscodeJobRequest,
    ) -> ice20201109_models.SubmitTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_transcode_job_with_options(request, runtime)

    async def submit_transcode_job_async(
        self,
        request: ice20201109_models.SubmitTranscodeJobRequest,
    ) -> ice20201109_models.SubmitTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_transcode_job_with_options_async(request, runtime)

    def update_category_with_options(
        self,
        request: ice20201109_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
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
            ice20201109_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_category_with_options_async(
        self,
        request: ice20201109_models.UpdateCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.cate_name):
            query['CateName'] = request.cate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
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
            ice20201109_models.UpdateCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_category(
        self,
        request: ice20201109_models.UpdateCategoryRequest,
    ) -> ice20201109_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    async def update_category_async(
        self,
        request: ice20201109_models.UpdateCategoryRequest,
    ) -> ice20201109_models.UpdateCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_category_with_options_async(request, runtime)

    def update_custom_template_with_options(
        self,
        request: ice20201109_models.UpdateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomTemplate',
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
            ice20201109_models.UpdateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_custom_template_with_options_async(
        self,
        request: ice20201109_models.UpdateCustomTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateCustomTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCustomTemplate',
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
            ice20201109_models.UpdateCustomTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_custom_template(
        self,
        request: ice20201109_models.UpdateCustomTemplateRequest,
    ) -> ice20201109_models.UpdateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_custom_template_with_options(request, runtime)

    async def update_custom_template_async(
        self,
        request: ice20201109_models.UpdateCustomTemplateRequest,
    ) -> ice20201109_models.UpdateCustomTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_custom_template_with_options_async(request, runtime)

    def update_editing_project_with_options(
        self,
        request: ice20201109_models.UpdateEditingProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateEditingProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
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
        if not UtilClient.is_unset(request.business_status):
            query['BusinessStatus'] = request.business_status
        if not UtilClient.is_unset(request.clips_param):
            query['ClipsParam'] = request.clips_param
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.timeline):
            query['Timeline'] = request.timeline
        if not UtilClient.is_unset(request.title):
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

    def update_live_record_template_with_options(
        self,
        tmp_req: ice20201109_models.UpdateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordTemplate',
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
            ice20201109_models.UpdateLiveRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_record_template_with_options_async(
        self,
        tmp_req: ice20201109_models.UpdateLiveRecordTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveRecordTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveRecordTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.record_format):
            request.record_format_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.record_format, 'RecordFormat', 'json')
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.record_format_shrink):
            body['RecordFormat'] = request.record_format_shrink
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordTemplate',
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
            ice20201109_models.UpdateLiveRecordTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_record_template(
        self,
        request: ice20201109_models.UpdateLiveRecordTemplateRequest,
    ) -> ice20201109_models.UpdateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_template_with_options(request, runtime)

    async def update_live_record_template_async(
        self,
        request: ice20201109_models.UpdateLiveRecordTemplateRequest,
    ) -> ice20201109_models.UpdateLiveRecordTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_record_template_with_options_async(request, runtime)

    def update_live_snapshot_template_with_options(
        self,
        request: ice20201109_models.UpdateLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotTemplate',
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
            ice20201109_models.UpdateLiveSnapshotTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_snapshot_template_with_options_async(
        self,
        request: ice20201109_models.UpdateLiveSnapshotTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveSnapshotTemplateResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.overwrite_format):
            body['OverwriteFormat'] = request.overwrite_format
        if not UtilClient.is_unset(request.sequence_format):
            body['SequenceFormat'] = request.sequence_format
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.time_interval):
            body['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotTemplate',
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
            ice20201109_models.UpdateLiveSnapshotTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_snapshot_template(
        self,
        request: ice20201109_models.UpdateLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.UpdateLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_snapshot_template_with_options(request, runtime)

    async def update_live_snapshot_template_async(
        self,
        request: ice20201109_models.UpdateLiveSnapshotTemplateRequest,
    ) -> ice20201109_models.UpdateLiveSnapshotTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_snapshot_template_with_options_async(request, runtime)

    def update_live_transcode_job_with_options(
        self,
        tmp_req: ice20201109_models.UpdateLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeJob',
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
            ice20201109_models.UpdateLiveTranscodeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_transcode_job_with_options_async(
        self,
        tmp_req: ice20201109_models.UpdateLiveTranscodeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveTranscodeJobResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.stream_input):
            request.stream_input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.stream_input, 'StreamInput', 'json')
        if not UtilClient.is_unset(tmp_req.timed_config):
            request.timed_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timed_config, 'TimedConfig', 'json')
        if not UtilClient.is_unset(tmp_req.transcode_output):
            request.transcode_output_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.transcode_output, 'TranscodeOutput', 'json')
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.stream_input_shrink):
            query['StreamInput'] = request.stream_input_shrink
        if not UtilClient.is_unset(request.timed_config_shrink):
            query['TimedConfig'] = request.timed_config_shrink
        if not UtilClient.is_unset(request.transcode_output_shrink):
            query['TranscodeOutput'] = request.transcode_output_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeJob',
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
            ice20201109_models.UpdateLiveTranscodeJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_transcode_job(
        self,
        request: ice20201109_models.UpdateLiveTranscodeJobRequest,
    ) -> ice20201109_models.UpdateLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_transcode_job_with_options(request, runtime)

    async def update_live_transcode_job_async(
        self,
        request: ice20201109_models.UpdateLiveTranscodeJobRequest,
    ) -> ice20201109_models.UpdateLiveTranscodeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_transcode_job_with_options_async(request, runtime)

    def update_live_transcode_template_with_options(
        self,
        tmp_req: ice20201109_models.UpdateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeTemplate',
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
            ice20201109_models.UpdateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_transcode_template_with_options_async(
        self,
        tmp_req: ice20201109_models.UpdateLiveTranscodeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateLiveTranscodeTemplateResponse:
        UtilClient.validate_model(tmp_req)
        request = ice20201109_models.UpdateLiveTranscodeTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_config):
            request.template_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_config, 'TemplateConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_config_shrink):
            query['TemplateConfig'] = request.template_config_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTranscodeTemplate',
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
            ice20201109_models.UpdateLiveTranscodeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live_transcode_template(
        self,
        request: ice20201109_models.UpdateLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.UpdateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_live_transcode_template_with_options(request, runtime)

    async def update_live_transcode_template_async(
        self,
        request: ice20201109_models.UpdateLiveTranscodeTemplateRequest,
    ) -> ice20201109_models.UpdateLiveTranscodeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_live_transcode_template_with_options_async(request, runtime)

    def update_media_info_with_options(
        self,
        request: ice20201109_models.UpdateMediaInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateMediaInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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
        if not UtilClient.is_unset(request.append_tags):
            query['AppendTags'] = request.append_tags
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.cate_id):
            query['CateId'] = request.cate_id
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.cover_url):
            query['CoverURL'] = request.cover_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.input_url):
            query['InputURL'] = request.input_url
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.media_tags):
            query['MediaTags'] = request.media_tags
        if not UtilClient.is_unset(request.reference_id):
            query['ReferenceId'] = request.reference_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.user_data):
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

    def update_pipeline_with_options(
        self,
        request: ice20201109_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
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
            ice20201109_models.UpdatePipelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pipeline_with_options_async(
        self,
        request: ice20201109_models.UpdatePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdatePipelineResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pipeline_id):
            query['PipelineId'] = request.pipeline_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePipeline',
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
            ice20201109_models.UpdatePipelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pipeline(
        self,
        request: ice20201109_models.UpdatePipelineRequest,
    ) -> ice20201109_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_pipeline_with_options(request, runtime)

    async def update_pipeline_async(
        self,
        request: ice20201109_models.UpdatePipelineRequest,
    ) -> ice20201109_models.UpdatePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_pipeline_with_options_async(request, runtime)

    def update_smart_job_with_options(
        self,
        request: ice20201109_models.UpdateSmartJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UpdateSmartJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feextend):
            query['FEExtend'] = request.feextend
        if not UtilClient.is_unset(request.job_id):
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
        if not UtilClient.is_unset(request.feextend):
            query['FEExtend'] = request.feextend
        if not UtilClient.is_unset(request.job_id):
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
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
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.cover_url):
            query['CoverUrl'] = request.cover_url
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.preview_media):
            query['PreviewMedia'] = request.preview_media
        if not UtilClient.is_unset(request.related_mediaids):
            query['RelatedMediaids'] = request.related_mediaids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_id):
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

    def upload_media_by_urlwith_options(
        self,
        request: ice20201109_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMediaByURL',
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
            ice20201109_models.UploadMediaByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_media_by_urlwith_options_async(
        self,
        request: ice20201109_models.UploadMediaByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UploadMediaByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.media_meta_data):
            query['MediaMetaData'] = request.media_meta_data
        if not UtilClient.is_unset(request.post_process_config):
            query['PostProcessConfig'] = request.post_process_config
        if not UtilClient.is_unset(request.upload_target_config):
            query['UploadTargetConfig'] = request.upload_target_config
        if not UtilClient.is_unset(request.upload_urls):
            query['UploadURLs'] = request.upload_urls
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadMediaByURL',
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
            ice20201109_models.UploadMediaByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_media_by_url(
        self,
        request: ice20201109_models.UploadMediaByURLRequest,
    ) -> ice20201109_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_media_by_urlwith_options(request, runtime)

    async def upload_media_by_url_async(
        self,
        request: ice20201109_models.UploadMediaByURLRequest,
    ) -> ice20201109_models.UploadMediaByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_media_by_urlwith_options_async(request, runtime)

    def upload_stream_by_urlwith_options(
        self,
        request: ice20201109_models.UploadStreamByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UploadStreamByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not UtilClient.is_unset(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadStreamByURL',
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
            ice20201109_models.UploadStreamByURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_stream_by_urlwith_options_async(
        self,
        request: ice20201109_models.UploadStreamByURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ice20201109_models.UploadStreamByURLResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.definition):
            query['Definition'] = request.definition
        if not UtilClient.is_unset(request.file_extension):
            query['FileExtension'] = request.file_extension
        if not UtilClient.is_unset(request.hdrtype):
            query['HDRType'] = request.hdrtype
        if not UtilClient.is_unset(request.media_id):
            query['MediaId'] = request.media_id
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadStreamByURL',
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
            ice20201109_models.UploadStreamByURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_stream_by_url(
        self,
        request: ice20201109_models.UploadStreamByURLRequest,
    ) -> ice20201109_models.UploadStreamByURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_stream_by_urlwith_options(request, runtime)

    async def upload_stream_by_url_async(
        self,
        request: ice20201109_models.UploadStreamByURLRequest,
    ) -> ice20201109_models.UploadStreamByURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_stream_by_urlwith_options_async(request, runtime)
