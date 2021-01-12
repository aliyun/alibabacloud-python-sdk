# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rds20140815 import models as rds_20140815_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'rds.aliyuncs.com',
            'cn-beijing': 'rds.aliyuncs.com',
            'cn-hangzhou': 'rds.aliyuncs.com',
            'cn-shanghai': 'rds.aliyuncs.com',
            'cn-shenzhen': 'rds.aliyuncs.com',
            'cn-hongkong': 'rds.aliyuncs.com',
            'ap-southeast-1': 'rds.aliyuncs.com',
            'us-west-1': 'rds.aliyuncs.com',
            'us-east-1': 'rds.aliyuncs.com',
            'cn-shanghai-finance-1': 'rds.aliyuncs.com',
            'cn-shenzhen-finance-1': 'rds.aliyuncs.com',
            'cn-north-2-gov-1': 'rds.aliyuncs.com',
            'ap-northeast-2-pop': 'rds.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'rds.aliyuncs.com',
            'cn-beijing-finance-pop': 'rds.aliyuncs.com',
            'cn-beijing-gov-1': 'rds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'rds.aliyuncs.com',
            'cn-edge-1': 'rds.aliyuncs.com',
            'cn-fujian': 'rds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'rds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'rds.aliyuncs.com',
            'cn-hangzhou-finance': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'rds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'rds.aliyuncs.com',
            'cn-hangzhou-test-306': 'rds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'rds.aliyuncs.com',
            'cn-qingdao-nebula': 'rds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'rds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'rds.aliyuncs.com',
            'cn-shanghai-inner': 'rds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'rds.aliyuncs.com',
            'cn-shenzhen-inner': 'rds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'rds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'rds.aliyuncs.com',
            'cn-wuhan': 'rds.aliyuncs.com',
            'cn-yushanfang': 'rds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'rds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'rds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'rds.aliyuncs.com',
            'eu-west-1-oxs': 'rds.ap-northeast-1.aliyuncs.com',
            'rus-west-1-pop': 'rds.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('rds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_tags_to_resource_with_options(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.AddTagsToResourceResponse().from_map(
            self.do_rpcrequest('AddTagsToResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_to_resource_with_options_async(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.AddTagsToResourceResponse().from_map(
            await self.do_rpcrequest_async('AddTagsToResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags_to_resource(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    async def add_tags_to_resource_async(
        self,
        request: rds_20140815_models.AddTagsToResourceRequest,
    ) -> rds_20140815_models.AddTagsToResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_to_resource_with_options_async(request, runtime)

    def allocate_instance_public_connection_with_options(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.AllocateInstancePublicConnectionResponse().from_map(
            self.do_rpcrequest('AllocateInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_instance_public_connection_with_options_async(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.AllocateInstancePublicConnectionResponse().from_map(
            await self.do_rpcrequest_async('AllocateInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_instance_public_connection(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    async def allocate_instance_public_connection_async(
        self,
        request: rds_20140815_models.AllocateInstancePublicConnectionRequest,
    ) -> rds_20140815_models.AllocateInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_instance_public_connection_with_options_async(request, runtime)

    def calculate_dbinstance_weight_with_options(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CalculateDBInstanceWeightResponse().from_map(
            self.do_rpcrequest('CalculateDBInstanceWeight', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def calculate_dbinstance_weight_with_options_async(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CalculateDBInstanceWeightResponse().from_map(
            await self.do_rpcrequest_async('CalculateDBInstanceWeight', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def calculate_dbinstance_weight(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    async def calculate_dbinstance_weight_async(
        self,
        request: rds_20140815_models.CalculateDBInstanceWeightRequest,
    ) -> rds_20140815_models.CalculateDBInstanceWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.calculate_dbinstance_weight_with_options_async(request, runtime)

    def cancel_import_with_options(
        self,
        request: rds_20140815_models.CancelImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CancelImportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CancelImportResponse().from_map(
            self.do_rpcrequest('CancelImport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_import_with_options_async(
        self,
        request: rds_20140815_models.CancelImportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CancelImportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CancelImportResponse().from_map(
            await self.do_rpcrequest_async('CancelImport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_import(
        self,
        request: rds_20140815_models.CancelImportRequest,
    ) -> rds_20140815_models.CancelImportResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    async def cancel_import_async(
        self,
        request: rds_20140815_models.CancelImportRequest,
    ) -> rds_20140815_models.CancelImportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_import_with_options_async(request, runtime)

    def check_create_ddr_dbinstance_with_options(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckCreateDdrDBInstanceResponse().from_map(
            self.do_rpcrequest('CheckCreateDdrDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_create_ddr_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckCreateDdrDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CheckCreateDdrDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_create_ddr_dbinstance(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    async def check_create_ddr_dbinstance_async(
        self,
        request: rds_20140815_models.CheckCreateDdrDBInstanceRequest,
    ) -> rds_20140815_models.CheckCreateDdrDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_create_ddr_dbinstance_with_options_async(request, runtime)

    def check_dbname_available_with_options(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckDBNameAvailableResponse().from_map(
            self.do_rpcrequest('CheckDBNameAvailable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_dbname_available_with_options_async(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckDBNameAvailableResponse().from_map(
            await self.do_rpcrequest_async('CheckDBNameAvailable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_dbname_available(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    async def check_dbname_available_async(
        self,
        request: rds_20140815_models.CheckDBNameAvailableRequest,
    ) -> rds_20140815_models.CheckDBNameAvailableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_dbname_available_with_options_async(request, runtime)

    def check_instance_exist_with_options(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckInstanceExistResponse().from_map(
            self.do_rpcrequest('CheckInstanceExist', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_instance_exist_with_options_async(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CheckInstanceExistResponse().from_map(
            await self.do_rpcrequest_async('CheckInstanceExist', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_instance_exist(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    async def check_instance_exist_async(
        self,
        request: rds_20140815_models.CheckInstanceExistRequest,
    ) -> rds_20140815_models.CheckInstanceExistResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_instance_exist_with_options_async(request, runtime)

    def clear_dedicated_host_with_options(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ClearDedicatedHostResponse().from_map(
            self.do_rpcrequest('ClearDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ClearDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('ClearDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_dedicated_host(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    async def clear_dedicated_host_async(
        self,
        request: rds_20140815_models.ClearDedicatedHostRequest,
    ) -> rds_20140815_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_dedicated_host_with_options_async(request, runtime)

    def clone_dbinstance_with_options(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CloneDBInstanceResponse().from_map(
            self.do_rpcrequest('CloneDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CloneDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CloneDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_dbinstance(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    async def clone_dbinstance_async(
        self,
        request: rds_20140815_models.CloneDBInstanceRequest,
    ) -> rds_20140815_models.CloneDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_dbinstance_with_options_async(request, runtime)

    def clone_parameter_group_with_options(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CloneParameterGroupResponse().from_map(
            self.do_rpcrequest('CloneParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CloneParameterGroupResponse().from_map(
            await self.do_rpcrequest_async('CloneParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_parameter_group(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    async def clone_parameter_group_async(
        self,
        request: rds_20140815_models.CloneParameterGroupRequest,
    ) -> rds_20140815_models.CloneParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_parameter_group_with_options_async(request, runtime)

    def copy_database_with_options(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CopyDatabaseResponse().from_map(
            self.do_rpcrequest('CopyDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_database_with_options_async(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CopyDatabaseResponse().from_map(
            await self.do_rpcrequest_async('CopyDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_database(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    async def copy_database_async(
        self,
        request: rds_20140815_models.CopyDatabaseRequest,
    ) -> rds_20140815_models.CopyDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_database_with_options_async(request, runtime)

    def copy_database_between_instances_with_options(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CopyDatabaseBetweenInstancesResponse().from_map(
            self.do_rpcrequest('CopyDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_database_between_instances_with_options_async(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CopyDatabaseBetweenInstancesResponse().from_map(
            await self.do_rpcrequest_async('CopyDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_database_between_instances(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    async def copy_database_between_instances_async(
        self,
        request: rds_20140815_models.CopyDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.CopyDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_database_between_instances_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: rds_20140815_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateAccountResponse().from_map(
            self.do_rpcrequest('CreateAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: rds_20140815_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_account(
        self,
        request: rds_20140815_models.CreateAccountRequest,
    ) -> rds_20140815_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: rds_20140815_models.CreateAccountRequest,
    ) -> rds_20140815_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: rds_20140815_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateBackupResponse().from_map(
            self.do_rpcrequest('CreateBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: rds_20140815_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateBackupResponse().from_map(
            await self.do_rpcrequest_async('CreateBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: rds_20140815_models.CreateBackupRequest,
    ) -> rds_20140815_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: rds_20140815_models.CreateBackupRequest,
    ) -> rds_20140815_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_database_with_options(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDatabaseResponse().from_map(
            self.do_rpcrequest('CreateDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_database_with_options_async(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDatabaseResponse().from_map(
            await self.do_rpcrequest_async('CreateDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_database(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    async def create_database_async(
        self,
        request: rds_20140815_models.CreateDatabaseRequest,
    ) -> rds_20140815_models.CreateDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_database_with_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbinstance(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: rds_20140815_models.CreateDBInstanceRequest,
    ) -> rds_20140815_models.CreateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDBProxyEndpointAddressResponse().from_map(
            self.do_rpcrequest('CreateDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDBProxyEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('CreateDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    async def create_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.CreateDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.CreateDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dbproxy_endpoint_address_with_options_async(request, runtime)

    def create_ddr_instance_with_options(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDdrInstanceResponse().from_map(
            self.do_rpcrequest('CreateDdrInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ddr_instance_with_options_async(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDdrInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateDdrInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ddr_instance(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    async def create_ddr_instance_async(
        self,
        request: rds_20140815_models.CreateDdrInstanceRequest,
    ) -> rds_20140815_models.CreateDdrInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ddr_instance_with_options_async(request, runtime)

    def create_dedicated_host_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostResponse().from_map(
            self.do_rpcrequest('CreateDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('CreateDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    async def create_dedicated_host_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostRequest,
    ) -> rds_20140815_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_with_options_async(request, runtime)

    def create_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostAccountResponse().from_map(
            self.do_rpcrequest('CreateDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_account(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    async def create_dedicated_host_account_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostAccountRequest,
    ) -> rds_20140815_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_account_with_options_async(request, runtime)

    def create_dedicated_host_group_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostGroupResponse().from_map(
            self.do_rpcrequest('CreateDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_group_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_group(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    async def create_dedicated_host_group_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostGroupRequest,
    ) -> rds_20140815_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_group_with_options_async(request, runtime)

    def create_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostUserResponse().from_map(
            self.do_rpcrequest('CreateDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDedicatedHostUserResponse().from_map(
            await self.do_rpcrequest_async('CreateDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_user(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_user_with_options(request, runtime)

    async def create_dedicated_host_user_async(
        self,
        request: rds_20140815_models.CreateDedicatedHostUserRequest,
    ) -> rds_20140815_models.CreateDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_user_with_options_async(request, runtime)

    def create_diagnostic_report_with_options(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDiagnosticReportResponse().from_map(
            self.do_rpcrequest('CreateDiagnosticReport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_diagnostic_report_with_options_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateDiagnosticReportResponse().from_map(
            await self.do_rpcrequest_async('CreateDiagnosticReport', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_diagnostic_report(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    async def create_diagnostic_report_async(
        self,
        request: rds_20140815_models.CreateDiagnosticReportRequest,
    ) -> rds_20140815_models.CreateDiagnosticReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_report_with_options_async(request, runtime)

    def create_host_account_with_options(
        self,
        request: rds_20140815_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateHostAccountResponse().from_map(
            self.do_rpcrequest('CreateHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_host_account_with_options_async(
        self,
        request: rds_20140815_models.CreateHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateHostAccountResponse().from_map(
            await self.do_rpcrequest_async('CreateHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_host_account(
        self,
        request: rds_20140815_models.CreateHostAccountRequest,
    ) -> rds_20140815_models.CreateHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    async def create_host_account_async(
        self,
        request: rds_20140815_models.CreateHostAccountRequest,
    ) -> rds_20140815_models.CreateHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_account_with_options_async(request, runtime)

    def create_migrate_task_with_options(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateMigrateTaskResponse().from_map(
            self.do_rpcrequest('CreateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_migrate_task_with_options_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateMigrateTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_migrate_task(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    async def create_migrate_task_async(
        self,
        request: rds_20140815_models.CreateMigrateTaskRequest,
    ) -> rds_20140815_models.CreateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migrate_task_with_options_async(request, runtime)

    def create_online_database_task_with_options(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateOnlineDatabaseTaskResponse().from_map(
            self.do_rpcrequest('CreateOnlineDatabaseTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_online_database_task_with_options_async(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateOnlineDatabaseTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateOnlineDatabaseTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_online_database_task(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    async def create_online_database_task_async(
        self,
        request: rds_20140815_models.CreateOnlineDatabaseTaskRequest,
    ) -> rds_20140815_models.CreateOnlineDatabaseTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_online_database_task_with_options_async(request, runtime)

    def create_parameter_group_with_options(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateParameterGroupResponse().from_map(
            self.do_rpcrequest('CreateParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateParameterGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_parameter_group(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    async def create_parameter_group_async(
        self,
        request: rds_20140815_models.CreateParameterGroupRequest,
    ) -> rds_20140815_models.CreateParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_parameter_group_with_options_async(request, runtime)

    def create_read_only_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateReadOnlyDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateReadOnlyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_read_only_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateReadOnlyDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateReadOnlyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_read_only_dbinstance(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    async def create_read_only_dbinstance_async(
        self,
        request: rds_20140815_models.CreateReadOnlyDBInstanceRequest,
    ) -> rds_20140815_models.CreateReadOnlyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_read_only_dbinstance_with_options_async(request, runtime)

    def create_temp_dbinstance_with_options(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateTempDBInstanceResponse().from_map(
            self.do_rpcrequest('CreateTempDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_temp_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.CreateTempDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateTempDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_temp_dbinstance(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    async def create_temp_dbinstance_async(
        self,
        request: rds_20140815_models.CreateTempDBInstanceRequest,
    ) -> rds_20140815_models.CreateTempDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_temp_dbinstance_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteAccountResponse().from_map(
            self.do_rpcrequest('DeleteAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_account(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
    ) -> rds_20140815_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: rds_20140815_models.DeleteAccountRequest,
    ) -> rds_20140815_models.DeleteAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteBackupResponse().from_map(
            self.do_rpcrequest('DeleteBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteBackupResponse().from_map(
            await self.do_rpcrequest_async('DeleteBackup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
    ) -> rds_20140815_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: rds_20140815_models.DeleteBackupRequest,
    ) -> rds_20140815_models.DeleteBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_backup_file_with_options(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteBackupFileResponse().from_map(
            self.do_rpcrequest('DeleteBackupFile', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_backup_file_with_options_async(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteBackupFileResponse().from_map(
            await self.do_rpcrequest_async('DeleteBackupFile', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_backup_file(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    async def delete_backup_file_async(
        self,
        request: rds_20140815_models.DeleteBackupFileRequest,
    ) -> rds_20140815_models.DeleteBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_file_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDatabaseResponse().from_map(
            self.do_rpcrequest('DeleteDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDatabaseResponse().from_map(
            await self.do_rpcrequest_async('DeleteDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_database(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: rds_20140815_models.DeleteDatabaseRequest,
    ) -> rds_20140815_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDBInstanceResponse().from_map(
            self.do_rpcrequest('DeleteDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbinstance(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: rds_20140815_models.DeleteDBInstanceRequest,
    ) -> rds_20140815_models.DeleteDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDBProxyEndpointAddressResponse().from_map(
            self.do_rpcrequest('DeleteDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDBProxyEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('DeleteDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    async def delete_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.DeleteDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.DeleteDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbproxy_endpoint_address_with_options_async(request, runtime)

    def delete_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDedicatedHostAccountResponse().from_map(
            self.do_rpcrequest('DeleteDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDedicatedHostAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_account(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    async def delete_dedicated_host_account_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostAccountRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_group_with_options(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDedicatedHostGroupResponse().from_map(
            self.do_rpcrequest('DeleteDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_host_group_with_options_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteDedicatedHostGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteDedicatedHostGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_group(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    async def delete_dedicated_host_group_async(
        self,
        request: rds_20140815_models.DeleteDedicatedHostGroupRequest,
    ) -> rds_20140815_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_group_with_options_async(request, runtime)

    def delete_host_account_with_options(
        self,
        request: rds_20140815_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteHostAccountResponse().from_map(
            self.do_rpcrequest('DeleteHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_host_account_with_options_async(
        self,
        request: rds_20140815_models.DeleteHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteHostAccountResponse().from_map(
            await self.do_rpcrequest_async('DeleteHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_host_account(
        self,
        request: rds_20140815_models.DeleteHostAccountRequest,
    ) -> rds_20140815_models.DeleteHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    async def delete_host_account_async(
        self,
        request: rds_20140815_models.DeleteHostAccountRequest,
    ) -> rds_20140815_models.DeleteHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_host_account_with_options_async(request, runtime)

    def delete_parameter_group_with_options(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteParameterGroupResponse().from_map(
            self.do_rpcrequest('DeleteParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DeleteParameterGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_parameter_group(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    async def delete_parameter_group_async(
        self,
        request: rds_20140815_models.DeleteParameterGroupRequest,
    ) -> rds_20140815_models.DeleteParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_parameter_group_with_options_async(request, runtime)

    def descibe_imports_from_database_with_options(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescibeImportsFromDatabaseResponse().from_map(
            self.do_rpcrequest('DescibeImportsFromDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def descibe_imports_from_database_with_options_async(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescibeImportsFromDatabaseResponse().from_map(
            await self.do_rpcrequest_async('DescibeImportsFromDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def descibe_imports_from_database(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    async def descibe_imports_from_database_async(
        self,
        request: rds_20140815_models.DescibeImportsFromDatabaseRequest,
    ) -> rds_20140815_models.DescibeImportsFromDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.descibe_imports_from_database_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAccountsResponse().from_map(
            self.do_rpcrequest('DescribeAccounts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccounts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_accounts(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: rds_20140815_models.DescribeAccountsRequest,
    ) -> rds_20140815_models.DescribeAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_action_event_policy_with_options(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeActionEventPolicyResponse().from_map(
            self.do_rpcrequest('DescribeActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_action_event_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeActionEventPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_action_event_policy(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    async def describe_action_event_policy_async(
        self,
        request: rds_20140815_models.DescribeActionEventPolicyRequest,
    ) -> rds_20140815_models.DescribeActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_action_event_policy_with_options_async(request, runtime)

    def describe_available_cross_region_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableCrossRegionResponse().from_map(
            self.do_rpcrequest('DescribeAvailableCrossRegion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_cross_region_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableCrossRegionResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableCrossRegion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_cross_region(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    async def describe_available_cross_region_async(
        self,
        request: rds_20140815_models.DescribeAvailableCrossRegionRequest,
    ) -> rds_20140815_models.DescribeAvailableCrossRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_cross_region_with_options_async(request, runtime)

    def describe_available_dedicated_host_classes_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse().from_map(
            self.do_rpcrequest('DescribeAvailableDedicatedHostClasses', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_dedicated_host_classes_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableDedicatedHostClasses', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_classes(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    async def describe_available_dedicated_host_classes_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_classes_with_options_async(request, runtime)

    def describe_available_dedicated_host_zones_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse().from_map(
            self.do_rpcrequest('DescribeAvailableDedicatedHostZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_dedicated_host_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableDedicatedHostZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_zones(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    async def describe_available_dedicated_host_zones_async(
        self,
        request: rds_20140815_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_zones_with_options_async(request, runtime)

    def describe_available_recovery_time_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableRecoveryTimeResponse().from_map(
            self.do_rpcrequest('DescribeAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_recovery_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableRecoveryTimeResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_recovery_time(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    async def describe_available_recovery_time_async(
        self,
        request: rds_20140815_models.DescribeAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_recovery_time_with_options_async(request, runtime)

    def describe_available_zones_with_options(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableZonesResponse().from_map(
            self.do_rpcrequest('DescribeAvailableZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeAvailableZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_zones(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    async def describe_available_zones_async(
        self,
        request: rds_20140815_models.DescribeAvailableZonesRequest,
    ) -> rds_20140815_models.DescribeAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_zones_with_options_async(request, runtime)

    def describe_backup_database_with_options(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupDatabaseResponse().from_map(
            self.do_rpcrequest('DescribeBackupDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_database_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupDatabaseResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupDatabase', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_database(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    async def describe_backup_database_async(
        self,
        request: rds_20140815_models.DescribeBackupDatabaseRequest,
    ) -> rds_20140815_models.DescribeBackupDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_database_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: rds_20140815_models.DescribeBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupsResponse().from_map(
            self.do_rpcrequest('DescribeBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backups(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: rds_20140815_models.DescribeBackupsRequest,
    ) -> rds_20140815_models.DescribeBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_backup_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupTasksResponse().from_map(
            self.do_rpcrequest('DescribeBackupTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBackupTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeBackupTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_tasks(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    async def describe_backup_tasks_async(
        self,
        request: rds_20140815_models.DescribeBackupTasksRequest,
    ) -> rds_20140815_models.DescribeBackupTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_tasks_with_options_async(request, runtime)

    def describe_binlog_files_with_options(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBinlogFilesResponse().from_map(
            self.do_rpcrequest('DescribeBinlogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_binlog_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeBinlogFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeBinlogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_binlog_files(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    async def describe_binlog_files_async(
        self,
        request: rds_20140815_models.DescribeBinlogFilesRequest,
    ) -> rds_20140815_models.DescribeBinlogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_binlog_files_with_options_async(request, runtime)

    def describe_character_set_name_with_options(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCharacterSetNameResponse().from_map(
            self.do_rpcrequest('DescribeCharacterSetName', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_character_set_name_with_options_async(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCharacterSetNameResponse().from_map(
            await self.do_rpcrequest_async('DescribeCharacterSetName', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_character_set_name(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    async def describe_character_set_name_async(
        self,
        request: rds_20140815_models.DescribeCharacterSetNameRequest,
    ) -> rds_20140815_models.DescribeCharacterSetNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_character_set_name_with_options_async(request, runtime)

    def describe_collation_time_zones_with_options(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCollationTimeZonesResponse().from_map(
            self.do_rpcrequest('DescribeCollationTimeZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_collation_time_zones_with_options_async(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCollationTimeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCollationTimeZones', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_collation_time_zones(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    async def describe_collation_time_zones_async(
        self,
        request: rds_20140815_models.DescribeCollationTimeZonesRequest,
    ) -> rds_20140815_models.DescribeCollationTimeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_collation_time_zones_with_options_async(request, runtime)

    def describe_cross_backup_meta_list_with_options(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossBackupMetaListResponse().from_map(
            self.do_rpcrequest('DescribeCrossBackupMetaList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cross_backup_meta_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossBackupMetaListResponse().from_map(
            await self.do_rpcrequest_async('DescribeCrossBackupMetaList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_backup_meta_list(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    async def describe_cross_backup_meta_list_async(
        self,
        request: rds_20140815_models.DescribeCrossBackupMetaListRequest,
    ) -> rds_20140815_models.DescribeCrossBackupMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_backup_meta_list_with_options_async(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse().from_map(
            self.do_rpcrequest('DescribeCrossRegionBackupDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cross_region_backup_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeCrossRegionBackupDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_backup_dbinstance(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    async def describe_cross_region_backup_dbinstance_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupDBInstanceRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_backup_dbinstance_with_options_async(request, runtime)

    def describe_cross_region_backups_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionBackupsResponse().from_map(
            self.do_rpcrequest('DescribeCrossRegionBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cross_region_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCrossRegionBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_backups(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    async def describe_cross_region_backups_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionBackupsRequest,
    ) -> rds_20140815_models.DescribeCrossRegionBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_backups_with_options_async(request, runtime)

    def describe_cross_region_log_backup_files_with_options(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse().from_map(
            self.do_rpcrequest('DescribeCrossRegionLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cross_region_log_backup_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCrossRegionLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_region_log_backup_files(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    async def describe_cross_region_log_backup_files_async(
        self,
        request: rds_20140815_models.DescribeCrossRegionLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_region_log_backup_files_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDatabasesResponse().from_map(
            self.do_rpcrequest('DescribeDatabases', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDatabasesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDatabases', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_databases(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: rds_20140815_models.DescribeDatabasesRequest,
    ) -> rds_20140815_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceAttributeRequest,
    ) -> rds_20140815_models.DescribeDBInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_detail_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceDetailResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceDetail', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_detail_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceDetail', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_detail(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    async def describe_dbinstance_detail_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceDetailRequest,
    ) -> rds_20140815_models.DescribeDBInstanceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_detail_with_options_async(request, runtime)

    def describe_dbinstance_haconfig_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceHAConfigResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_haconfig_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceHAConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_haconfig(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    async def describe_dbinstance_haconfig_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.DescribeDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_haconfig_with_options_async(request, runtime)

    def describe_dbinstance_iparray_list_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceIPArrayListResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceIPArrayList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_iparray_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceIPArrayListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceIPArrayList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_iparray_list(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    async def describe_dbinstance_iparray_list_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIPArrayListRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIPArrayListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_iparray_list_with_options_async(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceIpHostnameResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceIpHostname', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_ip_hostname_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceIpHostnameResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceIpHostname', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ip_hostname(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    async def describe_dbinstance_ip_hostname_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceIpHostnameRequest,
    ) -> rds_20140815_models.DescribeDBInstanceIpHostnameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_ip_hostname_with_options_async(request, runtime)

    def describe_dbinstance_monitor_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceMonitorResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_monitor_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceMonitorResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_monitor(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    async def describe_dbinstance_monitor_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceMonitorRequest,
    ) -> rds_20140815_models.DescribeDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_monitor_with_options_async(request, runtime)

    def describe_dbinstance_net_info_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceNetInfoResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceNetInfo', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_net_info_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceNetInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceNetInfo', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_net_info(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    async def describe_dbinstance_net_info_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceNetInfoRequest,
    ) -> rds_20140815_models.DescribeDBInstanceNetInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_net_info_with_options_async(request, runtime)

    def describe_dbinstance_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancePerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancePerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancePerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancePerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_performance(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    async def describe_dbinstance_performance_async(
        self,
        request: rds_20140815_models.DescribeDBInstancePerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancePerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_performance_with_options_async(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_proxy_configuration_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_proxy_configuration(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    async def describe_dbinstance_proxy_configuration_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_proxy_configuration_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesResponse().from_map(
            self.do_rpcrequest('DescribeDBInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesRequest,
    ) -> rds_20140815_models.DescribeDBInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_dbinstances_as_csv_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesAsCsvResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancesAsCsv', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_as_csv_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesAsCsvResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancesAsCsv', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_as_csv(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    async def describe_dbinstances_as_csv_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesAsCsvRequest,
    ) -> rds_20140815_models.DescribeDBInstancesAsCsvResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_as_csv_with_options_async(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesByExpireTimeResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancesByExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_by_expire_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesByExpireTimeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancesByExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_by_expire_time(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    async def describe_dbinstances_by_expire_time_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByExpireTimeRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_by_expire_time_with_options_async(request, runtime)

    def describe_dbinstances_by_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesByPerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancesByPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_by_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesByPerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancesByPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_by_performance(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    async def describe_dbinstances_by_performance_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesByPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBInstancesByPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_by_performance_with_options_async(request, runtime)

    def describe_dbinstances_for_clone_with_options(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesForCloneResponse().from_map(
            self.do_rpcrequest('DescribeDBInstancesForClone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstances_for_clone_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstancesForCloneResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstancesForClone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstances_for_clone(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    async def describe_dbinstances_for_clone_async(
        self,
        request: rds_20140815_models.DescribeDBInstancesForCloneRequest,
    ) -> rds_20140815_models.DescribeDBInstancesForCloneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_for_clone_with_options_async(request, runtime)

    def describe_dbinstance_sslwith_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceSSLResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_sslwith_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceSSLResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_ssl(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    async def describe_dbinstance_ssl_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceSSLRequest,
    ) -> rds_20140815_models.DescribeDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_sslwith_options_async(request, runtime)

    def describe_dbinstance_tdewith_options(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceTDEResponse().from_map(
            self.do_rpcrequest('DescribeDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbinstance_tdewith_options_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBInstanceTDEResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbinstance_tde(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    async def describe_dbinstance_tde_async(
        self,
        request: rds_20140815_models.DescribeDBInstanceTDERequest,
    ) -> rds_20140815_models.DescribeDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_tdewith_options_async(request, runtime)

    def describe_dbproxy_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyResponse().from_map(
            self.do_rpcrequest('DescribeDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbproxy_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    async def describe_dbproxy_async(
        self,
        request: rds_20140815_models.DescribeDBProxyRequest,
    ) -> rds_20140815_models.DescribeDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_with_options_async(request, runtime)

    def describe_dbproxy_endpoint_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyEndpointResponse().from_map(
            self.do_rpcrequest('DescribeDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbproxy_endpoint_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyEndpointResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy_endpoint(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    async def describe_dbproxy_endpoint_async(
        self,
        request: rds_20140815_models.DescribeDBProxyEndpointRequest,
    ) -> rds_20140815_models.DescribeDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_endpoint_with_options_async(request, runtime)

    def describe_dbproxy_performance_with_options(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyPerformanceResponse().from_map(
            self.do_rpcrequest('DescribeDBProxyPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dbproxy_performance_with_options_async(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDBProxyPerformanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDBProxyPerformance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dbproxy_performance(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    async def describe_dbproxy_performance_async(
        self,
        request: rds_20140815_models.DescribeDBProxyPerformanceRequest,
    ) -> rds_20140815_models.DescribeDBProxyPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbproxy_performance_with_options_async(request, runtime)

    def describe_dedicated_host_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostAttributeResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_attribute(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    async def describe_dedicated_host_attribute_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_attribute_with_options_async(request, runtime)

    def describe_dedicated_host_groups_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostGroupsResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_groups_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_groups(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    async def describe_dedicated_host_groups_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostGroupsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_groups_with_options_async(request, runtime)

    def describe_dedicated_host_image_categories_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostImageCategories', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_image_categories_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostImageCategories', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_image_categories(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_image_categories_with_options(request, runtime)

    async def describe_dedicated_host_image_categories_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostImageCategoriesRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_image_categories_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostsResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHosts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDedicatedHostsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHosts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: rds_20140815_models.DescribeDedicatedHostsRequest,
    ) -> rds_20140815_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_detached_backups_with_options(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDetachedBackupsResponse().from_map(
            self.do_rpcrequest('DescribeDetachedBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_detached_backups_with_options_async(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDetachedBackupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDetachedBackups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_detached_backups(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    async def describe_detached_backups_async(
        self,
        request: rds_20140815_models.DescribeDetachedBackupsRequest,
    ) -> rds_20140815_models.DescribeDetachedBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_detached_backups_with_options_async(request, runtime)

    def describe_diagnostic_report_list_with_options(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDiagnosticReportListResponse().from_map(
            self.do_rpcrequest('DescribeDiagnosticReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_diagnostic_report_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDiagnosticReportListResponse().from_map(
            await self.do_rpcrequest_async('DescribeDiagnosticReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_diagnostic_report_list(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    async def describe_diagnostic_report_list_async(
        self,
        request: rds_20140815_models.DescribeDiagnosticReportListRequest,
    ) -> rds_20140815_models.DescribeDiagnosticReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_report_list_with_options_async(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse().from_map(
            self.do_rpcrequest('DescribeDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse().from_map(
            await self.do_rpcrequest_async('DescribeDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dtcsecurity_ip_hosts_for_sqlserver(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    async def describe_dtcsecurity_ip_hosts_for_sqlserver_async(
        self,
        request: rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(request, runtime)

    def describe_error_logs_with_options(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeErrorLogsResponse().from_map(
            self.do_rpcrequest('DescribeErrorLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_error_logs_with_options_async(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeErrorLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeErrorLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_error_logs(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    async def describe_error_logs_async(
        self,
        request: rds_20140815_models.DescribeErrorLogsRequest,
    ) -> rds_20140815_models.DescribeErrorLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_error_logs_with_options_async(request, runtime)

    def describe_events_with_options(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeEventsResponse().from_map(
            self.do_rpcrequest('DescribeEvents', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_events_with_options_async(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeEvents', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_events(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
    ) -> rds_20140815_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    async def describe_events_async(
        self,
        request: rds_20140815_models.DescribeEventsRequest,
    ) -> rds_20140815_models.DescribeEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_events_with_options_async(request, runtime)

    def describe_haswitch_config_with_options(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeHASwitchConfigResponse().from_map(
            self.do_rpcrequest('DescribeHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_haswitch_config_with_options_async(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeHASwitchConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_haswitch_config(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    async def describe_haswitch_config_async(
        self,
        request: rds_20140815_models.DescribeHASwitchConfigRequest,
    ) -> rds_20140815_models.DescribeHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_haswitch_config_with_options_async(request, runtime)

    def describe_host_accounts_with_options(
        self,
        request: rds_20140815_models.DescribeHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHostAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeHostAccountsResponse().from_map(
            self.do_rpcrequest('DescribeHostAccounts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_accounts_with_options_async(
        self,
        request: rds_20140815_models.DescribeHostAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeHostAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeHostAccountsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHostAccounts', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_accounts(
        self,
        request: rds_20140815_models.DescribeHostAccountsRequest,
    ) -> rds_20140815_models.DescribeHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_accounts_with_options(request, runtime)

    async def describe_host_accounts_async(
        self,
        request: rds_20140815_models.DescribeHostAccountsRequest,
    ) -> rds_20140815_models.DescribeHostAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_accounts_with_options_async(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renewal_attribute_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renewal_attribute(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    async def describe_instance_auto_renewal_attribute_async(
        self,
        request: rds_20140815_models.DescribeInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def describe_instance_cross_backup_policy_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse().from_map(
            self.do_rpcrequest('DescribeInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_cross_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_cross_backup_policy(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    async def describe_instance_cross_backup_policy_async(
        self,
        request: rds_20140815_models.DescribeInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_cross_backup_policy_with_options_async(request, runtime)

    def describe_instance_keywords_with_options(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceKeywordsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceKeywords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_keywords_with_options_async(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeInstanceKeywordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceKeywords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_keywords(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    async def describe_instance_keywords_async(
        self,
        request: rds_20140815_models.DescribeInstanceKeywordsRequest,
    ) -> rds_20140815_models.DescribeInstanceKeywordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_keywords_with_options_async(request, runtime)

    def describe_local_available_recovery_time_with_options(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse().from_map(
            self.do_rpcrequest('DescribeLocalAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_local_available_recovery_time_with_options_async(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse().from_map(
            await self.do_rpcrequest_async('DescribeLocalAvailableRecoveryTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_local_available_recovery_time(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    async def describe_local_available_recovery_time_async(
        self,
        request: rds_20140815_models.DescribeLocalAvailableRecoveryTimeRequest,
    ) -> rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_local_available_recovery_time_with_options_async(request, runtime)

    def describe_log_backup_files_with_options(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeLogBackupFilesResponse().from_map(
            self.do_rpcrequest('DescribeLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_backup_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeLogBackupFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLogBackupFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_log_backup_files(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    async def describe_log_backup_files_async(
        self,
        request: rds_20140815_models.DescribeLogBackupFilesRequest,
    ) -> rds_20140815_models.DescribeLogBackupFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_backup_files_with_options_async(request, runtime)

    def describe_migrate_task_by_id_with_options(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeMigrateTaskByIdResponse().from_map(
            self.do_rpcrequest('DescribeMigrateTaskById', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migrate_task_by_id_with_options_async(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeMigrateTaskByIdResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrateTaskById', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migrate_task_by_id(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    async def describe_migrate_task_by_id_async(
        self,
        request: rds_20140815_models.DescribeMigrateTaskByIdRequest,
    ) -> rds_20140815_models.DescribeMigrateTaskByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migrate_task_by_id_with_options_async(request, runtime)

    def describe_migrate_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeMigrateTasksResponse().from_map(
            self.do_rpcrequest('DescribeMigrateTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_migrate_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeMigrateTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeMigrateTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_migrate_tasks(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    async def describe_migrate_tasks_async(
        self,
        request: rds_20140815_models.DescribeMigrateTasksRequest,
    ) -> rds_20140815_models.DescribeMigrateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migrate_tasks_with_options_async(request, runtime)

    def describe_modify_parameter_log_with_options(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeModifyParameterLogResponse().from_map(
            self.do_rpcrequest('DescribeModifyParameterLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_modify_parameter_log_with_options_async(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeModifyParameterLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeModifyParameterLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_modify_parameter_log(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    async def describe_modify_parameter_log_async(
        self,
        request: rds_20140815_models.DescribeModifyParameterLogRequest,
    ) -> rds_20140815_models.DescribeModifyParameterLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_modify_parameter_log_with_options_async(request, runtime)

    def describe_next_event_for_sign_with_options(
        self,
        request: rds_20140815_models.DescribeNextEventForSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeNextEventForSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeNextEventForSignResponse().from_map(
            self.do_rpcrequest('DescribeNextEventForSign', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_next_event_for_sign_with_options_async(
        self,
        request: rds_20140815_models.DescribeNextEventForSignRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeNextEventForSignResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeNextEventForSignResponse().from_map(
            await self.do_rpcrequest_async('DescribeNextEventForSign', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_next_event_for_sign(
        self,
        request: rds_20140815_models.DescribeNextEventForSignRequest,
    ) -> rds_20140815_models.DescribeNextEventForSignResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_next_event_for_sign_with_options(request, runtime)

    async def describe_next_event_for_sign_async(
        self,
        request: rds_20140815_models.DescribeNextEventForSignRequest,
    ) -> rds_20140815_models.DescribeNextEventForSignResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_next_event_for_sign_with_options_async(request, runtime)

    def describe_oss_downloads_with_options(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeOssDownloadsResponse().from_map(
            self.do_rpcrequest('DescribeOssDownloads', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_oss_downloads_with_options_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeOssDownloadsResponse().from_map(
            await self.do_rpcrequest_async('DescribeOssDownloads', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_oss_downloads(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    async def describe_oss_downloads_async(
        self,
        request: rds_20140815_models.DescribeOssDownloadsRequest,
    ) -> rds_20140815_models.DescribeOssDownloadsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_oss_downloads_with_options_async(request, runtime)

    def describe_parameter_group_with_options(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterGroupResponse().from_map(
            self.do_rpcrequest('DescribeParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterGroupResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_group(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    async def describe_parameter_group_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupRequest,
    ) -> rds_20140815_models.DescribeParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_group_with_options_async(request, runtime)

    def describe_parameter_groups_with_options(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterGroupsResponse().from_map(
            self.do_rpcrequest('DescribeParameterGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_groups_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterGroups', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_groups(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    async def describe_parameter_groups_async(
        self,
        request: rds_20140815_models.DescribeParameterGroupsRequest,
    ) -> rds_20140815_models.DescribeParameterGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_groups_with_options_async(request, runtime)

    def describe_parameters_with_options(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParametersResponse().from_map(
            self.do_rpcrequest('DescribeParameters', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameters_with_options_async(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParametersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParametersResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameters', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameters(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
    ) -> rds_20140815_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    async def describe_parameters_async(
        self,
        request: rds_20140815_models.DescribeParametersRequest,
    ) -> rds_20140815_models.DescribeParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameters_with_options_async(request, runtime)

    def describe_parameter_templates_with_options(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeParameterTemplates', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_parameter_templates_with_options_async(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeParameterTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeParameterTemplates', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parameter_templates(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    async def describe_parameter_templates_async(
        self,
        request: rds_20140815_models.DescribeParameterTemplatesRequest,
    ) -> rds_20140815_models.DescribeParameterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_parameter_templates_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: rds_20140815_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribePriceResponse().from_map(
            self.do_rpcrequest('DescribePrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: rds_20140815_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribePriceResponse().from_map(
            await self.do_rpcrequest_async('DescribePrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: rds_20140815_models.DescribePriceRequest,
    ) -> rds_20140815_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: rds_20140815_models.DescribePriceRequest,
    ) -> rds_20140815_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_rds_resource_settings_with_options(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRdsResourceSettingsResponse().from_map(
            self.do_rpcrequest('DescribeRdsResourceSettings', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_resource_settings_with_options_async(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRdsResourceSettingsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRdsResourceSettings', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_resource_settings(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    async def describe_rds_resource_settings_async(
        self,
        request: rds_20140815_models.DescribeRdsResourceSettingsRequest,
    ) -> rds_20140815_models.DescribeRdsResourceSettingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_resource_settings_with_options_async(request, runtime)

    def describe_read_dbinstance_delay_with_options(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeReadDBInstanceDelayResponse().from_map(
            self.do_rpcrequest('DescribeReadDBInstanceDelay', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_read_dbinstance_delay_with_options_async(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeReadDBInstanceDelayResponse().from_map(
            await self.do_rpcrequest_async('DescribeReadDBInstanceDelay', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_read_dbinstance_delay(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    async def describe_read_dbinstance_delay_async(
        self,
        request: rds_20140815_models.DescribeReadDBInstanceDelayRequest,
    ) -> rds_20140815_models.DescribeReadDBInstanceDelayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_read_dbinstance_delay_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: rds_20140815_models.DescribeRegionsRequest,
    ) -> rds_20140815_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_renewal_price_with_options(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRenewalPriceResponse().from_map(
            self.do_rpcrequest('DescribeRenewalPrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_renewal_price_with_options_async(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeRenewalPriceResponse().from_map(
            await self.do_rpcrequest_async('DescribeRenewalPrice', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renewal_price(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    async def describe_renewal_price_async(
        self,
        request: rds_20140815_models.DescribeRenewalPriceRequest,
    ) -> rds_20140815_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_renewal_price_with_options_async(request, runtime)

    def describe_resource_usage_with_options(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeResourceUsageResponse().from_map(
            self.do_rpcrequest('DescribeResourceUsage', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_usage_with_options_async(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeResourceUsageResponse().from_map(
            await self.do_rpcrequest_async('DescribeResourceUsage', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_usage(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    async def describe_resource_usage_async(
        self,
        request: rds_20140815_models.DescribeResourceUsageRequest,
    ) -> rds_20140815_models.DescribeResourceUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_usage_with_options_async(request, runtime)

    def describe_security_group_configuration_with_options(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_configuration_with_options_async(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSecurityGroupConfigurationResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_configuration(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    async def describe_security_group_configuration_async(
        self,
        request: rds_20140815_models.DescribeSecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.DescribeSecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_configuration_with_options_async(request, runtime)

    def describe_signed_event_actions_with_options(
        self,
        request: rds_20140815_models.DescribeSignedEventActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSignedEventActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSignedEventActionsResponse().from_map(
            self.do_rpcrequest('DescribeSignedEventActions', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_signed_event_actions_with_options_async(
        self,
        request: rds_20140815_models.DescribeSignedEventActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSignedEventActionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSignedEventActionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSignedEventActions', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_signed_event_actions(
        self,
        request: rds_20140815_models.DescribeSignedEventActionsRequest,
    ) -> rds_20140815_models.DescribeSignedEventActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_signed_event_actions_with_options(request, runtime)

    async def describe_signed_event_actions_async(
        self,
        request: rds_20140815_models.DescribeSignedEventActionsRequest,
    ) -> rds_20140815_models.DescribeSignedEventActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_signed_event_actions_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSlowLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSlowLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSlowLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlowLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: rds_20140815_models.DescribeSlowLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSlowLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_logs_with_options(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSlowLogsResponse().from_map(
            self.do_rpcrequest('DescribeSlowLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_slow_logs_with_options_async(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSlowLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSlowLogs', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_slow_logs(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    async def describe_slow_logs_async(
        self,
        request: rds_20140815_models.DescribeSlowLogsRequest,
    ) -> rds_20140815_models.DescribeSlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_logs_with_options_async(request, runtime)

    def describe_sqlcollector_policy_with_options(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLCollectorPolicyResponse().from_map(
            self.do_rpcrequest('DescribeSQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlcollector_policy_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLCollectorPolicyResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlcollector_policy(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    async def describe_sqlcollector_policy_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorPolicyRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlcollector_policy_with_options_async(request, runtime)

    def describe_sqlcollector_retention_with_options(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLCollectorRetentionResponse().from_map(
            self.do_rpcrequest('DescribeSQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlcollector_retention_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLCollectorRetentionResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlcollector_retention(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    async def describe_sqlcollector_retention_async(
        self,
        request: rds_20140815_models.DescribeSQLCollectorRetentionRequest,
    ) -> rds_20140815_models.DescribeSQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlcollector_retention_with_options_async(request, runtime)

    def describe_sqllog_files_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogFilesResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_files_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogFilesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogFiles', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_files(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    async def describe_sqllog_files_async(
        self,
        request: rds_20140815_models.DescribeSQLLogFilesRequest,
    ) -> rds_20140815_models.DescribeSQLLogFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_files_with_options_async(request, runtime)

    def describe_sqllog_records_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogRecordsResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_records_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogRecordsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogRecords', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_records(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    async def describe_sqllog_records_async(
        self,
        request: rds_20140815_models.DescribeSQLLogRecordsRequest,
    ) -> rds_20140815_models.DescribeSQLLogRecordsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_records_with_options_async(request, runtime)

    def describe_sqllog_report_list_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogReportListResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_report_list_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogReportListResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogReportList', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_report_list(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    async def describe_sqllog_report_list_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportListRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_report_list_with_options_async(request, runtime)

    def describe_sqllog_reports_with_options(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogReportsResponse().from_map(
            self.do_rpcrequest('DescribeSQLLogReports', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqllog_reports_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLLogReportsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLLogReports', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqllog_reports(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_reports_with_options(request, runtime)

    async def describe_sqllog_reports_async(
        self,
        request: rds_20140815_models.DescribeSQLLogReportsRequest,
    ) -> rds_20140815_models.DescribeSQLLogReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqllog_reports_with_options_async(request, runtime)

    def describe_sqlreports_with_options(
        self,
        request: rds_20140815_models.DescribeSQLReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLReportsResponse().from_map(
            self.do_rpcrequest('DescribeSQLReports', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sqlreports_with_options_async(
        self,
        request: rds_20140815_models.DescribeSQLReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeSQLReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeSQLReportsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSQLReports', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sqlreports(
        self,
        request: rds_20140815_models.DescribeSQLReportsRequest,
    ) -> rds_20140815_models.DescribeSQLReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlreports_with_options(request, runtime)

    async def describe_sqlreports_async(
        self,
        request: rds_20140815_models.DescribeSQLReportsRequest,
    ) -> rds_20140815_models.DescribeSQLReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sqlreports_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeTagsResponse().from_map(
            self.do_rpcrequest('DescribeTags', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTags', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
    ) -> rds_20140815_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: rds_20140815_models.DescribeTagsRequest,
    ) -> rds_20140815_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DescribeTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeTasks', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
    ) -> rds_20140815_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: rds_20140815_models.DescribeTasksRequest,
    ) -> rds_20140815_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def destroy_dbinstance_with_options(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DestroyDBInstanceResponse().from_map(
            self.do_rpcrequest('DestroyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def destroy_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DestroyDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('DestroyDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_dbinstance(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    async def destroy_dbinstance_async(
        self,
        request: rds_20140815_models.DestroyDBInstanceRequest,
    ) -> rds_20140815_models.DestroyDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.destroy_dbinstance_with_options_async(request, runtime)

    def drop_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DropDedicatedHostUserResponse().from_map(
            self.do_rpcrequest('DropDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def drop_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.DropDedicatedHostUserResponse().from_map(
            await self.do_rpcrequest_async('DropDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_dedicated_host_user(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    async def drop_dedicated_host_user_async(
        self,
        request: rds_20140815_models.DropDedicatedHostUserRequest,
    ) -> rds_20140815_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_dedicated_host_user_with_options_async(request, runtime)

    def evaluate_dedicated_host_instance_resource_with_options(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse().from_map(
            self.do_rpcrequest('EvaluateDedicatedHostInstanceResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def evaluate_dedicated_host_instance_resource_with_options_async(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse().from_map(
            await self.do_rpcrequest_async('EvaluateDedicatedHostInstanceResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def evaluate_dedicated_host_instance_resource(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.evaluate_dedicated_host_instance_resource_with_options(request, runtime)

    async def evaluate_dedicated_host_instance_resource_async(
        self,
        request: rds_20140815_models.EvaluateDedicatedHostInstanceResourceRequest,
    ) -> rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.evaluate_dedicated_host_instance_resource_with_options_async(request, runtime)

    def get_dbinstance_topology_with_options(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDBInstanceTopologyResponse().from_map(
            self.do_rpcrequest('GetDBInstanceTopology', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dbinstance_topology_with_options_async(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDBInstanceTopologyResponse().from_map(
            await self.do_rpcrequest_async('GetDBInstanceTopology', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dbinstance_topology(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dbinstance_topology_with_options(request, runtime)

    async def get_dbinstance_topology_async(
        self,
        request: rds_20140815_models.GetDBInstanceTopologyRequest,
    ) -> rds_20140815_models.GetDBInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dbinstance_topology_with_options_async(request, runtime)

    def get_db_proxy_instance_ssl_with_options(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDbProxyInstanceSslResponse().from_map(
            self.do_rpcrequest('GetDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_db_proxy_instance_ssl_with_options_async(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GetDbProxyInstanceSslResponse().from_map(
            await self.do_rpcrequest_async('GetDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_db_proxy_instance_ssl(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    async def get_db_proxy_instance_ssl_async(
        self,
        request: rds_20140815_models.GetDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.GetDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_db_proxy_instance_ssl_with_options_async(request, runtime)

    def grant_account_privilege_with_options(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GrantAccountPrivilegeResponse().from_map(
            self.do_rpcrequest('GrantAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_account_privilege_with_options_async(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GrantAccountPrivilegeResponse().from_map(
            await self.do_rpcrequest_async('GrantAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_account_privilege(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    async def grant_account_privilege_async(
        self,
        request: rds_20140815_models.GrantAccountPrivilegeRequest,
    ) -> rds_20140815_models.GrantAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_account_privilege_with_options_async(request, runtime)

    def grant_operator_permission_with_options(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GrantOperatorPermissionResponse().from_map(
            self.do_rpcrequest('GrantOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_operator_permission_with_options_async(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.GrantOperatorPermissionResponse().from_map(
            await self.do_rpcrequest_async('GrantOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_operator_permission(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    async def grant_operator_permission_async(
        self,
        request: rds_20140815_models.GrantOperatorPermissionRequest,
    ) -> rds_20140815_models.GrantOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_operator_permission_with_options_async(request, runtime)

    def import_database_between_instances_with_options(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ImportDatabaseBetweenInstancesResponse().from_map(
            self.do_rpcrequest('ImportDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_database_between_instances_with_options_async(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ImportDatabaseBetweenInstancesResponse().from_map(
            await self.do_rpcrequest_async('ImportDatabaseBetweenInstances', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_database_between_instances(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    async def import_database_between_instances_async(
        self,
        request: rds_20140815_models.ImportDatabaseBetweenInstancesRequest,
    ) -> rds_20140815_models.ImportDatabaseBetweenInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_database_between_instances_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: rds_20140815_models.ListTagResourcesRequest,
    ) -> rds_20140815_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def lock_account_with_options(
        self,
        request: rds_20140815_models.LockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.LockAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.LockAccountResponse().from_map(
            self.do_rpcrequest('LockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def lock_account_with_options_async(
        self,
        request: rds_20140815_models.LockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.LockAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.LockAccountResponse().from_map(
            await self.do_rpcrequest_async('LockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def lock_account(
        self,
        request: rds_20140815_models.LockAccountRequest,
    ) -> rds_20140815_models.LockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    async def lock_account_async(
        self,
        request: rds_20140815_models.LockAccountRequest,
    ) -> rds_20140815_models.LockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.lock_account_with_options_async(request, runtime)

    def migrate_connection_to_other_zone_with_options(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateConnectionToOtherZoneResponse().from_map(
            self.do_rpcrequest('MigrateConnectionToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_connection_to_other_zone_with_options_async(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateConnectionToOtherZoneResponse().from_map(
            await self.do_rpcrequest_async('MigrateConnectionToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_connection_to_other_zone(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_connection_to_other_zone_with_options(request, runtime)

    async def migrate_connection_to_other_zone_async(
        self,
        request: rds_20140815_models.MigrateConnectionToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateConnectionToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_connection_to_other_zone_with_options_async(request, runtime)

    def migrate_dbinstance_with_options(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateDBInstanceResponse().from_map(
            self.do_rpcrequest('MigrateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('MigrateDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_dbinstance(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    async def migrate_dbinstance_async(
        self,
        request: rds_20140815_models.MigrateDBInstanceRequest,
    ) -> rds_20140815_models.MigrateDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_dbinstance_with_options_async(request, runtime)

    def migrate_security_ipmode_with_options(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateSecurityIPModeResponse().from_map(
            self.do_rpcrequest('MigrateSecurityIPMode', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_security_ipmode_with_options_async(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateSecurityIPModeResponse().from_map(
            await self.do_rpcrequest_async('MigrateSecurityIPMode', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_security_ipmode(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    async def migrate_security_ipmode_async(
        self,
        request: rds_20140815_models.MigrateSecurityIPModeRequest,
    ) -> rds_20140815_models.MigrateSecurityIPModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_security_ipmode_with_options_async(request, runtime)

    def migrate_to_other_zone_with_options(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateToOtherZoneResponse().from_map(
            self.do_rpcrequest('MigrateToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def migrate_to_other_zone_with_options_async(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.MigrateToOtherZoneResponse().from_map(
            await self.do_rpcrequest_async('MigrateToOtherZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def migrate_to_other_zone(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    async def migrate_to_other_zone_async(
        self,
        request: rds_20140815_models.MigrateToOtherZoneRequest,
    ) -> rds_20140815_models.MigrateToOtherZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.migrate_to_other_zone_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyAccountDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyAccountDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyAccountDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyAccountDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: rds_20140815_models.ModifyAccountDescriptionRequest,
    ) -> rds_20140815_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_action_event_policy_with_options(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyActionEventPolicyResponse().from_map(
            self.do_rpcrequest('ModifyActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_action_event_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyActionEventPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyActionEventPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_action_event_policy(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    async def modify_action_event_policy_async(
        self,
        request: rds_20140815_models.ModifyActionEventPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_action_event_policy_with_options_async(request, runtime)

    def modify_action_event_verify_policy_with_options(
        self,
        request: rds_20140815_models.ModifyActionEventVerifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventVerifyPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyActionEventVerifyPolicyResponse().from_map(
            self.do_rpcrequest('ModifyActionEventVerifyPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_action_event_verify_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyActionEventVerifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyActionEventVerifyPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyActionEventVerifyPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyActionEventVerifyPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_action_event_verify_policy(
        self,
        request: rds_20140815_models.ModifyActionEventVerifyPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventVerifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_verify_policy_with_options(request, runtime)

    async def modify_action_event_verify_policy_async(
        self,
        request: rds_20140815_models.ModifyActionEventVerifyPolicyRequest,
    ) -> rds_20140815_models.ModifyActionEventVerifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_action_event_verify_policy_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_backup_policy(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: rds_20140815_models.ModifyBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_collation_time_zone_with_options(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyCollationTimeZoneResponse().from_map(
            self.do_rpcrequest('ModifyCollationTimeZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_collation_time_zone_with_options_async(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyCollationTimeZoneResponse().from_map(
            await self.do_rpcrequest_async('ModifyCollationTimeZone', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_collation_time_zone(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    async def modify_collation_time_zone_async(
        self,
        request: rds_20140815_models.ModifyCollationTimeZoneRequest,
    ) -> rds_20140815_models.ModifyCollationTimeZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_collation_time_zone_with_options_async(request, runtime)

    def modify_das_instance_config_with_options(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDasInstanceConfigResponse().from_map(
            self.do_rpcrequest('ModifyDasInstanceConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_das_instance_config_with_options_async(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDasInstanceConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyDasInstanceConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_das_instance_config(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    async def modify_das_instance_config_async(
        self,
        request: rds_20140815_models.ModifyDasInstanceConfigRequest,
    ) -> rds_20140815_models.ModifyDasInstanceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_das_instance_config_with_options_async(request, runtime)

    def modify_dbdescription_with_options(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyDBDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbdescription_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbdescription(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    async def modify_dbdescription_async(
        self,
        request: rds_20140815_models.ModifyDBDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbdescription_with_options_async(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceAutoUpgradeMinorVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_auto_upgrade_minor_version_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceAutoUpgradeMinorVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_auto_upgrade_minor_version(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    async def modify_dbinstance_auto_upgrade_minor_version_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_auto_upgrade_minor_version_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceConnectionStringResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceConnectionString', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceConnectionStringResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceConnectionString', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceConnectionStringRequest,
    ) -> rds_20140815_models.ModifyDBInstanceConnectionStringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_dbinstance_description_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceDescriptionResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_description_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceDescriptionResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceDescription', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_description(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    async def modify_dbinstance_description_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceDescriptionRequest,
    ) -> rds_20140815_models.ModifyDBInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_description_with_options_async(request, runtime)

    def modify_dbinstance_haconfig_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceHAConfigResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_haconfig_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceHAConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceHAConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_haconfig(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    async def modify_dbinstance_haconfig_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceHAConfigRequest,
    ) -> rds_20140815_models.ModifyDBInstanceHAConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_haconfig_with_options_async(request, runtime)

    def modify_dbinstance_maintain_time_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMaintainTimeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceMaintainTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_maintain_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMaintainTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceMaintainTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_maintain_time(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    async def modify_dbinstance_maintain_time_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMaintainTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMaintainTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_maintain_time_with_options_async(request, runtime)

    def modify_dbinstance_monitor_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMonitorResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_monitor_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceMonitorResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceMonitor', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_monitor(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    async def modify_dbinstance_monitor_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceMonitorRequest,
    ) -> rds_20140815_models.ModifyDBInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_monitor_with_options_async(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceNetworkExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_network_expire_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceNetworkExpireTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_expire_time(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    async def modify_dbinstance_network_expire_time_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkExpireTimeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_expire_time_with_options_async(request, runtime)

    def modify_dbinstance_network_type_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceNetworkTypeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceNetworkType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_network_type_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceNetworkTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceNetworkType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_network_type(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    async def modify_dbinstance_network_type_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceNetworkTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstanceNetworkTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_network_type_with_options_async(request, runtime)

    def modify_dbinstance_pay_type_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstancePayTypeResponse().from_map(
            self.do_rpcrequest('ModifyDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_pay_type_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstancePayTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_pay_type(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    async def modify_dbinstance_pay_type_async(
        self,
        request: rds_20140815_models.ModifyDBInstancePayTypeRequest,
    ) -> rds_20140815_models.ModifyDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_pay_type_with_options_async(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_proxy_configuration_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceProxyConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_proxy_configuration(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    async def modify_dbinstance_proxy_configuration_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceProxyConfigurationRequest,
    ) -> rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_proxy_configuration_with_options_async(request, runtime)

    def modify_dbinstance_spec_with_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceSpec', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_spec_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceSpec', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_spec(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    async def modify_dbinstance_spec_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSpecRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_spec_with_options_async(request, runtime)

    def modify_dbinstance_sslwith_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceSSLResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_sslwith_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceSSLResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceSSL', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_ssl(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    async def modify_dbinstance_ssl_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceSSLRequest,
    ) -> rds_20140815_models.ModifyDBInstanceSSLResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_sslwith_options_async(request, runtime)

    def modify_dbinstance_tdewith_options(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceTDEResponse().from_map(
            self.do_rpcrequest('ModifyDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_tdewith_options_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBInstanceTDEResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBInstanceTDE', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_tde(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    async def modify_dbinstance_tde_async(
        self,
        request: rds_20140815_models.ModifyDBInstanceTDERequest,
    ) -> rds_20140815_models.ModifyDBInstanceTDEResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_tdewith_options_async(request, runtime)

    def modify_dbproxy_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyResponse().from_map(
            self.do_rpcrequest('ModifyDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbproxy_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBProxy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    async def modify_dbproxy_async(
        self,
        request: rds_20140815_models.ModifyDBProxyRequest,
    ) -> rds_20140815_models.ModifyDBProxyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_with_options_async(request, runtime)

    def modify_dbproxy_endpoint_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyEndpointResponse().from_map(
            self.do_rpcrequest('ModifyDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbproxy_endpoint_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyEndpointResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBProxyEndpoint', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_endpoint(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    async def modify_dbproxy_endpoint_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_endpoint_with_options_async(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyEndpointAddressResponse().from_map(
            self.do_rpcrequest('ModifyDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbproxy_endpoint_address_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyEndpointAddressResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBProxyEndpointAddress', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_endpoint_address(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    async def modify_dbproxy_endpoint_address_async(
        self,
        request: rds_20140815_models.ModifyDBProxyEndpointAddressRequest,
    ) -> rds_20140815_models.ModifyDBProxyEndpointAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_endpoint_address_with_options_async(request, runtime)

    def modify_dbproxy_instance_with_options(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyInstanceResponse().from_map(
            self.do_rpcrequest('ModifyDBProxyInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbproxy_instance_with_options_async(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDBProxyInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyDBProxyInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbproxy_instance(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    async def modify_dbproxy_instance_async(
        self,
        request: rds_20140815_models.ModifyDBProxyInstanceRequest,
    ) -> rds_20140815_models.ModifyDBProxyInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbproxy_instance_with_options_async(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDbProxyInstanceSslResponse().from_map(
            self.do_rpcrequest('ModifyDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_db_proxy_instance_ssl_with_options_async(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDbProxyInstanceSslResponse().from_map(
            await self.do_rpcrequest_async('ModifyDbProxyInstanceSsl', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_db_proxy_instance_ssl(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    async def modify_db_proxy_instance_ssl_async(
        self,
        request: rds_20140815_models.ModifyDbProxyInstanceSslRequest,
    ) -> rds_20140815_models.ModifyDbProxyInstanceSslResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_db_proxy_instance_ssl_with_options_async(request, runtime)

    def modify_dedicated_host_account_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostAccountResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_account_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostAccountResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_account(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    async def modify_dedicated_host_account_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAccountRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_account_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostGroupAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_group_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostGroupAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_group_attribute(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    async def modify_dedicated_host_group_attribute_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_group_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_user_with_options(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostUserResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_user_with_options_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDedicatedHostUserResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostUser', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_user(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_user_with_options(request, runtime)

    async def modify_dedicated_host_user_async(
        self,
        request: rds_20140815_models.ModifyDedicatedHostUserRequest,
    ) -> rds_20140815_models.ModifyDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_user_with_options_async(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse().from_map(
            self.do_rpcrequest('ModifyDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse().from_map(
            await self.do_rpcrequest_async('ModifyDTCSecurityIpHostsForSQLServer', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dtcsecurity_ip_hosts_for_sqlserver(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    async def modify_dtcsecurity_ip_hosts_for_sqlserver_async(
        self,
        request: rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerRequest,
    ) -> rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options_async(request, runtime)

    def modify_haswitch_config_with_options(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyHASwitchConfigResponse().from_map(
            self.do_rpcrequest('ModifyHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_haswitch_config_with_options_async(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyHASwitchConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyHASwitchConfig', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_haswitch_config(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    async def modify_haswitch_config_async(
        self,
        request: rds_20140815_models.ModifyHASwitchConfigRequest,
    ) -> rds_20140815_models.ModifyHASwitchConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_haswitch_config_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewalAttribute', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: rds_20140815_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_instance_cross_backup_policy_with_options(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse().from_map(
            self.do_rpcrequest('ModifyInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_cross_backup_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceCrossBackupPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_cross_backup_policy(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    async def modify_instance_cross_backup_policy_async(
        self,
        request: rds_20140815_models.ModifyInstanceCrossBackupPolicyRequest,
    ) -> rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_cross_backup_policy_with_options_async(request, runtime)

    def modify_license_info_with_options(
        self,
        request: rds_20140815_models.ModifyLicenseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyLicenseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyLicenseInfoResponse().from_map(
            self.do_rpcrequest('ModifyLicenseInfo', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_license_info_with_options_async(
        self,
        request: rds_20140815_models.ModifyLicenseInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyLicenseInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyLicenseInfoResponse().from_map(
            await self.do_rpcrequest_async('ModifyLicenseInfo', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_license_info(
        self,
        request: rds_20140815_models.ModifyLicenseInfoRequest,
    ) -> rds_20140815_models.ModifyLicenseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_license_info_with_options(request, runtime)

    async def modify_license_info_async(
        self,
        request: rds_20140815_models.ModifyLicenseInfoRequest,
    ) -> rds_20140815_models.ModifyLicenseInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_license_info_with_options_async(request, runtime)

    def modify_parameter_with_options(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyParameterResponse().from_map(
            self.do_rpcrequest('ModifyParameter', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameter_with_options_async(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyParameterResponse().from_map(
            await self.do_rpcrequest_async('ModifyParameter', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
    ) -> rds_20140815_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    async def modify_parameter_async(
        self,
        request: rds_20140815_models.ModifyParameterRequest,
    ) -> rds_20140815_models.ModifyParameterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_with_options_async(request, runtime)

    def modify_parameter_group_with_options(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyParameterGroupResponse().from_map(
            self.do_rpcrequest('ModifyParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_parameter_group_with_options_async(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyParameterGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyParameterGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parameter_group(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    async def modify_parameter_group_async(
        self,
        request: rds_20140815_models.ModifyParameterGroupRequest,
    ) -> rds_20140815_models.ModifyParameterGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_parameter_group_with_options_async(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse().from_map(
            self.do_rpcrequest('ModifyReadonlyInstanceDelayReplicationTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_readonly_instance_delay_replication_time_with_options_async(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyReadonlyInstanceDelayReplicationTime', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_readonly_instance_delay_replication_time(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    async def modify_readonly_instance_delay_replication_time_async(
        self,
        request: rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeRequest,
    ) -> rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_readonly_instance_delay_replication_time_with_options_async(request, runtime)

    def modify_read_write_splitting_connection_with_options(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyReadWriteSplittingConnectionResponse().from_map(
            self.do_rpcrequest('ModifyReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_read_write_splitting_connection_with_options_async(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyReadWriteSplittingConnectionResponse().from_map(
            await self.do_rpcrequest_async('ModifyReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_read_write_splitting_connection(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    async def modify_read_write_splitting_connection_async(
        self,
        request: rds_20140815_models.ModifyReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ModifyReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_read_write_splitting_connection_with_options_async(request, runtime)

    def modify_resource_group_with_options(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyResourceGroupResponse().from_map(
            self.do_rpcrequest('ModifyResourceGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_group_with_options_async(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifyResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyResourceGroup', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_group(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    async def modify_resource_group_async(
        self,
        request: rds_20140815_models.ModifyResourceGroupRequest,
    ) -> rds_20140815_models.ModifyResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_group_with_options_async(request, runtime)

    def modify_security_group_configuration_with_options(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySecurityGroupConfigurationResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_configuration_with_options_async(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySecurityGroupConfigurationResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupConfiguration', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_configuration(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    async def modify_security_group_configuration_async(
        self,
        request: rds_20140815_models.ModifySecurityGroupConfigurationRequest,
    ) -> rds_20140815_models.ModifySecurityGroupConfigurationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_configuration_with_options_async(request, runtime)

    def modify_security_ips_with_options(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySecurityIpsResponse().from_map(
            self.do_rpcrequest('ModifySecurityIps', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_ips_with_options_async(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySecurityIpsResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityIps', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_ips(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    async def modify_security_ips_async(
        self,
        request: rds_20140815_models.ModifySecurityIpsRequest,
    ) -> rds_20140815_models.ModifySecurityIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_ips_with_options_async(request, runtime)

    def modify_sqlcollector_policy_with_options(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySQLCollectorPolicyResponse().from_map(
            self.do_rpcrequest('ModifySQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sqlcollector_policy_with_options_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySQLCollectorPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifySQLCollectorPolicy', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sqlcollector_policy(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    async def modify_sqlcollector_policy_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorPolicyRequest,
    ) -> rds_20140815_models.ModifySQLCollectorPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqlcollector_policy_with_options_async(request, runtime)

    def modify_sqlcollector_retention_with_options(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySQLCollectorRetentionResponse().from_map(
            self.do_rpcrequest('ModifySQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_sqlcollector_retention_with_options_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ModifySQLCollectorRetentionResponse().from_map(
            await self.do_rpcrequest_async('ModifySQLCollectorRetention', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sqlcollector_retention(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    async def modify_sqlcollector_retention_async(
        self,
        request: rds_20140815_models.ModifySQLCollectorRetentionRequest,
    ) -> rds_20140815_models.ModifySQLCollectorRetentionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_sqlcollector_retention_with_options_async(request, runtime)

    def purge_dbinstance_log_with_options(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.PurgeDBInstanceLogResponse().from_map(
            self.do_rpcrequest('PurgeDBInstanceLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purge_dbinstance_log_with_options_async(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.PurgeDBInstanceLogResponse().from_map(
            await self.do_rpcrequest_async('PurgeDBInstanceLog', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purge_dbinstance_log(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    async def purge_dbinstance_log_async(
        self,
        request: rds_20140815_models.PurgeDBInstanceLogRequest,
    ) -> rds_20140815_models.PurgeDBInstanceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purge_dbinstance_log_with_options_async(request, runtime)

    def rebuild_dbinstance_with_options(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RebuildDBInstanceResponse().from_map(
            self.do_rpcrequest('RebuildDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rebuild_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RebuildDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RebuildDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rebuild_dbinstance(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    async def rebuild_dbinstance_async(
        self,
        request: rds_20140815_models.RebuildDBInstanceRequest,
    ) -> rds_20140815_models.RebuildDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_dbinstance_with_options_async(request, runtime)

    def recovery_dbinstance_with_options(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RecoveryDBInstanceResponse().from_map(
            self.do_rpcrequest('RecoveryDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recovery_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RecoveryDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RecoveryDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recovery_dbinstance(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    async def recovery_dbinstance_async(
        self,
        request: rds_20140815_models.RecoveryDBInstanceRequest,
    ) -> rds_20140815_models.RecoveryDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recovery_dbinstance_with_options_async(request, runtime)

    def release_instance_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseInstanceConnectionResponse().from_map(
            self.do_rpcrequest('ReleaseInstanceConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseInstanceConnectionResponse().from_map(
            await self.do_rpcrequest_async('ReleaseInstanceConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_connection(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    async def release_instance_connection_async(
        self,
        request: rds_20140815_models.ReleaseInstanceConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstanceConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_connection_with_options_async(request, runtime)

    def release_instance_public_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseInstancePublicConnectionResponse().from_map(
            self.do_rpcrequest('ReleaseInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_public_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseInstancePublicConnectionResponse().from_map(
            await self.do_rpcrequest_async('ReleaseInstancePublicConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_public_connection(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    async def release_instance_public_connection_async(
        self,
        request: rds_20140815_models.ReleaseInstancePublicConnectionRequest,
    ) -> rds_20140815_models.ReleaseInstancePublicConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_public_connection_with_options_async(request, runtime)

    def release_read_write_splitting_connection_with_options(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse().from_map(
            self.do_rpcrequest('ReleaseReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_read_write_splitting_connection_with_options_async(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse().from_map(
            await self.do_rpcrequest_async('ReleaseReadWriteSplittingConnection', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_read_write_splitting_connection(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    async def release_read_write_splitting_connection_async(
        self,
        request: rds_20140815_models.ReleaseReadWriteSplittingConnectionRequest,
    ) -> rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_read_write_splitting_connection_with_options_async(request, runtime)

    def remove_tags_from_resource_with_options(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RemoveTagsFromResourceResponse().from_map(
            self.do_rpcrequest('RemoveTagsFromResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_from_resource_with_options_async(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RemoveTagsFromResourceResponse().from_map(
            await self.do_rpcrequest_async('RemoveTagsFromResource', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags_from_resource(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    async def remove_tags_from_resource_async(
        self,
        request: rds_20140815_models.RemoveTagsFromResourceRequest,
    ) -> rds_20140815_models.RemoveTagsFromResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_from_resource_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
    ) -> rds_20140815_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: rds_20140815_models.RenewInstanceRequest,
    ) -> rds_20140815_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_dedicated_host_with_options(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReplaceDedicatedHostResponse().from_map(
            self.do_rpcrequest('ReplaceDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ReplaceDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('ReplaceDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_dedicated_host(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    async def replace_dedicated_host_async(
        self,
        request: rds_20140815_models.ReplaceDedicatedHostRequest,
    ) -> rds_20140815_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_dedicated_host_with_options_async(request, runtime)

    def reset_account_with_options(
        self,
        request: rds_20140815_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountResponse().from_map(
            self.do_rpcrequest('ResetAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_with_options_async(
        self,
        request: rds_20140815_models.ResetAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountResponse().from_map(
            await self.do_rpcrequest_async('ResetAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account(
        self,
        request: rds_20140815_models.ResetAccountRequest,
    ) -> rds_20140815_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    async def reset_account_async(
        self,
        request: rds_20140815_models.ResetAccountRequest,
    ) -> rds_20140815_models.ResetAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_with_options_async(request, runtime)

    def reset_account_for_pgwith_options(
        self,
        request: rds_20140815_models.ResetAccountForPGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountForPGResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountForPGResponse().from_map(
            self.do_rpcrequest('ResetAccountForPG', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_for_pgwith_options_async(
        self,
        request: rds_20140815_models.ResetAccountForPGRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountForPGResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountForPGResponse().from_map(
            await self.do_rpcrequest_async('ResetAccountForPG', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_for_pg(
        self,
        request: rds_20140815_models.ResetAccountForPGRequest,
    ) -> rds_20140815_models.ResetAccountForPGResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_for_pgwith_options(request, runtime)

    async def reset_account_for_pg_async(
        self,
        request: rds_20140815_models.ResetAccountForPGRequest,
    ) -> rds_20140815_models.ResetAccountForPGResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_for_pgwith_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountPasswordResponse().from_map(
            self.do_rpcrequest('ResetAccountPassword', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetAccountPassword', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_account_password(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: rds_20140815_models.ResetAccountPasswordRequest,
    ) -> rds_20140815_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def reset_host_account_password_with_options(
        self,
        request: rds_20140815_models.ResetHostAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetHostAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetHostAccountPasswordResponse().from_map(
            self.do_rpcrequest('ResetHostAccountPassword', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_host_account_password_with_options_async(
        self,
        request: rds_20140815_models.ResetHostAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.ResetHostAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.ResetHostAccountPasswordResponse().from_map(
            await self.do_rpcrequest_async('ResetHostAccountPassword', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_host_account_password(
        self,
        request: rds_20140815_models.ResetHostAccountPasswordRequest,
    ) -> rds_20140815_models.ResetHostAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_host_account_password_with_options(request, runtime)

    async def reset_host_account_password_async(
        self,
        request: rds_20140815_models.ResetHostAccountPasswordRequest,
    ) -> rds_20140815_models.ResetHostAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_host_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestartDBInstanceResponse().from_map(
            self.do_rpcrequest('RestartDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestartDBInstanceResponse().from_map(
            await self.do_rpcrequest_async('RestartDBInstance', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dbinstance(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: rds_20140815_models.RestartDBInstanceRequest,
    ) -> rds_20140815_models.RestartDBInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def restart_dedicated_host_with_options(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestartDedicatedHostResponse().from_map(
            self.do_rpcrequest('RestartDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dedicated_host_with_options_async(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestartDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('RestartDedicatedHost', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dedicated_host(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    async def restart_dedicated_host_async(
        self,
        request: rds_20140815_models.RestartDedicatedHostRequest,
    ) -> rds_20140815_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dedicated_host_with_options_async(request, runtime)

    def restore_ddr_table_with_options(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestoreDdrTableResponse().from_map(
            self.do_rpcrequest('RestoreDdrTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_ddr_table_with_options_async(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestoreDdrTableResponse().from_map(
            await self.do_rpcrequest_async('RestoreDdrTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_ddr_table(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    async def restore_ddr_table_async(
        self,
        request: rds_20140815_models.RestoreDdrTableRequest,
    ) -> rds_20140815_models.RestoreDdrTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_ddr_table_with_options_async(request, runtime)

    def restore_table_with_options(
        self,
        request: rds_20140815_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestoreTableResponse().from_map(
            self.do_rpcrequest('RestoreTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_table_with_options_async(
        self,
        request: rds_20140815_models.RestoreTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RestoreTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RestoreTableResponse().from_map(
            await self.do_rpcrequest_async('RestoreTable', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_table(
        self,
        request: rds_20140815_models.RestoreTableRequest,
    ) -> rds_20140815_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    async def restore_table_async(
        self,
        request: rds_20140815_models.RestoreTableRequest,
    ) -> rds_20140815_models.RestoreTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_table_with_options_async(request, runtime)

    def revoke_account_privilege_with_options(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RevokeAccountPrivilegeResponse().from_map(
            self.do_rpcrequest('RevokeAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_account_privilege_with_options_async(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RevokeAccountPrivilegeResponse().from_map(
            await self.do_rpcrequest_async('RevokeAccountPrivilege', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_account_privilege(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    async def revoke_account_privilege_async(
        self,
        request: rds_20140815_models.RevokeAccountPrivilegeRequest,
    ) -> rds_20140815_models.RevokeAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_account_privilege_with_options_async(request, runtime)

    def revoke_operator_permission_with_options(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RevokeOperatorPermissionResponse().from_map(
            self.do_rpcrequest('RevokeOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_operator_permission_with_options_async(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.RevokeOperatorPermissionResponse().from_map(
            await self.do_rpcrequest_async('RevokeOperatorPermission', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_operator_permission(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    async def revoke_operator_permission_async(
        self,
        request: rds_20140815_models.RevokeOperatorPermissionRequest,
    ) -> rds_20140815_models.RevokeOperatorPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_operator_permission_with_options_async(request, runtime)

    def sign_event_action_with_options(
        self,
        request: rds_20140815_models.SignEventActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SignEventActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SignEventActionResponse().from_map(
            self.do_rpcrequest('SignEventAction', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sign_event_action_with_options_async(
        self,
        request: rds_20140815_models.SignEventActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SignEventActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SignEventActionResponse().from_map(
            await self.do_rpcrequest_async('SignEventAction', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sign_event_action(
        self,
        request: rds_20140815_models.SignEventActionRequest,
    ) -> rds_20140815_models.SignEventActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.sign_event_action_with_options(request, runtime)

    async def sign_event_action_async(
        self,
        request: rds_20140815_models.SignEventActionRequest,
    ) -> rds_20140815_models.SignEventActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sign_event_action_with_options_async(request, runtime)

    def switch_dbinstance_hawith_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceHAResponse().from_map(
            self.do_rpcrequest('SwitchDBInstanceHA', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dbinstance_hawith_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceHAResponse().from_map(
            await self.do_rpcrequest_async('SwitchDBInstanceHA', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_ha(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    async def switch_dbinstance_ha_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceHARequest,
    ) -> rds_20140815_models.SwitchDBInstanceHAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_hawith_options_async(request, runtime)

    def switch_dbinstance_net_type_with_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceNetTypeResponse().from_map(
            self.do_rpcrequest('SwitchDBInstanceNetType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dbinstance_net_type_with_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceNetTypeResponse().from_map(
            await self.do_rpcrequest_async('SwitchDBInstanceNetType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_net_type(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    async def switch_dbinstance_net_type_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceNetTypeRequest,
    ) -> rds_20140815_models.SwitchDBInstanceNetTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_net_type_with_options_async(request, runtime)

    def switch_dbinstance_vpc_with_options(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceVpcResponse().from_map(
            self.do_rpcrequest('SwitchDBInstanceVpc', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_dbinstance_vpc_with_options_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.SwitchDBInstanceVpcResponse().from_map(
            await self.do_rpcrequest_async('SwitchDBInstanceVpc', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_dbinstance_vpc(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    async def switch_dbinstance_vpc_async(
        self,
        request: rds_20140815_models.SwitchDBInstanceVpcRequest,
    ) -> rds_20140815_models.SwitchDBInstanceVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_dbinstance_vpc_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: rds_20140815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: rds_20140815_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: rds_20140815_models.TagResourcesRequest,
    ) -> rds_20140815_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: rds_20140815_models.TagResourcesRequest,
    ) -> rds_20140815_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def terminate_migrate_task_with_options(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TerminateMigrateTaskResponse().from_map(
            self.do_rpcrequest('TerminateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_migrate_task_with_options_async(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TerminateMigrateTaskResponse().from_map(
            await self.do_rpcrequest_async('TerminateMigrateTask', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_migrate_task(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    async def terminate_migrate_task_async(
        self,
        request: rds_20140815_models.TerminateMigrateTaskRequest,
    ) -> rds_20140815_models.TerminateMigrateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_migrate_task_with_options_async(request, runtime)

    def transform_dbinstance_pay_type_with_options(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TransformDBInstancePayTypeResponse().from_map(
            self.do_rpcrequest('TransformDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def transform_dbinstance_pay_type_with_options_async(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.TransformDBInstancePayTypeResponse().from_map(
            await self.do_rpcrequest_async('TransformDBInstancePayType', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def transform_dbinstance_pay_type(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    async def transform_dbinstance_pay_type_async(
        self,
        request: rds_20140815_models.TransformDBInstancePayTypeRequest,
    ) -> rds_20140815_models.TransformDBInstancePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transform_dbinstance_pay_type_with_options_async(request, runtime)

    def unlock_account_with_options(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UnlockAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UnlockAccountResponse().from_map(
            self.do_rpcrequest('UnlockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unlock_account_with_options_async(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UnlockAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UnlockAccountResponse().from_map(
            await self.do_rpcrequest_async('UnlockAccount', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_account(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
    ) -> rds_20140815_models.UnlockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    async def unlock_account_async(
        self,
        request: rds_20140815_models.UnlockAccountRequest,
    ) -> rds_20140815_models.UnlockAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unlock_account_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
    ) -> rds_20140815_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: rds_20140815_models.UntagResourcesRequest,
    ) -> rds_20140815_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBInstanceEngineVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBInstanceEngineVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_engine_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBInstanceEngineVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBInstanceEngineVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_engine_version(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    async def upgrade_dbinstance_engine_version_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceEngineVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceEngineVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_engine_version_with_options_async(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBInstanceKernelVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbinstance_kernel_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBInstanceKernelVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbinstance_kernel_version(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    async def upgrade_dbinstance_kernel_version_async(
        self,
        request: rds_20140815_models.UpgradeDBInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbinstance_kernel_version_with_options_async(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse().from_map(
            self.do_rpcrequest('UpgradeDBProxyInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_dbproxy_instance_kernel_version_with_options_async(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse().from_map(
            await self.do_rpcrequest_async('UpgradeDBProxyInstanceKernelVersion', '2014-08-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_dbproxy_instance_kernel_version(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)

    async def upgrade_dbproxy_instance_kernel_version_async(
        self,
        request: rds_20140815_models.UpgradeDBProxyInstanceKernelVersionRequest,
    ) -> rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_dbproxy_instance_kernel_version_with_options_async(request, runtime)
