# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iqa20190813 import models as iqa_20190813_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('iqa', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_project_with_options(
        self,
        request: iqa_20190813_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.CreateProjectResponse().from_map(
            self.do_rpcrequest('CreateProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: iqa_20190813_models.CreateProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.CreateProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.CreateProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(
        self,
        request: iqa_20190813_models.CreateProjectRequest,
    ) -> iqa_20190813_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    async def create_project_async(
        self,
        request: iqa_20190813_models.CreateProjectRequest,
    ) -> iqa_20190813_models.CreateProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_with_options_async(request, runtime)

    def delete_project_with_options(
        self,
        request: iqa_20190813_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DeleteProjectResponse().from_map(
            self.do_rpcrequest('DeleteProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        request: iqa_20190813_models.DeleteProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DeleteProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DeleteProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project(
        self,
        request: iqa_20190813_models.DeleteProjectRequest,
    ) -> iqa_20190813_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    async def delete_project_async(
        self,
        request: iqa_20190813_models.DeleteProjectRequest,
    ) -> iqa_20190813_models.DeleteProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_with_options_async(request, runtime)

    def deploy_service_with_options(
        self,
        request: iqa_20190813_models.DeployServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DeployServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DeployServiceResponse().from_map(
            self.do_rpcrequest('DeployService', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_service_with_options_async(
        self,
        request: iqa_20190813_models.DeployServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DeployServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DeployServiceResponse().from_map(
            await self.do_rpcrequest_async('DeployService', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_service(
        self,
        request: iqa_20190813_models.DeployServiceRequest,
    ) -> iqa_20190813_models.DeployServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_service_with_options(request, runtime)

    async def deploy_service_async(
        self,
        request: iqa_20190813_models.DeployServiceRequest,
    ) -> iqa_20190813_models.DeployServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_service_with_options_async(request, runtime)

    def describe_project_with_options(
        self,
        request: iqa_20190813_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DescribeProjectResponse().from_map(
            self.do_rpcrequest('DescribeProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_project_with_options_async(
        self,
        request: iqa_20190813_models.DescribeProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.DescribeProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.DescribeProjectResponse().from_map(
            await self.do_rpcrequest_async('DescribeProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project(
        self,
        request: iqa_20190813_models.DescribeProjectRequest,
    ) -> iqa_20190813_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_with_options(request, runtime)

    async def describe_project_async(
        self,
        request: iqa_20190813_models.DescribeProjectRequest,
    ) -> iqa_20190813_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_with_options_async(request, runtime)

    def get_predict_result_with_options(
        self,
        request: iqa_20190813_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.GetPredictResultResponse().from_map(
            self.do_rpcrequest('GetPredictResult', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_predict_result_with_options_async(
        self,
        request: iqa_20190813_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.GetPredictResultResponse().from_map(
            await self.do_rpcrequest_async('GetPredictResult', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_predict_result(
        self,
        request: iqa_20190813_models.GetPredictResultRequest,
    ) -> iqa_20190813_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_predict_result_with_options(request, runtime)

    async def get_predict_result_async(
        self,
        request: iqa_20190813_models.GetPredictResultRequest,
    ) -> iqa_20190813_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_predict_result_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: iqa_20190813_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.ListProjectsResponse().from_map(
            self.do_rpcrequest('ListProjects', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: iqa_20190813_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.ListProjectsResponse().from_map(
            await self.do_rpcrequest_async('ListProjects', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(
        self,
        request: iqa_20190813_models.ListProjectsRequest,
    ) -> iqa_20190813_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: iqa_20190813_models.ListProjectsRequest,
    ) -> iqa_20190813_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def modifiy_project_with_options(
        self,
        request: iqa_20190813_models.ModifiyProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.ModifiyProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.ModifiyProjectResponse().from_map(
            self.do_rpcrequest('ModifiyProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modifiy_project_with_options_async(
        self,
        request: iqa_20190813_models.ModifiyProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.ModifiyProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.ModifiyProjectResponse().from_map(
            await self.do_rpcrequest_async('ModifiyProject', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modifiy_project(
        self,
        request: iqa_20190813_models.ModifiyProjectRequest,
    ) -> iqa_20190813_models.ModifiyProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modifiy_project_with_options(request, runtime)

    async def modifiy_project_async(
        self,
        request: iqa_20190813_models.ModifiyProjectRequest,
    ) -> iqa_20190813_models.ModifiyProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modifiy_project_with_options_async(request, runtime)

    def upload_dictionary_with_options(
        self,
        request: iqa_20190813_models.UploadDictionaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.UploadDictionaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.UploadDictionaryResponse().from_map(
            self.do_rpcrequest('UploadDictionary', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_dictionary_with_options_async(
        self,
        request: iqa_20190813_models.UploadDictionaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.UploadDictionaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.UploadDictionaryResponse().from_map(
            await self.do_rpcrequest_async('UploadDictionary', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_dictionary(
        self,
        request: iqa_20190813_models.UploadDictionaryRequest,
    ) -> iqa_20190813_models.UploadDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_dictionary_with_options(request, runtime)

    async def upload_dictionary_async(
        self,
        request: iqa_20190813_models.UploadDictionaryRequest,
    ) -> iqa_20190813_models.UploadDictionaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_dictionary_with_options_async(request, runtime)

    def upload_document_with_options(
        self,
        request: iqa_20190813_models.UploadDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.UploadDocumentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.UploadDocumentResponse().from_map(
            self.do_rpcrequest('UploadDocument', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_document_with_options_async(
        self,
        request: iqa_20190813_models.UploadDocumentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> iqa_20190813_models.UploadDocumentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return iqa_20190813_models.UploadDocumentResponse().from_map(
            await self.do_rpcrequest_async('UploadDocument', '2019-08-13', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_document(
        self,
        request: iqa_20190813_models.UploadDocumentRequest,
    ) -> iqa_20190813_models.UploadDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_document_with_options(request, runtime)

    async def upload_document_async(
        self,
        request: iqa_20190813_models.UploadDocumentRequest,
    ) -> iqa_20190813_models.UploadDocumentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_document_with_options_async(request, runtime)
