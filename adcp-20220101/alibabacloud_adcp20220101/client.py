# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adcp20220101 import models as adcp_20220101_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-beijing': 'adcp.cn-beijing.aliyuncs.com',
            'cn-zhangjiakou': 'adcp.cn-zhangjiakou.aliyuncs.com',
            'cn-hangzhou': 'adcp.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'adcp.cn-shanghai.aliyuncs.com',
            'cn-shenzhen': 'adcp.cn-shenzhen.aliyuncs.com',
            'cn-heyuan': 'adcp.cn-heyuan.aliyuncs.com',
            'cn-hongkong': 'adcp.cn-hongkong.aliyuncs.com',
            'ap-northeast-1': 'adcp.ap-northeast-1.aliyuncs.com',
            'ap-southeast-1': 'adcp.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'adcp.ap-southeast-5.aliyuncs.com',
            'ap-south-1': 'adcp.ap-south-1.aliyuncs.com',
            'ap-southeast-2': 'adcp.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'adcp.ap-southeast-3.aliyuncs.com',
            'cn-chengdu': 'adcp-vpc.cn-chengdu.aliyuncs.com',
            'cn-huhehaote': 'adcp.cn-huhehaote.aliyuncs.com',
            'cn-qingdao': 'adcp.cn-qingdao.aliyuncs.com',
            'cn-shanghai-finance-1': 'adcp-vpc.cn-shanghai-finance-1.aliyuncs.com',
            'cn-wulanchabu': 'adcp.cn-wulanchabu.aliyuncs.com',
            'eu-central-1': 'adcp.eu-central-1.aliyuncs.com',
            'eu-west-1': 'adcp-vpc.eu-west-1.aliyuncs.com',
            'me-east-1': 'adcp.me-east-1.aliyuncs.com',
            'us-east-1': 'adcp.us-east-1.aliyuncs.com',
            'us-west-1': 'adcp.us-west-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('adcp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_cluster_to_hub_with_options(
        self,
        request: adcp_20220101_models.AttachClusterToHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.AttachClusterToHubResponse:
        """
        @summary You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: AttachClusterToHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachClusterToHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_to_mesh):
            query['AttachToMesh'] = request.attach_to_mesh
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachClusterToHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.AttachClusterToHubResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_cluster_to_hub_with_options_async(
        self,
        request: adcp_20220101_models.AttachClusterToHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.AttachClusterToHubResponse:
        """
        @summary You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: AttachClusterToHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AttachClusterToHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attach_to_mesh):
            query['AttachToMesh'] = request.attach_to_mesh
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachClusterToHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.AttachClusterToHubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_cluster_to_hub(
        self,
        request: adcp_20220101_models.AttachClusterToHubRequest,
    ) -> adcp_20220101_models.AttachClusterToHubResponse:
        """
        @summary You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: AttachClusterToHubRequest
        @return: AttachClusterToHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_cluster_to_hub_with_options(request, runtime)

    async def attach_cluster_to_hub_async(
        self,
        request: adcp_20220101_models.AttachClusterToHubRequest,
    ) -> adcp_20220101_models.AttachClusterToHubResponse:
        """
        @summary You can search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: AttachClusterToHubRequest
        @return: AttachClusterToHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.attach_cluster_to_hub_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: adcp_20220101_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.ChangeResourceGroupResponse:
        """
        @summary 更新资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: adcp_20220101_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.ChangeResourceGroupResponse:
        """
        @summary 更新资源组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: adcp_20220101_models.ChangeResourceGroupRequest,
    ) -> adcp_20220101_models.ChangeResourceGroupResponse:
        """
        @summary 更新资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: adcp_20220101_models.ChangeResourceGroupRequest,
    ) -> adcp_20220101_models.ChangeResourceGroupResponse:
        """
        @summary 更新资源组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_hub_cluster_with_options(
        self,
        tmp_req: adcp_20220101_models.CreateHubClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.CreateHubClusterResponse:
        """
        @summary Creates a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param tmp_req: CreateHubClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHubClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.CreateHubClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.argo_server_enabled):
            body['ArgoServerEnabled'] = request.argo_server_enabled
        if not UtilClient.is_unset(request.audit_log_enabled):
            body['AuditLogEnabled'] = request.audit_log_enabled
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.price_limit):
            body['PriceLimit'] = request.price_limit
        if not UtilClient.is_unset(request.profile):
            body['Profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupID'] = request.resource_group_id
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_schedule_mode):
            body['WorkflowScheduleMode'] = request.workflow_schedule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.CreateHubClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hub_cluster_with_options_async(
        self,
        tmp_req: adcp_20220101_models.CreateHubClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.CreateHubClusterResponse:
        """
        @summary Creates a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param tmp_req: CreateHubClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateHubClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.CreateHubClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        body = {}
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.argo_server_enabled):
            body['ArgoServerEnabled'] = request.argo_server_enabled
        if not UtilClient.is_unset(request.audit_log_enabled):
            body['AuditLogEnabled'] = request.audit_log_enabled
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.price_limit):
            body['PriceLimit'] = request.price_limit
        if not UtilClient.is_unset(request.profile):
            body['Profile'] = request.profile
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupID'] = request.resource_group_id
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.workflow_schedule_mode):
            body['WorkflowScheduleMode'] = request.workflow_schedule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.CreateHubClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hub_cluster(
        self,
        request: adcp_20220101_models.CreateHubClusterRequest,
    ) -> adcp_20220101_models.CreateHubClusterResponse:
        """
        @summary Creates a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: CreateHubClusterRequest
        @return: CreateHubClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_hub_cluster_with_options(request, runtime)

    async def create_hub_cluster_async(
        self,
        request: adcp_20220101_models.CreateHubClusterRequest,
    ) -> adcp_20220101_models.CreateHubClusterResponse:
        """
        @summary Creates a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: CreateHubClusterRequest
        @return: CreateHubClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_hub_cluster_with_options_async(request, runtime)

    def delete_hub_cluster_with_options(
        self,
        tmp_req: adcp_20220101_models.DeleteHubClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeleteHubClusterResponse:
        """
        @summary Deletes a master cluster in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param tmp_req: DeleteHubClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHubClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeleteHubClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'RetainResources', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['RetainResources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeleteHubClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hub_cluster_with_options_async(
        self,
        tmp_req: adcp_20220101_models.DeleteHubClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeleteHubClusterResponse:
        """
        @summary Deletes a master cluster in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param tmp_req: DeleteHubClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteHubClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeleteHubClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retain_resources):
            request.retain_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.retain_resources, 'RetainResources', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.retain_resources_shrink):
            query['RetainResources'] = request.retain_resources_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeleteHubClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hub_cluster(
        self,
        request: adcp_20220101_models.DeleteHubClusterRequest,
    ) -> adcp_20220101_models.DeleteHubClusterResponse:
        """
        @summary Deletes a master cluster in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DeleteHubClusterRequest
        @return: DeleteHubClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_hub_cluster_with_options(request, runtime)

    async def delete_hub_cluster_async(
        self,
        request: adcp_20220101_models.DeleteHubClusterRequest,
    ) -> adcp_20220101_models.DeleteHubClusterResponse:
        """
        @summary Deletes a master cluster in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DeleteHubClusterRequest
        @return: DeleteHubClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_hub_cluster_with_options_async(request, runtime)

    def delete_policy_instance_with_options(
        self,
        tmp_req: adcp_20220101_models.DeletePolicyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes a policy for associated clusters.
        
        @param tmp_req: DeletePolicyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeletePolicyInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeletePolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_instance_with_options_async(
        self,
        tmp_req: adcp_20220101_models.DeletePolicyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes a policy for associated clusters.
        
        @param tmp_req: DeletePolicyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeletePolicyInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeletePolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy_instance(
        self,
        request: adcp_20220101_models.DeletePolicyInstanceRequest,
    ) -> adcp_20220101_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes a policy for associated clusters.
        
        @param request: DeletePolicyInstanceRequest
        @return: DeletePolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_instance_with_options(request, runtime)

    async def delete_policy_instance_async(
        self,
        request: adcp_20220101_models.DeletePolicyInstanceRequest,
    ) -> adcp_20220101_models.DeletePolicyInstanceResponse:
        """
        @summary Deletes a policy for associated clusters.
        
        @param request: DeletePolicyInstanceRequest
        @return: DeletePolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_instance_with_options_async(request, runtime)

    def delete_user_permission_with_options(
        self,
        request: adcp_20220101_models.DeleteUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeleteUserPermissionResponse:
        """
        @summary Deletes the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: DeleteUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeleteUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_permission_with_options_async(
        self,
        request: adcp_20220101_models.DeleteUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeleteUserPermissionResponse:
        """
        @summary Deletes the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: DeleteUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeleteUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user_permission(
        self,
        request: adcp_20220101_models.DeleteUserPermissionRequest,
    ) -> adcp_20220101_models.DeleteUserPermissionResponse:
        """
        @summary Deletes the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: DeleteUserPermissionRequest
        @return: DeleteUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_permission_with_options(request, runtime)

    async def delete_user_permission_async(
        self,
        request: adcp_20220101_models.DeleteUserPermissionRequest,
    ) -> adcp_20220101_models.DeleteUserPermissionResponse:
        """
        @summary Deletes the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: DeleteUserPermissionRequest
        @return: DeleteUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_permission_with_options_async(request, runtime)

    def deploy_policy_instance_with_options(
        self,
        tmp_req: adcp_20220101_models.DeployPolicyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy instance in the clusters that are associated with a master instance.
        
        @param tmp_req: DeployPolicyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployPolicyInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeployPolicyInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.namespaces):
            request.namespaces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not UtilClient.is_unset(request.policy_action):
            query['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployPolicyInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeployPolicyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_policy_instance_with_options_async(
        self,
        tmp_req: adcp_20220101_models.DeployPolicyInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy instance in the clusters that are associated with a master instance.
        
        @param tmp_req: DeployPolicyInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployPolicyInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DeployPolicyInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_ids):
            request.cluster_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.cluster_ids, 'ClusterIds', 'json')
        if not UtilClient.is_unset(tmp_req.namespaces):
            request.namespaces_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_ids_shrink):
            query['ClusterIds'] = request.cluster_ids_shrink
        if not UtilClient.is_unset(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not UtilClient.is_unset(request.policy_action):
            query['PolicyAction'] = request.policy_action
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployPolicyInstance',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeployPolicyInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_policy_instance(
        self,
        request: adcp_20220101_models.DeployPolicyInstanceRequest,
    ) -> adcp_20220101_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy instance in the clusters that are associated with a master instance.
        
        @param request: DeployPolicyInstanceRequest
        @return: DeployPolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_policy_instance_with_options(request, runtime)

    async def deploy_policy_instance_async(
        self,
        request: adcp_20220101_models.DeployPolicyInstanceRequest,
    ) -> adcp_20220101_models.DeployPolicyInstanceResponse:
        """
        @summary Deploys a policy instance in the clusters that are associated with a master instance.
        
        @param request: DeployPolicyInstanceRequest
        @return: DeployPolicyInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_policy_instance_with_options_async(request, runtime)

    def describe_hub_cluster_details_with_options(
        self,
        request: adcp_20220101_models.DescribeHubClusterDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterDetailsResponse:
        """
        @summary Queries the details of a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DescribeHubClusterDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterDetails',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hub_cluster_details_with_options_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterDetailsResponse:
        """
        @summary Queries the details of a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DescribeHubClusterDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterDetails',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hub_cluster_details(
        self,
        request: adcp_20220101_models.DescribeHubClusterDetailsRequest,
    ) -> adcp_20220101_models.DescribeHubClusterDetailsResponse:
        """
        @summary Queries the details of a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DescribeHubClusterDetailsRequest
        @return: DescribeHubClusterDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_details_with_options(request, runtime)

    async def describe_hub_cluster_details_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterDetailsRequest,
    ) -> adcp_20220101_models.DescribeHubClusterDetailsResponse:
        """
        @summary Queries the details of a master instance in Alibaba Cloud Distributed Cloud Container Platform (ACK One).
        
        @param request: DescribeHubClusterDetailsRequest
        @return: DescribeHubClusterDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hub_cluster_details_with_options_async(request, runtime)

    def describe_hub_cluster_kubeconfig_with_options(
        self,
        request: adcp_20220101_models.DescribeHubClusterKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterKubeconfigResponse:
        """
        @summary Queries the kubeconfig file of a Distributed Cloud Container Platform for Kubernetes (ACK One) cluster. In addition to the Container Service for Kubernetes (ACK) console, you can also use the Kubernetes CLI kubectl to manage clusters and applications. If you use kubectl to manage an ACK cluster, you must obtain the kubeconfig file of the cluster and use kubectl to connect to the cluster.
        
        @param request: DescribeHubClusterKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterKubeconfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hub_cluster_kubeconfig_with_options_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterKubeconfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterKubeconfigResponse:
        """
        @summary Queries the kubeconfig file of a Distributed Cloud Container Platform for Kubernetes (ACK One) cluster. In addition to the Container Service for Kubernetes (ACK) console, you can also use the Kubernetes CLI kubectl to manage clusters and applications. If you use kubectl to manage an ACK cluster, you must obtain the kubeconfig file of the cluster and use kubectl to connect to the cluster.
        
        @param request: DescribeHubClusterKubeconfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterKubeconfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterKubeconfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterKubeconfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hub_cluster_kubeconfig(
        self,
        request: adcp_20220101_models.DescribeHubClusterKubeconfigRequest,
    ) -> adcp_20220101_models.DescribeHubClusterKubeconfigResponse:
        """
        @summary Queries the kubeconfig file of a Distributed Cloud Container Platform for Kubernetes (ACK One) cluster. In addition to the Container Service for Kubernetes (ACK) console, you can also use the Kubernetes CLI kubectl to manage clusters and applications. If you use kubectl to manage an ACK cluster, you must obtain the kubeconfig file of the cluster and use kubectl to connect to the cluster.
        
        @param request: DescribeHubClusterKubeconfigRequest
        @return: DescribeHubClusterKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_kubeconfig_with_options(request, runtime)

    async def describe_hub_cluster_kubeconfig_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterKubeconfigRequest,
    ) -> adcp_20220101_models.DescribeHubClusterKubeconfigResponse:
        """
        @summary Queries the kubeconfig file of a Distributed Cloud Container Platform for Kubernetes (ACK One) cluster. In addition to the Container Service for Kubernetes (ACK) console, you can also use the Kubernetes CLI kubectl to manage clusters and applications. If you use kubectl to manage an ACK cluster, you must obtain the kubeconfig file of the cluster and use kubectl to connect to the cluster.
        
        @param request: DescribeHubClusterKubeconfigRequest
        @return: DescribeHubClusterKubeconfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hub_cluster_kubeconfig_with_options_async(request, runtime)

    def describe_hub_cluster_logs_with_options(
        self,
        request: adcp_20220101_models.DescribeHubClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterLogsResponse:
        """
        @summary Queries the logs of the Fleet instance of a multi-cluster fleet of Distributed Cloud Container Platform for Kubernetes (ACK One).
        
        @param request: DescribeHubClusterLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterLogs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hub_cluster_logs_with_options_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClusterLogsResponse:
        """
        @summary Queries the logs of the Fleet instance of a multi-cluster fleet of Distributed Cloud Container Platform for Kubernetes (ACK One).
        
        @param request: DescribeHubClusterLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClusterLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterLogs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hub_cluster_logs(
        self,
        request: adcp_20220101_models.DescribeHubClusterLogsRequest,
    ) -> adcp_20220101_models.DescribeHubClusterLogsResponse:
        """
        @summary Queries the logs of the Fleet instance of a multi-cluster fleet of Distributed Cloud Container Platform for Kubernetes (ACK One).
        
        @param request: DescribeHubClusterLogsRequest
        @return: DescribeHubClusterLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_logs_with_options(request, runtime)

    async def describe_hub_cluster_logs_async(
        self,
        request: adcp_20220101_models.DescribeHubClusterLogsRequest,
    ) -> adcp_20220101_models.DescribeHubClusterLogsResponse:
        """
        @summary Queries the logs of the Fleet instance of a multi-cluster fleet of Distributed Cloud Container Platform for Kubernetes (ACK One).
        
        @param request: DescribeHubClusterLogsRequest
        @return: DescribeHubClusterLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hub_cluster_logs_with_options_async(request, runtime)

    def describe_hub_clusters_with_options(
        self,
        tmp_req: adcp_20220101_models.DescribeHubClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClustersResponse:
        """
        @summary Queries the Distributed Cloud Container Platform for Kubernetes (ACK One) clusters that are created by the current user.
        
        @param tmp_req: DescribeHubClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DescribeHubClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hub_clusters_with_options_async(
        self,
        tmp_req: adcp_20220101_models.DescribeHubClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeHubClustersResponse:
        """
        @summary Queries the Distributed Cloud Container Platform for Kubernetes (ACK One) clusters that are created by the current user.
        
        @param tmp_req: DescribeHubClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeHubClustersResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.DescribeHubClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hub_clusters(
        self,
        request: adcp_20220101_models.DescribeHubClustersRequest,
    ) -> adcp_20220101_models.DescribeHubClustersResponse:
        """
        @summary Queries the Distributed Cloud Container Platform for Kubernetes (ACK One) clusters that are created by the current user.
        
        @param request: DescribeHubClustersRequest
        @return: DescribeHubClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_clusters_with_options(request, runtime)

    async def describe_hub_clusters_async(
        self,
        request: adcp_20220101_models.DescribeHubClustersRequest,
    ) -> adcp_20220101_models.DescribeHubClustersResponse:
        """
        @summary Queries the Distributed Cloud Container Platform for Kubernetes (ACK One) clusters that are created by the current user.
        
        @param request: DescribeHubClustersRequest
        @return: DescribeHubClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_hub_clusters_with_options_async(request, runtime)

    def describe_managed_clusters_with_options(
        self,
        request: adcp_20220101_models.DescribeManagedClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeManagedClustersResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DescribeManagedClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManagedClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManagedClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeManagedClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_managed_clusters_with_options_async(
        self,
        request: adcp_20220101_models.DescribeManagedClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeManagedClustersResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DescribeManagedClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManagedClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManagedClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeManagedClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_managed_clusters(
        self,
        request: adcp_20220101_models.DescribeManagedClustersRequest,
    ) -> adcp_20220101_models.DescribeManagedClustersResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DescribeManagedClustersRequest
        @return: DescribeManagedClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_managed_clusters_with_options(request, runtime)

    async def describe_managed_clusters_async(
        self,
        request: adcp_20220101_models.DescribeManagedClustersRequest,
    ) -> adcp_20220101_models.DescribeManagedClustersResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DescribeManagedClustersRequest
        @return: DescribeManagedClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_managed_clusters_with_options_async(request, runtime)

    def describe_policies_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePoliciesResponse:
        """
        @summary Queries a list of policies.
        
        @param request: DescribePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribePolicies',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policies_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePoliciesResponse:
        """
        @summary Queries a list of policies.
        
        @param request: DescribePoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePoliciesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribePolicies',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policies(self) -> adcp_20220101_models.DescribePoliciesResponse:
        """
        @summary Queries a list of policies.
        
        @return: DescribePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policies_with_options(runtime)

    async def describe_policies_async(self) -> adcp_20220101_models.DescribePoliciesResponse:
        """
        @summary Queries a list of policies.
        
        @return: DescribePoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policies_with_options_async(runtime)

    def describe_policy_details_with_options(
        self,
        request: adcp_20220101_models.DescribePolicyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyDetailsResponse:
        """
        @summary Queries detailed information about a policy.
        
        @param request: DescribePolicyDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyDetails',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_details_with_options_async(
        self,
        request: adcp_20220101_models.DescribePolicyDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyDetailsResponse:
        """
        @summary Queries detailed information about a policy.
        
        @param request: DescribePolicyDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyDetails',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_details(
        self,
        request: adcp_20220101_models.DescribePolicyDetailsRequest,
    ) -> adcp_20220101_models.DescribePolicyDetailsResponse:
        """
        @summary Queries detailed information about a policy.
        
        @param request: DescribePolicyDetailsRequest
        @return: DescribePolicyDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_details_with_options(request, runtime)

    async def describe_policy_details_async(
        self,
        request: adcp_20220101_models.DescribePolicyDetailsRequest,
    ) -> adcp_20220101_models.DescribePolicyDetailsResponse:
        """
        @summary Queries detailed information about a policy.
        
        @param request: DescribePolicyDetailsRequest
        @return: DescribePolicyDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_details_with_options_async(request, runtime)

    def describe_policy_governance_in_cluster_with_options(
        self,
        request: adcp_20220101_models.DescribePolicyGovernanceInClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Queries detailed information about the policies used by the clusters that are associated with a master instance.
        
        @param request: DescribePolicyGovernanceInClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyGovernanceInClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyGovernanceInCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyGovernanceInClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_governance_in_cluster_with_options_async(
        self,
        request: adcp_20220101_models.DescribePolicyGovernanceInClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Queries detailed information about the policies used by the clusters that are associated with a master instance.
        
        @param request: DescribePolicyGovernanceInClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyGovernanceInClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyGovernanceInCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyGovernanceInClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_governance_in_cluster(
        self,
        request: adcp_20220101_models.DescribePolicyGovernanceInClusterRequest,
    ) -> adcp_20220101_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Queries detailed information about the policies used by the clusters that are associated with a master instance.
        
        @param request: DescribePolicyGovernanceInClusterRequest
        @return: DescribePolicyGovernanceInClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_governance_in_cluster_with_options(request, runtime)

    async def describe_policy_governance_in_cluster_async(
        self,
        request: adcp_20220101_models.DescribePolicyGovernanceInClusterRequest,
    ) -> adcp_20220101_models.DescribePolicyGovernanceInClusterResponse:
        """
        @summary Queries detailed information about the policies used by the clusters that are associated with a master instance.
        
        @param request: DescribePolicyGovernanceInClusterRequest
        @return: DescribePolicyGovernanceInClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_governance_in_cluster_with_options_async(request, runtime)

    def describe_policy_instances_with_options(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyInstancesResponse:
        """
        @summary Queries policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstances',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_with_options_async(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyInstancesResponse:
        """
        @summary Queries policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstances',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesRequest,
    ) -> adcp_20220101_models.DescribePolicyInstancesResponse:
        """
        @summary Queries policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesRequest
        @return: DescribePolicyInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_instances_with_options(request, runtime)

    async def describe_policy_instances_async(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesRequest,
    ) -> adcp_20220101_models.DescribePolicyInstancesResponse:
        """
        @summary Queries policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesRequest
        @return: DescribePolicyInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_instances_with_options_async(request, runtime)

    def describe_policy_instances_status_with_options(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries detailed information about policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstancesStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyInstancesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_policy_instances_status_with_options_async(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries detailed information about policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePolicyInstancesStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePolicyInstancesStatus',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribePolicyInstancesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_policy_instances_status(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesStatusRequest,
    ) -> adcp_20220101_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries detailed information about policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesStatusRequest
        @return: DescribePolicyInstancesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_instances_status_with_options(request, runtime)

    async def describe_policy_instances_status_async(
        self,
        request: adcp_20220101_models.DescribePolicyInstancesStatusRequest,
    ) -> adcp_20220101_models.DescribePolicyInstancesStatusResponse:
        """
        @summary Queries detailed information about policy instances that are deployed in the clusters associated with a master instance.
        
        @param request: DescribePolicyInstancesStatusRequest
        @return: DescribePolicyInstancesStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_policy_instances_status_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: adcp_20220101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeRegionsResponse:
        """
        @summary 查询地域列表
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: adcp_20220101_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeRegionsResponse:
        """
        @summary 查询地域列表
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: adcp_20220101_models.DescribeRegionsRequest,
    ) -> adcp_20220101_models.DescribeRegionsResponse:
        """
        @summary 查询地域列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: adcp_20220101_models.DescribeRegionsRequest,
    ) -> adcp_20220101_models.DescribeRegionsResponse:
        """
        @summary 查询地域列表
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_user_permissions_with_options(
        self,
        request: adcp_20220101_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeUserPermissionsResponse:
        """
        @summary Query the permissions of a Resource Access Management (RAM) user.
        
        @param request: DescribeUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_user_permissions_with_options_async(
        self,
        request: adcp_20220101_models.DescribeUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DescribeUserPermissionsResponse:
        """
        @summary Query the permissions of a Resource Access Management (RAM) user.
        
        @param request: DescribeUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeUserPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserPermissions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_user_permissions(
        self,
        request: adcp_20220101_models.DescribeUserPermissionsRequest,
    ) -> adcp_20220101_models.DescribeUserPermissionsResponse:
        """
        @summary Query the permissions of a Resource Access Management (RAM) user.
        
        @param request: DescribeUserPermissionsRequest
        @return: DescribeUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_user_permissions_with_options(request, runtime)

    async def describe_user_permissions_async(
        self,
        request: adcp_20220101_models.DescribeUserPermissionsRequest,
    ) -> adcp_20220101_models.DescribeUserPermissionsResponse:
        """
        @summary Query the permissions of a Resource Access Management (RAM) user.
        
        @param request: DescribeUserPermissionsRequest
        @return: DescribeUserPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_permissions_with_options_async(request, runtime)

    def detach_cluster_from_hub_with_options(
        self,
        request: adcp_20220101_models.DetachClusterFromHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DetachClusterFromHubResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DetachClusterFromHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachClusterFromHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.detach_from_mesh):
            query['DetachFromMesh'] = request.detach_from_mesh
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachClusterFromHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DetachClusterFromHubResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_cluster_from_hub_with_options_async(
        self,
        request: adcp_20220101_models.DetachClusterFromHubRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.DetachClusterFromHubResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DetachClusterFromHubRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DetachClusterFromHubResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.detach_from_mesh):
            query['DetachFromMesh'] = request.detach_from_mesh
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachClusterFromHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DetachClusterFromHubResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_cluster_from_hub(
        self,
        request: adcp_20220101_models.DetachClusterFromHubRequest,
    ) -> adcp_20220101_models.DetachClusterFromHubResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DetachClusterFromHubRequest
        @return: DetachClusterFromHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.detach_cluster_from_hub_with_options(request, runtime)

    async def detach_cluster_from_hub_async(
        self,
        request: adcp_20220101_models.DetachClusterFromHubRequest,
    ) -> adcp_20220101_models.DetachClusterFromHubResponse:
        """
        @summary Alibaba Cloud CLI allows you to search for API operations, call and debug API operations online, and dynamically generate executable sample code for SDKs.
        
        @param request: DetachClusterFromHubRequest
        @return: DetachClusterFromHubResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.detach_cluster_from_hub_with_options_async(request, runtime)

    def grant_user_permission_with_options(
        self,
        request: adcp_20220101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.GrantUserPermissionResponse:
        """
        @summary Grants role-based access control (RBAC) permissions to Resource Access Management (RAM) users or RAM roles. System policies can be attached to RAM users to grant only the operation permissions on Distributed Cloud Container Platform for Kubernetes (ACK One) cluster resources. The operation permissions include creating and viewing instances. If you want to perform operations on Kubernetes resources in a specific cluster by using a RAM user or assuming a RAM role, such as creating GitOps applications and Argo workflows, you must grant RBAC permissions to the RAM user or RAM role to perform operations on the specified ACK One cluster and namespace. This topic describes how to grant RBAC permissions to a RAM user or RAM role.
        
        @description    To call this API operation to grant permissions to a RAM user or RAM role on a specific cluster, you must use an Alibaba Cloud account, the account that is used to create the cluster, or a RAM user that has the cluster administrator permissions. A regular RAM user does not have the permissions to call this operation.
        Before you grant RBAC permissions to a RAM user or RAM role on a cluster, you must grant the operation permissions to the RAM user or RAM role on the specified cluster. For more information, see [Attach a system permission policy to a RAM user or RAM role](https://help.aliyun.com/document_detail/613486.html).
        For more information, see [Authorization overview](https://help.aliyun.com/document_detail/613468.html).
        
        @param request: GrantUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.is_ram_role):
            query['IsRamRole'] = request.is_ram_role
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.GrantUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_permission_with_options_async(
        self,
        request: adcp_20220101_models.GrantUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.GrantUserPermissionResponse:
        """
        @summary Grants role-based access control (RBAC) permissions to Resource Access Management (RAM) users or RAM roles. System policies can be attached to RAM users to grant only the operation permissions on Distributed Cloud Container Platform for Kubernetes (ACK One) cluster resources. The operation permissions include creating and viewing instances. If you want to perform operations on Kubernetes resources in a specific cluster by using a RAM user or assuming a RAM role, such as creating GitOps applications and Argo workflows, you must grant RBAC permissions to the RAM user or RAM role to perform operations on the specified ACK One cluster and namespace. This topic describes how to grant RBAC permissions to a RAM user or RAM role.
        
        @description    To call this API operation to grant permissions to a RAM user or RAM role on a specific cluster, you must use an Alibaba Cloud account, the account that is used to create the cluster, or a RAM user that has the cluster administrator permissions. A regular RAM user does not have the permissions to call this operation.
        Before you grant RBAC permissions to a RAM user or RAM role on a cluster, you must grant the operation permissions to the RAM user or RAM role on the specified cluster. For more information, see [Attach a system permission policy to a RAM user or RAM role](https://help.aliyun.com/document_detail/613486.html).
        For more information, see [Authorization overview](https://help.aliyun.com/document_detail/613468.html).
        
        @param request: GrantUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.is_ram_role):
            query['IsRamRole'] = request.is_ram_role
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.GrantUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_user_permission(
        self,
        request: adcp_20220101_models.GrantUserPermissionRequest,
    ) -> adcp_20220101_models.GrantUserPermissionResponse:
        """
        @summary Grants role-based access control (RBAC) permissions to Resource Access Management (RAM) users or RAM roles. System policies can be attached to RAM users to grant only the operation permissions on Distributed Cloud Container Platform for Kubernetes (ACK One) cluster resources. The operation permissions include creating and viewing instances. If you want to perform operations on Kubernetes resources in a specific cluster by using a RAM user or assuming a RAM role, such as creating GitOps applications and Argo workflows, you must grant RBAC permissions to the RAM user or RAM role to perform operations on the specified ACK One cluster and namespace. This topic describes how to grant RBAC permissions to a RAM user or RAM role.
        
        @description    To call this API operation to grant permissions to a RAM user or RAM role on a specific cluster, you must use an Alibaba Cloud account, the account that is used to create the cluster, or a RAM user that has the cluster administrator permissions. A regular RAM user does not have the permissions to call this operation.
        Before you grant RBAC permissions to a RAM user or RAM role on a cluster, you must grant the operation permissions to the RAM user or RAM role on the specified cluster. For more information, see [Attach a system permission policy to a RAM user or RAM role](https://help.aliyun.com/document_detail/613486.html).
        For more information, see [Authorization overview](https://help.aliyun.com/document_detail/613468.html).
        
        @param request: GrantUserPermissionRequest
        @return: GrantUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permission_with_options(request, runtime)

    async def grant_user_permission_async(
        self,
        request: adcp_20220101_models.GrantUserPermissionRequest,
    ) -> adcp_20220101_models.GrantUserPermissionResponse:
        """
        @summary Grants role-based access control (RBAC) permissions to Resource Access Management (RAM) users or RAM roles. System policies can be attached to RAM users to grant only the operation permissions on Distributed Cloud Container Platform for Kubernetes (ACK One) cluster resources. The operation permissions include creating and viewing instances. If you want to perform operations on Kubernetes resources in a specific cluster by using a RAM user or assuming a RAM role, such as creating GitOps applications and Argo workflows, you must grant RBAC permissions to the RAM user or RAM role to perform operations on the specified ACK One cluster and namespace. This topic describes how to grant RBAC permissions to a RAM user or RAM role.
        
        @description    To call this API operation to grant permissions to a RAM user or RAM role on a specific cluster, you must use an Alibaba Cloud account, the account that is used to create the cluster, or a RAM user that has the cluster administrator permissions. A regular RAM user does not have the permissions to call this operation.
        Before you grant RBAC permissions to a RAM user or RAM role on a cluster, you must grant the operation permissions to the RAM user or RAM role on the specified cluster. For more information, see [Attach a system permission policy to a RAM user or RAM role](https://help.aliyun.com/document_detail/613486.html).
        For more information, see [Authorization overview](https://help.aliyun.com/document_detail/613468.html).
        
        @param request: GrantUserPermissionRequest
        @return: GrantUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_permission_with_options_async(request, runtime)

    def grant_user_permissions_with_options(
        self,
        tmp_req: adcp_20220101_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.GrantUserPermissionsResponse:
        """
        @deprecated OpenAPI GrantUserPermissions is deprecated, please use adcp::2022-01-01::GrantUserPermission instead.
        
        @summary Grant permissions to a Resource Access Management (RAM) user.
        
        @param tmp_req: GrantUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionsResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not UtilClient.is_unset(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.GrantUserPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_user_permissions_with_options_async(
        self,
        tmp_req: adcp_20220101_models.GrantUserPermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.GrantUserPermissionsResponse:
        """
        @deprecated OpenAPI GrantUserPermissions is deprecated, please use adcp::2022-01-01::GrantUserPermission instead.
        
        @summary Grant permissions to a Resource Access Management (RAM) user.
        
        @param tmp_req: GrantUserPermissionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GrantUserPermissionsResponse
        Deprecated
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.GrantUserPermissionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.permissions):
            request.permissions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.permissions, 'Permissions', 'json')
        query = {}
        if not UtilClient.is_unset(request.permissions_shrink):
            query['Permissions'] = request.permissions_shrink
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GrantUserPermissions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.GrantUserPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_user_permissions(
        self,
        request: adcp_20220101_models.GrantUserPermissionsRequest,
    ) -> adcp_20220101_models.GrantUserPermissionsResponse:
        """
        @deprecated OpenAPI GrantUserPermissions is deprecated, please use adcp::2022-01-01::GrantUserPermission instead.
        
        @summary Grant permissions to a Resource Access Management (RAM) user.
        
        @param request: GrantUserPermissionsRequest
        @return: GrantUserPermissionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.grant_user_permissions_with_options(request, runtime)

    async def grant_user_permissions_async(
        self,
        request: adcp_20220101_models.GrantUserPermissionsRequest,
    ) -> adcp_20220101_models.GrantUserPermissionsResponse:
        """
        @deprecated OpenAPI GrantUserPermissions is deprecated, please use adcp::2022-01-01::GrantUserPermission instead.
        
        @summary Grant permissions to a Resource Access Management (RAM) user.
        
        @param request: GrantUserPermissionsRequest
        @return: GrantUserPermissionsResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.grant_user_permissions_with_options_async(request, runtime)

    def update_hub_cluster_feature_with_options(
        self,
        tmp_req: adcp_20220101_models.UpdateHubClusterFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.UpdateHubClusterFeatureResponse:
        """
        @summary Updates the configurations of a Container Service for Kubernetes (ACK) cluster that serves as a master instance.
        
        @param tmp_req: UpdateHubClusterFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHubClusterFeatureResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.UpdateHubClusterFeatureShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.access_control_list):
            request.access_control_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.access_control_list, 'AccessControlList', 'json')
        if not UtilClient.is_unset(tmp_req.v_switches):
            request.v_switches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_control_list_shrink):
            query['AccessControlList'] = request.access_control_list_shrink
        if not UtilClient.is_unset(request.api_server_eip_id):
            query['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.argo_cdenabled):
            query['ArgoCDEnabled'] = request.argo_cdenabled
        if not UtilClient.is_unset(request.argo_cdhaenabled):
            query['ArgoCDHAEnabled'] = request.argo_cdhaenabled
        if not UtilClient.is_unset(request.argo_events_enabled):
            query['ArgoEventsEnabled'] = request.argo_events_enabled
        if not UtilClient.is_unset(request.argo_server_enabled):
            query['ArgoServerEnabled'] = request.argo_server_enabled
        if not UtilClient.is_unset(request.audit_log_enabled):
            query['AuditLogEnabled'] = request.audit_log_enabled
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_mesh):
            query['EnableMesh'] = request.enable_mesh
        if not UtilClient.is_unset(request.gateway_enabled):
            query['GatewayEnabled'] = request.gateway_enabled
        if not UtilClient.is_unset(request.monitor_enabled):
            query['MonitorEnabled'] = request.monitor_enabled
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.price_limit):
            query['PriceLimit'] = request.price_limit
        if not UtilClient.is_unset(request.public_access_enabled):
            query['PublicAccessEnabled'] = request.public_access_enabled
        if not UtilClient.is_unset(request.public_api_server_enabled):
            query['PublicApiServerEnabled'] = request.public_api_server_enabled
        if not UtilClient.is_unset(request.v_switches_shrink):
            query['VSwitches'] = request.v_switches_shrink
        if not UtilClient.is_unset(request.workflow_schedule_mode):
            query['WorkflowScheduleMode'] = request.workflow_schedule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHubClusterFeature',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.UpdateHubClusterFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_hub_cluster_feature_with_options_async(
        self,
        tmp_req: adcp_20220101_models.UpdateHubClusterFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.UpdateHubClusterFeatureResponse:
        """
        @summary Updates the configurations of a Container Service for Kubernetes (ACK) cluster that serves as a master instance.
        
        @param tmp_req: UpdateHubClusterFeatureRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateHubClusterFeatureResponse
        """
        UtilClient.validate_model(tmp_req)
        request = adcp_20220101_models.UpdateHubClusterFeatureShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.access_control_list):
            request.access_control_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.access_control_list, 'AccessControlList', 'json')
        if not UtilClient.is_unset(tmp_req.v_switches):
            request.v_switches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.v_switches, 'VSwitches', 'json')
        query = {}
        if not UtilClient.is_unset(request.access_control_list_shrink):
            query['AccessControlList'] = request.access_control_list_shrink
        if not UtilClient.is_unset(request.api_server_eip_id):
            query['ApiServerEipId'] = request.api_server_eip_id
        if not UtilClient.is_unset(request.argo_cdenabled):
            query['ArgoCDEnabled'] = request.argo_cdenabled
        if not UtilClient.is_unset(request.argo_cdhaenabled):
            query['ArgoCDHAEnabled'] = request.argo_cdhaenabled
        if not UtilClient.is_unset(request.argo_events_enabled):
            query['ArgoEventsEnabled'] = request.argo_events_enabled
        if not UtilClient.is_unset(request.argo_server_enabled):
            query['ArgoServerEnabled'] = request.argo_server_enabled
        if not UtilClient.is_unset(request.audit_log_enabled):
            query['AuditLogEnabled'] = request.audit_log_enabled
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.enable_mesh):
            query['EnableMesh'] = request.enable_mesh
        if not UtilClient.is_unset(request.gateway_enabled):
            query['GatewayEnabled'] = request.gateway_enabled
        if not UtilClient.is_unset(request.monitor_enabled):
            query['MonitorEnabled'] = request.monitor_enabled
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.price_limit):
            query['PriceLimit'] = request.price_limit
        if not UtilClient.is_unset(request.public_access_enabled):
            query['PublicAccessEnabled'] = request.public_access_enabled
        if not UtilClient.is_unset(request.public_api_server_enabled):
            query['PublicApiServerEnabled'] = request.public_api_server_enabled
        if not UtilClient.is_unset(request.v_switches_shrink):
            query['VSwitches'] = request.v_switches_shrink
        if not UtilClient.is_unset(request.workflow_schedule_mode):
            query['WorkflowScheduleMode'] = request.workflow_schedule_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateHubClusterFeature',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.UpdateHubClusterFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_hub_cluster_feature(
        self,
        request: adcp_20220101_models.UpdateHubClusterFeatureRequest,
    ) -> adcp_20220101_models.UpdateHubClusterFeatureResponse:
        """
        @summary Updates the configurations of a Container Service for Kubernetes (ACK) cluster that serves as a master instance.
        
        @param request: UpdateHubClusterFeatureRequest
        @return: UpdateHubClusterFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_hub_cluster_feature_with_options(request, runtime)

    async def update_hub_cluster_feature_async(
        self,
        request: adcp_20220101_models.UpdateHubClusterFeatureRequest,
    ) -> adcp_20220101_models.UpdateHubClusterFeatureResponse:
        """
        @summary Updates the configurations of a Container Service for Kubernetes (ACK) cluster that serves as a master instance.
        
        @param request: UpdateHubClusterFeatureRequest
        @return: UpdateHubClusterFeatureResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_hub_cluster_feature_with_options_async(request, runtime)

    def update_user_permission_with_options(
        self,
        request: adcp_20220101_models.UpdateUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.UpdateUserPermissionResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: UpdateUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.UpdateUserPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_permission_with_options_async(
        self,
        request: adcp_20220101_models.UpdateUserPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> adcp_20220101_models.UpdateUserPermissionResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: UpdateUserPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        if not UtilClient.is_unset(request.role_type):
            query['RoleType'] = request.role_type
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserPermission',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.UpdateUserPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_permission(
        self,
        request: adcp_20220101_models.UpdateUserPermissionRequest,
    ) -> adcp_20220101_models.UpdateUserPermissionResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: UpdateUserPermissionRequest
        @return: UpdateUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_permission_with_options(request, runtime)

    async def update_user_permission_async(
        self,
        request: adcp_20220101_models.UpdateUserPermissionRequest,
    ) -> adcp_20220101_models.UpdateUserPermissionResponse:
        """
        @summary Updates the role-based access control (RBAC) permissions of a RAM user.
        
        @param request: UpdateUserPermissionRequest
        @return: UpdateUserPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_permission_with_options_async(request, runtime)
