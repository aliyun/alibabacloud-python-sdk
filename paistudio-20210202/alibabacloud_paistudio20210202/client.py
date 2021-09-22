# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_paistudio20210202 import models as pai_studio_20210202_models
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
            'cn-beijing': 'pai.cn-beijing.aliyuncs.com',
            'cn-hangzhou': 'pai.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'pai.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'pai.cn-shenzhen.aliyuncs.com',
            'cn-hongkong': 'pai.cn-hongkong.aliyuncs.com',
            'ap-southeast-1': 'pai.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'pai.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'pai.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'pai.ap-southeast-5.aliyuncs.com',
            'us-west-1': 'pai.us-west-1.aliyuncs.com',
            'us-east-1': 'pai.us-east-1.aliyuncs.com',
            'eu-central-1': 'pai.eu-central-1.aliyuncs.com',
            'me-east-1': 'pai.me-east-1.aliyuncs.com',
            'ap-south-1': 'pai.ap-south-1.aliyuncs.com',
            'cn-qingdao': 'pai.cn-qingdao.aliyuncs.com',
            'cn-zhangjiakou': 'pai.cn-zhangjiakou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('paistudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_image(
        self,
        request: pai_studio_20210202_models.AddImageRequest,
    ) -> pai_studio_20210202_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_with_options(request, headers, runtime)

    async def add_image_async(
        self,
        request: pai_studio_20210202_models.AddImageRequest,
    ) -> pai_studio_20210202_models.AddImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_with_options_async(request, headers, runtime)

    def add_image_with_options(
        self,
        request: pai_studio_20210202_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageResponse(),
            self.do_roarequest('AddImage', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    async def add_image_with_options_async(
        self,
        request: pai_studio_20210202_models.AddImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.AddImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.image_uri):
            body['ImageUri'] = request.image_uri
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageResponse(),
            await self.do_roarequest_async('AddImage', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    def add_image_labels(
        self,
        image_id: str,
        request: pai_studio_20210202_models.AddImageLabelsRequest,
    ) -> pai_studio_20210202_models.AddImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_image_labels_with_options(image_id, request, headers, runtime)

    async def add_image_labels_async(
        self,
        image_id: str,
        request: pai_studio_20210202_models.AddImageLabelsRequest,
    ) -> pai_studio_20210202_models.AddImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_image_labels_with_options_async(image_id, request, headers, runtime)

    def add_image_labels_with_options(
        self,
        image_id: str,
        request: pai_studio_20210202_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.AddImageLabelsResponse:
        UtilClient.validate_model(request)
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageLabelsResponse(),
            self.do_roarequest('AddImageLabels', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/images/{image_id}/labels', 'json', req, runtime)
        )

    async def add_image_labels_with_options_async(
        self,
        image_id: str,
        request: pai_studio_20210202_models.AddImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.AddImageLabelsResponse:
        UtilClient.validate_model(request)
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        body = {}
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.AddImageLabelsResponse(),
            await self.do_roarequest_async('AddImageLabels', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/images/{image_id}/labels', 'json', req, runtime)
        )

    def copy_experiment(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.CopyExperimentRequest,
    ) -> pai_studio_20210202_models.CopyExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.copy_experiment_with_options(experiment_id, request, headers, runtime)

    async def copy_experiment_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.CopyExperimentRequest,
    ) -> pai_studio_20210202_models.CopyExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.copy_experiment_with_options_async(experiment_id, request, headers, runtime)

    def copy_experiment_with_options(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.CopyExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CopyExperimentResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CopyExperimentResponse(),
            self.do_roarequest('CopyExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments/[ExperimentId]/copy', 'json', req, runtime)
        )

    async def copy_experiment_with_options_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.CopyExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CopyExperimentResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CopyExperimentResponse(),
            await self.do_roarequest_async('CopyExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments/[ExperimentId]/copy', 'json', req, runtime)
        )

    def create_experiment(
        self,
        request: pai_studio_20210202_models.CreateExperimentRequest,
    ) -> pai_studio_20210202_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_with_options(request, headers, runtime)

    async def create_experiment_async(
        self,
        request: pai_studio_20210202_models.CreateExperimentRequest,
    ) -> pai_studio_20210202_models.CreateExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_with_options_async(request, headers, runtime)

    def create_experiment_with_options(
        self,
        request: pai_studio_20210202_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentResponse(),
            self.do_roarequest('CreateExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments', 'json', req, runtime)
        )

    async def create_experiment_with_options_async(
        self,
        request: pai_studio_20210202_models.CreateExperimentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateExperimentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentResponse(),
            await self.do_roarequest_async('CreateExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments', 'json', req, runtime)
        )

    def create_experiment_folder(
        self,
        request: pai_studio_20210202_models.CreateExperimentFolderRequest,
    ) -> pai_studio_20210202_models.CreateExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_experiment_folder_with_options(request, headers, runtime)

    async def create_experiment_folder_async(
        self,
        request: pai_studio_20210202_models.CreateExperimentFolderRequest,
    ) -> pai_studio_20210202_models.CreateExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_experiment_folder_with_options_async(request, headers, runtime)

    def create_experiment_folder_with_options(
        self,
        request: pai_studio_20210202_models.CreateExperimentFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateExperimentFolderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentFolderResponse(),
            self.do_roarequest('CreateExperimentFolder', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experimentfolders', 'json', req, runtime)
        )

    async def create_experiment_folder_with_options_async(
        self,
        request: pai_studio_20210202_models.CreateExperimentFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateExperimentFolderResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateExperimentFolderResponse(),
            await self.do_roarequest_async('CreateExperimentFolder', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experimentfolders', 'json', req, runtime)
        )

    def create_job(
        self,
        request: pai_studio_20210202_models.CreateJobRequest,
    ) -> pai_studio_20210202_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(request, headers, runtime)

    async def create_job_async(
        self,
        request: pai_studio_20210202_models.CreateJobRequest,
    ) -> pai_studio_20210202_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        request: pai_studio_20210202_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.execute_type):
            body['ExecuteType'] = request.execute_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateJobResponse(),
            self.do_roarequest('CreateJob', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: pai_studio_20210202_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateJobResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.experiment_id):
            body['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.execute_type):
            body['ExecuteType'] = request.execute_type
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateJobResponse(),
            await self.do_roarequest_async('CreateJob', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    def create_service(
        self,
        request: pai_studio_20210202_models.CreateServiceRequest,
    ) -> pai_studio_20210202_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: pai_studio_20210202_models.CreateServiceRequest,
    ) -> pai_studio_20210202_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: pai_studio_20210202_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateServiceResponse(),
            self.do_roarequest('CreateService', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/services', 'json', req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: pai_studio_20210202_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.CreateServiceResponse(),
            await self.do_roarequest_async('CreateService', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/services', 'json', req, runtime)
        )

    def delete_experiment(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_with_options(experiment_id, headers, runtime)

    async def delete_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.DeleteExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_with_options_async(experiment_id, headers, runtime)

    def delete_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentResponse(),
            self.do_roarequest('DeleteExperiment', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/experiments/{experiment_id}', 'json', req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentResponse(),
            await self.do_roarequest_async('DeleteExperiment', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/experiments/{experiment_id}', 'json', req, runtime)
        )

    def delete_experiment_folder(
        self,
        folder_id: str,
    ) -> pai_studio_20210202_models.DeleteExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_experiment_folder_with_options(folder_id, headers, runtime)

    async def delete_experiment_folder_async(
        self,
        folder_id: str,
    ) -> pai_studio_20210202_models.DeleteExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_experiment_folder_with_options_async(folder_id, headers, runtime)

    def delete_experiment_folder_with_options(
        self,
        folder_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteExperimentFolderResponse:
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentFolderResponse(),
            self.do_roarequest('DeleteExperimentFolder', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/experimentfolders/{folder_id}', 'json', req, runtime)
        )

    async def delete_experiment_folder_with_options_async(
        self,
        folder_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteExperimentFolderResponse:
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteExperimentFolderResponse(),
            await self.do_roarequest_async('DeleteExperimentFolder', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/experimentfolders/{folder_id}', 'json', req, runtime)
        )

    def delete_service(
        self,
        service_id: str,
    ) -> pai_studio_20210202_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(service_id, headers, runtime)

    async def delete_service_async(
        self,
        service_id: str,
    ) -> pai_studio_20210202_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(service_id, headers, runtime)

    def delete_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteServiceResponse:
        service_id = OpenApiUtilClient.get_encode_param(service_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteServiceResponse(),
            self.do_roarequest('DeleteService', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/services/{service_id}', 'json', req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.DeleteServiceResponse:
        service_id = OpenApiUtilClient.get_encode_param(service_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.DeleteServiceResponse(),
            await self.do_roarequest_async('DeleteService', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/services/{service_id}', 'json', req, runtime)
        )

    def get_algorithm_def(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmDefResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_def_with_options(request, headers, runtime)

    async def get_algorithm_def_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmDefResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_def_with_options_async(request, headers, runtime)

    def get_algorithm_def_with_options(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmDefResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.algo_version):
            query['AlgoVersion'] = request.algo_version
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefResponse(),
            self.do_roarequest('GetAlgorithmDef', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/def', 'json', req, runtime)
        )

    async def get_algorithm_def_with_options_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmDefResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.algo_version):
            query['AlgoVersion'] = request.algo_version
        if not UtilClient.is_unset(request.signature):
            query['Signature'] = request.signature
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefResponse(),
            await self.do_roarequest_async('GetAlgorithmDef', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/def', 'json', req, runtime)
        )

    def get_algorithm_defs(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefsRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmDefsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_defs_with_options(request, headers, runtime)

    async def get_algorithm_defs_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefsRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmDefsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_defs_with_options_async(request, headers, runtime)

    def get_algorithm_defs_with_options(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmDefsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.latest_timestamp):
            query['LatestTimestamp'] = request.latest_timestamp
        if not UtilClient.is_unset(request.range_start):
            query['RangeStart'] = request.range_start
        if not UtilClient.is_unset(request.range_end):
            query['RangeEnd'] = request.range_end
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefsResponse(),
            self.do_roarequest('GetAlgorithmDefs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/defs', 'json', req, runtime)
        )

    async def get_algorithm_defs_with_options_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmDefsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmDefsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.timestamp):
            query['Timestamp'] = request.timestamp
        if not UtilClient.is_unset(request.latest_timestamp):
            query['LatestTimestamp'] = request.latest_timestamp
        if not UtilClient.is_unset(request.range_start):
            query['RangeStart'] = request.range_start
        if not UtilClient.is_unset(request.range_end):
            query['RangeEnd'] = request.range_end
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmDefsResponse(),
            await self.do_roarequest_async('GetAlgorithmDefs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/defs', 'json', req, runtime)
        )

    def get_algorithm_tree(
        self,
        request: pai_studio_20210202_models.GetAlgorithmTreeRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algorithm_tree_with_options(request, headers, runtime)

    async def get_algorithm_tree_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmTreeRequest,
    ) -> pai_studio_20210202_models.GetAlgorithmTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algorithm_tree_with_options_async(request, headers, runtime)

    def get_algorithm_tree_with_options(
        self,
        request: pai_studio_20210202_models.GetAlgorithmTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmTreeResponse(),
            self.do_roarequest('GetAlgorithmTree', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/tree', 'json', req, runtime)
        )

    async def get_algorithm_tree_with_options_async(
        self,
        request: pai_studio_20210202_models.GetAlgorithmTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgorithmTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgorithmTreeResponse(),
            await self.do_roarequest_async('GetAlgorithmTree', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algorithm/tree', 'json', req, runtime)
        )

    def get_algo_tree(
        self,
        request: pai_studio_20210202_models.GetAlgoTreeRequest,
    ) -> pai_studio_20210202_models.GetAlgoTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_algo_tree_with_options(request, headers, runtime)

    async def get_algo_tree_async(
        self,
        request: pai_studio_20210202_models.GetAlgoTreeRequest,
    ) -> pai_studio_20210202_models.GetAlgoTreeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_algo_tree_with_options_async(request, headers, runtime)

    def get_algo_tree_with_options(
        self,
        request: pai_studio_20210202_models.GetAlgoTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgoTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgoTreeResponse(),
            self.do_roarequest('GetAlgoTree', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algo/tree', 'json', req, runtime)
        )

    async def get_algo_tree_with_options_async(
        self,
        request: pai_studio_20210202_models.GetAlgoTreeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetAlgoTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetAlgoTreeResponse(),
            await self.do_roarequest_async('GetAlgoTree', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/algo/tree', 'json', req, runtime)
        )

    def get_experiment(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_with_options(experiment_id, headers, runtime)

    async def get_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_with_options_async(experiment_id, headers, runtime)

    def get_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentResponse(),
            self.do_roarequest('GetExperiment', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}', 'json', req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentResponse(),
            await self.do_roarequest_async('GetExperiment', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}', 'json', req, runtime)
        )

    def get_experiment_folder_children(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.GetExperimentFolderChildrenRequest,
    ) -> pai_studio_20210202_models.GetExperimentFolderChildrenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_folder_children_with_options(folder_id, request, headers, runtime)

    async def get_experiment_folder_children_async(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.GetExperimentFolderChildrenRequest,
    ) -> pai_studio_20210202_models.GetExperimentFolderChildrenResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_folder_children_with_options_async(folder_id, request, headers, runtime)

    def get_experiment_folder_children_with_options(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.GetExperimentFolderChildrenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentFolderChildrenResponse:
        UtilClient.validate_model(request)
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.only_folder):
            query['OnlyFolder'] = request.only_folder
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentFolderChildrenResponse(),
            self.do_roarequest('GetExperimentFolderChildren', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experimentfolders/{folder_id}/children', 'json', req, runtime)
        )

    async def get_experiment_folder_children_with_options_async(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.GetExperimentFolderChildrenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentFolderChildrenResponse:
        UtilClient.validate_model(request)
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.only_folder):
            query['OnlyFolder'] = request.only_folder
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentFolderChildrenResponse(),
            await self.do_roarequest_async('GetExperimentFolderChildren', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experimentfolders/{folder_id}/children', 'json', req, runtime)
        )

    def get_experiment_meta(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_meta_with_options(experiment_id, headers, runtime)

    async def get_experiment_meta_async(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_meta_with_options_async(experiment_id, headers, runtime)

    def get_experiment_meta_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentMetaResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentMetaResponse(),
            self.do_roarequest('GetExperimentMeta', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/meta', 'json', req, runtime)
        )

    async def get_experiment_meta_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentMetaResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentMetaResponse(),
            await self.do_roarequest_async('GetExperimentMeta', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/meta', 'json', req, runtime)
        )

    def get_experiments_statistics(
        self,
        request: pai_studio_20210202_models.GetExperimentsStatisticsRequest,
    ) -> pai_studio_20210202_models.GetExperimentsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiments_statistics_with_options(request, headers, runtime)

    async def get_experiments_statistics_async(
        self,
        request: pai_studio_20210202_models.GetExperimentsStatisticsRequest,
    ) -> pai_studio_20210202_models.GetExperimentsStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiments_statistics_with_options_async(request, headers, runtime)

    def get_experiments_statistics_with_options(
        self,
        request: pai_studio_20210202_models.GetExperimentsStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentsStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentsStatisticsResponse(),
            self.do_roarequest('GetExperimentsStatistics', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/experiments', 'json', req, runtime)
        )

    async def get_experiments_statistics_with_options_async(
        self,
        request: pai_studio_20210202_models.GetExperimentsStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentsStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_ids):
            query['WorkspaceIds'] = request.workspace_ids
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentsStatisticsResponse(),
            await self.do_roarequest_async('GetExperimentsStatistics', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/statistics/experiments', 'json', req, runtime)
        )

    def get_experiment_status(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_experiment_status_with_options(experiment_id, headers, runtime)

    async def get_experiment_status_async(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.GetExperimentStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_experiment_status_with_options_async(experiment_id, headers, runtime)

    def get_experiment_status_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentStatusResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentStatusResponse(),
            self.do_roarequest('GetExperimentStatus', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/status', 'json', req, runtime)
        )

    async def get_experiment_status_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetExperimentStatusResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetExperimentStatusResponse(),
            await self.do_roarequest_async('GetExperimentStatus', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/status', 'json', req, runtime)
        )

    def get_image(
        self,
        image_id: str,
        request: pai_studio_20210202_models.GetImageRequest,
    ) -> pai_studio_20210202_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_image_with_options(image_id, request, headers, runtime)

    async def get_image_async(
        self,
        image_id: str,
        request: pai_studio_20210202_models.GetImageRequest,
    ) -> pai_studio_20210202_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_image_with_options_async(image_id, request, headers, runtime)

    def get_image_with_options(
        self,
        image_id: str,
        request: pai_studio_20210202_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetImageResponse:
        UtilClient.validate_model(request)
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetImageResponse(),
            self.do_roarequest('GetImage', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/images/{image_id}', 'json', req, runtime)
        )

    async def get_image_with_options_async(
        self,
        image_id: str,
        request: pai_studio_20210202_models.GetImageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetImageResponse:
        UtilClient.validate_model(request)
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetImageResponse(),
            await self.do_roarequest_async('GetImage', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/images/{image_id}', 'json', req, runtime)
        )

    def get_job(
        self,
        job_id: str,
        request: pai_studio_20210202_models.GetJobRequest,
    ) -> pai_studio_20210202_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(job_id, request, headers, runtime)

    async def get_job_async(
        self,
        job_id: str,
        request: pai_studio_20210202_models.GetJobRequest,
    ) -> pai_studio_20210202_models.GetJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(job_id, request, headers, runtime)

    def get_job_with_options(
        self,
        job_id: str,
        request: pai_studio_20210202_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetJobResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetJobResponse(),
            self.do_roarequest('GetJob', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}', 'json', req, runtime)
        )

    async def get_job_with_options_async(
        self,
        job_id: str,
        request: pai_studio_20210202_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetJobResponse:
        UtilClient.validate_model(request)
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        query = {}
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetJobResponse(),
            await self.do_roarequest_async('GetJob', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs/{job_id}', 'json', req, runtime)
        )

    def get_mctable_schema(
        self,
        table_name: str,
        request: pai_studio_20210202_models.GetMCTableSchemaRequest,
    ) -> pai_studio_20210202_models.GetMCTableSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_mctable_schema_with_options(table_name, request, headers, runtime)

    async def get_mctable_schema_async(
        self,
        table_name: str,
        request: pai_studio_20210202_models.GetMCTableSchemaRequest,
    ) -> pai_studio_20210202_models.GetMCTableSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_mctable_schema_with_options_async(table_name, request, headers, runtime)

    def get_mctable_schema_with_options(
        self,
        table_name: str,
        request: pai_studio_20210202_models.GetMCTableSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetMCTableSchemaResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetMCTableSchemaResponse(),
            self.do_roarequest('GetMCTableSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables/{table_name}/schema', 'json', req, runtime)
        )

    async def get_mctable_schema_with_options_async(
        self,
        table_name: str,
        request: pai_studio_20210202_models.GetMCTableSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetMCTableSchemaResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetMCTableSchemaResponse(),
            await self.do_roarequest_async('GetMCTableSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables/{table_name}/schema', 'json', req, runtime)
        )

    def get_node_input_schema(
        self,
        experiment_id: str,
        node_id: str,
        request: pai_studio_20210202_models.GetNodeInputSchemaRequest,
    ) -> pai_studio_20210202_models.GetNodeInputSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_input_schema_with_options(experiment_id, node_id, request, headers, runtime)

    async def get_node_input_schema_async(
        self,
        experiment_id: str,
        node_id: str,
        request: pai_studio_20210202_models.GetNodeInputSchemaRequest,
    ) -> pai_studio_20210202_models.GetNodeInputSchemaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_input_schema_with_options_async(experiment_id, node_id, request, headers, runtime)

    def get_node_input_schema_with_options(
        self,
        experiment_id: str,
        node_id: str,
        request: pai_studio_20210202_models.GetNodeInputSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeInputSchemaResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.input_id):
            query['InputId'] = request.input_id
        if not UtilClient.is_unset(request.input_index):
            query['InputIndex'] = request.input_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeInputSchemaResponse(),
            self.do_roarequest('GetNodeInputSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/schema', 'json', req, runtime)
        )

    async def get_node_input_schema_with_options_async(
        self,
        experiment_id: str,
        node_id: str,
        request: pai_studio_20210202_models.GetNodeInputSchemaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeInputSchemaResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        query = {}
        if not UtilClient.is_unset(request.input_id):
            query['InputId'] = request.input_id
        if not UtilClient.is_unset(request.input_index):
            query['InputIndex'] = request.input_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeInputSchemaResponse(),
            await self.do_roarequest_async('GetNodeInputSchema', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/schema', 'json', req, runtime)
        )

    def get_node_output(
        self,
        experiment_id: str,
        node_id: str,
        output_id: str,
        request: pai_studio_20210202_models.GetNodeOutputRequest,
    ) -> pai_studio_20210202_models.GetNodeOutputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_output_with_options(experiment_id, node_id, output_id, request, headers, runtime)

    async def get_node_output_async(
        self,
        experiment_id: str,
        node_id: str,
        output_id: str,
        request: pai_studio_20210202_models.GetNodeOutputRequest,
    ) -> pai_studio_20210202_models.GetNodeOutputResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_output_with_options_async(experiment_id, node_id, output_id, request, headers, runtime)

    def get_node_output_with_options(
        self,
        experiment_id: str,
        node_id: str,
        output_id: str,
        request: pai_studio_20210202_models.GetNodeOutputRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeOutputResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        output_id = OpenApiUtilClient.get_encode_param(output_id)
        query = {}
        if not UtilClient.is_unset(request.output_index):
            query['OutputIndex'] = request.output_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeOutputResponse(),
            self.do_roarequest('GetNodeOutput', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/outputs/{output_id}', 'json', req, runtime)
        )

    async def get_node_output_with_options_async(
        self,
        experiment_id: str,
        node_id: str,
        output_id: str,
        request: pai_studio_20210202_models.GetNodeOutputRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeOutputResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        output_id = OpenApiUtilClient.get_encode_param(output_id)
        query = {}
        if not UtilClient.is_unset(request.output_index):
            query['OutputIndex'] = request.output_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeOutputResponse(),
            await self.do_roarequest_async('GetNodeOutput', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/outputs/{output_id}', 'json', req, runtime)
        )

    def get_node_visualization(
        self,
        experiment_id: str,
        node_id: str,
        visualization_id: str,
        request: pai_studio_20210202_models.GetNodeVisualizationRequest,
    ) -> pai_studio_20210202_models.GetNodeVisualizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_node_visualization_with_options(experiment_id, node_id, visualization_id, request, headers, runtime)

    async def get_node_visualization_async(
        self,
        experiment_id: str,
        node_id: str,
        visualization_id: str,
        request: pai_studio_20210202_models.GetNodeVisualizationRequest,
    ) -> pai_studio_20210202_models.GetNodeVisualizationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_node_visualization_with_options_async(experiment_id, node_id, visualization_id, request, headers, runtime)

    def get_node_visualization_with_options(
        self,
        experiment_id: str,
        node_id: str,
        visualization_id: str,
        request: pai_studio_20210202_models.GetNodeVisualizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeVisualizationResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        visualization_id = OpenApiUtilClient.get_encode_param(visualization_id)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeVisualizationResponse(),
            self.do_roarequest('GetNodeVisualization', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/visualizations/{visualization_id}', 'json', req, runtime)
        )

    async def get_node_visualization_with_options_async(
        self,
        experiment_id: str,
        node_id: str,
        visualization_id: str,
        request: pai_studio_20210202_models.GetNodeVisualizationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetNodeVisualizationResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        visualization_id = OpenApiUtilClient.get_encode_param(visualization_id)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetNodeVisualizationResponse(),
            await self.do_roarequest_async('GetNodeVisualization', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/visualizations/{visualization_id}', 'json', req, runtime)
        )

    def get_service(
        self,
        service_id: str,
        request: pai_studio_20210202_models.GetServiceRequest,
    ) -> pai_studio_20210202_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(service_id, request, headers, runtime)

    async def get_service_async(
        self,
        service_id: str,
        request: pai_studio_20210202_models.GetServiceRequest,
    ) -> pai_studio_20210202_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(service_id, request, headers, runtime)

    def get_service_with_options(
        self,
        service_id: str,
        request: pai_studio_20210202_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetServiceResponse:
        UtilClient.validate_model(request)
        service_id = OpenApiUtilClient.get_encode_param(service_id)
        query = {}
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetServiceResponse(),
            self.do_roarequest('GetService', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/services/{service_id}', 'json', req, runtime)
        )

    async def get_service_with_options_async(
        self,
        service_id: str,
        request: pai_studio_20210202_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetServiceResponse:
        UtilClient.validate_model(request)
        service_id = OpenApiUtilClient.get_encode_param(service_id)
        query = {}
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetServiceResponse(),
            await self.do_roarequest_async('GetService', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/services/{service_id}', 'json', req, runtime)
        )

    def get_template(
        self,
        template_id: str,
    ) -> pai_studio_20210202_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_template_with_options(template_id, headers, runtime)

    async def get_template_async(
        self,
        template_id: str,
    ) -> pai_studio_20210202_models.GetTemplateResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_template_with_options_async(template_id, headers, runtime)

    def get_template_with_options(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetTemplateResponse:
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetTemplateResponse(),
            self.do_roarequest('GetTemplate', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/templates/{template_id}', 'json', req, runtime)
        )

    async def get_template_with_options_async(
        self,
        template_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.GetTemplateResponse:
        template_id = OpenApiUtilClient.get_encode_param(template_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.GetTemplateResponse(),
            await self.do_roarequest_async('GetTemplate', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/templates/{template_id}', 'json', req, runtime)
        )

    def list_algo_defs(
        self,
        request: pai_studio_20210202_models.ListAlgoDefsRequest,
    ) -> pai_studio_20210202_models.ListAlgoDefsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_algo_defs_with_options(request, headers, runtime)

    async def list_algo_defs_async(
        self,
        request: pai_studio_20210202_models.ListAlgoDefsRequest,
    ) -> pai_studio_20210202_models.ListAlgoDefsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_algo_defs_with_options_async(request, headers, runtime)

    def list_algo_defs_with_options(
        self,
        request: pai_studio_20210202_models.ListAlgoDefsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListAlgoDefsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAlgoDefsResponse(),
            self.do_roarequest('ListAlgoDefs', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/algo/detail', 'json', req, runtime)
        )

    async def list_algo_defs_with_options_async(
        self,
        request: pai_studio_20210202_models.ListAlgoDefsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListAlgoDefsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=UtilClient.to_array(request.body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAlgoDefsResponse(),
            await self.do_roarequest_async('ListAlgoDefs', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/algo/detail', 'json', req, runtime)
        )

    def list_auth_roles(
        self,
        request: pai_studio_20210202_models.ListAuthRolesRequest,
    ) -> pai_studio_20210202_models.ListAuthRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_auth_roles_with_options(request, headers, runtime)

    async def list_auth_roles_async(
        self,
        request: pai_studio_20210202_models.ListAuthRolesRequest,
    ) -> pai_studio_20210202_models.ListAuthRolesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_auth_roles_with_options_async(request, headers, runtime)

    def list_auth_roles_with_options(
        self,
        request: pai_studio_20210202_models.ListAuthRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListAuthRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.is_generate_token):
            query['IsGenerateToken'] = request.is_generate_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAuthRolesResponse(),
            self.do_roarequest('ListAuthRoles', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/authorization/roles', 'json', req, runtime)
        )

    async def list_auth_roles_with_options_async(
        self,
        request: pai_studio_20210202_models.ListAuthRolesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListAuthRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.is_generate_token):
            query['IsGenerateToken'] = request.is_generate_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListAuthRolesResponse(),
            await self.do_roarequest_async('ListAuthRoles', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/authorization/roles', 'json', req, runtime)
        )

    def list_experiments(
        self,
        request: pai_studio_20210202_models.ListExperimentsRequest,
    ) -> pai_studio_20210202_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_experiments_with_options(request, headers, runtime)

    async def list_experiments_async(
        self,
        request: pai_studio_20210202_models.ListExperimentsRequest,
    ) -> pai_studio_20210202_models.ListExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_experiments_with_options_async(request, headers, runtime)

    def list_experiments_with_options(
        self,
        request: pai_studio_20210202_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListExperimentsResponse(),
            self.do_roarequest('ListExperiments', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments', 'json', req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: pai_studio_20210202_models.ListExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListExperimentsResponse(),
            await self.do_roarequest_async('ListExperiments', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments', 'json', req, runtime)
        )

    def list_image_labels(
        self,
        request: pai_studio_20210202_models.ListImageLabelsRequest,
    ) -> pai_studio_20210202_models.ListImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_image_labels_with_options(request, headers, runtime)

    async def list_image_labels_async(
        self,
        request: pai_studio_20210202_models.ListImageLabelsRequest,
    ) -> pai_studio_20210202_models.ListImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_image_labels_with_options_async(request, headers, runtime)

    def list_image_labels_with_options(
        self,
        request: pai_studio_20210202_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListImageLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImageLabelsResponse(),
            self.do_roarequest('ListImageLabels', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/image/labels', 'json', req, runtime)
        )

    async def list_image_labels_with_options_async(
        self,
        request: pai_studio_20210202_models.ListImageLabelsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListImageLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.label_keys):
            query['LabelKeys'] = request.label_keys
        if not UtilClient.is_unset(request.label_filter):
            query['LabelFilter'] = request.label_filter
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImageLabelsResponse(),
            await self.do_roarequest_async('ListImageLabels', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/image/labels', 'json', req, runtime)
        )

    def list_images(
        self,
        request: pai_studio_20210202_models.ListImagesRequest,
    ) -> pai_studio_20210202_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_images_with_options(request, headers, runtime)

    async def list_images_async(
        self,
        request: pai_studio_20210202_models.ListImagesRequest,
    ) -> pai_studio_20210202_models.ListImagesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_images_with_options_async(request, headers, runtime)

    def list_images_with_options(
        self,
        request: pai_studio_20210202_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImagesResponse(),
            self.do_roarequest('ListImages', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: pai_studio_20210202_models.ListImagesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListImagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListImagesResponse(),
            await self.do_roarequest_async('ListImages', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/images', 'json', req, runtime)
        )

    def list_jobs(
        self,
        request: pai_studio_20210202_models.ListJobsRequest,
    ) -> pai_studio_20210202_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(request, headers, runtime)

    async def list_jobs_async(
        self,
        request: pai_studio_20210202_models.ListJobsRequest,
    ) -> pai_studio_20210202_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        request: pai_studio_20210202_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListJobsResponse(),
            self.do_roarequest('ListJobs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: pai_studio_20210202_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.creator):
            query['Creator'] = request.creator
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListJobsResponse(),
            await self.do_roarequest_async('ListJobs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/jobs', 'json', req, runtime)
        )

    def list_node_outputs(
        self,
        experiment_id: str,
        node_id: str,
    ) -> pai_studio_20210202_models.ListNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_outputs_with_options(experiment_id, node_id, headers, runtime)

    async def list_node_outputs_async(
        self,
        experiment_id: str,
        node_id: str,
    ) -> pai_studio_20210202_models.ListNodeOutputsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_node_outputs_with_options_async(experiment_id, node_id, headers, runtime)

    def list_node_outputs_with_options(
        self,
        experiment_id: str,
        node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListNodeOutputsResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListNodeOutputsResponse(),
            self.do_roarequest('ListNodeOutputs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/outputs', 'json', req, runtime)
        )

    async def list_node_outputs_with_options_async(
        self,
        experiment_id: str,
        node_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListNodeOutputsResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        node_id = OpenApiUtilClient.get_encode_param(node_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListNodeOutputsResponse(),
            await self.do_roarequest_async('ListNodeOutputs', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/experiments/{experiment_id}/nodes/{node_id}/outputs', 'json', req, runtime)
        )

    def list_recent_experiments(
        self,
        request: pai_studio_20210202_models.ListRecentExperimentsRequest,
    ) -> pai_studio_20210202_models.ListRecentExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_recent_experiments_with_options(request, headers, runtime)

    async def list_recent_experiments_async(
        self,
        request: pai_studio_20210202_models.ListRecentExperimentsRequest,
    ) -> pai_studio_20210202_models.ListRecentExperimentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_recent_experiments_with_options_async(request, headers, runtime)

    def list_recent_experiments_with_options(
        self,
        request: pai_studio_20210202_models.ListRecentExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListRecentExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListRecentExperimentsResponse(),
            self.do_roarequest('ListRecentExperiments', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/recentexperiments', 'json', req, runtime)
        )

    async def list_recent_experiments_with_options_async(
        self,
        request: pai_studio_20210202_models.ListRecentExperimentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListRecentExperimentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListRecentExperimentsResponse(),
            await self.do_roarequest_async('ListRecentExperiments', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/recentexperiments', 'json', req, runtime)
        )

    def list_services(
        self,
        request: pai_studio_20210202_models.ListServicesRequest,
    ) -> pai_studio_20210202_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: pai_studio_20210202_models.ListServicesRequest,
    ) -> pai_studio_20210202_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_services_with_options(
        self,
        request: pai_studio_20210202_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListServicesResponse(),
            self.do_roarequest('ListServices', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/services', 'json', req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: pai_studio_20210202_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListServicesResponse(),
            await self.do_roarequest_async('ListServices', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/services', 'json', req, runtime)
        )

    def list_templates(
        self,
        request: pai_studio_20210202_models.ListTemplatesRequest,
    ) -> pai_studio_20210202_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_templates_with_options(request, headers, runtime)

    async def list_templates_async(
        self,
        request: pai_studio_20210202_models.ListTemplatesRequest,
    ) -> pai_studio_20210202_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_templates_with_options_async(request, headers, runtime)

    def list_templates_with_options(
        self,
        request: pai_studio_20210202_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.list):
            query['List'] = request.list
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListTemplatesResponse(),
            self.do_roarequest('ListTemplates', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: pai_studio_20210202_models.ListTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.list):
            query['List'] = request.list
        if not UtilClient.is_unset(request.tag_id):
            query['TagId'] = request.tag_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.type_id):
            query['TypeId'] = request.type_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.ListTemplatesResponse(),
            await self.do_roarequest_async('ListTemplates', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/templates', 'json', req, runtime)
        )

    def preview_mctable(
        self,
        table_name: str,
        request: pai_studio_20210202_models.PreviewMCTableRequest,
    ) -> pai_studio_20210202_models.PreviewMCTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.preview_mctable_with_options(table_name, request, headers, runtime)

    async def preview_mctable_async(
        self,
        table_name: str,
        request: pai_studio_20210202_models.PreviewMCTableRequest,
    ) -> pai_studio_20210202_models.PreviewMCTableResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.preview_mctable_with_options_async(table_name, request, headers, runtime)

    def preview_mctable_with_options(
        self,
        table_name: str,
        request: pai_studio_20210202_models.PreviewMCTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.PreviewMCTableResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.PreviewMCTableResponse(),
            self.do_roarequest('PreviewMCTable', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables/{table_name}/preview', 'json', req, runtime)
        )

    async def preview_mctable_with_options_async(
        self,
        table_name: str,
        request: pai_studio_20210202_models.PreviewMCTableRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.PreviewMCTableResponse:
        UtilClient.validate_model(request)
        table_name = OpenApiUtilClient.get_encode_param(table_name)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.PreviewMCTableResponse(),
            await self.do_roarequest_async('PreviewMCTable', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables/{table_name}/preview', 'json', req, runtime)
        )

    def remove_image(
        self,
        image_id: str,
    ) -> pai_studio_20210202_models.RemoveImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_with_options(image_id, headers, runtime)

    async def remove_image_async(
        self,
        image_id: str,
    ) -> pai_studio_20210202_models.RemoveImageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_image_with_options_async(image_id, headers, runtime)

    def remove_image_with_options(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.RemoveImageResponse:
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageResponse(),
            self.do_roarequest('RemoveImage', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/images/{image_id}', 'json', req, runtime)
        )

    async def remove_image_with_options_async(
        self,
        image_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.RemoveImageResponse:
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageResponse(),
            await self.do_roarequest_async('RemoveImage', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/images/{image_id}', 'json', req, runtime)
        )

    def remove_image_labels(
        self,
        image_id: str,
        label_key: str,
    ) -> pai_studio_20210202_models.RemoveImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_image_labels_with_options(image_id, label_key, headers, runtime)

    async def remove_image_labels_async(
        self,
        image_id: str,
        label_key: str,
    ) -> pai_studio_20210202_models.RemoveImageLabelsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_image_labels_with_options_async(image_id, label_key, headers, runtime)

    def remove_image_labels_with_options(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.RemoveImageLabelsResponse:
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        label_key = OpenApiUtilClient.get_encode_param(label_key)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageLabelsResponse(),
            self.do_roarequest('RemoveImageLabels', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/images/{image_id}/labels/{label_key}', 'json', req, runtime)
        )

    async def remove_image_labels_with_options_async(
        self,
        image_id: str,
        label_key: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.RemoveImageLabelsResponse:
        image_id = OpenApiUtilClient.get_encode_param(image_id)
        label_key = OpenApiUtilClient.get_encode_param(label_key)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.RemoveImageLabelsResponse(),
            await self.do_roarequest_async('RemoveImageLabels', '2021-02-02', 'HTTPS', 'DELETE', 'AK', f'/api/v1/images/{image_id}/labels/{label_key}', 'json', req, runtime)
        )

    def search_mctables(
        self,
        request: pai_studio_20210202_models.SearchMCTablesRequest,
    ) -> pai_studio_20210202_models.SearchMCTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_mctables_with_options(request, headers, runtime)

    async def search_mctables_async(
        self,
        request: pai_studio_20210202_models.SearchMCTablesRequest,
    ) -> pai_studio_20210202_models.SearchMCTablesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_mctables_with_options_async(request, headers, runtime)

    def search_mctables_with_options(
        self,
        request: pai_studio_20210202_models.SearchMCTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.SearchMCTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.SearchMCTablesResponse(),
            self.do_roarequest('SearchMCTables', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables', 'json', req, runtime)
        )

    async def search_mctables_with_options_async(
        self,
        request: pai_studio_20210202_models.SearchMCTablesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.SearchMCTablesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.SearchMCTablesResponse(),
            await self.do_roarequest_async('SearchMCTables', '2021-02-02', 'HTTPS', 'GET', 'AK', f'/api/v1/datasources/maxcompute/tables', 'json', req, runtime)
        )

    def stop_experiment(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.StopExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_experiment_with_options(experiment_id, headers, runtime)

    async def stop_experiment_async(
        self,
        experiment_id: str,
    ) -> pai_studio_20210202_models.StopExperimentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_experiment_with_options_async(experiment_id, headers, runtime)

    def stop_experiment_with_options(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.StopExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopExperimentResponse(),
            self.do_roarequest('StopExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments/{experiment_id}/stop', 'json', req, runtime)
        )

    async def stop_experiment_with_options_async(
        self,
        experiment_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.StopExperimentResponse:
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopExperimentResponse(),
            await self.do_roarequest_async('StopExperiment', '2021-02-02', 'HTTPS', 'POST', 'AK', f'/api/v1/experiments/{experiment_id}/stop', 'json', req, runtime)
        )

    def stop_job(
        self,
        job_id: str,
    ) -> pai_studio_20210202_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.stop_job_with_options(job_id, headers, runtime)

    async def stop_job_async(
        self,
        job_id: str,
    ) -> pai_studio_20210202_models.StopJobResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.stop_job_with_options_async(job_id, headers, runtime)

    def stop_job_with_options(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.StopJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopJobResponse(),
            self.do_roarequest('StopJob', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/jobs/{job_id}/stop', 'json', req, runtime)
        )

    async def stop_job_with_options_async(
        self,
        job_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.StopJobResponse:
        job_id = OpenApiUtilClient.get_encode_param(job_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.StopJobResponse(),
            await self.do_roarequest_async('StopJob', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/jobs/{job_id}/stop', 'json', req, runtime)
        )

    def update_experiment_content(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentContentRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_content_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_content_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentContentRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentContentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_content_with_options_async(experiment_id, request, headers, runtime)

    def update_experiment_content_with_options(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentContentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentContentResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentContentResponse(),
            self.do_roarequest('UpdateExperimentContent', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experiments/{experiment_id}/content', 'json', req, runtime)
        )

    async def update_experiment_content_with_options_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentContentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentContentResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.version):
            body['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentContentResponse(),
            await self.do_roarequest_async('UpdateExperimentContent', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experiments/{experiment_id}/content', 'json', req, runtime)
        )

    def update_experiment_folder(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.UpdateExperimentFolderRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_folder_with_options(folder_id, request, headers, runtime)

    async def update_experiment_folder_async(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.UpdateExperimentFolderRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentFolderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_folder_with_options_async(folder_id, request, headers, runtime)

    def update_experiment_folder_with_options(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.UpdateExperimentFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentFolderResponse:
        UtilClient.validate_model(request)
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentFolderResponse(),
            self.do_roarequest('UpdateExperimentFolder', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experimentfolders/{folder_id}', 'json', req, runtime)
        )

    async def update_experiment_folder_with_options_async(
        self,
        folder_id: str,
        request: pai_studio_20210202_models.UpdateExperimentFolderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentFolderResponse:
        UtilClient.validate_model(request)
        folder_id = OpenApiUtilClient.get_encode_param(folder_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.parent_folder_id):
            body['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentFolderResponse(),
            await self.do_roarequest_async('UpdateExperimentFolder', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experimentfolders/{folder_id}', 'json', req, runtime)
        )

    def update_experiment_meta(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentMetaRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_experiment_meta_with_options(experiment_id, request, headers, runtime)

    async def update_experiment_meta_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentMetaRequest,
    ) -> pai_studio_20210202_models.UpdateExperimentMetaResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_experiment_meta_with_options_async(experiment_id, request, headers, runtime)

    def update_experiment_meta_with_options(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentMetaResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentMetaResponse(),
            self.do_roarequest('UpdateExperimentMeta', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experiments/{experiment_id}/meta', 'json', req, runtime)
        )

    async def update_experiment_meta_with_options_async(
        self,
        experiment_id: str,
        request: pai_studio_20210202_models.UpdateExperimentMetaRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> pai_studio_20210202_models.UpdateExperimentMetaResponse:
        UtilClient.validate_model(request)
        experiment_id = OpenApiUtilClient.get_encode_param(experiment_id)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.folder_id):
            body['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.options):
            body['Options'] = request.options
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        return TeaCore.from_map(
            pai_studio_20210202_models.UpdateExperimentMetaResponse(),
            await self.do_roarequest_async('UpdateExperimentMeta', '2021-02-02', 'HTTPS', 'PUT', 'AK', f'/api/v1/experiments/{experiment_id}/meta', 'json', req, runtime)
        )
