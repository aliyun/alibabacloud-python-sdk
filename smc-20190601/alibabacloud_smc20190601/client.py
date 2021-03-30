# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_smc20190601 import models as smc_20190601_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('smc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_replication_job_with_options(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['Name'] = request.name
        query['Description'] = request.description
        query['SourceId'] = request.source_id
        query['TargetType'] = request.target_type
        query['ScheduledStartTime'] = request.scheduled_start_time
        query['ValidTime'] = request.valid_time
        query['ImageName'] = request.image_name
        query['InstanceId'] = request.instance_id
        query['SystemDiskSize'] = request.system_disk_size
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['ReplicationParameters'] = request.replication_parameters
        query['NetMode'] = request.net_mode
        query['RunOnce'] = request.run_once
        query['Frequency'] = request.frequency
        query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        query['InstanceType'] = request.instance_type
        query['LaunchTemplateId'] = request.launch_template_id
        query['LaunchTemplateVersion'] = request.launch_template_version
        query['InstanceRamRole'] = request.instance_ram_role
        query['ContainerNamespace'] = request.container_namespace
        query['ContainerRepository'] = request.container_repository
        query['ContainerTag'] = request.container_tag
        query['LicenseType'] = request.license_type
        query['DataDisk'] = request.data_disk
        query['Tag'] = request.tag
        query['SystemDiskPart'] = request.system_disk_part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CreateReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_replication_job_with_options_async(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['RegionId'] = request.region_id
        query['ClientToken'] = request.client_token
        query['Name'] = request.name
        query['Description'] = request.description
        query['SourceId'] = request.source_id
        query['TargetType'] = request.target_type
        query['ScheduledStartTime'] = request.scheduled_start_time
        query['ValidTime'] = request.valid_time
        query['ImageName'] = request.image_name
        query['InstanceId'] = request.instance_id
        query['SystemDiskSize'] = request.system_disk_size
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['ReplicationParameters'] = request.replication_parameters
        query['NetMode'] = request.net_mode
        query['RunOnce'] = request.run_once
        query['Frequency'] = request.frequency
        query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        query['InstanceType'] = request.instance_type
        query['LaunchTemplateId'] = request.launch_template_id
        query['LaunchTemplateVersion'] = request.launch_template_version
        query['InstanceRamRole'] = request.instance_ram_role
        query['ContainerNamespace'] = request.container_namespace
        query['ContainerRepository'] = request.container_repository
        query['ContainerTag'] = request.container_tag
        query['LicenseType'] = request.license_type
        query['DataDisk'] = request.data_disk
        query['Tag'] = request.tag
        query['SystemDiskPart'] = request.system_disk_part
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CreateReplicationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_replication_job(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_replication_job_with_options(request, runtime)

    async def create_replication_job_async(
        self,
        request: smc_20190601_models.CreateReplicationJobRequest,
    ) -> smc_20190601_models.CreateReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_replication_job_with_options_async(request, runtime)

    def cut_over_replication_job_with_options(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['SyncData'] = request.sync_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CutOverReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CutOverReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def cut_over_replication_job_with_options_async(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['SyncData'] = request.sync_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CutOverReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.CutOverReplicationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cut_over_replication_job(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.cut_over_replication_job_with_options(request, runtime)

    async def cut_over_replication_job_async(
        self,
        request: smc_20190601_models.CutOverReplicationJobRequest,
    ) -> smc_20190601_models.CutOverReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cut_over_replication_job_with_options_async(request, runtime)

    def delete_replication_job_with_options(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_replication_job_with_options_async(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteReplicationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_replication_job(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_replication_job_with_options(request, runtime)

    async def delete_replication_job_async(
        self,
        request: smc_20190601_models.DeleteReplicationJobRequest,
    ) -> smc_20190601_models.DeleteReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_replication_job_with_options_async(request, runtime)

    def delete_source_server_with_options(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['SourceId'] = request.source_id
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSourceServer',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteSourceServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_server_with_options_async(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['SourceId'] = request.source_id
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSourceServer',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DeleteSourceServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source_server(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_source_server_with_options(request, runtime)

    async def delete_source_server_async(
        self,
        request: smc_20190601_models.DeleteSourceServerRequest,
    ) -> smc_20190601_models.DeleteSourceServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_source_server_with_options_async(request, runtime)

    def describe_replication_jobs_with_options(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        query['BusinessStatus'] = request.business_status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SourceId'] = request.source_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReplicationJobs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeReplicationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_replication_jobs_with_options_async(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        query['BusinessStatus'] = request.business_status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SourceId'] = request.source_id
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeReplicationJobs',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeReplicationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_replication_jobs(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_replication_jobs_with_options(request, runtime)

    async def describe_replication_jobs_async(
        self,
        request: smc_20190601_models.DescribeReplicationJobsRequest,
    ) -> smc_20190601_models.DescribeReplicationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_replication_jobs_with_options_async(request, runtime)

    def describe_source_servers_with_options(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['State'] = request.state
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSourceServers',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeSourceServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_source_servers_with_options_async(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['State'] = request.state
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SourceId'] = request.source_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSourceServers',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.DescribeSourceServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_source_servers(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_source_servers_with_options(request, runtime)

    async def describe_source_servers_async(
        self,
        request: smc_20190601_models.DescribeSourceServersRequest,
    ) -> smc_20190601_models.DescribeSourceServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_source_servers_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: smc_20190601_models.ListTagResourcesRequest,
    ) -> smc_20190601_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_replication_job_attribute_with_options(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['TargetType'] = request.target_type
        query['ScheduledStartTime'] = request.scheduled_start_time
        query['ImageName'] = request.image_name
        query['InstanceId'] = request.instance_id
        query['SystemDiskSize'] = request.system_disk_size
        query['Frequency'] = request.frequency
        query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        query['InstanceType'] = request.instance_type
        query['LaunchTemplateId'] = request.launch_template_id
        query['LaunchTemplateVersion'] = request.launch_template_version
        query['InstanceRamRole'] = request.instance_ram_role
        query['ContainerNamespace'] = request.container_namespace
        query['ContainerRepository'] = request.container_repository
        query['ContainerTag'] = request.container_tag
        query['ValidTime'] = request.valid_time
        query['SystemDiskPart'] = request.system_disk_part
        query['DataDisk'] = request.data_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReplicationJobAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifyReplicationJobAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_replication_job_attribute_with_options_async(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['TargetType'] = request.target_type
        query['ScheduledStartTime'] = request.scheduled_start_time
        query['ImageName'] = request.image_name
        query['InstanceId'] = request.instance_id
        query['SystemDiskSize'] = request.system_disk_size
        query['Frequency'] = request.frequency
        query['MaxNumberOfImageToKeep'] = request.max_number_of_image_to_keep
        query['InstanceType'] = request.instance_type
        query['LaunchTemplateId'] = request.launch_template_id
        query['LaunchTemplateVersion'] = request.launch_template_version
        query['InstanceRamRole'] = request.instance_ram_role
        query['ContainerNamespace'] = request.container_namespace
        query['ContainerRepository'] = request.container_repository
        query['ContainerTag'] = request.container_tag
        query['ValidTime'] = request.valid_time
        query['SystemDiskPart'] = request.system_disk_part
        query['DataDisk'] = request.data_disk
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyReplicationJobAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifyReplicationJobAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_replication_job_attribute(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_replication_job_attribute_with_options(request, runtime)

    async def modify_replication_job_attribute_async(
        self,
        request: smc_20190601_models.ModifyReplicationJobAttributeRequest,
    ) -> smc_20190601_models.ModifyReplicationJobAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_replication_job_attribute_with_options_async(request, runtime)

    def modify_source_server_attribute_with_options(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['SourceId'] = request.source_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySourceServerAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifySourceServerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_source_server_attribute_with_options_async(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['SourceId'] = request.source_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySourceServerAttribute',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.ModifySourceServerAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_source_server_attribute(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_source_server_attribute_with_options(request, runtime)

    async def modify_source_server_attribute_async(
        self,
        request: smc_20190601_models.ModifySourceServerAttributeRequest,
    ) -> smc_20190601_models.ModifySourceServerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_source_server_attribute_with_options_async(request, runtime)

    def start_replication_job_with_options(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StartReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_replication_job_with_options_async(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StartReplicationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_replication_job(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_replication_job_with_options(request, runtime)

    async def start_replication_job_async(
        self,
        request: smc_20190601_models.StartReplicationJobRequest,
    ) -> smc_20190601_models.StartReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_replication_job_with_options_async(request, runtime)

    def stop_replication_job_with_options(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StopReplicationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_replication_job_with_options_async(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopReplicationJob',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.StopReplicationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_replication_job(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_replication_job_with_options(request, runtime)

    async def stop_replication_job_async(
        self,
        request: smc_20190601_models.StopReplicationJobRequest,
    ) -> smc_20190601_models.StopReplicationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_replication_job_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: smc_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: smc_20190601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: smc_20190601_models.TagResourcesRequest,
    ) -> smc_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: smc_20190601_models.TagResourcesRequest,
    ) -> smc_20190601_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> smc_20190601_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            smc_20190601_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
    ) -> smc_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: smc_20190601_models.UntagResourcesRequest,
    ) -> smc_20190601_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
