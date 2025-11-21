# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_milvus20231012 import models as milvus_20231012_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('milvus', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: milvus_20231012_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: milvus_20231012_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/resourceGroup/change',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: milvus_20231012_models.ChangeResourceGroupRequest,
    ) -> milvus_20231012_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: milvus_20231012_models.ChangeResourceGroupRequest,
    ) -> milvus_20231012_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def create_default_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.CreateDefaultRoleResponse:
        """
        @summary Create a service role for Milvus to access other cloud products
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefaultRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDefaultRole',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.CreateDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_default_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.CreateDefaultRoleResponse:
        """
        @summary Create a service role for Milvus to access other cloud products
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDefaultRoleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CreateDefaultRole',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.CreateDefaultRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_default_role(self) -> milvus_20231012_models.CreateDefaultRoleResponse:
        """
        @summary Create a service role for Milvus to access other cloud products
        
        @return: CreateDefaultRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_default_role_with_options(headers, runtime)

    async def create_default_role_async(self) -> milvus_20231012_models.CreateDefaultRoleResponse:
        """
        @summary Create a service role for Milvus to access other cloud products
        
        @return: CreateDefaultRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_default_role_with_options_async(headers, runtime)

    def create_instance_with_options(
        self,
        request: milvus_20231012_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.db_admin_password):
            body['dbAdminPassword'] = request.db_admin_password
        if not UtilClient.is_unset(request.db_version):
            body['dbVersion'] = request.db_version
        if not UtilClient.is_unset(request.encrypted):
            body['encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.ha):
            body['ha'] = request.ha
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.kms_key_id):
            body['kmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.multi_zone_mode):
            body['multiZoneMode'] = request.multi_zone_mode
        if not UtilClient.is_unset(request.payment_duration):
            body['paymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_ids):
            body['vSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: milvus_20231012_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.db_admin_password):
            body['dbAdminPassword'] = request.db_admin_password
        if not UtilClient.is_unset(request.db_version):
            body['dbVersion'] = request.db_version
        if not UtilClient.is_unset(request.encrypted):
            body['encrypted'] = request.encrypted
        if not UtilClient.is_unset(request.ha):
            body['ha'] = request.ha
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.kms_key_id):
            body['kmsKeyId'] = request.kms_key_id
        if not UtilClient.is_unset(request.multi_zone_mode):
            body['multiZoneMode'] = request.multi_zone_mode
        if not UtilClient.is_unset(request.payment_duration):
            body['paymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            body['paymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.payment_type):
            body['paymentType'] = request.payment_type
        if not UtilClient.is_unset(request.resource_group_id):
            body['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_ids):
            body['vSwitchIds'] = request.v_switch_ids
        if not UtilClient.is_unset(request.vpc_id):
            body['vpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            body['zoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: milvus_20231012_models.CreateInstanceRequest,
    ) -> milvus_20231012_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: milvus_20231012_models.CreateInstanceRequest,
    ) -> milvus_20231012_models.CreateInstanceResponse:
        """
        @summary 创建实例
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def delete_instance_with_options(
        self,
        request: milvus_20231012_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: milvus_20231012_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/delete',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: milvus_20231012_models.DeleteInstanceRequest,
    ) -> milvus_20231012_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(request, headers, runtime)

    async def delete_instance_async(
        self,
        request: milvus_20231012_models.DeleteInstanceRequest,
    ) -> milvus_20231012_models.DeleteInstanceResponse:
        """
        @summary 删除实例
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(request, headers, runtime)

    def describe_access_control_list_with_options(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary Get the public IP address whitelist of a Milvus instance.
        
        @param request: DescribeAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/describe_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_access_control_list_with_options_async(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary Get the public IP address whitelist of a Milvus instance.
        
        @param request: DescribeAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/describe_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_access_control_list(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary Get the public IP address whitelist of a Milvus instance.
        
        @param request: DescribeAccessControlListRequest
        @return: DescribeAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_access_control_list_with_options(request, headers, runtime)

    async def describe_access_control_list_async(
        self,
        request: milvus_20231012_models.DescribeAccessControlListRequest,
    ) -> milvus_20231012_models.DescribeAccessControlListResponse:
        """
        @summary Get the public IP address whitelist of a Milvus instance.
        
        @param request: DescribeAccessControlListRequest
        @return: DescribeAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_access_control_list_with_options_async(request, headers, runtime)

    def describe_instance_configs_with_options(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary Get information about the custom configuration of each component of Milvus.
        
        @param request: DescribeInstanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceConfigs',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/describe_milvus_user_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeInstanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_configs_with_options_async(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary Get information about the custom configuration of each component of Milvus.
        
        @param request: DescribeInstanceConfigsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceConfigs',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/describe_milvus_user_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.DescribeInstanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_configs(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary Get information about the custom configuration of each component of Milvus.
        
        @param request: DescribeInstanceConfigsRequest
        @return: DescribeInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_instance_configs_with_options(request, headers, runtime)

    async def describe_instance_configs_async(
        self,
        request: milvus_20231012_models.DescribeInstanceConfigsRequest,
    ) -> milvus_20231012_models.DescribeInstanceConfigsResponse:
        """
        @summary Get information about the custom configuration of each component of Milvus.
        
        @param request: DescribeInstanceConfigsRequest
        @return: DescribeInstanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_instance_configs_with_options_async(request, headers, runtime)

    def get_instance_with_options(
        self,
        request: milvus_20231012_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceResponse:
        """
        @summary 获取实例详情
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: milvus_20231012_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceResponse:
        """
        @summary 获取实例详情
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/get',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: milvus_20231012_models.GetInstanceRequest,
    ) -> milvus_20231012_models.GetInstanceResponse:
        """
        @summary 获取实例详情
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(request, headers, runtime)

    async def get_instance_async(
        self,
        request: milvus_20231012_models.GetInstanceRequest,
    ) -> milvus_20231012_models.GetInstanceResponse:
        """
        @summary 获取实例详情
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(request, headers, runtime)

    def get_instance_detail_with_options(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary Get the details of an instance.
        
        @param request: GetInstanceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceDetail',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_detail_with_options_async(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary Get the details of an instance.
        
        @param request: GetInstanceDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceDetail',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.GetInstanceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_detail(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary Get the details of an instance.
        
        @param request: GetInstanceDetailRequest
        @return: GetInstanceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_detail_with_options(request, headers, runtime)

    async def get_instance_detail_async(
        self,
        request: milvus_20231012_models.GetInstanceDetailRequest,
    ) -> milvus_20231012_models.GetInstanceDetailResponse:
        """
        @summary Get the details of an instance.
        
        @param request: GetInstanceDetailRequest
        @return: GetInstanceDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_detail_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: milvus_20231012_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary Get the list of Milvus instances under the current account.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: milvus_20231012_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary Get the list of Milvus instances under the current account.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary Get the list of Milvus instances under the current account.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: milvus_20231012_models.ListInstancesRequest,
    ) -> milvus_20231012_models.ListInstancesResponse:
        """
        @summary Get the list of Milvus instances under the current account.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_instances_v2with_options(
        self,
        tmp_req: milvus_20231012_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesV2Response:
        """
        @summary 根据集群ID或者名称搜索集群
        
        @param tmp_req: ListInstancesV2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.ListInstancesV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesV2',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_v2with_options_async(
        self,
        tmp_req: milvus_20231012_models.ListInstancesV2Request,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ListInstancesV2Response:
        """
        @summary 根据集群ID或者名称搜索集群
        
        @param tmp_req: ListInstancesV2Request
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesV2Response
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.ListInstancesV2ShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.instance_id):
            query['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstancesV2',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/list',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ListInstancesV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances_v2(
        self,
        request: milvus_20231012_models.ListInstancesV2Request,
    ) -> milvus_20231012_models.ListInstancesV2Response:
        """
        @summary 根据集群ID或者名称搜索集群
        
        @param request: ListInstancesV2Request
        @return: ListInstancesV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_v2with_options(request, headers, runtime)

    async def list_instances_v2_async(
        self,
        request: milvus_20231012_models.ListInstancesV2Request,
    ) -> milvus_20231012_models.ListInstancesV2Response:
        """
        @summary 根据集群ID或者名称搜索集群
        
        @param request: ListInstancesV2Request
        @return: ListInstancesV2Response
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_v2with_options_async(request, headers, runtime)

    def modify_instance_config_with_options(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary Update the configuration parameters of each component of Milvus.
        
        @param request: ModifyInstanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/modify_milvus_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ModifyInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_instance_config_with_options_async(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary Update the configuration parameters of each component of Milvus.
        
        @param request: ModifyInstanceConfigRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.user_config):
            query['UserConfig'] = request.user_config
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceConfig',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/config/modify_milvus_config',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.ModifyInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_instance_config(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary Update the configuration parameters of each component of Milvus.
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.modify_instance_config_with_options(request, headers, runtime)

    async def modify_instance_config_async(
        self,
        request: milvus_20231012_models.ModifyInstanceConfigRequest,
    ) -> milvus_20231012_models.ModifyInstanceConfigResponse:
        """
        @summary Update the configuration parameters of each component of Milvus.
        
        @param request: ModifyInstanceConfigRequest
        @return: ModifyInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.modify_instance_config_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: milvus_20231012_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: milvus_20231012_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: milvus_20231012_models.TagResourcesRequest,
    ) -> milvus_20231012_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: milvus_20231012_models.TagResourcesRequest,
    ) -> milvus_20231012_models.TagResourcesResponse:
        """
        @summary 打标
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def un_tag_resources_with_options(
        self,
        tmp_req: milvus_20231012_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param tmp_req: UnTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.UnTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        tmp_req: milvus_20231012_models.UnTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param tmp_req: UnTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = milvus_20231012_models.UnTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_id):
            request.resource_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_id, 'ResourceId', 'json')
        if not UtilClient.is_unset(tmp_req.tag_key):
            request.tag_key_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag_key, 'TagKey', 'json')
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id_shrink):
            query['ResourceId'] = request.resource_id_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key_shrink):
            query['TagKey'] = request.tag_key_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagResources',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/tags',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: milvus_20231012_models.UnTagResourcesRequest,
    ) -> milvus_20231012_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.un_tag_resources_with_options(request, headers, runtime)

    async def un_tag_resources_async(
        self,
        request: milvus_20231012_models.UnTagResourcesRequest,
    ) -> milvus_20231012_models.UnTagResourcesResponse:
        """
        @summary 删除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.un_tag_resources_with_options_async(request, headers, runtime)

    def update_access_control_list_with_options(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary Configure Public IP Address Whitelist
        
        @param request: UpdateAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/update_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_access_control_list_with_options_async(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary Configure Public IP Address Whitelist
        
        @param request: UpdateAccessControlListRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccessControlList',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/milvus/update_access_control_list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateAccessControlListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_access_control_list(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary Configure Public IP Address Whitelist
        
        @param request: UpdateAccessControlListRequest
        @return: UpdateAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_access_control_list_with_options(request, headers, runtime)

    async def update_access_control_list_async(
        self,
        request: milvus_20231012_models.UpdateAccessControlListRequest,
    ) -> milvus_20231012_models.UpdateAccessControlListResponse:
        """
        @summary Configure Public IP Address Whitelist
        
        @param request: UpdateAccessControlListRequest
        @return: UpdateAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_access_control_list_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        request: milvus_20231012_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.ha):
            body['ha'] = request.ha
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: milvus_20231012_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.auto_backup):
            body['autoBackup'] = request.auto_backup
        if not UtilClient.is_unset(request.components):
            body['components'] = request.components
        if not UtilClient.is_unset(request.configuration):
            body['configuration'] = request.configuration
        if not UtilClient.is_unset(request.ha):
            body['ha'] = request.ha
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/instance/update',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: milvus_20231012_models.UpdateInstanceRequest,
    ) -> milvus_20231012_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(request, headers, runtime)

    async def update_instance_async(
        self,
        request: milvus_20231012_models.UpdateInstanceRequest,
    ) -> milvus_20231012_models.UpdateInstanceResponse:
        """
        @summary 更新实例
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(request, headers, runtime)

    def update_instance_name_with_options(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_name_with_options_async(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceName',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdateInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_name(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_name_with_options(request, headers, runtime)

    async def update_instance_name_async(
        self,
        request: milvus_20231012_models.UpdateInstanceNameRequest,
    ) -> milvus_20231012_models.UpdateInstanceNameResponse:
        """
        @summary Modifies the name of an instance.
        
        @param request: UpdateInstanceNameRequest
        @return: UpdateInstanceNameResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_name_with_options_async(request, headers, runtime)

    def update_public_network_status_with_options(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary Enable or disable Internet access for Milvus.
        
        @param request: UpdatePublicNetworkStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicNetworkStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetworkStatus',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/network/updatePublicNetworkStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdatePublicNetworkStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_public_network_status_with_options_async(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary Enable or disable Internet access for Milvus.
        
        @param request: UpdatePublicNetworkStatusRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePublicNetworkStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cidr):
            query['Cidr'] = request.cidr
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.public_network_enabled):
            query['PublicNetworkEnabled'] = request.public_network_enabled
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePublicNetworkStatus',
            version='2023-10-12',
            protocol='HTTPS',
            pathname=f'/webapi/network/updatePublicNetworkStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            milvus_20231012_models.UpdatePublicNetworkStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_public_network_status(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary Enable or disable Internet access for Milvus.
        
        @param request: UpdatePublicNetworkStatusRequest
        @return: UpdatePublicNetworkStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_public_network_status_with_options(request, headers, runtime)

    async def update_public_network_status_async(
        self,
        request: milvus_20231012_models.UpdatePublicNetworkStatusRequest,
    ) -> milvus_20231012_models.UpdatePublicNetworkStatusResponse:
        """
        @summary Enable or disable Internet access for Milvus.
        
        @param request: UpdatePublicNetworkStatusRequest
        @return: UpdatePublicNetworkStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_public_network_status_with_options_async(request, headers, runtime)
