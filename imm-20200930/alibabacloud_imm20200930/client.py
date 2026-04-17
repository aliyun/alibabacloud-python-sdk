# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_imm20200930 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_image_mosaic_with_options(
        self,
        tmp_req: main_models.AddImageMosaicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageMosaicResponse:
        tmp_req.validate()
        request = main_models.AddImageMosaicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.image_format):
            query['ImageFormat'] = request.image_format
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddImageMosaic',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageMosaicResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_mosaic_with_options_async(
        self,
        tmp_req: main_models.AddImageMosaicRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageMosaicResponse:
        tmp_req.validate()
        request = main_models.AddImageMosaicShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.image_format):
            query['ImageFormat'] = request.image_format
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddImageMosaic',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageMosaicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_mosaic(
        self,
        request: main_models.AddImageMosaicRequest,
    ) -> main_models.AddImageMosaicResponse:
        runtime = RuntimeOptions()
        return self.add_image_mosaic_with_options(request, runtime)

    async def add_image_mosaic_async(
        self,
        request: main_models.AddImageMosaicRequest,
    ) -> main_models.AddImageMosaicResponse:
        runtime = RuntimeOptions()
        return await self.add_image_mosaic_with_options_async(request, runtime)

    def add_story_files_with_options(
        self,
        tmp_req: main_models.AddStoryFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddStoryFilesResponse:
        tmp_req.validate()
        request = main_models.AddStoryFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddStoryFiles',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_story_files_with_options_async(
        self,
        tmp_req: main_models.AddStoryFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddStoryFilesResponse:
        tmp_req.validate()
        request = main_models.AddStoryFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddStoryFiles',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_story_files(
        self,
        request: main_models.AddStoryFilesRequest,
    ) -> main_models.AddStoryFilesResponse:
        runtime = RuntimeOptions()
        return self.add_story_files_with_options(request, runtime)

    async def add_story_files_async(
        self,
        request: main_models.AddStoryFilesRequest,
    ) -> main_models.AddStoryFilesResponse:
        runtime = RuntimeOptions()
        return await self.add_story_files_with_options_async(request, runtime)

    def attach_ossbucket_with_options(
        self,
        request: main_models.AttachOSSBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachOSSBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachOSSBucket',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_ossbucket_with_options_async(
        self,
        request: main_models.AttachOSSBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachOSSBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachOSSBucket',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_ossbucket(
        self,
        request: main_models.AttachOSSBucketRequest,
    ) -> main_models.AttachOSSBucketResponse:
        runtime = RuntimeOptions()
        return self.attach_ossbucket_with_options(request, runtime)

    async def attach_ossbucket_async(
        self,
        request: main_models.AttachOSSBucketRequest,
    ) -> main_models.AttachOSSBucketResponse:
        runtime = RuntimeOptions()
        return await self.attach_ossbucket_with_options_async(request, runtime)

    def batch_delete_file_meta_with_options(
        self,
        tmp_req: main_models.BatchDeleteFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uris):
            request.uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_delete_file_meta_with_options_async(
        self,
        tmp_req: main_models.BatchDeleteFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchDeleteFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchDeleteFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uris):
            request.uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchDeleteFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchDeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_delete_file_meta(
        self,
        request: main_models.BatchDeleteFileMetaRequest,
    ) -> main_models.BatchDeleteFileMetaResponse:
        runtime = RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    async def batch_delete_file_meta_async(
        self,
        request: main_models.BatchDeleteFileMetaRequest,
    ) -> main_models.BatchDeleteFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.batch_delete_file_meta_with_options_async(request, runtime)

    def batch_get_figure_cluster_with_options(
        self,
        tmp_req: main_models.BatchGetFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetFigureClusterResponse:
        tmp_req.validate()
        request = main_models.BatchGetFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_figure_cluster_with_options_async(
        self,
        tmp_req: main_models.BatchGetFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetFigureClusterResponse:
        tmp_req.validate()
        request = main_models.BatchGetFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.object_ids):
            request.object_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.object_ids, 'ObjectIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_ids_shrink):
            query['ObjectIds'] = request.object_ids_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_figure_cluster(
        self,
        request: main_models.BatchGetFigureClusterRequest,
    ) -> main_models.BatchGetFigureClusterResponse:
        runtime = RuntimeOptions()
        return self.batch_get_figure_cluster_with_options(request, runtime)

    async def batch_get_figure_cluster_async(
        self,
        request: main_models.BatchGetFigureClusterRequest,
    ) -> main_models.BatchGetFigureClusterResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_figure_cluster_with_options_async(request, runtime)

    def batch_get_file_meta_with_options(
        self,
        tmp_req: main_models.BatchGetFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchGetFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uris):
            request.uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_file_meta_with_options_async(
        self,
        tmp_req: main_models.BatchGetFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchGetFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.uris):
            request.uris_shrink = Utils.array_to_string_with_specified_style(tmp_req.uris, 'URIs', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uris_shrink):
            query['URIs'] = request.uris_shrink
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_file_meta(
        self,
        request: main_models.BatchGetFileMetaRequest,
    ) -> main_models.BatchGetFileMetaResponse:
        runtime = RuntimeOptions()
        return self.batch_get_file_meta_with_options(request, runtime)

    async def batch_get_file_meta_async(
        self,
        request: main_models.BatchGetFileMetaRequest,
    ) -> main_models.BatchGetFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_file_meta_with_options_async(request, runtime)

    def batch_index_file_meta_with_options(
        self,
        tmp_req: main_models.BatchIndexFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchIndexFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchIndexFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            query['Files'] = request.files_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchIndexFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchIndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_index_file_meta_with_options_async(
        self,
        tmp_req: main_models.BatchIndexFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchIndexFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchIndexFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            query['Files'] = request.files_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchIndexFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchIndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_index_file_meta(
        self,
        request: main_models.BatchIndexFileMetaRequest,
    ) -> main_models.BatchIndexFileMetaResponse:
        runtime = RuntimeOptions()
        return self.batch_index_file_meta_with_options(request, runtime)

    async def batch_index_file_meta_async(
        self,
        request: main_models.BatchIndexFileMetaRequest,
    ) -> main_models.BatchIndexFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.batch_index_file_meta_with_options_async(request, runtime)

    def batch_update_file_meta_with_options(
        self,
        tmp_req: main_models.BatchUpdateFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            query['Files'] = request.files_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_update_file_meta_with_options_async(
        self,
        tmp_req: main_models.BatchUpdateFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchUpdateFileMetaResponse:
        tmp_req.validate()
        request = main_models.BatchUpdateFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            query['Files'] = request.files_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchUpdateFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchUpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_update_file_meta(
        self,
        request: main_models.BatchUpdateFileMetaRequest,
    ) -> main_models.BatchUpdateFileMetaResponse:
        runtime = RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    async def batch_update_file_meta_async(
        self,
        request: main_models.BatchUpdateFileMetaRequest,
    ) -> main_models.BatchUpdateFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.batch_update_file_meta_with_options_async(request, runtime)

    def compare_image_faces_with_options(
        self,
        tmp_req: main_models.CompareImageFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareImageFacesResponse:
        tmp_req.validate()
        request = main_models.CompareImageFacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareImageFaces',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def compare_image_faces_with_options_async(
        self,
        tmp_req: main_models.CompareImageFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CompareImageFacesResponse:
        tmp_req.validate()
        request = main_models.CompareImageFacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.source):
            request.source_shrink = Utils.array_to_string_with_specified_style(tmp_req.source, 'Source', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_shrink):
            query['Source'] = request.source_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CompareImageFaces',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompareImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def compare_image_faces(
        self,
        request: main_models.CompareImageFacesRequest,
    ) -> main_models.CompareImageFacesResponse:
        runtime = RuntimeOptions()
        return self.compare_image_faces_with_options(request, runtime)

    async def compare_image_faces_async(
        self,
        request: main_models.CompareImageFacesRequest,
    ) -> main_models.CompareImageFacesResponse:
        runtime = RuntimeOptions()
        return await self.compare_image_faces_with_options_async(request, runtime)

    def contextual_answer_with_sse(
        self,
        tmp_req: main_models.ContextualAnswerRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ContextualAnswerResponse, None, None]:
        tmp_req.validate()
        request = main_models.ContextualAnswerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualAnswer',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ContextualAnswerResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    async def contextual_answer_with_sse_async(
        self,
        tmp_req: main_models.ContextualAnswerRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ContextualAnswerResponse, None, None]:
        tmp_req.validate()
        request = main_models.ContextualAnswerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualAnswer',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            if not DaraCore.is_null(resp.event) and not DaraCore.is_null(resp.event.data):
                data = json.loads(resp.event.data)
                yield  DaraCore.from_map(
                    main_models.ContextualAnswerResponse(),
                    {
                    'statusCode': resp.status_code,
                    'headers': resp.headers,
                    'id': resp.event.id,
                    'event': resp.event.event,
                    'body': data
                })

    def contextual_answer_with_options(
        self,
        tmp_req: main_models.ContextualAnswerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContextualAnswerResponse:
        tmp_req.validate()
        request = main_models.ContextualAnswerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualAnswer',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContextualAnswerResponse(),
            self.call_api(params, req, runtime)
        )

    async def contextual_answer_with_options_async(
        self,
        tmp_req: main_models.ContextualAnswerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContextualAnswerResponse:
        tmp_req.validate()
        request = main_models.ContextualAnswerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualAnswer',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContextualAnswerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contextual_answer(
        self,
        request: main_models.ContextualAnswerRequest,
    ) -> main_models.ContextualAnswerResponse:
        runtime = RuntimeOptions()
        return self.contextual_answer_with_options(request, runtime)

    async def contextual_answer_async(
        self,
        request: main_models.ContextualAnswerRequest,
    ) -> main_models.ContextualAnswerResponse:
        runtime = RuntimeOptions()
        return await self.contextual_answer_with_options_async(request, runtime)

    def contextual_retrieval_with_options(
        self,
        tmp_req: main_models.ContextualRetrievalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContextualRetrievalResponse:
        tmp_req.validate()
        request = main_models.ContextualRetrievalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        if not DaraCore.is_null(tmp_req.smart_cluster_ids):
            request.smart_cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.smart_cluster_ids, 'SmartClusterIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.recall_only):
            query['RecallOnly'] = request.recall_only
        body = {}
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        if not DaraCore.is_null(request.smart_cluster_ids_shrink):
            body['SmartClusterIds'] = request.smart_cluster_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualRetrieval',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContextualRetrievalResponse(),
            self.call_api(params, req, runtime)
        )

    async def contextual_retrieval_with_options_async(
        self,
        tmp_req: main_models.ContextualRetrievalRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContextualRetrievalResponse:
        tmp_req.validate()
        request = main_models.ContextualRetrievalShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.messages):
            request.messages_shrink = Utils.array_to_string_with_specified_style(tmp_req.messages, 'Messages', 'json')
        if not DaraCore.is_null(tmp_req.smart_cluster_ids):
            request.smart_cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.smart_cluster_ids, 'SmartClusterIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.recall_only):
            query['RecallOnly'] = request.recall_only
        body = {}
        if not DaraCore.is_null(request.messages_shrink):
            body['Messages'] = request.messages_shrink
        if not DaraCore.is_null(request.smart_cluster_ids_shrink):
            body['SmartClusterIds'] = request.smart_cluster_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ContextualRetrieval',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContextualRetrievalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def contextual_retrieval(
        self,
        request: main_models.ContextualRetrievalRequest,
    ) -> main_models.ContextualRetrievalResponse:
        runtime = RuntimeOptions()
        return self.contextual_retrieval_with_options(request, runtime)

    async def contextual_retrieval_async(
        self,
        request: main_models.ContextualRetrievalRequest,
    ) -> main_models.ContextualRetrievalResponse:
        runtime = RuntimeOptions()
        return await self.contextual_retrieval_with_options_async(request, runtime)

    def create_archive_file_inspection_task_with_options(
        self,
        tmp_req: main_models.CreateArchiveFileInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArchiveFileInspectionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateArchiveFileInspectionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArchiveFileInspectionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArchiveFileInspectionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_archive_file_inspection_task_with_options_async(
        self,
        tmp_req: main_models.CreateArchiveFileInspectionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArchiveFileInspectionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateArchiveFileInspectionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArchiveFileInspectionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArchiveFileInspectionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_archive_file_inspection_task(
        self,
        request: main_models.CreateArchiveFileInspectionTaskRequest,
    ) -> main_models.CreateArchiveFileInspectionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_archive_file_inspection_task_with_options(request, runtime)

    async def create_archive_file_inspection_task_async(
        self,
        request: main_models.CreateArchiveFileInspectionTaskRequest,
    ) -> main_models.CreateArchiveFileInspectionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_archive_file_inspection_task_with_options_async(request, runtime)

    def create_batch_with_options(
        self,
        tmp_req: main_models.CreateBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchResponse:
        tmp_req.validate()
        request = main_models.CreateBatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            body['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_batch_with_options_async(
        self,
        tmp_req: main_models.CreateBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBatchResponse:
        tmp_req.validate()
        request = main_models.CreateBatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            body['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_batch(
        self,
        request: main_models.CreateBatchRequest,
    ) -> main_models.CreateBatchResponse:
        runtime = RuntimeOptions()
        return self.create_batch_with_options(request, runtime)

    async def create_batch_async(
        self,
        request: main_models.CreateBatchRequest,
    ) -> main_models.CreateBatchResponse:
        runtime = RuntimeOptions()
        return await self.create_batch_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: main_models.CreateBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: main_models.CreateBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_binding(
        self,
        request: main_models.CreateBindingRequest,
    ) -> main_models.CreateBindingResponse:
        runtime = RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: main_models.CreateBindingRequest,
    ) -> main_models.CreateBindingResponse:
        runtime = RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_compress_point_cloud_task_with_options(
        self,
        tmp_req: main_models.CreateCompressPointCloudTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCompressPointCloudTaskResponse:
        tmp_req.validate()
        request = main_models.CreateCompressPointCloudTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.kdtree_option):
            request.kdtree_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.octree_option):
            request.octree_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not DaraCore.is_null(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not DaraCore.is_null(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not DaraCore.is_null(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCompressPointCloudTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCompressPointCloudTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_compress_point_cloud_task_with_options_async(
        self,
        tmp_req: main_models.CreateCompressPointCloudTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCompressPointCloudTaskResponse:
        tmp_req.validate()
        request = main_models.CreateCompressPointCloudTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.kdtree_option):
            request.kdtree_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.kdtree_option, 'KdtreeOption', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.octree_option):
            request.octree_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.octree_option, 'OctreeOption', 'json')
        if not DaraCore.is_null(tmp_req.point_cloud_fields):
            request.point_cloud_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.point_cloud_fields, 'PointCloudFields', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.compress_method):
            query['CompressMethod'] = request.compress_method
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.kdtree_option_shrink):
            query['KdtreeOption'] = request.kdtree_option_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.octree_option_shrink):
            query['OctreeOption'] = request.octree_option_shrink
        if not DaraCore.is_null(request.point_cloud_fields_shrink):
            query['PointCloudFields'] = request.point_cloud_fields_shrink
        if not DaraCore.is_null(request.point_cloud_file_format):
            query['PointCloudFileFormat'] = request.point_cloud_file_format
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCompressPointCloudTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCompressPointCloudTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_compress_point_cloud_task(
        self,
        request: main_models.CreateCompressPointCloudTaskRequest,
    ) -> main_models.CreateCompressPointCloudTaskResponse:
        runtime = RuntimeOptions()
        return self.create_compress_point_cloud_task_with_options(request, runtime)

    async def create_compress_point_cloud_task_async(
        self,
        request: main_models.CreateCompressPointCloudTaskRequest,
    ) -> main_models.CreateCompressPointCloudTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_compress_point_cloud_task_with_options_async(request, runtime)

    def create_customized_story_with_options(
        self,
        tmp_req: main_models.CreateCustomizedStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomizedStoryResponse:
        tmp_req.validate()
        request = main_models.CreateCustomizedStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cover):
            request.cover_shrink = Utils.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomizedStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomizedStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_customized_story_with_options_async(
        self,
        tmp_req: main_models.CreateCustomizedStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCustomizedStoryResponse:
        tmp_req.validate()
        request = main_models.CreateCustomizedStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cover):
            request.cover_shrink = Utils.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCustomizedStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCustomizedStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_customized_story(
        self,
        request: main_models.CreateCustomizedStoryRequest,
    ) -> main_models.CreateCustomizedStoryResponse:
        runtime = RuntimeOptions()
        return self.create_customized_story_with_options(request, runtime)

    async def create_customized_story_async(
        self,
        request: main_models.CreateCustomizedStoryRequest,
    ) -> main_models.CreateCustomizedStoryResponse:
        runtime = RuntimeOptions()
        return await self.create_customized_story_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            query['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        tmp_req: main_models.CreateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatasetResponse:
        tmp_req.validate()
        request = main_models.CreateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            query['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: main_models.CreateDatasetRequest,
    ) -> main_models.CreateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_decode_blind_watermark_task_with_options(
        self,
        tmp_req: main_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDecodeBlindWatermarkTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDecodeBlindWatermarkTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDecodeBlindWatermarkTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_decode_blind_watermark_task_with_options_async(
        self,
        tmp_req: main_models.CreateDecodeBlindWatermarkTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDecodeBlindWatermarkTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDecodeBlindWatermarkTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.original_image_uri):
            query['OriginalImageURI'] = request.original_image_uri
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.watermark_type):
            query['WatermarkType'] = request.watermark_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDecodeBlindWatermarkTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDecodeBlindWatermarkTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_decode_blind_watermark_task(
        self,
        request: main_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> main_models.CreateDecodeBlindWatermarkTaskResponse:
        runtime = RuntimeOptions()
        return self.create_decode_blind_watermark_task_with_options(request, runtime)

    async def create_decode_blind_watermark_task_async(
        self,
        request: main_models.CreateDecodeBlindWatermarkTaskRequest,
    ) -> main_models.CreateDecodeBlindWatermarkTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_decode_blind_watermark_task_with_options_async(request, runtime)

    def create_faces_searching_task_with_options(
        self,
        tmp_req: main_models.CreateFacesSearchingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFacesSearchingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFacesSearchingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFacesSearchingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFacesSearchingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_faces_searching_task_with_options_async(
        self,
        tmp_req: main_models.CreateFacesSearchingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFacesSearchingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFacesSearchingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_result):
            query['MaxResult'] = request.max_result
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFacesSearchingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFacesSearchingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_faces_searching_task(
        self,
        request: main_models.CreateFacesSearchingTaskRequest,
    ) -> main_models.CreateFacesSearchingTaskResponse:
        runtime = RuntimeOptions()
        return self.create_faces_searching_task_with_options(request, runtime)

    async def create_faces_searching_task_async(
        self,
        request: main_models.CreateFacesSearchingTaskRequest,
    ) -> main_models.CreateFacesSearchingTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_faces_searching_task_with_options_async(request, runtime)

    def create_figure_clustering_task_with_options(
        self,
        tmp_req: main_models.CreateFigureClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFigureClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFigureClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFigureClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFigureClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clustering_task_with_options_async(
        self,
        tmp_req: main_models.CreateFigureClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFigureClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFigureClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFigureClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFigureClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clustering_task(
        self,
        request: main_models.CreateFigureClusteringTaskRequest,
    ) -> main_models.CreateFigureClusteringTaskResponse:
        runtime = RuntimeOptions()
        return self.create_figure_clustering_task_with_options(request, runtime)

    async def create_figure_clustering_task_async(
        self,
        request: main_models.CreateFigureClusteringTaskRequest,
    ) -> main_models.CreateFigureClusteringTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_figure_clustering_task_with_options_async(request, runtime)

    def create_figure_clusters_merging_task_with_options(
        self,
        tmp_req: main_models.CreateFigureClustersMergingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFigureClustersMergingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFigureClustersMergingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.froms):
            request.froms_shrink = Utils.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFigureClustersMergingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFigureClustersMergingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_figure_clusters_merging_task_with_options_async(
        self,
        tmp_req: main_models.CreateFigureClustersMergingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFigureClustersMergingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFigureClustersMergingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.froms):
            request.froms_shrink = Utils.array_to_string_with_specified_style(tmp_req.froms, 'Froms', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.froms_shrink):
            query['Froms'] = request.froms_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFigureClustersMergingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFigureClustersMergingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_figure_clusters_merging_task(
        self,
        request: main_models.CreateFigureClustersMergingTaskRequest,
    ) -> main_models.CreateFigureClustersMergingTaskResponse:
        runtime = RuntimeOptions()
        return self.create_figure_clusters_merging_task_with_options(request, runtime)

    async def create_figure_clusters_merging_task_async(
        self,
        request: main_models.CreateFigureClustersMergingTaskRequest,
    ) -> main_models.CreateFigureClustersMergingTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_figure_clusters_merging_task_with_options_async(request, runtime)

    def create_file_compression_task_with_options(
        self,
        tmp_req: main_models.CreateFileCompressionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileCompressionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFileCompressionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not DaraCore.is_null(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileCompressionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileCompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_compression_task_with_options_async(
        self,
        tmp_req: main_models.CreateFileCompressionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileCompressionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFileCompressionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        query = {}
        if not DaraCore.is_null(request.compressed_format):
            query['CompressedFormat'] = request.compressed_format
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_manifest_uri):
            query['SourceManifestURI'] = request.source_manifest_uri
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileCompressionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileCompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_compression_task(
        self,
        request: main_models.CreateFileCompressionTaskRequest,
    ) -> main_models.CreateFileCompressionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_file_compression_task_with_options(request, runtime)

    async def create_file_compression_task_async(
        self,
        request: main_models.CreateFileCompressionTaskRequest,
    ) -> main_models.CreateFileCompressionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_file_compression_task_with_options_async(request, runtime)

    def create_file_uncompression_task_with_options(
        self,
        tmp_req: main_models.CreateFileUncompressionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileUncompressionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFileUncompressionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.selected_files):
            request.selected_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileUncompressionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileUncompressionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_file_uncompression_task_with_options_async(
        self,
        tmp_req: main_models.CreateFileUncompressionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFileUncompressionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateFileUncompressionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.selected_files):
            request.selected_files_shrink = Utils.array_to_string_with_specified_style(tmp_req.selected_files, 'SelectedFiles', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.selected_files_shrink):
            query['SelectedFiles'] = request.selected_files_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFileUncompressionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFileUncompressionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_file_uncompression_task(
        self,
        request: main_models.CreateFileUncompressionTaskRequest,
    ) -> main_models.CreateFileUncompressionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_file_uncompression_task_with_options(request, runtime)

    async def create_file_uncompression_task_async(
        self,
        request: main_models.CreateFileUncompressionTaskRequest,
    ) -> main_models.CreateFileUncompressionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_file_uncompression_task_with_options_async(request, runtime)

    def create_highlight_task_with_options(
        self,
        tmp_req: main_models.CreateHighlightTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHighlightTaskResponse:
        tmp_req.validate()
        request = main_models.CreateHighlightTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.edit):
            request.edit_shrink = Utils.array_to_string_with_specified_style(tmp_req.edit, 'Edit', 'json')
        if not DaraCore.is_null(tmp_req.highlight):
            request.highlight_shrink = Utils.array_to_string_with_specified_style(tmp_req.highlight, 'Highlight', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.output):
            request.output_shrink = Utils.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            body['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.edit_shrink):
            body['Edit'] = request.edit_shrink
        if not DaraCore.is_null(request.highlight_shrink):
            body['Highlight'] = request.highlight_shrink
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.output_shrink):
            body['Output'] = request.output_shrink
        if not DaraCore.is_null(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHighlightTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHighlightTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_highlight_task_with_options_async(
        self,
        tmp_req: main_models.CreateHighlightTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHighlightTaskResponse:
        tmp_req.validate()
        request = main_models.CreateHighlightTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.edit):
            request.edit_shrink = Utils.array_to_string_with_specified_style(tmp_req.edit, 'Edit', 'json')
        if not DaraCore.is_null(tmp_req.highlight):
            request.highlight_shrink = Utils.array_to_string_with_specified_style(tmp_req.highlight, 'Highlight', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.output):
            request.output_shrink = Utils.array_to_string_with_specified_style(tmp_req.output, 'Output', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            body['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.edit_shrink):
            body['Edit'] = request.edit_shrink
        if not DaraCore.is_null(request.highlight_shrink):
            body['Highlight'] = request.highlight_shrink
        if not DaraCore.is_null(request.mode):
            body['Mode'] = request.mode
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.output_shrink):
            body['Output'] = request.output_shrink
        if not DaraCore.is_null(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateHighlightTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHighlightTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_highlight_task(
        self,
        request: main_models.CreateHighlightTaskRequest,
    ) -> main_models.CreateHighlightTaskResponse:
        runtime = RuntimeOptions()
        return self.create_highlight_task_with_options(request, runtime)

    async def create_highlight_task_async(
        self,
        request: main_models.CreateHighlightTaskRequest,
    ) -> main_models.CreateHighlightTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_highlight_task_with_options_async(request, runtime)

    def create_image_moderation_task_with_options(
        self,
        tmp_req: main_models.CreateImageModerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageModerationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageModerationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.scenes):
            request.scenes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageModerationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_moderation_task_with_options_async(
        self,
        tmp_req: main_models.CreateImageModerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageModerationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageModerationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.scenes):
            request.scenes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageModerationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_moderation_task(
        self,
        request: main_models.CreateImageModerationTaskRequest,
    ) -> main_models.CreateImageModerationTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_moderation_task_with_options(request, runtime)

    async def create_image_moderation_task_async(
        self,
        request: main_models.CreateImageModerationTaskRequest,
    ) -> main_models.CreateImageModerationTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_moderation_task_with_options_async(request, runtime)

    def create_image_splicing_task_with_options(
        self,
        tmp_req: main_models.CreateImageSplicingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageSplicingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageSplicingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.align):
            query['Align'] = request.align
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.image_format):
            query['ImageFormat'] = request.image_format
        if not DaraCore.is_null(request.margin):
            query['Margin'] = request.margin
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.padding):
            query['Padding'] = request.padding
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageSplicingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageSplicingTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_splicing_task_with_options_async(
        self,
        tmp_req: main_models.CreateImageSplicingTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageSplicingTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageSplicingTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.align):
            query['Align'] = request.align
        if not DaraCore.is_null(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.image_format):
            query['ImageFormat'] = request.image_format
        if not DaraCore.is_null(request.margin):
            query['Margin'] = request.margin
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.padding):
            query['Padding'] = request.padding
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.scale_type):
            query['ScaleType'] = request.scale_type
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageSplicingTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageSplicingTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_splicing_task(
        self,
        request: main_models.CreateImageSplicingTaskRequest,
    ) -> main_models.CreateImageSplicingTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_splicing_task_with_options(request, runtime)

    async def create_image_splicing_task_async(
        self,
        request: main_models.CreateImageSplicingTaskRequest,
    ) -> main_models.CreateImageSplicingTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_splicing_task_with_options_async(request, runtime)

    def create_image_to_pdftask_with_options(
        self,
        tmp_req: main_models.CreateImageToPDFTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageToPDFTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageToPDFTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageToPDFTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageToPDFTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_to_pdftask_with_options_async(
        self,
        tmp_req: main_models.CreateImageToPDFTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateImageToPDFTaskResponse:
        tmp_req.validate()
        request = main_models.CreateImageToPDFTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateImageToPDFTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateImageToPDFTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_to_pdftask(
        self,
        request: main_models.CreateImageToPDFTaskRequest,
    ) -> main_models.CreateImageToPDFTaskResponse:
        runtime = RuntimeOptions()
        return self.create_image_to_pdftask_with_options(request, runtime)

    async def create_image_to_pdftask_async(
        self,
        request: main_models.CreateImageToPDFTaskRequest,
    ) -> main_models.CreateImageToPDFTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_image_to_pdftask_with_options_async(request, runtime)

    def create_location_date_clustering_task_with_options(
        self,
        tmp_req: main_models.CreateLocationDateClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocationDateClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateLocationDateClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.date_options):
            request.date_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not DaraCore.is_null(tmp_req.location_options):
            request.location_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not DaraCore.is_null(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocationDateClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocationDateClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_location_date_clustering_task_with_options_async(
        self,
        tmp_req: main_models.CreateLocationDateClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateLocationDateClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateLocationDateClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.date_options):
            request.date_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.date_options, 'DateOptions', 'json')
        if not DaraCore.is_null(tmp_req.location_options):
            request.location_options_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_options, 'LocationOptions', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.date_options_shrink):
            query['DateOptions'] = request.date_options_shrink
        if not DaraCore.is_null(request.location_options_shrink):
            query['LocationOptions'] = request.location_options_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateLocationDateClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLocationDateClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_location_date_clustering_task(
        self,
        request: main_models.CreateLocationDateClusteringTaskRequest,
    ) -> main_models.CreateLocationDateClusteringTaskResponse:
        runtime = RuntimeOptions()
        return self.create_location_date_clustering_task_with_options(request, runtime)

    async def create_location_date_clustering_task_async(
        self,
        request: main_models.CreateLocationDateClusteringTaskRequest,
    ) -> main_models.CreateLocationDateClusteringTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_location_date_clustering_task_with_options_async(request, runtime)

    def create_media_convert_task_with_options(
        self,
        tmp_req: main_models.CreateMediaConvertTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMediaConvertTaskResponse:
        tmp_req.validate()
        request = main_models.CreateMediaConvertTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.target_groups):
            request.target_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_groups, 'TargetGroups', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_groups_shrink):
            query['TargetGroups'] = request.target_groups_shrink
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMediaConvertTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMediaConvertTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_media_convert_task_with_options_async(
        self,
        tmp_req: main_models.CreateMediaConvertTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMediaConvertTaskResponse:
        tmp_req.validate()
        request = main_models.CreateMediaConvertTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.target_groups):
            request.target_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.target_groups, 'TargetGroups', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.alignment_index):
            query['AlignmentIndex'] = request.alignment_index
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_groups_shrink):
            query['TargetGroups'] = request.target_groups_shrink
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMediaConvertTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMediaConvertTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_media_convert_task(
        self,
        request: main_models.CreateMediaConvertTaskRequest,
    ) -> main_models.CreateMediaConvertTaskResponse:
        runtime = RuntimeOptions()
        return self.create_media_convert_task_with_options(request, runtime)

    async def create_media_convert_task_async(
        self,
        request: main_models.CreateMediaConvertTaskRequest,
    ) -> main_models.CreateMediaConvertTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_media_convert_task_with_options_async(request, runtime)

    def create_office_conversion_task_with_options(
        self,
        tmp_req: main_models.CreateOfficeConversionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOfficeConversionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateOfficeConversionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.trim_policy):
            request.trim_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.end_page):
            query['EndPage'] = request.end_page
        if not DaraCore.is_null(request.first_page):
            query['FirstPage'] = request.first_page
        if not DaraCore.is_null(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not DaraCore.is_null(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not DaraCore.is_null(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not DaraCore.is_null(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not DaraCore.is_null(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not DaraCore.is_null(request.long_text):
            query['LongText'] = request.long_text
        if not DaraCore.is_null(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not DaraCore.is_null(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.pages):
            query['Pages'] = request.pages
        if not DaraCore.is_null(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not DaraCore.is_null(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not DaraCore.is_null(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not DaraCore.is_null(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not DaraCore.is_null(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.start_page):
            query['StartPage'] = request.start_page
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not DaraCore.is_null(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not DaraCore.is_null(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOfficeConversionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        tmp_req: main_models.CreateOfficeConversionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOfficeConversionTaskResponse:
        tmp_req.validate()
        request = main_models.CreateOfficeConversionTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.trim_policy):
            request.trim_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.trim_policy, 'TrimPolicy', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.end_page):
            query['EndPage'] = request.end_page
        if not DaraCore.is_null(request.first_page):
            query['FirstPage'] = request.first_page
        if not DaraCore.is_null(request.fit_to_height):
            query['FitToHeight'] = request.fit_to_height
        if not DaraCore.is_null(request.fit_to_width):
            query['FitToWidth'] = request.fit_to_width
        if not DaraCore.is_null(request.hold_line_feed):
            query['HoldLineFeed'] = request.hold_line_feed
        if not DaraCore.is_null(request.image_dpi):
            query['ImageDPI'] = request.image_dpi
        if not DaraCore.is_null(request.long_picture):
            query['LongPicture'] = request.long_picture
        if not DaraCore.is_null(request.long_text):
            query['LongText'] = request.long_text
        if not DaraCore.is_null(request.max_sheet_column):
            query['MaxSheetColumn'] = request.max_sheet_column
        if not DaraCore.is_null(request.max_sheet_row):
            query['MaxSheetRow'] = request.max_sheet_row
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.pages):
            query['Pages'] = request.pages
        if not DaraCore.is_null(request.paper_horizontal):
            query['PaperHorizontal'] = request.paper_horizontal
        if not DaraCore.is_null(request.paper_size):
            query['PaperSize'] = request.paper_size
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.quality):
            query['Quality'] = request.quality
        if not DaraCore.is_null(request.scale_percentage):
            query['ScalePercentage'] = request.scale_percentage
        if not DaraCore.is_null(request.sheet_count):
            query['SheetCount'] = request.sheet_count
        if not DaraCore.is_null(request.sheet_index):
            query['SheetIndex'] = request.sheet_index
        if not DaraCore.is_null(request.show_comments):
            query['ShowComments'] = request.show_comments
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.start_page):
            query['StartPage'] = request.start_page
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.target_type):
            query['TargetType'] = request.target_type
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        if not DaraCore.is_null(request.target_uriprefix):
            query['TargetURIPrefix'] = request.target_uriprefix
        if not DaraCore.is_null(request.trim_policy_shrink):
            query['TrimPolicy'] = request.trim_policy_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not DaraCore.is_null(request.sources_shrink):
            body['Sources'] = request.sources_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOfficeConversionTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_office_conversion_task(
        self,
        request: main_models.CreateOfficeConversionTaskRequest,
    ) -> main_models.CreateOfficeConversionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    async def create_office_conversion_task_async(
        self,
        request: main_models.CreateOfficeConversionTaskRequest,
    ) -> main_models.CreateOfficeConversionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_office_conversion_task_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        tmp_req: main_models.CreateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        tmp_req.validate()
        request = main_models.CreateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            query['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        tmp_req: main_models.CreateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        tmp_req.validate()
        request = main_models.CreateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            query['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_similar_image_clustering_task_with_options(
        self,
        tmp_req: main_models.CreateSimilarImageClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarImageClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateSimilarImageClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarImageClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarImageClusteringTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_similar_image_clustering_task_with_options_async(
        self,
        tmp_req: main_models.CreateSimilarImageClusteringTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSimilarImageClusteringTaskResponse:
        tmp_req.validate()
        request = main_models.CreateSimilarImageClusteringTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSimilarImageClusteringTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSimilarImageClusteringTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_similar_image_clustering_task(
        self,
        request: main_models.CreateSimilarImageClusteringTaskRequest,
    ) -> main_models.CreateSimilarImageClusteringTaskResponse:
        runtime = RuntimeOptions()
        return self.create_similar_image_clustering_task_with_options(request, runtime)

    async def create_similar_image_clustering_task_async(
        self,
        request: main_models.CreateSimilarImageClusteringTaskRequest,
    ) -> main_models.CreateSimilarImageClusteringTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_similar_image_clustering_task_with_options_async(request, runtime)

    def create_story_with_options(
        self,
        tmp_req: main_models.CreateStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoryResponse:
        tmp_req.validate()
        request = main_models.CreateStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address):
            request.address_shrink = Utils.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not DaraCore.is_null(request.address_shrink):
            body['Address'] = request.address_shrink
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not DaraCore.is_null(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not DaraCore.is_null(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not DaraCore.is_null(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_story_with_options_async(
        self,
        tmp_req: main_models.CreateStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStoryResponse:
        tmp_req.validate()
        request = main_models.CreateStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address):
            request.address_shrink = Utils.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        body = {}
        if not DaraCore.is_null(request.address_shrink):
            body['Address'] = request.address_shrink
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_file_count):
            body['MaxFileCount'] = request.max_file_count
        if not DaraCore.is_null(request.min_file_count):
            body['MinFileCount'] = request.min_file_count
        if not DaraCore.is_null(request.notify_topic_name):
            body['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_end_time):
            body['StoryEndTime'] = request.story_end_time
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_start_time):
            body['StoryStartTime'] = request.story_start_time
        if not DaraCore.is_null(request.story_sub_type):
            body['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            body['StoryType'] = request.story_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_story(
        self,
        request: main_models.CreateStoryRequest,
    ) -> main_models.CreateStoryResponse:
        runtime = RuntimeOptions()
        return self.create_story_with_options(request, runtime)

    async def create_story_async(
        self,
        request: main_models.CreateStoryRequest,
    ) -> main_models.CreateStoryResponse:
        runtime = RuntimeOptions()
        return await self.create_story_with_options_async(request, runtime)

    def create_trigger_with_options(
        self,
        tmp_req: main_models.CreateTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        tmp_req.validate()
        request = main_models.CreateTriggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            body['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_trigger_with_options_async(
        self,
        tmp_req: main_models.CreateTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTriggerResponse:
        tmp_req.validate()
        request = main_models.CreateTriggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.notification_shrink):
            body['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            body['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_trigger(
        self,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    async def create_trigger_async(
        self,
        request: main_models.CreateTriggerRequest,
    ) -> main_models.CreateTriggerResponse:
        runtime = RuntimeOptions()
        return await self.create_trigger_with_options_async(request, runtime)

    def create_video_label_classification_task_with_options(
        self,
        tmp_req: main_models.CreateVideoLabelClassificationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoLabelClassificationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateVideoLabelClassificationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoLabelClassificationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoLabelClassificationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_label_classification_task_with_options_async(
        self,
        tmp_req: main_models.CreateVideoLabelClassificationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoLabelClassificationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateVideoLabelClassificationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoLabelClassificationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoLabelClassificationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_label_classification_task(
        self,
        request: main_models.CreateVideoLabelClassificationTaskRequest,
    ) -> main_models.CreateVideoLabelClassificationTaskResponse:
        runtime = RuntimeOptions()
        return self.create_video_label_classification_task_with_options(request, runtime)

    async def create_video_label_classification_task_async(
        self,
        request: main_models.CreateVideoLabelClassificationTaskRequest,
    ) -> main_models.CreateVideoLabelClassificationTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_video_label_classification_task_with_options_async(request, runtime)

    def create_video_moderation_task_with_options(
        self,
        tmp_req: main_models.CreateVideoModerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoModerationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateVideoModerationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.scenes):
            request.scenes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoModerationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoModerationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_moderation_task_with_options_async(
        self,
        tmp_req: main_models.CreateVideoModerationTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVideoModerationTaskResponse:
        tmp_req.validate()
        request = main_models.CreateVideoModerationTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.scenes):
            request.scenes_shrink = Utils.array_to_string_with_specified_style(tmp_req.scenes, 'Scenes', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.max_frames):
            query['MaxFrames'] = request.max_frames
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.scenes_shrink):
            query['Scenes'] = request.scenes_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateVideoModerationTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVideoModerationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_moderation_task(
        self,
        request: main_models.CreateVideoModerationTaskRequest,
    ) -> main_models.CreateVideoModerationTaskResponse:
        runtime = RuntimeOptions()
        return self.create_video_moderation_task_with_options(request, runtime)

    async def create_video_moderation_task_async(
        self,
        request: main_models.CreateVideoModerationTaskRequest,
    ) -> main_models.CreateVideoModerationTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_video_moderation_task_with_options_async(request, runtime)

    def delete_batch_with_options(
        self,
        request: main_models.DeleteBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_batch_with_options_async(
        self,
        request: main_models.DeleteBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_batch(
        self,
        request: main_models.DeleteBatchRequest,
    ) -> main_models.DeleteBatchResponse:
        runtime = RuntimeOptions()
        return self.delete_batch_with_options(request, runtime)

    async def delete_batch_async(
        self,
        request: main_models.DeleteBatchRequest,
    ) -> main_models.DeleteBatchResponse:
        runtime = RuntimeOptions()
        return await self.delete_batch_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: main_models.DeleteBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: main_models.DeleteBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_binding(
        self,
        request: main_models.DeleteBindingRequest,
    ) -> main_models.DeleteBindingResponse:
        runtime = RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: main_models.DeleteBindingRequest,
    ) -> main_models.DeleteBindingResponse:
        runtime = RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: main_models.DeleteDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: main_models.DeleteDatasetRequest,
    ) -> main_models.DeleteDatasetResponse:
        runtime = RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_file_meta_with_options(
        self,
        request: main_models.DeleteFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_file_meta_with_options_async(
        self,
        request: main_models.DeleteFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFileMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_file_meta(
        self,
        request: main_models.DeleteFileMetaRequest,
    ) -> main_models.DeleteFileMetaResponse:
        runtime = RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    async def delete_file_meta_async(
        self,
        request: main_models.DeleteFileMetaRequest,
    ) -> main_models.DeleteFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.delete_file_meta_with_options_async(request, runtime)

    def delete_location_date_cluster_with_options(
        self,
        request: main_models.DeleteLocationDateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLocationDateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLocationDateCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_location_date_cluster_with_options_async(
        self,
        request: main_models.DeleteLocationDateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLocationDateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        body = {}
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLocationDateCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_location_date_cluster(
        self,
        request: main_models.DeleteLocationDateClusterRequest,
    ) -> main_models.DeleteLocationDateClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_location_date_cluster_with_options(request, runtime)

    async def delete_location_date_cluster_async(
        self,
        request: main_models.DeleteLocationDateClusterRequest,
    ) -> main_models.DeleteLocationDateClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_location_date_cluster_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: main_models.DeleteProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: main_models.DeleteProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: main_models.DeleteProjectRequest,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_story_with_options(
        self,
        request: main_models.DeleteStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_story_with_options_async(
        self,
        request: main_models.DeleteStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_story(
        self,
        request: main_models.DeleteStoryRequest,
    ) -> main_models.DeleteStoryResponse:
        runtime = RuntimeOptions()
        return self.delete_story_with_options(request, runtime)

    async def delete_story_async(
        self,
        request: main_models.DeleteStoryRequest,
    ) -> main_models.DeleteStoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_story_with_options_async(request, runtime)

    def delete_trigger_with_options(
        self,
        request: main_models.DeleteTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trigger_with_options_async(
        self,
        request: main_models.DeleteTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trigger(
        self,
        request: main_models.DeleteTriggerRequest,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    async def delete_trigger_async(
        self,
        request: main_models.DeleteTriggerRequest,
    ) -> main_models.DeleteTriggerResponse:
        runtime = RuntimeOptions()
        return await self.delete_trigger_with_options_async(request, runtime)

    def detach_ossbucket_with_options(
        self,
        request: main_models.DetachOSSBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachOSSBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachOSSBucket',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachOSSBucketResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_ossbucket_with_options_async(
        self,
        request: main_models.DetachOSSBucketRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachOSSBucketResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachOSSBucket',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachOSSBucketResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_ossbucket(
        self,
        request: main_models.DetachOSSBucketRequest,
    ) -> main_models.DetachOSSBucketResponse:
        runtime = RuntimeOptions()
        return self.detach_ossbucket_with_options(request, runtime)

    async def detach_ossbucket_async(
        self,
        request: main_models.DetachOSSBucketRequest,
    ) -> main_models.DetachOSSBucketResponse:
        runtime = RuntimeOptions()
        return await self.detach_ossbucket_with_options_async(request, runtime)

    def detect_image_bodies_with_options(
        self,
        tmp_req: main_models.DetectImageBodiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageBodiesResponse:
        tmp_req.validate()
        request = main_models.DetectImageBodiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageBodies',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageBodiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_bodies_with_options_async(
        self,
        tmp_req: main_models.DetectImageBodiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageBodiesResponse:
        tmp_req.validate()
        request = main_models.DetectImageBodiesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sensitivity):
            query['Sensitivity'] = request.sensitivity
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageBodies',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageBodiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_bodies(
        self,
        request: main_models.DetectImageBodiesRequest,
    ) -> main_models.DetectImageBodiesResponse:
        runtime = RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    async def detect_image_bodies_async(
        self,
        request: main_models.DetectImageBodiesRequest,
    ) -> main_models.DetectImageBodiesResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_bodies_with_options_async(request, runtime)

    def detect_image_cars_with_options(
        self,
        tmp_req: main_models.DetectImageCarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCarsResponse:
        tmp_req.validate()
        request = main_models.DetectImageCarsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCars',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cars_with_options_async(
        self,
        tmp_req: main_models.DetectImageCarsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCarsResponse:
        tmp_req.validate()
        request = main_models.DetectImageCarsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCars',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cars(
        self,
        request: main_models.DetectImageCarsRequest,
    ) -> main_models.DetectImageCarsResponse:
        runtime = RuntimeOptions()
        return self.detect_image_cars_with_options(request, runtime)

    async def detect_image_cars_async(
        self,
        request: main_models.DetectImageCarsRequest,
    ) -> main_models.DetectImageCarsResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_cars_with_options_async(request, runtime)

    def detect_image_codes_with_options(
        self,
        tmp_req: main_models.DetectImageCodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCodesResponse:
        tmp_req.validate()
        request = main_models.DetectImageCodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCodes',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_codes_with_options_async(
        self,
        tmp_req: main_models.DetectImageCodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCodesResponse:
        tmp_req.validate()
        request = main_models.DetectImageCodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCodes',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_codes(
        self,
        request: main_models.DetectImageCodesRequest,
    ) -> main_models.DetectImageCodesResponse:
        runtime = RuntimeOptions()
        return self.detect_image_codes_with_options(request, runtime)

    async def detect_image_codes_async(
        self,
        request: main_models.DetectImageCodesRequest,
    ) -> main_models.DetectImageCodesResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_codes_with_options_async(request, runtime)

    def detect_image_cropping_with_options(
        self,
        tmp_req: main_models.DetectImageCroppingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCroppingResponse:
        tmp_req.validate()
        request = main_models.DetectImageCroppingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCropping',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCroppingResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_cropping_with_options_async(
        self,
        tmp_req: main_models.DetectImageCroppingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageCroppingResponse:
        tmp_req.validate()
        request = main_models.DetectImageCroppingShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.aspect_ratios):
            query['AspectRatios'] = request.aspect_ratios
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageCropping',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageCroppingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_cropping(
        self,
        request: main_models.DetectImageCroppingRequest,
    ) -> main_models.DetectImageCroppingResponse:
        runtime = RuntimeOptions()
        return self.detect_image_cropping_with_options(request, runtime)

    async def detect_image_cropping_async(
        self,
        request: main_models.DetectImageCroppingRequest,
    ) -> main_models.DetectImageCroppingResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_cropping_with_options_async(request, runtime)

    def detect_image_faces_with_options(
        self,
        tmp_req: main_models.DetectImageFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageFacesResponse:
        tmp_req.validate()
        request = main_models.DetectImageFacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageFaces',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageFacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_faces_with_options_async(
        self,
        tmp_req: main_models.DetectImageFacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageFacesResponse:
        tmp_req.validate()
        request = main_models.DetectImageFacesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageFaces',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageFacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_faces(
        self,
        request: main_models.DetectImageFacesRequest,
    ) -> main_models.DetectImageFacesResponse:
        runtime = RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    async def detect_image_faces_async(
        self,
        request: main_models.DetectImageFacesRequest,
    ) -> main_models.DetectImageFacesResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_faces_with_options_async(request, runtime)

    def detect_image_labels_with_options(
        self,
        tmp_req: main_models.DetectImageLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageLabelsResponse:
        tmp_req.validate()
        request = main_models.DetectImageLabelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageLabels',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_labels_with_options_async(
        self,
        tmp_req: main_models.DetectImageLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageLabelsResponse:
        tmp_req.validate()
        request = main_models.DetectImageLabelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageLabels',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_labels(
        self,
        request: main_models.DetectImageLabelsRequest,
    ) -> main_models.DetectImageLabelsResponse:
        runtime = RuntimeOptions()
        return self.detect_image_labels_with_options(request, runtime)

    async def detect_image_labels_async(
        self,
        request: main_models.DetectImageLabelsRequest,
    ) -> main_models.DetectImageLabelsResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_labels_with_options_async(request, runtime)

    def detect_image_score_with_options(
        self,
        tmp_req: main_models.DetectImageScoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageScoreResponse:
        tmp_req.validate()
        request = main_models.DetectImageScoreShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageScore',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageScoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_score_with_options_async(
        self,
        tmp_req: main_models.DetectImageScoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageScoreResponse:
        tmp_req.validate()
        request = main_models.DetectImageScoreShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageScore',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageScoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_score(
        self,
        request: main_models.DetectImageScoreRequest,
    ) -> main_models.DetectImageScoreResponse:
        runtime = RuntimeOptions()
        return self.detect_image_score_with_options(request, runtime)

    async def detect_image_score_async(
        self,
        request: main_models.DetectImageScoreRequest,
    ) -> main_models.DetectImageScoreResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_score_with_options_async(request, runtime)

    def detect_image_texts_with_options(
        self,
        tmp_req: main_models.DetectImageTextsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageTextsResponse:
        tmp_req.validate()
        request = main_models.DetectImageTextsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageTexts',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageTextsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_texts_with_options_async(
        self,
        tmp_req: main_models.DetectImageTextsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectImageTextsResponse:
        tmp_req.validate()
        request = main_models.DetectImageTextsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectImageTexts',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectImageTextsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_image_texts(
        self,
        request: main_models.DetectImageTextsRequest,
    ) -> main_models.DetectImageTextsResponse:
        runtime = RuntimeOptions()
        return self.detect_image_texts_with_options(request, runtime)

    async def detect_image_texts_async(
        self,
        request: main_models.DetectImageTextsRequest,
    ) -> main_models.DetectImageTextsResponse:
        runtime = RuntimeOptions()
        return await self.detect_image_texts_with_options_async(request, runtime)

    def detect_media_meta_with_options(
        self,
        tmp_req: main_models.DetectMediaMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectMediaMetaResponse:
        tmp_req.validate()
        request = main_models.DetectMediaMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectMediaMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_media_meta_with_options_async(
        self,
        tmp_req: main_models.DetectMediaMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectMediaMetaResponse:
        tmp_req.validate()
        request = main_models.DetectMediaMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectMediaMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectMediaMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_media_meta(
        self,
        request: main_models.DetectMediaMetaRequest,
    ) -> main_models.DetectMediaMetaResponse:
        runtime = RuntimeOptions()
        return self.detect_media_meta_with_options(request, runtime)

    async def detect_media_meta_async(
        self,
        request: main_models.DetectMediaMetaRequest,
    ) -> main_models.DetectMediaMetaResponse:
        runtime = RuntimeOptions()
        return await self.detect_media_meta_with_options_async(request, runtime)

    def detect_text_anomaly_with_options(
        self,
        request: main_models.DetectTextAnomalyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectTextAnomalyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectTextAnomaly',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectTextAnomalyResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_text_anomaly_with_options_async(
        self,
        request: main_models.DetectTextAnomalyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectTextAnomalyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectTextAnomaly',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectTextAnomalyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_text_anomaly(
        self,
        request: main_models.DetectTextAnomalyRequest,
    ) -> main_models.DetectTextAnomalyResponse:
        runtime = RuntimeOptions()
        return self.detect_text_anomaly_with_options(request, runtime)

    async def detect_text_anomaly_async(
        self,
        request: main_models.DetectTextAnomalyRequest,
    ) -> main_models.DetectTextAnomalyResponse:
        runtime = RuntimeOptions()
        return await self.detect_text_anomaly_with_options_async(request, runtime)

    def encode_blind_watermark_with_options(
        self,
        request: main_models.EncodeBlindWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncodeBlindWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncodeBlindWatermark',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncodeBlindWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    async def encode_blind_watermark_with_options_async(
        self,
        request: main_models.EncodeBlindWatermarkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EncodeBlindWatermarkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.image_quality):
            query['ImageQuality'] = request.image_quality
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.strength_level):
            query['StrengthLevel'] = request.strength_level
        if not DaraCore.is_null(request.target_uri):
            query['TargetURI'] = request.target_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EncodeBlindWatermark',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EncodeBlindWatermarkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def encode_blind_watermark(
        self,
        request: main_models.EncodeBlindWatermarkRequest,
    ) -> main_models.EncodeBlindWatermarkResponse:
        runtime = RuntimeOptions()
        return self.encode_blind_watermark_with_options(request, runtime)

    async def encode_blind_watermark_async(
        self,
        request: main_models.EncodeBlindWatermarkRequest,
    ) -> main_models.EncodeBlindWatermarkResponse:
        runtime = RuntimeOptions()
        return await self.encode_blind_watermark_with_options_async(request, runtime)

    def extract_document_text_with_options(
        self,
        tmp_req: main_models.ExtractDocumentTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExtractDocumentTextResponse:
        tmp_req.validate()
        request = main_models.ExtractDocumentTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExtractDocumentText',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExtractDocumentTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def extract_document_text_with_options_async(
        self,
        tmp_req: main_models.ExtractDocumentTextRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExtractDocumentTextResponse:
        tmp_req.validate()
        request = main_models.ExtractDocumentTextShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExtractDocumentText',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExtractDocumentTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extract_document_text(
        self,
        request: main_models.ExtractDocumentTextRequest,
    ) -> main_models.ExtractDocumentTextResponse:
        runtime = RuntimeOptions()
        return self.extract_document_text_with_options(request, runtime)

    async def extract_document_text_async(
        self,
        request: main_models.ExtractDocumentTextRequest,
    ) -> main_models.ExtractDocumentTextResponse:
        runtime = RuntimeOptions()
        return await self.extract_document_text_with_options_async(request, runtime)

    def fuzzy_query_with_options(
        self,
        tmp_req: main_models.FuzzyQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FuzzyQueryResponse:
        tmp_req.validate()
        request = main_models.FuzzyQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FuzzyQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FuzzyQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def fuzzy_query_with_options_async(
        self,
        tmp_req: main_models.FuzzyQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.FuzzyQueryResponse:
        tmp_req.validate()
        request = main_models.FuzzyQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'FuzzyQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FuzzyQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def fuzzy_query(
        self,
        request: main_models.FuzzyQueryRequest,
    ) -> main_models.FuzzyQueryResponse:
        runtime = RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    async def fuzzy_query_async(
        self,
        request: main_models.FuzzyQueryRequest,
    ) -> main_models.FuzzyQueryResponse:
        runtime = RuntimeOptions()
        return await self.fuzzy_query_with_options_async(request, runtime)

    def generate_video_playlist_with_options(
        self,
        tmp_req: main_models.GenerateVideoPlaylistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateVideoPlaylistResponse:
        tmp_req.validate()
        request = main_models.GenerateVideoPlaylistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.source_subtitles):
            request.source_subtitles_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not DaraCore.is_null(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not DaraCore.is_null(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateVideoPlaylist',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateVideoPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_video_playlist_with_options_async(
        self,
        tmp_req: main_models.GenerateVideoPlaylistRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateVideoPlaylistResponse:
        tmp_req.validate()
        request = main_models.GenerateVideoPlaylistShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.source_subtitles):
            request.source_subtitles_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_subtitles, 'SourceSubtitles', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not DaraCore.is_null(tmp_req.targets):
            request.targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.master_uri):
            query['MasterURI'] = request.master_uri
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.overwrite_policy):
            query['OverwritePolicy'] = request.overwrite_policy
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_duration):
            query['SourceDuration'] = request.source_duration
        if not DaraCore.is_null(request.source_start_time):
            query['SourceStartTime'] = request.source_start_time
        if not DaraCore.is_null(request.source_subtitles_shrink):
            query['SourceSubtitles'] = request.source_subtitles_shrink
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets_shrink):
            query['Targets'] = request.targets_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateVideoPlaylist',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateVideoPlaylistResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_video_playlist(
        self,
        request: main_models.GenerateVideoPlaylistRequest,
    ) -> main_models.GenerateVideoPlaylistResponse:
        runtime = RuntimeOptions()
        return self.generate_video_playlist_with_options(request, runtime)

    async def generate_video_playlist_async(
        self,
        request: main_models.GenerateVideoPlaylistRequest,
    ) -> main_models.GenerateVideoPlaylistResponse:
        runtime = RuntimeOptions()
        return await self.generate_video_playlist_with_options_async(request, runtime)

    def generate_weboffice_token_with_options(
        self,
        tmp_req: main_models.GenerateWebofficeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateWebofficeTokenResponse:
        tmp_req.validate()
        request = main_models.GenerateWebofficeTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.permission):
            request.permission_shrink = Utils.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not DaraCore.is_null(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not DaraCore.is_null(request.filename):
            query['Filename'] = request.filename
        if not DaraCore.is_null(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not DaraCore.is_null(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.user_shrink):
            query['User'] = request.user_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateWebofficeToken',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_weboffice_token_with_options_async(
        self,
        tmp_req: main_models.GenerateWebofficeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateWebofficeTokenResponse:
        tmp_req.validate()
        request = main_models.GenerateWebofficeTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        if not DaraCore.is_null(tmp_req.permission):
            request.permission_shrink = Utils.array_to_string_with_specified_style(tmp_req.permission, 'Permission', 'json')
        if not DaraCore.is_null(tmp_req.user):
            request.user_shrink = Utils.array_to_string_with_specified_style(tmp_req.user, 'User', 'json')
        if not DaraCore.is_null(tmp_req.watermark):
            request.watermark_shrink = Utils.array_to_string_with_specified_style(tmp_req.watermark, 'Watermark', 'json')
        query = {}
        if not DaraCore.is_null(request.cache_preview):
            query['CachePreview'] = request.cache_preview
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.external_uploaded):
            query['ExternalUploaded'] = request.external_uploaded
        if not DaraCore.is_null(request.filename):
            query['Filename'] = request.filename
        if not DaraCore.is_null(request.hidecmb):
            query['Hidecmb'] = request.hidecmb
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.permission_shrink):
            query['Permission'] = request.permission_shrink
        if not DaraCore.is_null(request.preview_pages):
            query['PreviewPages'] = request.preview_pages
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.user_shrink):
            query['User'] = request.user_shrink
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        if not DaraCore.is_null(request.watermark_shrink):
            query['Watermark'] = request.watermark_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateWebofficeToken',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_weboffice_token(
        self,
        request: main_models.GenerateWebofficeTokenRequest,
    ) -> main_models.GenerateWebofficeTokenResponse:
        runtime = RuntimeOptions()
        return self.generate_weboffice_token_with_options(request, runtime)

    async def generate_weboffice_token_async(
        self,
        request: main_models.GenerateWebofficeTokenRequest,
    ) -> main_models.GenerateWebofficeTokenResponse:
        runtime = RuntimeOptions()
        return await self.generate_weboffice_token_with_options_async(request, runtime)

    def get_batch_with_options(
        self,
        request: main_models.GetBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_with_options_async(
        self,
        request: main_models.GetBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch(
        self,
        request: main_models.GetBatchRequest,
    ) -> main_models.GetBatchResponse:
        runtime = RuntimeOptions()
        return self.get_batch_with_options(request, runtime)

    async def get_batch_async(
        self,
        request: main_models.GetBatchRequest,
    ) -> main_models.GetBatchResponse:
        runtime = RuntimeOptions()
        return await self.get_batch_with_options_async(request, runtime)

    def get_binding_with_options(
        self,
        request: main_models.GetBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_binding_with_options_async(
        self,
        request: main_models.GetBindingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBindingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBinding',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_binding(
        self,
        request: main_models.GetBindingRequest,
    ) -> main_models.GetBindingResponse:
        runtime = RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    async def get_binding_async(
        self,
        request: main_models.GetBindingRequest,
    ) -> main_models.GetBindingResponse:
        runtime = RuntimeOptions()
        return await self.get_binding_with_options_async(request, runtime)

    def get_drmlicense_with_options(
        self,
        request: main_models.GetDRMLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDRMLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not DaraCore.is_null(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDRMLicense',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDRMLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_drmlicense_with_options_async(
        self,
        request: main_models.GetDRMLicenseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDRMLicenseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not DaraCore.is_null(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.protection_system):
            query['ProtectionSystem'] = request.protection_system
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDRMLicense',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDRMLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_drmlicense(
        self,
        request: main_models.GetDRMLicenseRequest,
    ) -> main_models.GetDRMLicenseResponse:
        runtime = RuntimeOptions()
        return self.get_drmlicense_with_options(request, runtime)

    async def get_drmlicense_async(
        self,
        request: main_models.GetDRMLicenseRequest,
    ) -> main_models.GetDRMLicenseResponse:
        runtime = RuntimeOptions()
        return await self.get_drmlicense_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: main_models.GetDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: main_models.GetDatasetRequest,
    ) -> main_models.GetDatasetResponse:
        runtime = RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_decode_blind_watermark_result_with_options(
        self,
        request: main_models.GetDecodeBlindWatermarkResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDecodeBlindWatermarkResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDecodeBlindWatermarkResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDecodeBlindWatermarkResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_decode_blind_watermark_result_with_options_async(
        self,
        request: main_models.GetDecodeBlindWatermarkResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDecodeBlindWatermarkResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDecodeBlindWatermarkResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDecodeBlindWatermarkResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_decode_blind_watermark_result(
        self,
        request: main_models.GetDecodeBlindWatermarkResultRequest,
    ) -> main_models.GetDecodeBlindWatermarkResultResponse:
        runtime = RuntimeOptions()
        return self.get_decode_blind_watermark_result_with_options(request, runtime)

    async def get_decode_blind_watermark_result_async(
        self,
        request: main_models.GetDecodeBlindWatermarkResultRequest,
    ) -> main_models.GetDecodeBlindWatermarkResultResponse:
        runtime = RuntimeOptions()
        return await self.get_decode_blind_watermark_result_with_options_async(request, runtime)

    def get_figure_cluster_with_options(
        self,
        request: main_models.GetFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFigureClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_figure_cluster_with_options_async(
        self,
        request: main_models.GetFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFigureClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_figure_cluster(
        self,
        request: main_models.GetFigureClusterRequest,
    ) -> main_models.GetFigureClusterResponse:
        runtime = RuntimeOptions()
        return self.get_figure_cluster_with_options(request, runtime)

    async def get_figure_cluster_async(
        self,
        request: main_models.GetFigureClusterRequest,
    ) -> main_models.GetFigureClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_figure_cluster_with_options_async(request, runtime)

    def get_file_meta_with_options(
        self,
        tmp_req: main_models.GetFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileMetaResponse:
        tmp_req.validate()
        request = main_models.GetFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_meta_with_options_async(
        self,
        tmp_req: main_models.GetFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFileMetaResponse:
        tmp_req.validate()
        request = main_models.GetFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.uri):
            query['URI'] = request.uri
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_meta(
        self,
        request: main_models.GetFileMetaRequest,
    ) -> main_models.GetFileMetaResponse:
        runtime = RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    async def get_file_meta_async(
        self,
        request: main_models.GetFileMetaRequest,
    ) -> main_models.GetFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.get_file_meta_with_options_async(request, runtime)

    def get_image_moderation_result_with_options(
        self,
        request: main_models.GetImageModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageModerationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_moderation_result_with_options_async(
        self,
        request: main_models.GetImageModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageModerationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_moderation_result(
        self,
        request: main_models.GetImageModerationResultRequest,
    ) -> main_models.GetImageModerationResultResponse:
        runtime = RuntimeOptions()
        return self.get_image_moderation_result_with_options(request, runtime)

    async def get_image_moderation_result_async(
        self,
        request: main_models.GetImageModerationResultRequest,
    ) -> main_models.GetImageModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.get_image_moderation_result_with_options_async(request, runtime)

    def get_ossbucket_attachment_with_options(
        self,
        request: main_models.GetOSSBucketAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSBucketAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOSSBucketAttachment',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSBucketAttachmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ossbucket_attachment_with_options_async(
        self,
        request: main_models.GetOSSBucketAttachmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOSSBucketAttachmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ossbucket):
            query['OSSBucket'] = request.ossbucket
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOSSBucketAttachment',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOSSBucketAttachmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ossbucket_attachment(
        self,
        request: main_models.GetOSSBucketAttachmentRequest,
    ) -> main_models.GetOSSBucketAttachmentResponse:
        runtime = RuntimeOptions()
        return self.get_ossbucket_attachment_with_options(request, runtime)

    async def get_ossbucket_attachment_async(
        self,
        request: main_models.GetOSSBucketAttachmentRequest,
    ) -> main_models.GetOSSBucketAttachmentResponse:
        runtime = RuntimeOptions()
        return await self.get_ossbucket_attachment_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: main_models.GetProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.with_statistics):
            query['WithStatistics'] = request.with_statistics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: main_models.GetProjectRequest,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_story_with_options(
        self,
        request: main_models.GetStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_story_with_options_async(
        self,
        request: main_models.GetStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_story(
        self,
        request: main_models.GetStoryRequest,
    ) -> main_models.GetStoryResponse:
        runtime = RuntimeOptions()
        return self.get_story_with_options(request, runtime)

    async def get_story_async(
        self,
        request: main_models.GetStoryRequest,
    ) -> main_models.GetStoryResponse:
        runtime = RuntimeOptions()
        return await self.get_story_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_trigger_with_options(
        self,
        request: main_models.GetTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trigger_with_options_async(
        self,
        request: main_models.GetTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trigger(
        self,
        request: main_models.GetTriggerRequest,
    ) -> main_models.GetTriggerResponse:
        runtime = RuntimeOptions()
        return self.get_trigger_with_options(request, runtime)

    async def get_trigger_async(
        self,
        request: main_models.GetTriggerRequest,
    ) -> main_models.GetTriggerResponse:
        runtime = RuntimeOptions()
        return await self.get_trigger_with_options_async(request, runtime)

    def get_video_label_classification_result_with_options(
        self,
        request: main_models.GetVideoLabelClassificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoLabelClassificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoLabelClassificationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoLabelClassificationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_label_classification_result_with_options_async(
        self,
        request: main_models.GetVideoLabelClassificationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoLabelClassificationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoLabelClassificationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoLabelClassificationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_label_classification_result(
        self,
        request: main_models.GetVideoLabelClassificationResultRequest,
    ) -> main_models.GetVideoLabelClassificationResultResponse:
        runtime = RuntimeOptions()
        return self.get_video_label_classification_result_with_options(request, runtime)

    async def get_video_label_classification_result_async(
        self,
        request: main_models.GetVideoLabelClassificationResultRequest,
    ) -> main_models.GetVideoLabelClassificationResultResponse:
        runtime = RuntimeOptions()
        return await self.get_video_label_classification_result_with_options_async(request, runtime)

    def get_video_moderation_result_with_options(
        self,
        request: main_models.GetVideoModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoModerationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoModerationResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_video_moderation_result_with_options_async(
        self,
        request: main_models.GetVideoModerationResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetVideoModerationResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetVideoModerationResult',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetVideoModerationResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_video_moderation_result(
        self,
        request: main_models.GetVideoModerationResultRequest,
    ) -> main_models.GetVideoModerationResultResponse:
        runtime = RuntimeOptions()
        return self.get_video_moderation_result_with_options(request, runtime)

    async def get_video_moderation_result_async(
        self,
        request: main_models.GetVideoModerationResultRequest,
    ) -> main_models.GetVideoModerationResultResponse:
        runtime = RuntimeOptions()
        return await self.get_video_moderation_result_with_options_async(request, runtime)

    def index_file_meta_with_options(
        self,
        tmp_req: main_models.IndexFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IndexFileMetaResponse:
        tmp_req.validate()
        request = main_models.IndexFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file):
            request.file_shrink = Utils.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.file_shrink):
            query['File'] = request.file_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IndexFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IndexFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def index_file_meta_with_options_async(
        self,
        tmp_req: main_models.IndexFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IndexFileMetaResponse:
        tmp_req.validate()
        request = main_models.IndexFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file):
            request.file_shrink = Utils.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        if not DaraCore.is_null(tmp_req.notification):
            request.notification_shrink = Utils.array_to_string_with_specified_style(tmp_req.notification, 'Notification', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.file_shrink):
            query['File'] = request.file_shrink
        if not DaraCore.is_null(request.notification_shrink):
            query['Notification'] = request.notification_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IndexFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IndexFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def index_file_meta(
        self,
        request: main_models.IndexFileMetaRequest,
    ) -> main_models.IndexFileMetaResponse:
        runtime = RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    async def index_file_meta_async(
        self,
        request: main_models.IndexFileMetaRequest,
    ) -> main_models.IndexFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.index_file_meta_with_options_async(request, runtime)

    def list_attached_ossbuckets_with_options(
        self,
        request: main_models.ListAttachedOSSBucketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAttachedOSSBucketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAttachedOSSBuckets',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAttachedOSSBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_attached_ossbuckets_with_options_async(
        self,
        request: main_models.ListAttachedOSSBucketsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAttachedOSSBucketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAttachedOSSBuckets',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAttachedOSSBucketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_attached_ossbuckets(
        self,
        request: main_models.ListAttachedOSSBucketsRequest,
    ) -> main_models.ListAttachedOSSBucketsResponse:
        runtime = RuntimeOptions()
        return self.list_attached_ossbuckets_with_options(request, runtime)

    async def list_attached_ossbuckets_async(
        self,
        request: main_models.ListAttachedOSSBucketsRequest,
    ) -> main_models.ListAttachedOSSBucketsResponse:
        runtime = RuntimeOptions()
        return await self.list_attached_ossbuckets_with_options_async(request, runtime)

    def list_batches_with_options(
        self,
        request: main_models.ListBatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBatches',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_batches_with_options_async(
        self,
        request: main_models.ListBatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBatches',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_batches(
        self,
        request: main_models.ListBatchesRequest,
    ) -> main_models.ListBatchesResponse:
        runtime = RuntimeOptions()
        return self.list_batches_with_options(request, runtime)

    async def list_batches_async(
        self,
        request: main_models.ListBatchesRequest,
    ) -> main_models.ListBatchesResponse:
        runtime = RuntimeOptions()
        return await self.list_batches_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: main_models.ListBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindings',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: main_models.ListBindingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBindingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBindings',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_bindings(
        self,
        request: main_models.ListBindingsRequest,
    ) -> main_models.ListBindingsResponse:
        runtime = RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: main_models.ListBindingsRequest,
    ) -> main_models.ListBindingsResponse:
        runtime = RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: main_models.ListDatasetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDatasetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatasets',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: main_models.ListDatasetsRequest,
    ) -> main_models.ListDatasetsResponse:
        runtime = RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        tmp_req: main_models.ListProjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectsResponse:
        tmp_req.validate()
        request = main_models.ListProjectsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.prefix):
            query['Prefix'] = request.prefix
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProjects',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: main_models.ListProjectsRequest,
    ) -> main_models.ListProjectsResponse:
        runtime = RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        request: main_models.ListRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: main_models.ListRegionsRequest,
    ) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.end_time_range):
            request.end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.start_time_range):
            request.start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.task_types):
            request.task_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not DaraCore.is_null(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.end_time_range):
            request.end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.end_time_range, 'EndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.start_time_range):
            request.start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.start_time_range, 'StartTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.task_types):
            request.task_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_types, 'TaskTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time_range_shrink):
            query['EndTimeRange'] = request.end_time_range_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.request_definition):
            query['RequestDefinition'] = request.request_definition
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.start_time_range_shrink):
            query['StartTimeRange'] = request.start_time_range_shrink
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        if not DaraCore.is_null(request.task_types_shrink):
            query['TaskTypes'] = request.task_types_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def list_triggers_with_options(
        self,
        request: main_models.ListTriggersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTriggersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTriggers',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTriggersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_triggers_with_options_async(
        self,
        request: main_models.ListTriggersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTriggersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.tag_selector):
            query['TagSelector'] = request.tag_selector
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTriggers',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTriggersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_triggers(
        self,
        request: main_models.ListTriggersRequest,
    ) -> main_models.ListTriggersResponse:
        runtime = RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    async def list_triggers_async(
        self,
        request: main_models.ListTriggersRequest,
    ) -> main_models.ListTriggersResponse:
        runtime = RuntimeOptions()
        return await self.list_triggers_with_options_async(request, runtime)

    def query_figure_clusters_with_options(
        self,
        tmp_req: main_models.QueryFigureClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFigureClustersResponse:
        tmp_req.validate()
        request = main_models.QueryFigureClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.update_time_range):
            request.update_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not DaraCore.is_null(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFigureClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFigureClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_figure_clusters_with_options_async(
        self,
        tmp_req: main_models.QueryFigureClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryFigureClustersResponse:
        tmp_req.validate()
        request = main_models.QueryFigureClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.update_time_range):
            request.update_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        if not DaraCore.is_null(request.with_total_count):
            query['WithTotalCount'] = request.with_total_count
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryFigureClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryFigureClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_figure_clusters(
        self,
        request: main_models.QueryFigureClustersRequest,
    ) -> main_models.QueryFigureClustersResponse:
        runtime = RuntimeOptions()
        return self.query_figure_clusters_with_options(request, runtime)

    async def query_figure_clusters_async(
        self,
        request: main_models.QueryFigureClustersRequest,
    ) -> main_models.QueryFigureClustersResponse:
        runtime = RuntimeOptions()
        return await self.query_figure_clusters_with_options_async(request, runtime)

    def query_location_date_clusters_with_options(
        self,
        tmp_req: main_models.QueryLocationDateClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocationDateClustersResponse:
        tmp_req.validate()
        request = main_models.QueryLocationDateClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address):
            request.address_shrink = Utils.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.update_time_range):
            request.update_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.address_shrink):
            query['Address'] = request.address_shrink
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not DaraCore.is_null(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not DaraCore.is_null(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocationDateClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocationDateClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_location_date_clusters_with_options_async(
        self,
        tmp_req: main_models.QueryLocationDateClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryLocationDateClustersResponse:
        tmp_req.validate()
        request = main_models.QueryLocationDateClustersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.address):
            request.address_shrink = Utils.array_to_string_with_specified_style(tmp_req.address, 'Address', 'json')
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_end_time_range):
            request.location_date_cluster_end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_end_time_range, 'LocationDateClusterEndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_levels):
            request.location_date_cluster_levels_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_levels, 'LocationDateClusterLevels', 'json')
        if not DaraCore.is_null(tmp_req.location_date_cluster_start_time_range):
            request.location_date_cluster_start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.location_date_cluster_start_time_range, 'LocationDateClusterStartTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.update_time_range):
            request.update_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_time_range, 'UpdateTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.address_shrink):
            query['Address'] = request.address_shrink
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.location_date_cluster_end_time_range_shrink):
            query['LocationDateClusterEndTimeRange'] = request.location_date_cluster_end_time_range_shrink
        if not DaraCore.is_null(request.location_date_cluster_levels_shrink):
            query['LocationDateClusterLevels'] = request.location_date_cluster_levels_shrink
        if not DaraCore.is_null(request.location_date_cluster_start_time_range_shrink):
            query['LocationDateClusterStartTimeRange'] = request.location_date_cluster_start_time_range_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.update_time_range_shrink):
            query['UpdateTimeRange'] = request.update_time_range_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryLocationDateClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryLocationDateClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_location_date_clusters(
        self,
        request: main_models.QueryLocationDateClustersRequest,
    ) -> main_models.QueryLocationDateClustersResponse:
        runtime = RuntimeOptions()
        return self.query_location_date_clusters_with_options(request, runtime)

    async def query_location_date_clusters_async(
        self,
        request: main_models.QueryLocationDateClustersRequest,
    ) -> main_models.QueryLocationDateClustersResponse:
        runtime = RuntimeOptions()
        return await self.query_location_date_clusters_with_options_async(request, runtime)

    def query_similar_image_clusters_with_options(
        self,
        request: main_models.QuerySimilarImageClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySimilarImageClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySimilarImageClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySimilarImageClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_similar_image_clusters_with_options_async(
        self,
        request: main_models.QuerySimilarImageClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QuerySimilarImageClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QuerySimilarImageClusters',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QuerySimilarImageClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_similar_image_clusters(
        self,
        request: main_models.QuerySimilarImageClustersRequest,
    ) -> main_models.QuerySimilarImageClustersResponse:
        runtime = RuntimeOptions()
        return self.query_similar_image_clusters_with_options(request, runtime)

    async def query_similar_image_clusters_async(
        self,
        request: main_models.QuerySimilarImageClustersRequest,
    ) -> main_models.QuerySimilarImageClustersResponse:
        runtime = RuntimeOptions()
        return await self.query_similar_image_clusters_with_options_async(request, runtime)

    def query_stories_with_options(
        self,
        tmp_req: main_models.QueryStoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStoriesResponse:
        tmp_req.validate()
        request = main_models.QueryStoriesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not DaraCore.is_null(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not DaraCore.is_null(request.story_name):
            query['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not DaraCore.is_null(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            query['StoryType'] = request.story_type
        if not DaraCore.is_null(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStories',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_stories_with_options_async(
        self,
        tmp_req: main_models.QueryStoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryStoriesResponse:
        tmp_req.validate()
        request = main_models.QueryStoriesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.create_time_range):
            request.create_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.create_time_range, 'CreateTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not DaraCore.is_null(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.story_end_time_range, 'StoryEndTimeRange', 'json')
        if not DaraCore.is_null(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = Utils.array_to_string_with_specified_style(tmp_req.story_start_time_range, 'StoryStartTimeRange', 'json')
        query = {}
        if not DaraCore.is_null(request.create_time_range_shrink):
            query['CreateTimeRange'] = request.create_time_range_shrink
        if not DaraCore.is_null(request.custom_labels):
            query['CustomLabels'] = request.custom_labels
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.figure_cluster_ids_shrink):
            query['FigureClusterIds'] = request.figure_cluster_ids_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.story_end_time_range_shrink):
            query['StoryEndTimeRange'] = request.story_end_time_range_shrink
        if not DaraCore.is_null(request.story_name):
            query['StoryName'] = request.story_name
        if not DaraCore.is_null(request.story_start_time_range_shrink):
            query['StoryStartTimeRange'] = request.story_start_time_range_shrink
        if not DaraCore.is_null(request.story_sub_type):
            query['StorySubType'] = request.story_sub_type
        if not DaraCore.is_null(request.story_type):
            query['StoryType'] = request.story_type
        if not DaraCore.is_null(request.with_empty_stories):
            query['WithEmptyStories'] = request.with_empty_stories
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryStories',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryStoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_stories(
        self,
        request: main_models.QueryStoriesRequest,
    ) -> main_models.QueryStoriesResponse:
        runtime = RuntimeOptions()
        return self.query_stories_with_options(request, runtime)

    async def query_stories_async(
        self,
        request: main_models.QueryStoriesRequest,
    ) -> main_models.QueryStoriesResponse:
        runtime = RuntimeOptions()
        return await self.query_stories_with_options_async(request, runtime)

    def refresh_weboffice_token_with_options(
        self,
        tmp_req: main_models.RefreshWebofficeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshWebofficeTokenResponse:
        tmp_req.validate()
        request = main_models.RefreshWebofficeTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshWebofficeToken',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshWebofficeTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_weboffice_token_with_options_async(
        self,
        tmp_req: main_models.RefreshWebofficeTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RefreshWebofficeTokenResponse:
        tmp_req.validate()
        request = main_models.RefreshWebofficeTokenShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.access_token):
            query['AccessToken'] = request.access_token
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.refresh_token):
            query['RefreshToken'] = request.refresh_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RefreshWebofficeToken',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RefreshWebofficeTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_weboffice_token(
        self,
        request: main_models.RefreshWebofficeTokenRequest,
    ) -> main_models.RefreshWebofficeTokenResponse:
        runtime = RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    async def refresh_weboffice_token_async(
        self,
        request: main_models.RefreshWebofficeTokenRequest,
    ) -> main_models.RefreshWebofficeTokenResponse:
        runtime = RuntimeOptions()
        return await self.refresh_weboffice_token_with_options_async(request, runtime)

    def remove_story_files_with_options(
        self,
        tmp_req: main_models.RemoveStoryFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveStoryFilesResponse:
        tmp_req.validate()
        request = main_models.RemoveStoryFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveStoryFiles',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveStoryFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_story_files_with_options_async(
        self,
        tmp_req: main_models.RemoveStoryFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveStoryFilesResponse:
        tmp_req.validate()
        request = main_models.RemoveStoryFilesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.files):
            request.files_shrink = Utils.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        body = {}
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.files_shrink):
            body['Files'] = request.files_shrink
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RemoveStoryFiles',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveStoryFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_story_files(
        self,
        request: main_models.RemoveStoryFilesRequest,
    ) -> main_models.RemoveStoryFilesResponse:
        runtime = RuntimeOptions()
        return self.remove_story_files_with_options(request, runtime)

    async def remove_story_files_async(
        self,
        request: main_models.RemoveStoryFilesRequest,
    ) -> main_models.RemoveStoryFilesResponse:
        runtime = RuntimeOptions()
        return await self.remove_story_files_with_options_async(request, runtime)

    def resume_batch_with_options(
        self,
        request: main_models.ResumeBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_batch_with_options_async(
        self,
        request: main_models.ResumeBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_batch(
        self,
        request: main_models.ResumeBatchRequest,
    ) -> main_models.ResumeBatchResponse:
        runtime = RuntimeOptions()
        return self.resume_batch_with_options(request, runtime)

    async def resume_batch_async(
        self,
        request: main_models.ResumeBatchRequest,
    ) -> main_models.ResumeBatchResponse:
        runtime = RuntimeOptions()
        return await self.resume_batch_with_options_async(request, runtime)

    def resume_trigger_with_options(
        self,
        request: main_models.ResumeTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_trigger_with_options_async(
        self,
        request: main_models.ResumeTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResumeTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ResumeTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResumeTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_trigger(
        self,
        request: main_models.ResumeTriggerRequest,
    ) -> main_models.ResumeTriggerResponse:
        runtime = RuntimeOptions()
        return self.resume_trigger_with_options(request, runtime)

    async def resume_trigger_async(
        self,
        request: main_models.ResumeTriggerRequest,
    ) -> main_models.ResumeTriggerResponse:
        runtime = RuntimeOptions()
        return await self.resume_trigger_with_options_async(request, runtime)

    def search_image_figure_cluster_with_options(
        self,
        tmp_req: main_models.SearchImageFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageFigureClusterResponse:
        tmp_req.validate()
        request = main_models.SearchImageFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_image_figure_cluster_with_options_async(
        self,
        tmp_req: main_models.SearchImageFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchImageFigureClusterResponse:
        tmp_req.validate()
        request = main_models.SearchImageFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.credential_config):
            request.credential_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.credential_config, 'CredentialConfig', 'json')
        query = {}
        if not DaraCore.is_null(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchImageFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchImageFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_image_figure_cluster(
        self,
        request: main_models.SearchImageFigureClusterRequest,
    ) -> main_models.SearchImageFigureClusterResponse:
        runtime = RuntimeOptions()
        return self.search_image_figure_cluster_with_options(request, runtime)

    async def search_image_figure_cluster_async(
        self,
        request: main_models.SearchImageFigureClusterRequest,
    ) -> main_models.SearchImageFigureClusterResponse:
        runtime = RuntimeOptions()
        return await self.search_image_figure_cluster_with_options_async(request, runtime)

    def semantic_query_with_options(
        self,
        tmp_req: main_models.SemanticQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SemanticQueryResponse:
        tmp_req.validate()
        request = main_models.SemanticQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.media_types):
            request.media_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SemanticQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SemanticQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def semantic_query_with_options_async(
        self,
        tmp_req: main_models.SemanticQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SemanticQueryResponse:
        tmp_req.validate()
        request = main_models.SemanticQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.media_types):
            request.media_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.media_types, 'MediaTypes', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.media_types_shrink):
            query['MediaTypes'] = request.media_types_shrink
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.source_uri):
            query['SourceURI'] = request.source_uri
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SemanticQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SemanticQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def semantic_query(
        self,
        request: main_models.SemanticQueryRequest,
    ) -> main_models.SemanticQueryResponse:
        runtime = RuntimeOptions()
        return self.semantic_query_with_options(request, runtime)

    async def semantic_query_async(
        self,
        request: main_models.SemanticQueryRequest,
    ) -> main_models.SemanticQueryResponse:
        runtime = RuntimeOptions()
        return await self.semantic_query_with_options_async(request, runtime)

    def simple_query_with_options(
        self,
        tmp_req: main_models.SimpleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SimpleQueryResponse:
        tmp_req.validate()
        request = main_models.SimpleQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregations):
            request.aggregations_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not DaraCore.is_null(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SimpleQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SimpleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_query_with_options_async(
        self,
        tmp_req: main_models.SimpleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SimpleQueryResponse:
        tmp_req.validate()
        request = main_models.SimpleQueryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.aggregations):
            request.aggregations_shrink = Utils.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.with_fields):
            request.with_fields_shrink = Utils.array_to_string_with_specified_style(tmp_req.with_fields, 'WithFields', 'json')
        query = {}
        if not DaraCore.is_null(request.aggregations_shrink):
            query['Aggregations'] = request.aggregations_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.query_shrink):
            query['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort):
            query['Sort'] = request.sort
        if not DaraCore.is_null(request.with_fields_shrink):
            query['WithFields'] = request.with_fields_shrink
        if not DaraCore.is_null(request.without_total_hits):
            query['WithoutTotalHits'] = request.without_total_hits
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SimpleQuery',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SimpleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_query(
        self,
        request: main_models.SimpleQueryRequest,
    ) -> main_models.SimpleQueryResponse:
        runtime = RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    async def simple_query_async(
        self,
        request: main_models.SimpleQueryRequest,
    ) -> main_models.SimpleQueryResponse:
        runtime = RuntimeOptions()
        return await self.simple_query_with_options_async(request, runtime)

    def suspend_batch_with_options(
        self,
        request: main_models.SuspendBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_batch_with_options_async(
        self,
        request: main_models.SuspendBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendBatchResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_batch(
        self,
        request: main_models.SuspendBatchRequest,
    ) -> main_models.SuspendBatchResponse:
        runtime = RuntimeOptions()
        return self.suspend_batch_with_options(request, runtime)

    async def suspend_batch_async(
        self,
        request: main_models.SuspendBatchRequest,
    ) -> main_models.SuspendBatchResponse:
        runtime = RuntimeOptions()
        return await self.suspend_batch_with_options_async(request, runtime)

    def suspend_trigger_with_options(
        self,
        request: main_models.SuspendTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_trigger_with_options_async(
        self,
        request: main_models.SuspendTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SuspendTriggerResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SuspendTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SuspendTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_trigger(
        self,
        request: main_models.SuspendTriggerRequest,
    ) -> main_models.SuspendTriggerResponse:
        runtime = RuntimeOptions()
        return self.suspend_trigger_with_options(request, runtime)

    async def suspend_trigger_async(
        self,
        request: main_models.SuspendTriggerRequest,
    ) -> main_models.SuspendTriggerResponse:
        runtime = RuntimeOptions()
        return await self.suspend_trigger_with_options_async(request, runtime)

    def update_batch_with_options(
        self,
        tmp_req: main_models.UpdateBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_batch_with_options_async(
        self,
        tmp_req: main_models.UpdateBatchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBatchResponse:
        tmp_req.validate()
        request = main_models.UpdateBatchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBatch',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_batch(
        self,
        request: main_models.UpdateBatchRequest,
    ) -> main_models.UpdateBatchResponse:
        runtime = RuntimeOptions()
        return self.update_batch_with_options(request, runtime)

    async def update_batch_async(
        self,
        request: main_models.UpdateBatchRequest,
    ) -> main_models.UpdateBatchResponse:
        runtime = RuntimeOptions()
        return await self.update_batch_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        tmp_req: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            query['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        tmp_req: main_models.UpdateDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDatasetResponse:
        tmp_req.validate()
        request = main_models.UpdateDatasetShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_config):
            request.dataset_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_config, 'DatasetConfig', 'json')
        if not DaraCore.is_null(tmp_req.workflow_parameters):
            request.workflow_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.workflow_parameters, 'WorkflowParameters', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_config_shrink):
            query['DatasetConfig'] = request.dataset_config_shrink
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workflow_parameters_shrink):
            query['WorkflowParameters'] = request.workflow_parameters_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDataset',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: main_models.UpdateDatasetRequest,
    ) -> main_models.UpdateDatasetResponse:
        runtime = RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_figure_cluster_with_options(
        self,
        tmp_req: main_models.UpdateFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFigureClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.figure_cluster):
            request.figure_cluster_shrink = Utils.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFigureClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_figure_cluster_with_options_async(
        self,
        tmp_req: main_models.UpdateFigureClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFigureClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateFigureClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.figure_cluster):
            request.figure_cluster_shrink = Utils.array_to_string_with_specified_style(tmp_req.figure_cluster, 'FigureCluster', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.figure_cluster_shrink):
            query['FigureCluster'] = request.figure_cluster_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFigureCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFigureClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_figure_cluster(
        self,
        request: main_models.UpdateFigureClusterRequest,
    ) -> main_models.UpdateFigureClusterResponse:
        runtime = RuntimeOptions()
        return self.update_figure_cluster_with_options(request, runtime)

    async def update_figure_cluster_async(
        self,
        request: main_models.UpdateFigureClusterRequest,
    ) -> main_models.UpdateFigureClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_figure_cluster_with_options_async(request, runtime)

    def update_file_meta_with_options(
        self,
        tmp_req: main_models.UpdateFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileMetaResponse:
        tmp_req.validate()
        request = main_models.UpdateFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file):
            request.file_shrink = Utils.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.file_shrink):
            query['File'] = request.file_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_file_meta_with_options_async(
        self,
        tmp_req: main_models.UpdateFileMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFileMetaResponse:
        tmp_req.validate()
        request = main_models.UpdateFileMetaShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.file):
            request.file_shrink = Utils.array_to_string_with_specified_style(tmp_req.file, 'File', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.file_shrink):
            query['File'] = request.file_shrink
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFileMeta',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFileMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_file_meta(
        self,
        request: main_models.UpdateFileMetaRequest,
    ) -> main_models.UpdateFileMetaResponse:
        runtime = RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    async def update_file_meta_async(
        self,
        request: main_models.UpdateFileMetaRequest,
    ) -> main_models.UpdateFileMetaResponse:
        runtime = RuntimeOptions()
        return await self.update_file_meta_with_options_async(request, runtime)

    def update_location_date_cluster_with_options(
        self,
        tmp_req: main_models.UpdateLocationDateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocationDateClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateLocationDateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_id):
            query['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocationDateCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocationDateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_location_date_cluster_with_options_async(
        self,
        tmp_req: main_models.UpdateLocationDateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLocationDateClusterResponse:
        tmp_req.validate()
        request = main_models.UpdateLocationDateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        query = {}
        if not DaraCore.is_null(request.custom_id):
            query['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            query['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            query['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLocationDateCluster',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLocationDateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_location_date_cluster(
        self,
        request: main_models.UpdateLocationDateClusterRequest,
    ) -> main_models.UpdateLocationDateClusterResponse:
        runtime = RuntimeOptions()
        return self.update_location_date_cluster_with_options(request, runtime)

    async def update_location_date_cluster_async(
        self,
        request: main_models.UpdateLocationDateClusterRequest,
    ) -> main_models.UpdateLocationDateClusterResponse:
        runtime = RuntimeOptions()
        return await self.update_location_date_cluster_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        tmp_req: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        tmp_req.validate()
        request = main_models.UpdateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            query['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: main_models.UpdateProjectRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        tmp_req.validate()
        request = main_models.UpdateProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.dataset_max_bind_count):
            query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        if not DaraCore.is_null(request.dataset_max_entity_count):
            query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        if not DaraCore.is_null(request.dataset_max_file_count):
            query['DatasetMaxFileCount'] = request.dataset_max_file_count
        if not DaraCore.is_null(request.dataset_max_relation_count):
            query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        if not DaraCore.is_null(request.dataset_max_total_file_size):
            query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not DaraCore.is_null(request.project_name):
            query['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.service_role):
            query['ServiceRole'] = request.service_role
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_story_with_options(
        self,
        tmp_req: main_models.UpdateStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoryResponse:
        tmp_req.validate()
        request = main_models.UpdateStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cover):
            request.cover_shrink = Utils.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not DaraCore.is_null(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_story_with_options_async(
        self,
        tmp_req: main_models.UpdateStoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStoryResponse:
        tmp_req.validate()
        request = main_models.UpdateStoryShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.cover):
            request.cover_shrink = Utils.array_to_string_with_specified_style(tmp_req.cover, 'Cover', 'json')
        if not DaraCore.is_null(tmp_req.custom_labels):
            request.custom_labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        body = {}
        if not DaraCore.is_null(request.cover_shrink):
            body['Cover'] = request.cover_shrink
        if not DaraCore.is_null(request.custom_id):
            body['CustomId'] = request.custom_id
        if not DaraCore.is_null(request.custom_labels_shrink):
            body['CustomLabels'] = request.custom_labels_shrink
        if not DaraCore.is_null(request.dataset_name):
            body['DatasetName'] = request.dataset_name
        if not DaraCore.is_null(request.object_id):
            body['ObjectId'] = request.object_id
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.story_name):
            body['StoryName'] = request.story_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStory',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_story(
        self,
        request: main_models.UpdateStoryRequest,
    ) -> main_models.UpdateStoryResponse:
        runtime = RuntimeOptions()
        return self.update_story_with_options(request, runtime)

    async def update_story_async(
        self,
        request: main_models.UpdateStoryRequest,
    ) -> main_models.UpdateStoryResponse:
        runtime = RuntimeOptions()
        return await self.update_story_with_options_async(request, runtime)

    def update_trigger_with_options(
        self,
        tmp_req: main_models.UpdateTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTriggerResponse:
        tmp_req.validate()
        request = main_models.UpdateTriggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_trigger_with_options_async(
        self,
        tmp_req: main_models.UpdateTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTriggerResponse:
        tmp_req.validate()
        request = main_models.UpdateTriggerShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.actions):
            request.actions_shrink = Utils.array_to_string_with_specified_style(tmp_req.actions, 'Actions', 'json')
        if not DaraCore.is_null(tmp_req.input):
            request.input_shrink = Utils.array_to_string_with_specified_style(tmp_req.input, 'Input', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        body = {}
        if not DaraCore.is_null(request.actions_shrink):
            body['Actions'] = request.actions_shrink
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.input_shrink):
            body['Input'] = request.input_shrink
        if not DaraCore.is_null(request.project_name):
            body['ProjectName'] = request.project_name
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTrigger',
            version = '2020-09-30',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_trigger(
        self,
        request: main_models.UpdateTriggerRequest,
    ) -> main_models.UpdateTriggerResponse:
        runtime = RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)

    async def update_trigger_async(
        self,
        request: main_models.UpdateTriggerRequest,
    ) -> main_models.UpdateTriggerResponse:
        runtime = RuntimeOptions()
        return await self.update_trigger_with_options_async(request, runtime)
