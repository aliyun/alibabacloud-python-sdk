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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            self.do_rpcrequest('BatchDeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchDeleteFileMetaResponse(),
            await self.do_rpcrequest_async('BatchDeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            self.do_rpcrequest('BatchGetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchGetFileMetaResponse(),
            await self.do_rpcrequest_async('BatchGetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            self.do_rpcrequest('BatchIndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchIndexFileMetaResponse(),
            await self.do_rpcrequest_async('BatchIndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            self.do_rpcrequest('BatchUpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.BatchUpdateFileMetaResponse(),
            await self.do_rpcrequest_async('BatchUpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            self.do_rpcrequest('CreateBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_binding_with_options_async(
        self,
        request: imm_20200930_models.CreateBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateBindingResponse(),
            await self.do_rpcrequest_async('CreateBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            self.do_rpcrequest('CreateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: imm_20200930_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateDatasetResponse(),
            await self.do_rpcrequest_async('CreateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_project_with_options(
        self,
        request: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: imm_20200930_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.CreateProjectResponse(),
            await self.do_rpcrequest_async('CreateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            self.do_rpcrequest('DeleteBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_binding_with_options_async(
        self,
        request: imm_20200930_models.DeleteBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteBindingResponse(),
            await self.do_rpcrequest_async('DeleteBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            self.do_rpcrequest('DeleteDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: imm_20200930_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteDatasetResponse(),
            await self.do_rpcrequest_async('DeleteDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            self.do_rpcrequest('DeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_meta_with_options_async(
        self,
        request: imm_20200930_models.DeleteFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteFileMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteFileMetaResponse(),
            await self.do_rpcrequest_async('DeleteFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            self.do_rpcrequest('DeleteProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: imm_20200930_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.DeleteProjectResponse(),
            await self.do_rpcrequest_async('DeleteProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def fuzzy_query_with_options(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            self.do_rpcrequest('FuzzyQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def fuzzy_query_with_options_async(
        self,
        request: imm_20200930_models.FuzzyQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.FuzzyQueryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.FuzzyQueryResponse(),
            await self.do_rpcrequest_async('FuzzyQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            self.do_rpcrequest('GetBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_binding_with_options_async(
        self,
        request: imm_20200930_models.GetBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetBindingResponse(),
            await self.do_rpcrequest_async('GetBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            self.do_rpcrequest('GetDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: imm_20200930_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetDatasetResponse(),
            await self.do_rpcrequest_async('GetDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            self.do_rpcrequest('GetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_file_meta_with_options_async(
        self,
        request: imm_20200930_models.GetFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileMetaResponse(),
            await self.do_rpcrequest_async('GetFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileSignedURIResponse(),
            self.do_rpcrequest('GetFileSignedURI', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_file_signed_uriwith_options_async(
        self,
        request: imm_20200930_models.GetFileSignedURIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetFileSignedURIResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetFileSignedURIResponse(),
            await self.do_rpcrequest_async('GetFileSignedURI', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_project_with_options(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: imm_20200930_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.GetProjectResponse(),
            await self.do_rpcrequest_async('GetProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def index_file_meta_with_options(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            self.do_rpcrequest('IndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def index_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.IndexFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.IndexFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.IndexFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.IndexFileMetaResponse(),
            await self.do_rpcrequest_async('IndexFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            self.do_rpcrequest('ListBindings', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_bindings_with_options_async(
        self,
        request: imm_20200930_models.ListBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListBindingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListBindingsResponse(),
            await self.do_rpcrequest_async('ListBindings', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            self.do_rpcrequest('ListDatasets', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: imm_20200930_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListDatasetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListDatasetsResponse(),
            await self.do_rpcrequest_async('ListDatasets', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: imm_20200930_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ListProjectsResponse(),
            await self.do_rpcrequest_async('ListProjects', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def resume_binding_with_options(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBindingResponse(),
            self.do_rpcrequest('ResumeBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_binding_with_options_async(
        self,
        request: imm_20200930_models.ResumeBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.ResumeBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.ResumeBindingResponse(),
            await self.do_rpcrequest_async('ResumeBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query), 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            self.do_rpcrequest('SimpleQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def simple_query_with_options_async(
        self,
        tmp_req: imm_20200930_models.SimpleQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.SimpleQueryResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.SimpleQueryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.query), 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.aggregations):
            request.aggregations_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aggregations, 'Aggregations', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.SimpleQueryResponse(),
            await self.do_rpcrequest_async('SimpleQuery', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.StopBindingResponse(),
            self.do_rpcrequest('StopBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_binding_with_options_async(
        self,
        request: imm_20200930_models.StopBindingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.StopBindingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.StopBindingResponse(),
            await self.do_rpcrequest_async('StopBinding', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        tmp_req: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            self.do_rpcrequest('UpdateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateDatasetResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateDatasetShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateDatasetResponse(),
            await self.do_rpcrequest_async('UpdateDataset', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            self.do_rpcrequest('UpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_file_meta_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateFileMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateFileMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateFileMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.custom_labels):
            request.custom_labels_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_labels, 'CustomLabels', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateFileMetaResponse(),
            await self.do_rpcrequest_async('UpdateFileMeta', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_project_with_options_async(
        self,
        tmp_req: imm_20200930_models.UpdateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> imm_20200930_models.UpdateProjectResponse:
        UtilClient.validate_model(tmp_req)
        request = imm_20200930_models.UpdateProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.reset_items):
            request.reset_items_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.reset_items, 'ResetItems', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            imm_20200930_models.UpdateProjectResponse(),
            await self.do_rpcrequest_async('UpdateProject', '2020-09-30', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
