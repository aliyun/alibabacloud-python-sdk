# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tablestore20201209 import models as tablestore_20201209_models
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
        self._endpoint = self.get_endpoint('tablestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: tablestore_20201209_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/changeresourcegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: tablestore_20201209_models.ChangeResourceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            body['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/changeresourcegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: tablestore_20201209_models.ChangeResourceGroupRequest,
    ) -> tablestore_20201209_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.change_resource_group_with_options(request, headers, runtime)

    async def change_resource_group_async(
        self,
        request: tablestore_20201209_models.ChangeResourceGroupRequest,
    ) -> tablestore_20201209_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which an instance belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.change_resource_group_with_options_async(request, headers, runtime)

    def check_instance_policy_with_options(
        self,
        request: tablestore_20201209_models.CheckInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.CheckInstancePolicyResponse:
        """
        @summary Checks the validity of a Resource Access Management (RAM) policy for an instance.
        
        @param request: CheckInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/checkinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.CheckInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_instance_policy_with_options_async(
        self,
        request: tablestore_20201209_models.CheckInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.CheckInstancePolicyResponse:
        """
        @summary Checks the validity of a Resource Access Management (RAM) policy for an instance.
        
        @param request: CheckInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/checkinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.CheckInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_instance_policy(
        self,
        request: tablestore_20201209_models.CheckInstancePolicyRequest,
    ) -> tablestore_20201209_models.CheckInstancePolicyResponse:
        """
        @summary Checks the validity of a Resource Access Management (RAM) policy for an instance.
        
        @param request: CheckInstancePolicyRequest
        @return: CheckInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_instance_policy_with_options(request, headers, runtime)

    async def check_instance_policy_async(
        self,
        request: tablestore_20201209_models.CheckInstancePolicyRequest,
    ) -> tablestore_20201209_models.CheckInstancePolicyResponse:
        """
        @summary Checks the validity of a Resource Access Management (RAM) policy for an instance.
        
        @param request: CheckInstancePolicyRequest
        @return: CheckInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_instance_policy_with_options_async(request, headers, runtime)

    def create_instance_with_options(
        self,
        request: tablestore_20201209_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.CreateInstanceResponse:
        """
        @summary Creates an instance.
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        Each Alibaba Cloud account can create up to 10 instances. The name of an instance must be unique within the region in which the instance resides.
        After you create an instance, you cannot change the type of the instance. Proceed with caution.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.disable_replication):
            body['DisableReplication'] = request.disable_replication
        if not UtilClient.is_unset(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            body['Network'] = request.network
        if not UtilClient.is_unset(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not UtilClient.is_unset(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/createinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: tablestore_20201209_models.CreateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.CreateInstanceResponse:
        """
        @summary Creates an instance.
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        Each Alibaba Cloud account can create up to 10 instances. The name of an instance must be unique within the region in which the instance resides.
        After you create an instance, you cannot change the type of the instance. Proceed with caution.
        
        @param request: CreateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.disable_replication):
            body['DisableReplication'] = request.disable_replication
        if not UtilClient.is_unset(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            body['Network'] = request.network
        if not UtilClient.is_unset(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not UtilClient.is_unset(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/createinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.CreateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance(
        self,
        request: tablestore_20201209_models.CreateInstanceRequest,
    ) -> tablestore_20201209_models.CreateInstanceResponse:
        """
        @summary Creates an instance.
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        Each Alibaba Cloud account can create up to 10 instances. The name of an instance must be unique within the region in which the instance resides.
        After you create an instance, you cannot change the type of the instance. Proceed with caution.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_instance_with_options(request, headers, runtime)

    async def create_instance_async(
        self,
        request: tablestore_20201209_models.CreateInstanceRequest,
    ) -> tablestore_20201209_models.CreateInstanceResponse:
        """
        @summary Creates an instance.
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        Each Alibaba Cloud account can create up to 10 instances. The name of an instance must be unique within the region in which the instance resides.
        After you create an instance, you cannot change the type of the instance. Proceed with caution.
        
        @param request: CreateInstanceRequest
        @return: CreateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_instance_with_options_async(request, headers, runtime)

    def delete_instance_with_options(
        self,
        request: tablestore_20201209_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance.
        
        @description    Before you delete an instance, make sure that all data tables and time series tables in the instance are deleted and virtual private clouds (VPCs) are unbound from the instance.
        To prevent conflicts, do not create an instance that has the same name as the instance that is being deleted.
        After an instance is deleted, the instance becomes unavailable and the tables, table data, and related indexes in the instance cannot be recovered. Proceed with caution.
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/deleteinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: tablestore_20201209_models.DeleteInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance.
        
        @description    Before you delete an instance, make sure that all data tables and time series tables in the instance are deleted and virtual private clouds (VPCs) are unbound from the instance.
        To prevent conflicts, do not create an instance that has the same name as the instance that is being deleted.
        After an instance is deleted, the instance becomes unavailable and the tables, table data, and related indexes in the instance cannot be recovered. Proceed with caution.
        
        @param request: DeleteInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/deleteinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: tablestore_20201209_models.DeleteInstanceRequest,
    ) -> tablestore_20201209_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance.
        
        @description    Before you delete an instance, make sure that all data tables and time series tables in the instance are deleted and virtual private clouds (VPCs) are unbound from the instance.
        To prevent conflicts, do not create an instance that has the same name as the instance that is being deleted.
        After an instance is deleted, the instance becomes unavailable and the tables, table data, and related indexes in the instance cannot be recovered. Proceed with caution.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_with_options(request, headers, runtime)

    async def delete_instance_async(
        self,
        request: tablestore_20201209_models.DeleteInstanceRequest,
    ) -> tablestore_20201209_models.DeleteInstanceResponse:
        """
        @summary Deletes an instance.
        
        @description    Before you delete an instance, make sure that all data tables and time series tables in the instance are deleted and virtual private clouds (VPCs) are unbound from the instance.
        To prevent conflicts, do not create an instance that has the same name as the instance that is being deleted.
        After an instance is deleted, the instance becomes unavailable and the tables, table data, and related indexes in the instance cannot be recovered. Proceed with caution.
        
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_with_options_async(request, headers, runtime)

    def delete_instance_policy_with_options(
        self,
        request: tablestore_20201209_models.DeleteInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DeleteInstancePolicyResponse:
        """
        @summary Deletes a Resource Access Management (RAM) policy of an instance.
        
        @description    You cannot recover a deleted instance policy. Proceed with caution.
        After you delete an instance policy, the access control that is specified by the instance policy becomes invalid. Make sure that your instance is in a secure environment.
        
        @param request: DeleteInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/deleteinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DeleteInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_policy_with_options_async(
        self,
        request: tablestore_20201209_models.DeleteInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DeleteInstancePolicyResponse:
        """
        @summary Deletes a Resource Access Management (RAM) policy of an instance.
        
        @description    You cannot recover a deleted instance policy. Proceed with caution.
        After you delete an instance policy, the access control that is specified by the instance policy becomes invalid. Make sure that your instance is in a secure environment.
        
        @param request: DeleteInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/deleteinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DeleteInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_policy(
        self,
        request: tablestore_20201209_models.DeleteInstancePolicyRequest,
    ) -> tablestore_20201209_models.DeleteInstancePolicyResponse:
        """
        @summary Deletes a Resource Access Management (RAM) policy of an instance.
        
        @description    You cannot recover a deleted instance policy. Proceed with caution.
        After you delete an instance policy, the access control that is specified by the instance policy becomes invalid. Make sure that your instance is in a secure environment.
        
        @param request: DeleteInstancePolicyRequest
        @return: DeleteInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_instance_policy_with_options(request, headers, runtime)

    async def delete_instance_policy_async(
        self,
        request: tablestore_20201209_models.DeleteInstancePolicyRequest,
    ) -> tablestore_20201209_models.DeleteInstancePolicyResponse:
        """
        @summary Deletes a Resource Access Management (RAM) policy of an instance.
        
        @description    You cannot recover a deleted instance policy. Proceed with caution.
        After you delete an instance policy, the access control that is specified by the instance policy becomes invalid. Make sure that your instance is in a secure environment.
        
        @param request: DeleteInstancePolicyRequest
        @return: DeleteInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_instance_policy_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        request: tablestore_20201209_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/region/DescribeRegions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: tablestore_20201209_models.DescribeRegionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/region/DescribeRegions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: tablestore_20201209_models.DescribeRegionsRequest,
    ) -> tablestore_20201209_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(request, headers, runtime)

    async def describe_regions_async(
        self,
        request: tablestore_20201209_models.DescribeRegionsRequest,
    ) -> tablestore_20201209_models.DescribeRegionsResponse:
        """
        @summary Queries supported regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(request, headers, runtime)

    def get_instance_with_options(
        self,
        request: tablestore_20201209_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.GetInstanceResponse:
        """
        @summary Queries instance information.
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/getinstance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: tablestore_20201209_models.GetInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.GetInstanceResponse:
        """
        @summary Queries instance information.
        
        @param request: GetInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/getinstance',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: tablestore_20201209_models.GetInstanceRequest,
    ) -> tablestore_20201209_models.GetInstanceResponse:
        """
        @summary Queries instance information.
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_instance_with_options(request, headers, runtime)

    async def get_instance_async(
        self,
        request: tablestore_20201209_models.GetInstanceRequest,
    ) -> tablestore_20201209_models.GetInstanceResponse:
        """
        @summary Queries instance information.
        
        @param request: GetInstanceRequest
        @return: GetInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_instance_with_options_async(request, headers, runtime)

    def list_instances_with_options(
        self,
        tmp_req: tablestore_20201209_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ListInstancesResponse:
        """
        @summary Queries instances.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = tablestore_20201209_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_name_list):
            request.instance_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_name_list, 'InstanceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_name_list_shrink):
            query['InstanceNameList'] = request.instance_name_list_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/listinstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instances_with_options_async(
        self,
        tmp_req: tablestore_20201209_models.ListInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ListInstancesResponse:
        """
        @summary Queries instances.
        
        @param tmp_req: ListInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = tablestore_20201209_models.ListInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_name_list):
            request.instance_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_name_list, 'InstanceNameList', 'simple')
        query = {}
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_name_list_shrink):
            query['InstanceNameList'] = request.instance_name_list_shrink
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/listinstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ListInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instances(
        self,
        request: tablestore_20201209_models.ListInstancesRequest,
    ) -> tablestore_20201209_models.ListInstancesResponse:
        """
        @summary Queries instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_instances_with_options(request, headers, runtime)

    async def list_instances_async(
        self,
        request: tablestore_20201209_models.ListInstancesRequest,
    ) -> tablestore_20201209_models.ListInstancesResponse:
        """
        @summary Queries instances.
        
        @param request: ListInstancesRequest
        @return: ListInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_instances_with_options_async(request, headers, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: tablestore_20201209_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = tablestore_20201209_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/listtagresources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        tmp_req: tablestore_20201209_models.ListTagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param tmp_req: ListTagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = tablestore_20201209_models.ListTagResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_ids):
            request.resource_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'simple')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/listtagresources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: tablestore_20201209_models.ListTagResourcesRequest,
    ) -> tablestore_20201209_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tag_resources_with_options(request, headers, runtime)

    async def list_tag_resources_async(
        self,
        request: tablestore_20201209_models.ListTagResourcesRequest,
    ) -> tablestore_20201209_models.ListTagResourcesResponse:
        """
        @summary Queries tagged resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tag_resources_with_options_async(request, headers, runtime)

    def tag_resources_with_options(
        self,
        request: tablestore_20201209_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.TagResourcesResponse:
        """
        @summary Adds tags to instances.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/tagresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: tablestore_20201209_models.TagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.TagResourcesResponse:
        """
        @summary Adds tags to instances.
        
        @param request: TagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/tagresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: tablestore_20201209_models.TagResourcesRequest,
    ) -> tablestore_20201209_models.TagResourcesResponse:
        """
        @summary Adds tags to instances.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.tag_resources_with_options(request, headers, runtime)

    async def tag_resources_async(
        self,
        request: tablestore_20201209_models.TagResourcesRequest,
    ) -> tablestore_20201209_models.TagResourcesResponse:
        """
        @summary Adds tags to instances.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.tag_resources_with_options_async(request, headers, runtime)

    def untag_resources_with_options(
        self,
        request: tablestore_20201209_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @description Removing tags from resources helps simplify resource management, optimize system performance, and mitigate potential security vulnerabilities. After a tag is removed from a resource, the system automatically deletes the tag if the tag is not added to other resources.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/untagresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: tablestore_20201209_models.UntagResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @description Removing tags from resources helps simplify resource management, optimize system performance, and mitigate potential security vulnerabilities. After a tag is removed from a resource, the system automatically deletes the tag if the tag is not added to other resources.
        
        @param request: UntagResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.all):
            body['All'] = request.all
        if not UtilClient.is_unset(request.resource_ids):
            body['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            body['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/untagresources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: tablestore_20201209_models.UntagResourcesRequest,
    ) -> tablestore_20201209_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @description Removing tags from resources helps simplify resource management, optimize system performance, and mitigate potential security vulnerabilities. After a tag is removed from a resource, the system automatically deletes the tag if the tag is not added to other resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.untag_resources_with_options(request, headers, runtime)

    async def untag_resources_async(
        self,
        request: tablestore_20201209_models.UntagResourcesRequest,
    ) -> tablestore_20201209_models.UntagResourcesResponse:
        """
        @summary Removes tags from resources.
        
        @description Removing tags from resources helps simplify resource management, optimize system performance, and mitigate potential security vulnerabilities. After a tag is removed from a resource, the system automatically deletes the tag if the tag is not added to other resources.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.untag_resources_with_options_async(request, headers, runtime)

    def update_instance_with_options(
        self,
        request: tablestore_20201209_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstanceResponse:
        """
        @summary Updates instance information.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            body['Network'] = request.network
        if not UtilClient.is_unset(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not UtilClient.is_unset(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_with_options_async(
        self,
        request: tablestore_20201209_models.UpdateInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstanceResponse:
        """
        @summary Updates instance information.
        
        @param request: UpdateInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alias_name):
            body['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.instance_description):
            body['InstanceDescription'] = request.instance_description
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.network):
            body['Network'] = request.network
        if not UtilClient.is_unset(request.network_source_acl):
            body['NetworkSourceACL'] = request.network_source_acl
        if not UtilClient.is_unset(request.network_type_acl):
            body['NetworkTypeACL'] = request.network_type_acl
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstance',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance(
        self,
        request: tablestore_20201209_models.UpdateInstanceRequest,
    ) -> tablestore_20201209_models.UpdateInstanceResponse:
        """
        @summary Updates instance information.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_with_options(request, headers, runtime)

    async def update_instance_async(
        self,
        request: tablestore_20201209_models.UpdateInstanceRequest,
    ) -> tablestore_20201209_models.UpdateInstanceResponse:
        """
        @summary Updates instance information.
        
        @param request: UpdateInstanceRequest
        @return: UpdateInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_with_options_async(request, headers, runtime)

    def update_instance_elastic_vcuupper_limit_with_options(
        self,
        request: tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse:
        """
        @summary Modifies the upper limit for the VCUs of an instance in VCU mode (formerly reserved mode).
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        After you enable scalability for an instance, the default upper limit for the VCUs of the instance is the sum of the scalability and the reserved VCUs.
        To use more computing resources when your business grows, you can modify the upper limit for the VCUs of your instance. The new upper limit for the VCUs of your instance immediately takes effect.
        
        @param request: UpdateInstanceElasticVCUUpperLimitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceElasticVCUUpperLimitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_vcuupper_limit):
            body['ElasticVCUUpperLimit'] = request.elastic_vcuupper_limit
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceElasticVCUUpperLimit',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstanceelasticvcuupperlimit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_elastic_vcuupper_limit_with_options_async(
        self,
        request: tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse:
        """
        @summary Modifies the upper limit for the VCUs of an instance in VCU mode (formerly reserved mode).
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        After you enable scalability for an instance, the default upper limit for the VCUs of the instance is the sum of the scalability and the reserved VCUs.
        To use more computing resources when your business grows, you can modify the upper limit for the VCUs of your instance. The new upper limit for the VCUs of your instance immediately takes effect.
        
        @param request: UpdateInstanceElasticVCUUpperLimitRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstanceElasticVCUUpperLimitResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.elastic_vcuupper_limit):
            body['ElasticVCUUpperLimit'] = request.elastic_vcuupper_limit
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstanceElasticVCUUpperLimit',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstanceelasticvcuupperlimit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_elastic_vcuupper_limit(
        self,
        request: tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitRequest,
    ) -> tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse:
        """
        @summary Modifies the upper limit for the VCUs of an instance in VCU mode (formerly reserved mode).
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        After you enable scalability for an instance, the default upper limit for the VCUs of the instance is the sum of the scalability and the reserved VCUs.
        To use more computing resources when your business grows, you can modify the upper limit for the VCUs of your instance. The new upper limit for the VCUs of your instance immediately takes effect.
        
        @param request: UpdateInstanceElasticVCUUpperLimitRequest
        @return: UpdateInstanceElasticVCUUpperLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_elastic_vcuupper_limit_with_options(request, headers, runtime)

    async def update_instance_elastic_vcuupper_limit_async(
        self,
        request: tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitRequest,
    ) -> tablestore_20201209_models.UpdateInstanceElasticVCUUpperLimitResponse:
        """
        @summary Modifies the upper limit for the VCUs of an instance in VCU mode (formerly reserved mode).
        
        @description    **Before you call this operation, you must understand the billing and pricing of Tablestore. For more information, see [Billing overview](https://help.aliyun.com/document_detail/27291.html).**\
        After you enable scalability for an instance, the default upper limit for the VCUs of the instance is the sum of the scalability and the reserved VCUs.
        To use more computing resources when your business grows, you can modify the upper limit for the VCUs of your instance. The new upper limit for the VCUs of your instance immediately takes effect.
        
        @param request: UpdateInstanceElasticVCUUpperLimitRequest
        @return: UpdateInstanceElasticVCUUpperLimitResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_elastic_vcuupper_limit_with_options_async(request, headers, runtime)

    def update_instance_policy_with_options(
        self,
        request: tablestore_20201209_models.UpdateInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstancePolicyResponse:
        """
        @summary Modifies a Resource Access Management (RAM) policy for an instance.
        
        @param request: UpdateInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstancePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_policy_with_options_async(
        self,
        request: tablestore_20201209_models.UpdateInstancePolicyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> tablestore_20201209_models.UpdateInstancePolicyResponse:
        """
        @summary Modifies a Resource Access Management (RAM) policy for an instance.
        
        @param request: UpdateInstancePolicyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateInstancePolicyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.policy):
            body['Policy'] = request.policy
        if not UtilClient.is_unset(request.policy_version):
            body['PolicyVersion'] = request.policy_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateInstancePolicy',
            version='2020-12-09',
            protocol='HTTPS',
            pathname=f'/v2/openapi/updateinstancepolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            tablestore_20201209_models.UpdateInstancePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_policy(
        self,
        request: tablestore_20201209_models.UpdateInstancePolicyRequest,
    ) -> tablestore_20201209_models.UpdateInstancePolicyResponse:
        """
        @summary Modifies a Resource Access Management (RAM) policy for an instance.
        
        @param request: UpdateInstancePolicyRequest
        @return: UpdateInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_instance_policy_with_options(request, headers, runtime)

    async def update_instance_policy_async(
        self,
        request: tablestore_20201209_models.UpdateInstancePolicyRequest,
    ) -> tablestore_20201209_models.UpdateInstancePolicyResponse:
        """
        @summary Modifies a Resource Access Management (RAM) policy for an instance.
        
        @param request: UpdateInstancePolicyRequest
        @return: UpdateInstancePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_instance_policy_with_options_async(request, headers, runtime)
