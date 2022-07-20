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

    def add_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.AddStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AddStoryFilesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.add_story_files_with_options(request, runtime)

    async def add_story_files_async(
        self,
        request: imm_20200930_models.AddStoryFilesRequest,
    ) -> imm_20200930_models.AddStoryFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_story_files_with_options_async(request, runtime)

    def attach_ossbucket_with_options(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.attach_ossbucket_with_options(request, runtime)

    async def attach_ossbucket_async(
        self,
        request: imm_20200930_models.AttachOSSBucketRequest,
    ) -> imm_20200930_models.AttachOSSBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_ossbucket_with_options_async(request, runtime)

    def batch_delete_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchDeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_file_meta_with_options(request, runtime)

    async def batch_delete_file_meta_async(
        self,
        request: imm_20200930_models.BatchDeleteFileMetaRequest,
    ) -> imm_20200930_models.BatchDeleteFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_delete_file_meta_with_options_async(request, runtime)

    def batch_get_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchGetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchGetFileMetaShrinkRequest()
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
        runtime = util_models.RuntimeOptions()
        return self.batch_get_file_meta_with_options(request, runtime)

    async def batch_get_file_meta_async(
        self,
        request: imm_20200930_models.BatchGetFileMetaRequest,
    ) -> imm_20200930_models.BatchGetFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_get_file_meta_with_options_async(request, runtime)

    def batch_index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchIndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.BatchIndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.files):
            request.files_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.files, 'Files', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.files_shrink):
            query['Files'] = request.files_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
        runtime = util_models.RuntimeOptions()
        return self.batch_index_file_meta_with_options(request, runtime)

    async def batch_index_file_meta_async(
        self,
        request: imm_20200930_models.BatchIndexFileMetaRequest,
    ) -> imm_20200930_models.BatchIndexFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_index_file_meta_with_options_async(request, runtime)

    def batch_update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.BatchUpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.batch_update_file_meta_with_options(request, runtime)

    async def batch_update_file_meta_async(
        self,
        request: imm_20200930_models.BatchUpdateFileMetaRequest,
    ) -> imm_20200930_models.BatchUpdateFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_update_file_meta_with_options_async(request, runtime)

    def create_binding_with_options(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_binding_with_options(request, runtime)

    async def create_binding_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
    ) -> imm_20200930_models.CreateBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_with_options_async(request, runtime)

    def create_dataset_with_options(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
    ) -> imm_20200930_models.CreateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_detect_video_labels_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateDetectVideoLabelsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDetectVideoLabelsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDetectVideoLabelsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
            action='CreateDetectVideoLabelsTask',
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
            imm_20200930_models.CreateDetectVideoLabelsTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_detect_video_labels_task_with_options_async(
        self,
        tmp_req: imm_20200930_models.CreateDetectVideoLabelsTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDetectVideoLabelsTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateDetectVideoLabelsTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
            action='CreateDetectVideoLabelsTask',
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
            imm_20200930_models.CreateDetectVideoLabelsTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_detect_video_labels_task(
        self,
        request: imm_20200930_models.CreateDetectVideoLabelsTaskRequest,
    ) -> imm_20200930_models.CreateDetectVideoLabelsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_detect_video_labels_task_with_options(request, runtime)

    async def create_detect_video_labels_task_async(
        self,
        request: imm_20200930_models.CreateDetectVideoLabelsTaskRequest,
    ) -> imm_20200930_models.CreateDetectVideoLabelsTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_detect_video_labels_task_with_options_async(request, runtime)

    def create_figure_clustering_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClusteringTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClusteringTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clustering_task_with_options(request, runtime)

    async def create_figure_clustering_task_async(
        self,
        request: imm_20200930_models.CreateFigureClusteringTaskRequest,
    ) -> imm_20200930_models.CreateFigureClusteringTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clustering_task_with_options_async(request, runtime)

    def create_figure_clusters_merging_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateFigureClustersMergingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        runtime = util_models.RuntimeOptions()
        return self.create_figure_clusters_merging_task_with_options(request, runtime)

    async def create_figure_clusters_merging_task_async(
        self,
        request: imm_20200930_models.CreateFigureClustersMergingTaskRequest,
    ) -> imm_20200930_models.CreateFigureClustersMergingTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_figure_clusters_merging_task_with_options_async(request, runtime)

    def create_image_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reviewer):
            query['Reviewer'] = request.reviewer
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reviewer):
            query['Reviewer'] = request.reviewer
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
        runtime = util_models.RuntimeOptions()
        return self.create_image_moderation_task_with_options(request, runtime)

    async def create_image_moderation_task_async(
        self,
        request: imm_20200930_models.CreateImageModerationTaskRequest,
    ) -> imm_20200930_models.CreateImageModerationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_moderation_task_with_options_async(request, runtime)

    def create_image_splicing_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateImageSplicingTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateImageSplicingTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        runtime = util_models.RuntimeOptions()
        return self.create_image_splicing_task_with_options(request, runtime)

    async def create_image_splicing_task_async(
        self,
        request: imm_20200930_models.CreateImageSplicingTaskRequest,
    ) -> imm_20200930_models.CreateImageSplicingTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_splicing_task_with_options_async(request, runtime)

    def create_media_convert_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateMediaConvertTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateMediaConvertTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.sources):
            request.sources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.targets):
            request.targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.targets, 'Targets', 'json')
        query = {}
        if not UtilClient.is_unset(request.credential_config_shrink):
            query['CredentialConfig'] = request.credential_config_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        runtime = util_models.RuntimeOptions()
        return self.create_media_convert_task_with_options(request, runtime)

    async def create_media_convert_task_async(
        self,
        request: imm_20200930_models.CreateMediaConvertTaskRequest,
    ) -> imm_20200930_models.CreateMediaConvertTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_media_convert_task_with_options_async(request, runtime)

    def create_office_conversion_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.trim_policy), 'TrimPolicy', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateOfficeConversionTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        if not UtilClient.is_unset(tmp_req.trim_policy):
            request.trim_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.trim_policy), 'TrimPolicy', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
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
        runtime = util_models.RuntimeOptions()
        return self.create_office_conversion_task_with_options(request, runtime)

    async def create_office_conversion_task_async(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_office_conversion_task_with_options_async(request, runtime)

    def create_project_with_options(
        self,
        request: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.engine_concurrency):
            query['EngineConcurrency'] = request.engine_concurrency
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_queries_per_second):
            query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
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
        request: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.engine_concurrency):
            query['EngineConcurrency'] = request.engine_concurrency
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_queries_per_second):
            query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
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
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: imm_20200930_models.CreateProjectRequest,
    ) -> imm_20200930_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def create_story_with_options(
        self,
        tmp_req: imm_20200930_models.CreateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateStoryResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
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
        if not UtilClient.is_unset(request.notify_endpoint):
            body['NotifyEndpoint'] = request.notify_endpoint
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        body = {}
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
        if not UtilClient.is_unset(request.notify_endpoint):
            body['NotifyEndpoint'] = request.notify_endpoint
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
        runtime = util_models.RuntimeOptions()
        return self.create_story_with_options(request, runtime)

    async def create_story_async(
        self,
        request: imm_20200930_models.CreateStoryRequest,
    ) -> imm_20200930_models.CreateStoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_story_with_options_async(request, runtime)

    def create_video_moderation_task_with_options(
        self,
        tmp_req: imm_20200930_models.CreateVideoModerationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reviewer):
            query['Reviewer'] = request.reviewer
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.CreateVideoModerationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reviewer):
            query['Reviewer'] = request.reviewer
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
        runtime = util_models.RuntimeOptions()
        return self.create_video_moderation_task_with_options(request, runtime)

    async def create_video_moderation_task_async(
        self,
        request: imm_20200930_models.CreateVideoModerationTaskRequest,
    ) -> imm_20200930_models.CreateVideoModerationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_video_moderation_task_with_options_async(request, runtime)

    def delete_binding_with_options(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cleanup):
            query['Cleanup'] = request.cleanup
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cleanup):
            query['Cleanup'] = request.cleanup
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
        runtime = util_models.RuntimeOptions()
        return self.delete_binding_with_options(request, runtime)

    async def delete_binding_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
    ) -> imm_20200930_models.DeleteBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_binding_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_file_meta_with_options(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_file_meta_with_options(request, runtime)

    async def delete_file_meta_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_meta_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
    ) -> imm_20200930_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def delete_story_with_options(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteStoryResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_story_with_options(request, runtime)

    async def delete_story_async(
        self,
        request: imm_20200930_models.DeleteStoryRequest,
    ) -> imm_20200930_models.DeleteStoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_story_with_options_async(request, runtime)

    def detach_ossbucket_with_options(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.detach_ossbucket_with_options(request, runtime)

    async def detach_ossbucket_async(
        self,
        request: imm_20200930_models.DetachOSSBucketRequest,
    ) -> imm_20200930_models.DetachOSSBucketResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_ossbucket_with_options_async(request, runtime)

    def detect_image_bodies_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageBodiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageBodiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_bodies_with_options(request, runtime)

    async def detect_image_bodies_async(
        self,
        request: imm_20200930_models.DetectImageBodiesRequest,
    ) -> imm_20200930_models.DetectImageBodiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_bodies_with_options_async(request, runtime)

    def detect_image_codes_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_codes_with_options(request, runtime)

    async def detect_image_codes_async(
        self,
        request: imm_20200930_models.DetectImageCodesRequest,
    ) -> imm_20200930_models.DetectImageCodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_codes_with_options_async(request, runtime)

    def detect_image_cropping_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageCroppingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageCroppingShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_cropping_with_options(request, runtime)

    async def detect_image_cropping_async(
        self,
        request: imm_20200930_models.DetectImageCroppingRequest,
    ) -> imm_20200930_models.DetectImageCroppingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_cropping_with_options_async(request, runtime)

    def detect_image_faces_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageFacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageFacesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_faces_with_options(request, runtime)

    async def detect_image_faces_async(
        self,
        request: imm_20200930_models.DetectImageFacesRequest,
    ) -> imm_20200930_models.DetectImageFacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_faces_with_options_async(request, runtime)

    def detect_image_labels_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageLabelsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_labels_with_options(request, runtime)

    async def detect_image_labels_async(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_labels_with_options_async(request, runtime)

    def detect_image_score_with_options(
        self,
        tmp_req: imm_20200930_models.DetectImageScoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.DetectImageScoreShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.detect_image_score_with_options(request, runtime)

    async def detect_image_score_async(
        self,
        request: imm_20200930_models.DetectImageScoreRequest,
    ) -> imm_20200930_models.DetectImageScoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_image_score_with_options_async(request, runtime)

    def detect_text_anomaly_with_options(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.detect_text_anomaly_with_options(request, runtime)

    async def detect_text_anomaly_async(
        self,
        request: imm_20200930_models.DetectTextAnomalyRequest,
    ) -> imm_20200930_models.DetectTextAnomalyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_text_anomaly_with_options_async(request, runtime)

    def fuzzy_query_with_options(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
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
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
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
        request: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
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
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
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
        runtime = util_models.RuntimeOptions()
        return self.fuzzy_query_with_options(request, runtime)

    async def fuzzy_query_async(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.fuzzy_query_with_options_async(request, runtime)

    def get_binding_with_options(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_binding_with_options(request, runtime)

    async def get_binding_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
    ) -> imm_20200930_models.GetBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_binding_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
    ) -> imm_20200930_models.GetDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_detect_video_labels_result_with_options(
        self,
        request: imm_20200930_models.GetDetectVideoLabelsResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDetectVideoLabelsResultResponse:
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
            action='GetDetectVideoLabelsResult',
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
            imm_20200930_models.GetDetectVideoLabelsResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_detect_video_labels_result_with_options_async(
        self,
        request: imm_20200930_models.GetDetectVideoLabelsResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDetectVideoLabelsResultResponse:
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
            action='GetDetectVideoLabelsResult',
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
            imm_20200930_models.GetDetectVideoLabelsResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_detect_video_labels_result(
        self,
        request: imm_20200930_models.GetDetectVideoLabelsResultRequest,
    ) -> imm_20200930_models.GetDetectVideoLabelsResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_detect_video_labels_result_with_options(request, runtime)

    async def get_detect_video_labels_result_async(
        self,
        request: imm_20200930_models.GetDetectVideoLabelsResultRequest,
    ) -> imm_20200930_models.GetDetectVideoLabelsResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_detect_video_labels_result_with_options_async(request, runtime)

    def get_figure_cluster_with_options(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFigureClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_figure_cluster_with_options(request, runtime)

    async def get_figure_cluster_async(
        self,
        request: imm_20200930_models.GetFigureClusterRequest,
    ) -> imm_20200930_models.GetFigureClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_figure_cluster_with_options_async(request, runtime)

    def get_file_meta_with_options(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
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
        request: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_file_meta_with_options(request, runtime)

    async def get_file_meta_async(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
    ) -> imm_20200930_models.GetFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_meta_with_options_async(request, runtime)

    def get_media_meta_with_options(
        self,
        tmp_req: imm_20200930_models.GetMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetMediaMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
            action='GetMediaMeta',
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
            imm_20200930_models.GetMediaMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_media_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.GetMediaMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetMediaMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetMediaMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
            action='GetMediaMeta',
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
            imm_20200930_models.GetMediaMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_media_meta(
        self,
        request: imm_20200930_models.GetMediaMetaRequest,
    ) -> imm_20200930_models.GetMediaMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_media_meta_with_options(request, runtime)

    async def get_media_meta_async(
        self,
        request: imm_20200930_models.GetMediaMetaRequest,
    ) -> imm_20200930_models.GetMediaMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_media_meta_with_options_async(request, runtime)

    def get_ossbucket_attachment_with_options(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_ossbucket_attachment_with_options(request, runtime)

    async def get_ossbucket_attachment_async(
        self,
        request: imm_20200930_models.GetOSSBucketAttachmentRequest,
    ) -> imm_20200930_models.GetOSSBucketAttachmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ossbucket_attachment_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
    ) -> imm_20200930_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_story_with_options(
        self,
        request: imm_20200930_models.GetStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetStoryResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_story_with_options(request, runtime)

    async def get_story_async(
        self,
        request: imm_20200930_models.GetStoryRequest,
    ) -> imm_20200930_models.GetStoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_story_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: imm_20200930_models.GetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: imm_20200930_models.GetTaskRequest,
    ) -> imm_20200930_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_weboffice_urlwith_options(
        self,
        tmp_req: imm_20200930_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetWebofficeURLResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetWebofficeURLShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.permission), 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.watermark), 'Watermark', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
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
            action='GetWebofficeURL',
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
            imm_20200930_models.GetWebofficeURLResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_weboffice_urlwith_options_async(
        self,
        tmp_req: imm_20200930_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetWebofficeURLResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetWebofficeURLShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.permission), 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.watermark), 'Watermark', 'json')
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
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
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
            action='GetWebofficeURL',
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
            imm_20200930_models.GetWebofficeURLResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_weboffice_url(
        self,
        request: imm_20200930_models.GetWebofficeURLRequest,
    ) -> imm_20200930_models.GetWebofficeURLResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_weboffice_urlwith_options(request, runtime)

    async def get_weboffice_url_async(
        self,
        request: imm_20200930_models.GetWebofficeURLRequest,
    ) -> imm_20200930_models.GetWebofficeURLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_weboffice_urlwith_options_async(request, runtime)

    def index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.file), 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.file), 'File', 'json')
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.file_shrink):
            query['File'] = request.file_shrink
        if not UtilClient.is_unset(request.notify_endpoint):
            query['NotifyEndpoint'] = request.notify_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
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
        runtime = util_models.RuntimeOptions()
        return self.index_file_meta_with_options(request, runtime)

    async def index_file_meta_async(
        self,
        request: imm_20200930_models.IndexFileMetaRequest,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.index_file_meta_with_options_async(request, runtime)

    def list_bindings_with_options(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_bindings_with_options(request, runtime)

    async def list_bindings_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
    ) -> imm_20200930_models.ListBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_bindings_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
    ) -> imm_20200930_models.ListDatasetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
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
        request: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
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
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: imm_20200930_models.ListProjectsRequest,
    ) -> imm_20200930_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        request: imm_20200930_models.ListRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_regions_with_options(request, runtime)

    async def list_regions_async(
        self,
        request: imm_20200930_models.ListRegionsRequest,
    ) -> imm_20200930_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_regions_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: imm_20200930_models.ListTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.end_time_range), 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.start_time_range), 'StartTimeRange', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.end_time_range):
            request.end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.end_time_range), 'EndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.start_time_range):
            request.start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.start_time_range), 'StartTimeRange', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: imm_20200930_models.ListTasksRequest,
    ) -> imm_20200930_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def merge_figure_clusters_with_options(
        self,
        request: imm_20200930_models.MergeFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.MergeFigureClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id_from):
            query['ClusterIdFrom'] = request.cluster_id_from
        if not UtilClient.is_unset(request.cluster_id_to):
            query['ClusterIdTo'] = request.cluster_id_to
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_type):
            query['FigureType'] = request.figure_type
        if not UtilClient.is_unset(request.notify_topic_endpoint):
            query['NotifyTopicEndpoint'] = request.notify_topic_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MergeFigureClusters',
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
            imm_20200930_models.MergeFigureClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def merge_figure_clusters_with_options_async(
        self,
        request: imm_20200930_models.MergeFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.MergeFigureClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id_from):
            query['ClusterIdFrom'] = request.cluster_id_from
        if not UtilClient.is_unset(request.cluster_id_to):
            query['ClusterIdTo'] = request.cluster_id_to
        if not UtilClient.is_unset(request.custom_message):
            query['CustomMessage'] = request.custom_message
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.figure_type):
            query['FigureType'] = request.figure_type
        if not UtilClient.is_unset(request.notify_topic_endpoint):
            query['NotifyTopicEndpoint'] = request.notify_topic_endpoint
        if not UtilClient.is_unset(request.notify_topic_name):
            query['NotifyTopicName'] = request.notify_topic_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MergeFigureClusters',
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
            imm_20200930_models.MergeFigureClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def merge_figure_clusters(
        self,
        request: imm_20200930_models.MergeFigureClustersRequest,
    ) -> imm_20200930_models.MergeFigureClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.merge_figure_clusters_with_options(request, runtime)

    async def merge_figure_clusters_async(
        self,
        request: imm_20200930_models.MergeFigureClustersRequest,
    ) -> imm_20200930_models.MergeFigureClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.merge_figure_clusters_with_options_async(request, runtime)

    def query_figure_clusters_with_options(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
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
        request: imm_20200930_models.QueryFigureClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.query_figure_clusters_with_options(request, runtime)

    async def query_figure_clusters_async(
        self,
        request: imm_20200930_models.QueryFigureClustersRequest,
    ) -> imm_20200930_models.QueryFigureClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_figure_clusters_with_options_async(request, runtime)

    def query_stories_with_options(
        self,
        tmp_req: imm_20200930_models.QueryStoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.QueryStoriesResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_time_range), 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.story_end_time_range), 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.story_start_time_range), 'StoryStartTimeRange', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.QueryStoriesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_time_range):
            request.create_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_time_range), 'CreateTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.figure_cluster_ids):
            request.figure_cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.figure_cluster_ids, 'FigureClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.story_end_time_range):
            request.story_end_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.story_end_time_range), 'StoryEndTimeRange', 'json')
        if not UtilClient.is_unset(tmp_req.story_start_time_range):
            request.story_start_time_range_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.story_start_time_range), 'StoryStartTimeRange', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.query_stories_with_options(request, runtime)

    async def query_stories_async(
        self,
        request: imm_20200930_models.QueryStoriesRequest,
    ) -> imm_20200930_models.QueryStoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_stories_with_options_async(request, runtime)

    def refresh_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.credential_config):
            request.credential_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.credential_config), 'CredentialConfig', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.refresh_weboffice_token_with_options(request, runtime)

    async def refresh_weboffice_token_async(
        self,
        request: imm_20200930_models.RefreshWebofficeTokenRequest,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_weboffice_token_with_options_async(request, runtime)

    def remove_story_files_with_options(
        self,
        tmp_req: imm_20200930_models.RemoveStoryFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.remove_story_files_with_options(request, runtime)

    async def remove_story_files_async(
        self,
        request: imm_20200930_models.RemoveStoryFilesRequest,
    ) -> imm_20200930_models.RemoveStoryFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_story_files_with_options_async(request, runtime)

    def resume_binding_with_options(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBindingResponse:
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
            action='ResumeBinding',
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
            imm_20200930_models.ResumeBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_binding_with_options_async(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBindingResponse:
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
            action='ResumeBinding',
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
            imm_20200930_models.ResumeBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_binding(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
    ) -> imm_20200930_models.ResumeBindingResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_binding_with_options(request, runtime)

    async def resume_binding_async(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
    ) -> imm_20200930_models.ResumeBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_binding_with_options_async(request, runtime)

    def semantic_query_with_options(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
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
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
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
        request: imm_20200930_models.SemanticQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SemanticQueryResponse:
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
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
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
        runtime = util_models.RuntimeOptions()
        return self.semantic_query_with_options(request, runtime)

    async def semantic_query_async(
        self,
        request: imm_20200930_models.SemanticQueryRequest,
    ) -> imm_20200930_models.SemanticQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.semantic_query_with_options_async(request, runtime)

    def simple_query_with_options(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query), 'Query', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query), 'Query', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.simple_query_with_options(request, runtime)

    async def simple_query_async(
        self,
        request: imm_20200930_models.SimpleQueryRequest,
    ) -> imm_20200930_models.SimpleQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.simple_query_with_options_async(request, runtime)

    def stop_binding_with_options(
        self,
        request: imm_20200930_models.StopBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.StopBindingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBinding',
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
            imm_20200930_models.StopBindingResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_binding_with_options_async(
        self,
        request: imm_20200930_models.StopBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.StopBindingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.uri):
            query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBinding',
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
            imm_20200930_models.StopBindingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_binding(
        self,
        request: imm_20200930_models.StopBindingRequest,
    ) -> imm_20200930_models.StopBindingResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_binding_with_options(request, runtime)

    async def stop_binding_async(
        self,
        request: imm_20200930_models.StopBindingRequest,
    ) -> imm_20200930_models.StopBindingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_binding_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: imm_20200930_models.UpdateDatasetRequest,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_figure_cluster_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFigureClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.figure_cluster), 'FigureCluster', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFigureClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.figure_cluster):
            request.figure_cluster_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.figure_cluster), 'FigureCluster', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.update_figure_cluster_with_options(request, runtime)

    async def update_figure_cluster_async(
        self,
        request: imm_20200930_models.UpdateFigureClusterRequest,
    ) -> imm_20200930_models.UpdateFigureClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_figure_cluster_with_options_async(request, runtime)

    def update_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.file), 'File', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.file):
            request.file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.file), 'File', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.update_file_meta_with_options(request, runtime)

    async def update_file_meta_async(
        self,
        request: imm_20200930_models.UpdateFileMetaRequest,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_file_meta_with_options_async(request, runtime)

    def update_project_with_options(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.engine_concurrency):
            query['EngineConcurrency'] = request.engine_concurrency
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_queries_per_second):
            query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
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
        request: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.engine_concurrency):
            query['EngineConcurrency'] = request.engine_concurrency
        if not UtilClient.is_unset(request.project_max_dataset_count):
            query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        if not UtilClient.is_unset(request.project_name):
            query['ProjectName'] = request.project_name
        if not UtilClient.is_unset(request.project_queries_per_second):
            query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        if not UtilClient.is_unset(request.service_role):
            query['ServiceRole'] = request.service_role
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
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    async def update_project_async(
        self,
        request: imm_20200930_models.UpdateProjectRequest,
    ) -> imm_20200930_models.UpdateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_project_with_options_async(request, runtime)

    def update_story_with_options(
        self,
        tmp_req: imm_20200930_models.UpdateStoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateStoryResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cover), 'Cover', 'json')
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
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateStoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cover):
            request.cover_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cover), 'Cover', 'json')
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
        runtime = util_models.RuntimeOptions()
        return self.update_story_with_options(request, runtime)

    async def update_story_async(
        self,
        request: imm_20200930_models.UpdateStoryRequest,
    ) -> imm_20200930_models.UpdateStoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_story_with_options_async(request, runtime)
