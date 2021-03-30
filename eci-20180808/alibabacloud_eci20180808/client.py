# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eci20180808 import models as eci_20180808_models
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
        self._endpoint = self.get_endpoint('eci', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_container_group_with_options(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['SecurityGroupId'] = request.security_group_id
        query['VSwitchId'] = request.v_switch_id
        query['ContainerGroupName'] = request.container_group_name
        query['RestartPolicy'] = request.restart_policy
        query['EipInstanceId'] = request.eip_instance_id
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['ResourceGroupId'] = request.resource_group_id
        query['DnsPolicy'] = request.dns_policy
        query['ClientToken'] = request.client_token
        query['InstanceType'] = request.instance_type
        query['SlsEnable'] = request.sls_enable
        query['ImageSnapshotId'] = request.image_snapshot_id
        query['RamRoleName'] = request.ram_role_name
        query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        query['AutoMatchImageCache'] = request.auto_match_image_cache
        query['Ipv6AddressCount'] = request.ipv_6address_count
        query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        query['SpotStrategy'] = request.spot_strategy
        query['SpotPriceLimit'] = request.spot_price_limit
        query['ScheduleStrategy'] = request.schedule_strategy
        query['TenantVSwitchId'] = request.tenant_vswitch_id
        query['TenantSecurityGroupId'] = request.tenant_security_group_id
        query['CorePattern'] = request.core_pattern
        query['ShareProcessNamespace'] = request.share_process_namespace
        query['ProductOnEciMode'] = request.product_on_eci_mode
        query['SecondaryENIPolicy'] = request.secondary_enipolicy
        query['AutoCreateEip'] = request.auto_create_eip
        query['EipBandwidth'] = request.eip_bandwidth
        query['EipISP'] = request.eip_isp
        query['EipCommonBandwidthPackage'] = request.eip_common_bandwidth_package
        query['HostName'] = request.host_name
        query['IngressBandwidth'] = request.ingress_bandwidth
        query['EgressBandwidth'] = request.egress_bandwidth
        query['CpuOptionsCore'] = request.cpu_options_core
        query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        query['CpuOptionsNuma'] = request.cpu_options_numa
        query['EphemeralStorage'] = request.ephemeral_storage
        query['Tag'] = request.tag
        query['ImageRegistryCredential'] = request.image_registry_credential
        query['Container'] = request.container
        query['Volume'] = request.volume
        query['InitContainer'] = request.init_container
        query['HostAliase'] = request.host_aliase
        query['Arn'] = request.arn
        query['NtpServer'] = request.ntp_server
        query['AcrRegistryInfo'] = request.acr_registry_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_container_group_with_options_async(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['SecurityGroupId'] = request.security_group_id
        query['VSwitchId'] = request.v_switch_id
        query['ContainerGroupName'] = request.container_group_name
        query['RestartPolicy'] = request.restart_policy
        query['EipInstanceId'] = request.eip_instance_id
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['ResourceGroupId'] = request.resource_group_id
        query['DnsPolicy'] = request.dns_policy
        query['ClientToken'] = request.client_token
        query['InstanceType'] = request.instance_type
        query['SlsEnable'] = request.sls_enable
        query['ImageSnapshotId'] = request.image_snapshot_id
        query['RamRoleName'] = request.ram_role_name
        query['TerminationGracePeriodSeconds'] = request.termination_grace_period_seconds
        query['AutoMatchImageCache'] = request.auto_match_image_cache
        query['Ipv6AddressCount'] = request.ipv_6address_count
        query['ActiveDeadlineSeconds'] = request.active_deadline_seconds
        query['SpotStrategy'] = request.spot_strategy
        query['SpotPriceLimit'] = request.spot_price_limit
        query['ScheduleStrategy'] = request.schedule_strategy
        query['TenantVSwitchId'] = request.tenant_vswitch_id
        query['TenantSecurityGroupId'] = request.tenant_security_group_id
        query['CorePattern'] = request.core_pattern
        query['ShareProcessNamespace'] = request.share_process_namespace
        query['ProductOnEciMode'] = request.product_on_eci_mode
        query['SecondaryENIPolicy'] = request.secondary_enipolicy
        query['AutoCreateEip'] = request.auto_create_eip
        query['EipBandwidth'] = request.eip_bandwidth
        query['EipISP'] = request.eip_isp
        query['EipCommonBandwidthPackage'] = request.eip_common_bandwidth_package
        query['HostName'] = request.host_name
        query['IngressBandwidth'] = request.ingress_bandwidth
        query['EgressBandwidth'] = request.egress_bandwidth
        query['CpuOptionsCore'] = request.cpu_options_core
        query['CpuOptionsThreadsPerCore'] = request.cpu_options_threads_per_core
        query['CpuOptionsNuma'] = request.cpu_options_numa
        query['EphemeralStorage'] = request.ephemeral_storage
        query['Tag'] = request.tag
        query['ImageRegistryCredential'] = request.image_registry_credential
        query['Container'] = request.container
        query['Volume'] = request.volume
        query['InitContainer'] = request.init_container
        query['HostAliase'] = request.host_aliase
        query['Arn'] = request.arn
        query['NtpServer'] = request.ntp_server
        query['AcrRegistryInfo'] = request.acr_registry_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateContainerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_container_group(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_container_group_with_options(request, runtime)

    async def create_container_group_async(
        self,
        request: eci_20180808_models.CreateContainerGroupRequest,
    ) -> eci_20180808_models.CreateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_container_group_with_options_async(request, runtime)

    def create_image_cache_with_options(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['SecurityGroupId'] = request.security_group_id
        query['VSwitchId'] = request.v_switch_id
        query['ImageCacheName'] = request.image_cache_name
        query['EipInstanceId'] = request.eip_instance_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ClientToken'] = request.client_token
        query['ImageCacheSize'] = request.image_cache_size
        query['RetentionDays'] = request.retention_days
        query['AutoMatchImageCache'] = request.auto_match_image_cache
        query['ImageRegistryCredential'] = request.image_registry_credential
        query['Image'] = request.image
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_image_cache_with_options_async(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['SecurityGroupId'] = request.security_group_id
        query['VSwitchId'] = request.v_switch_id
        query['ImageCacheName'] = request.image_cache_name
        query['EipInstanceId'] = request.eip_instance_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ClientToken'] = request.client_token
        query['ImageCacheSize'] = request.image_cache_size
        query['RetentionDays'] = request.retention_days
        query['AutoMatchImageCache'] = request.auto_match_image_cache
        query['ImageRegistryCredential'] = request.image_registry_credential
        query['Image'] = request.image
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.CreateImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_image_cache(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_cache_with_options(request, runtime)

    async def create_image_cache_async(
        self,
        request: eci_20180808_models.CreateImageCacheRequest,
    ) -> eci_20180808_models.CreateImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_cache_with_options_async(request, runtime)

    def delete_container_group_with_options(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_container_group_with_options_async(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteContainerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_container_group(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_container_group_with_options(request, runtime)

    async def delete_container_group_async(
        self,
        request: eci_20180808_models.DeleteContainerGroupRequest,
    ) -> eci_20180808_models.DeleteContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_container_group_with_options_async(request, runtime)

    def delete_image_cache_with_options(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ImageCacheId'] = request.image_cache_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteImageCacheResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_image_cache_with_options_async(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ImageCacheId'] = request.image_cache_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteImageCache',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DeleteImageCacheResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_image_cache(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_cache_with_options(request, runtime)

    async def delete_image_cache_async(
        self,
        request: eci_20180808_models.DeleteImageCacheRequest,
    ) -> eci_20180808_models.DeleteImageCacheResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_cache_with_options_async(request, runtime)

    def describe_container_group_metric_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Period'] = request.period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_group_metric_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['Period'] = request.period
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_group_metric(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_metric_with_options(request, runtime)

    async def describe_container_group_metric_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_group_metric_with_options_async(request, runtime)

    def describe_container_group_price_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['InstanceType'] = request.instance_type
        query['SpotStrategy'] = request.spot_strategy
        query['ZoneId'] = request.zone_id
        query['SpotPriceLimit'] = request.spot_price_limit
        query['EphemeralStorage'] = request.ephemeral_storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupPrice',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_group_price_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['InstanceType'] = request.instance_type
        query['SpotStrategy'] = request.spot_strategy
        query['ZoneId'] = request.zone_id
        query['SpotPriceLimit'] = request.spot_price_limit
        query['EphemeralStorage'] = request.ephemeral_storage
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroupPrice',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_group_price(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_group_price_with_options(request, runtime)

    async def describe_container_group_price_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupPriceRequest,
    ) -> eci_20180808_models.DescribeContainerGroupPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_group_price_with_options_async(request, runtime)

    def describe_container_groups_with_options(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['VSwitchId'] = request.v_switch_id
        query['NextToken'] = request.next_token
        query['Limit'] = request.limit
        query['ContainerGroupIds'] = request.container_group_ids
        query['ContainerGroupName'] = request.container_group_name
        query['Status'] = request.status
        query['ResourceGroupId'] = request.resource_group_id
        query['WithEvent'] = request.with_event
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroups',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_groups_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['VSwitchId'] = request.v_switch_id
        query['NextToken'] = request.next_token
        query['Limit'] = request.limit
        query['ContainerGroupIds'] = request.container_group_ids
        query['ContainerGroupName'] = request.container_group_name
        query['Status'] = request.status
        query['ResourceGroupId'] = request.resource_group_id
        query['WithEvent'] = request.with_event
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerGroups',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_groups(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_groups_with_options(request, runtime)

    async def describe_container_groups_async(
        self,
        request: eci_20180808_models.DescribeContainerGroupsRequest,
    ) -> eci_20180808_models.DescribeContainerGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_groups_with_options_async(request, runtime)

    def describe_container_log_with_options(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ContainerName'] = request.container_name
        query['StartTime'] = request.start_time
        query['Tail'] = request.tail
        query['LastTime'] = request.last_time
        query['SinceSeconds'] = request.since_seconds
        query['LimitBytes'] = request.limit_bytes
        query['Timestamps'] = request.timestamps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerLog',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_container_log_with_options_async(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ContainerName'] = request.container_name
        query['StartTime'] = request.start_time
        query['Tail'] = request.tail
        query['LastTime'] = request.last_time
        query['SinceSeconds'] = request.since_seconds
        query['LimitBytes'] = request.limit_bytes
        query['Timestamps'] = request.timestamps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeContainerLog',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeContainerLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_container_log(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_container_log_with_options(request, runtime)

    async def describe_container_log_async(
        self,
        request: eci_20180808_models.DescribeContainerLogRequest,
    ) -> eci_20180808_models.DescribeContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_container_log_with_options_async(request, runtime)

    def describe_image_caches_with_options(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ImageCacheId'] = request.image_cache_id
        query['ImageCacheName'] = request.image_cache_name
        query['SnapshotId'] = request.snapshot_id
        query['Image'] = request.image
        query['ResourceGroupId'] = request.resource_group_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeImageCaches',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeImageCachesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_image_caches_with_options_async(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ImageCacheId'] = request.image_cache_id
        query['ImageCacheName'] = request.image_cache_name
        query['SnapshotId'] = request.snapshot_id
        query['Image'] = request.image
        query['ResourceGroupId'] = request.resource_group_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeImageCaches',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeImageCachesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_image_caches(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_caches_with_options(request, runtime)

    async def describe_image_caches_async(
        self,
        request: eci_20180808_models.DescribeImageCachesRequest,
    ) -> eci_20180808_models.DescribeImageCachesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_caches_with_options_async(request, runtime)

    def describe_multi_container_group_metric_with_options(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupIds'] = request.container_group_ids
        query['ResourceGroupId'] = request.resource_group_id
        query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMultiContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeMultiContainerGroupMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_multi_container_group_metric_with_options_async(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupIds'] = request.container_group_ids
        query['ResourceGroupId'] = request.resource_group_id
        query['MetricType'] = request.metric_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMultiContainerGroupMetric',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeMultiContainerGroupMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_multi_container_group_metric(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_multi_container_group_metric_with_options(request, runtime)

    async def describe_multi_container_group_metric_async(
        self,
        request: eci_20180808_models.DescribeMultiContainerGroupMetricRequest,
    ) -> eci_20180808_models.DescribeMultiContainerGroupMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_multi_container_group_metric_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: eci_20180808_models.DescribeRegionsRequest,
    ) -> eci_20180808_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def exec_container_command_with_options(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ContainerName'] = request.container_name
        query['Command'] = request.command
        query['TTY'] = request.tty
        query['Stdin'] = request.stdin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecContainerCommand',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ExecContainerCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def exec_container_command_with_options_async(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ContainerName'] = request.container_name
        query['Command'] = request.command
        query['TTY'] = request.tty
        query['Stdin'] = request.stdin
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExecContainerCommand',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ExecContainerCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def exec_container_command(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.exec_container_command_with_options(request, runtime)

    async def exec_container_command_async(
        self,
        request: eci_20180808_models.ExecContainerCommandRequest,
    ) -> eci_20180808_models.ExecContainerCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.exec_container_command_with_options_async(request, runtime)

    def list_usage_with_options(
        self,
        request: eci_20180808_models.ListUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ListUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsage',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ListUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_usage_with_options_async(
        self,
        request: eci_20180808_models.ListUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.ListUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsage',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.ListUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_usage(
        self,
        request: eci_20180808_models.ListUsageRequest,
    ) -> eci_20180808_models.ListUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_usage_with_options(request, runtime)

    async def list_usage_async(
        self,
        request: eci_20180808_models.ListUsageRequest,
    ) -> eci_20180808_models.ListUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_usage_with_options_async(request, runtime)

    def restart_container_group_with_options(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.RestartContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_container_group_with_options_async(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['ClientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.RestartContainerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_container_group(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_container_group_with_options(request, runtime)

    async def restart_container_group_async(
        self,
        request: eci_20180808_models.RestartContainerGroupRequest,
    ) -> eci_20180808_models.RestartContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_container_group_with_options_async(request, runtime)

    def update_container_group_with_options(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['RestartPolicy'] = request.restart_policy
        query['ClientToken'] = request.client_token
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['ResourceGroupId'] = request.resource_group_id
        query['Tag'] = request.tag
        query['Volume'] = request.volume
        query['Container'] = request.container
        query['InitContainer'] = request.init_container
        query['ImageRegistryCredential'] = request.image_registry_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateContainerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_container_group_with_options_async(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['OwnerId'] = request.owner_id
        query['ResourceOwnerAccount'] = request.resource_owner_account
        query['ResourceOwnerId'] = request.resource_owner_id
        query['OwnerAccount'] = request.owner_account
        query['RegionId'] = request.region_id
        query['RegionId'] = request.region_id
        query['ContainerGroupId'] = request.container_group_id
        query['RestartPolicy'] = request.restart_policy
        query['ClientToken'] = request.client_token
        query['Cpu'] = request.cpu
        query['Memory'] = request.memory
        query['ResourceGroupId'] = request.resource_group_id
        query['Tag'] = request.tag
        query['Volume'] = request.volume
        query['Container'] = request.container
        query['InitContainer'] = request.init_container
        query['ImageRegistryCredential'] = request.image_registry_credential
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateContainerGroup',
            version='2018-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            eci_20180808_models.UpdateContainerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_container_group(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_container_group_with_options(request, runtime)

    async def update_container_group_async(
        self,
        request: eci_20180808_models.UpdateContainerGroupRequest,
    ) -> eci_20180808_models.UpdateContainerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_container_group_with_options_async(request, runtime)
