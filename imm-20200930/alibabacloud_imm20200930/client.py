# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_imm20200930 import models as imm_20200930_models
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

    def add_image_mosaic_with_options(
        self,
        tmp_req: imm_20200930_models.AddImageMosaicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary 图片打马赛克算子
        
        @param tmp_req: AddImageMosaicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageMosaicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddImageMosaicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageMosaic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddImageMosaicResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_mosaic_with_options_async(
        self,
        tmp_req: imm_20200930_models.AddImageMosaicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary 图片打马赛克算子
        
        @param tmp_req: AddImageMosaicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageMosaicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddImageMosaicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddImageMosaic',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddImageMosaicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_mosaic(
        self,
        request: imm_20200930_models.AddImageMosaicRequest,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary 图片打马赛克算子
        
        @param request: AddImageMosaicRequest
        @return: AddImageMosaicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_image_mosaic_with_options(request, runtime)

    async def add_image_mosaic_async(
        self,
        request: imm_20200930_models.AddImageMosaicRequest,
    ) -> imm_20200930_models.AddImageMosaicResponse:
        """
        @summary 图片打马赛克算子
        
        @param request: AddImageMosaicRequest
        @return: AddImageMosaicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_image_mosaic_with_options_async(request, runtime)

    def add_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.AddStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary 为故事新增文件
        
        @param tmp_req: AddStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_story_files_with_options_async(
        self,
        tmp_req: imm_20200930_models.AddStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary 为故事新增文件
        
        @param tmp_req: AddStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.AddStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AddStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_story_files(
        self,
        request: imm_20200930_models.AddStoryFilesRequest,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary 为故事新增文件
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_story_files_with_options(request, runtime)

    async def add_story_files_async(
        self,
        request: imm_20200930_models.AddStoryFilesRequest,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        """
        @summary 为故事新增文件
        
        @param request: AddStoryFilesRequest
        @return: AddStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_story_files_with_options_async(request, runtime)

    def attach_ossbucket_with_options(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary 绑定ossbucket
        
        @param request: AttachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AttachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ossbucket_with_options_async(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary 绑定ossbucket
        
        @param request: AttachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.AttachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ossbucket(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary 绑定ossbucket
        
        @param request: AttachOSSBucketRequest
        @return: AttachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_ossbucket_with_options(request, runtime)

    async def attach_ossbucket_async(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        """
        @summary 绑定ossbucket
        
        @param request: AttachOSSBucketRequest
        @return: AttachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_ossbucket_with_options_async(request, runtime)

    def batch_delete_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchDeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary 批量删除文件元信息
        
        @param tmp_req: BatchDeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchDeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary 批量删除文件元信息
        
        @param tmp_req: BatchDeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchDeleteFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchDeleteFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_file_meta(
        self,
        request: imm_20200930_models.BatchDeleteFileMetaRequest,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary 批量删除文件元信息
        
        @param request: BatchDeleteFileMetaRequest
        @return: BatchDeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    async def batch_delete_file_meta_async(
        self,
        request: imm_20200930_models.BatchDeleteFileMetaRequest,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        """
        @summary 批量删除文件元信息
        
        @param request: BatchDeleteFileMetaRequest
        @return: BatchDeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_file_meta_with_options_async(request, runtime)

    def batch_get_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.BatchGetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary 批量获取分组信息
        
        @param tmp_req: BatchGetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchGetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary 批量获取分组信息
        
        @param tmp_req: BatchGetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.object_ids):
            request.object_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_figure_cluster(
        self,
        request: imm_20200930_models.BatchGetFigureClusterRequest,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary 批量获取分组信息
        
        @param request: BatchGetFigureClusterRequest
        @return: BatchGetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_figure_cluster_with_options(request, runtime)

    async def batch_get_figure_cluster_async(
        self,
        request: imm_20200930_models.BatchGetFigureClusterRequest,
    ) -> imm_20200930_models.BatchGetFigureClusterResponse:
        """
        @summary 批量获取分组信息
        
        @param request: BatchGetFigureClusterRequest
        @return: BatchGetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_figure_cluster_with_options_async(request, runtime)

    def batch_get_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchGetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary 批量获取文件元信息
        
        @param tmp_req: BatchGetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchGetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary 批量获取文件元信息
        
        @param tmp_req: BatchGetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchGetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.uris):
            request.uris_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_file_meta(
        self,
        request: imm_20200930_models.BatchGetFileMetaRequest,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary 批量获取文件元信息
        
        @param request: BatchGetFileMetaRequest
        @return: BatchGetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_get_file_meta_with_options(request, runtime)

    async def batch_get_file_meta_async(
        self,
        request: imm_20200930_models.BatchGetFileMetaRequest,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        """
        @summary 批量获取文件元信息
        
        @param request: BatchGetFileMetaRequest
        @return: BatchGetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_file_meta_with_options_async(request, runtime)

    def batch_index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchIndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary 批量索引文件元信息
        
        @param tmp_req: BatchIndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchIndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_index_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchIndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary 批量索引文件元信息
        
        @param tmp_req: BatchIndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchIndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_index_file_meta(
        self,
        request: imm_20200930_models.BatchIndexFileMetaRequest,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary 批量索引文件元信息
        
        @param request: BatchIndexFileMetaRequest
        @return: BatchIndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_index_file_meta_with_options(request, runtime)

    async def batch_index_file_meta_async(
        self,
        request: imm_20200930_models.BatchIndexFileMetaRequest,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        """
        @summary 批量索引文件元信息
        
        @param request: BatchIndexFileMetaRequest
        @return: BatchIndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_index_file_meta_with_options_async(request, runtime)

    def batch_update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchUpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary 批量更新文件元信息
        
        @param tmp_req: BatchUpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchUpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.BatchUpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary 批量更新文件元信息
        
        @param tmp_req: BatchUpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchUpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchUpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_file_meta(
        self,
        request: imm_20200930_models.BatchUpdateFileMetaRequest,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary 批量更新文件元信息
        
        @param request: BatchUpdateFileMetaRequest
        @return: BatchUpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    async def batch_update_file_meta_async(
        self,
        request: imm_20200930_models.BatchUpdateFileMetaRequest,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        """
        @summary 批量更新文件元信息
        
        @param request: BatchUpdateFileMetaRequest
        @return: BatchUpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_file_meta_with_options_async(request, runtime)

    def compare_image_faces_with_options(
        self,
        tmp_req: imm_20200930_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary 以脸搜分组
        
        @param tmp_req: CompareImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CompareImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CompareImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_image_faces_with_options_async(
        self,
        tmp_req: imm_20200930_models.CompareImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary 以脸搜分组
        
        @param tmp_req: CompareImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CompareImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CompareImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.source):
            request.source_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompareImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CompareImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_image_faces(
        self,
        request: imm_20200930_models.CompareImageFacesRequest,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary 以脸搜分组
        
        @param request: CompareImageFacesRequest
        @return: CompareImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    async def compare_image_faces_async(
        self,
        request: imm_20200930_models.CompareImageFacesRequest,
    ) -> imm_20200930_models.CompareImageFacesResponse:
        """
        @summary 以脸搜分组
        
        @param request: CompareImageFacesRequest
        @return: CompareImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.compare_image_faces_with_options_async(request, runtime)

    def create_archive_file_inspection_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary 创建查看压缩包内文件列表任务
        
        @param tmp_req: CreateArchiveFileInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArchiveFileInspectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateArchiveFileInspectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArchiveFileInspectionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateArchiveFileInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_archive_file_inspection_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary 创建查看压缩包内文件列表任务
        
        @param tmp_req: CreateArchiveFileInspectionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArchiveFileInspectionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateArchiveFileInspectionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArchiveFileInspectionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateArchiveFileInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_archive_file_inspection_task(
        self,
        request: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary 创建查看压缩包内文件列表任务
        
        @param request: CreateArchiveFileInspectionTaskRequest
        @return: CreateArchiveFileInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_archive_file_inspection_task_with_options(request, runtime)

    async def create_archive_file_inspection_task_async(
        self,
        request: imm_20200930_models.CreateArchiveFileInspectionTaskRequest,
    ) -> imm_20200930_models.CreateArchiveFileInspectionTaskResponse:
        """
        @summary 创建查看压缩包内文件列表任务
        
        @param request: CreateArchiveFileInspectionTaskRequest
        @return: CreateArchiveFileInspectionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_archive_file_inspection_task_with_options_async(request, runtime)

    def create_batch_with_options(
        self,
        tmp_req: imm_20200930_models.CreateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary 创建数据接入
        
        @param tmp_req: CreateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary 创建数据接入
        
        @param tmp_req: CreateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch(
        self,
        request: imm_20200930_models.CreateBatchRequest,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary 创建数据接入
        
        @param request: CreateBatchRequest
        @return: CreateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_batch_with_options(request, runtime)

    async def create_batch_async(
        self,
        request: imm_20200930_models.CreateBatchRequest,
    ) -> imm_20200930_models.CreateBatchResponse:
        """
        @summary 创建数据接入
        
        @param request: CreateBatchRequest
        @return: CreateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_batch_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary 创建绑定
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary 创建绑定
        
        @param request: CreateBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_binding(
        self,
        request: imm_20200930_models.CreateBindingRequest,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary 创建绑定
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
    ) -> imm_20200930_models.CreateBindingResponse:
        """
        @summary 创建绑定
        
        @param request: CreateBindingRequest
        @return: CreateBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_compress_point_cloud_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateCompressPointCloudTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary 创建点云压缩任务
        
        @param tmp_req: CreateCompressPointCloudTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompressPointCloudTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCompressPointCloudTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.kdtree_option):
            request.kdtree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.octree_option):
            request.octree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not UtilClient.is_unset(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not UtilClient.is_unset(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCompressPointCloudTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCompressPointCloudTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compress_point_cloud_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateCompressPointCloudTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary 创建点云压缩任务
        
        @param tmp_req: CreateCompressPointCloudTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCompressPointCloudTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCompressPointCloudTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.kdtree_option):
            request.kdtree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.octree_option):
            request.octree_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not UtilClient.is_unset(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not UtilClient.is_unset(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not UtilClient.is_unset(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCompressPointCloudTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCompressPointCloudTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compress_point_cloud_task(
        self,
        request: imm_20200930_models.CreateCompressPointCloudTaskRequest,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary 创建点云压缩任务
        
        @param request: CreateCompressPointCloudTaskRequest
        @return: CreateCompressPointCloudTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_compress_point_cloud_task_with_options(request, runtime)

    async def create_compress_point_cloud_task_async(
        self,
        request: imm_20200930_models.CreateCompressPointCloudTaskRequest,
    ) -> imm_20200930_models.CreateCompressPointCloudTaskResponse:
        """
        @summary 创建点云压缩任务
        
        @param request: CreateCompressPointCloudTaskRequest
        @return: CreateCompressPointCloudTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_compress_point_cloud_task_with_options_async(request, runtime)

    def create_customized_story_with_options(
        self,
        tmp_req: imm_20200930_models.CreateCustomizedStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param tmp_req: CreateCustomizedStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCustomizedStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCustomizedStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customized_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateCustomizedStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param tmp_req: CreateCustomizedStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCustomizedStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateCustomizedStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCustomizedStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateCustomizedStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customized_story(
        self,
        request: imm_20200930_models.CreateCustomizedStoryRequest,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_customized_story_with_options(request, runtime)

    async def create_customized_story_async(
        self,
        request: imm_20200930_models.CreateCustomizedStoryRequest,
    ) -> imm_20200930_models.CreateCustomizedStoryResponse:
        """
        @summary 创建自定义故事
        
        @param request: CreateCustomizedStoryRequest
        @return: CreateCustomizedStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_customized_story_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
    ) -> imm_20200930_models.CreateDatasetResponse:
        """
        @summary 创建数据集
        
        @param request: CreateDatasetRequest
        @return: CreateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_decode_blind_watermark_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary 提取盲水印
        
        @param tmp_req: CreateDecodeBlindWatermarkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDecodeBlindWatermarkTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_decode_blind_watermark_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary 提取盲水印
        
        @param tmp_req: CreateDecodeBlindWatermarkTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.model):
            query['Model'] = request.model
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDecodeBlindWatermarkTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_decode_blind_watermark_task(
        self,
        request: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary 提取盲水印
        
        @param request: CreateDecodeBlindWatermarkTaskRequest
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_decode_blind_watermark_task_with_options(request, runtime)

    async def create_decode_blind_watermark_task_async(
        self,
        request: imm_20200930_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> imm_20200930_models.CreateDecodeBlindWatermarkTaskResponse:
        """
        @summary 提取盲水印
        
        @param request: CreateDecodeBlindWatermarkTaskRequest
        @return: CreateDecodeBlindWatermarkTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_decode_blind_watermark_task_with_options_async(request, runtime)

    def create_faces_searching_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFacesSearchingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary 以脸搜图
        
        @param tmp_req: CreateFacesSearchingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFacesSearchingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFacesSearchingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFacesSearchingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFacesSearchingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_faces_searching_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFacesSearchingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary 以脸搜图
        
        @param tmp_req: CreateFacesSearchingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFacesSearchingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFacesSearchingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFacesSearchingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFacesSearchingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_faces_searching_task(
        self,
        request: imm_20200930_models.CreateFacesSearchingTaskRequest,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary 以脸搜图
        
        @param request: CreateFacesSearchingTaskRequest
        @return: CreateFacesSearchingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_faces_searching_task_with_options(request, runtime)

    async def create_faces_searching_task_async(
        self,
        request: imm_20200930_models.CreateFacesSearchingTaskRequest,
    ) -> imm_20200930_models.CreateFacesSearchingTaskResponse:
        """
        @summary 以脸搜图
        
        @param request: CreateFacesSearchingTaskRequest
        @return: CreateFacesSearchingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_faces_searching_task_with_options_async(request, runtime)

    def create_figure_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary 聚类
        
        @param tmp_req: CreateFigureClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFigureClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary 聚类
        
        @param tmp_req: CreateFigureClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clustering_task(
        self,
        request: imm_20200930_models.CreateFigureClusteringTaskRequest,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary 聚类
        
        @param request: CreateFigureClusteringTaskRequest
        @return: CreateFigureClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clustering_task_with_options(request, runtime)

    async def create_figure_clustering_task_async(
        self,
        request: imm_20200930_models.CreateFigureClusteringTaskRequest,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        """
        @summary 聚类
        
        @param request: CreateFigureClusteringTaskRequest
        @return: CreateFigureClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clustering_task_with_options_async(request, runtime)

    def create_figure_clusters_merging_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary 合并聚类
        
        @param tmp_req: CreateFigureClustersMergingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClustersMergingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.froms):
            request.froms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClustersMergingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClustersMergingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clusters_merging_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary 合并聚类
        
        @param tmp_req: CreateFigureClustersMergingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFigureClustersMergingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.froms):
            request.froms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFigureClustersMergingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFigureClustersMergingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clusters_merging_task(
        self,
        request: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary 合并聚类
        
        @param request: CreateFigureClustersMergingTaskRequest
        @return: CreateFigureClustersMergingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clusters_merging_task_with_options(request, runtime)

    async def create_figure_clusters_merging_task_async(
        self,
        request: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        """
        @summary 合并聚类
        
        @param request: CreateFigureClustersMergingTaskRequest
        @return: CreateFigureClustersMergingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clusters_merging_task_with_options_async(request, runtime)

    def create_file_compression_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFileCompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary 压缩/打包下载API
        
        @param tmp_req: CreateFileCompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileCompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileCompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileCompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileCompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_compression_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFileCompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary 压缩/打包下载API
        
        @param tmp_req: CreateFileCompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileCompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileCompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not UtilClient.is_unset(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileCompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileCompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_compression_task(
        self,
        request: imm_20200930_models.CreateFileCompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary 压缩/打包下载API
        
        @param request: CreateFileCompressionTaskRequest
        @return: CreateFileCompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_compression_task_with_options(request, runtime)

    async def create_file_compression_task_async(
        self,
        request: imm_20200930_models.CreateFileCompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileCompressionTaskResponse:
        """
        @summary 压缩/打包下载API
        
        @param request: CreateFileCompressionTaskRequest
        @return: CreateFileCompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_compression_task_with_options_async(request, runtime)

    def create_file_uncompression_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFileUncompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary 在线解压API
        
        @param tmp_req: CreateFileUncompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileUncompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileUncompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.selected_files):
            request.selected_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileUncompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileUncompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_uncompression_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateFileUncompressionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary 在线解压API
        
        @param tmp_req: CreateFileUncompressionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFileUncompressionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFileUncompressionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.selected_files):
            request.selected_files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFileUncompressionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateFileUncompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_uncompression_task(
        self,
        request: imm_20200930_models.CreateFileUncompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary 在线解压API
        
        @param request: CreateFileUncompressionTaskRequest
        @return: CreateFileUncompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_file_uncompression_task_with_options(request, runtime)

    async def create_file_uncompression_task_async(
        self,
        request: imm_20200930_models.CreateFileUncompressionTaskRequest,
    ) -> imm_20200930_models.CreateFileUncompressionTaskResponse:
        """
        @summary 在线解压API
        
        @param request: CreateFileUncompressionTaskRequest
        @return: CreateFileUncompressionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_file_uncompression_task_with_options_async(request, runtime)

    def create_image_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary 创建图片检测
        
        @param tmp_req: CreateImageModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_moderation_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary 创建图片检测
        
        @param tmp_req: CreateImageModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_moderation_task(
        self,
        request: imm_20200930_models.CreateImageModerationTaskRequest,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary 创建图片检测
        
        @param request: CreateImageModerationTaskRequest
        @return: CreateImageModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_moderation_task_with_options(request, runtime)

    async def create_image_moderation_task_async(
        self,
        request: imm_20200930_models.CreateImageModerationTaskRequest,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        """
        @summary 创建图片检测
        
        @param request: CreateImageModerationTaskRequest
        @return: CreateImageModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_moderation_task_with_options_async(request, runtime)

    def create_image_splicing_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageSplicingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary 图片拼接
        
        @param tmp_req: CreateImageSplicingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageSplicingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.align):
            query['Align'] = request.align
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.margin):
            query['Margin'] = request.margin
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.padding):
            query['Padding'] = request.padding
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageSplicingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageSplicingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_splicing_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageSplicingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary 图片拼接
        
        @param tmp_req: CreateImageSplicingTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageSplicingTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.align):
            query['Align'] = request.align
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.image_format):
            query['ImageFormat'] = request.image_format
        if not UtilClient.is_unset(request.margin):
            query['Margin'] = request.margin
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.padding):
            query['Padding'] = request.padding
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageSplicingTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageSplicingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_splicing_task(
        self,
        request: imm_20200930_models.CreateImageSplicingTaskRequest,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary 图片拼接
        
        @param request: CreateImageSplicingTaskRequest
        @return: CreateImageSplicingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_splicing_task_with_options(request, runtime)

    async def create_image_splicing_task_async(
        self,
        request: imm_20200930_models.CreateImageSplicingTaskRequest,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        """
        @summary 图片拼接
        
        @param request: CreateImageSplicingTaskRequest
        @return: CreateImageSplicingTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_splicing_task_with_options_async(request, runtime)

    def create_image_to_pdftask_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageToPDFTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary 图片转PDF
        
        @param tmp_req: CreateImageToPDFTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageToPDFTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageToPDFTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageToPDFTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageToPDFTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_to_pdftask_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateImageToPDFTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary 图片转PDF
        
        @param tmp_req: CreateImageToPDFTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateImageToPDFTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageToPDFTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateImageToPDFTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateImageToPDFTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_to_pdftask(
        self,
        request: imm_20200930_models.CreateImageToPDFTaskRequest,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary 图片转PDF
        
        @param request: CreateImageToPDFTaskRequest
        @return: CreateImageToPDFTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_image_to_pdftask_with_options(request, runtime)

    async def create_image_to_pdftask_async(
        self,
        request: imm_20200930_models.CreateImageToPDFTaskRequest,
    ) -> imm_20200930_models.CreateImageToPDFTaskResponse:
        """
        @summary 图片转PDF
        
        @param request: CreateImageToPDFTaskRequest
        @return: CreateImageToPDFTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_image_to_pdftask_with_options_async(request, runtime)

    def create_location_date_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary 创建时空聚类任务
        
        @param tmp_req: CreateLocationDateClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLocationDateClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateLocationDateClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.date_options):
            request.date_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.location_options):
            request.location_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not UtilClient.is_unset(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocationDateClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateLocationDateClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_location_date_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary 创建时空聚类任务
        
        @param tmp_req: CreateLocationDateClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateLocationDateClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateLocationDateClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.date_options):
            request.date_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not UtilClient.is_unset(tmp_req.location_options):
            request.location_options_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not UtilClient.is_unset(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocationDateClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateLocationDateClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_location_date_clustering_task(
        self,
        request: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary 创建时空聚类任务
        
        @param request: CreateLocationDateClusteringTaskRequest
        @return: CreateLocationDateClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_location_date_clustering_task_with_options(request, runtime)

    async def create_location_date_clustering_task_async(
        self,
        request: imm_20200930_models.CreateLocationDateClusteringTaskRequest,
    ) -> imm_20200930_models.CreateLocationDateClusteringTaskResponse:
        """
        @summary 创建时空聚类任务
        
        @param request: CreateLocationDateClusteringTaskRequest
        @return: CreateLocationDateClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_location_date_clustering_task_with_options_async(request, runtime)

    def create_media_convert_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateMediaConvertTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary 创建转码服务
        
        @param tmp_req: CreateMediaConvertTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMediaConvertTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMediaConvertTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateMediaConvertTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_media_convert_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateMediaConvertTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary 创建转码服务
        
        @param tmp_req: CreateMediaConvertTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateMediaConvertTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMediaConvertTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateMediaConvertTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_media_convert_task(
        self,
        request: imm_20200930_models.CreateMediaConvertTaskRequest,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary 创建转码服务
        
        @param request: CreateMediaConvertTaskRequest
        @return: CreateMediaConvertTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_media_convert_task_with_options(request, runtime)

    async def create_media_convert_task_async(
        self,
        request: imm_20200930_models.CreateMediaConvertTaskRequest,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        """
        @summary 创建转码服务
        
        @param request: CreateMediaConvertTaskRequest
        @return: CreateMediaConvertTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_media_convert_task_with_options_async(request, runtime)

    def create_office_conversion_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary 创建文档转换任务
        
        @param tmp_req: CreateOfficeConversionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOfficeConversionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.first_page):
            query['FirstPage'] = request.first_page
        if not UtilClient.is_unset(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not UtilClient.is_unset(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not UtilClient.is_unset(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not UtilClient.is_unset(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not UtilClient.is_unset(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not UtilClient.is_unset(request.long_text):
            query['LongText'] = request.long_text
        if not UtilClient.is_unset(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not UtilClient.is_unset(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not UtilClient.is_unset(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not UtilClient.is_unset(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not UtilClient.is_unset(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not UtilClient.is_unset(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary 创建文档转换任务
        
        @param tmp_req: CreateOfficeConversionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateOfficeConversionTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.end_page):
            query['EndPage'] = request.end_page
        if not UtilClient.is_unset(request.first_page):
            query['FirstPage'] = request.first_page
        if not UtilClient.is_unset(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not UtilClient.is_unset(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not UtilClient.is_unset(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not UtilClient.is_unset(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not UtilClient.is_unset(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not UtilClient.is_unset(request.long_text):
            query['LongText'] = request.long_text
        if not UtilClient.is_unset(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not UtilClient.is_unset(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.pages):
            query['Pages'] = request.pages
        if not UtilClient.is_unset(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not UtilClient.is_unset(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.quality):
            query['Quality'] = request.quality
        if not UtilClient.is_unset(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not UtilClient.is_unset(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not UtilClient.is_unset(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not UtilClient.is_unset(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.start_page):
            query['StartPage'] = request.start_page
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not UtilClient.is_unset(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not UtilClient.is_unset(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_office_conversion_task(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary 创建文档转换任务
        
        @param request: CreateOfficeConversionTaskRequest
        @return: CreateOfficeConversionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    async def create_office_conversion_task_async(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        """
        @summary 创建文档转换任务
        
        @param request: CreateOfficeConversionTaskRequest
        @return: CreateOfficeConversionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_office_conversion_task_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param tmp_req: CreateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: imm_20200930_models.CreateProjectRequest,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: imm_20200930_models.CreateProjectRequest,
    ) -> imm_20200930_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_similar_image_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param tmp_req: CreateSimilarImageClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateSimilarImageClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateSimilarImageClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_similar_image_clustering_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param tmp_req: CreateSimilarImageClusteringTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSimilarImageClusteringTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateSimilarImageClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSimilarImageClusteringTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateSimilarImageClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_similar_image_clustering_task(
        self,
        request: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusteringTaskRequest
        @return: CreateSimilarImageClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_similar_image_clustering_task_with_options(request, runtime)

    async def create_similar_image_clustering_task_async(
        self,
        request: imm_20200930_models.CreateSimilarImageClusteringTaskRequest,
    ) -> imm_20200930_models.CreateSimilarImageClusteringTaskResponse:
        """
        @summary 创建相似图片聚类任务
        
        @param request: CreateSimilarImageClusteringTaskRequest
        @return: CreateSimilarImageClusteringTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_similar_image_clustering_task_with_options_async(request, runtime)

    def create_story_with_options(
        self,
        tmp_req: imm_20200930_models.CreateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary 创建一个 Story
        
        @param tmp_req: CreateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.address_shrink):
            body['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not UtilClient.is_unset(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not UtilClient.is_unset(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary 创建一个 Story
        
        @param tmp_req: CreateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not UtilClient.is_unset(request.address_shrink):
            body['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not UtilClient.is_unset(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not UtilClient.is_unset(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not UtilClient.is_unset(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_story(
        self,
        request: imm_20200930_models.CreateStoryRequest,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary 创建一个 Story
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_story_with_options(request, runtime)

    async def create_story_async(
        self,
        request: imm_20200930_models.CreateStoryRequest,
    ) -> imm_20200930_models.CreateStoryResponse:
        """
        @summary 创建一个 Story
        
        @param request: CreateStoryRequest
        @return: CreateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_story_with_options_async(request, runtime)

    def create_trigger_with_options(
        self,
        tmp_req: imm_20200930_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary 创建数据接入
        
        @param tmp_req: CreateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary 创建数据接入
        
        @param tmp_req: CreateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            body['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        request: imm_20200930_models.CreateTriggerRequest,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary 创建数据接入
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    async def create_trigger_async(
        self,
        request: imm_20200930_models.CreateTriggerRequest,
    ) -> imm_20200930_models.CreateTriggerResponse:
        """
        @summary 创建数据接入
        
        @param request: CreateTriggerRequest
        @return: CreateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_trigger_with_options_async(request, runtime)

    def create_video_label_classification_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary 检测视频中的内容
        
        @param tmp_req: CreateVideoLabelClassificationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoLabelClassificationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoLabelClassificationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoLabelClassificationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoLabelClassificationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_label_classification_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary 检测视频中的内容
        
        @param tmp_req: CreateVideoLabelClassificationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoLabelClassificationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoLabelClassificationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoLabelClassificationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoLabelClassificationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_label_classification_task(
        self,
        request: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary 检测视频中的内容
        
        @param request: CreateVideoLabelClassificationTaskRequest
        @return: CreateVideoLabelClassificationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_video_label_classification_task_with_options(request, runtime)

    async def create_video_label_classification_task_async(
        self,
        request: imm_20200930_models.CreateVideoLabelClassificationTaskRequest,
    ) -> imm_20200930_models.CreateVideoLabelClassificationTaskResponse:
        """
        @summary 检测视频中的内容
        
        @param request: CreateVideoLabelClassificationTaskRequest
        @return: CreateVideoLabelClassificationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_video_label_classification_task_with_options_async(request, runtime)

    def create_video_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateVideoModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary 创建视频检测
        
        @param tmp_req: CreateVideoModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_moderation_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateVideoModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary 创建视频检测
        
        @param tmp_req: CreateVideoModerationTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVideoModerationTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.scenes):
            request.scenes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVideoModerationTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateVideoModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_moderation_task(
        self,
        request: imm_20200930_models.CreateVideoModerationTaskRequest,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary 创建视频检测
        
        @param request: CreateVideoModerationTaskRequest
        @return: CreateVideoModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_video_moderation_task_with_options(request, runtime)

    async def create_video_moderation_task_async(
        self,
        request: imm_20200930_models.CreateVideoModerationTaskRequest,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        """
        @summary 创建视频检测
        
        @param request: CreateVideoModerationTaskRequest
        @return: CreateVideoModerationTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_video_moderation_task_with_options_async(request, runtime)

    def delete_batch_with_options(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_with_options_async(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteBatchRequest
        @return: DeleteBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_batch_with_options(request, runtime)

    async def delete_batch_async(
        self,
        request: imm_20200930_models.DeleteBatchRequest,
    ) -> imm_20200930_models.DeleteBatchResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteBatchRequest
        @return: DeleteBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_batch_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary 删除绑定
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary 删除绑定
        
        @param request: DeleteBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_binding(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary 删除绑定
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
    ) -> imm_20200930_models.DeleteBindingResponse:
        """
        @summary 删除绑定
        
        @param request: DeleteBindingRequest
        @return: DeleteBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary 删除媒体集
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary 删除媒体集
        
        @param request: DeleteDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary 删除媒体集
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        """
        @summary 删除媒体集
        
        @param request: DeleteDatasetRequest
        @return: DeleteDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_file_meta_with_options(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary 删除文件元信息
        
        @param request: DeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_meta_with_options_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary 删除文件元信息
        
        @param request: DeleteFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFileMetaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_meta(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary 删除文件元信息
        
        @param request: DeleteFileMetaRequest
        @return: DeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    async def delete_file_meta_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        """
        @summary 删除文件元信息
        
        @param request: DeleteFileMetaRequest
        @return: DeleteFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_meta_with_options_async(request, runtime)

    def delete_location_date_cluster_with_options(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary 删除时空聚类
        
        @param request: DeleteLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLocationDateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_location_date_cluster_with_options_async(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary 删除时空聚类
        
        @param request: DeleteLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteLocationDateClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_location_date_cluster(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary 删除时空聚类
        
        @param request: DeleteLocationDateClusterRequest
        @return: DeleteLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_location_date_cluster_with_options(request, runtime)

    async def delete_location_date_cluster_async(
        self,
        request: imm_20200930_models.DeleteLocationDateClusterRequest,
    ) -> imm_20200930_models.DeleteLocationDateClusterResponse:
        """
        @summary 删除时空聚类
        
        @param request: DeleteLocationDateClusterRequest
        @return: DeleteLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_location_date_cluster_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
    ) -> imm_20200930_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param request: DeleteProjectRequest
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_story_with_options(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary 删除一个 Story
        
        @param request: DeleteStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_story_with_options_async(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary 删除一个 Story
        
        @param request: DeleteStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_story(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary 删除一个 Story
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_story_with_options(request, runtime)

    async def delete_story_async(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
    ) -> imm_20200930_models.DeleteStoryResponse:
        """
        @summary 删除一个 Story
        
        @param request: DeleteStoryRequest
        @return: DeleteStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_story_with_options_async(request, runtime)

    def delete_trigger_with_options(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteTriggerRequest
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    async def delete_trigger_async(
        self,
        request: imm_20200930_models.DeleteTriggerRequest,
    ) -> imm_20200930_models.DeleteTriggerResponse:
        """
        @summary 删除数据接入实例
        
        @param request: DeleteTriggerRequest
        @return: DeleteTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_trigger_with_options_async(request, runtime)

    def detach_ossbucket_with_options(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary 解绑ossbucket
        
        @param request: DetachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_ossbucket_with_options_async(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary 解绑ossbucket
        
        @param request: DetachOSSBucketRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachOSSBucketResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachOSSBucket',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_ossbucket(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary 解绑ossbucket
        
        @param request: DetachOSSBucketRequest
        @return: DetachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_ossbucket_with_options(request, runtime)

    async def detach_ossbucket_async(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        """
        @summary 解绑ossbucket
        
        @param request: DetachOSSBucketRequest
        @return: DetachOSSBucketResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_ossbucket_with_options_async(request, runtime)

    def detect_image_bodies_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary 人体检测算子
        
        @param tmp_req: DetectImageBodiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageBodiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageBodiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_bodies_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary 人体检测算子
        
        @param tmp_req: DetectImageBodiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageBodiesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageBodies',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageBodiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_bodies(
        self,
        request: imm_20200930_models.DetectImageBodiesRequest,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary 人体检测算子
        
        @param request: DetectImageBodiesRequest
        @return: DetectImageBodiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    async def detect_image_bodies_async(
        self,
        request: imm_20200930_models.DetectImageBodiesRequest,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        """
        @summary 人体检测算子
        
        @param request: DetectImageBodiesRequest
        @return: DetectImageBodiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_bodies_with_options_async(request, runtime)

    def detect_image_cars_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary 检测图片中车辆信息
        
        @param tmp_req: DetectImageCarsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCarsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCars',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cars_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCarsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary 检测图片中车辆信息
        
        @param tmp_req: DetectImageCarsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCarsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCarsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCars',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cars(
        self,
        request: imm_20200930_models.DetectImageCarsRequest,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary 检测图片中车辆信息
        
        @param request: DetectImageCarsRequest
        @return: DetectImageCarsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cars_with_options(request, runtime)

    async def detect_image_cars_async(
        self,
        request: imm_20200930_models.DetectImageCarsRequest,
    ) -> imm_20200930_models.DetectImageCarsResponse:
        """
        @summary 检测图片中车辆信息
        
        @param request: DetectImageCarsRequest
        @return: DetectImageCarsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_cars_with_options_async(request, runtime)

    def detect_image_codes_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary 获取图片二维码检测
        
        @param tmp_req: DetectImageCodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCodes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_codes_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary 获取图片二维码检测
        
        @param tmp_req: DetectImageCodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCodes',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_codes(
        self,
        request: imm_20200930_models.DetectImageCodesRequest,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary 获取图片二维码检测
        
        @param request: DetectImageCodesRequest
        @return: DetectImageCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_codes_with_options(request, runtime)

    async def detect_image_codes_async(
        self,
        request: imm_20200930_models.DetectImageCodesRequest,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        """
        @summary 获取图片二维码检测
        
        @param request: DetectImageCodesRequest
        @return: DetectImageCodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_codes_with_options_async(request, runtime)

    def detect_image_cropping_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCroppingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary 获取图片裁剪信息
        
        @param tmp_req: DetectImageCroppingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCroppingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCropping',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCroppingResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cropping_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageCroppingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary 获取图片裁剪信息
        
        @param tmp_req: DetectImageCroppingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageCroppingResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageCropping',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageCroppingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cropping(
        self,
        request: imm_20200930_models.DetectImageCroppingRequest,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary 获取图片裁剪信息
        
        @param request: DetectImageCroppingRequest
        @return: DetectImageCroppingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cropping_with_options(request, runtime)

    async def detect_image_cropping_async(
        self,
        request: imm_20200930_models.DetectImageCroppingRequest,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        """
        @summary 获取图片裁剪信息
        
        @param request: DetectImageCroppingRequest
        @return: DetectImageCroppingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_cropping_with_options_async(request, runtime)

    def detect_image_faces_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary 获取图片人脸信息
        
        @param tmp_req: DetectImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_faces_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary 获取图片人脸信息
        
        @param tmp_req: DetectImageFacesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageFacesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageFaces',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_faces(
        self,
        request: imm_20200930_models.DetectImageFacesRequest,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary 获取图片人脸信息
        
        @param request: DetectImageFacesRequest
        @return: DetectImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    async def detect_image_faces_async(
        self,
        request: imm_20200930_models.DetectImageFacesRequest,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        """
        @summary 获取图片人脸信息
        
        @param request: DetectImageFacesRequest
        @return: DetectImageFacesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_faces_with_options_async(request, runtime)

    def detect_image_labels_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary 检测图像中的内容
        
        @param tmp_req: DetectImageLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageLabelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_labels_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary 检测图像中的内容
        
        @param tmp_req: DetectImageLabelsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageLabelsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_labels(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary 检测图像中的内容
        
        @param request: DetectImageLabelsRequest
        @return: DetectImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_labels_with_options(request, runtime)

    async def detect_image_labels_async(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        """
        @summary 检测图像中的内容
        
        @param request: DetectImageLabelsRequest
        @return: DetectImageLabelsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_labels_with_options_async(request, runtime)

    def detect_image_score_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary 获取图片打分
        
        @param tmp_req: DetectImageScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageScoreResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageScore',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_score_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary 获取图片打分
        
        @param tmp_req: DetectImageScoreRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageScoreResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageScore',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_score(
        self,
        request: imm_20200930_models.DetectImageScoreRequest,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary 获取图片打分
        
        @param request: DetectImageScoreRequest
        @return: DetectImageScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_score_with_options(request, runtime)

    async def detect_image_score_async(
        self,
        request: imm_20200930_models.DetectImageScoreRequest,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        """
        @summary 获取图片打分
        
        @param request: DetectImageScoreRequest
        @return: DetectImageScoreResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_score_with_options_async(request, runtime)

    def detect_image_texts_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary 进行图片光学字符检测
        
        @param tmp_req: DetectImageTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageTextsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageTextsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTexts',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_texts_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectImageTextsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary 进行图片光学字符检测
        
        @param tmp_req: DetectImageTextsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectImageTextsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageTextsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectImageTexts',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_texts(
        self,
        request: imm_20200930_models.DetectImageTextsRequest,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary 进行图片光学字符检测
        
        @param request: DetectImageTextsRequest
        @return: DetectImageTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_image_texts_with_options(request, runtime)

    async def detect_image_texts_async(
        self,
        request: imm_20200930_models.DetectImageTextsRequest,
    ) -> imm_20200930_models.DetectImageTextsResponse:
        """
        @summary 进行图片光学字符检测
        
        @param request: DetectImageTextsRequest
        @return: DetectImageTextsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_texts_with_options_async(request, runtime)

    def detect_media_meta_with_options(
        self,
        tmp_req: imm_20200930_models.DetectMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary 获取媒体文件信息
        
        @param tmp_req: DetectMediaMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMediaMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMediaMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_media_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.DetectMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary 获取媒体文件信息
        
        @param tmp_req: DetectMediaMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectMediaMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectMediaMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectMediaMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_media_meta(
        self,
        request: imm_20200930_models.DetectMediaMetaRequest,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary 获取媒体文件信息
        
        @param request: DetectMediaMetaRequest
        @return: DetectMediaMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_media_meta_with_options(request, runtime)

    async def detect_media_meta_async(
        self,
        request: imm_20200930_models.DetectMediaMetaRequest,
    ) -> imm_20200930_models.DetectMediaMetaResponse:
        """
        @summary 获取媒体文件信息
        
        @param request: DetectMediaMetaRequest
        @return: DetectMediaMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_media_meta_with_options_async(request, runtime)

    def detect_text_anomaly_with_options(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary 检测文本
        
        @param request: DetectTextAnomalyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectTextAnomalyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectTextAnomaly',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectTextAnomalyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_text_anomaly_with_options_async(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary 检测文本
        
        @param request: DetectTextAnomalyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetectTextAnomalyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectTextAnomaly',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectTextAnomalyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_text_anomaly(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary 检测文本
        
        @param request: DetectTextAnomalyRequest
        @return: DetectTextAnomalyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detect_text_anomaly_with_options(request, runtime)

    async def detect_text_anomaly_async(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        """
        @summary 检测文本
        
        @param request: DetectTextAnomalyRequest
        @return: DetectTextAnomalyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detect_text_anomaly_with_options_async(request, runtime)

    def encode_blind_watermark_with_options(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary 嵌入图片盲水印算子
        
        @param request: EncodeBlindWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncodeBlindWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.EncodeBlindWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def encode_blind_watermark_with_options_async(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary 嵌入图片盲水印算子
        
        @param request: EncodeBlindWatermarkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EncodeBlindWatermarkResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not UtilClient.is_unset(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EncodeBlindWatermark',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.EncodeBlindWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encode_blind_watermark(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary 嵌入图片盲水印算子
        
        @param request: EncodeBlindWatermarkRequest
        @return: EncodeBlindWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.encode_blind_watermark_with_options(request, runtime)

    async def encode_blind_watermark_async(
        self,
        request: imm_20200930_models.EncodeBlindWatermarkRequest,
    ) -> imm_20200930_models.EncodeBlindWatermarkResponse:
        """
        @summary 嵌入图片盲水印算子
        
        @param request: EncodeBlindWatermarkRequest
        @return: EncodeBlindWatermarkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.encode_blind_watermark_with_options_async(request, runtime)

    def extract_document_text_with_options(
        self,
        tmp_req: imm_20200930_models.ExtractDocumentTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary 提取文档中的文本
        
        @param tmp_req: ExtractDocumentTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractDocumentTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ExtractDocumentTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractDocumentText',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ExtractDocumentTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_document_text_with_options_async(
        self,
        tmp_req: imm_20200930_models.ExtractDocumentTextRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary 提取文档中的文本
        
        @param tmp_req: ExtractDocumentTextRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtractDocumentTextResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ExtractDocumentTextShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExtractDocumentText',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ExtractDocumentTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_document_text(
        self,
        request: imm_20200930_models.ExtractDocumentTextRequest,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary 提取文档中的文本
        
        @param request: ExtractDocumentTextRequest
        @return: ExtractDocumentTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.extract_document_text_with_options(request, runtime)

    async def extract_document_text_async(
        self,
        request: imm_20200930_models.ExtractDocumentTextRequest,
    ) -> imm_20200930_models.ExtractDocumentTextResponse:
        """
        @summary 提取文档中的文本
        
        @param request: ExtractDocumentTextRequest
        @return: ExtractDocumentTextResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.extract_document_text_with_options_async(request, runtime)

    def fuzzy_query_with_options(
        self,
        tmp_req: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary 对 Dataset 内的元数据进行模糊搜索。
        
        @param tmp_req: FuzzyQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.FuzzyQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary 对 Dataset 内的元数据进行模糊搜索。
        
        @param tmp_req: FuzzyQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: FuzzyQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.FuzzyQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_query(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary 对 Dataset 内的元数据进行模糊搜索。
        
        @param request: FuzzyQueryRequest
        @return: FuzzyQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    async def fuzzy_query_async(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        """
        @summary 对 Dataset 内的元数据进行模糊搜索。
        
        @param request: FuzzyQueryRequest
        @return: FuzzyQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_query_with_options_async(request, runtime)

    def generate_video_playlist_with_options(
        self,
        tmp_req: imm_20200930_models.GenerateVideoPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary 创建实时转码任务
        
        @param tmp_req: GenerateVideoPlaylistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoPlaylistResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateVideoPlaylistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.source_subtitles):
            request.source_subtitles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not UtilClient.is_unset(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not UtilClient.is_unset(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateVideoPlaylist',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateVideoPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_video_playlist_with_options_async(
        self,
        tmp_req: imm_20200930_models.GenerateVideoPlaylistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary 创建实时转码任务
        
        @param tmp_req: GenerateVideoPlaylistRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateVideoPlaylistResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateVideoPlaylistShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.source_subtitles):
            request.source_subtitles_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not UtilClient.is_unset(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not UtilClient.is_unset(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateVideoPlaylist',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateVideoPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_video_playlist(
        self,
        request: imm_20200930_models.GenerateVideoPlaylistRequest,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary 创建实时转码任务
        
        @param request: GenerateVideoPlaylistRequest
        @return: GenerateVideoPlaylistResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_video_playlist_with_options(request, runtime)

    async def generate_video_playlist_async(
        self,
        request: imm_20200930_models.GenerateVideoPlaylistRequest,
    ) -> imm_20200930_models.GenerateVideoPlaylistResponse:
        """
        @summary 创建实时转码任务
        
        @param request: GenerateVideoPlaylistRequest
        @return: GenerateVideoPlaylistResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_video_playlist_with_options_async(request, runtime)

    def generate_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.GenerateWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary 获取文档预览编辑凭证
        
        @param tmp_req: GenerateWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not UtilClient.is_unset(request.filename):
            query['Filename'] = request.filename
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not UtilClient.is_unset(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_weboffice_token_with_options_async(
        self,
        tmp_req: imm_20200930_models.GenerateWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary 获取文档预览编辑凭证
        
        @param tmp_req: GenerateWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GenerateWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not UtilClient.is_unset(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not UtilClient.is_unset(request.filename):
            query['Filename'] = request.filename
        if not UtilClient.is_unset(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not UtilClient.is_unset(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.referer):
            query['Referer'] = request.referer
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not UtilClient.is_unset(request.user_shrink):
            query['User'] = request.user_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        if not UtilClient.is_unset(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GenerateWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_weboffice_token(
        self,
        request: imm_20200930_models.GenerateWebofficeTokenRequest,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary 获取文档预览编辑凭证
        
        @param request: GenerateWebofficeTokenRequest
        @return: GenerateWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_weboffice_token_with_options(request, runtime)

    async def generate_weboffice_token_async(
        self,
        request: imm_20200930_models.GenerateWebofficeTokenRequest,
    ) -> imm_20200930_models.GenerateWebofficeTokenResponse:
        """
        @summary 获取文档预览编辑凭证
        
        @param request: GenerateWebofficeTokenRequest
        @return: GenerateWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_weboffice_token_with_options_async(request, runtime)

    def get_batch_with_options(
        self,
        request: imm_20200930_models.GetBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_with_options_async(
        self,
        request: imm_20200930_models.GetBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBatchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch(
        self,
        request: imm_20200930_models.GetBatchRequest,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetBatchRequest
        @return: GetBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_batch_with_options(request, runtime)

    async def get_batch_async(
        self,
        request: imm_20200930_models.GetBatchRequest,
    ) -> imm_20200930_models.GetBatchResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetBatchRequest
        @return: GetBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_with_options_async(request, runtime)

    def get_binding_with_options(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary 获取绑定
        
        @param request: GetBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_with_options_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary 获取绑定
        
        @param request: GetBindingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBindingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding(
        self,
        request: imm_20200930_models.GetBindingRequest,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary 获取绑定
        
        @param request: GetBindingRequest
        @return: GetBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    async def get_binding_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
    ) -> imm_20200930_models.GetBindingResponse:
        """
        @summary 获取绑定
        
        @param request: GetBindingRequest
        @return: GetBindingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_binding_with_options_async(request, runtime)

    def get_drmlicense_with_options(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDRMLicenseResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDRMLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_drmlicense_with_options_async(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDRMLicenseResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_id):
            query['KeyId'] = request.key_id
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDRMLicense',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDRMLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_drmlicense(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @return: GetDRMLicenseResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_drmlicense_with_options(request, runtime)

    async def get_drmlicense_async(
        self,
        request: imm_20200930_models.GetDRMLicenseRequest,
    ) -> imm_20200930_models.GetDRMLicenseResponse:
        """
        @deprecated OpenAPI GetDRMLicense is deprecated
        
        @summary drmlicense获取
        
        @param request: GetDRMLicenseRequest
        @return: GetDRMLicenseResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_drmlicense_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary 获取媒体集信息
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary 获取媒体集信息
        
        @param request: GetDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: imm_20200930_models.GetDatasetRequest,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary 获取媒体集信息
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
    ) -> imm_20200930_models.GetDatasetResponse:
        """
        @summary 获取媒体集信息
        
        @param request: GetDatasetRequest
        @return: GetDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_decode_blind_watermark_result_with_options(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary 获取提取水印的结果
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDecodeBlindWatermarkResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDecodeBlindWatermarkResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDecodeBlindWatermarkResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_decode_blind_watermark_result_with_options_async(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary 获取提取水印的结果
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDecodeBlindWatermarkResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDecodeBlindWatermarkResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDecodeBlindWatermarkResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_decode_blind_watermark_result(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary 获取提取水印的结果
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @return: GetDecodeBlindWatermarkResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_decode_blind_watermark_result_with_options(request, runtime)

    async def get_decode_blind_watermark_result_async(
        self,
        request: imm_20200930_models.GetDecodeBlindWatermarkResultRequest,
    ) -> imm_20200930_models.GetDecodeBlindWatermarkResultResponse:
        """
        @summary 获取提取水印的结果
        
        @param request: GetDecodeBlindWatermarkResultRequest
        @return: GetDecodeBlindWatermarkResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_decode_blind_watermark_result_with_options_async(request, runtime)

    def get_figure_cluster_with_options(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary 获取聚类
        
        @param request: GetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFigureClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_figure_cluster_with_options_async(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary 获取聚类
        
        @param request: GetFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFigureClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_figure_cluster(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary 获取聚类
        
        @param request: GetFigureClusterRequest
        @return: GetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_figure_cluster_with_options(request, runtime)

    async def get_figure_cluster_async(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        """
        @summary 获取聚类
        
        @param request: GetFigureClusterRequest
        @return: GetFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_figure_cluster_with_options_async(request, runtime)

    def get_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary 获取文件元信息
        
        @param tmp_req: GetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary 获取文件元信息
        
        @param tmp_req: GetFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_meta(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary 获取文件元信息
        
        @param request: GetFileMetaRequest
        @return: GetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    async def get_file_meta_async(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
    ) -> imm_20200930_models.GetFileMetaResponse:
        """
        @summary 获取文件元信息
        
        @param request: GetFileMetaRequest
        @return: GetFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_file_meta_with_options_async(request, runtime)

    def get_image_moderation_result_with_options(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary 获取图片审核任务结果
        
        @param request: GetImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_moderation_result_with_options_async(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary 获取图片审核任务结果
        
        @param request: GetImageModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetImageModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_moderation_result(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary 获取图片审核任务结果
        
        @param request: GetImageModerationResultRequest
        @return: GetImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_moderation_result_with_options(request, runtime)

    async def get_image_moderation_result_async(
        self,
        request: imm_20200930_models.GetImageModerationResultRequest,
    ) -> imm_20200930_models.GetImageModerationResultResponse:
        """
        @summary 获取图片审核任务结果
        
        @param request: GetImageModerationResultRequest
        @return: GetImageModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_moderation_result_with_options_async(request, runtime)

    def get_ossbucket_attachment_with_options(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary 获取绑定的ossbucket
        
        @param request: GetOSSBucketAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSBucketAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSBucketAttachment',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOSSBucketAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossbucket_attachment_with_options_async(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary 获取绑定的ossbucket
        
        @param request: GetOSSBucketAttachmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOSSBucketAttachmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOSSBucketAttachment',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOSSBucketAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossbucket_attachment(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary 获取绑定的ossbucket
        
        @param request: GetOSSBucketAttachmentRequest
        @return: GetOSSBucketAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_ossbucket_attachment_with_options(request, runtime)

    async def get_ossbucket_attachment_async(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        """
        @summary 获取绑定的ossbucket
        
        @param request: GetOSSBucketAttachmentRequest
        @return: GetOSSBucketAttachmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_ossbucket_attachment_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary 获取项目信息
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary 获取项目信息
        
        @param request: GetProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: imm_20200930_models.GetProjectRequest,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary 获取项目信息
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
    ) -> imm_20200930_models.GetProjectResponse:
        """
        @summary 获取项目信息
        
        @param request: GetProjectRequest
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_story_with_options(
        self,
        request: imm_20200930_models.GetStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary 返回一个 Story 的详细信息
        
        @param request: GetStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_story_with_options_async(
        self,
        request: imm_20200930_models.GetStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary 返回一个 Story 的详细信息
        
        @param request: GetStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_story(
        self,
        request: imm_20200930_models.GetStoryRequest,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary 返回一个 Story 的详细信息
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_story_with_options(request, runtime)

    async def get_story_async(
        self,
        request: imm_20200930_models.GetStoryRequest,
    ) -> imm_20200930_models.GetStoryResponse:
        """
        @summary 返回一个 Story 的详细信息
        
        @param request: GetStoryRequest
        @return: GetStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_story_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: imm_20200930_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary 获取任务信息
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: imm_20200930_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary 获取任务信息
        
        @param request: GetTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: imm_20200930_models.GetTaskRequest,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary 获取任务信息
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: imm_20200930_models.GetTaskRequest,
    ) -> imm_20200930_models.GetTaskResponse:
        """
        @summary 获取任务信息
        
        @param request: GetTaskRequest
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_trigger_with_options(
        self,
        request: imm_20200930_models.GetTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        request: imm_20200930_models.GetTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTriggerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        request: imm_20200930_models.GetTriggerRequest,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetTriggerRequest
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trigger_with_options(request, runtime)

    async def get_trigger_async(
        self,
        request: imm_20200930_models.GetTriggerRequest,
    ) -> imm_20200930_models.GetTriggerResponse:
        """
        @summary 获取数据接入实例
        
        @param request: GetTriggerRequest
        @return: GetTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_trigger_with_options_async(request, runtime)

    def get_video_label_classification_result_with_options(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary 获取视频标签检测任务结果
        
        @param request: GetVideoLabelClassificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoLabelClassificationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoLabelClassificationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoLabelClassificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_label_classification_result_with_options_async(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary 获取视频标签检测任务结果
        
        @param request: GetVideoLabelClassificationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoLabelClassificationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoLabelClassificationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoLabelClassificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_label_classification_result(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary 获取视频标签检测任务结果
        
        @param request: GetVideoLabelClassificationResultRequest
        @return: GetVideoLabelClassificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_label_classification_result_with_options(request, runtime)

    async def get_video_label_classification_result_async(
        self,
        request: imm_20200930_models.GetVideoLabelClassificationResultRequest,
    ) -> imm_20200930_models.GetVideoLabelClassificationResultResponse:
        """
        @summary 获取视频标签检测任务结果
        
        @param request: GetVideoLabelClassificationResultRequest
        @return: GetVideoLabelClassificationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_video_label_classification_result_with_options_async(request, runtime)

    def get_video_moderation_result_with_options(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_moderation_result_with_options_async(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetVideoModerationResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetVideoModerationResult',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetVideoModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_moderation_result(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @return: GetVideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_video_moderation_result_with_options(request, runtime)

    async def get_video_moderation_result_async(
        self,
        request: imm_20200930_models.GetVideoModerationResultRequest,
    ) -> imm_20200930_models.GetVideoModerationResultResponse:
        """
        @summary 获取视频审核任务结果
        
        @param request: GetVideoModerationResultRequest
        @return: GetVideoModerationResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_video_moderation_result_with_options_async(request, runtime)

    def index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary 添加文件元信息
        
        @param tmp_req: IndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary 添加文件元信息
        
        @param tmp_req: IndexFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IndexFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not UtilClient.is_unset(tmp_req.notification):
            request.notification_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_file_meta(
        self,
        request: imm_20200930_models.IndexFileMetaRequest,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary 添加文件元信息
        
        @param request: IndexFileMetaRequest
        @return: IndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    async def index_file_meta_async(
        self,
        request: imm_20200930_models.IndexFileMetaRequest,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        """
        @summary 添加文件元信息
        
        @param request: IndexFileMetaRequest
        @return: IndexFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.index_file_meta_with_options_async(request, runtime)

    def list_batches_with_options(
        self,
        request: imm_20200930_models.ListBatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListBatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatches',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batches_with_options_async(
        self,
        request: imm_20200930_models.ListBatchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListBatchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBatchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBatches',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batches(
        self,
        request: imm_20200930_models.ListBatchesRequest,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListBatchesRequest
        @return: ListBatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_batches_with_options(request, runtime)

    async def list_batches_async(
        self,
        request: imm_20200930_models.ListBatchesRequest,
    ) -> imm_20200930_models.ListBatchesResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListBatchesRequest
        @return: ListBatchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_batches_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary 列出绑定
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary 列出绑定
        
        @param request: ListBindingsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListBindingsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bindings(
        self,
        request: imm_20200930_models.ListBindingsRequest,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary 列出绑定
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
    ) -> imm_20200930_models.ListBindingsResponse:
        """
        @summary 列出绑定
        
        @param request: ListBindingsRequest
        @return: ListBindingsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary 列出媒体集列表
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary 列出媒体集列表
        
        @param request: ListDatasetsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDatasetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary 列出媒体集列表
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
    ) -> imm_20200930_models.ListDatasetsResponse:
        """
        @summary 列出媒体集列表
        
        @param request: ListDatasetsRequest
        @return: ListDatasetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary 获取项目列表
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary 获取项目列表
        
        @param tmp_req: ListProjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListProjectsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: imm_20200930_models.ListProjectsRequest,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary 获取项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: imm_20200930_models.ListProjectsRequest,
    ) -> imm_20200930_models.ListProjectsResponse:
        """
        @summary 获取项目列表
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: imm_20200930_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary 获取地区列表
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: imm_20200930_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary 获取地区列表
        
        @param request: ListRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: imm_20200930_models.ListRegionsRequest,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary 获取地区列表
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: imm_20200930_models.ListRegionsRequest,
    ) -> imm_20200930_models.ListRegionsResponse:
        """
        @summary 获取地区列表
        
        @param request: ListRegionsRequest
        @return: ListRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: imm_20200930_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary 获取任务信息列表
        
        @param tmp_req: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.task_types):
            request.task_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not UtilClient.is_unset(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: imm_20200930_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary 获取任务信息列表
        
        @param tmp_req: ListTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.task_types):
            request.task_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not UtilClient.is_unset(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: imm_20200930_models.ListTasksRequest,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary 获取任务信息列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: imm_20200930_models.ListTasksRequest,
    ) -> imm_20200930_models.ListTasksResponse:
        """
        @summary 获取任务信息列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_triggers_with_options(
        self,
        request: imm_20200930_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListTriggersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        request: imm_20200930_models.ListTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListTriggersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTriggersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTriggers',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        request: imm_20200930_models.ListTriggersRequest,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    async def list_triggers_async(
        self,
        request: imm_20200930_models.ListTriggersRequest,
    ) -> imm_20200930_models.ListTriggersResponse:
        """
        @summary 列出数据接入实例
        
        @param request: ListTriggersRequest
        @return: ListTriggersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_triggers_with_options_async(request, runtime)

    def query_figure_clusters_with_options(
        self,
        tmp_req: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary 查询聚类分组
        
        @param tmp_req: QueryFigureClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFigureClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryFigureClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not UtilClient.is_unset(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFigureClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryFigureClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_figure_clusters_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary 查询聚类分组
        
        @param tmp_req: QueryFigureClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryFigureClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryFigureClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not UtilClient.is_unset(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFigureClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryFigureClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_figure_clusters(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary 查询聚类分组
        
        @param request: QueryFigureClustersRequest
        @return: QueryFigureClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_figure_clusters_with_options(request, runtime)

    async def query_figure_clusters_async(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        """
        @summary 查询聚类分组
        
        @param request: QueryFigureClustersRequest
        @return: QueryFigureClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_figure_clusters_with_options_async(request, runtime)

    def query_location_date_clusters_with_options(
        self,
        tmp_req: imm_20200930_models.QueryLocationDateClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary 查找时空分组
        
        @param tmp_req: QueryLocationDateClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocationDateClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryLocationDateClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not UtilClient.is_unset(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not UtilClient.is_unset(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocationDateClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryLocationDateClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_location_date_clusters_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryLocationDateClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary 查找时空分组
        
        @param tmp_req: QueryLocationDateClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryLocationDateClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryLocationDateClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.address):
            request.address_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not UtilClient.is_unset(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.update_time_range):
            request.update_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.address_shrink):
            query['Address'] = request.address_shrink
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not UtilClient.is_unset(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not UtilClient.is_unset(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLocationDateClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryLocationDateClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_location_date_clusters(
        self,
        request: imm_20200930_models.QueryLocationDateClustersRequest,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary 查找时空分组
        
        @param request: QueryLocationDateClustersRequest
        @return: QueryLocationDateClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_location_date_clusters_with_options(request, runtime)

    async def query_location_date_clusters_async(
        self,
        request: imm_20200930_models.QueryLocationDateClustersRequest,
    ) -> imm_20200930_models.QueryLocationDateClustersResponse:
        """
        @summary 查找时空分组
        
        @param request: QueryLocationDateClustersRequest
        @return: QueryLocationDateClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_location_date_clusters_with_options_async(request, runtime)

    def query_similar_image_clusters_with_options(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary 查找相似图片分组
        
        @param request: QuerySimilarImageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimilarImageClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QuerySimilarImageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_similar_image_clusters_with_options_async(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary 查找相似图片分组
        
        @param request: QuerySimilarImageClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QuerySimilarImageClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySimilarImageClusters',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QuerySimilarImageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_similar_image_clusters(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary 查找相似图片分组
        
        @param request: QuerySimilarImageClustersRequest
        @return: QuerySimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_similar_image_clusters_with_options(request, runtime)

    async def query_similar_image_clusters_async(
        self,
        request: imm_20200930_models.QuerySimilarImageClustersRequest,
    ) -> imm_20200930_models.QuerySimilarImageClustersResponse:
        """
        @summary 查找相似图片分组
        
        @param request: QuerySimilarImageClustersRequest
        @return: QuerySimilarImageClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_similar_image_clusters_with_options_async(request, runtime)

    def query_stories_with_options(
        self,
        tmp_req: imm_20200930_models.QueryStoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary 查找 Story
        
        @param tmp_req: QueryStoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not UtilClient.is_unset(request.story_name):
            query['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not UtilClient.is_unset(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            query['StoryType'] = request.story_type
        if not UtilClient.is_unset(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryStoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stories_with_options_async(
        self,
        tmp_req: imm_20200930_models.QueryStoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary 查找 Story
        
        @param tmp_req: QueryStoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryStoriesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not UtilClient.is_unset(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not UtilClient.is_unset(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not UtilClient.is_unset(request.story_name):
            query['StoryName'] = request.story_name
        if not UtilClient.is_unset(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not UtilClient.is_unset(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not UtilClient.is_unset(request.story_type):
            query['StoryType'] = request.story_type
        if not UtilClient.is_unset(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStories',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.QueryStoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stories(
        self,
        request: imm_20200930_models.QueryStoriesRequest,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary 查找 Story
        
        @param request: QueryStoriesRequest
        @return: QueryStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_stories_with_options(request, runtime)

    async def query_stories_async(
        self,
        request: imm_20200930_models.QueryStoriesRequest,
    ) -> imm_20200930_models.QueryStoriesResponse:
        """
        @summary 查找 Story
        
        @param request: QueryStoriesRequest
        @return: QueryStoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_stories_with_options_async(request, runtime)

    def refresh_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary 刷新文档预览编辑凭证
        
        @param tmp_req: RefreshWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RefreshWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_weboffice_token_with_options_async(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary 刷新文档预览编辑凭证
        
        @param tmp_req: RefreshWebofficeTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RefreshWebofficeTokenResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_token):
            query['AccessToken'] = request.access_token
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RefreshWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_weboffice_token(
        self,
        request: imm_20200930_models.RefreshWebofficeTokenRequest,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary 刷新文档预览编辑凭证
        
        @param request: RefreshWebofficeTokenRequest
        @return: RefreshWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    async def refresh_weboffice_token_async(
        self,
        request: imm_20200930_models.RefreshWebofficeTokenRequest,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        """
        @summary 刷新文档预览编辑凭证
        
        @param request: RefreshWebofficeTokenRequest
        @return: RefreshWebofficeTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.refresh_weboffice_token_with_options_async(request, runtime)

    def remove_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.RemoveStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary 为故事移除文件
        
        @param tmp_req: RemoveStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RemoveStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RemoveStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_story_files_with_options_async(
        self,
        tmp_req: imm_20200930_models.RemoveStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary 为故事移除文件
        
        @param tmp_req: RemoveStoryFilesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveStoryFilesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RemoveStoryFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            body['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveStoryFiles',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.RemoveStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_story_files(
        self,
        request: imm_20200930_models.RemoveStoryFilesRequest,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary 为故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_story_files_with_options(request, runtime)

    async def remove_story_files_async(
        self,
        request: imm_20200930_models.RemoveStoryFilesRequest,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        """
        @summary 为故事移除文件
        
        @param request: RemoveStoryFilesRequest
        @return: RemoveStoryFilesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_story_files_with_options_async(request, runtime)

    def resume_batch_with_options(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_batch_with_options_async(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_batch(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeBatchRequest
        @return: ResumeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_batch_with_options(request, runtime)

    async def resume_batch_async(
        self,
        request: imm_20200930_models.ResumeBatchRequest,
    ) -> imm_20200930_models.ResumeBatchResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeBatchRequest
        @return: ResumeBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_batch_with_options_async(request, runtime)

    def resume_trigger_with_options(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_trigger_with_options_async(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResumeTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_trigger(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeTriggerRequest
        @return: ResumeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.resume_trigger_with_options(request, runtime)

    async def resume_trigger_async(
        self,
        request: imm_20200930_models.ResumeTriggerRequest,
    ) -> imm_20200930_models.ResumeTriggerResponse:
        """
        @summary 恢复一个挂起的数据接入任务
        
        @param request: ResumeTriggerRequest
        @return: ResumeTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.resume_trigger_with_options_async(request, runtime)

    def search_image_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.SearchImageFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary 以脸搜分组
        
        @param tmp_req: SearchImageFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SearchImageFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SearchImageFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.SearchImageFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary 以脸搜分组
        
        @param tmp_req: SearchImageFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchImageFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SearchImageFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchImageFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SearchImageFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_figure_cluster(
        self,
        request: imm_20200930_models.SearchImageFigureClusterRequest,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary 以脸搜分组
        
        @param request: SearchImageFigureClusterRequest
        @return: SearchImageFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_image_figure_cluster_with_options(request, runtime)

    async def search_image_figure_cluster_async(
        self,
        request: imm_20200930_models.SearchImageFigureClusterRequest,
    ) -> imm_20200930_models.SearchImageFigureClusterResponse:
        """
        @summary 以脸搜分组
        
        @param request: SearchImageFigureClusterRequest
        @return: SearchImageFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_image_figure_cluster_with_options_async(request, runtime)

    def semantic_query_with_options(
        self,
        tmp_req: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary 通过输入自然语言文字，对 Dataset 内的元数据进行查询与统计分析
        
        @param tmp_req: SemanticQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SemanticQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SemanticQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.media_types):
            request.media_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SemanticQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SemanticQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def semantic_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary 通过输入自然语言文字，对 Dataset 内的元数据进行查询与统计分析
        
        @param tmp_req: SemanticQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SemanticQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SemanticQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.media_types):
            request.media_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SemanticQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SemanticQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def semantic_query(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary 通过输入自然语言文字，对 Dataset 内的元数据进行查询与统计分析
        
        @param request: SemanticQueryRequest
        @return: SemanticQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.semantic_query_with_options(request, runtime)

    async def semantic_query_async(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
    ) -> imm_20200930_models.SemanticQueryResponse:
        """
        @summary 通过输入自然语言文字，对 Dataset 内的元数据进行查询与统计分析
        
        @param request: SemanticQueryRequest
        @return: SemanticQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.semantic_query_with_options_async(request, runtime)

    def simple_query_with_options(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary 通过 JSON 结构的查询语言，对 Dataset 内的元数据进行查询与统计分析。
        
        @param tmp_req: SimpleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SimpleQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not UtilClient.is_unset(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary 通过 JSON 结构的查询语言，对 Dataset 内的元数据进行查询与统计分析。
        
        @param tmp_req: SimpleQueryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SimpleQueryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.with_fields):
            request.with_fields_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not UtilClient.is_unset(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.query_shrink):
            query['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort):
            query['Sort'] = request.sort
        if not UtilClient.is_unset(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not UtilClient.is_unset(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_query(
        self,
        request: imm_20200930_models.SimpleQueryRequest,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary 通过 JSON 结构的查询语言，对 Dataset 内的元数据进行查询与统计分析。
        
        @param request: SimpleQueryRequest
        @return: SimpleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    async def simple_query_async(
        self,
        request: imm_20200930_models.SimpleQueryRequest,
    ) -> imm_20200930_models.SimpleQueryResponse:
        """
        @summary 通过 JSON 结构的查询语言，对 Dataset 内的元数据进行查询与统计分析。
        
        @param request: SimpleQueryRequest
        @return: SimpleQueryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.simple_query_with_options_async(request, runtime)

    def suspend_batch_with_options(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_batch_with_options_async(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendBatchResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_batch(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendBatchRequest
        @return: SuspendBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_batch_with_options(request, runtime)

    async def suspend_batch_async(
        self,
        request: imm_20200930_models.SuspendBatchRequest,
    ) -> imm_20200930_models.SuspendBatchResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendBatchRequest
        @return: SuspendBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_batch_with_options_async(request, runtime)

    def suspend_trigger_with_options(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_trigger_with_options_async(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SuspendTriggerResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.SuspendTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_trigger(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendTriggerRequest
        @return: SuspendTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.suspend_trigger_with_options(request, runtime)

    async def suspend_trigger_async(
        self,
        request: imm_20200930_models.SuspendTriggerRequest,
    ) -> imm_20200930_models.SuspendTriggerResponse:
        """
        @summary 挂起一个数据接入任务
        
        @param request: SuspendTriggerRequest
        @return: SuspendTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.suspend_trigger_with_options_async(request, runtime)

    def update_batch_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary 更新数据接入实例
        
        @param tmp_req: UpdateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateBatchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary 更新数据接入实例
        
        @param tmp_req: UpdateBatchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBatchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateBatchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateBatch',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch(
        self,
        request: imm_20200930_models.UpdateBatchRequest,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary 更新数据接入实例
        
        @param request: UpdateBatchRequest
        @return: UpdateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_batch_with_options(request, runtime)

    async def update_batch_async(
        self,
        request: imm_20200930_models.UpdateBatchRequest,
    ) -> imm_20200930_models.UpdateBatchResponse:
        """
        @summary 更新数据接入实例
        
        @param request: UpdateBatchRequest
        @return: UpdateBatchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_batch_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary 更新媒体集
        
        @param request: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary 更新媒体集
        
        @param request: UpdateDatasetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateDatasetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary 更新媒体集
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        """
        @summary 更新媒体集
        
        @param request: UpdateDatasetRequest
        @return: UpdateDatasetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary 更新聚类
        
        @param tmp_req: UpdateFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_figure_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary 更新聚类
        
        @param tmp_req: UpdateFigureClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFigureClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFigureCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_figure_cluster(
        self,
        request: imm_20200930_models.UpdateFigureClusterRequest,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary 更新聚类
        
        @param request: UpdateFigureClusterRequest
        @return: UpdateFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_figure_cluster_with_options(request, runtime)

    async def update_figure_cluster_async(
        self,
        request: imm_20200930_models.UpdateFigureClusterRequest,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        """
        @summary 更新聚类
        
        @param request: UpdateFigureClusterRequest
        @return: UpdateFigureClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_figure_cluster_with_options_async(request, runtime)

    def update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary 更新文件元信息
        
        @param tmp_req: UpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary 更新文件元信息
        
        @param tmp_req: UpdateFileMetaRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateFileMetaResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_meta(
        self,
        request: imm_20200930_models.UpdateFileMetaRequest,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary 更新文件元信息
        
        @param request: UpdateFileMetaRequest
        @return: UpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    async def update_file_meta_async(
        self,
        request: imm_20200930_models.UpdateFileMetaRequest,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        """
        @summary 更新文件元信息
        
        @param request: UpdateFileMetaRequest
        @return: UpdateFileMetaResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_file_meta_with_options_async(request, runtime)

    def update_location_date_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary 更新时空聚类
        
        @param tmp_req: UpdateLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocationDateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateLocationDateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_id):
            query['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_location_date_cluster_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateLocationDateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary 更新时空聚类
        
        @param tmp_req: UpdateLocationDateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLocationDateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateLocationDateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not UtilClient.is_unset(request.custom_id):
            query['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            query['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLocationDateCluster',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_location_date_cluster(
        self,
        request: imm_20200930_models.UpdateLocationDateClusterRequest,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary 更新时空聚类
        
        @param request: UpdateLocationDateClusterRequest
        @return: UpdateLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_location_date_cluster_with_options(request, runtime)

    async def update_location_date_cluster_async(
        self,
        request: imm_20200930_models.UpdateLocationDateClusterRequest,
    ) -> imm_20200930_models.UpdateLocationDateClusterResponse:
        """
        @summary 更新时空聚类
        
        @param request: UpdateLocationDateClusterRequest
        @return: UpdateLocationDateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_location_date_cluster_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary 更新项目
        
        @param tmp_req: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary 更新项目
        
        @param tmp_req: UpdateProjectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not UtilClient.is_unset(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not UtilClient.is_unset(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not UtilClient.is_unset(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not UtilClient.is_unset(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary 更新项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
    ) -> imm_20200930_models.UpdateProjectResponse:
        """
        @summary 更新项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_story_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param tmp_req: UpdateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_story_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param tmp_req: UpdateStoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStoryResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not UtilClient.is_unset(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not UtilClient.is_unset(request.custom_id):
            body['CustomId'] = request.custom_id
        if not UtilClient.is_unset(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not UtilClient.is_unset(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.object_id):
            body['ObjectId'] = request.object_id
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStory',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_story(
        self,
        request: imm_20200930_models.UpdateStoryRequest,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_story_with_options(request, runtime)

    async def update_story_async(
        self,
        request: imm_20200930_models.UpdateStoryRequest,
    ) -> imm_20200930_models.UpdateStoryResponse:
        """
        @summary 更新故事
        
        @param request: UpdateStoryRequest
        @return: UpdateStoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_story_with_options_async(request, runtime)

    def update_trigger_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary 更新数据接入实例
        
        @param tmp_req: UpdateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateTriggerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary 更新数据接入实例
        
        @param tmp_req: UpdateTriggerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTriggerResponse
        """
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateTriggerShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.actions):
            request.actions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not UtilClient.is_unset(tmp_req.input):
            request.input_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not UtilClient.is_unset(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.input_shrink):
            body['Input'] = request.input_shrink
        if not UtilClient.is_unset(request.project_name):
            body['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrigger',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        request: imm_20200930_models.UpdateTriggerRequest,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary 更新数据接入实例
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)

    async def update_trigger_async(
        self,
        request: imm_20200930_models.UpdateTriggerRequest,
    ) -> imm_20200930_models.UpdateTriggerResponse:
        """
        @summary 更新数据接入实例
        
        @param request: UpdateTriggerRequest
        @return: UpdateTriggerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_trigger_with_options_async(request, runtime)
