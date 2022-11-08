# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_viapi_regen20211119 import models as viapi_regen_20211119_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


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
            'ap-northeast-1': 'viapi-regen-daily.aliyuncs.com',
            'ap-northeast-2-pop': 'viapi-regen-daily.aliyuncs.com',
            'ap-south-1': 'viapi-regen-daily.aliyuncs.com',
            'ap-southeast-1': 'viapi-regen-daily.aliyuncs.com',
            'ap-southeast-2': 'viapi-regen-daily.aliyuncs.com',
            'ap-southeast-3': 'viapi-regen-daily.aliyuncs.com',
            'ap-southeast-5': 'viapi-regen-daily.aliyuncs.com',
            'cn-beijing': 'viapi-regen-daily.aliyuncs.com',
            'cn-beijing-finance-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-beijing-finance-pop': 'viapi-regen-daily.aliyuncs.com',
            'cn-beijing-gov-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-beijing-nu16-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-chengdu': 'viapi-regen-daily.aliyuncs.com',
            'cn-edge-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-fujian': 'viapi-regen-daily.aliyuncs.com',
            'cn-haidian-cm12-c01': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-finance': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'viapi-regen-daily.aliyuncs.com',
            'cn-hangzhou-test-306': 'viapi-regen-daily.aliyuncs.com',
            'cn-hongkong': 'viapi-regen-daily.aliyuncs.com',
            'cn-hongkong-finance-pop': 'viapi-regen-daily.aliyuncs.com',
            'cn-huhehaote': 'viapi-regen-daily.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-north-2-gov-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-qingdao': 'viapi-regen-daily.aliyuncs.com',
            'cn-qingdao-nebula': 'viapi-regen-daily.aliyuncs.com',
            'cn-shanghai-et15-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-shanghai-et2-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-shanghai-finance-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-shanghai-inner': 'viapi-regen-daily.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-shenzhen': 'viapi-regen-daily.aliyuncs.com',
            'cn-shenzhen-finance-1': 'viapi-regen-daily.aliyuncs.com',
            'cn-shenzhen-inner': 'viapi-regen-daily.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'viapi-regen-daily.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-wuhan': 'viapi-regen-daily.aliyuncs.com',
            'cn-wulanchabu': 'viapi-regen-daily.aliyuncs.com',
            'cn-yushanfang': 'viapi-regen-daily.aliyuncs.com',
            'cn-zhangbei': 'viapi-regen-daily.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'viapi-regen-daily.aliyuncs.com',
            'cn-zhangjiakou': 'viapi-regen-daily.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'viapi-regen-daily.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'viapi-regen-daily.aliyuncs.com',
            'eu-central-1': 'viapi-regen-daily.aliyuncs.com',
            'eu-west-1': 'viapi-regen-daily.aliyuncs.com',
            'eu-west-1-oxs': 'viapi-regen-daily.aliyuncs.com',
            'me-east-1': 'viapi-regen-daily.aliyuncs.com',
            'rus-west-1-pop': 'viapi-regen-daily.aliyuncs.com',
            'us-east-1': 'viapi-regen-daily.aliyuncs.com',
            'us-west-1': 'viapi-regen-daily.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('viapi-regen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_dataset_with_options(
        self,
        request: viapi_regen_20211119_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dataset_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dataset(
        self,
        request: viapi_regen_20211119_models.CreateDatasetRequest,
    ) -> viapi_regen_20211119_models.CreateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dataset_with_options(request, runtime)

    async def create_dataset_async(
        self,
        request: viapi_regen_20211119_models.CreateDatasetRequest,
    ) -> viapi_regen_20211119_models.CreateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dataset_with_options_async(request, runtime)

    def create_labelset_with_options(
        self,
        request: viapi_regen_20211119_models.CreateLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.object_key):
            body['ObjectKey'] = request.object_key
        if not UtilClient.is_unset(request.pre_label_id):
            body['PreLabelId'] = request.pre_label_id
        if not UtilClient.is_unset(request.tag_settings):
            body['TagSettings'] = request.tag_settings
        if not UtilClient.is_unset(request.tag_user_list):
            body['TagUserList'] = request.tag_user_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateLabelsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_labelset_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.object_key):
            body['ObjectKey'] = request.object_key
        if not UtilClient.is_unset(request.pre_label_id):
            body['PreLabelId'] = request.pre_label_id
        if not UtilClient.is_unset(request.tag_settings):
            body['TagSettings'] = request.tag_settings
        if not UtilClient.is_unset(request.tag_user_list):
            body['TagUserList'] = request.tag_user_list
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateLabelsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_labelset(
        self,
        request: viapi_regen_20211119_models.CreateLabelsetRequest,
    ) -> viapi_regen_20211119_models.CreateLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_labelset_with_options(request, runtime)

    async def create_labelset_async(
        self,
        request: viapi_regen_20211119_models.CreateLabelsetRequest,
    ) -> viapi_regen_20211119_models.CreateLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_labelset_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: viapi_regen_20211119_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.authorized_account):
            body['AuthorizedAccount'] = request.authorized_account
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.train_task_id):
            body['TrainTaskId'] = request.train_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.authorized_account):
            body['AuthorizedAccount'] = request.authorized_account
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.train_task_id):
            body['TrainTaskId'] = request.train_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: viapi_regen_20211119_models.CreateServiceRequest,
    ) -> viapi_regen_20211119_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: viapi_regen_20211119_models.CreateServiceRequest,
    ) -> viapi_regen_20211119_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def create_tag_task_with_options(
        self,
        request: viapi_regen_20211119_models.CreateTagTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateTagTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labelset_id):
            body['LabelsetId'] = request.labelset_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateTagTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateTagTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateTagTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labelset_id):
            body['LabelsetId'] = request.labelset_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTagTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateTagTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_task(
        self,
        request: viapi_regen_20211119_models.CreateTagTaskRequest,
    ) -> viapi_regen_20211119_models.CreateTagTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_task_with_options(request, runtime)

    async def create_tag_task_async(
        self,
        request: viapi_regen_20211119_models.CreateTagTaskRequest,
    ) -> viapi_regen_20211119_models.CreateTagTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_task_with_options_async(request, runtime)

    def create_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.CreateTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_parameters):
            body['AdvancedParameters'] = request.advanced_parameters
        if not UtilClient.is_unset(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_train_task_id):
            body['PreTrainTaskId'] = request.pre_train_task_id
        if not UtilClient.is_unset(request.train_mode):
            body['TrainMode'] = request.train_mode
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_parameters):
            body['AdvancedParameters'] = request.advanced_parameters
        if not UtilClient.is_unset(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_train_task_id):
            body['PreTrainTaskId'] = request.pre_train_task_id
        if not UtilClient.is_unset(request.train_mode):
            body['TrainMode'] = request.train_mode
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_train_task(
        self,
        request: viapi_regen_20211119_models.CreateTrainTaskRequest,
    ) -> viapi_regen_20211119_models.CreateTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_train_task_with_options(request, runtime)

    async def create_train_task_async(
        self,
        request: viapi_regen_20211119_models.CreateTrainTaskRequest,
    ) -> viapi_regen_20211119_models.CreateTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_train_task_with_options_async(request, runtime)

    def create_workspace_with_options(
        self,
        request: viapi_regen_20211119_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_workspace_with_options_async(
        self,
        request: viapi_regen_20211119_models.CreateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CreateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CreateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_workspace(
        self,
        request: viapi_regen_20211119_models.CreateWorkspaceRequest,
    ) -> viapi_regen_20211119_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_workspace_with_options(request, runtime)

    async def create_workspace_async(
        self,
        request: viapi_regen_20211119_models.CreateWorkspaceRequest,
    ) -> viapi_regen_20211119_models.CreateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_workspace_with_options_async(request, runtime)

    def customize_classify_image_with_options(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeClassifyImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeClassifyImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def customize_classify_image_with_options_async(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeClassifyImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeClassifyImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customize_classify_image(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.customize_classify_image_with_options(request, runtime)

    async def customize_classify_image_async(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.customize_classify_image_with_options_async(request, runtime)

    def customize_classify_image_advance(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_classify_image_req = viapi_regen_20211119_models.CustomizeClassifyImageRequest()
        OpenApiUtilClient.convert(request, customize_classify_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            customize_classify_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_classify_image_resp = self.customize_classify_image_with_options(customize_classify_image_req, runtime)
        return customize_classify_image_resp

    async def customize_classify_image_advance_async(
        self,
        request: viapi_regen_20211119_models.CustomizeClassifyImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeClassifyImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_classify_image_req = viapi_regen_20211119_models.CustomizeClassifyImageRequest()
        OpenApiUtilClient.convert(request, customize_classify_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            customize_classify_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_classify_image_resp = await self.customize_classify_image_with_options_async(customize_classify_image_req, runtime)
        return customize_classify_image_resp

    def customize_detect_image_with_options(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeDetectImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeDetectImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def customize_detect_image_with_options_async(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeDetectImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeDetectImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customize_detect_image(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.customize_detect_image_with_options(request, runtime)

    async def customize_detect_image_async(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.customize_detect_image_with_options_async(request, runtime)

    def customize_detect_image_advance(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_detect_image_req = viapi_regen_20211119_models.CustomizeDetectImageRequest()
        OpenApiUtilClient.convert(request, customize_detect_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            customize_detect_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_detect_image_resp = self.customize_detect_image_with_options(customize_detect_image_req, runtime)
        return customize_detect_image_resp

    async def customize_detect_image_advance_async(
        self,
        request: viapi_regen_20211119_models.CustomizeDetectImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeDetectImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_detect_image_req = viapi_regen_20211119_models.CustomizeDetectImageRequest()
        OpenApiUtilClient.convert(request, customize_detect_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            customize_detect_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_detect_image_resp = await self.customize_detect_image_with_options_async(customize_detect_image_req, runtime)
        return customize_detect_image_resp

    def customize_instance_segment_image_with_options(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeInstanceSegmentImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def customize_instance_segment_image_with_options_async(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CustomizeInstanceSegmentImage',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def customize_instance_segment_image(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.customize_instance_segment_image_with_options(request, runtime)

    async def customize_instance_segment_image_async(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.customize_instance_segment_image_with_options_async(request, runtime)

    def customize_instance_segment_image_advance(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_instance_segment_image_req = viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest()
        OpenApiUtilClient.convert(request, customize_instance_segment_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            customize_instance_segment_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_instance_segment_image_resp = self.customize_instance_segment_image_with_options(customize_instance_segment_image_req, runtime)
        return customize_instance_segment_image_resp

    async def customize_instance_segment_image_advance_async(
        self,
        request: viapi_regen_20211119_models.CustomizeInstanceSegmentImageAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.CustomizeInstanceSegmentImageResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='viapi-regen',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        customize_instance_segment_image_req = viapi_regen_20211119_models.CustomizeInstanceSegmentImageRequest()
        OpenApiUtilClient.convert(request, customize_instance_segment_image_req)
        if not UtilClient.is_unset(request.image_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.image_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            customize_instance_segment_image_req.image_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        customize_instance_segment_image_resp = await self.customize_instance_segment_image_with_options_async(customize_instance_segment_image_req, runtime)
        return customize_instance_segment_image_resp

    def debug_service_with_options(
        self,
        request: viapi_regen_20211119_models.DebugServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DebugServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DebugServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def debug_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.DebugServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DebugServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DebugService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DebugServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def debug_service(
        self,
        request: viapi_regen_20211119_models.DebugServiceRequest,
    ) -> viapi_regen_20211119_models.DebugServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.debug_service_with_options(request, runtime)

    async def debug_service_async(
        self,
        request: viapi_regen_20211119_models.DebugServiceRequest,
    ) -> viapi_regen_20211119_models.DebugServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.debug_service_with_options_async(request, runtime)

    def delete_data_reflow_data_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteDataReflowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteDataReflowDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataReflowData',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteDataReflowDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_reflow_data_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteDataReflowDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteDataReflowDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataReflowData',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteDataReflowDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_reflow_data(
        self,
        request: viapi_regen_20211119_models.DeleteDataReflowDataRequest,
    ) -> viapi_regen_20211119_models.DeleteDataReflowDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_reflow_data_with_options(request, runtime)

    async def delete_data_reflow_data_async(
        self,
        request: viapi_regen_20211119_models.DeleteDataReflowDataRequest,
    ) -> viapi_regen_20211119_models.DeleteDataReflowDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_reflow_data_with_options_async(request, runtime)

    def delete_dataset_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dataset_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dataset(
        self,
        request: viapi_regen_20211119_models.DeleteDatasetRequest,
    ) -> viapi_regen_20211119_models.DeleteDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dataset_with_options(request, runtime)

    async def delete_dataset_async(
        self,
        request: viapi_regen_20211119_models.DeleteDatasetRequest,
    ) -> viapi_regen_20211119_models.DeleteDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dataset_with_options_async(request, runtime)

    def delete_labelset_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteLabelsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_labelset_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteLabelsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_labelset(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetRequest,
    ) -> viapi_regen_20211119_models.DeleteLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_labelset_with_options(request, runtime)

    async def delete_labelset_async(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetRequest,
    ) -> viapi_regen_20211119_models.DeleteLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_labelset_with_options_async(request, runtime)

    def delete_labelset_data_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteLabelsetDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabelsetData',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteLabelsetDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_labelset_data_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteLabelsetDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteLabelsetData',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteLabelsetDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_labelset_data(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetDataRequest,
    ) -> viapi_regen_20211119_models.DeleteLabelsetDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_labelset_data_with_options(request, runtime)

    async def delete_labelset_data_async(
        self,
        request: viapi_regen_20211119_models.DeleteLabelsetDataRequest,
    ) -> viapi_regen_20211119_models.DeleteLabelsetDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_labelset_data_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: viapi_regen_20211119_models.DeleteServiceRequest,
    ) -> viapi_regen_20211119_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: viapi_regen_20211119_models.DeleteServiceRequest,
    ) -> viapi_regen_20211119_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def delete_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_train_task(
        self,
        request: viapi_regen_20211119_models.DeleteTrainTaskRequest,
    ) -> viapi_regen_20211119_models.DeleteTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_train_task_with_options(request, runtime)

    async def delete_train_task_async(
        self,
        request: viapi_regen_20211119_models.DeleteTrainTaskRequest,
    ) -> viapi_regen_20211119_models.DeleteTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_train_task_with_options_async(request, runtime)

    def delete_workspace_with_options(
        self,
        request: viapi_regen_20211119_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_workspace_with_options_async(
        self,
        request: viapi_regen_20211119_models.DeleteWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DeleteWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DeleteWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_workspace(
        self,
        request: viapi_regen_20211119_models.DeleteWorkspaceRequest,
    ) -> viapi_regen_20211119_models.DeleteWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_workspace_with_options(request, runtime)

    async def delete_workspace_async(
        self,
        request: viapi_regen_20211119_models.DeleteWorkspaceRequest,
    ) -> viapi_regen_20211119_models.DeleteWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_workspace_with_options_async(request, runtime)

    def disable_data_reflow_with_options(
        self,
        request: viapi_regen_20211119_models.DisableDataReflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DisableDataReflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableDataReflow',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DisableDataReflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_data_reflow_with_options_async(
        self,
        request: viapi_regen_20211119_models.DisableDataReflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DisableDataReflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableDataReflow',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DisableDataReflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_data_reflow(
        self,
        request: viapi_regen_20211119_models.DisableDataReflowRequest,
    ) -> viapi_regen_20211119_models.DisableDataReflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_data_reflow_with_options(request, runtime)

    async def disable_data_reflow_async(
        self,
        request: viapi_regen_20211119_models.DisableDataReflowRequest,
    ) -> viapi_regen_20211119_models.DisableDataReflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_data_reflow_with_options_async(request, runtime)

    def download_file_name_list_with_options(
        self,
        request: viapi_regen_20211119_models.DownloadFileNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DownloadFileNameListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFileNameList',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DownloadFileNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_file_name_list_with_options_async(
        self,
        request: viapi_regen_20211119_models.DownloadFileNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DownloadFileNameListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadFileNameList',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DownloadFileNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_file_name_list(
        self,
        request: viapi_regen_20211119_models.DownloadFileNameListRequest,
    ) -> viapi_regen_20211119_models.DownloadFileNameListResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_file_name_list_with_options(request, runtime)

    async def download_file_name_list_async(
        self,
        request: viapi_regen_20211119_models.DownloadFileNameListRequest,
    ) -> viapi_regen_20211119_models.DownloadFileNameListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_file_name_list_with_options_async(request, runtime)

    def download_label_file_with_options(
        self,
        request: viapi_regen_20211119_models.DownloadLabelFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DownloadLabelFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadLabelFile',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DownloadLabelFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_label_file_with_options_async(
        self,
        request: viapi_regen_20211119_models.DownloadLabelFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.DownloadLabelFileResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadLabelFile',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.DownloadLabelFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_label_file(
        self,
        request: viapi_regen_20211119_models.DownloadLabelFileRequest,
    ) -> viapi_regen_20211119_models.DownloadLabelFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_label_file_with_options(request, runtime)

    async def download_label_file_async(
        self,
        request: viapi_regen_20211119_models.DownloadLabelFileRequest,
    ) -> viapi_regen_20211119_models.DownloadLabelFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_label_file_with_options_async(request, runtime)

    def enable_data_reflow_with_options(
        self,
        request: viapi_regen_20211119_models.EnableDataReflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.EnableDataReflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_reflow_oss_path):
            body['DataReflowOssPath'] = request.data_reflow_oss_path
        if not UtilClient.is_unset(request.data_reflow_rate):
            body['DataReflowRate'] = request.data_reflow_rate
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableDataReflow',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.EnableDataReflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_data_reflow_with_options_async(
        self,
        request: viapi_regen_20211119_models.EnableDataReflowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.EnableDataReflowResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_reflow_oss_path):
            body['DataReflowOssPath'] = request.data_reflow_oss_path
        if not UtilClient.is_unset(request.data_reflow_rate):
            body['DataReflowRate'] = request.data_reflow_rate
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableDataReflow',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.EnableDataReflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_data_reflow(
        self,
        request: viapi_regen_20211119_models.EnableDataReflowRequest,
    ) -> viapi_regen_20211119_models.EnableDataReflowResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_data_reflow_with_options(request, runtime)

    async def enable_data_reflow_async(
        self,
        request: viapi_regen_20211119_models.EnableDataReflowRequest,
    ) -> viapi_regen_20211119_models.EnableDataReflowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_data_reflow_with_options_async(request, runtime)

    def export_data_reflow_data_list_with_options(
        self,
        request: viapi_regen_20211119_models.ExportDataReflowDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ExportDataReflowDataListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportDataReflowDataList',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ExportDataReflowDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_data_reflow_data_list_with_options_async(
        self,
        request: viapi_regen_20211119_models.ExportDataReflowDataListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ExportDataReflowDataListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportDataReflowDataList',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ExportDataReflowDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_data_reflow_data_list(
        self,
        request: viapi_regen_20211119_models.ExportDataReflowDataListRequest,
    ) -> viapi_regen_20211119_models.ExportDataReflowDataListResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_data_reflow_data_list_with_options(request, runtime)

    async def export_data_reflow_data_list_async(
        self,
        request: viapi_regen_20211119_models.ExportDataReflowDataListRequest,
    ) -> viapi_regen_20211119_models.ExportDataReflowDataListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_data_reflow_data_list_with_options_async(request, runtime)

    def get_dataset_with_options(
        self,
        request: viapi_regen_20211119_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dataset_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dataset(
        self,
        request: viapi_regen_20211119_models.GetDatasetRequest,
    ) -> viapi_regen_20211119_models.GetDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dataset_with_options(request, runtime)

    async def get_dataset_async(
        self,
        request: viapi_regen_20211119_models.GetDatasetRequest,
    ) -> viapi_regen_20211119_models.GetDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dataset_with_options_async(request, runtime)

    def get_diff_count_labelset_and_dataset_with_options(
        self,
        request: viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labelset_id):
            body['LabelsetId'] = request.labelset_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDiffCountLabelsetAndDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diff_count_labelset_and_dataset_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.labelset_id):
            body['LabelsetId'] = request.labelset_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDiffCountLabelsetAndDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diff_count_labelset_and_dataset(
        self,
        request: viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetRequest,
    ) -> viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_diff_count_labelset_and_dataset_with_options(request, runtime)

    async def get_diff_count_labelset_and_dataset_async(
        self,
        request: viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetRequest,
    ) -> viapi_regen_20211119_models.GetDiffCountLabelsetAndDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_diff_count_labelset_and_dataset_with_options_async(request, runtime)

    def get_label_detail_with_options(
        self,
        request: viapi_regen_20211119_models.GetLabelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetLabelDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLabelDetail',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetLabelDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_label_detail_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetLabelDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetLabelDetailResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLabelDetail',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetLabelDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_label_detail(
        self,
        request: viapi_regen_20211119_models.GetLabelDetailRequest,
    ) -> viapi_regen_20211119_models.GetLabelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_label_detail_with_options(request, runtime)

    async def get_label_detail_async(
        self,
        request: viapi_regen_20211119_models.GetLabelDetailRequest,
    ) -> viapi_regen_20211119_models.GetLabelDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_label_detail_with_options_async(request, runtime)

    def get_labelset_with_options(
        self,
        request: viapi_regen_20211119_models.GetLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetLabelsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_labelset_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetLabelsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_labelset(
        self,
        request: viapi_regen_20211119_models.GetLabelsetRequest,
    ) -> viapi_regen_20211119_models.GetLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_labelset_with_options(request, runtime)

    async def get_labelset_async(
        self,
        request: viapi_regen_20211119_models.GetLabelsetRequest,
    ) -> viapi_regen_20211119_models.GetLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_labelset_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: viapi_regen_20211119_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        request: viapi_regen_20211119_models.GetServiceRequest,
    ) -> viapi_regen_20211119_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: viapi_regen_20211119_models.GetServiceRequest,
    ) -> viapi_regen_20211119_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_train_model_with_options(
        self,
        request: viapi_regen_20211119_models.GetTrainModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainModel',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_train_model_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetTrainModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainModelResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainModel',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_train_model(
        self,
        request: viapi_regen_20211119_models.GetTrainModelRequest,
    ) -> viapi_regen_20211119_models.GetTrainModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_model_with_options(request, runtime)

    async def get_train_model_async(
        self,
        request: viapi_regen_20211119_models.GetTrainModelRequest,
    ) -> viapi_regen_20211119_models.GetTrainModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_model_with_options_async(request, runtime)

    def get_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_train_task(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskRequest,
    ) -> viapi_regen_20211119_models.GetTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_task_with_options(request, runtime)

    async def get_train_task_async(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskRequest,
    ) -> viapi_regen_20211119_models.GetTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_task_with_options_async(request, runtime)

    def get_train_task_estimated_time_with_options(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskEstimatedTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainTaskEstimatedTime',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_train_task_estimated_time_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskEstimatedTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTrainTaskEstimatedTime',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_train_task_estimated_time(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskEstimatedTimeRequest,
    ) -> viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_train_task_estimated_time_with_options(request, runtime)

    async def get_train_task_estimated_time_async(
        self,
        request: viapi_regen_20211119_models.GetTrainTaskEstimatedTimeRequest,
    ) -> viapi_regen_20211119_models.GetTrainTaskEstimatedTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_train_task_estimated_time_with_options_async(request, runtime)

    def get_upload_policy_with_options(
        self,
        request: viapi_regen_20211119_models.GetUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadPolicy',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetUploadPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_policy_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetUploadPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetUploadPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadPolicy',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetUploadPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_policy(
        self,
        request: viapi_regen_20211119_models.GetUploadPolicyRequest,
    ) -> viapi_regen_20211119_models.GetUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_upload_policy_with_options(request, runtime)

    async def get_upload_policy_async(
        self,
        request: viapi_regen_20211119_models.GetUploadPolicyRequest,
    ) -> viapi_regen_20211119_models.GetUploadPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_policy_with_options_async(request, runtime)

    def get_workspace_with_options(
        self,
        request: viapi_regen_20211119_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workspace_with_options_async(
        self,
        request: viapi_regen_20211119_models.GetWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.GetWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.GetWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workspace(
        self,
        request: viapi_regen_20211119_models.GetWorkspaceRequest,
    ) -> viapi_regen_20211119_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workspace_with_options(request, runtime)

    async def get_workspace_async(
        self,
        request: viapi_regen_20211119_models.GetWorkspaceRequest,
    ) -> viapi_regen_20211119_models.GetWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workspace_with_options_async(request, runtime)

    def list_data_reflow_datas_with_options(
        self,
        request: viapi_regen_20211119_models.ListDataReflowDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDataReflowDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReflowDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDataReflowDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_reflow_datas_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListDataReflowDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDataReflowDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.image_name):
            body['ImageName'] = request.image_name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_id):
            body['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReflowDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDataReflowDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_reflow_datas(
        self,
        request: viapi_regen_20211119_models.ListDataReflowDatasRequest,
    ) -> viapi_regen_20211119_models.ListDataReflowDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_reflow_datas_with_options(request, runtime)

    async def list_data_reflow_datas_async(
        self,
        request: viapi_regen_20211119_models.ListDataReflowDatasRequest,
    ) -> viapi_regen_20211119_models.ListDataReflowDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_reflow_datas_with_options_async(request, runtime)

    def list_dataset_datas_with_options(
        self,
        request: viapi_regen_20211119_models.ListDatasetDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDatasetDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasetDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDatasetDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dataset_datas_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListDatasetDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDatasetDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.identity):
            body['Identity'] = request.identity
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasetDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDatasetDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dataset_datas(
        self,
        request: viapi_regen_20211119_models.ListDatasetDatasRequest,
    ) -> viapi_regen_20211119_models.ListDatasetDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dataset_datas_with_options(request, runtime)

    async def list_dataset_datas_async(
        self,
        request: viapi_regen_20211119_models.ListDatasetDatasRequest,
    ) -> viapi_regen_20211119_models.ListDatasetDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dataset_datas_with_options_async(request, runtime)

    def list_datasets_with_options(
        self,
        request: viapi_regen_20211119_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDatasetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDatasetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datasets_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListDatasetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListDatasetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatasets',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListDatasetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datasets(
        self,
        request: viapi_regen_20211119_models.ListDatasetsRequest,
    ) -> viapi_regen_20211119_models.ListDatasetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_datasets_with_options(request, runtime)

    async def list_datasets_async(
        self,
        request: viapi_regen_20211119_models.ListDatasetsRequest,
    ) -> viapi_regen_20211119_models.ListDatasetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_datasets_with_options_async(request, runtime)

    def list_labelset_datas_with_options(
        self,
        request: viapi_regen_20211119_models.ListLabelsetDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListLabelsetDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_abandon):
            body['IsAbandon'] = request.is_abandon
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabelsetDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListLabelsetDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_labelset_datas_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListLabelsetDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListLabelsetDatasResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.is_abandon):
            body['IsAbandon'] = request.is_abandon
        if not UtilClient.is_unset(request.label_id):
            body['LabelId'] = request.label_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.operation):
            body['Operation'] = request.operation
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabelsetDatas',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListLabelsetDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_labelset_datas(
        self,
        request: viapi_regen_20211119_models.ListLabelsetDatasRequest,
    ) -> viapi_regen_20211119_models.ListLabelsetDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_labelset_datas_with_options(request, runtime)

    async def list_labelset_datas_async(
        self,
        request: viapi_regen_20211119_models.ListLabelsetDatasRequest,
    ) -> viapi_regen_20211119_models.ListLabelsetDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_labelset_datas_with_options_async(request, runtime)

    def list_labelsets_with_options(
        self,
        request: viapi_regen_20211119_models.ListLabelsetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListLabelsetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabelsets',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListLabelsetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_labelsets_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListLabelsetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListLabelsetsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLabelsets',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListLabelsetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_labelsets(
        self,
        request: viapi_regen_20211119_models.ListLabelsetsRequest,
    ) -> viapi_regen_20211119_models.ListLabelsetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_labelsets_with_options(request, runtime)

    async def list_labelsets_async(
        self,
        request: viapi_regen_20211119_models.ListLabelsetsRequest,
    ) -> viapi_regen_20211119_models.ListLabelsetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_labelsets_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: viapi_regen_20211119_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: viapi_regen_20211119_models.ListServicesRequest,
    ) -> viapi_regen_20211119_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: viapi_regen_20211119_models.ListServicesRequest,
    ) -> viapi_regen_20211119_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def list_train_tasks_with_options(
        self,
        request: viapi_regen_20211119_models.ListTrainTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListTrainTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrainTasks',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListTrainTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_train_tasks_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListTrainTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListTrainTasksResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrainTasks',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListTrainTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_train_tasks(
        self,
        request: viapi_regen_20211119_models.ListTrainTasksRequest,
    ) -> viapi_regen_20211119_models.ListTrainTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_train_tasks_with_options(request, runtime)

    async def list_train_tasks_async(
        self,
        request: viapi_regen_20211119_models.ListTrainTasksRequest,
    ) -> viapi_regen_20211119_models.ListTrainTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_train_tasks_with_options_async(request, runtime)

    def list_workspaces_with_options(
        self,
        request: viapi_regen_20211119_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListWorkspacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workspaces_with_options_async(
        self,
        request: viapi_regen_20211119_models.ListWorkspacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.ListWorkspacesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkspaces',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.ListWorkspacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workspaces(
        self,
        request: viapi_regen_20211119_models.ListWorkspacesRequest,
    ) -> viapi_regen_20211119_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_workspaces_with_options(request, runtime)

    async def list_workspaces_async(
        self,
        request: viapi_regen_20211119_models.ListWorkspacesRequest,
    ) -> viapi_regen_20211119_models.ListWorkspacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_workspaces_with_options_async(request, runtime)

    def set_dataset_user_oss_path_with_options(
        self,
        request: viapi_regen_20211119_models.SetDatasetUserOssPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.SetDatasetUserOssPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDatasetUserOssPath',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.SetDatasetUserOssPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_dataset_user_oss_path_with_options_async(
        self,
        request: viapi_regen_20211119_models.SetDatasetUserOssPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.SetDatasetUserOssPathResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dataset_id):
            body['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetDatasetUserOssPath',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.SetDatasetUserOssPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_dataset_user_oss_path(
        self,
        request: viapi_regen_20211119_models.SetDatasetUserOssPathRequest,
    ) -> viapi_regen_20211119_models.SetDatasetUserOssPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_dataset_user_oss_path_with_options(request, runtime)

    async def set_dataset_user_oss_path_async(
        self,
        request: viapi_regen_20211119_models.SetDatasetUserOssPathRequest,
    ) -> viapi_regen_20211119_models.SetDatasetUserOssPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_dataset_user_oss_path_with_options_async(request, runtime)

    def start_service_with_options(
        self,
        request: viapi_regen_20211119_models.StartServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StartServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StartServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.StartServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StartServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StartServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service(
        self,
        request: viapi_regen_20211119_models.StartServiceRequest,
    ) -> viapi_regen_20211119_models.StartServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_service_with_options(request, runtime)

    async def start_service_async(
        self,
        request: viapi_regen_20211119_models.StartServiceRequest,
    ) -> viapi_regen_20211119_models.StartServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_service_with_options_async(request, runtime)

    def start_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.StartTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StartTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_start_flag):
            body['ForceStartFlag'] = request.force_start_flag
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.rely_on_task_id):
            body['RelyOnTaskId'] = request.rely_on_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StartTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.StartTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StartTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_start_flag):
            body['ForceStartFlag'] = request.force_start_flag
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.rely_on_task_id):
            body['RelyOnTaskId'] = request.rely_on_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StartTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_train_task(
        self,
        request: viapi_regen_20211119_models.StartTrainTaskRequest,
    ) -> viapi_regen_20211119_models.StartTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_train_task_with_options(request, runtime)

    async def start_train_task_async(
        self,
        request: viapi_regen_20211119_models.StartTrainTaskRequest,
    ) -> viapi_regen_20211119_models.StartTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_train_task_with_options_async(request, runtime)

    def stop_service_with_options(
        self,
        request: viapi_regen_20211119_models.StopServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StopServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StopServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.StopServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StopServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StopServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service(
        self,
        request: viapi_regen_20211119_models.StopServiceRequest,
    ) -> viapi_regen_20211119_models.StopServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_service_with_options(request, runtime)

    async def stop_service_async(
        self,
        request: viapi_regen_20211119_models.StopServiceRequest,
    ) -> viapi_regen_20211119_models.StopServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_service_with_options_async(request, runtime)

    def stop_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.StopTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StopTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StopTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.StopTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.StopTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.StopTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_train_task(
        self,
        request: viapi_regen_20211119_models.StopTrainTaskRequest,
    ) -> viapi_regen_20211119_models.StopTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_train_task_with_options(request, runtime)

    async def stop_train_task_async(
        self,
        request: viapi_regen_20211119_models.StopTrainTaskRequest,
    ) -> viapi_regen_20211119_models.StopTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_train_task_with_options_async(request, runtime)

    def update_dataset_with_options(
        self,
        request: viapi_regen_20211119_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dataset_with_options_async(
        self,
        request: viapi_regen_20211119_models.UpdateDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateDatasetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dataset(
        self,
        request: viapi_regen_20211119_models.UpdateDatasetRequest,
    ) -> viapi_regen_20211119_models.UpdateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dataset_with_options(request, runtime)

    async def update_dataset_async(
        self,
        request: viapi_regen_20211119_models.UpdateDatasetRequest,
    ) -> viapi_regen_20211119_models.UpdateDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dataset_with_options_async(request, runtime)

    def update_labelset_with_options(
        self,
        request: viapi_regen_20211119_models.UpdateLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.object_key):
            body['ObjectKey'] = request.object_key
        if not UtilClient.is_unset(request.tag_user_list):
            body['TagUserList'] = request.tag_user_list
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateLabelsetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_labelset_with_options_async(
        self,
        request: viapi_regen_20211119_models.UpdateLabelsetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateLabelsetResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.object_key):
            body['ObjectKey'] = request.object_key
        if not UtilClient.is_unset(request.tag_user_list):
            body['TagUserList'] = request.tag_user_list
        if not UtilClient.is_unset(request.user_oss_url):
            body['UserOssUrl'] = request.user_oss_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLabelset',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateLabelsetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_labelset(
        self,
        request: viapi_regen_20211119_models.UpdateLabelsetRequest,
    ) -> viapi_regen_20211119_models.UpdateLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_labelset_with_options(request, runtime)

    async def update_labelset_async(
        self,
        request: viapi_regen_20211119_models.UpdateLabelsetRequest,
    ) -> viapi_regen_20211119_models.UpdateLabelsetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_labelset_with_options_async(request, runtime)

    def update_service_with_options(
        self,
        request: viapi_regen_20211119_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.authorized_account):
            body['AuthorizedAccount'] = request.authorized_account
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        request: viapi_regen_20211119_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.authorization_type):
            body['AuthorizationType'] = request.authorization_type
        if not UtilClient.is_unset(request.authorized_account):
            body['AuthorizedAccount'] = request.authorized_account
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        request: viapi_regen_20211119_models.UpdateServiceRequest,
    ) -> viapi_regen_20211119_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    async def update_service_async(
        self,
        request: viapi_regen_20211119_models.UpdateServiceRequest,
    ) -> viapi_regen_20211119_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_with_options_async(request, runtime)

    def update_train_task_with_options(
        self,
        request: viapi_regen_20211119_models.UpdateTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_parameters):
            body['AdvancedParameters'] = request.advanced_parameters
        if not UtilClient.is_unset(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_train_task_flag):
            body['PreTrainTaskFlag'] = request.pre_train_task_flag
        if not UtilClient.is_unset(request.pre_train_task_id):
            body['PreTrainTaskId'] = request.pre_train_task_id
        if not UtilClient.is_unset(request.train_mode):
            body['TrainMode'] = request.train_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateTrainTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_train_task_with_options_async(
        self,
        request: viapi_regen_20211119_models.UpdateTrainTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateTrainTaskResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.advanced_parameters):
            body['AdvancedParameters'] = request.advanced_parameters
        if not UtilClient.is_unset(request.dataset_ids):
            body['DatasetIds'] = request.dataset_ids
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.label_ids):
            body['LabelIds'] = request.label_ids
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.pre_train_task_flag):
            body['PreTrainTaskFlag'] = request.pre_train_task_flag
        if not UtilClient.is_unset(request.pre_train_task_id):
            body['PreTrainTaskId'] = request.pre_train_task_id
        if not UtilClient.is_unset(request.train_mode):
            body['TrainMode'] = request.train_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTrainTask',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateTrainTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_train_task(
        self,
        request: viapi_regen_20211119_models.UpdateTrainTaskRequest,
    ) -> viapi_regen_20211119_models.UpdateTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_train_task_with_options(request, runtime)

    async def update_train_task_async(
        self,
        request: viapi_regen_20211119_models.UpdateTrainTaskRequest,
    ) -> viapi_regen_20211119_models.UpdateTrainTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_train_task_with_options_async(request, runtime)

    def update_workspace_with_options(
        self,
        request: viapi_regen_20211119_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_workspace_with_options_async(
        self,
        request: viapi_regen_20211119_models.UpdateWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> viapi_regen_20211119_models.UpdateWorkspaceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkspace',
            version='2021-11-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            viapi_regen_20211119_models.UpdateWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_workspace(
        self,
        request: viapi_regen_20211119_models.UpdateWorkspaceRequest,
    ) -> viapi_regen_20211119_models.UpdateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_workspace_with_options(request, runtime)

    async def update_workspace_async(
        self,
        request: viapi_regen_20211119_models.UpdateWorkspaceRequest,
    ) -> viapi_regen_20211119_models.UpdateWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_workspace_with_options_async(request, runtime)
