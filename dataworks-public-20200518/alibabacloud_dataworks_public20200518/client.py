# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dataworks_public20200518 import models as dataworks_public_20200518_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_rpc import models as rpc_models
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient
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
            'ap-northeast-1': 'dataworks.ap-northeast-1.aliyuncs.com',
            'ap-south-1': 'dataworks.ap-south-1.aliyuncs.com',
            'ap-southeast-1': 'dataworks.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dataworks.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dataworks.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dataworks.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dataworks.cn-beijing.aliyuncs.com',
            'cn-chengdu': 'dataworks.cn-chengdu.aliyuncs.com',
            'cn-hangzhou': 'dataworks.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dataworks.cn-hongkong.aliyuncs.com',
            'cn-huhehaote': 'dataworks.aliyuncs.com',
            'cn-qingdao': 'dataworks.aliyuncs.com',
            'cn-shanghai': 'dataworks.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'dataworks.cn-shenzhen.aliyuncs.com',
            'cn-zhangjiakou': 'dataworks.aliyuncs.com',
            'eu-central-1': 'dataworks.eu-central-1.aliyuncs.com',
            'eu-west-1': 'dataworks.eu-west-1.aliyuncs.com',
            'me-east-1': 'dataworks.me-east-1.aliyuncs.com',
            'us-east-1': 'dataworks.us-east-1.aliyuncs.com',
            'us-west-1': 'dataworks.us-west-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dataworks.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dataworks.aliyuncs.com',
            'cn-shanghai-finance-1': 'dataworks.aliyuncs.com',
            'cn-north-2-gov-1': 'dataworks.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dataworks-public', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.AbolishDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AbolishDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AbolishDataServiceApiResponse(),
            self.do_rpcrequest('AbolishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def abolish_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.AbolishDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AbolishDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AbolishDataServiceApiResponse(),
            await self.do_rpcrequest_async('AbolishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abolish_data_service_api(
        self,
        request: dataworks_public_20200518_models.AbolishDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.AbolishDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_data_service_api_with_options(request, runtime)

    async def abolish_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.AbolishDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.AbolishDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_data_service_api_with_options_async(request, runtime)

    def add_project_member_to_role_with_options(
        self,
        request: dataworks_public_20200518_models.AddProjectMemberToRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AddProjectMemberToRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddProjectMemberToRoleResponse(),
            self.do_rpcrequest('AddProjectMemberToRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_project_member_to_role_with_options_async(
        self,
        request: dataworks_public_20200518_models.AddProjectMemberToRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AddProjectMemberToRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddProjectMemberToRoleResponse(),
            await self.do_rpcrequest_async('AddProjectMemberToRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_project_member_to_role(
        self,
        request: dataworks_public_20200518_models.AddProjectMemberToRoleRequest,
    ) -> dataworks_public_20200518_models.AddProjectMemberToRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_project_member_to_role_with_options(request, runtime)

    async def add_project_member_to_role_async(
        self,
        request: dataworks_public_20200518_models.AddProjectMemberToRoleRequest,
    ) -> dataworks_public_20200518_models.AddProjectMemberToRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_project_member_to_role_with_options_async(request, runtime)

    def add_to_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.AddToMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AddToMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddToMetaCategoryResponse(),
            self.do_rpcrequest('AddToMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_to_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.AddToMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.AddToMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.AddToMetaCategoryResponse(),
            await self.do_rpcrequest_async('AddToMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_to_meta_category(
        self,
        request: dataworks_public_20200518_models.AddToMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.AddToMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_to_meta_category_with_options(request, runtime)

    async def add_to_meta_category_async(
        self,
        request: dataworks_public_20200518_models.AddToMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.AddToMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_to_meta_category_with_options_async(request, runtime)

    def approve_permission_apply_order_with_options(
        self,
        request: dataworks_public_20200518_models.ApprovePermissionApplyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse(),
            self.do_rpcrequest('ApprovePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def approve_permission_apply_order_with_options_async(
        self,
        request: dataworks_public_20200518_models.ApprovePermissionApplyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse(),
            await self.do_rpcrequest_async('ApprovePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def approve_permission_apply_order(
        self,
        request: dataworks_public_20200518_models.ApprovePermissionApplyOrderRequest,
    ) -> dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.approve_permission_apply_order_with_options(request, runtime)

    async def approve_permission_apply_order_async(
        self,
        request: dataworks_public_20200518_models.ApprovePermissionApplyOrderRequest,
    ) -> dataworks_public_20200518_models.ApprovePermissionApplyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_permission_apply_order_with_options_async(request, runtime)

    def check_engine_meta_partition_with_options(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckEngineMetaPartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaPartitionResponse(),
            self.do_rpcrequest('CheckEngineMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_engine_meta_partition_with_options_async(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckEngineMetaPartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaPartitionResponse(),
            await self.do_rpcrequest_async('CheckEngineMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_engine_meta_partition(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaPartitionRequest,
    ) -> dataworks_public_20200518_models.CheckEngineMetaPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_engine_meta_partition_with_options(request, runtime)

    async def check_engine_meta_partition_async(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaPartitionRequest,
    ) -> dataworks_public_20200518_models.CheckEngineMetaPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_engine_meta_partition_with_options_async(request, runtime)

    def check_engine_meta_table_with_options(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckEngineMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaTableResponse(),
            self.do_rpcrequest('CheckEngineMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_engine_meta_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckEngineMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckEngineMetaTableResponse(),
            await self.do_rpcrequest_async('CheckEngineMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_engine_meta_table(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaTableRequest,
    ) -> dataworks_public_20200518_models.CheckEngineMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_engine_meta_table_with_options(request, runtime)

    async def check_engine_meta_table_async(
        self,
        request: dataworks_public_20200518_models.CheckEngineMetaTableRequest,
    ) -> dataworks_public_20200518_models.CheckEngineMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_engine_meta_table_with_options_async(request, runtime)

    def check_file_deployment_with_options(
        self,
        request: dataworks_public_20200518_models.CheckFileDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckFileDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckFileDeploymentResponse(),
            self.do_rpcrequest('CheckFileDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_file_deployment_with_options_async(
        self,
        request: dataworks_public_20200518_models.CheckFileDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckFileDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckFileDeploymentResponse(),
            await self.do_rpcrequest_async('CheckFileDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_file_deployment(
        self,
        request: dataworks_public_20200518_models.CheckFileDeploymentRequest,
    ) -> dataworks_public_20200518_models.CheckFileDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_file_deployment_with_options(request, runtime)

    async def check_file_deployment_async(
        self,
        request: dataworks_public_20200518_models.CheckFileDeploymentRequest,
    ) -> dataworks_public_20200518_models.CheckFileDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_file_deployment_with_options_async(request, runtime)

    def check_meta_partition_with_options(
        self,
        request: dataworks_public_20200518_models.CheckMetaPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaPartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaPartitionResponse(),
            self.do_rpcrequest('CheckMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_meta_partition_with_options_async(
        self,
        request: dataworks_public_20200518_models.CheckMetaPartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaPartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaPartitionResponse(),
            await self.do_rpcrequest_async('CheckMetaPartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_partition(
        self,
        request: dataworks_public_20200518_models.CheckMetaPartitionRequest,
    ) -> dataworks_public_20200518_models.CheckMetaPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_meta_partition_with_options(request, runtime)

    async def check_meta_partition_async(
        self,
        request: dataworks_public_20200518_models.CheckMetaPartitionRequest,
    ) -> dataworks_public_20200518_models.CheckMetaPartitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_meta_partition_with_options_async(request, runtime)

    def check_meta_table_with_options(
        self,
        request: dataworks_public_20200518_models.CheckMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableResponse(),
            self.do_rpcrequest('CheckMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_meta_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.CheckMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableResponse(),
            await self.do_rpcrequest_async('CheckMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_table(
        self,
        request: dataworks_public_20200518_models.CheckMetaTableRequest,
    ) -> dataworks_public_20200518_models.CheckMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_with_options(request, runtime)

    async def check_meta_table_async(
        self,
        request: dataworks_public_20200518_models.CheckMetaTableRequest,
    ) -> dataworks_public_20200518_models.CheckMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_meta_table_with_options_async(request, runtime)

    def check_meta_table_task_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaTableTaskResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableTaskResponse(),
            self.do_rpcrequest('CheckMetaTableTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_meta_table_task_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CheckMetaTableTaskResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            dataworks_public_20200518_models.CheckMetaTableTaskResponse(),
            await self.do_rpcrequest_async('CheckMetaTableTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_meta_table_task(self) -> dataworks_public_20200518_models.CheckMetaTableTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_meta_table_task_with_options(runtime)

    async def check_meta_table_task_async(self) -> dataworks_public_20200518_models.CheckMetaTableTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_meta_table_task_with_options_async(runtime)

    def create_business_with_options(
        self,
        request: dataworks_public_20200518_models.CreateBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateBusinessResponse(),
            self.do_rpcrequest('CreateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateBusinessResponse(),
            await self.do_rpcrequest_async('CreateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_business(
        self,
        request: dataworks_public_20200518_models.CreateBusinessRequest,
    ) -> dataworks_public_20200518_models.CreateBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_business_with_options(request, runtime)

    async def create_business_async(
        self,
        request: dataworks_public_20200518_models.CreateBusinessRequest,
    ) -> dataworks_public_20200518_models.CreateBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_business_with_options_async(request, runtime)

    def create_connection_with_options(
        self,
        request: dataworks_public_20200518_models.CreateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateConnectionResponse(),
            self.do_rpcrequest('CreateConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_connection_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateConnectionResponse(),
            await self.do_rpcrequest_async('CreateConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_connection(
        self,
        request: dataworks_public_20200518_models.CreateConnectionRequest,
    ) -> dataworks_public_20200518_models.CreateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_connection_with_options(request, runtime)

    async def create_connection_async(
        self,
        request: dataworks_public_20200518_models.CreateConnectionRequest,
    ) -> dataworks_public_20200518_models.CreateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_connection_with_options_async(request, runtime)

    def create_dag_complement_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDagComplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDagComplementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagComplementResponse(),
            self.do_rpcrequest('CreateDagComplement', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dag_complement_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDagComplementRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDagComplementResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagComplementResponse(),
            await self.do_rpcrequest_async('CreateDagComplement', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dag_complement(
        self,
        request: dataworks_public_20200518_models.CreateDagComplementRequest,
    ) -> dataworks_public_20200518_models.CreateDagComplementResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dag_complement_with_options(request, runtime)

    async def create_dag_complement_async(
        self,
        request: dataworks_public_20200518_models.CreateDagComplementRequest,
    ) -> dataworks_public_20200518_models.CreateDagComplementResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dag_complement_with_options_async(request, runtime)

    def create_dag_test_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDagTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDagTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagTestResponse(),
            self.do_rpcrequest('CreateDagTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dag_test_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDagTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDagTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDagTestResponse(),
            await self.do_rpcrequest_async('CreateDagTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dag_test(
        self,
        request: dataworks_public_20200518_models.CreateDagTestRequest,
    ) -> dataworks_public_20200518_models.CreateDagTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dag_test_with_options(request, runtime)

    async def create_dag_test_async(
        self,
        request: dataworks_public_20200518_models.CreateDagTestRequest,
    ) -> dataworks_public_20200518_models.CreateDagTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dag_test_with_options_async(request, runtime)

    def create_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiResponse(),
            self.do_rpcrequest('CreateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiResponse(),
            await self.do_rpcrequest_async('CreateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_api(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_with_options(request, runtime)

    async def create_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_service_api_with_options_async(request, runtime)

    def create_data_service_api_authority_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse(),
            self.do_rpcrequest('CreateDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_service_api_authority_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse(),
            await self.do_rpcrequest_async('CreateDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_api_authority(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiAuthorityRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_api_authority_with_options(request, runtime)

    async def create_data_service_api_authority_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceApiAuthorityRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceApiAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_service_api_authority_with_options_async(request, runtime)

    def create_data_service_folder_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceFolderResponse(),
            self.do_rpcrequest('CreateDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_service_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceFolderResponse(),
            await self.do_rpcrequest_async('CreateDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_folder(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceFolderRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_folder_with_options(request, runtime)

    async def create_data_service_folder_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceFolderRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_service_folder_with_options_async(request, runtime)

    def create_data_service_group_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceGroupResponse(),
            self.do_rpcrequest('CreateDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_service_group_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataServiceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataServiceGroupResponse(),
            await self.do_rpcrequest_async('CreateDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_service_group(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceGroupRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_service_group_with_options(request, runtime)

    async def create_data_service_group_async(
        self,
        request: dataworks_public_20200518_models.CreateDataServiceGroupRequest,
    ) -> dataworks_public_20200518_models.CreateDataServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_service_group_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataSourceResponse(),
            self.do_rpcrequest('CreateDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDataSourceResponse(),
            await self.do_rpcrequest_async('CreateDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_source(
        self,
        request: dataworks_public_20200518_models.CreateDataSourceRequest,
    ) -> dataworks_public_20200518_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: dataworks_public_20200518_models.CreateDataSourceRequest,
    ) -> dataworks_public_20200518_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_disync_task_with_options(
        self,
        request: dataworks_public_20200518_models.CreateDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDISyncTaskResponse(),
            self.do_rpcrequest('CreateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_disync_task_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateDISyncTaskResponse(),
            await self.do_rpcrequest_async('CreateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_disync_task(
        self,
        request: dataworks_public_20200518_models.CreateDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.CreateDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disync_task_with_options(request, runtime)

    async def create_disync_task_async(
        self,
        request: dataworks_public_20200518_models.CreateDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.CreateDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disync_task_with_options_async(request, runtime)

    def create_file_with_options(
        self,
        request: dataworks_public_20200518_models.CreateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFileResponse(),
            self.do_rpcrequest('CreateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFileResponse(),
            await self.do_rpcrequest_async('CreateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_file(
        self,
        request: dataworks_public_20200518_models.CreateFileRequest,
    ) -> dataworks_public_20200518_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_file_with_options(request, runtime)

    async def create_file_async(
        self,
        request: dataworks_public_20200518_models.CreateFileRequest,
    ) -> dataworks_public_20200518_models.CreateFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_file_with_options_async(request, runtime)

    def create_folder_with_options(
        self,
        request: dataworks_public_20200518_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFolderResponse(),
            self.do_rpcrequest('CreateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateFolderResponse(),
            await self.do_rpcrequest_async('CreateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_folder(
        self,
        request: dataworks_public_20200518_models.CreateFolderRequest,
    ) -> dataworks_public_20200518_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    async def create_folder_async(
        self,
        request: dataworks_public_20200518_models.CreateFolderRequest,
    ) -> dataworks_public_20200518_models.CreateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_folder_with_options_async(request, runtime)

    def create_import_migration_with_options(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateImportMigrationResponse(),
            self.do_rpcrequest('CreateImportMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_import_migration_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateImportMigrationResponse(),
            await self.do_rpcrequest_async('CreateImportMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_import_migration(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationRequest,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_import_migration_with_options(request, runtime)

    async def create_import_migration_async(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationRequest,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_import_migration_with_options_async(request, runtime)

    def create_import_migration_advance(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
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
        auth_config = rpc_models.Config(
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
            product='dataworks-public',
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
        create_import_migration_req = dataworks_public_20200518_models.CreateImportMigrationRequest()
        OpenApiUtilClient.convert(request, create_import_migration_req)
        if not UtilClient.is_unset(request.package_file_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.package_file_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            create_import_migration_req.package_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        create_import_migration_resp = self.create_import_migration_with_options(create_import_migration_req, runtime)
        return create_import_migration_resp

    async def create_import_migration_advance_async(
        self,
        request: dataworks_public_20200518_models.CreateImportMigrationAdvanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateImportMigrationResponse:
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
        auth_config = rpc_models.Config(
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
            product='dataworks-public',
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
        create_import_migration_req = dataworks_public_20200518_models.CreateImportMigrationRequest()
        OpenApiUtilClient.convert(request, create_import_migration_req)
        if not UtilClient.is_unset(request.package_file_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.endpoint, auth_response.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.object_key,
                content=request.package_file_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.access_key_id,
                policy=auth_response.encoded_policy,
                signature=auth_response.signature,
                key=auth_response.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            create_import_migration_req.package_file = f'http://{auth_response.bucket}.{auth_response.endpoint}/{auth_response.object_key}'
        create_import_migration_resp = await self.create_import_migration_with_options_async(create_import_migration_req, runtime)
        return create_import_migration_resp

    def create_manual_dag_with_options(
        self,
        request: dataworks_public_20200518_models.CreateManualDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateManualDagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateManualDagResponse(),
            self.do_rpcrequest('CreateManualDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_manual_dag_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateManualDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateManualDagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateManualDagResponse(),
            await self.do_rpcrequest_async('CreateManualDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_manual_dag(
        self,
        request: dataworks_public_20200518_models.CreateManualDagRequest,
    ) -> dataworks_public_20200518_models.CreateManualDagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_manual_dag_with_options(request, runtime)

    async def create_manual_dag_async(
        self,
        request: dataworks_public_20200518_models.CreateManualDagRequest,
    ) -> dataworks_public_20200518_models.CreateManualDagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_manual_dag_with_options_async(request, runtime)

    def create_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.CreateMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateMetaCategoryResponse(),
            self.do_rpcrequest('CreateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateMetaCategoryResponse(),
            await self.do_rpcrequest_async('CreateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_meta_category(
        self,
        request: dataworks_public_20200518_models.CreateMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.CreateMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_meta_category_with_options(request, runtime)

    async def create_meta_category_async(
        self,
        request: dataworks_public_20200518_models.CreateMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.CreateMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_meta_category_with_options_async(request, runtime)

    def create_permission_apply_order_with_options(
        self,
        request: dataworks_public_20200518_models.CreatePermissionApplyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreatePermissionApplyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreatePermissionApplyOrderResponse(),
            self.do_rpcrequest('CreatePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_permission_apply_order_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreatePermissionApplyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreatePermissionApplyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreatePermissionApplyOrderResponse(),
            await self.do_rpcrequest_async('CreatePermissionApplyOrder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_permission_apply_order(
        self,
        request: dataworks_public_20200518_models.CreatePermissionApplyOrderRequest,
    ) -> dataworks_public_20200518_models.CreatePermissionApplyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_permission_apply_order_with_options(request, runtime)

    async def create_permission_apply_order_async(
        self,
        request: dataworks_public_20200518_models.CreatePermissionApplyOrderRequest,
    ) -> dataworks_public_20200518_models.CreatePermissionApplyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_permission_apply_order_with_options_async(request, runtime)

    def create_project_member_with_options(
        self,
        request: dataworks_public_20200518_models.CreateProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateProjectMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateProjectMemberResponse(),
            self.do_rpcrequest('CreateProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_project_member_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateProjectMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateProjectMemberResponse(),
            await self.do_rpcrequest_async('CreateProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_member(
        self,
        request: dataworks_public_20200518_models.CreateProjectMemberRequest,
    ) -> dataworks_public_20200518_models.CreateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_project_member_with_options(request, runtime)

    async def create_project_member_async(
        self,
        request: dataworks_public_20200518_models.CreateProjectMemberRequest,
    ) -> dataworks_public_20200518_models.CreateProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_project_member_with_options_async(request, runtime)

    def create_quality_entity_with_options(
        self,
        request: dataworks_public_20200518_models.CreateQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityEntityResponse(),
            self.do_rpcrequest('CreateQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_entity_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityEntityResponse(),
            await self.do_rpcrequest_async('CreateQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_entity(
        self,
        request: dataworks_public_20200518_models.CreateQualityEntityRequest,
    ) -> dataworks_public_20200518_models.CreateQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_entity_with_options(request, runtime)

    async def create_quality_entity_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityEntityRequest,
    ) -> dataworks_public_20200518_models.CreateQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_entity_with_options_async(request, runtime)

    def create_quality_follower_with_options(
        self,
        request: dataworks_public_20200518_models.CreateQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityFollowerResponse(),
            self.do_rpcrequest('CreateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_follower_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityFollowerResponse(),
            await self.do_rpcrequest_async('CreateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_follower(
        self,
        request: dataworks_public_20200518_models.CreateQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.CreateQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_follower_with_options(request, runtime)

    async def create_quality_follower_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.CreateQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_follower_with_options_async(request, runtime)

    def create_quality_relative_node_with_options(
        self,
        request: dataworks_public_20200518_models.CreateQualityRelativeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityRelativeNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRelativeNodeResponse(),
            self.do_rpcrequest('CreateQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_relative_node_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityRelativeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityRelativeNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRelativeNodeResponse(),
            await self.do_rpcrequest_async('CreateQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_relative_node(
        self,
        request: dataworks_public_20200518_models.CreateQualityRelativeNodeRequest,
    ) -> dataworks_public_20200518_models.CreateQualityRelativeNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_relative_node_with_options(request, runtime)

    async def create_quality_relative_node_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityRelativeNodeRequest,
    ) -> dataworks_public_20200518_models.CreateQualityRelativeNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_relative_node_with_options_async(request, runtime)

    def create_quality_rule_with_options(
        self,
        request: dataworks_public_20200518_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRuleResponse(),
            self.do_rpcrequest('CreateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_quality_rule_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateQualityRuleResponse(),
            await self.do_rpcrequest_async('CreateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_quality_rule(
        self,
        request: dataworks_public_20200518_models.CreateQualityRuleRequest,
    ) -> dataworks_public_20200518_models.CreateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_quality_rule_with_options(request, runtime)

    async def create_quality_rule_async(
        self,
        request: dataworks_public_20200518_models.CreateQualityRuleRequest,
    ) -> dataworks_public_20200518_models.CreateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_rule_with_options_async(request, runtime)

    def create_remind_with_options(
        self,
        request: dataworks_public_20200518_models.CreateRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateRemindResponse(),
            self.do_rpcrequest('CreateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_remind_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateRemindResponse(),
            await self.do_rpcrequest_async('CreateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_remind(
        self,
        request: dataworks_public_20200518_models.CreateRemindRequest,
    ) -> dataworks_public_20200518_models.CreateRemindResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_remind_with_options(request, runtime)

    async def create_remind_async(
        self,
        request: dataworks_public_20200518_models.CreateRemindRequest,
    ) -> dataworks_public_20200518_models.CreateRemindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_remind_with_options_async(request, runtime)

    def create_table_with_options(
        self,
        request: dataworks_public_20200518_models.CreateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableResponse(),
            self.do_rpcrequest('CreateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableResponse(),
            await self.do_rpcrequest_async('CreateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table(
        self,
        request: dataworks_public_20200518_models.CreateTableRequest,
    ) -> dataworks_public_20200518_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_table_with_options(request, runtime)

    async def create_table_async(
        self,
        request: dataworks_public_20200518_models.CreateTableRequest,
    ) -> dataworks_public_20200518_models.CreateTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_table_with_options_async(request, runtime)

    def create_table_level_with_options(
        self,
        request: dataworks_public_20200518_models.CreateTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableLevelResponse(),
            self.do_rpcrequest('CreateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_table_level_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableLevelResponse(),
            await self.do_rpcrequest_async('CreateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table_level(
        self,
        request: dataworks_public_20200518_models.CreateTableLevelRequest,
    ) -> dataworks_public_20200518_models.CreateTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_table_level_with_options(request, runtime)

    async def create_table_level_async(
        self,
        request: dataworks_public_20200518_models.CreateTableLevelRequest,
    ) -> dataworks_public_20200518_models.CreateTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_table_level_with_options_async(request, runtime)

    def create_table_theme_with_options(
        self,
        request: dataworks_public_20200518_models.CreateTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableThemeResponse(),
            self.do_rpcrequest('CreateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_table_theme_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateTableThemeResponse(),
            await self.do_rpcrequest_async('CreateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_table_theme(
        self,
        request: dataworks_public_20200518_models.CreateTableThemeRequest,
    ) -> dataworks_public_20200518_models.CreateTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_table_theme_with_options(request, runtime)

    async def create_table_theme_async(
        self,
        request: dataworks_public_20200518_models.CreateTableThemeRequest,
    ) -> dataworks_public_20200518_models.CreateTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_table_theme_with_options_async(request, runtime)

    def create_udf_file_with_options(
        self,
        request: dataworks_public_20200518_models.CreateUdfFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateUdfFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateUdfFileResponse(),
            self.do_rpcrequest('CreateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_udf_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateUdfFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateUdfFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateUdfFileResponse(),
            await self.do_rpcrequest_async('CreateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_udf_file(
        self,
        request: dataworks_public_20200518_models.CreateUdfFileRequest,
    ) -> dataworks_public_20200518_models.CreateUdfFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_udf_file_with_options(request, runtime)

    async def create_udf_file_async(
        self,
        request: dataworks_public_20200518_models.CreateUdfFileRequest,
    ) -> dataworks_public_20200518_models.CreateUdfFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_udf_file_with_options_async(request, runtime)

    def create_view_with_options(
        self,
        request: dataworks_public_20200518_models.CreateViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateViewResponse(),
            self.do_rpcrequest('CreateView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_view_with_options_async(
        self,
        request: dataworks_public_20200518_models.CreateViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.CreateViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.CreateViewResponse(),
            await self.do_rpcrequest_async('CreateView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_view(
        self,
        request: dataworks_public_20200518_models.CreateViewRequest,
    ) -> dataworks_public_20200518_models.CreateViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_view_with_options(request, runtime)

    async def create_view_async(
        self,
        request: dataworks_public_20200518_models.CreateViewRequest,
    ) -> dataworks_public_20200518_models.CreateViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_view_with_options_async(request, runtime)

    def delete_business_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteBusinessResponse(),
            self.do_rpcrequest('DeleteBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteBusinessResponse(),
            await self.do_rpcrequest_async('DeleteBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_business(
        self,
        request: dataworks_public_20200518_models.DeleteBusinessRequest,
    ) -> dataworks_public_20200518_models.DeleteBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_business_with_options(request, runtime)

    async def delete_business_async(
        self,
        request: dataworks_public_20200518_models.DeleteBusinessRequest,
    ) -> dataworks_public_20200518_models.DeleteBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_business_with_options_async(request, runtime)

    def delete_connection_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteConnectionResponse(),
            self.do_rpcrequest('DeleteConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_connection_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteConnectionResponse(),
            await self.do_rpcrequest_async('DeleteConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_connection(
        self,
        request: dataworks_public_20200518_models.DeleteConnectionRequest,
    ) -> dataworks_public_20200518_models.DeleteConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_connection_with_options(request, runtime)

    async def delete_connection_async(
        self,
        request: dataworks_public_20200518_models.DeleteConnectionRequest,
    ) -> dataworks_public_20200518_models.DeleteConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_connection_with_options_async(request, runtime)

    def delete_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiResponse(),
            self.do_rpcrequest('DeleteDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiResponse(),
            await self.do_rpcrequest_async('DeleteDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_service_api(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_with_options(request, runtime)

    async def delete_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_service_api_with_options_async(request, runtime)

    def delete_data_service_api_authority_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse(),
            self.do_rpcrequest('DeleteDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_service_api_authority_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse(),
            await self.do_rpcrequest_async('DeleteDataServiceApiAuthority', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_service_api_authority(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiAuthorityRequest,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_service_api_authority_with_options(request, runtime)

    async def delete_data_service_api_authority_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataServiceApiAuthorityRequest,
    ) -> dataworks_public_20200518_models.DeleteDataServiceApiAuthorityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_service_api_authority_with_options_async(request, runtime)

    def delete_data_source_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataSourceResponse(),
            self.do_rpcrequest('DeleteDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_source_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDataSourceResponse(),
            await self.do_rpcrequest_async('DeleteDataSource', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_data_source(
        self,
        request: dataworks_public_20200518_models.DeleteDataSourceRequest,
    ) -> dataworks_public_20200518_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    async def delete_data_source_async(
        self,
        request: dataworks_public_20200518_models.DeleteDataSourceRequest,
    ) -> dataworks_public_20200518_models.DeleteDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_source_with_options_async(request, runtime)

    def delete_disync_task_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDISyncTaskResponse(),
            self.do_rpcrequest('DeleteDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_disync_task_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteDISyncTaskResponse(),
            await self.do_rpcrequest_async('DeleteDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_disync_task(
        self,
        request: dataworks_public_20200518_models.DeleteDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.DeleteDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_disync_task_with_options(request, runtime)

    async def delete_disync_task_async(
        self,
        request: dataworks_public_20200518_models.DeleteDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.DeleteDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_disync_task_with_options_async(request, runtime)

    def delete_file_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFileResponse(),
            self.do_rpcrequest('DeleteFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFileResponse(),
            await self.do_rpcrequest_async('DeleteFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_file(
        self,
        request: dataworks_public_20200518_models.DeleteFileRequest,
    ) -> dataworks_public_20200518_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_file_with_options(request, runtime)

    async def delete_file_async(
        self,
        request: dataworks_public_20200518_models.DeleteFileRequest,
    ) -> dataworks_public_20200518_models.DeleteFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_file_with_options_async(request, runtime)

    def delete_folder_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFolderResponse(),
            self.do_rpcrequest('DeleteFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFolderResponse(),
            await self.do_rpcrequest_async('DeleteFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_folder(
        self,
        request: dataworks_public_20200518_models.DeleteFolderRequest,
    ) -> dataworks_public_20200518_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    async def delete_folder_async(
        self,
        request: dataworks_public_20200518_models.DeleteFolderRequest,
    ) -> dataworks_public_20200518_models.DeleteFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_folder_with_options_async(request, runtime)

    def delete_from_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteFromMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFromMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFromMetaCategoryResponse(),
            self.do_rpcrequest('DeleteFromMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_from_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteFromMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteFromMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteFromMetaCategoryResponse(),
            await self.do_rpcrequest_async('DeleteFromMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_from_meta_category(
        self,
        request: dataworks_public_20200518_models.DeleteFromMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.DeleteFromMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_from_meta_category_with_options(request, runtime)

    async def delete_from_meta_category_async(
        self,
        request: dataworks_public_20200518_models.DeleteFromMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.DeleteFromMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_from_meta_category_with_options_async(request, runtime)

    def delete_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteMetaCategoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCategoryResponse(),
            self.do_rpcrequest('DeleteMetaCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def delete_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteMetaCategoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteMetaCategoryResponse(),
            await self.do_rpcrequest_async('DeleteMetaCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_meta_category(
        self,
        request: dataworks_public_20200518_models.DeleteMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.DeleteMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_meta_category_with_options(request, runtime)

    async def delete_meta_category_async(
        self,
        request: dataworks_public_20200518_models.DeleteMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.DeleteMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_meta_category_with_options_async(request, runtime)

    def delete_project_member_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteProjectMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteProjectMemberResponse(),
            self.do_rpcrequest('DeleteProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_project_member_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteProjectMemberRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteProjectMemberResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteProjectMemberResponse(),
            await self.do_rpcrequest_async('DeleteProjectMember', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_member(
        self,
        request: dataworks_public_20200518_models.DeleteProjectMemberRequest,
    ) -> dataworks_public_20200518_models.DeleteProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_project_member_with_options(request, runtime)

    async def delete_project_member_async(
        self,
        request: dataworks_public_20200518_models.DeleteProjectMemberRequest,
    ) -> dataworks_public_20200518_models.DeleteProjectMemberResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_project_member_with_options_async(request, runtime)

    def delete_quality_entity_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityEntityResponse(),
            self.do_rpcrequest('DeleteQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_entity_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityEntityResponse(),
            await self.do_rpcrequest_async('DeleteQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_entity(
        self,
        request: dataworks_public_20200518_models.DeleteQualityEntityRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_entity_with_options(request, runtime)

    async def delete_quality_entity_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityEntityRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_entity_with_options_async(request, runtime)

    def delete_quality_follower_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityFollowerResponse(),
            self.do_rpcrequest('DeleteQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_follower_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityFollowerResponse(),
            await self.do_rpcrequest_async('DeleteQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_follower(
        self,
        request: dataworks_public_20200518_models.DeleteQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_follower_with_options(request, runtime)

    async def delete_quality_follower_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_follower_with_options_async(request, runtime)

    def delete_quality_relative_node_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRelativeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse(),
            self.do_rpcrequest('DeleteQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_relative_node_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRelativeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse(),
            await self.do_rpcrequest_async('DeleteQualityRelativeNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_relative_node(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRelativeNodeRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_relative_node_with_options(request, runtime)

    async def delete_quality_relative_node_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRelativeNodeRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityRelativeNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_relative_node_with_options_async(request, runtime)

    def delete_quality_rule_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRuleResponse(),
            self.do_rpcrequest('DeleteQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_quality_rule_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteQualityRuleResponse(),
            await self.do_rpcrequest_async('DeleteQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_quality_rule(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRuleRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_rule_with_options(request, runtime)

    async def delete_quality_rule_async(
        self,
        request: dataworks_public_20200518_models.DeleteQualityRuleRequest,
    ) -> dataworks_public_20200518_models.DeleteQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_rule_with_options_async(request, runtime)

    def delete_remind_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteRemindResponse(),
            self.do_rpcrequest('DeleteRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_remind_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteRemindResponse(),
            await self.do_rpcrequest_async('DeleteRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_remind(
        self,
        request: dataworks_public_20200518_models.DeleteRemindRequest,
    ) -> dataworks_public_20200518_models.DeleteRemindResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_remind_with_options(request, runtime)

    async def delete_remind_async(
        self,
        request: dataworks_public_20200518_models.DeleteRemindRequest,
    ) -> dataworks_public_20200518_models.DeleteRemindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_remind_with_options_async(request, runtime)

    def delete_table_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableResponse(),
            self.do_rpcrequest('DeleteTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableResponse(),
            await self.do_rpcrequest_async('DeleteTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table(
        self,
        request: dataworks_public_20200518_models.DeleteTableRequest,
    ) -> dataworks_public_20200518_models.DeleteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_table_with_options(request, runtime)

    async def delete_table_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableRequest,
    ) -> dataworks_public_20200518_models.DeleteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_table_with_options_async(request, runtime)

    def delete_table_level_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableLevelResponse(),
            self.do_rpcrequest('DeleteTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_table_level_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableLevelResponse(),
            await self.do_rpcrequest_async('DeleteTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table_level(
        self,
        request: dataworks_public_20200518_models.DeleteTableLevelRequest,
    ) -> dataworks_public_20200518_models.DeleteTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_table_level_with_options(request, runtime)

    async def delete_table_level_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableLevelRequest,
    ) -> dataworks_public_20200518_models.DeleteTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_table_level_with_options_async(request, runtime)

    def delete_table_theme_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableThemeResponse(),
            self.do_rpcrequest('DeleteTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_table_theme_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteTableThemeResponse(),
            await self.do_rpcrequest_async('DeleteTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_table_theme(
        self,
        request: dataworks_public_20200518_models.DeleteTableThemeRequest,
    ) -> dataworks_public_20200518_models.DeleteTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_table_theme_with_options(request, runtime)

    async def delete_table_theme_async(
        self,
        request: dataworks_public_20200518_models.DeleteTableThemeRequest,
    ) -> dataworks_public_20200518_models.DeleteTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_table_theme_with_options_async(request, runtime)

    def delete_view_with_options(
        self,
        request: dataworks_public_20200518_models.DeleteViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteViewResponse(),
            self.do_rpcrequest('DeleteView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_view_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeleteViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeleteViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeleteViewResponse(),
            await self.do_rpcrequest_async('DeleteView', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_view(
        self,
        request: dataworks_public_20200518_models.DeleteViewRequest,
    ) -> dataworks_public_20200518_models.DeleteViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_view_with_options(request, runtime)

    async def delete_view_async(
        self,
        request: dataworks_public_20200518_models.DeleteViewRequest,
    ) -> dataworks_public_20200518_models.DeleteViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_view_with_options_async(request, runtime)

    def deploy_disync_task_with_options(
        self,
        request: dataworks_public_20200518_models.DeployDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeployDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployDISyncTaskResponse(),
            self.do_rpcrequest('DeployDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_disync_task_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeployDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeployDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployDISyncTaskResponse(),
            await self.do_rpcrequest_async('DeployDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_disync_task(
        self,
        request: dataworks_public_20200518_models.DeployDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.DeployDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_disync_task_with_options(request, runtime)

    async def deploy_disync_task_async(
        self,
        request: dataworks_public_20200518_models.DeployDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.DeployDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_disync_task_with_options_async(request, runtime)

    def deploy_file_with_options(
        self,
        request: dataworks_public_20200518_models.DeployFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeployFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployFileResponse(),
            self.do_rpcrequest('DeployFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.DeployFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DeployFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DeployFileResponse(),
            await self.do_rpcrequest_async('DeployFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_file(
        self,
        request: dataworks_public_20200518_models.DeployFileRequest,
    ) -> dataworks_public_20200518_models.DeployFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_file_with_options(request, runtime)

    async def deploy_file_async(
        self,
        request: dataworks_public_20200518_models.DeployFileRequest,
    ) -> dataworks_public_20200518_models.DeployFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_file_with_options_async(request, runtime)

    def desensitize_data_with_options(
        self,
        request: dataworks_public_20200518_models.DesensitizeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DesensitizeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DesensitizeDataResponse(),
            self.do_rpcrequest('DesensitizeData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def desensitize_data_with_options_async(
        self,
        request: dataworks_public_20200518_models.DesensitizeDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.DesensitizeDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.DesensitizeDataResponse(),
            await self.do_rpcrequest_async('DesensitizeData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def desensitize_data(
        self,
        request: dataworks_public_20200518_models.DesensitizeDataRequest,
    ) -> dataworks_public_20200518_models.DesensitizeDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.desensitize_data_with_options(request, runtime)

    async def desensitize_data_async(
        self,
        request: dataworks_public_20200518_models.DesensitizeDataRequest,
    ) -> dataworks_public_20200518_models.DesensitizeDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.desensitize_data_with_options_async(request, runtime)

    def establish_relation_table_to_business_with_options(
        self,
        request: dataworks_public_20200518_models.EstablishRelationTableToBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse(),
            self.do_rpcrequest('EstablishRelationTableToBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def establish_relation_table_to_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.EstablishRelationTableToBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse(),
            await self.do_rpcrequest_async('EstablishRelationTableToBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def establish_relation_table_to_business(
        self,
        request: dataworks_public_20200518_models.EstablishRelationTableToBusinessRequest,
    ) -> dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.establish_relation_table_to_business_with_options(request, runtime)

    async def establish_relation_table_to_business_async(
        self,
        request: dataworks_public_20200518_models.EstablishRelationTableToBusinessRequest,
    ) -> dataworks_public_20200518_models.EstablishRelationTableToBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.establish_relation_table_to_business_with_options_async(request, runtime)

    def export_connections_with_options(
        self,
        request: dataworks_public_20200518_models.ExportConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportConnectionsResponse(),
            self.do_rpcrequest('ExportConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def export_connections_with_options_async(
        self,
        request: dataworks_public_20200518_models.ExportConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportConnectionsResponse(),
            await self.do_rpcrequest_async('ExportConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def export_connections(
        self,
        request: dataworks_public_20200518_models.ExportConnectionsRequest,
    ) -> dataworks_public_20200518_models.ExportConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_connections_with_options(request, runtime)

    async def export_connections_async(
        self,
        request: dataworks_public_20200518_models.ExportConnectionsRequest,
    ) -> dataworks_public_20200518_models.ExportConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_connections_with_options_async(request, runtime)

    def export_data_sources_with_options(
        self,
        request: dataworks_public_20200518_models.ExportDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportDataSourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDataSourcesResponse(),
            self.do_rpcrequest('ExportDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def export_data_sources_with_options_async(
        self,
        request: dataworks_public_20200518_models.ExportDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportDataSourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDataSourcesResponse(),
            await self.do_rpcrequest_async('ExportDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def export_data_sources(
        self,
        request: dataworks_public_20200518_models.ExportDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ExportDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_data_sources_with_options(request, runtime)

    async def export_data_sources_async(
        self,
        request: dataworks_public_20200518_models.ExportDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ExportDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_data_sources_with_options_async(request, runtime)

    def export_disync_tasks_with_options(
        self,
        request: dataworks_public_20200518_models.ExportDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDISyncTasksResponse(),
            self.do_rpcrequest('ExportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_disync_tasks_with_options_async(
        self,
        request: dataworks_public_20200518_models.ExportDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ExportDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ExportDISyncTasksResponse(),
            await self.do_rpcrequest_async('ExportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_disync_tasks(
        self,
        request: dataworks_public_20200518_models.ExportDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ExportDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_disync_tasks_with_options(request, runtime)

    async def export_disync_tasks_async(
        self,
        request: dataworks_public_20200518_models.ExportDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ExportDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_disync_tasks_with_options_async(request, runtime)

    def generate_disync_task_config_for_creating_with_options(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse(),
            self.do_rpcrequest('GenerateDISyncTaskConfigForCreating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_disync_task_config_for_creating_with_options_async(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse(),
            await self.do_rpcrequest_async('GenerateDISyncTaskConfigForCreating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_disync_task_config_for_creating(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingRequest,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_creating_with_options(request, runtime)

    async def generate_disync_task_config_for_creating_async(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingRequest,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForCreatingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_disync_task_config_for_creating_with_options_async(request, runtime)

    def generate_disync_task_config_for_updating_with_options(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse(),
            self.do_rpcrequest('GenerateDISyncTaskConfigForUpdating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def generate_disync_task_config_for_updating_with_options_async(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse(),
            await self.do_rpcrequest_async('GenerateDISyncTaskConfigForUpdating', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_disync_task_config_for_updating(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingRequest,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse:
        runtime = util_models.RuntimeOptions()
        return self.generate_disync_task_config_for_updating_with_options(request, runtime)

    async def generate_disync_task_config_for_updating_async(
        self,
        request: dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingRequest,
    ) -> dataworks_public_20200518_models.GenerateDISyncTaskConfigForUpdatingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.generate_disync_task_config_for_updating_with_options_async(request, runtime)

    def get_baseline_config_with_options(
        self,
        request: dataworks_public_20200518_models.GetBaselineConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineConfigResponse(),
            self.do_rpcrequest('GetBaselineConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_baseline_config_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineConfigResponse(),
            await self.do_rpcrequest_async('GetBaselineConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_config(
        self,
        request: dataworks_public_20200518_models.GetBaselineConfigRequest,
    ) -> dataworks_public_20200518_models.GetBaselineConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_config_with_options(request, runtime)

    async def get_baseline_config_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineConfigRequest,
    ) -> dataworks_public_20200518_models.GetBaselineConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_baseline_config_with_options_async(request, runtime)

    def get_baseline_key_path_with_options(
        self,
        request: dataworks_public_20200518_models.GetBaselineKeyPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineKeyPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineKeyPathResponse(),
            self.do_rpcrequest('GetBaselineKeyPath', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_baseline_key_path_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineKeyPathRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineKeyPathResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineKeyPathResponse(),
            await self.do_rpcrequest_async('GetBaselineKeyPath', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_key_path(
        self,
        request: dataworks_public_20200518_models.GetBaselineKeyPathRequest,
    ) -> dataworks_public_20200518_models.GetBaselineKeyPathResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_key_path_with_options(request, runtime)

    async def get_baseline_key_path_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineKeyPathRequest,
    ) -> dataworks_public_20200518_models.GetBaselineKeyPathResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_baseline_key_path_with_options_async(request, runtime)

    def get_baseline_status_with_options(
        self,
        request: dataworks_public_20200518_models.GetBaselineStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineStatusResponse(),
            self.do_rpcrequest('GetBaselineStatus', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_baseline_status_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBaselineStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBaselineStatusResponse(),
            await self.do_rpcrequest_async('GetBaselineStatus', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_baseline_status(
        self,
        request: dataworks_public_20200518_models.GetBaselineStatusRequest,
    ) -> dataworks_public_20200518_models.GetBaselineStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_baseline_status_with_options(request, runtime)

    async def get_baseline_status_async(
        self,
        request: dataworks_public_20200518_models.GetBaselineStatusRequest,
    ) -> dataworks_public_20200518_models.GetBaselineStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_baseline_status_with_options_async(request, runtime)

    def get_business_with_options(
        self,
        request: dataworks_public_20200518_models.GetBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBusinessResponse(),
            self.do_rpcrequest('GetBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetBusinessResponse(),
            await self.do_rpcrequest_async('GetBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_business(
        self,
        request: dataworks_public_20200518_models.GetBusinessRequest,
    ) -> dataworks_public_20200518_models.GetBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_business_with_options(request, runtime)

    async def get_business_async(
        self,
        request: dataworks_public_20200518_models.GetBusinessRequest,
    ) -> dataworks_public_20200518_models.GetBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_with_options_async(request, runtime)

    def get_connection_meta_with_options(
        self,
        request: dataworks_public_20200518_models.GetConnectionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetConnectionMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetConnectionMetaResponse(),
            self.do_rpcrequest('GetConnectionMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_connection_meta_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetConnectionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetConnectionMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetConnectionMetaResponse(),
            await self.do_rpcrequest_async('GetConnectionMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_connection_meta(
        self,
        request: dataworks_public_20200518_models.GetConnectionMetaRequest,
    ) -> dataworks_public_20200518_models.GetConnectionMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_connection_meta_with_options(request, runtime)

    async def get_connection_meta_async(
        self,
        request: dataworks_public_20200518_models.GetConnectionMetaRequest,
    ) -> dataworks_public_20200518_models.GetConnectionMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_connection_meta_with_options_async(request, runtime)

    def get_dag_with_options(
        self,
        request: dataworks_public_20200518_models.GetDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDagResponse(),
            self.do_rpcrequest('GetDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dag_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDagResponse(),
            await self.do_rpcrequest_async('GetDag', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dag(
        self,
        request: dataworks_public_20200518_models.GetDagRequest,
    ) -> dataworks_public_20200518_models.GetDagResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dag_with_options(request, runtime)

    async def get_dag_async(
        self,
        request: dataworks_public_20200518_models.GetDagRequest,
    ) -> dataworks_public_20200518_models.GetDagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dag_with_options_async(request, runtime)

    def get_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApiResponse(),
            self.do_rpcrequest('GetDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApiResponse(),
            await self.do_rpcrequest_async('GetDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_api(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_api_with_options(request, runtime)

    async def get_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_api_with_options_async(request, runtime)

    def get_data_service_application_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApplicationResponse(),
            self.do_rpcrequest('GetDataServiceApplication', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_service_application_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceApplicationResponse(),
            await self.do_rpcrequest_async('GetDataServiceApplication', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_application(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApplicationRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_application_with_options(request, runtime)

    async def get_data_service_application_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceApplicationRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_application_with_options_async(request, runtime)

    def get_data_service_folder_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataServiceFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceFolderResponse(),
            self.do_rpcrequest('GetDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_service_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceFolderResponse(),
            await self.do_rpcrequest_async('GetDataServiceFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_folder(
        self,
        request: dataworks_public_20200518_models.GetDataServiceFolderRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_folder_with_options(request, runtime)

    async def get_data_service_folder_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceFolderRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_folder_with_options_async(request, runtime)

    def get_data_service_group_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataServiceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceGroupResponse(),
            self.do_rpcrequest('GetDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_service_group_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServiceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServiceGroupResponse(),
            await self.do_rpcrequest_async('GetDataServiceGroup', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_group(
        self,
        request: dataworks_public_20200518_models.GetDataServiceGroupRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_group_with_options(request, runtime)

    async def get_data_service_group_async(
        self,
        request: dataworks_public_20200518_models.GetDataServiceGroupRequest,
    ) -> dataworks_public_20200518_models.GetDataServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_group_with_options_async(request, runtime)

    def get_data_service_published_api_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataServicePublishedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServicePublishedApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServicePublishedApiResponse(),
            self.do_rpcrequest('GetDataServicePublishedApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_service_published_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataServicePublishedApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataServicePublishedApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataServicePublishedApiResponse(),
            await self.do_rpcrequest_async('GetDataServicePublishedApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_service_published_api(
        self,
        request: dataworks_public_20200518_models.GetDataServicePublishedApiRequest,
    ) -> dataworks_public_20200518_models.GetDataServicePublishedApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_service_published_api_with_options(request, runtime)

    async def get_data_service_published_api_async(
        self,
        request: dataworks_public_20200518_models.GetDataServicePublishedApiRequest,
    ) -> dataworks_public_20200518_models.GetDataServicePublishedApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_service_published_api_with_options_async(request, runtime)

    def get_data_source_meta_with_options(
        self,
        request: dataworks_public_20200518_models.GetDataSourceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataSourceMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataSourceMetaResponse(),
            self.do_rpcrequest('GetDataSourceMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_data_source_meta_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDataSourceMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDataSourceMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDataSourceMetaResponse(),
            await self.do_rpcrequest_async('GetDataSourceMeta', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_data_source_meta(
        self,
        request: dataworks_public_20200518_models.GetDataSourceMetaRequest,
    ) -> dataworks_public_20200518_models.GetDataSourceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_meta_with_options(request, runtime)

    async def get_data_source_meta_async(
        self,
        request: dataworks_public_20200518_models.GetDataSourceMetaRequest,
    ) -> dataworks_public_20200518_models.GetDataSourceMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_data_source_meta_with_options_async(request, runtime)

    def get_ddljob_status_with_options(
        self,
        request: dataworks_public_20200518_models.GetDDLJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDDLJobStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDDLJobStatusResponse(),
            self.do_rpcrequest('GetDDLJobStatus', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_ddljob_status_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDDLJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDDLJobStatusResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDDLJobStatusResponse(),
            await self.do_rpcrequest_async('GetDDLJobStatus', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ddljob_status(
        self,
        request: dataworks_public_20200518_models.GetDDLJobStatusRequest,
    ) -> dataworks_public_20200518_models.GetDDLJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ddljob_status_with_options(request, runtime)

    async def get_ddljob_status_async(
        self,
        request: dataworks_public_20200518_models.GetDDLJobStatusRequest,
    ) -> dataworks_public_20200518_models.GetDDLJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ddljob_status_with_options_async(request, runtime)

    def get_deployment_with_options(
        self,
        request: dataworks_public_20200518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDeploymentResponse(),
            self.do_rpcrequest('GetDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDeploymentResponse(),
            await self.do_rpcrequest_async('GetDeployment', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_deployment(
        self,
        request: dataworks_public_20200518_models.GetDeploymentRequest,
    ) -> dataworks_public_20200518_models.GetDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_deployment_with_options(request, runtime)

    async def get_deployment_async(
        self,
        request: dataworks_public_20200518_models.GetDeploymentRequest,
    ) -> dataworks_public_20200518_models.GetDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_deployment_with_options_async(request, runtime)

    def get_disync_instance_info_with_options(
        self,
        request: dataworks_public_20200518_models.GetDISyncInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncInstanceInfoResponse(),
            self.do_rpcrequest('GetDISyncInstanceInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_disync_instance_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncInstanceInfoResponse(),
            await self.do_rpcrequest_async('GetDISyncInstanceInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_disync_instance_info(
        self,
        request: dataworks_public_20200518_models.GetDISyncInstanceInfoRequest,
    ) -> dataworks_public_20200518_models.GetDISyncInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_disync_instance_info_with_options(request, runtime)

    async def get_disync_instance_info_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncInstanceInfoRequest,
    ) -> dataworks_public_20200518_models.GetDISyncInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_disync_instance_info_with_options_async(request, runtime)

    def get_disync_task_with_options(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskResponse(),
            self.do_rpcrequest('GetDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_disync_task_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskResponse(),
            await self.do_rpcrequest_async('GetDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_disync_task(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.GetDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_with_options(request, runtime)

    async def get_disync_task_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.GetDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_disync_task_with_options_async(request, runtime)

    def get_disync_task_metric_info_with_options(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskMetricInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse(),
            self.do_rpcrequest('GetDISyncTaskMetricInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_disync_task_metric_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskMetricInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse(),
            await self.do_rpcrequest_async('GetDISyncTaskMetricInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_disync_task_metric_info(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskMetricInfoRequest,
    ) -> dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_disync_task_metric_info_with_options(request, runtime)

    async def get_disync_task_metric_info_async(
        self,
        request: dataworks_public_20200518_models.GetDISyncTaskMetricInfoRequest,
    ) -> dataworks_public_20200518_models.GetDISyncTaskMetricInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_disync_task_metric_info_with_options_async(request, runtime)

    def get_file_with_options(
        self,
        request: dataworks_public_20200518_models.GetFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileResponse(),
            self.do_rpcrequest('GetFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileResponse(),
            await self.do_rpcrequest_async('GetFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file(
        self,
        request: dataworks_public_20200518_models.GetFileRequest,
    ) -> dataworks_public_20200518_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_with_options(request, runtime)

    async def get_file_async(
        self,
        request: dataworks_public_20200518_models.GetFileRequest,
    ) -> dataworks_public_20200518_models.GetFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_with_options_async(request, runtime)

    def get_file_type_statistic_with_options(
        self,
        request: dataworks_public_20200518_models.GetFileTypeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileTypeStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileTypeStatisticResponse(),
            self.do_rpcrequest('GetFileTypeStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_file_type_statistic_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetFileTypeStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileTypeStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileTypeStatisticResponse(),
            await self.do_rpcrequest_async('GetFileTypeStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_type_statistic(
        self,
        request: dataworks_public_20200518_models.GetFileTypeStatisticRequest,
    ) -> dataworks_public_20200518_models.GetFileTypeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_type_statistic_with_options(request, runtime)

    async def get_file_type_statistic_async(
        self,
        request: dataworks_public_20200518_models.GetFileTypeStatisticRequest,
    ) -> dataworks_public_20200518_models.GetFileTypeStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_type_statistic_with_options_async(request, runtime)

    def get_file_version_with_options(
        self,
        request: dataworks_public_20200518_models.GetFileVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileVersionResponse(),
            self.do_rpcrequest('GetFileVersion', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_file_version_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetFileVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFileVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFileVersionResponse(),
            await self.do_rpcrequest_async('GetFileVersion', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_file_version(
        self,
        request: dataworks_public_20200518_models.GetFileVersionRequest,
    ) -> dataworks_public_20200518_models.GetFileVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_file_version_with_options(request, runtime)

    async def get_file_version_async(
        self,
        request: dataworks_public_20200518_models.GetFileVersionRequest,
    ) -> dataworks_public_20200518_models.GetFileVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_file_version_with_options_async(request, runtime)

    def get_folder_with_options(
        self,
        request: dataworks_public_20200518_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFolderResponse(),
            self.do_rpcrequest('GetFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetFolderResponse(),
            await self.do_rpcrequest_async('GetFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_folder(
        self,
        request: dataworks_public_20200518_models.GetFolderRequest,
    ) -> dataworks_public_20200518_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    async def get_folder_async(
        self,
        request: dataworks_public_20200518_models.GetFolderRequest,
    ) -> dataworks_public_20200518_models.GetFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_folder_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceResponse(),
            self.do_rpcrequest('GetInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceResponse(),
            await self.do_rpcrequest_async('GetInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance(
        self,
        request: dataworks_public_20200518_models.GetInstanceRequest,
    ) -> dataworks_public_20200518_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceRequest,
    ) -> dataworks_public_20200518_models.GetInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_consume_time_rank_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceConsumeTimeRankRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse(),
            self.do_rpcrequest('GetInstanceConsumeTimeRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_consume_time_rank_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceConsumeTimeRankRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse(),
            await self.do_rpcrequest_async('GetInstanceConsumeTimeRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_consume_time_rank(
        self,
        request: dataworks_public_20200518_models.GetInstanceConsumeTimeRankRequest,
    ) -> dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_consume_time_rank_with_options(request, runtime)

    async def get_instance_consume_time_rank_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceConsumeTimeRankRequest,
    ) -> dataworks_public_20200518_models.GetInstanceConsumeTimeRankResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_consume_time_rank_with_options_async(request, runtime)

    def get_instance_count_trend_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceCountTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceCountTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceCountTrendResponse(),
            self.do_rpcrequest('GetInstanceCountTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_count_trend_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceCountTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceCountTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceCountTrendResponse(),
            await self.do_rpcrequest_async('GetInstanceCountTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_count_trend(
        self,
        request: dataworks_public_20200518_models.GetInstanceCountTrendRequest,
    ) -> dataworks_public_20200518_models.GetInstanceCountTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_count_trend_with_options(request, runtime)

    async def get_instance_count_trend_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceCountTrendRequest,
    ) -> dataworks_public_20200518_models.GetInstanceCountTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_count_trend_with_options_async(request, runtime)

    def get_instance_error_rank_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceErrorRankRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceErrorRankResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceErrorRankResponse(),
            self.do_rpcrequest('GetInstanceErrorRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_error_rank_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceErrorRankRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceErrorRankResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceErrorRankResponse(),
            await self.do_rpcrequest_async('GetInstanceErrorRank', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_error_rank(
        self,
        request: dataworks_public_20200518_models.GetInstanceErrorRankRequest,
    ) -> dataworks_public_20200518_models.GetInstanceErrorRankResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_error_rank_with_options(request, runtime)

    async def get_instance_error_rank_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceErrorRankRequest,
    ) -> dataworks_public_20200518_models.GetInstanceErrorRankResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_error_rank_with_options_async(request, runtime)

    def get_instance_log_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceLogResponse(),
            self.do_rpcrequest('GetInstanceLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_log_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceLogResponse(),
            await self.do_rpcrequest_async('GetInstanceLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_log(
        self,
        request: dataworks_public_20200518_models.GetInstanceLogRequest,
    ) -> dataworks_public_20200518_models.GetInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_log_with_options(request, runtime)

    async def get_instance_log_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceLogRequest,
    ) -> dataworks_public_20200518_models.GetInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_log_with_options_async(request, runtime)

    def get_instance_status_count_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceStatusCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusCountResponse(),
            self.do_rpcrequest('GetInstanceStatusCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_status_count_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceStatusCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusCountResponse(),
            await self.do_rpcrequest_async('GetInstanceStatusCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_status_count(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusCountRequest,
    ) -> dataworks_public_20200518_models.GetInstanceStatusCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_count_with_options(request, runtime)

    async def get_instance_status_count_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusCountRequest,
    ) -> dataworks_public_20200518_models.GetInstanceStatusCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_status_count_with_options_async(request, runtime)

    def get_instance_status_statistic_with_options(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceStatusStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusStatisticResponse(),
            self.do_rpcrequest('GetInstanceStatusStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_status_statistic_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusStatisticRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetInstanceStatusStatisticResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetInstanceStatusStatisticResponse(),
            await self.do_rpcrequest_async('GetInstanceStatusStatistic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_status_statistic(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusStatisticRequest,
    ) -> dataworks_public_20200518_models.GetInstanceStatusStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_status_statistic_with_options(request, runtime)

    async def get_instance_status_statistic_async(
        self,
        request: dataworks_public_20200518_models.GetInstanceStatusStatisticRequest,
    ) -> dataworks_public_20200518_models.GetInstanceStatusStatisticResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_status_statistic_with_options_async(request, runtime)

    def get_manual_dag_instances_with_options(
        self,
        request: dataworks_public_20200518_models.GetManualDagInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetManualDagInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetManualDagInstancesResponse(),
            self.do_rpcrequest('GetManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_manual_dag_instances_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetManualDagInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetManualDagInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetManualDagInstancesResponse(),
            await self.do_rpcrequest_async('GetManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_manual_dag_instances(
        self,
        request: dataworks_public_20200518_models.GetManualDagInstancesRequest,
    ) -> dataworks_public_20200518_models.GetManualDagInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_manual_dag_instances_with_options(request, runtime)

    async def get_manual_dag_instances_async(
        self,
        request: dataworks_public_20200518_models.GetManualDagInstancesRequest,
    ) -> dataworks_public_20200518_models.GetManualDagInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_manual_dag_instances_with_options_async(request, runtime)

    def get_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaCategoryResponse(),
            self.do_rpcrequest('GetMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaCategoryResponse(),
            await self.do_rpcrequest_async('GetMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_category(
        self,
        request: dataworks_public_20200518_models.GetMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.GetMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_category_with_options(request, runtime)

    async def get_meta_category_async(
        self,
        request: dataworks_public_20200518_models.GetMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.GetMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_category_with_options_async(request, runtime)

    def get_meta_column_lineage_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaColumnLineageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaColumnLineageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaColumnLineageResponse(),
            self.do_rpcrequest('GetMetaColumnLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_column_lineage_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaColumnLineageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaColumnLineageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaColumnLineageResponse(),
            await self.do_rpcrequest_async('GetMetaColumnLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_column_lineage(
        self,
        request: dataworks_public_20200518_models.GetMetaColumnLineageRequest,
    ) -> dataworks_public_20200518_models.GetMetaColumnLineageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_column_lineage_with_options(request, runtime)

    async def get_meta_column_lineage_async(
        self,
        request: dataworks_public_20200518_models.GetMetaColumnLineageRequest,
    ) -> dataworks_public_20200518_models.GetMetaColumnLineageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_column_lineage_with_options_async(request, runtime)

    def get_meta_dbinfo_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaDBInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaDBInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBInfoResponse(),
            self.do_rpcrequest('GetMetaDBInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_dbinfo_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaDBInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaDBInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBInfoResponse(),
            await self.do_rpcrequest_async('GetMetaDBInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_dbinfo(
        self,
        request: dataworks_public_20200518_models.GetMetaDBInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaDBInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbinfo_with_options(request, runtime)

    async def get_meta_dbinfo_async(
        self,
        request: dataworks_public_20200518_models.GetMetaDBInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaDBInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_dbinfo_with_options_async(request, runtime)

    def get_meta_dbtable_list_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaDBTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaDBTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBTableListResponse(),
            self.do_rpcrequest('GetMetaDBTableList', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_dbtable_list_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaDBTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaDBTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaDBTableListResponse(),
            await self.do_rpcrequest_async('GetMetaDBTableList', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_dbtable_list(
        self,
        request: dataworks_public_20200518_models.GetMetaDBTableListRequest,
    ) -> dataworks_public_20200518_models.GetMetaDBTableListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_dbtable_list_with_options(request, runtime)

    async def get_meta_dbtable_list_async(
        self,
        request: dataworks_public_20200518_models.GetMetaDBTableListRequest,
    ) -> dataworks_public_20200518_models.GetMetaDBTableListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_dbtable_list_with_options_async(request, runtime)

    def get_meta_table_basic_info_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableBasicInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableBasicInfoResponse(),
            self.do_rpcrequest('GetMetaTableBasicInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_basic_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableBasicInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableBasicInfoResponse(),
            await self.do_rpcrequest_async('GetMetaTableBasicInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_basic_info(
        self,
        request: dataworks_public_20200518_models.GetMetaTableBasicInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_basic_info_with_options(request, runtime)

    async def get_meta_table_basic_info_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableBasicInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_basic_info_with_options_async(request, runtime)

    def get_meta_table_change_log_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableChangeLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableChangeLogResponse(),
            self.do_rpcrequest('GetMetaTableChangeLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_change_log_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableChangeLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableChangeLogResponse(),
            await self.do_rpcrequest_async('GetMetaTableChangeLog', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_change_log(
        self,
        request: dataworks_public_20200518_models.GetMetaTableChangeLogRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableChangeLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_change_log_with_options(request, runtime)

    async def get_meta_table_change_log_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableChangeLogRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableChangeLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_change_log_with_options_async(request, runtime)

    def get_meta_table_column_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableColumnResponse(),
            self.do_rpcrequest('GetMetaTableColumn', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_column_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableColumnResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableColumnResponse(),
            await self.do_rpcrequest_async('GetMetaTableColumn', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_column(
        self,
        request: dataworks_public_20200518_models.GetMetaTableColumnRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableColumnResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_column_with_options(request, runtime)

    async def get_meta_table_column_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableColumnRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableColumnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_column_with_options_async(request, runtime)

    def get_meta_table_full_info_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableFullInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableFullInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableFullInfoResponse(),
            self.do_rpcrequest('GetMetaTableFullInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_full_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableFullInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableFullInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableFullInfoResponse(),
            await self.do_rpcrequest_async('GetMetaTableFullInfo', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_full_info(
        self,
        request: dataworks_public_20200518_models.GetMetaTableFullInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableFullInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_full_info_with_options(request, runtime)

    async def get_meta_table_full_info_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableFullInfoRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableFullInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_full_info_with_options_async(request, runtime)

    def get_meta_table_intro_wiki_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableIntroWikiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableIntroWikiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableIntroWikiResponse(),
            self.do_rpcrequest('GetMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_intro_wiki_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableIntroWikiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableIntroWikiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableIntroWikiResponse(),
            await self.do_rpcrequest_async('GetMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_intro_wiki(
        self,
        request: dataworks_public_20200518_models.GetMetaTableIntroWikiRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableIntroWikiResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_intro_wiki_with_options(request, runtime)

    async def get_meta_table_intro_wiki_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableIntroWikiRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableIntroWikiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_intro_wiki_with_options_async(request, runtime)

    def get_meta_table_lineage_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableLineageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableLineageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableLineageResponse(),
            self.do_rpcrequest('GetMetaTableLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_lineage_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableLineageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableLineageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableLineageResponse(),
            await self.do_rpcrequest_async('GetMetaTableLineage', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_lineage(
        self,
        request: dataworks_public_20200518_models.GetMetaTableLineageRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableLineageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_lineage_with_options(request, runtime)

    async def get_meta_table_lineage_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableLineageRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableLineageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_lineage_with_options_async(request, runtime)

    def get_meta_table_list_by_category_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableListByCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableListByCategoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableListByCategoryResponse(),
            self.do_rpcrequest('GetMetaTableListByCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_list_by_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableListByCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableListByCategoryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableListByCategoryResponse(),
            await self.do_rpcrequest_async('GetMetaTableListByCategory', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_list_by_category(
        self,
        request: dataworks_public_20200518_models.GetMetaTableListByCategoryRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableListByCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_list_by_category_with_options(request, runtime)

    async def get_meta_table_list_by_category_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableListByCategoryRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableListByCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_list_by_category_with_options_async(request, runtime)

    def get_meta_table_output_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableOutputResponse(),
            self.do_rpcrequest('GetMetaTableOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_output_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableOutputResponse(),
            await self.do_rpcrequest_async('GetMetaTableOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_output(
        self,
        request: dataworks_public_20200518_models.GetMetaTableOutputRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_output_with_options(request, runtime)

    async def get_meta_table_output_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableOutputRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_output_with_options_async(request, runtime)

    def get_meta_table_partition_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTablePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTablePartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTablePartitionResponse(),
            self.do_rpcrequest('GetMetaTablePartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_partition_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTablePartitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTablePartitionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTablePartitionResponse(),
            await self.do_rpcrequest_async('GetMetaTablePartition', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_table_partition(
        self,
        request: dataworks_public_20200518_models.GetMetaTablePartitionRequest,
    ) -> dataworks_public_20200518_models.GetMetaTablePartitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_partition_with_options(request, runtime)

    async def get_meta_table_partition_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTablePartitionRequest,
    ) -> dataworks_public_20200518_models.GetMetaTablePartitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_partition_with_options_async(request, runtime)

    def get_meta_table_theme_level_with_options(
        self,
        request: dataworks_public_20200518_models.GetMetaTableThemeLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableThemeLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableThemeLevelResponse(),
            self.do_rpcrequest('GetMetaTableThemeLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_meta_table_theme_level_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableThemeLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMetaTableThemeLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMetaTableThemeLevelResponse(),
            await self.do_rpcrequest_async('GetMetaTableThemeLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_meta_table_theme_level(
        self,
        request: dataworks_public_20200518_models.GetMetaTableThemeLevelRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableThemeLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_meta_table_theme_level_with_options(request, runtime)

    async def get_meta_table_theme_level_async(
        self,
        request: dataworks_public_20200518_models.GetMetaTableThemeLevelRequest,
    ) -> dataworks_public_20200518_models.GetMetaTableThemeLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_meta_table_theme_level_with_options_async(request, runtime)

    def get_migration_process_with_options(
        self,
        request: dataworks_public_20200518_models.GetMigrationProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMigrationProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMigrationProcessResponse(),
            self.do_rpcrequest('GetMigrationProcess', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_migration_process_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetMigrationProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetMigrationProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetMigrationProcessResponse(),
            await self.do_rpcrequest_async('GetMigrationProcess', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_migration_process(
        self,
        request: dataworks_public_20200518_models.GetMigrationProcessRequest,
    ) -> dataworks_public_20200518_models.GetMigrationProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_migration_process_with_options(request, runtime)

    async def get_migration_process_async(
        self,
        request: dataworks_public_20200518_models.GetMigrationProcessRequest,
    ) -> dataworks_public_20200518_models.GetMigrationProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_migration_process_with_options_async(request, runtime)

    def get_node_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeResponse(),
            self.do_rpcrequest('GetNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeResponse(),
            await self.do_rpcrequest_async('GetNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node(
        self,
        request: dataworks_public_20200518_models.GetNodeRequest,
    ) -> dataworks_public_20200518_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_with_options(request, runtime)

    async def get_node_async(
        self,
        request: dataworks_public_20200518_models.GetNodeRequest,
    ) -> dataworks_public_20200518_models.GetNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_with_options_async(request, runtime)

    def get_node_children_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeChildrenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeChildrenResponse(),
            self.do_rpcrequest('GetNodeChildren', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_children_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeChildrenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeChildrenResponse(),
            await self.do_rpcrequest_async('GetNodeChildren', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_children(
        self,
        request: dataworks_public_20200518_models.GetNodeChildrenRequest,
    ) -> dataworks_public_20200518_models.GetNodeChildrenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_children_with_options(request, runtime)

    async def get_node_children_async(
        self,
        request: dataworks_public_20200518_models.GetNodeChildrenRequest,
    ) -> dataworks_public_20200518_models.GetNodeChildrenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_children_with_options_async(request, runtime)

    def get_node_code_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeCodeResponse(),
            self.do_rpcrequest('GetNodeCode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_code_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeCodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeCodeResponse(),
            await self.do_rpcrequest_async('GetNodeCode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_code(
        self,
        request: dataworks_public_20200518_models.GetNodeCodeRequest,
    ) -> dataworks_public_20200518_models.GetNodeCodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_code_with_options(request, runtime)

    async def get_node_code_async(
        self,
        request: dataworks_public_20200518_models.GetNodeCodeRequest,
    ) -> dataworks_public_20200518_models.GetNodeCodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_code_with_options_async(request, runtime)

    def get_node_on_baseline_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeOnBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeOnBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeOnBaselineResponse(),
            self.do_rpcrequest('GetNodeOnBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_on_baseline_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeOnBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeOnBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeOnBaselineResponse(),
            await self.do_rpcrequest_async('GetNodeOnBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_on_baseline(
        self,
        request: dataworks_public_20200518_models.GetNodeOnBaselineRequest,
    ) -> dataworks_public_20200518_models.GetNodeOnBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_on_baseline_with_options(request, runtime)

    async def get_node_on_baseline_async(
        self,
        request: dataworks_public_20200518_models.GetNodeOnBaselineRequest,
    ) -> dataworks_public_20200518_models.GetNodeOnBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_on_baseline_with_options_async(request, runtime)

    def get_node_parents_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeParentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeParentsResponse(),
            self.do_rpcrequest('GetNodeParents', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_parents_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeParentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeParentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeParentsResponse(),
            await self.do_rpcrequest_async('GetNodeParents', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_parents(
        self,
        request: dataworks_public_20200518_models.GetNodeParentsRequest,
    ) -> dataworks_public_20200518_models.GetNodeParentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_parents_with_options(request, runtime)

    async def get_node_parents_async(
        self,
        request: dataworks_public_20200518_models.GetNodeParentsRequest,
    ) -> dataworks_public_20200518_models.GetNodeParentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_parents_with_options_async(request, runtime)

    def get_node_type_list_info_with_options(
        self,
        request: dataworks_public_20200518_models.GetNodeTypeListInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeTypeListInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeTypeListInfoResponse(),
            self.do_rpcrequest('GetNodeTypeListInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_node_type_list_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetNodeTypeListInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetNodeTypeListInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetNodeTypeListInfoResponse(),
            await self.do_rpcrequest_async('GetNodeTypeListInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_node_type_list_info(
        self,
        request: dataworks_public_20200518_models.GetNodeTypeListInfoRequest,
    ) -> dataworks_public_20200518_models.GetNodeTypeListInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_type_list_info_with_options(request, runtime)

    async def get_node_type_list_info_async(
        self,
        request: dataworks_public_20200518_models.GetNodeTypeListInfoRequest,
    ) -> dataworks_public_20200518_models.GetNodeTypeListInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_type_list_info_with_options_async(request, runtime)

    def get_op_risk_data_with_options(
        self,
        request: dataworks_public_20200518_models.GetOpRiskDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetOpRiskDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpRiskDataResponse(),
            self.do_rpcrequest('GetOpRiskData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_op_risk_data_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetOpRiskDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetOpRiskDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpRiskDataResponse(),
            await self.do_rpcrequest_async('GetOpRiskData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_op_risk_data(
        self,
        request: dataworks_public_20200518_models.GetOpRiskDataRequest,
    ) -> dataworks_public_20200518_models.GetOpRiskDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_op_risk_data_with_options(request, runtime)

    async def get_op_risk_data_async(
        self,
        request: dataworks_public_20200518_models.GetOpRiskDataRequest,
    ) -> dataworks_public_20200518_models.GetOpRiskDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_op_risk_data_with_options_async(request, runtime)

    def get_op_sensitive_data_with_options(
        self,
        request: dataworks_public_20200518_models.GetOpSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetOpSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpSensitiveDataResponse(),
            self.do_rpcrequest('GetOpSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_op_sensitive_data_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetOpSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetOpSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetOpSensitiveDataResponse(),
            await self.do_rpcrequest_async('GetOpSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_op_sensitive_data(
        self,
        request: dataworks_public_20200518_models.GetOpSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.GetOpSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_op_sensitive_data_with_options(request, runtime)

    async def get_op_sensitive_data_async(
        self,
        request: dataworks_public_20200518_models.GetOpSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.GetOpSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_op_sensitive_data_with_options_async(request, runtime)

    def get_permission_apply_order_detail_with_options(
        self,
        request: dataworks_public_20200518_models.GetPermissionApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse(),
            self.do_rpcrequest('GetPermissionApplyOrderDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_permission_apply_order_detail_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetPermissionApplyOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse(),
            await self.do_rpcrequest_async('GetPermissionApplyOrderDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_permission_apply_order_detail(
        self,
        request: dataworks_public_20200518_models.GetPermissionApplyOrderDetailRequest,
    ) -> dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_permission_apply_order_detail_with_options(request, runtime)

    async def get_permission_apply_order_detail_async(
        self,
        request: dataworks_public_20200518_models.GetPermissionApplyOrderDetailRequest,
    ) -> dataworks_public_20200518_models.GetPermissionApplyOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_permission_apply_order_detail_with_options_async(request, runtime)

    def get_project_with_options(
        self,
        request: dataworks_public_20200518_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectResponse(),
            self.do_rpcrequest('GetProject', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectResponse(),
            await self.do_rpcrequest_async('GetProject', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project(
        self,
        request: dataworks_public_20200518_models.GetProjectRequest,
    ) -> dataworks_public_20200518_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_with_options(request, runtime)

    async def get_project_async(
        self,
        request: dataworks_public_20200518_models.GetProjectRequest,
    ) -> dataworks_public_20200518_models.GetProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_with_options_async(request, runtime)

    def get_project_detail_with_options(
        self,
        request: dataworks_public_20200518_models.GetProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetProjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectDetailResponse(),
            self.do_rpcrequest('GetProjectDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_project_detail_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetProjectDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetProjectDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetProjectDetailResponse(),
            await self.do_rpcrequest_async('GetProjectDetail', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_project_detail(
        self,
        request: dataworks_public_20200518_models.GetProjectDetailRequest,
    ) -> dataworks_public_20200518_models.GetProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_project_detail_with_options(request, runtime)

    async def get_project_detail_async(
        self,
        request: dataworks_public_20200518_models.GetProjectDetailRequest,
    ) -> dataworks_public_20200518_models.GetProjectDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_project_detail_with_options_async(request, runtime)

    def get_quality_entity_with_options(
        self,
        request: dataworks_public_20200518_models.GetQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityEntityResponse(),
            self.do_rpcrequest('GetQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_entity_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetQualityEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityEntityResponse(),
            await self.do_rpcrequest_async('GetQualityEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_entity(
        self,
        request: dataworks_public_20200518_models.GetQualityEntityRequest,
    ) -> dataworks_public_20200518_models.GetQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_entity_with_options(request, runtime)

    async def get_quality_entity_async(
        self,
        request: dataworks_public_20200518_models.GetQualityEntityRequest,
    ) -> dataworks_public_20200518_models.GetQualityEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_entity_with_options_async(request, runtime)

    def get_quality_follower_with_options(
        self,
        request: dataworks_public_20200518_models.GetQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityFollowerResponse(),
            self.do_rpcrequest('GetQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_follower_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityFollowerResponse(),
            await self.do_rpcrequest_async('GetQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_follower(
        self,
        request: dataworks_public_20200518_models.GetQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.GetQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_follower_with_options(request, runtime)

    async def get_quality_follower_async(
        self,
        request: dataworks_public_20200518_models.GetQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.GetQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_follower_with_options_async(request, runtime)

    def get_quality_rule_with_options(
        self,
        request: dataworks_public_20200518_models.GetQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityRuleResponse(),
            self.do_rpcrequest('GetQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_quality_rule_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetQualityRuleResponse(),
            await self.do_rpcrequest_async('GetQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_quality_rule(
        self,
        request: dataworks_public_20200518_models.GetQualityRuleRequest,
    ) -> dataworks_public_20200518_models.GetQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_quality_rule_with_options(request, runtime)

    async def get_quality_rule_async(
        self,
        request: dataworks_public_20200518_models.GetQualityRuleRequest,
    ) -> dataworks_public_20200518_models.GetQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_rule_with_options_async(request, runtime)

    def get_remind_with_options(
        self,
        request: dataworks_public_20200518_models.GetRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetRemindResponse(),
            self.do_rpcrequest('GetRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_remind_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetRemindResponse(),
            await self.do_rpcrequest_async('GetRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_remind(
        self,
        request: dataworks_public_20200518_models.GetRemindRequest,
    ) -> dataworks_public_20200518_models.GetRemindResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_remind_with_options(request, runtime)

    async def get_remind_async(
        self,
        request: dataworks_public_20200518_models.GetRemindRequest,
    ) -> dataworks_public_20200518_models.GetRemindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_remind_with_options_async(request, runtime)

    def get_sensitive_data_with_options(
        self,
        request: dataworks_public_20200518_models.GetSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSensitiveDataResponse(),
            self.do_rpcrequest('GetSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_sensitive_data_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSensitiveDataResponse(),
            await self.do_rpcrequest_async('GetSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_sensitive_data(
        self,
        request: dataworks_public_20200518_models.GetSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.GetSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_sensitive_data_with_options(request, runtime)

    async def get_sensitive_data_async(
        self,
        request: dataworks_public_20200518_models.GetSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.GetSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sensitive_data_with_options_async(request, runtime)

    def get_success_instance_trend_with_options(
        self,
        request: dataworks_public_20200518_models.GetSuccessInstanceTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetSuccessInstanceTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSuccessInstanceTrendResponse(),
            self.do_rpcrequest('GetSuccessInstanceTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_success_instance_trend_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetSuccessInstanceTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetSuccessInstanceTrendResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetSuccessInstanceTrendResponse(),
            await self.do_rpcrequest_async('GetSuccessInstanceTrend', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_success_instance_trend(
        self,
        request: dataworks_public_20200518_models.GetSuccessInstanceTrendRequest,
    ) -> dataworks_public_20200518_models.GetSuccessInstanceTrendResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_success_instance_trend_with_options(request, runtime)

    async def get_success_instance_trend_async(
        self,
        request: dataworks_public_20200518_models.GetSuccessInstanceTrendRequest,
    ) -> dataworks_public_20200518_models.GetSuccessInstanceTrendResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_success_instance_trend_with_options_async(request, runtime)

    def get_topic_with_options(
        self,
        request: dataworks_public_20200518_models.GetTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicResponse(),
            self.do_rpcrequest('GetTopic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetTopicResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicResponse(),
            await self.do_rpcrequest_async('GetTopic', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic(
        self,
        request: dataworks_public_20200518_models.GetTopicRequest,
    ) -> dataworks_public_20200518_models.GetTopicResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    async def get_topic_async(
        self,
        request: dataworks_public_20200518_models.GetTopicRequest,
    ) -> dataworks_public_20200518_models.GetTopicResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_with_options_async(request, runtime)

    def get_topic_influence_with_options(
        self,
        request: dataworks_public_20200518_models.GetTopicInfluenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetTopicInfluenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicInfluenceResponse(),
            self.do_rpcrequest('GetTopicInfluence', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_topic_influence_with_options_async(
        self,
        request: dataworks_public_20200518_models.GetTopicInfluenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.GetTopicInfluenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.GetTopicInfluenceResponse(),
            await self.do_rpcrequest_async('GetTopicInfluence', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_influence(
        self,
        request: dataworks_public_20200518_models.GetTopicInfluenceRequest,
    ) -> dataworks_public_20200518_models.GetTopicInfluenceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_topic_influence_with_options(request, runtime)

    async def get_topic_influence_async(
        self,
        request: dataworks_public_20200518_models.GetTopicInfluenceRequest,
    ) -> dataworks_public_20200518_models.GetTopicInfluenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_influence_with_options_async(request, runtime)

    def import_connections_with_options(
        self,
        request: dataworks_public_20200518_models.ImportConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportConnectionsResponse(),
            self.do_rpcrequest('ImportConnections', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_connections_with_options_async(
        self,
        request: dataworks_public_20200518_models.ImportConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportConnectionsResponse(),
            await self.do_rpcrequest_async('ImportConnections', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_connections(
        self,
        request: dataworks_public_20200518_models.ImportConnectionsRequest,
    ) -> dataworks_public_20200518_models.ImportConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_connections_with_options(request, runtime)

    async def import_connections_async(
        self,
        request: dataworks_public_20200518_models.ImportConnectionsRequest,
    ) -> dataworks_public_20200518_models.ImportConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_connections_with_options_async(request, runtime)

    def import_data_sources_with_options(
        self,
        request: dataworks_public_20200518_models.ImportDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDataSourcesResponse(),
            self.do_rpcrequest('ImportDataSources', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_data_sources_with_options_async(
        self,
        request: dataworks_public_20200518_models.ImportDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportDataSourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDataSourcesResponse(),
            await self.do_rpcrequest_async('ImportDataSources', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_data_sources(
        self,
        request: dataworks_public_20200518_models.ImportDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ImportDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_data_sources_with_options(request, runtime)

    async def import_data_sources_async(
        self,
        request: dataworks_public_20200518_models.ImportDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ImportDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_data_sources_with_options_async(request, runtime)

    def import_disync_tasks_with_options(
        self,
        request: dataworks_public_20200518_models.ImportDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDISyncTasksResponse(),
            self.do_rpcrequest('ImportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_disync_tasks_with_options_async(
        self,
        request: dataworks_public_20200518_models.ImportDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ImportDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ImportDISyncTasksResponse(),
            await self.do_rpcrequest_async('ImportDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_disync_tasks(
        self,
        request: dataworks_public_20200518_models.ImportDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ImportDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_disync_tasks_with_options(request, runtime)

    async def import_disync_tasks_async(
        self,
        request: dataworks_public_20200518_models.ImportDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ImportDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_disync_tasks_with_options_async(request, runtime)

    def list_alert_messages_with_options(
        self,
        request: dataworks_public_20200518_models.ListAlertMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListAlertMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListAlertMessagesResponse(),
            self.do_rpcrequest('ListAlertMessages', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_alert_messages_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListAlertMessagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListAlertMessagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListAlertMessagesResponse(),
            await self.do_rpcrequest_async('ListAlertMessages', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_alert_messages(
        self,
        request: dataworks_public_20200518_models.ListAlertMessagesRequest,
    ) -> dataworks_public_20200518_models.ListAlertMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alert_messages_with_options(request, runtime)

    async def list_alert_messages_async(
        self,
        request: dataworks_public_20200518_models.ListAlertMessagesRequest,
    ) -> dataworks_public_20200518_models.ListAlertMessagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_messages_with_options_async(request, runtime)

    def list_baseline_configs_with_options(
        self,
        request: dataworks_public_20200518_models.ListBaselineConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBaselineConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineConfigsResponse(),
            self.do_rpcrequest('ListBaselineConfigs', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_baseline_configs_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListBaselineConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBaselineConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineConfigsResponse(),
            await self.do_rpcrequest_async('ListBaselineConfigs', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_baseline_configs(
        self,
        request: dataworks_public_20200518_models.ListBaselineConfigsRequest,
    ) -> dataworks_public_20200518_models.ListBaselineConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_configs_with_options(request, runtime)

    async def list_baseline_configs_async(
        self,
        request: dataworks_public_20200518_models.ListBaselineConfigsRequest,
    ) -> dataworks_public_20200518_models.ListBaselineConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_baseline_configs_with_options_async(request, runtime)

    def list_baseline_statuses_with_options(
        self,
        request: dataworks_public_20200518_models.ListBaselineStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBaselineStatusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineStatusesResponse(),
            self.do_rpcrequest('ListBaselineStatuses', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_baseline_statuses_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListBaselineStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBaselineStatusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBaselineStatusesResponse(),
            await self.do_rpcrequest_async('ListBaselineStatuses', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_baseline_statuses(
        self,
        request: dataworks_public_20200518_models.ListBaselineStatusesRequest,
    ) -> dataworks_public_20200518_models.ListBaselineStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_baseline_statuses_with_options(request, runtime)

    async def list_baseline_statuses_async(
        self,
        request: dataworks_public_20200518_models.ListBaselineStatusesRequest,
    ) -> dataworks_public_20200518_models.ListBaselineStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_baseline_statuses_with_options_async(request, runtime)

    def list_business_with_options(
        self,
        request: dataworks_public_20200518_models.ListBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBusinessResponse(),
            self.do_rpcrequest('ListBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListBusinessResponse(),
            await self.do_rpcrequest_async('ListBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_business(
        self,
        request: dataworks_public_20200518_models.ListBusinessRequest,
    ) -> dataworks_public_20200518_models.ListBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_business_with_options(request, runtime)

    async def list_business_async(
        self,
        request: dataworks_public_20200518_models.ListBusinessRequest,
    ) -> dataworks_public_20200518_models.ListBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_business_with_options_async(request, runtime)

    def list_calc_engines_with_options(
        self,
        request: dataworks_public_20200518_models.ListCalcEnginesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListCalcEnginesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListCalcEnginesResponse(),
            self.do_rpcrequest('ListCalcEngines', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_calc_engines_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListCalcEnginesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListCalcEnginesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListCalcEnginesResponse(),
            await self.do_rpcrequest_async('ListCalcEngines', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_calc_engines(
        self,
        request: dataworks_public_20200518_models.ListCalcEnginesRequest,
    ) -> dataworks_public_20200518_models.ListCalcEnginesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_calc_engines_with_options(request, runtime)

    async def list_calc_engines_async(
        self,
        request: dataworks_public_20200518_models.ListCalcEnginesRequest,
    ) -> dataworks_public_20200518_models.ListCalcEnginesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_calc_engines_with_options_async(request, runtime)

    def list_connections_with_options(
        self,
        request: dataworks_public_20200518_models.ListConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListConnectionsResponse(),
            self.do_rpcrequest('ListConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_connections_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListConnectionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListConnectionsResponse(),
            await self.do_rpcrequest_async('ListConnections', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_connections(
        self,
        request: dataworks_public_20200518_models.ListConnectionsRequest,
    ) -> dataworks_public_20200518_models.ListConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connections_with_options(request, runtime)

    async def list_connections_async(
        self,
        request: dataworks_public_20200518_models.ListConnectionsRequest,
    ) -> dataworks_public_20200518_models.ListConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connections_with_options_async(request, runtime)

    def list_data_service_api_authorities_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApiAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse(),
            self.do_rpcrequest('ListDataServiceApiAuthorities', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_api_authorities_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApiAuthoritiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse(),
            await self.do_rpcrequest_async('ListDataServiceApiAuthorities', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_api_authorities(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApiAuthoritiesRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_api_authorities_with_options(request, runtime)

    async def list_data_service_api_authorities_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApiAuthoritiesRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApiAuthoritiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_api_authorities_with_options_async(request, runtime)

    def list_data_service_apis_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApisResponse(),
            self.do_rpcrequest('ListDataServiceApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_apis_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApisResponse(),
            await self.do_rpcrequest_async('ListDataServiceApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_apis(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_apis_with_options(request, runtime)

    async def list_data_service_apis_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_apis_with_options_async(request, runtime)

    def list_data_service_applications_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApplicationsResponse(),
            self.do_rpcrequest('ListDataServiceApplications', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_applications_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceApplicationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceApplicationsResponse(),
            await self.do_rpcrequest_async('ListDataServiceApplications', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_applications(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApplicationsRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_applications_with_options(request, runtime)

    async def list_data_service_applications_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceApplicationsRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_applications_with_options_async(request, runtime)

    def list_data_service_authorized_apis_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceAuthorizedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse(),
            self.do_rpcrequest('ListDataServiceAuthorizedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_authorized_apis_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceAuthorizedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse(),
            await self.do_rpcrequest_async('ListDataServiceAuthorizedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_authorized_apis(
        self,
        request: dataworks_public_20200518_models.ListDataServiceAuthorizedApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_authorized_apis_with_options(request, runtime)

    async def list_data_service_authorized_apis_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceAuthorizedApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceAuthorizedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_authorized_apis_with_options_async(request, runtime)

    def list_data_service_folders_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceFoldersResponse(),
            self.do_rpcrequest('ListDataServiceFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_folders_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceFoldersResponse(),
            await self.do_rpcrequest_async('ListDataServiceFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_folders(
        self,
        request: dataworks_public_20200518_models.ListDataServiceFoldersRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_folders_with_options(request, runtime)

    async def list_data_service_folders_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceFoldersRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_folders_with_options_async(request, runtime)

    def list_data_service_groups_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServiceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceGroupsResponse(),
            self.do_rpcrequest('ListDataServiceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_groups_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServiceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServiceGroupsResponse(),
            await self.do_rpcrequest_async('ListDataServiceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_groups(
        self,
        request: dataworks_public_20200518_models.ListDataServiceGroupsRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_groups_with_options(request, runtime)

    async def list_data_service_groups_async(
        self,
        request: dataworks_public_20200518_models.ListDataServiceGroupsRequest,
    ) -> dataworks_public_20200518_models.ListDataServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_groups_with_options_async(request, runtime)

    def list_data_service_published_apis_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataServicePublishedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServicePublishedApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServicePublishedApisResponse(),
            self.do_rpcrequest('ListDataServicePublishedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_service_published_apis_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataServicePublishedApisRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataServicePublishedApisResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataServicePublishedApisResponse(),
            await self.do_rpcrequest_async('ListDataServicePublishedApis', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_service_published_apis(
        self,
        request: dataworks_public_20200518_models.ListDataServicePublishedApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServicePublishedApisResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_service_published_apis_with_options(request, runtime)

    async def list_data_service_published_apis_async(
        self,
        request: dataworks_public_20200518_models.ListDataServicePublishedApisRequest,
    ) -> dataworks_public_20200518_models.ListDataServicePublishedApisResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_service_published_apis_with_options_async(request, runtime)

    def list_data_sources_with_options(
        self,
        request: dataworks_public_20200518_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataSourcesResponse(),
            self.do_rpcrequest('ListDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDataSourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDataSourcesResponse(),
            await self.do_rpcrequest_async('ListDataSources', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_data_sources(
        self,
        request: dataworks_public_20200518_models.ListDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_sources_with_options(request, runtime)

    async def list_data_sources_async(
        self,
        request: dataworks_public_20200518_models.ListDataSourcesRequest,
    ) -> dataworks_public_20200518_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_sources_with_options_async(request, runtime)

    def list_diproject_config_with_options(
        self,
        request: dataworks_public_20200518_models.ListDIProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDIProjectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDIProjectConfigResponse(),
            self.do_rpcrequest('ListDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_diproject_config_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDIProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDIProjectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDIProjectConfigResponse(),
            await self.do_rpcrequest_async('ListDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_diproject_config(
        self,
        request: dataworks_public_20200518_models.ListDIProjectConfigRequest,
    ) -> dataworks_public_20200518_models.ListDIProjectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_diproject_config_with_options(request, runtime)

    async def list_diproject_config_async(
        self,
        request: dataworks_public_20200518_models.ListDIProjectConfigRequest,
    ) -> dataworks_public_20200518_models.ListDIProjectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_diproject_config_with_options_async(request, runtime)

    def list_disync_tasks_with_options(
        self,
        request: dataworks_public_20200518_models.ListDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDISyncTasksResponse(),
            self.do_rpcrequest('ListDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_disync_tasks_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListDISyncTasksResponse(),
            await self.do_rpcrequest_async('ListDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_disync_tasks(
        self,
        request: dataworks_public_20200518_models.ListDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ListDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_disync_tasks_with_options(request, runtime)

    async def list_disync_tasks_async(
        self,
        request: dataworks_public_20200518_models.ListDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ListDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_disync_tasks_with_options_async(request, runtime)

    def list_files_with_options(
        self,
        request: dataworks_public_20200518_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFilesResponse(),
            self.do_rpcrequest('ListFiles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_files_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFilesResponse(),
            await self.do_rpcrequest_async('ListFiles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_files(
        self,
        request: dataworks_public_20200518_models.ListFilesRequest,
    ) -> dataworks_public_20200518_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_files_with_options(request, runtime)

    async def list_files_async(
        self,
        request: dataworks_public_20200518_models.ListFilesRequest,
    ) -> dataworks_public_20200518_models.ListFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_files_with_options_async(request, runtime)

    def list_file_type_with_options(
        self,
        request: dataworks_public_20200518_models.ListFileTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFileTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileTypeResponse(),
            self.do_rpcrequest('ListFileType', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_file_type_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListFileTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFileTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileTypeResponse(),
            await self.do_rpcrequest_async('ListFileType', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_file_type(
        self,
        request: dataworks_public_20200518_models.ListFileTypeRequest,
    ) -> dataworks_public_20200518_models.ListFileTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_file_type_with_options(request, runtime)

    async def list_file_type_async(
        self,
        request: dataworks_public_20200518_models.ListFileTypeRequest,
    ) -> dataworks_public_20200518_models.ListFileTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_type_with_options_async(request, runtime)

    def list_file_versions_with_options(
        self,
        request: dataworks_public_20200518_models.ListFileVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFileVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileVersionsResponse(),
            self.do_rpcrequest('ListFileVersions', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_file_versions_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListFileVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFileVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFileVersionsResponse(),
            await self.do_rpcrequest_async('ListFileVersions', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_file_versions(
        self,
        request: dataworks_public_20200518_models.ListFileVersionsRequest,
    ) -> dataworks_public_20200518_models.ListFileVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_file_versions_with_options(request, runtime)

    async def list_file_versions_async(
        self,
        request: dataworks_public_20200518_models.ListFileVersionsRequest,
    ) -> dataworks_public_20200518_models.ListFileVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_file_versions_with_options_async(request, runtime)

    def list_folders_with_options(
        self,
        request: dataworks_public_20200518_models.ListFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFoldersResponse(),
            self.do_rpcrequest('ListFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_folders_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListFoldersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListFoldersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListFoldersResponse(),
            await self.do_rpcrequest_async('ListFolders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_folders(
        self,
        request: dataworks_public_20200518_models.ListFoldersRequest,
    ) -> dataworks_public_20200518_models.ListFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_folders_with_options(request, runtime)

    async def list_folders_async(
        self,
        request: dataworks_public_20200518_models.ListFoldersRequest,
    ) -> dataworks_public_20200518_models.ListFoldersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_folders_with_options_async(request, runtime)

    def list_instance_amount_with_options(
        self,
        request: dataworks_public_20200518_models.ListInstanceAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListInstanceAmountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstanceAmountResponse(),
            self.do_rpcrequest('ListInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instance_amount_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListInstanceAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListInstanceAmountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstanceAmountResponse(),
            await self.do_rpcrequest_async('ListInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instance_amount(
        self,
        request: dataworks_public_20200518_models.ListInstanceAmountRequest,
    ) -> dataworks_public_20200518_models.ListInstanceAmountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instance_amount_with_options(request, runtime)

    async def list_instance_amount_async(
        self,
        request: dataworks_public_20200518_models.ListInstanceAmountRequest,
    ) -> dataworks_public_20200518_models.ListInstanceAmountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_amount_with_options_async(request, runtime)

    def list_instances_with_options(
        self,
        request: dataworks_public_20200518_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstancesResponse(),
            self.do_rpcrequest('ListInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListInstancesResponse(),
            await self.do_rpcrequest_async('ListInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_instances(
        self,
        request: dataworks_public_20200518_models.ListInstancesRequest,
    ) -> dataworks_public_20200518_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    async def list_instances_async(
        self,
        request: dataworks_public_20200518_models.ListInstancesRequest,
    ) -> dataworks_public_20200518_models.ListInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_instances_with_options_async(request, runtime)

    def list_manual_dag_instances_with_options(
        self,
        request: dataworks_public_20200518_models.ListManualDagInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListManualDagInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListManualDagInstancesResponse(),
            self.do_rpcrequest('ListManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_manual_dag_instances_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListManualDagInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListManualDagInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListManualDagInstancesResponse(),
            await self.do_rpcrequest_async('ListManualDagInstances', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_manual_dag_instances(
        self,
        request: dataworks_public_20200518_models.ListManualDagInstancesRequest,
    ) -> dataworks_public_20200518_models.ListManualDagInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_manual_dag_instances_with_options(request, runtime)

    async def list_manual_dag_instances_async(
        self,
        request: dataworks_public_20200518_models.ListManualDagInstancesRequest,
    ) -> dataworks_public_20200518_models.ListManualDagInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_manual_dag_instances_with_options_async(request, runtime)

    def list_meta_dbwith_options(
        self,
        request: dataworks_public_20200518_models.ListMetaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListMetaDBResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaDBResponse(),
            self.do_rpcrequest('ListMetaDB', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_meta_dbwith_options_async(
        self,
        request: dataworks_public_20200518_models.ListMetaDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListMetaDBResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListMetaDBResponse(),
            await self.do_rpcrequest_async('ListMetaDB', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_meta_db(
        self,
        request: dataworks_public_20200518_models.ListMetaDBRequest,
    ) -> dataworks_public_20200518_models.ListMetaDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_meta_dbwith_options(request, runtime)

    async def list_meta_db_async(
        self,
        request: dataworks_public_20200518_models.ListMetaDBRequest,
    ) -> dataworks_public_20200518_models.ListMetaDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_meta_dbwith_options_async(request, runtime)

    def list_node_input_or_output_with_options(
        self,
        request: dataworks_public_20200518_models.ListNodeInputOrOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodeInputOrOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeInputOrOutputResponse(),
            self.do_rpcrequest('ListNodeInputOrOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_node_input_or_output_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListNodeInputOrOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodeInputOrOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeInputOrOutputResponse(),
            await self.do_rpcrequest_async('ListNodeInputOrOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_node_input_or_output(
        self,
        request: dataworks_public_20200518_models.ListNodeInputOrOutputRequest,
    ) -> dataworks_public_20200518_models.ListNodeInputOrOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_input_or_output_with_options(request, runtime)

    async def list_node_input_or_output_async(
        self,
        request: dataworks_public_20200518_models.ListNodeInputOrOutputRequest,
    ) -> dataworks_public_20200518_models.ListNodeInputOrOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_input_or_output_with_options_async(request, runtime)

    def list_node_iowith_options(
        self,
        request: dataworks_public_20200518_models.ListNodeIORequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodeIOResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeIOResponse(),
            self.do_rpcrequest('ListNodeIO', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_node_iowith_options_async(
        self,
        request: dataworks_public_20200518_models.ListNodeIORequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodeIOResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodeIOResponse(),
            await self.do_rpcrequest_async('ListNodeIO', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_node_io(
        self,
        request: dataworks_public_20200518_models.ListNodeIORequest,
    ) -> dataworks_public_20200518_models.ListNodeIOResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_iowith_options(request, runtime)

    async def list_node_io_async(
        self,
        request: dataworks_public_20200518_models.ListNodeIORequest,
    ) -> dataworks_public_20200518_models.ListNodeIOResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_iowith_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: dataworks_public_20200518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesResponse(),
            self.do_rpcrequest('ListNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesResponse(),
            await self.do_rpcrequest_async('ListNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes(
        self,
        request: dataworks_public_20200518_models.ListNodesRequest,
    ) -> dataworks_public_20200518_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: dataworks_public_20200518_models.ListNodesRequest,
    ) -> dataworks_public_20200518_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_nodes_by_baseline_with_options(
        self,
        request: dataworks_public_20200518_models.ListNodesByBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesByBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByBaselineResponse(),
            self.do_rpcrequest('ListNodesByBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nodes_by_baseline_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListNodesByBaselineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesByBaselineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByBaselineResponse(),
            await self.do_rpcrequest_async('ListNodesByBaseline', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_baseline(
        self,
        request: dataworks_public_20200518_models.ListNodesByBaselineRequest,
    ) -> dataworks_public_20200518_models.ListNodesByBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_baseline_with_options(request, runtime)

    async def list_nodes_by_baseline_async(
        self,
        request: dataworks_public_20200518_models.ListNodesByBaselineRequest,
    ) -> dataworks_public_20200518_models.ListNodesByBaselineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_by_baseline_with_options_async(request, runtime)

    def list_nodes_by_output_with_options(
        self,
        request: dataworks_public_20200518_models.ListNodesByOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesByOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByOutputResponse(),
            self.do_rpcrequest('ListNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nodes_by_output_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListNodesByOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListNodesByOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListNodesByOutputResponse(),
            await self.do_rpcrequest_async('ListNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nodes_by_output(
        self,
        request: dataworks_public_20200518_models.ListNodesByOutputRequest,
    ) -> dataworks_public_20200518_models.ListNodesByOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_by_output_with_options(request, runtime)

    async def list_nodes_by_output_async(
        self,
        request: dataworks_public_20200518_models.ListNodesByOutputRequest,
    ) -> dataworks_public_20200518_models.ListNodesByOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_by_output_with_options_async(request, runtime)

    def list_permission_apply_orders_with_options(
        self,
        request: dataworks_public_20200518_models.ListPermissionApplyOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListPermissionApplyOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListPermissionApplyOrdersResponse(),
            self.do_rpcrequest('ListPermissionApplyOrders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_permission_apply_orders_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListPermissionApplyOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListPermissionApplyOrdersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListPermissionApplyOrdersResponse(),
            await self.do_rpcrequest_async('ListPermissionApplyOrders', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_permission_apply_orders(
        self,
        request: dataworks_public_20200518_models.ListPermissionApplyOrdersRequest,
    ) -> dataworks_public_20200518_models.ListPermissionApplyOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_permission_apply_orders_with_options(request, runtime)

    async def list_permission_apply_orders_async(
        self,
        request: dataworks_public_20200518_models.ListPermissionApplyOrdersRequest,
    ) -> dataworks_public_20200518_models.ListPermissionApplyOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_permission_apply_orders_with_options_async(request, runtime)

    def list_program_type_count_with_options(
        self,
        request: dataworks_public_20200518_models.ListProgramTypeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProgramTypeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProgramTypeCountResponse(),
            self.do_rpcrequest('ListProgramTypeCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_program_type_count_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListProgramTypeCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProgramTypeCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProgramTypeCountResponse(),
            await self.do_rpcrequest_async('ListProgramTypeCount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_program_type_count(
        self,
        request: dataworks_public_20200518_models.ListProgramTypeCountRequest,
    ) -> dataworks_public_20200518_models.ListProgramTypeCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_program_type_count_with_options(request, runtime)

    async def list_program_type_count_async(
        self,
        request: dataworks_public_20200518_models.ListProgramTypeCountRequest,
    ) -> dataworks_public_20200518_models.ListProgramTypeCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_program_type_count_with_options_async(request, runtime)

    def list_project_ids_with_options(
        self,
        request: dataworks_public_20200518_models.ListProjectIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectIdsResponse(),
            self.do_rpcrequest('ListProjectIds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_ids_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListProjectIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectIdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectIdsResponse(),
            await self.do_rpcrequest_async('ListProjectIds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_ids(
        self,
        request: dataworks_public_20200518_models.ListProjectIdsRequest,
    ) -> dataworks_public_20200518_models.ListProjectIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_ids_with_options(request, runtime)

    async def list_project_ids_async(
        self,
        request: dataworks_public_20200518_models.ListProjectIdsRequest,
    ) -> dataworks_public_20200518_models.ListProjectIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_ids_with_options_async(request, runtime)

    def list_project_members_with_options(
        self,
        request: dataworks_public_20200518_models.ListProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectMembersResponse(),
            self.do_rpcrequest('ListProjectMembers', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_members_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListProjectMembersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectMembersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectMembersResponse(),
            await self.do_rpcrequest_async('ListProjectMembers', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_members(
        self,
        request: dataworks_public_20200518_models.ListProjectMembersRequest,
    ) -> dataworks_public_20200518_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_members_with_options(request, runtime)

    async def list_project_members_async(
        self,
        request: dataworks_public_20200518_models.ListProjectMembersRequest,
    ) -> dataworks_public_20200518_models.ListProjectMembersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_members_with_options_async(request, runtime)

    def list_project_roles_with_options(
        self,
        request: dataworks_public_20200518_models.ListProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectRolesResponse(),
            self.do_rpcrequest('ListProjectRoles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_project_roles_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListProjectRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectRolesResponse(),
            await self.do_rpcrequest_async('ListProjectRoles', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_roles(
        self,
        request: dataworks_public_20200518_models.ListProjectRolesRequest,
    ) -> dataworks_public_20200518_models.ListProjectRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_project_roles_with_options(request, runtime)

    async def list_project_roles_async(
        self,
        request: dataworks_public_20200518_models.ListProjectRolesRequest,
    ) -> dataworks_public_20200518_models.ListProjectRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_project_roles_with_options_async(request, runtime)

    def list_projects_with_options(
        self,
        request: dataworks_public_20200518_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListProjectsResponse(),
            await self.do_rpcrequest_async('ListProjects', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(
        self,
        request: dataworks_public_20200518_models.ListProjectsRequest,
    ) -> dataworks_public_20200518_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(request, runtime)

    async def list_projects_async(
        self,
        request: dataworks_public_20200518_models.ListProjectsRequest,
    ) -> dataworks_public_20200518_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_projects_with_options_async(request, runtime)

    def list_quality_results_by_entity_with_options(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityResultsByEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByEntityResponse(),
            self.do_rpcrequest('ListQualityResultsByEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_quality_results_by_entity_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityResultsByEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByEntityResponse(),
            await self.do_rpcrequest_async('ListQualityResultsByEntity', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_results_by_entity(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByEntityRequest,
    ) -> dataworks_public_20200518_models.ListQualityResultsByEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_entity_with_options(request, runtime)

    async def list_quality_results_by_entity_async(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByEntityRequest,
    ) -> dataworks_public_20200518_models.ListQualityResultsByEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quality_results_by_entity_with_options_async(request, runtime)

    def list_quality_results_by_rule_with_options(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityResultsByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByRuleResponse(),
            self.do_rpcrequest('ListQualityResultsByRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_quality_results_by_rule_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityResultsByRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityResultsByRuleResponse(),
            await self.do_rpcrequest_async('ListQualityResultsByRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_results_by_rule(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByRuleRequest,
    ) -> dataworks_public_20200518_models.ListQualityResultsByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quality_results_by_rule_with_options(request, runtime)

    async def list_quality_results_by_rule_async(
        self,
        request: dataworks_public_20200518_models.ListQualityResultsByRuleRequest,
    ) -> dataworks_public_20200518_models.ListQualityResultsByRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quality_results_by_rule_with_options_async(request, runtime)

    def list_quality_rules_with_options(
        self,
        request: dataworks_public_20200518_models.ListQualityRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityRulesResponse(),
            self.do_rpcrequest('ListQualityRules', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_quality_rules_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListQualityRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListQualityRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListQualityRulesResponse(),
            await self.do_rpcrequest_async('ListQualityRules', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_quality_rules(
        self,
        request: dataworks_public_20200518_models.ListQualityRulesRequest,
    ) -> dataworks_public_20200518_models.ListQualityRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_quality_rules_with_options(request, runtime)

    async def list_quality_rules_async(
        self,
        request: dataworks_public_20200518_models.ListQualityRulesRequest,
    ) -> dataworks_public_20200518_models.ListQualityRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quality_rules_with_options_async(request, runtime)

    def list_ref_disync_tasks_with_options(
        self,
        request: dataworks_public_20200518_models.ListRefDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListRefDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRefDISyncTasksResponse(),
            self.do_rpcrequest('ListRefDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ref_disync_tasks_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListRefDISyncTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListRefDISyncTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRefDISyncTasksResponse(),
            await self.do_rpcrequest_async('ListRefDISyncTasks', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ref_disync_tasks(
        self,
        request: dataworks_public_20200518_models.ListRefDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ListRefDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ref_disync_tasks_with_options(request, runtime)

    async def list_ref_disync_tasks_async(
        self,
        request: dataworks_public_20200518_models.ListRefDISyncTasksRequest,
    ) -> dataworks_public_20200518_models.ListRefDISyncTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ref_disync_tasks_with_options_async(request, runtime)

    def list_reminds_with_options(
        self,
        request: dataworks_public_20200518_models.ListRemindsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListRemindsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRemindsResponse(),
            self.do_rpcrequest('ListReminds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_reminds_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListRemindsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListRemindsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListRemindsResponse(),
            await self.do_rpcrequest_async('ListReminds', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_reminds(
        self,
        request: dataworks_public_20200518_models.ListRemindsRequest,
    ) -> dataworks_public_20200518_models.ListRemindsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_reminds_with_options(request, runtime)

    async def list_reminds_async(
        self,
        request: dataworks_public_20200518_models.ListRemindsRequest,
    ) -> dataworks_public_20200518_models.ListRemindsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_reminds_with_options_async(request, runtime)

    def list_resource_groups_with_options(
        self,
        request: dataworks_public_20200518_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListResourceGroupsResponse(),
            self.do_rpcrequest('ListResourceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_groups_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListResourceGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListResourceGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListResourceGroupsResponse(),
            await self.do_rpcrequest_async('ListResourceGroups', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_groups(
        self,
        request: dataworks_public_20200518_models.ListResourceGroupsRequest,
    ) -> dataworks_public_20200518_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    async def list_resource_groups_async(
        self,
        request: dataworks_public_20200518_models.ListResourceGroupsRequest,
    ) -> dataworks_public_20200518_models.ListResourceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_groups_with_options_async(request, runtime)

    def list_success_instance_amount_with_options(
        self,
        request: dataworks_public_20200518_models.ListSuccessInstanceAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListSuccessInstanceAmountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListSuccessInstanceAmountResponse(),
            self.do_rpcrequest('ListSuccessInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_success_instance_amount_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListSuccessInstanceAmountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListSuccessInstanceAmountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListSuccessInstanceAmountResponse(),
            await self.do_rpcrequest_async('ListSuccessInstanceAmount', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_success_instance_amount(
        self,
        request: dataworks_public_20200518_models.ListSuccessInstanceAmountRequest,
    ) -> dataworks_public_20200518_models.ListSuccessInstanceAmountResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_success_instance_amount_with_options(request, runtime)

    async def list_success_instance_amount_async(
        self,
        request: dataworks_public_20200518_models.ListSuccessInstanceAmountRequest,
    ) -> dataworks_public_20200518_models.ListSuccessInstanceAmountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_success_instance_amount_with_options_async(request, runtime)

    def list_table_level_with_options(
        self,
        request: dataworks_public_20200518_models.ListTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTableLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableLevelResponse(),
            self.do_rpcrequest('ListTableLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_table_level_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTableLevelResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableLevelResponse(),
            await self.do_rpcrequest_async('ListTableLevel', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_table_level(
        self,
        request: dataworks_public_20200518_models.ListTableLevelRequest,
    ) -> dataworks_public_20200518_models.ListTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_table_level_with_options(request, runtime)

    async def list_table_level_async(
        self,
        request: dataworks_public_20200518_models.ListTableLevelRequest,
    ) -> dataworks_public_20200518_models.ListTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_table_level_with_options_async(request, runtime)

    def list_table_theme_with_options(
        self,
        request: dataworks_public_20200518_models.ListTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTableThemeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableThemeResponse(),
            self.do_rpcrequest('ListTableTheme', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_table_theme_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTableThemeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTableThemeResponse(),
            await self.do_rpcrequest_async('ListTableTheme', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_table_theme(
        self,
        request: dataworks_public_20200518_models.ListTableThemeRequest,
    ) -> dataworks_public_20200518_models.ListTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_table_theme_with_options(request, runtime)

    async def list_table_theme_async(
        self,
        request: dataworks_public_20200518_models.ListTableThemeRequest,
    ) -> dataworks_public_20200518_models.ListTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_table_theme_with_options_async(request, runtime)

    def list_topics_with_options(
        self,
        request: dataworks_public_20200518_models.ListTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTopicsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTopicsResponse(),
            self.do_rpcrequest('ListTopics', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_topics_with_options_async(
        self,
        request: dataworks_public_20200518_models.ListTopicsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ListTopicsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ListTopicsResponse(),
            await self.do_rpcrequest_async('ListTopics', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_topics(
        self,
        request: dataworks_public_20200518_models.ListTopicsRequest,
    ) -> dataworks_public_20200518_models.ListTopicsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_topics_with_options(request, runtime)

    async def list_topics_async(
        self,
        request: dataworks_public_20200518_models.ListTopicsRequest,
    ) -> dataworks_public_20200518_models.ListTopicsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_topics_with_options_async(request, runtime)

    def publish_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.PublishDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.PublishDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.PublishDataServiceApiResponse(),
            self.do_rpcrequest('PublishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.PublishDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.PublishDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.PublishDataServiceApiResponse(),
            await self.do_rpcrequest_async('PublishDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_data_service_api(
        self,
        request: dataworks_public_20200518_models.PublishDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.PublishDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_data_service_api_with_options(request, runtime)

    async def publish_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.PublishDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.PublishDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_data_service_api_with_options_async(request, runtime)

    def query_disync_task_config_process_result_with_options(
        self,
        request: dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse(),
            self.do_rpcrequest('QueryDISyncTaskConfigProcessResult', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_disync_task_config_process_result_with_options_async(
        self,
        request: dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse(),
            await self.do_rpcrequest_async('QueryDISyncTaskConfigProcessResult', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_disync_task_config_process_result(
        self,
        request: dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultRequest,
    ) -> dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_disync_task_config_process_result_with_options(request, runtime)

    async def query_disync_task_config_process_result_async(
        self,
        request: dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultRequest,
    ) -> dataworks_public_20200518_models.QueryDISyncTaskConfigProcessResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_disync_task_config_process_result_with_options_async(request, runtime)

    def query_public_model_engine_with_options(
        self,
        request: dataworks_public_20200518_models.QueryPublicModelEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.QueryPublicModelEngineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryPublicModelEngineResponse(),
            self.do_rpcrequest('QueryPublicModelEngine', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_public_model_engine_with_options_async(
        self,
        request: dataworks_public_20200518_models.QueryPublicModelEngineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.QueryPublicModelEngineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.QueryPublicModelEngineResponse(),
            await self.do_rpcrequest_async('QueryPublicModelEngine', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_public_model_engine(
        self,
        request: dataworks_public_20200518_models.QueryPublicModelEngineRequest,
    ) -> dataworks_public_20200518_models.QueryPublicModelEngineResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_public_model_engine_with_options(request, runtime)

    async def query_public_model_engine_async(
        self,
        request: dataworks_public_20200518_models.QueryPublicModelEngineRequest,
    ) -> dataworks_public_20200518_models.QueryPublicModelEngineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_public_model_engine_with_options_async(request, runtime)

    def remove_project_member_from_role_with_options(
        self,
        request: dataworks_public_20200518_models.RemoveProjectMemberFromRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse(),
            self.do_rpcrequest('RemoveProjectMemberFromRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_project_member_from_role_with_options_async(
        self,
        request: dataworks_public_20200518_models.RemoveProjectMemberFromRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse(),
            await self.do_rpcrequest_async('RemoveProjectMemberFromRole', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_project_member_from_role(
        self,
        request: dataworks_public_20200518_models.RemoveProjectMemberFromRoleRequest,
    ) -> dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_project_member_from_role_with_options(request, runtime)

    async def remove_project_member_from_role_async(
        self,
        request: dataworks_public_20200518_models.RemoveProjectMemberFromRoleRequest,
    ) -> dataworks_public_20200518_models.RemoveProjectMemberFromRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_project_member_from_role_with_options_async(request, runtime)

    def restart_instance_with_options(
        self,
        request: dataworks_public_20200518_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RestartInstanceResponse(),
            self.do_rpcrequest('RestartInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.RestartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RestartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RestartInstanceResponse(),
            await self.do_rpcrequest_async('RestartInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_instance(
        self,
        request: dataworks_public_20200518_models.RestartInstanceRequest,
    ) -> dataworks_public_20200518_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_instance_with_options(request, runtime)

    async def restart_instance_async(
        self,
        request: dataworks_public_20200518_models.RestartInstanceRequest,
    ) -> dataworks_public_20200518_models.RestartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_instance_with_options_async(request, runtime)

    def resume_instance_with_options(
        self,
        request: dataworks_public_20200518_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ResumeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ResumeInstanceResponse(),
            self.do_rpcrequest('ResumeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.ResumeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ResumeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ResumeInstanceResponse(),
            await self.do_rpcrequest_async('ResumeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_instance(
        self,
        request: dataworks_public_20200518_models.ResumeInstanceRequest,
    ) -> dataworks_public_20200518_models.ResumeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_instance_with_options(request, runtime)

    async def resume_instance_async(
        self,
        request: dataworks_public_20200518_models.ResumeInstanceRequest,
    ) -> dataworks_public_20200518_models.ResumeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_instance_with_options_async(request, runtime)

    def revoke_column_permission_with_options(
        self,
        request: dataworks_public_20200518_models.RevokeColumnPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RevokeColumnPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeColumnPermissionResponse(),
            self.do_rpcrequest('RevokeColumnPermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_column_permission_with_options_async(
        self,
        request: dataworks_public_20200518_models.RevokeColumnPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RevokeColumnPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeColumnPermissionResponse(),
            await self.do_rpcrequest_async('RevokeColumnPermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_column_permission(
        self,
        request: dataworks_public_20200518_models.RevokeColumnPermissionRequest,
    ) -> dataworks_public_20200518_models.RevokeColumnPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_column_permission_with_options(request, runtime)

    async def revoke_column_permission_async(
        self,
        request: dataworks_public_20200518_models.RevokeColumnPermissionRequest,
    ) -> dataworks_public_20200518_models.RevokeColumnPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_column_permission_with_options_async(request, runtime)

    def revoke_table_permission_with_options(
        self,
        request: dataworks_public_20200518_models.RevokeTablePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RevokeTablePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeTablePermissionResponse(),
            self.do_rpcrequest('RevokeTablePermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_table_permission_with_options_async(
        self,
        request: dataworks_public_20200518_models.RevokeTablePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RevokeTablePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RevokeTablePermissionResponse(),
            await self.do_rpcrequest_async('RevokeTablePermission', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_table_permission(
        self,
        request: dataworks_public_20200518_models.RevokeTablePermissionRequest,
    ) -> dataworks_public_20200518_models.RevokeTablePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_table_permission_with_options(request, runtime)

    async def revoke_table_permission_async(
        self,
        request: dataworks_public_20200518_models.RevokeTablePermissionRequest,
    ) -> dataworks_public_20200518_models.RevokeTablePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_table_permission_with_options_async(request, runtime)

    def run_cycle_dag_nodes_with_options(
        self,
        request: dataworks_public_20200518_models.RunCycleDagNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunCycleDagNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunCycleDagNodesResponse(),
            self.do_rpcrequest('RunCycleDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_cycle_dag_nodes_with_options_async(
        self,
        request: dataworks_public_20200518_models.RunCycleDagNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunCycleDagNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunCycleDagNodesResponse(),
            await self.do_rpcrequest_async('RunCycleDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cycle_dag_nodes(
        self,
        request: dataworks_public_20200518_models.RunCycleDagNodesRequest,
    ) -> dataworks_public_20200518_models.RunCycleDagNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_cycle_dag_nodes_with_options(request, runtime)

    async def run_cycle_dag_nodes_async(
        self,
        request: dataworks_public_20200518_models.RunCycleDagNodesRequest,
    ) -> dataworks_public_20200518_models.RunCycleDagNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cycle_dag_nodes_with_options_async(request, runtime)

    def run_manual_dag_nodes_with_options(
        self,
        request: dataworks_public_20200518_models.RunManualDagNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunManualDagNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunManualDagNodesResponse(),
            self.do_rpcrequest('RunManualDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_manual_dag_nodes_with_options_async(
        self,
        request: dataworks_public_20200518_models.RunManualDagNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunManualDagNodesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunManualDagNodesResponse(),
            await self.do_rpcrequest_async('RunManualDagNodes', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_manual_dag_nodes(
        self,
        request: dataworks_public_20200518_models.RunManualDagNodesRequest,
    ) -> dataworks_public_20200518_models.RunManualDagNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_manual_dag_nodes_with_options(request, runtime)

    async def run_manual_dag_nodes_async(
        self,
        request: dataworks_public_20200518_models.RunManualDagNodesRequest,
    ) -> dataworks_public_20200518_models.RunManualDagNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_manual_dag_nodes_with_options_async(request, runtime)

    def run_smoke_test_with_options(
        self,
        request: dataworks_public_20200518_models.RunSmokeTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunSmokeTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunSmokeTestResponse(),
            self.do_rpcrequest('RunSmokeTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_smoke_test_with_options_async(
        self,
        request: dataworks_public_20200518_models.RunSmokeTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunSmokeTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunSmokeTestResponse(),
            await self.do_rpcrequest_async('RunSmokeTest', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_smoke_test(
        self,
        request: dataworks_public_20200518_models.RunSmokeTestRequest,
    ) -> dataworks_public_20200518_models.RunSmokeTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_smoke_test_with_options(request, runtime)

    async def run_smoke_test_async(
        self,
        request: dataworks_public_20200518_models.RunSmokeTestRequest,
    ) -> dataworks_public_20200518_models.RunSmokeTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_smoke_test_with_options_async(request, runtime)

    def run_trigger_node_with_options(
        self,
        request: dataworks_public_20200518_models.RunTriggerNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunTriggerNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunTriggerNodeResponse(),
            self.do_rpcrequest('RunTriggerNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_trigger_node_with_options_async(
        self,
        request: dataworks_public_20200518_models.RunTriggerNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.RunTriggerNodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.RunTriggerNodeResponse(),
            await self.do_rpcrequest_async('RunTriggerNode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_trigger_node(
        self,
        request: dataworks_public_20200518_models.RunTriggerNodeRequest,
    ) -> dataworks_public_20200518_models.RunTriggerNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_trigger_node_with_options(request, runtime)

    async def run_trigger_node_async(
        self,
        request: dataworks_public_20200518_models.RunTriggerNodeRequest,
    ) -> dataworks_public_20200518_models.RunTriggerNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_trigger_node_with_options_async(request, runtime)

    def scan_sensitive_data_with_options(
        self,
        request: dataworks_public_20200518_models.ScanSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ScanSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ScanSensitiveDataResponse(),
            self.do_rpcrequest('ScanSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def scan_sensitive_data_with_options_async(
        self,
        request: dataworks_public_20200518_models.ScanSensitiveDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.ScanSensitiveDataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.ScanSensitiveDataResponse(),
            await self.do_rpcrequest_async('ScanSensitiveData', '2020-05-18', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def scan_sensitive_data(
        self,
        request: dataworks_public_20200518_models.ScanSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.ScanSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.scan_sensitive_data_with_options(request, runtime)

    async def scan_sensitive_data_async(
        self,
        request: dataworks_public_20200518_models.ScanSensitiveDataRequest,
    ) -> dataworks_public_20200518_models.ScanSensitiveDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scan_sensitive_data_with_options_async(request, runtime)

    def search_meta_tables_with_options(
        self,
        request: dataworks_public_20200518_models.SearchMetaTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SearchMetaTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchMetaTablesResponse(),
            self.do_rpcrequest('SearchMetaTables', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_meta_tables_with_options_async(
        self,
        request: dataworks_public_20200518_models.SearchMetaTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SearchMetaTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchMetaTablesResponse(),
            await self.do_rpcrequest_async('SearchMetaTables', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_meta_tables(
        self,
        request: dataworks_public_20200518_models.SearchMetaTablesRequest,
    ) -> dataworks_public_20200518_models.SearchMetaTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_meta_tables_with_options(request, runtime)

    async def search_meta_tables_async(
        self,
        request: dataworks_public_20200518_models.SearchMetaTablesRequest,
    ) -> dataworks_public_20200518_models.SearchMetaTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_meta_tables_with_options_async(request, runtime)

    def search_nodes_by_output_with_options(
        self,
        request: dataworks_public_20200518_models.SearchNodesByOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SearchNodesByOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchNodesByOutputResponse(),
            self.do_rpcrequest('SearchNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_nodes_by_output_with_options_async(
        self,
        request: dataworks_public_20200518_models.SearchNodesByOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SearchNodesByOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SearchNodesByOutputResponse(),
            await self.do_rpcrequest_async('SearchNodesByOutput', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_nodes_by_output(
        self,
        request: dataworks_public_20200518_models.SearchNodesByOutputRequest,
    ) -> dataworks_public_20200518_models.SearchNodesByOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_nodes_by_output_with_options(request, runtime)

    async def search_nodes_by_output_async(
        self,
        request: dataworks_public_20200518_models.SearchNodesByOutputRequest,
    ) -> dataworks_public_20200518_models.SearchNodesByOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_nodes_by_output_with_options_async(request, runtime)

    def set_connection_share_with_options(
        self,
        request: dataworks_public_20200518_models.SetConnectionShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetConnectionShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetConnectionShareResponse(),
            self.do_rpcrequest('SetConnectionShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_connection_share_with_options_async(
        self,
        request: dataworks_public_20200518_models.SetConnectionShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetConnectionShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetConnectionShareResponse(),
            await self.do_rpcrequest_async('SetConnectionShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_connection_share(
        self,
        request: dataworks_public_20200518_models.SetConnectionShareRequest,
    ) -> dataworks_public_20200518_models.SetConnectionShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_connection_share_with_options(request, runtime)

    async def set_connection_share_async(
        self,
        request: dataworks_public_20200518_models.SetConnectionShareRequest,
    ) -> dataworks_public_20200518_models.SetConnectionShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_connection_share_with_options_async(request, runtime)

    def set_data_source_share_with_options(
        self,
        request: dataworks_public_20200518_models.SetDataSourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetDataSourceShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetDataSourceShareResponse(),
            self.do_rpcrequest('SetDataSourceShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_data_source_share_with_options_async(
        self,
        request: dataworks_public_20200518_models.SetDataSourceShareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetDataSourceShareResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetDataSourceShareResponse(),
            await self.do_rpcrequest_async('SetDataSourceShare', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_data_source_share(
        self,
        request: dataworks_public_20200518_models.SetDataSourceShareRequest,
    ) -> dataworks_public_20200518_models.SetDataSourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_data_source_share_with_options(request, runtime)

    async def set_data_source_share_async(
        self,
        request: dataworks_public_20200518_models.SetDataSourceShareRequest,
    ) -> dataworks_public_20200518_models.SetDataSourceShareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_data_source_share_with_options_async(request, runtime)

    def set_success_instance_with_options(
        self,
        request: dataworks_public_20200518_models.SetSuccessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetSuccessInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetSuccessInstanceResponse(),
            self.do_rpcrequest('SetSuccessInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_success_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.SetSuccessInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SetSuccessInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SetSuccessInstanceResponse(),
            await self.do_rpcrequest_async('SetSuccessInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_success_instance(
        self,
        request: dataworks_public_20200518_models.SetSuccessInstanceRequest,
    ) -> dataworks_public_20200518_models.SetSuccessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_success_instance_with_options(request, runtime)

    async def set_success_instance_async(
        self,
        request: dataworks_public_20200518_models.SetSuccessInstanceRequest,
    ) -> dataworks_public_20200518_models.SetSuccessInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_success_instance_with_options_async(request, runtime)

    def start_disync_instance_with_options(
        self,
        request: dataworks_public_20200518_models.StartDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StartDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartDISyncInstanceResponse(),
            self.do_rpcrequest('StartDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_disync_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.StartDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StartDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartDISyncInstanceResponse(),
            await self.do_rpcrequest_async('StartDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_disync_instance(
        self,
        request: dataworks_public_20200518_models.StartDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.StartDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_disync_instance_with_options(request, runtime)

    async def start_disync_instance_async(
        self,
        request: dataworks_public_20200518_models.StartDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.StartDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_disync_instance_with_options_async(request, runtime)

    def start_migration_with_options(
        self,
        request: dataworks_public_20200518_models.StartMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StartMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartMigrationResponse(),
            self.do_rpcrequest('StartMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_migration_with_options_async(
        self,
        request: dataworks_public_20200518_models.StartMigrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StartMigrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StartMigrationResponse(),
            await self.do_rpcrequest_async('StartMigration', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_migration(
        self,
        request: dataworks_public_20200518_models.StartMigrationRequest,
    ) -> dataworks_public_20200518_models.StartMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_migration_with_options(request, runtime)

    async def start_migration_async(
        self,
        request: dataworks_public_20200518_models.StartMigrationRequest,
    ) -> dataworks_public_20200518_models.StartMigrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_migration_with_options_async(request, runtime)

    def stop_disync_instance_with_options(
        self,
        request: dataworks_public_20200518_models.StopDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StopDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopDISyncInstanceResponse(),
            self.do_rpcrequest('StopDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_disync_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.StopDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StopDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopDISyncInstanceResponse(),
            await self.do_rpcrequest_async('StopDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_disync_instance(
        self,
        request: dataworks_public_20200518_models.StopDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.StopDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_disync_instance_with_options(request, runtime)

    async def stop_disync_instance_async(
        self,
        request: dataworks_public_20200518_models.StopDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.StopDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_disync_instance_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: dataworks_public_20200518_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopInstanceResponse(),
            self.do_rpcrequest('StopInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.StopInstanceResponse(),
            await self.do_rpcrequest_async('StopInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(
        self,
        request: dataworks_public_20200518_models.StopInstanceRequest,
    ) -> dataworks_public_20200518_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: dataworks_public_20200518_models.StopInstanceRequest,
    ) -> dataworks_public_20200518_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def submit_file_with_options(
        self,
        request: dataworks_public_20200518_models.SubmitFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SubmitFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SubmitFileResponse(),
            self.do_rpcrequest('SubmitFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.SubmitFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SubmitFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SubmitFileResponse(),
            await self.do_rpcrequest_async('SubmitFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_file(
        self,
        request: dataworks_public_20200518_models.SubmitFileRequest,
    ) -> dataworks_public_20200518_models.SubmitFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_file_with_options(request, runtime)

    async def submit_file_async(
        self,
        request: dataworks_public_20200518_models.SubmitFileRequest,
    ) -> dataworks_public_20200518_models.SubmitFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_file_with_options_async(request, runtime)

    def suspend_instance_with_options(
        self,
        request: dataworks_public_20200518_models.SuspendInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SuspendInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SuspendInstanceResponse(),
            self.do_rpcrequest('SuspendInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.SuspendInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.SuspendInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.SuspendInstanceResponse(),
            await self.do_rpcrequest_async('SuspendInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_instance(
        self,
        request: dataworks_public_20200518_models.SuspendInstanceRequest,
    ) -> dataworks_public_20200518_models.SuspendInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_instance_with_options(request, runtime)

    async def suspend_instance_async(
        self,
        request: dataworks_public_20200518_models.SuspendInstanceRequest,
    ) -> dataworks_public_20200518_models.SuspendInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_instance_with_options_async(request, runtime)

    def terminate_disync_instance_with_options(
        self,
        request: dataworks_public_20200518_models.TerminateDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TerminateDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TerminateDISyncInstanceResponse(),
            self.do_rpcrequest('TerminateDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_disync_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.TerminateDISyncInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TerminateDISyncInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TerminateDISyncInstanceResponse(),
            await self.do_rpcrequest_async('TerminateDISyncInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_disync_instance(
        self,
        request: dataworks_public_20200518_models.TerminateDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.TerminateDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_disync_instance_with_options(request, runtime)

    async def terminate_disync_instance_async(
        self,
        request: dataworks_public_20200518_models.TerminateDISyncInstanceRequest,
    ) -> dataworks_public_20200518_models.TerminateDISyncInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_disync_instance_with_options_async(request, runtime)

    def test_network_connection_with_options(
        self,
        request: dataworks_public_20200518_models.TestNetworkConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TestNetworkConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TestNetworkConnectionResponse(),
            self.do_rpcrequest('TestNetworkConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def test_network_connection_with_options_async(
        self,
        request: dataworks_public_20200518_models.TestNetworkConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TestNetworkConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TestNetworkConnectionResponse(),
            await self.do_rpcrequest_async('TestNetworkConnection', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_network_connection(
        self,
        request: dataworks_public_20200518_models.TestNetworkConnectionRequest,
    ) -> dataworks_public_20200518_models.TestNetworkConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_network_connection_with_options(request, runtime)

    async def test_network_connection_async(
        self,
        request: dataworks_public_20200518_models.TestNetworkConnectionRequest,
    ) -> dataworks_public_20200518_models.TestNetworkConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_network_connection_with_options_async(request, runtime)

    def top_ten_elapsed_time_instance_with_options(
        self,
        request: dataworks_public_20200518_models.TopTenElapsedTimeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse(),
            self.do_rpcrequest('TopTenElapsedTimeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def top_ten_elapsed_time_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.TopTenElapsedTimeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse(),
            await self.do_rpcrequest_async('TopTenElapsedTimeInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def top_ten_elapsed_time_instance(
        self,
        request: dataworks_public_20200518_models.TopTenElapsedTimeInstanceRequest,
    ) -> dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.top_ten_elapsed_time_instance_with_options(request, runtime)

    async def top_ten_elapsed_time_instance_async(
        self,
        request: dataworks_public_20200518_models.TopTenElapsedTimeInstanceRequest,
    ) -> dataworks_public_20200518_models.TopTenElapsedTimeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.top_ten_elapsed_time_instance_with_options_async(request, runtime)

    def top_ten_error_times_instance_with_options(
        self,
        request: dataworks_public_20200518_models.TopTenErrorTimesInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse(),
            self.do_rpcrequest('TopTenErrorTimesInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def top_ten_error_times_instance_with_options_async(
        self,
        request: dataworks_public_20200518_models.TopTenErrorTimesInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse(),
            await self.do_rpcrequest_async('TopTenErrorTimesInstance', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def top_ten_error_times_instance(
        self,
        request: dataworks_public_20200518_models.TopTenErrorTimesInstanceRequest,
    ) -> dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.top_ten_error_times_instance_with_options(request, runtime)

    async def top_ten_error_times_instance_async(
        self,
        request: dataworks_public_20200518_models.TopTenErrorTimesInstanceRequest,
    ) -> dataworks_public_20200518_models.TopTenErrorTimesInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.top_ten_error_times_instance_with_options_async(request, runtime)

    def update_business_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateBusinessResponse(),
            self.do_rpcrequest('UpdateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_business_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateBusinessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateBusinessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateBusinessResponse(),
            await self.do_rpcrequest_async('UpdateBusiness', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_business(
        self,
        request: dataworks_public_20200518_models.UpdateBusinessRequest,
    ) -> dataworks_public_20200518_models.UpdateBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_business_with_options(request, runtime)

    async def update_business_async(
        self,
        request: dataworks_public_20200518_models.UpdateBusinessRequest,
    ) -> dataworks_public_20200518_models.UpdateBusinessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_business_with_options_async(request, runtime)

    def update_connection_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateConnectionResponse(),
            self.do_rpcrequest('UpdateConnection', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def update_connection_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateConnectionResponse(),
            await self.do_rpcrequest_async('UpdateConnection', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_connection(
        self,
        request: dataworks_public_20200518_models.UpdateConnectionRequest,
    ) -> dataworks_public_20200518_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    async def update_connection_async(
        self,
        request: dataworks_public_20200518_models.UpdateConnectionRequest,
    ) -> dataworks_public_20200518_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_connection_with_options_async(request, runtime)

    def update_data_service_api_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataServiceApiResponse(),
            self.do_rpcrequest('UpdateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_data_service_api_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateDataServiceApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDataServiceApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataServiceApiResponse(),
            await self.do_rpcrequest_async('UpdateDataServiceApi', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_data_service_api(
        self,
        request: dataworks_public_20200518_models.UpdateDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.UpdateDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_service_api_with_options(request, runtime)

    async def update_data_service_api_async(
        self,
        request: dataworks_public_20200518_models.UpdateDataServiceApiRequest,
    ) -> dataworks_public_20200518_models.UpdateDataServiceApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_service_api_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataSourceResponse(),
            self.do_rpcrequest('UpdateDataSource', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDataSourceResponse(),
            await self.do_rpcrequest_async('UpdateDataSource', '2020-05-18', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def update_data_source(
        self,
        request: dataworks_public_20200518_models.UpdateDataSourceRequest,
    ) -> dataworks_public_20200518_models.UpdateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: dataworks_public_20200518_models.UpdateDataSourceRequest,
    ) -> dataworks_public_20200518_models.UpdateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_diproject_config_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateDIProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDIProjectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDIProjectConfigResponse(),
            self.do_rpcrequest('UpdateDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_diproject_config_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateDIProjectConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDIProjectConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDIProjectConfigResponse(),
            await self.do_rpcrequest_async('UpdateDIProjectConfig', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_diproject_config(
        self,
        request: dataworks_public_20200518_models.UpdateDIProjectConfigRequest,
    ) -> dataworks_public_20200518_models.UpdateDIProjectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_diproject_config_with_options(request, runtime)

    async def update_diproject_config_async(
        self,
        request: dataworks_public_20200518_models.UpdateDIProjectConfigRequest,
    ) -> dataworks_public_20200518_models.UpdateDIProjectConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_diproject_config_with_options_async(request, runtime)

    def update_disync_task_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDISyncTaskResponse(),
            self.do_rpcrequest('UpdateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_disync_task_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateDISyncTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateDISyncTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateDISyncTaskResponse(),
            await self.do_rpcrequest_async('UpdateDISyncTask', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_disync_task(
        self,
        request: dataworks_public_20200518_models.UpdateDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.UpdateDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_disync_task_with_options(request, runtime)

    async def update_disync_task_async(
        self,
        request: dataworks_public_20200518_models.UpdateDISyncTaskRequest,
    ) -> dataworks_public_20200518_models.UpdateDISyncTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_disync_task_with_options_async(request, runtime)

    def update_file_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFileResponse(),
            self.do_rpcrequest('UpdateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFileResponse(),
            await self.do_rpcrequest_async('UpdateFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_file(
        self,
        request: dataworks_public_20200518_models.UpdateFileRequest,
    ) -> dataworks_public_20200518_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_file_with_options(request, runtime)

    async def update_file_async(
        self,
        request: dataworks_public_20200518_models.UpdateFileRequest,
    ) -> dataworks_public_20200518_models.UpdateFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_file_with_options_async(request, runtime)

    def update_folder_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFolderResponse(),
            self.do_rpcrequest('UpdateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_folder_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateFolderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateFolderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateFolderResponse(),
            await self.do_rpcrequest_async('UpdateFolder', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_folder(
        self,
        request: dataworks_public_20200518_models.UpdateFolderRequest,
    ) -> dataworks_public_20200518_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    async def update_folder_async(
        self,
        request: dataworks_public_20200518_models.UpdateFolderRequest,
    ) -> dataworks_public_20200518_models.UpdateFolderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_folder_with_options_async(request, runtime)

    def update_meta_category_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaCategoryResponse(),
            self.do_rpcrequest('UpdateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_meta_category_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaCategoryResponse(),
            await self.do_rpcrequest_async('UpdateMetaCategory', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_category(
        self,
        request: dataworks_public_20200518_models.UpdateMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_meta_category_with_options(request, runtime)

    async def update_meta_category_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaCategoryRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_meta_category_with_options_async(request, runtime)

    def update_meta_table_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableResponse(),
            self.do_rpcrequest('UpdateMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_meta_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableResponse(),
            await self.do_rpcrequest_async('UpdateMetaTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_table(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_with_options(request, runtime)

    async def update_meta_table_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_meta_table_with_options_async(request, runtime)

    def update_meta_table_intro_wiki_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableIntroWikiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse(),
            self.do_rpcrequest('UpdateMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_meta_table_intro_wiki_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableIntroWikiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse(),
            await self.do_rpcrequest_async('UpdateMetaTableIntroWiki', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_meta_table_intro_wiki(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableIntroWikiRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_meta_table_intro_wiki_with_options(request, runtime)

    async def update_meta_table_intro_wiki_async(
        self,
        request: dataworks_public_20200518_models.UpdateMetaTableIntroWikiRequest,
    ) -> dataworks_public_20200518_models.UpdateMetaTableIntroWikiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_meta_table_intro_wiki_with_options_async(request, runtime)

    def update_node_owner_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateNodeOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateNodeOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeOwnerResponse(),
            self.do_rpcrequest('UpdateNodeOwner', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_node_owner_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateNodeOwnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateNodeOwnerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeOwnerResponse(),
            await self.do_rpcrequest_async('UpdateNodeOwner', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_node_owner(
        self,
        request: dataworks_public_20200518_models.UpdateNodeOwnerRequest,
    ) -> dataworks_public_20200518_models.UpdateNodeOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_node_owner_with_options(request, runtime)

    async def update_node_owner_async(
        self,
        request: dataworks_public_20200518_models.UpdateNodeOwnerRequest,
    ) -> dataworks_public_20200518_models.UpdateNodeOwnerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_node_owner_with_options_async(request, runtime)

    def update_node_run_mode_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateNodeRunModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateNodeRunModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeRunModeResponse(),
            self.do_rpcrequest('UpdateNodeRunMode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_node_run_mode_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateNodeRunModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateNodeRunModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateNodeRunModeResponse(),
            await self.do_rpcrequest_async('UpdateNodeRunMode', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_node_run_mode(
        self,
        request: dataworks_public_20200518_models.UpdateNodeRunModeRequest,
    ) -> dataworks_public_20200518_models.UpdateNodeRunModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_node_run_mode_with_options(request, runtime)

    async def update_node_run_mode_async(
        self,
        request: dataworks_public_20200518_models.UpdateNodeRunModeRequest,
    ) -> dataworks_public_20200518_models.UpdateNodeRunModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_node_run_mode_with_options_async(request, runtime)

    def update_quality_follower_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityFollowerResponse(),
            self.do_rpcrequest('UpdateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_quality_follower_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateQualityFollowerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateQualityFollowerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityFollowerResponse(),
            await self.do_rpcrequest_async('UpdateQualityFollower', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_quality_follower(
        self,
        request: dataworks_public_20200518_models.UpdateQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.UpdateQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_quality_follower_with_options(request, runtime)

    async def update_quality_follower_async(
        self,
        request: dataworks_public_20200518_models.UpdateQualityFollowerRequest,
    ) -> dataworks_public_20200518_models.UpdateQualityFollowerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_follower_with_options_async(request, runtime)

    def update_quality_rule_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityRuleResponse(),
            self.do_rpcrequest('UpdateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_quality_rule_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateQualityRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateQualityRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateQualityRuleResponse(),
            await self.do_rpcrequest_async('UpdateQualityRule', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_quality_rule(
        self,
        request: dataworks_public_20200518_models.UpdateQualityRuleRequest,
    ) -> dataworks_public_20200518_models.UpdateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_quality_rule_with_options(request, runtime)

    async def update_quality_rule_async(
        self,
        request: dataworks_public_20200518_models.UpdateQualityRuleRequest,
    ) -> dataworks_public_20200518_models.UpdateQualityRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_rule_with_options_async(request, runtime)

    def update_remind_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateRemindResponse(),
            self.do_rpcrequest('UpdateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_remind_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateRemindRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateRemindResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateRemindResponse(),
            await self.do_rpcrequest_async('UpdateRemind', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_remind(
        self,
        request: dataworks_public_20200518_models.UpdateRemindRequest,
    ) -> dataworks_public_20200518_models.UpdateRemindResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_remind_with_options(request, runtime)

    async def update_remind_async(
        self,
        request: dataworks_public_20200518_models.UpdateRemindRequest,
    ) -> dataworks_public_20200518_models.UpdateRemindResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_remind_with_options_async(request, runtime)

    def update_table_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableResponse(),
            self.do_rpcrequest('UpdateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_table_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableResponse(),
            await self.do_rpcrequest_async('UpdateTable', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table(
        self,
        request: dataworks_public_20200518_models.UpdateTableRequest,
    ) -> dataworks_public_20200518_models.UpdateTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_table_with_options(request, runtime)

    async def update_table_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableRequest,
    ) -> dataworks_public_20200518_models.UpdateTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_table_with_options_async(request, runtime)

    def update_table_add_column_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateTableAddColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableAddColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableAddColumnResponse(),
            self.do_rpcrequest('UpdateTableAddColumn', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_table_add_column_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableAddColumnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableAddColumnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableAddColumnResponse(),
            await self.do_rpcrequest_async('UpdateTableAddColumn', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_add_column(
        self,
        request: dataworks_public_20200518_models.UpdateTableAddColumnRequest,
    ) -> dataworks_public_20200518_models.UpdateTableAddColumnResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_table_add_column_with_options(request, runtime)

    async def update_table_add_column_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableAddColumnRequest,
    ) -> dataworks_public_20200518_models.UpdateTableAddColumnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_table_add_column_with_options_async(request, runtime)

    def update_table_level_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableLevelResponse(),
            self.do_rpcrequest('UpdateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_table_level_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableLevelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableLevelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableLevelResponse(),
            await self.do_rpcrequest_async('UpdateTableLevel', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_level(
        self,
        request: dataworks_public_20200518_models.UpdateTableLevelRequest,
    ) -> dataworks_public_20200518_models.UpdateTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_table_level_with_options(request, runtime)

    async def update_table_level_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableLevelRequest,
    ) -> dataworks_public_20200518_models.UpdateTableLevelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_table_level_with_options_async(request, runtime)

    def update_table_model_info_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateTableModelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableModelInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableModelInfoResponse(),
            self.do_rpcrequest('UpdateTableModelInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_table_model_info_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableModelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableModelInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableModelInfoResponse(),
            await self.do_rpcrequest_async('UpdateTableModelInfo', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_model_info(
        self,
        request: dataworks_public_20200518_models.UpdateTableModelInfoRequest,
    ) -> dataworks_public_20200518_models.UpdateTableModelInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_table_model_info_with_options(request, runtime)

    async def update_table_model_info_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableModelInfoRequest,
    ) -> dataworks_public_20200518_models.UpdateTableModelInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_table_model_info_with_options_async(request, runtime)

    def update_table_theme_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableThemeResponse(),
            self.do_rpcrequest('UpdateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_table_theme_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableThemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateTableThemeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateTableThemeResponse(),
            await self.do_rpcrequest_async('UpdateTableTheme', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_table_theme(
        self,
        request: dataworks_public_20200518_models.UpdateTableThemeRequest,
    ) -> dataworks_public_20200518_models.UpdateTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_table_theme_with_options(request, runtime)

    async def update_table_theme_async(
        self,
        request: dataworks_public_20200518_models.UpdateTableThemeRequest,
    ) -> dataworks_public_20200518_models.UpdateTableThemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_table_theme_with_options_async(request, runtime)

    def update_udf_file_with_options(
        self,
        request: dataworks_public_20200518_models.UpdateUdfFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateUdfFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateUdfFileResponse(),
            self.do_rpcrequest('UpdateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_udf_file_with_options_async(
        self,
        request: dataworks_public_20200518_models.UpdateUdfFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dataworks_public_20200518_models.UpdateUdfFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dataworks_public_20200518_models.UpdateUdfFileResponse(),
            await self.do_rpcrequest_async('UpdateUdfFile', '2020-05-18', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_udf_file(
        self,
        request: dataworks_public_20200518_models.UpdateUdfFileRequest,
    ) -> dataworks_public_20200518_models.UpdateUdfFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_udf_file_with_options(request, runtime)

    async def update_udf_file_async(
        self,
        request: dataworks_public_20200518_models.UpdateUdfFileRequest,
    ) -> dataworks_public_20200518_models.UpdateUdfFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_udf_file_with_options_async(request, runtime)
