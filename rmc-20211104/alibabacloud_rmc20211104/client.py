# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rmc20211104 import models as rmc20211104_models
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
        self._endpoint = self.get_endpoint('rmc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def list_resource_relationships_with_options(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        """
        This section provides the types of resources that can be queried. Two-way queries are supported. For example, you can query the disks (ACS::ECS::Disk) that are associated with a specific Elastic Compute Service (ECS) instance (ACS::ECS::Instance) or query the ECS instance that is associated with a specific disk.
        - For ECS instances, the following types of resources can be queried:    - ACS::ECS::Disk
        - ACS::EIP::EipAddress
        - ACS::VPC::VPC
        - ACS::ECS::KeyPair
        - ACS::ECS::SecurityGroup
        - ACS::ECS::NetworkInterface
        - ACS::ECS::Image
        - For virtual private clouds (VPCs), which are indicated by ACS::VPC::VPC, the following types of resources can be queried:    - ACS::ECS::Instance
        - ACS::RDS::DBInstance
        - ACS::SLB::LoadBalancer
        - ACS::ALB::LoadBalancer
        - ACS::Elasticsearch::Instance
        - ACS::Redis::DBInstance
        - ACS::PolarDB::DBCluster
        - ACS::MongoDB::DBInstance
        - ACS::DRDS::PolarDBXInstance
        - ACS::EDAS::Cluster
        - ACS::ECI::ContainerGroup
        - ACS::ADB::DBCluster
        - ACS::DRDS::DBInstance
        - ACS::HBase::Cluster
        - ACS::EMR::Cluster
        This topic provides an example on how to call the API operation to query the resources that are associated with the ECS instance `i-uf6imlgyr1nudhud****` in the China (Shanghai) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: ListResourceRelationshipsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRelationshipsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.source_resource_type):
            query['SourceResourceType'] = request.source_resource_type
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelationships',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.ListResourceRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_relationships_with_options_async(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        """
        This section provides the types of resources that can be queried. Two-way queries are supported. For example, you can query the disks (ACS::ECS::Disk) that are associated with a specific Elastic Compute Service (ECS) instance (ACS::ECS::Instance) or query the ECS instance that is associated with a specific disk.
        - For ECS instances, the following types of resources can be queried:    - ACS::ECS::Disk
        - ACS::EIP::EipAddress
        - ACS::VPC::VPC
        - ACS::ECS::KeyPair
        - ACS::ECS::SecurityGroup
        - ACS::ECS::NetworkInterface
        - ACS::ECS::Image
        - For virtual private clouds (VPCs), which are indicated by ACS::VPC::VPC, the following types of resources can be queried:    - ACS::ECS::Instance
        - ACS::RDS::DBInstance
        - ACS::SLB::LoadBalancer
        - ACS::ALB::LoadBalancer
        - ACS::Elasticsearch::Instance
        - ACS::Redis::DBInstance
        - ACS::PolarDB::DBCluster
        - ACS::MongoDB::DBInstance
        - ACS::DRDS::PolarDBXInstance
        - ACS::EDAS::Cluster
        - ACS::ECI::ContainerGroup
        - ACS::ADB::DBCluster
        - ACS::DRDS::DBInstance
        - ACS::HBase::Cluster
        - ACS::EMR::Cluster
        This topic provides an example on how to call the API operation to query the resources that are associated with the ECS instance `i-uf6imlgyr1nudhud****` in the China (Shanghai) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: ListResourceRelationshipsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceRelationshipsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.source_region_id):
            query['SourceRegionId'] = request.source_region_id
        if not UtilClient.is_unset(request.source_resource_id):
            query['SourceResourceId'] = request.source_resource_id
        if not UtilClient.is_unset(request.source_resource_type):
            query['SourceResourceType'] = request.source_resource_type
        if not UtilClient.is_unset(request.target_resource_type):
            query['TargetResourceType'] = request.target_resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceRelationships',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.ListResourceRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_relationships(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        """
        This section provides the types of resources that can be queried. Two-way queries are supported. For example, you can query the disks (ACS::ECS::Disk) that are associated with a specific Elastic Compute Service (ECS) instance (ACS::ECS::Instance) or query the ECS instance that is associated with a specific disk.
        - For ECS instances, the following types of resources can be queried:    - ACS::ECS::Disk
        - ACS::EIP::EipAddress
        - ACS::VPC::VPC
        - ACS::ECS::KeyPair
        - ACS::ECS::SecurityGroup
        - ACS::ECS::NetworkInterface
        - ACS::ECS::Image
        - For virtual private clouds (VPCs), which are indicated by ACS::VPC::VPC, the following types of resources can be queried:    - ACS::ECS::Instance
        - ACS::RDS::DBInstance
        - ACS::SLB::LoadBalancer
        - ACS::ALB::LoadBalancer
        - ACS::Elasticsearch::Instance
        - ACS::Redis::DBInstance
        - ACS::PolarDB::DBCluster
        - ACS::MongoDB::DBInstance
        - ACS::DRDS::PolarDBXInstance
        - ACS::EDAS::Cluster
        - ACS::ECI::ContainerGroup
        - ACS::ADB::DBCluster
        - ACS::DRDS::DBInstance
        - ACS::HBase::Cluster
        - ACS::EMR::Cluster
        This topic provides an example on how to call the API operation to query the resources that are associated with the ECS instance `i-uf6imlgyr1nudhud****` in the China (Shanghai) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: ListResourceRelationshipsRequest
        @return: ListResourceRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_relationships_with_options(request, runtime)

    async def list_resource_relationships_async(
        self,
        request: rmc20211104_models.ListResourceRelationshipsRequest,
    ) -> rmc20211104_models.ListResourceRelationshipsResponse:
        """
        This section provides the types of resources that can be queried. Two-way queries are supported. For example, you can query the disks (ACS::ECS::Disk) that are associated with a specific Elastic Compute Service (ECS) instance (ACS::ECS::Instance) or query the ECS instance that is associated with a specific disk.
        - For ECS instances, the following types of resources can be queried:    - ACS::ECS::Disk
        - ACS::EIP::EipAddress
        - ACS::VPC::VPC
        - ACS::ECS::KeyPair
        - ACS::ECS::SecurityGroup
        - ACS::ECS::NetworkInterface
        - ACS::ECS::Image
        - For virtual private clouds (VPCs), which are indicated by ACS::VPC::VPC, the following types of resources can be queried:    - ACS::ECS::Instance
        - ACS::RDS::DBInstance
        - ACS::SLB::LoadBalancer
        - ACS::ALB::LoadBalancer
        - ACS::Elasticsearch::Instance
        - ACS::Redis::DBInstance
        - ACS::PolarDB::DBCluster
        - ACS::MongoDB::DBInstance
        - ACS::DRDS::PolarDBXInstance
        - ACS::EDAS::Cluster
        - ACS::ECI::ContainerGroup
        - ACS::ADB::DBCluster
        - ACS::DRDS::DBInstance
        - ACS::HBase::Cluster
        - ACS::EMR::Cluster
        This topic provides an example on how to call the API operation to query the resources that are associated with the ECS instance `i-uf6imlgyr1nudhud****` in the China (Shanghai) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: ListResourceRelationshipsRequest
        @return: ListResourceRelationshipsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_relationships_with_options_async(request, runtime)

    def search_resources_with_options(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        """
        For more information about resource types that support RMC, see [Resource types that support RMC](https://www.alibabacloud.com/help/en/resource-management/latest/resource-types-that-support-rmc).
        This topic provides an example on how to call the API operation to query the resources that can be accessed within the current account in the China (Hangzhou) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SearchResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rmc20211104_models.SearchResourcesResponse:
        """
        For more information about resource types that support RMC, see [Resource types that support RMC](https://www.alibabacloud.com/help/en/resource-management/latest/resource-types-that-support-rmc).
        This topic provides an example on how to call the API operation to query the resources that can be accessed within the current account in the China (Hangzhou) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SearchResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchResources',
            version='2021-11-04',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rmc20211104_models.SearchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_resources(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        """
        For more information about resource types that support RMC, see [Resource types that support RMC](https://www.alibabacloud.com/help/en/resource-management/latest/resource-types-that-support-rmc).
        This topic provides an example on how to call the API operation to query the resources that can be accessed within the current account in the China (Hangzhou) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SearchResourcesRequest
        @return: SearchResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: rmc20211104_models.SearchResourcesRequest,
    ) -> rmc20211104_models.SearchResourcesResponse:
        """
        For more information about resource types that support RMC, see [Resource types that support RMC](https://www.alibabacloud.com/help/en/resource-management/latest/resource-types-that-support-rmc).
        This topic provides an example on how to call the API operation to query the resources that can be accessed within the current account in the China (Hangzhou) region.
        ## Prerequisites
        Resource Meta Center (RMC) is enabled. For more information, see [Query resources that belong to different resource groups](~~310198~~).
        ## QPS limits
        You can call this API operation up to 20 times per second per account. Requests that exceed this limit will fail, and you may experience service interruptions. We recommend that you take note of this limit when you call this operation.
        
        @param request: SearchResourcesRequest
        @return: SearchResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)
