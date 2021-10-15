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
        query['DatasetName'] = request.dataset_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchDeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URIs'] = request.uris_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchGetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['Files'] = request.files_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['Files'] = request.files_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchIndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['Files'] = request.files_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['Files'] = request.files_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchUpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['DatasetName'] = request.dataset_name
        query['Description'] = request.description
        query['ProjectName'] = request.project_name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['DatasetName'] = request.dataset_name
        query['Description'] = request.description
        query['ProjectName'] = request.project_name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def create_office_conversion_task_with_options(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndPage'] = request.end_page
        query['FirstPage'] = request.first_page
        query['FitToHeight'] = request.fit_to_height
        query['FitToWidth'] = request.fit_to_width
        query['IsHorizontal'] = request.is_horizontal
        query['LongPic'] = request.long_pic
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['PaperSize'] = request.paper_size
        query['Password'] = request.password
        query['ProjectName'] = request.project_name
        query['Quality'] = request.quality
        query['Scale'] = request.scale
        query['SheetCount'] = request.sheet_count
        query['SheetIndex'] = request.sheet_index
        query['ShowComments'] = request.show_comments
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['StartPage'] = request.start_page
        query['TargetType'] = request.target_type
        query['TargetUri'] = request.target_uri
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_office_conversion_task_with_options_async(
        self,
        request: imm_20200930_models.CreateOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndPage'] = request.end_page
        query['FirstPage'] = request.first_page
        query['FitToHeight'] = request.fit_to_height
        query['FitToWidth'] = request.fit_to_width
        query['IsHorizontal'] = request.is_horizontal
        query['LongPic'] = request.long_pic
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['PaperSize'] = request.paper_size
        query['Password'] = request.password
        query['ProjectName'] = request.project_name
        query['Quality'] = request.quality
        query['Scale'] = request.scale
        query['SheetCount'] = request.sheet_count
        query['SheetIndex'] = request.sheet_index
        query['ShowComments'] = request.show_comments
        query['SourceType'] = request.source_type
        query['SourceUri'] = request.source_uri
        query['StartPage'] = request.start_page
        query['TargetType'] = request.target_type
        query['TargetUri'] = request.target_uri
        query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['Description'] = request.description
        query['EngineConcurrency'] = request.engine_concurrency
        query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        query['ProjectName'] = request.project_name
        query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        query['ServiceRole'] = request.service_role
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['Description'] = request.description
        query['EngineConcurrency'] = request.engine_concurrency
        query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        query['ProjectName'] = request.project_name
        query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        query['ServiceRole'] = request.service_role
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def delete_binding_with_options(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def detect_image_labels_with_options(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['SourceURI'] = request.source_uri
        query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.DetectImageLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_image_labels_with_options_async(
        self,
        request: imm_20200930_models.DetectImageLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DetectImageLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['SourceURI'] = request.source_uri
        query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetectImageLabels',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def fuzzy_query_with_options(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        query['Query'] = request.query
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='FuzzyQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_file_meta_with_options(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_file_signed_uriwith_options(
        self,
        request: imm_20200930_models.GetFileSignedURIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileSignedURIResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetFileSignedURI',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileSignedURIResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_signed_uriwith_options_async(
        self,
        request: imm_20200930_models.GetFileSignedURIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileSignedURIResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetFileSignedURI',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileSignedURIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_signed_uri(
        self,
        request: imm_20200930_models.GetFileSignedURIRequest,
    ) -> imm_20200930_models.GetFileSignedURIResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_signed_uriwith_options(request, runtime)

    async def get_file_signed_uri_async(
        self,
        request: imm_20200930_models.GetFileSignedURIRequest,
    ) -> imm_20200930_models.GetFileSignedURIResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_signed_uriwith_options_async(request, runtime)

    def get_office_conversion_task_with_options(
        self,
        request: imm_20200930_models.GetOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_office_conversion_task_with_options_async(
        self,
        request: imm_20200930_models.GetOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.GetOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_office_conversion_task(
        self,
        request: imm_20200930_models.GetOfficeConversionTaskRequest,
    ) -> imm_20200930_models.GetOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_office_conversion_task_with_options(request, runtime)

    async def get_office_conversion_task_async(
        self,
        request: imm_20200930_models.GetOfficeConversionTaskRequest,
    ) -> imm_20200930_models.GetOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_office_conversion_task_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectName'] = request.project_name
        query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['ProjectName'] = request.project_name
        query['WithStatistics'] = request.with_statistics
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def get_weboffice_urlwith_options(
        self,
        tmp_req: imm_20200930_models.GetWebofficeURLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetWebofficeURLResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.GetWebofficeURLShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_role_chain):
            request.assume_role_chain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.assume_role_chain), 'AssumeRoleChain', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.permission), 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.watermark), 'Watermark', 'json')
        query = {}
        query['AssumeRoleChain'] = request.assume_role_chain_shrink
        query['ExternalUploaded'] = request.external_uploaded
        query['Filename'] = request.filename
        query['Hidecmb'] = request.hidecmb
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['Password'] = request.password
        query['Permission'] = request.permission_shrink
        query['PreviewPages'] = request.preview_pages
        query['ProjectName'] = request.project_name
        query['Referer'] = request.referer
        query['SourceURI'] = request.source_uri
        query['User'] = request.user_shrink
        query['UserData'] = request.user_data
        query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        if not UtilClient.is_unset(tmp_req.assume_role_chain):
            request.assume_role_chain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.assume_role_chain), 'AssumeRoleChain', 'json')
        if not UtilClient.is_unset(tmp_req.permission):
            request.permission_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.permission), 'Permission', 'json')
        if not UtilClient.is_unset(tmp_req.user):
            request.user_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.user), 'User', 'json')
        if not UtilClient.is_unset(tmp_req.watermark):
            request.watermark_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.watermark), 'Watermark', 'json')
        query = {}
        query['AssumeRoleChain'] = request.assume_role_chain_shrink
        query['ExternalUploaded'] = request.external_uploaded
        query['Filename'] = request.filename
        query['Hidecmb'] = request.hidecmb
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['Password'] = request.password
        query['Permission'] = request.permission_shrink
        query['PreviewPages'] = request.preview_pages
        query['ProjectName'] = request.project_name
        query['Referer'] = request.referer
        query['SourceURI'] = request.source_uri
        query['User'] = request.user_shrink
        query['UserData'] = request.user_data
        query['Watermark'] = request.watermark_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetWebofficeURL',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['File'] = request.file_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['File'] = request.file_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='IndexFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBindings',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Prefix'] = request.prefix
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Prefix'] = request.prefix
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def list_office_conversion_task_with_options(
        self,
        request: imm_20200930_models.ListOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListOfficeConversionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_office_conversion_task_with_options_async(
        self,
        request: imm_20200930_models.ListOfficeConversionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListOfficeConversionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListOfficeConversionTask',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            imm_20200930_models.ListOfficeConversionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_office_conversion_task(
        self,
        request: imm_20200930_models.ListOfficeConversionTaskRequest,
    ) -> imm_20200930_models.ListOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_office_conversion_task_with_options(request, runtime)

    async def list_office_conversion_task_async(
        self,
        request: imm_20200930_models.ListOfficeConversionTaskRequest,
    ) -> imm_20200930_models.ListOfficeConversionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_office_conversion_task_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def refresh_weboffice_token_with_options(
        self,
        tmp_req: imm_20200930_models.RefreshWebofficeTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.RefreshWebofficeTokenResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.RefreshWebofficeTokenShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.assume_role_chain):
            request.assume_role_chain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.assume_role_chain), 'AssumeRoleChain', 'json')
        query = {}
        query['AccessToken'] = request.access_token
        query['AssumeRoleChain'] = request.assume_role_chain_shrink
        query['ProjectName'] = request.project_name
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        if not UtilClient.is_unset(tmp_req.assume_role_chain):
            request.assume_role_chain_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.assume_role_chain), 'AssumeRoleChain', 'json')
        query = {}
        query['AccessToken'] = request.access_token
        query['AssumeRoleChain'] = request.assume_role_chain_shrink
        query['ProjectName'] = request.project_name
        query['RefreshToken'] = request.refresh_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshWebofficeToken',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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

    def resume_binding_with_options(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBindingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query = {}
        query['Aggregations'] = request.aggregations_shrink
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Order'] = request.order
        query['ProjectName'] = request.project_name
        query['Query'] = request.query_shrink
        query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query = {}
        query['Aggregations'] = request.aggregations_shrink
        query['DatasetName'] = request.dataset_name
        query['MaxResults'] = request.max_results
        query['NextToken'] = request.next_token
        query['Order'] = request.order
        query['ProjectName'] = request.project_name
        query['Query'] = request.query_shrink
        query['Sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SimpleQuery',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['Reason'] = request.reason
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['ProjectName'] = request.project_name
        query['Reason'] = request.reason
        query['URI'] = request.uri
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopBinding',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['DatasetName'] = request.dataset_name
        query['Description'] = request.description
        query['ProjectName'] = request.project_name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['DatasetName'] = request.dataset_name
        query['Description'] = request.description
        query['ProjectName'] = request.project_name
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['File'] = request.file_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetName'] = request.dataset_name
        query['File'] = request.file_shrink
        query['NotifyEndpoint'] = request.notify_endpoint
        query['NotifyTopicName'] = request.notify_topic_name
        query['ProjectName'] = request.project_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateFileMeta',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['Description'] = request.description
        query['EngineConcurrency'] = request.engine_concurrency
        query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        query['ProjectName'] = request.project_name
        query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        query['ServiceRole'] = request.service_role
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
        query['DatasetMaxBindCount'] = request.dataset_max_bind_count
        query['DatasetMaxEntityCount'] = request.dataset_max_entity_count
        query['DatasetMaxFileCount'] = request.dataset_max_file_count
        query['DatasetMaxRelationCount'] = request.dataset_max_relation_count
        query['DatasetMaxTotalFileSize'] = request.dataset_max_total_file_size
        query['Description'] = request.description
        query['EngineConcurrency'] = request.engine_concurrency
        query['ProjectMaxDatasetCount'] = request.project_max_dataset_count
        query['ProjectName'] = request.project_name
        query['ProjectQueriesPerSecond'] = request.project_queries_per_second
        query['ServiceRole'] = request.service_role
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2020-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
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
