# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ecs20140526 import models as ecs_20140526_models
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
            'cn-qingdao': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'ecs-cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-west-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'us-east-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'ecs.aliyuncs.com',
            'ap-northeast-2-pop': 'ecs.ap-northeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'ecs.aliyuncs.com',
            'cn-beijing-finance-pop': 'ecs.aliyuncs.com',
            'cn-beijing-gov-1': 'ecs.aliyuncs.com',
            'cn-beijing-nu16-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-edge-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'cn-fujian': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-haidian-cm12-c01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-finance': 'ecs.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hangzhou-test-306': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-hongkong-finance-pop': 'ecs.aliyuncs.com',
            'cn-shanghai-et15-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-et2-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shanghai-inner': 'ecs.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-inner': 'ecs.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-wuhan': 'ecs.aliyuncs.com',
            'cn-yushanfang': 'ecs.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'ecs-cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'ecs.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'ecs.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'ecs.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'ecs.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ecs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def accept_inquired_system_event_with_options(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AcceptInquiredSystemEventResponse().from_map(
            self.do_rpcrequest('AcceptInquiredSystemEvent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def accept_inquired_system_event_with_options_async(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AcceptInquiredSystemEventResponse().from_map(
            await self.do_rpcrequest_async('AcceptInquiredSystemEvent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_inquired_system_event(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.accept_inquired_system_event_with_options(request, runtime)

    async def accept_inquired_system_event_async(
        self,
        request: ecs_20140526_models.AcceptInquiredSystemEventRequest,
    ) -> ecs_20140526_models.AcceptInquiredSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.accept_inquired_system_event_with_options_async(request, runtime)

    def activate_router_interface_with_options(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ActivateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('ActivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ActivateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ActivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_router_interface(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_router_interface_with_options(request, runtime)

    async def activate_router_interface_async(
        self,
        request: ecs_20140526_models.ActivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_router_interface_with_options_async(request, runtime)

    def add_bandwidth_package_ips_with_options(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddBandwidthPackageIpsResponse().from_map(
            self.do_rpcrequest('AddBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_bandwidth_package_ips_with_options_async(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddBandwidthPackageIpsResponse().from_map(
            await self.do_rpcrequest_async('AddBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bandwidth_package_ips(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    async def add_bandwidth_package_ips_async(
        self,
        request: ecs_20140526_models.AddBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.AddBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_bandwidth_package_ips_with_options_async(request, runtime)

    def add_tags_with_options(
        self,
        request: ecs_20140526_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddTagsResponse().from_map(
            self.do_rpcrequest('AddTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: ecs_20140526_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AddTagsResponse().from_map(
            await self.do_rpcrequest_async('AddTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(
        self,
        request: ecs_20140526_models.AddTagsRequest,
    ) -> ecs_20140526_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: ecs_20140526_models.AddTagsRequest,
    ) -> ecs_20140526_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def allocate_dedicated_hosts_with_options(
        self,
        request: ecs_20140526_models.AllocateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocateDedicatedHostsResponse().from_map(
            self.do_rpcrequest('AllocateDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_dedicated_hosts_with_options_async(
        self,
        request: ecs_20140526_models.AllocateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocateDedicatedHostsResponse().from_map(
            await self.do_rpcrequest_async('AllocateDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_dedicated_hosts(
        self,
        request: ecs_20140526_models.AllocateDedicatedHostsRequest,
    ) -> ecs_20140526_models.AllocateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_dedicated_hosts_with_options(request, runtime)

    async def allocate_dedicated_hosts_async(
        self,
        request: ecs_20140526_models.AllocateDedicatedHostsRequest,
    ) -> ecs_20140526_models.AllocateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_dedicated_hosts_with_options_async(request, runtime)

    def allocate_eip_address_with_options(
        self,
        request: ecs_20140526_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocateEipAddressResponse().from_map(
            self.do_rpcrequest('AllocateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_address(
        self,
        request: ecs_20140526_models.AllocateEipAddressRequest,
    ) -> ecs_20140526_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    async def allocate_eip_address_async(
        self,
        request: ecs_20140526_models.AllocateEipAddressRequest,
    ) -> ecs_20140526_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_eip_address_with_options_async(request, runtime)

    def allocate_public_ip_address_with_options(
        self,
        request: ecs_20140526_models.AllocatePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocatePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocatePublicIpAddressResponse().from_map(
            self.do_rpcrequest('AllocatePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_public_ip_address_with_options_async(
        self,
        request: ecs_20140526_models.AllocatePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AllocatePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AllocatePublicIpAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocatePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_public_ip_address(
        self,
        request: ecs_20140526_models.AllocatePublicIpAddressRequest,
    ) -> ecs_20140526_models.AllocatePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_public_ip_address_with_options(request, runtime)

    async def allocate_public_ip_address_async(
        self,
        request: ecs_20140526_models.AllocatePublicIpAddressRequest,
    ) -> ecs_20140526_models.AllocatePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_public_ip_address_with_options_async(request, runtime)

    def apply_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ApplyAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('ApplyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.ApplyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ApplyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ApplyAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('ApplyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.ApplyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    async def apply_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.ApplyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ApplyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_auto_snapshot_policy_with_options_async(request, runtime)

    def assign_ipv_6addresses_with_options(
        self,
        request: ecs_20140526_models.AssignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssignIpv6AddressesResponse().from_map(
            self.do_rpcrequest('AssignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_ipv_6addresses_with_options_async(
        self,
        request: ecs_20140526_models.AssignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssignIpv6AddressesResponse().from_map(
            await self.do_rpcrequest_async('AssignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_ipv_6addresses(
        self,
        request: ecs_20140526_models.AssignIpv6AddressesRequest,
    ) -> ecs_20140526_models.AssignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_ipv_6addresses_with_options(request, runtime)

    async def assign_ipv_6addresses_async(
        self,
        request: ecs_20140526_models.AssignIpv6AddressesRequest,
    ) -> ecs_20140526_models.AssignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_ipv_6addresses_with_options_async(request, runtime)

    def assign_private_ip_addresses_with_options(
        self,
        request: ecs_20140526_models.AssignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssignPrivateIpAddressesResponse().from_map(
            self.do_rpcrequest('AssignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_private_ip_addresses_with_options_async(
        self,
        request: ecs_20140526_models.AssignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssignPrivateIpAddressesResponse().from_map(
            await self.do_rpcrequest_async('AssignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def assign_private_ip_addresses(
        self,
        request: ecs_20140526_models.AssignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.AssignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.assign_private_ip_addresses_with_options(request, runtime)

    async def assign_private_ip_addresses_async(
        self,
        request: ecs_20140526_models.AssignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.AssignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_private_ip_addresses_with_options_async(request, runtime)

    def associate_eip_address_with_options(
        self,
        request: ecs_20140526_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssociateEipAddressResponse().from_map(
            self.do_rpcrequest('AssociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AssociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_eip_address(
        self,
        request: ecs_20140526_models.AssociateEipAddressRequest,
    ) -> ecs_20140526_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    async def associate_eip_address_async(
        self,
        request: ecs_20140526_models.AssociateEipAddressRequest,
    ) -> ecs_20140526_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_eip_address_with_options_async(request, runtime)

    def associate_ha_vip_with_options(
        self,
        request: ecs_20140526_models.AssociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssociateHaVipResponse().from_map(
            self.do_rpcrequest('AssociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_ha_vip_with_options_async(
        self,
        request: ecs_20140526_models.AssociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AssociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AssociateHaVipResponse().from_map(
            await self.do_rpcrequest_async('AssociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_ha_vip(
        self,
        request: ecs_20140526_models.AssociateHaVipRequest,
    ) -> ecs_20140526_models.AssociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_ha_vip_with_options(request, runtime)

    async def associate_ha_vip_async(
        self,
        request: ecs_20140526_models.AssociateHaVipRequest,
    ) -> ecs_20140526_models.AssociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_ha_vip_with_options_async(request, runtime)

    def attach_classic_link_vpc_with_options(
        self,
        request: ecs_20140526_models.AttachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachClassicLinkVpcResponse().from_map(
            self.do_rpcrequest('AttachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_classic_link_vpc_with_options_async(
        self,
        request: ecs_20140526_models.AttachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachClassicLinkVpcResponse().from_map(
            await self.do_rpcrequest_async('AttachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_classic_link_vpc(
        self,
        request: ecs_20140526_models.AttachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.AttachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_classic_link_vpc_with_options(request, runtime)

    async def attach_classic_link_vpc_async(
        self,
        request: ecs_20140526_models.AttachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.AttachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_classic_link_vpc_with_options_async(request, runtime)

    def attach_disk_with_options(
        self,
        request: ecs_20140526_models.AttachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachDiskResponse().from_map(
            self.do_rpcrequest('AttachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_disk_with_options_async(
        self,
        request: ecs_20140526_models.AttachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachDiskResponse().from_map(
            await self.do_rpcrequest_async('AttachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_disk(
        self,
        request: ecs_20140526_models.AttachDiskRequest,
    ) -> ecs_20140526_models.AttachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_disk_with_options(request, runtime)

    async def attach_disk_async(
        self,
        request: ecs_20140526_models.AttachDiskRequest,
    ) -> ecs_20140526_models.AttachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_disk_with_options_async(request, runtime)

    def attach_instance_ram_role_with_options(
        self,
        request: ecs_20140526_models.AttachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachInstanceRamRoleResponse().from_map(
            self.do_rpcrequest('AttachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_instance_ram_role_with_options_async(
        self,
        request: ecs_20140526_models.AttachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachInstanceRamRoleResponse().from_map(
            await self.do_rpcrequest_async('AttachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_instance_ram_role(
        self,
        request: ecs_20140526_models.AttachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.AttachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_instance_ram_role_with_options(request, runtime)

    async def attach_instance_ram_role_async(
        self,
        request: ecs_20140526_models.AttachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.AttachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_instance_ram_role_with_options_async(request, runtime)

    def attach_key_pair_with_options(
        self,
        request: ecs_20140526_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachKeyPairResponse().from_map(
            self.do_rpcrequest('AttachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.AttachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachKeyPairResponse().from_map(
            await self.do_rpcrequest_async('AttachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_key_pair(
        self,
        request: ecs_20140526_models.AttachKeyPairRequest,
    ) -> ecs_20140526_models.AttachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_key_pair_with_options(request, runtime)

    async def attach_key_pair_async(
        self,
        request: ecs_20140526_models.AttachKeyPairRequest,
    ) -> ecs_20140526_models.AttachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_key_pair_with_options_async(request, runtime)

    def attach_network_interface_with_options(
        self,
        request: ecs_20140526_models.AttachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('AttachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_network_interface_with_options_async(
        self,
        request: ecs_20140526_models.AttachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AttachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AttachNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('AttachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_network_interface(
        self,
        request: ecs_20140526_models.AttachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.AttachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_network_interface_with_options(request, runtime)

    async def attach_network_interface_async(
        self,
        request: ecs_20140526_models.AttachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.AttachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_network_interface_with_options_async(request, runtime)

    def authorize_security_group_with_options(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AuthorizeSecurityGroupResponse().from_map(
            self.do_rpcrequest('AuthorizeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def authorize_security_group_with_options_async(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AuthorizeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('AuthorizeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupRequest,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    async def authorize_security_group_async(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupRequest,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_with_options_async(request, runtime)

    def authorize_security_group_egress_with_options(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AuthorizeSecurityGroupEgressResponse().from_map(
            self.do_rpcrequest('AuthorizeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def authorize_security_group_egress_with_options_async(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.AuthorizeSecurityGroupEgressResponse().from_map(
            await self.do_rpcrequest_async('AuthorizeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group_egress(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    async def authorize_security_group_egress_async(
        self,
        request: ecs_20140526_models.AuthorizeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.AuthorizeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_egress_with_options_async(request, runtime)

    def cancel_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('CancelAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.CancelAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('CancelAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.CancelAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    async def cancel_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.CancelAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.CancelAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_auto_snapshot_policy_with_options_async(request, runtime)

    def cancel_copy_image_with_options(
        self,
        request: ecs_20140526_models.CancelCopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelCopyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelCopyImageResponse().from_map(
            self.do_rpcrequest('CancelCopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_copy_image_with_options_async(
        self,
        request: ecs_20140526_models.CancelCopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelCopyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelCopyImageResponse().from_map(
            await self.do_rpcrequest_async('CancelCopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_copy_image(
        self,
        request: ecs_20140526_models.CancelCopyImageRequest,
    ) -> ecs_20140526_models.CancelCopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_copy_image_with_options(request, runtime)

    async def cancel_copy_image_async(
        self,
        request: ecs_20140526_models.CancelCopyImageRequest,
    ) -> ecs_20140526_models.CancelCopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_copy_image_with_options_async(request, runtime)

    def cancel_image_pipeline_execution_with_options(
        self,
        request: ecs_20140526_models.CancelImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelImagePipelineExecutionResponse().from_map(
            self.do_rpcrequest('CancelImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_image_pipeline_execution_with_options_async(
        self,
        request: ecs_20140526_models.CancelImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelImagePipelineExecutionResponse().from_map(
            await self.do_rpcrequest_async('CancelImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_image_pipeline_execution(
        self,
        request: ecs_20140526_models.CancelImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.CancelImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_image_pipeline_execution_with_options(request, runtime)

    async def cancel_image_pipeline_execution_async(
        self,
        request: ecs_20140526_models.CancelImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.CancelImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_image_pipeline_execution_with_options_async(request, runtime)

    def cancel_physical_connection_with_options(
        self,
        request: ecs_20140526_models.CancelPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('CancelPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.CancelPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('CancelPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_physical_connection(
        self,
        request: ecs_20140526_models.CancelPhysicalConnectionRequest,
    ) -> ecs_20140526_models.CancelPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_physical_connection_with_options(request, runtime)

    async def cancel_physical_connection_async(
        self,
        request: ecs_20140526_models.CancelPhysicalConnectionRequest,
    ) -> ecs_20140526_models.CancelPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_physical_connection_with_options_async(request, runtime)

    def cancel_simulated_system_events_with_options(
        self,
        request: ecs_20140526_models.CancelSimulatedSystemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelSimulatedSystemEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelSimulatedSystemEventsResponse().from_map(
            self.do_rpcrequest('CancelSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_simulated_system_events_with_options_async(
        self,
        request: ecs_20140526_models.CancelSimulatedSystemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelSimulatedSystemEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelSimulatedSystemEventsResponse().from_map(
            await self.do_rpcrequest_async('CancelSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_simulated_system_events(
        self,
        request: ecs_20140526_models.CancelSimulatedSystemEventsRequest,
    ) -> ecs_20140526_models.CancelSimulatedSystemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_simulated_system_events_with_options(request, runtime)

    async def cancel_simulated_system_events_async(
        self,
        request: ecs_20140526_models.CancelSimulatedSystemEventsRequest,
    ) -> ecs_20140526_models.CancelSimulatedSystemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_simulated_system_events_with_options_async(request, runtime)

    def cancel_task_with_options(
        self,
        request: ecs_20140526_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelTaskResponse().from_map(
            self.do_rpcrequest('CancelTask', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        request: ecs_20140526_models.CancelTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CancelTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CancelTaskResponse().from_map(
            await self.do_rpcrequest_async('CancelTask', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_task(
        self,
        request: ecs_20140526_models.CancelTaskRequest,
    ) -> ecs_20140526_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_task_with_options(request, runtime)

    async def cancel_task_async(
        self,
        request: ecs_20140526_models.CancelTaskRequest,
    ) -> ecs_20140526_models.CancelTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_task_with_options_async(request, runtime)

    def connect_router_interface_with_options(
        self,
        request: ecs_20140526_models.ConnectRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ConnectRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ConnectRouterInterfaceResponse().from_map(
            self.do_rpcrequest('ConnectRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def connect_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.ConnectRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ConnectRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ConnectRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ConnectRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def connect_router_interface(
        self,
        request: ecs_20140526_models.ConnectRouterInterfaceRequest,
    ) -> ecs_20140526_models.ConnectRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.connect_router_interface_with_options(request, runtime)

    async def connect_router_interface_async(
        self,
        request: ecs_20140526_models.ConnectRouterInterfaceRequest,
    ) -> ecs_20140526_models.ConnectRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.connect_router_interface_with_options_async(request, runtime)

    def convert_nat_public_ip_to_eip_with_options(
        self,
        request: ecs_20140526_models.ConvertNatPublicIpToEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ConvertNatPublicIpToEipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ConvertNatPublicIpToEipResponse().from_map(
            self.do_rpcrequest('ConvertNatPublicIpToEip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_nat_public_ip_to_eip_with_options_async(
        self,
        request: ecs_20140526_models.ConvertNatPublicIpToEipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ConvertNatPublicIpToEipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ConvertNatPublicIpToEipResponse().from_map(
            await self.do_rpcrequest_async('ConvertNatPublicIpToEip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_nat_public_ip_to_eip(
        self,
        request: ecs_20140526_models.ConvertNatPublicIpToEipRequest,
    ) -> ecs_20140526_models.ConvertNatPublicIpToEipResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_nat_public_ip_to_eip_with_options(request, runtime)

    async def convert_nat_public_ip_to_eip_async(
        self,
        request: ecs_20140526_models.ConvertNatPublicIpToEipRequest,
    ) -> ecs_20140526_models.ConvertNatPublicIpToEipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_nat_public_ip_to_eip_with_options_async(request, runtime)

    def copy_image_with_options(
        self,
        request: ecs_20140526_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CopyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CopyImageResponse().from_map(
            self.do_rpcrequest('CopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_image_with_options_async(
        self,
        request: ecs_20140526_models.CopyImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CopyImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CopyImageResponse().from_map(
            await self.do_rpcrequest_async('CopyImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_image(
        self,
        request: ecs_20140526_models.CopyImageRequest,
    ) -> ecs_20140526_models.CopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_image_with_options(request, runtime)

    async def copy_image_async(
        self,
        request: ecs_20140526_models.CopyImageRequest,
    ) -> ecs_20140526_models.CopyImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_image_with_options_async(request, runtime)

    def copy_snapshot_with_options(
        self,
        request: ecs_20140526_models.CopySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CopySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CopySnapshotResponse().from_map(
            self.do_rpcrequest('CopySnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.CopySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CopySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CopySnapshotResponse().from_map(
            await self.do_rpcrequest_async('CopySnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_snapshot(
        self,
        request: ecs_20140526_models.CopySnapshotRequest,
    ) -> ecs_20140526_models.CopySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_snapshot_with_options(request, runtime)

    async def copy_snapshot_async(
        self,
        request: ecs_20140526_models.CopySnapshotRequest,
    ) -> ecs_20140526_models.CopySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_snapshot_with_options_async(request, runtime)

    def create_activation_with_options(
        self,
        request: ecs_20140526_models.CreateActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateActivationResponse().from_map(
            self.do_rpcrequest('CreateActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_activation_with_options_async(
        self,
        request: ecs_20140526_models.CreateActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateActivationResponse().from_map(
            await self.do_rpcrequest_async('CreateActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_activation(
        self,
        request: ecs_20140526_models.CreateActivationRequest,
    ) -> ecs_20140526_models.CreateActivationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_activation_with_options(request, runtime)

    async def create_activation_async(
        self,
        request: ecs_20140526_models.CreateActivationRequest,
    ) -> ecs_20140526_models.CreateActivationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_activation_with_options_async(request, runtime)

    def create_auto_provisioning_group_with_options(
        self,
        request: ecs_20140526_models.CreateAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateAutoProvisioningGroupResponse().from_map(
            self.do_rpcrequest('CreateAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_auto_provisioning_group_with_options_async(
        self,
        request: ecs_20140526_models.CreateAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateAutoProvisioningGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_provisioning_group(
        self,
        request: ecs_20140526_models.CreateAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.CreateAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_provisioning_group_with_options(request, runtime)

    async def create_auto_provisioning_group_async(
        self,
        request: ecs_20140526_models.CreateAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.CreateAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_provisioning_group_with_options_async(request, runtime)

    def create_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('CreateAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.CreateAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('CreateAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.CreateAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    async def create_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.CreateAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.CreateAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_snapshot_policy_with_options_async(request, runtime)

    def create_capacity_reservation_with_options(
        self,
        request: ecs_20140526_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateCapacityReservationResponse().from_map(
            self.do_rpcrequest('CreateCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_capacity_reservation_with_options_async(
        self,
        request: ecs_20140526_models.CreateCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateCapacityReservationResponse().from_map(
            await self.do_rpcrequest_async('CreateCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_capacity_reservation(
        self,
        request: ecs_20140526_models.CreateCapacityReservationRequest,
    ) -> ecs_20140526_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_capacity_reservation_with_options(request, runtime)

    async def create_capacity_reservation_async(
        self,
        request: ecs_20140526_models.CreateCapacityReservationRequest,
    ) -> ecs_20140526_models.CreateCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_capacity_reservation_with_options_async(request, runtime)

    def create_command_with_options(
        self,
        request: ecs_20140526_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateCommandResponse().from_map(
            self.do_rpcrequest('CreateCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_command_with_options_async(
        self,
        request: ecs_20140526_models.CreateCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateCommandResponse().from_map(
            await self.do_rpcrequest_async('CreateCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_command(
        self,
        request: ecs_20140526_models.CreateCommandRequest,
    ) -> ecs_20140526_models.CreateCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_command_with_options(request, runtime)

    async def create_command_async(
        self,
        request: ecs_20140526_models.CreateCommandRequest,
    ) -> ecs_20140526_models.CreateCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_command_with_options_async(request, runtime)

    def create_dedicated_host_cluster_with_options(
        self,
        request: ecs_20140526_models.CreateDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDedicatedHostClusterResponse().from_map(
            self.do_rpcrequest('CreateDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_cluster_with_options_async(
        self,
        request: ecs_20140526_models.CreateDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDedicatedHostClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_cluster(
        self,
        request: ecs_20140526_models.CreateDedicatedHostClusterRequest,
    ) -> ecs_20140526_models.CreateDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_cluster_with_options(request, runtime)

    async def create_dedicated_host_cluster_async(
        self,
        request: ecs_20140526_models.CreateDedicatedHostClusterRequest,
    ) -> ecs_20140526_models.CreateDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_cluster_with_options_async(request, runtime)

    def create_demand_with_options(
        self,
        request: ecs_20140526_models.CreateDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDemandResponse().from_map(
            self.do_rpcrequest('CreateDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_demand_with_options_async(
        self,
        request: ecs_20140526_models.CreateDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDemandResponse().from_map(
            await self.do_rpcrequest_async('CreateDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_demand(
        self,
        request: ecs_20140526_models.CreateDemandRequest,
    ) -> ecs_20140526_models.CreateDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_demand_with_options(request, runtime)

    async def create_demand_async(
        self,
        request: ecs_20140526_models.CreateDemandRequest,
    ) -> ecs_20140526_models.CreateDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_demand_with_options_async(request, runtime)

    def create_deployment_set_with_options(
        self,
        request: ecs_20140526_models.CreateDeploymentSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDeploymentSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDeploymentSetResponse().from_map(
            self.do_rpcrequest('CreateDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_deployment_set_with_options_async(
        self,
        request: ecs_20140526_models.CreateDeploymentSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDeploymentSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDeploymentSetResponse().from_map(
            await self.do_rpcrequest_async('CreateDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_deployment_set(
        self,
        request: ecs_20140526_models.CreateDeploymentSetRequest,
    ) -> ecs_20140526_models.CreateDeploymentSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_deployment_set_with_options(request, runtime)

    async def create_deployment_set_async(
        self,
        request: ecs_20140526_models.CreateDeploymentSetRequest,
    ) -> ecs_20140526_models.CreateDeploymentSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_deployment_set_with_options_async(request, runtime)

    def create_disk_with_options(
        self,
        request: ecs_20140526_models.CreateDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDiskResponse().from_map(
            self.do_rpcrequest('CreateDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_disk_with_options_async(
        self,
        request: ecs_20140526_models.CreateDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateDiskResponse().from_map(
            await self.do_rpcrequest_async('CreateDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_disk(
        self,
        request: ecs_20140526_models.CreateDiskRequest,
    ) -> ecs_20140526_models.CreateDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_disk_with_options(request, runtime)

    async def create_disk_async(
        self,
        request: ecs_20140526_models.CreateDiskRequest,
    ) -> ecs_20140526_models.CreateDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_disk_with_options_async(request, runtime)

    def create_elasticity_assurance_with_options(
        self,
        request: ecs_20140526_models.CreateElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateElasticityAssuranceResponse().from_map(
            self.do_rpcrequest('CreateElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_elasticity_assurance_with_options_async(
        self,
        request: ecs_20140526_models.CreateElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateElasticityAssuranceResponse().from_map(
            await self.do_rpcrequest_async('CreateElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_elasticity_assurance(
        self,
        request: ecs_20140526_models.CreateElasticityAssuranceRequest,
    ) -> ecs_20140526_models.CreateElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_elasticity_assurance_with_options(request, runtime)

    async def create_elasticity_assurance_async(
        self,
        request: ecs_20140526_models.CreateElasticityAssuranceRequest,
    ) -> ecs_20140526_models.CreateElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_elasticity_assurance_with_options_async(request, runtime)

    def create_forward_entry_with_options(
        self,
        request: ecs_20140526_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateForwardEntryResponse().from_map(
            self.do_rpcrequest('CreateForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_forward_entry_with_options_async(
        self,
        request: ecs_20140526_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_forward_entry(
        self,
        request: ecs_20140526_models.CreateForwardEntryRequest,
    ) -> ecs_20140526_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_forward_entry_with_options(request, runtime)

    async def create_forward_entry_async(
        self,
        request: ecs_20140526_models.CreateForwardEntryRequest,
    ) -> ecs_20140526_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_forward_entry_with_options_async(request, runtime)

    def create_ha_vip_with_options(
        self,
        request: ecs_20140526_models.CreateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateHaVipResponse().from_map(
            self.do_rpcrequest('CreateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ha_vip_with_options_async(
        self,
        request: ecs_20140526_models.CreateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateHaVipResponse().from_map(
            await self.do_rpcrequest_async('CreateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ha_vip(
        self,
        request: ecs_20140526_models.CreateHaVipRequest,
    ) -> ecs_20140526_models.CreateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ha_vip_with_options(request, runtime)

    async def create_ha_vip_async(
        self,
        request: ecs_20140526_models.CreateHaVipRequest,
    ) -> ecs_20140526_models.CreateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ha_vip_with_options_async(request, runtime)

    def create_hpc_cluster_with_options(
        self,
        request: ecs_20140526_models.CreateHpcClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateHpcClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateHpcClusterResponse().from_map(
            self.do_rpcrequest('CreateHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_hpc_cluster_with_options_async(
        self,
        request: ecs_20140526_models.CreateHpcClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateHpcClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateHpcClusterResponse().from_map(
            await self.do_rpcrequest_async('CreateHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_hpc_cluster(
        self,
        request: ecs_20140526_models.CreateHpcClusterRequest,
    ) -> ecs_20140526_models.CreateHpcClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_hpc_cluster_with_options(request, runtime)

    async def create_hpc_cluster_async(
        self,
        request: ecs_20140526_models.CreateHpcClusterRequest,
    ) -> ecs_20140526_models.CreateHpcClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_hpc_cluster_with_options_async(request, runtime)

    def create_image_with_options(
        self,
        request: ecs_20140526_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImageResponse().from_map(
            self.do_rpcrequest('CreateImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_with_options_async(
        self,
        request: ecs_20140526_models.CreateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImageResponse().from_map(
            await self.do_rpcrequest_async('CreateImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image(
        self,
        request: ecs_20140526_models.CreateImageRequest,
    ) -> ecs_20140526_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    async def create_image_async(
        self,
        request: ecs_20140526_models.CreateImageRequest,
    ) -> ecs_20140526_models.CreateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_with_options_async(request, runtime)

    def create_image_component_with_options(
        self,
        request: ecs_20140526_models.CreateImageComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImageComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImageComponentResponse().from_map(
            self.do_rpcrequest('CreateImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_component_with_options_async(
        self,
        request: ecs_20140526_models.CreateImageComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImageComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImageComponentResponse().from_map(
            await self.do_rpcrequest_async('CreateImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_component(
        self,
        request: ecs_20140526_models.CreateImageComponentRequest,
    ) -> ecs_20140526_models.CreateImageComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_component_with_options(request, runtime)

    async def create_image_component_async(
        self,
        request: ecs_20140526_models.CreateImageComponentRequest,
    ) -> ecs_20140526_models.CreateImageComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_component_with_options_async(request, runtime)

    def create_image_pipeline_with_options(
        self,
        request: ecs_20140526_models.CreateImagePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImagePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImagePipelineResponse().from_map(
            self.do_rpcrequest('CreateImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_image_pipeline_with_options_async(
        self,
        request: ecs_20140526_models.CreateImagePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateImagePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateImagePipelineResponse().from_map(
            await self.do_rpcrequest_async('CreateImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_image_pipeline(
        self,
        request: ecs_20140526_models.CreateImagePipelineRequest,
    ) -> ecs_20140526_models.CreateImagePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_image_pipeline_with_options(request, runtime)

    async def create_image_pipeline_async(
        self,
        request: ecs_20140526_models.CreateImagePipelineRequest,
    ) -> ecs_20140526_models.CreateImagePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_image_pipeline_with_options_async(request, runtime)

    def create_instance_with_options(
        self,
        request: ecs_20140526_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateInstanceResponse().from_map(
            self.do_rpcrequest('CreateInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_with_options_async(
        self,
        request: ecs_20140526_models.CreateInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance(
        self,
        request: ecs_20140526_models.CreateInstanceRequest,
    ) -> ecs_20140526_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    async def create_instance_async(
        self,
        request: ecs_20140526_models.CreateInstanceRequest,
    ) -> ecs_20140526_models.CreateInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_with_options_async(request, runtime)

    def create_key_pair_with_options(
        self,
        request: ecs_20140526_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateKeyPairResponse().from_map(
            self.do_rpcrequest('CreateKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.CreateKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateKeyPairResponse().from_map(
            await self.do_rpcrequest_async('CreateKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_key_pair(
        self,
        request: ecs_20140526_models.CreateKeyPairRequest,
    ) -> ecs_20140526_models.CreateKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    async def create_key_pair_async(
        self,
        request: ecs_20140526_models.CreateKeyPairRequest,
    ) -> ecs_20140526_models.CreateKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_key_pair_with_options_async(request, runtime)

    def create_launch_template_with_options(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateLaunchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateLaunchTemplateResponse().from_map(
            self.do_rpcrequest('CreateLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_launch_template_with_options_async(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateLaunchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateLaunchTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_launch_template(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateRequest,
    ) -> ecs_20140526_models.CreateLaunchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_with_options(request, runtime)

    async def create_launch_template_async(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateRequest,
    ) -> ecs_20140526_models.CreateLaunchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_launch_template_with_options_async(request, runtime)

    def create_launch_template_version_with_options(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateLaunchTemplateVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateLaunchTemplateVersionResponse().from_map(
            self.do_rpcrequest('CreateLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_launch_template_version_with_options_async(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateLaunchTemplateVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateLaunchTemplateVersionResponse().from_map(
            await self.do_rpcrequest_async('CreateLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_launch_template_version(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateVersionRequest,
    ) -> ecs_20140526_models.CreateLaunchTemplateVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_launch_template_version_with_options(request, runtime)

    async def create_launch_template_version_async(
        self,
        request: ecs_20140526_models.CreateLaunchTemplateVersionRequest,
    ) -> ecs_20140526_models.CreateLaunchTemplateVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_launch_template_version_with_options_async(request, runtime)

    def create_nat_gateway_with_options(
        self,
        request: ecs_20140526_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNatGatewayResponse().from_map(
            self.do_rpcrequest('CreateNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nat_gateway_with_options_async(
        self,
        request: ecs_20140526_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNatGatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nat_gateway(
        self,
        request: ecs_20140526_models.CreateNatGatewayRequest,
    ) -> ecs_20140526_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nat_gateway_with_options(request, runtime)

    async def create_nat_gateway_async(
        self,
        request: ecs_20140526_models.CreateNatGatewayRequest,
    ) -> ecs_20140526_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_gateway_with_options_async(request, runtime)

    def create_network_interface_with_options(
        self,
        request: ecs_20140526_models.CreateNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('CreateNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_interface_with_options_async(
        self,
        request: ecs_20140526_models.CreateNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('CreateNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_interface(
        self,
        request: ecs_20140526_models.CreateNetworkInterfaceRequest,
    ) -> ecs_20140526_models.CreateNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_with_options(request, runtime)

    async def create_network_interface_async(
        self,
        request: ecs_20140526_models.CreateNetworkInterfaceRequest,
    ) -> ecs_20140526_models.CreateNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_interface_with_options_async(request, runtime)

    def create_network_interface_permission_with_options(
        self,
        request: ecs_20140526_models.CreateNetworkInterfacePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNetworkInterfacePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNetworkInterfacePermissionResponse().from_map(
            self.do_rpcrequest('CreateNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_interface_permission_with_options_async(
        self,
        request: ecs_20140526_models.CreateNetworkInterfacePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateNetworkInterfacePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateNetworkInterfacePermissionResponse().from_map(
            await self.do_rpcrequest_async('CreateNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_interface_permission(
        self,
        request: ecs_20140526_models.CreateNetworkInterfacePermissionRequest,
    ) -> ecs_20140526_models.CreateNetworkInterfacePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_interface_permission_with_options(request, runtime)

    async def create_network_interface_permission_async(
        self,
        request: ecs_20140526_models.CreateNetworkInterfacePermissionRequest,
    ) -> ecs_20140526_models.CreateNetworkInterfacePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_interface_permission_with_options_async(request, runtime)

    def create_physical_connection_with_options(
        self,
        request: ecs_20140526_models.CreatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreatePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('CreatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.CreatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreatePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_connection(
        self,
        request: ecs_20140526_models.CreatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.CreatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_with_options(request, runtime)

    async def create_physical_connection_async(
        self,
        request: ecs_20140526_models.CreatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.CreatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_connection_with_options_async(request, runtime)

    def create_resource_02with_options(
        self,
        request: ecs_20140526_models.CreateResource02Request,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateResource02Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateResource02Response().from_map(
            self.do_rpcrequest('CreateResource02', '2014-05-26', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    async def create_resource_02with_options_async(
        self,
        request: ecs_20140526_models.CreateResource02Request,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateResource02Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateResource02Response().from_map(
            await self.do_rpcrequest_async('CreateResource02', '2014-05-26', 'HTTPS', 'PUT', 'AK', 'json', req, runtime)
        )

    def create_resource_02(
        self,
        request: ecs_20140526_models.CreateResource02Request,
    ) -> ecs_20140526_models.CreateResource02Response:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_02with_options(request, runtime)

    async def create_resource_02_async(
        self,
        request: ecs_20140526_models.CreateResource02Request,
    ) -> ecs_20140526_models.CreateResource02Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_02with_options_async(request, runtime)

    def create_route_entry_with_options(
        self,
        request: ecs_20140526_models.CreateRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateRouteEntryResponse().from_map(
            self.do_rpcrequest('CreateRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_route_entry_with_options_async(
        self,
        request: ecs_20140526_models.CreateRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_route_entry(
        self,
        request: ecs_20140526_models.CreateRouteEntryRequest,
    ) -> ecs_20140526_models.CreateRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_route_entry_with_options(request, runtime)

    async def create_route_entry_async(
        self,
        request: ecs_20140526_models.CreateRouteEntryRequest,
    ) -> ecs_20140526_models.CreateRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_route_entry_with_options_async(request, runtime)

    def create_router_interface_with_options(
        self,
        request: ecs_20140526_models.CreateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('CreateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.CreateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('CreateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_router_interface(
        self,
        request: ecs_20140526_models.CreateRouterInterfaceRequest,
    ) -> ecs_20140526_models.CreateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_router_interface_with_options(request, runtime)

    async def create_router_interface_async(
        self,
        request: ecs_20140526_models.CreateRouterInterfaceRequest,
    ) -> ecs_20140526_models.CreateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_router_interface_with_options_async(request, runtime)

    def create_security_group_with_options(
        self,
        request: ecs_20140526_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSecurityGroupResponse().from_map(
            self.do_rpcrequest('CreateSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_security_group_with_options_async(
        self,
        request: ecs_20140526_models.CreateSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_security_group(
        self,
        request: ecs_20140526_models.CreateSecurityGroupRequest,
    ) -> ecs_20140526_models.CreateSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_security_group_with_options(request, runtime)

    async def create_security_group_async(
        self,
        request: ecs_20140526_models.CreateSecurityGroupRequest,
    ) -> ecs_20140526_models.CreateSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_security_group_with_options_async(request, runtime)

    def create_simulated_system_events_with_options(
        self,
        request: ecs_20140526_models.CreateSimulatedSystemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSimulatedSystemEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSimulatedSystemEventsResponse().from_map(
            self.do_rpcrequest('CreateSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_simulated_system_events_with_options_async(
        self,
        request: ecs_20140526_models.CreateSimulatedSystemEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSimulatedSystemEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSimulatedSystemEventsResponse().from_map(
            await self.do_rpcrequest_async('CreateSimulatedSystemEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_simulated_system_events(
        self,
        request: ecs_20140526_models.CreateSimulatedSystemEventsRequest,
    ) -> ecs_20140526_models.CreateSimulatedSystemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_simulated_system_events_with_options(request, runtime)

    async def create_simulated_system_events_async(
        self,
        request: ecs_20140526_models.CreateSimulatedSystemEventsRequest,
    ) -> ecs_20140526_models.CreateSimulatedSystemEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_simulated_system_events_with_options_async(request, runtime)

    def create_snapshot_with_options(
        self,
        request: ecs_20140526_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSnapshotResponse().from_map(
            self.do_rpcrequest('CreateSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.CreateSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSnapshotResponse().from_map(
            await self.do_rpcrequest_async('CreateSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot(
        self,
        request: ecs_20140526_models.CreateSnapshotRequest,
    ) -> ecs_20140526_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_with_options(request, runtime)

    async def create_snapshot_async(
        self,
        request: ecs_20140526_models.CreateSnapshotRequest,
    ) -> ecs_20140526_models.CreateSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_with_options_async(request, runtime)

    def create_snapshot_group_with_options(
        self,
        request: ecs_20140526_models.CreateSnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSnapshotGroupResponse().from_map(
            self.do_rpcrequest('CreateSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snapshot_group_with_options_async(
        self,
        request: ecs_20140526_models.CreateSnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateSnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateSnapshotGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snapshot_group(
        self,
        request: ecs_20140526_models.CreateSnapshotGroupRequest,
    ) -> ecs_20140526_models.CreateSnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snapshot_group_with_options(request, runtime)

    async def create_snapshot_group_async(
        self,
        request: ecs_20140526_models.CreateSnapshotGroupRequest,
    ) -> ecs_20140526_models.CreateSnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snapshot_group_with_options_async(request, runtime)

    def create_storage_set_with_options(
        self,
        request: ecs_20140526_models.CreateStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateStorageSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateStorageSetResponse().from_map(
            self.do_rpcrequest('CreateStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_storage_set_with_options_async(
        self,
        request: ecs_20140526_models.CreateStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateStorageSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateStorageSetResponse().from_map(
            await self.do_rpcrequest_async('CreateStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_storage_set(
        self,
        request: ecs_20140526_models.CreateStorageSetRequest,
    ) -> ecs_20140526_models.CreateStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_storage_set_with_options(request, runtime)

    async def create_storage_set_async(
        self,
        request: ecs_20140526_models.CreateStorageSetRequest,
    ) -> ecs_20140526_models.CreateStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_storage_set_with_options_async(request, runtime)

    def create_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.CreateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('CreateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.CreateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('CreateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_border_router(
        self,
        request: ecs_20140526_models.CreateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.CreateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_border_router_with_options(request, runtime)

    async def create_virtual_border_router_async(
        self,
        request: ecs_20140526_models.CreateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.CreateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_border_router_with_options_async(request, runtime)

    def create_vpc_with_options(
        self,
        request: ecs_20140526_models.CreateVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVpcResponse().from_map(
            self.do_rpcrequest('CreateVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpc_with_options_async(
        self,
        request: ecs_20140526_models.CreateVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVpcResponse().from_map(
            await self.do_rpcrequest_async('CreateVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc(
        self,
        request: ecs_20140526_models.CreateVpcRequest,
    ) -> ecs_20140526_models.CreateVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_with_options(request, runtime)

    async def create_vpc_async(
        self,
        request: ecs_20140526_models.CreateVpcRequest,
    ) -> ecs_20140526_models.CreateVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_with_options_async(request, runtime)

    def create_vswitch_with_options(
        self,
        request: ecs_20140526_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVSwitchResponse().from_map(
            self.do_rpcrequest('CreateVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vswitch_with_options_async(
        self,
        request: ecs_20140526_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.CreateVSwitchResponse().from_map(
            await self.do_rpcrequest_async('CreateVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vswitch(
        self,
        request: ecs_20140526_models.CreateVSwitchRequest,
    ) -> ecs_20140526_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    async def create_vswitch_async(
        self,
        request: ecs_20140526_models.CreateVSwitchRequest,
    ) -> ecs_20140526_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vswitch_with_options_async(request, runtime)

    def deactivate_router_interface_with_options(
        self,
        request: ecs_20140526_models.DeactivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeactivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeactivateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('DeactivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactivate_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.DeactivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeactivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeactivateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeactivateRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_router_interface(
        self,
        request: ecs_20140526_models.DeactivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.DeactivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactivate_router_interface_with_options(request, runtime)

    async def deactivate_router_interface_async(
        self,
        request: ecs_20140526_models.DeactivateRouterInterfaceRequest,
    ) -> ecs_20140526_models.DeactivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_router_interface_with_options_async(request, runtime)

    def delete_activation_with_options(
        self,
        request: ecs_20140526_models.DeleteActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteActivationResponse().from_map(
            self.do_rpcrequest('DeleteActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_activation_with_options_async(
        self,
        request: ecs_20140526_models.DeleteActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteActivationResponse().from_map(
            await self.do_rpcrequest_async('DeleteActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_activation(
        self,
        request: ecs_20140526_models.DeleteActivationRequest,
    ) -> ecs_20140526_models.DeleteActivationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_activation_with_options(request, runtime)

    async def delete_activation_async(
        self,
        request: ecs_20140526_models.DeleteActivationRequest,
    ) -> ecs_20140526_models.DeleteActivationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_activation_with_options_async(request, runtime)

    def delete_auto_provisioning_group_with_options(
        self,
        request: ecs_20140526_models.DeleteAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteAutoProvisioningGroupResponse().from_map(
            self.do_rpcrequest('DeleteAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_provisioning_group_with_options_async(
        self,
        request: ecs_20140526_models.DeleteAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteAutoProvisioningGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_provisioning_group(
        self,
        request: ecs_20140526_models.DeleteAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.DeleteAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_provisioning_group_with_options(request, runtime)

    async def delete_auto_provisioning_group_async(
        self,
        request: ecs_20140526_models.DeleteAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.DeleteAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_provisioning_group_with_options_async(request, runtime)

    def delete_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('DeleteAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.DeleteAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('DeleteAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.DeleteAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    async def delete_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.DeleteAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.DeleteAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_snapshot_policy_with_options_async(request, runtime)

    def delete_bandwidth_package_with_options(
        self,
        request: ecs_20140526_models.DeleteBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteBandwidthPackageResponse().from_map(
            self.do_rpcrequest('DeleteBandwidthPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bandwidth_package_with_options_async(
        self,
        request: ecs_20140526_models.DeleteBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteBandwidthPackageResponse().from_map(
            await self.do_rpcrequest_async('DeleteBandwidthPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bandwidth_package(
        self,
        request: ecs_20140526_models.DeleteBandwidthPackageRequest,
    ) -> ecs_20140526_models.DeleteBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bandwidth_package_with_options(request, runtime)

    async def delete_bandwidth_package_async(
        self,
        request: ecs_20140526_models.DeleteBandwidthPackageRequest,
    ) -> ecs_20140526_models.DeleteBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bandwidth_package_with_options_async(request, runtime)

    def delete_command_with_options(
        self,
        request: ecs_20140526_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteCommandResponse().from_map(
            self.do_rpcrequest('DeleteCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_command_with_options_async(
        self,
        request: ecs_20140526_models.DeleteCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteCommandResponse().from_map(
            await self.do_rpcrequest_async('DeleteCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_command(
        self,
        request: ecs_20140526_models.DeleteCommandRequest,
    ) -> ecs_20140526_models.DeleteCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_command_with_options(request, runtime)

    async def delete_command_async(
        self,
        request: ecs_20140526_models.DeleteCommandRequest,
    ) -> ecs_20140526_models.DeleteCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_command_with_options_async(request, runtime)

    def delete_dedicated_host_cluster_with_options(
        self,
        request: ecs_20140526_models.DeleteDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDedicatedHostClusterResponse().from_map(
            self.do_rpcrequest('DeleteDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_host_cluster_with_options_async(
        self,
        request: ecs_20140526_models.DeleteDedicatedHostClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDedicatedHostClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDedicatedHostClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteDedicatedHostCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_cluster(
        self,
        request: ecs_20140526_models.DeleteDedicatedHostClusterRequest,
    ) -> ecs_20140526_models.DeleteDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_cluster_with_options(request, runtime)

    async def delete_dedicated_host_cluster_async(
        self,
        request: ecs_20140526_models.DeleteDedicatedHostClusterRequest,
    ) -> ecs_20140526_models.DeleteDedicatedHostClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_cluster_with_options_async(request, runtime)

    def delete_demand_with_options(
        self,
        request: ecs_20140526_models.DeleteDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDemandResponse().from_map(
            self.do_rpcrequest('DeleteDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_demand_with_options_async(
        self,
        request: ecs_20140526_models.DeleteDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDemandResponse().from_map(
            await self.do_rpcrequest_async('DeleteDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_demand(
        self,
        request: ecs_20140526_models.DeleteDemandRequest,
    ) -> ecs_20140526_models.DeleteDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_demand_with_options(request, runtime)

    async def delete_demand_async(
        self,
        request: ecs_20140526_models.DeleteDemandRequest,
    ) -> ecs_20140526_models.DeleteDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_demand_with_options_async(request, runtime)

    def delete_deployment_set_with_options(
        self,
        request: ecs_20140526_models.DeleteDeploymentSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDeploymentSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDeploymentSetResponse().from_map(
            self.do_rpcrequest('DeleteDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_deployment_set_with_options_async(
        self,
        request: ecs_20140526_models.DeleteDeploymentSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDeploymentSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDeploymentSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteDeploymentSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_deployment_set(
        self,
        request: ecs_20140526_models.DeleteDeploymentSetRequest,
    ) -> ecs_20140526_models.DeleteDeploymentSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_deployment_set_with_options(request, runtime)

    async def delete_deployment_set_async(
        self,
        request: ecs_20140526_models.DeleteDeploymentSetRequest,
    ) -> ecs_20140526_models.DeleteDeploymentSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_deployment_set_with_options_async(request, runtime)

    def delete_disk_with_options(
        self,
        request: ecs_20140526_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDiskResponse().from_map(
            self.do_rpcrequest('DeleteDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_disk_with_options_async(
        self,
        request: ecs_20140526_models.DeleteDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteDiskResponse().from_map(
            await self.do_rpcrequest_async('DeleteDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_disk(
        self,
        request: ecs_20140526_models.DeleteDiskRequest,
    ) -> ecs_20140526_models.DeleteDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_disk_with_options(request, runtime)

    async def delete_disk_async(
        self,
        request: ecs_20140526_models.DeleteDiskRequest,
    ) -> ecs_20140526_models.DeleteDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_disk_with_options_async(request, runtime)

    def delete_forward_entry_with_options(
        self,
        request: ecs_20140526_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteForwardEntryResponse().from_map(
            self.do_rpcrequest('DeleteForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_forward_entry_with_options_async(
        self,
        request: ecs_20140526_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_forward_entry(
        self,
        request: ecs_20140526_models.DeleteForwardEntryRequest,
    ) -> ecs_20140526_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_forward_entry_with_options(request, runtime)

    async def delete_forward_entry_async(
        self,
        request: ecs_20140526_models.DeleteForwardEntryRequest,
    ) -> ecs_20140526_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_forward_entry_with_options_async(request, runtime)

    def delete_ha_vip_with_options(
        self,
        request: ecs_20140526_models.DeleteHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteHaVipResponse().from_map(
            self.do_rpcrequest('DeleteHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ha_vip_with_options_async(
        self,
        request: ecs_20140526_models.DeleteHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteHaVipResponse().from_map(
            await self.do_rpcrequest_async('DeleteHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ha_vip(
        self,
        request: ecs_20140526_models.DeleteHaVipRequest,
    ) -> ecs_20140526_models.DeleteHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ha_vip_with_options(request, runtime)

    async def delete_ha_vip_async(
        self,
        request: ecs_20140526_models.DeleteHaVipRequest,
    ) -> ecs_20140526_models.DeleteHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ha_vip_with_options_async(request, runtime)

    def delete_hpc_cluster_with_options(
        self,
        request: ecs_20140526_models.DeleteHpcClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteHpcClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteHpcClusterResponse().from_map(
            self.do_rpcrequest('DeleteHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_hpc_cluster_with_options_async(
        self,
        request: ecs_20140526_models.DeleteHpcClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteHpcClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteHpcClusterResponse().from_map(
            await self.do_rpcrequest_async('DeleteHpcCluster', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_hpc_cluster(
        self,
        request: ecs_20140526_models.DeleteHpcClusterRequest,
    ) -> ecs_20140526_models.DeleteHpcClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_hpc_cluster_with_options(request, runtime)

    async def delete_hpc_cluster_async(
        self,
        request: ecs_20140526_models.DeleteHpcClusterRequest,
    ) -> ecs_20140526_models.DeleteHpcClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_hpc_cluster_with_options_async(request, runtime)

    def delete_image_with_options(
        self,
        request: ecs_20140526_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImageResponse().from_map(
            self.do_rpcrequest('DeleteImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_with_options_async(
        self,
        request: ecs_20140526_models.DeleteImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImageResponse().from_map(
            await self.do_rpcrequest_async('DeleteImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image(
        self,
        request: ecs_20140526_models.DeleteImageRequest,
    ) -> ecs_20140526_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_with_options(request, runtime)

    async def delete_image_async(
        self,
        request: ecs_20140526_models.DeleteImageRequest,
    ) -> ecs_20140526_models.DeleteImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_with_options_async(request, runtime)

    def delete_image_component_with_options(
        self,
        request: ecs_20140526_models.DeleteImageComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImageComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImageComponentResponse().from_map(
            self.do_rpcrequest('DeleteImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_component_with_options_async(
        self,
        request: ecs_20140526_models.DeleteImageComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImageComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImageComponentResponse().from_map(
            await self.do_rpcrequest_async('DeleteImageComponent', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_component(
        self,
        request: ecs_20140526_models.DeleteImageComponentRequest,
    ) -> ecs_20140526_models.DeleteImageComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_component_with_options(request, runtime)

    async def delete_image_component_async(
        self,
        request: ecs_20140526_models.DeleteImageComponentRequest,
    ) -> ecs_20140526_models.DeleteImageComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_component_with_options_async(request, runtime)

    def delete_image_pipeline_with_options(
        self,
        request: ecs_20140526_models.DeleteImagePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImagePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImagePipelineResponse().from_map(
            self.do_rpcrequest('DeleteImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_image_pipeline_with_options_async(
        self,
        request: ecs_20140526_models.DeleteImagePipelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteImagePipelineResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteImagePipelineResponse().from_map(
            await self.do_rpcrequest_async('DeleteImagePipeline', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_image_pipeline(
        self,
        request: ecs_20140526_models.DeleteImagePipelineRequest,
    ) -> ecs_20140526_models.DeleteImagePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_image_pipeline_with_options(request, runtime)

    async def delete_image_pipeline_async(
        self,
        request: ecs_20140526_models.DeleteImagePipelineRequest,
    ) -> ecs_20140526_models.DeleteImagePipelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_image_pipeline_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: ecs_20140526_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: ecs_20140526_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(
        self,
        request: ecs_20140526_models.DeleteInstanceRequest,
    ) -> ecs_20140526_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: ecs_20140526_models.DeleteInstanceRequest,
    ) -> ecs_20140526_models.DeleteInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_instances_with_options(
        self,
        request: ecs_20140526_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteInstancesResponse().from_map(
            self.do_rpcrequest('DeleteInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_instances_with_options_async(
        self,
        request: ecs_20140526_models.DeleteInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteInstancesResponse().from_map(
            await self.do_rpcrequest_async('DeleteInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instances(
        self,
        request: ecs_20140526_models.DeleteInstancesRequest,
    ) -> ecs_20140526_models.DeleteInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_instances_with_options(request, runtime)

    async def delete_instances_async(
        self,
        request: ecs_20140526_models.DeleteInstancesRequest,
    ) -> ecs_20140526_models.DeleteInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_instances_with_options_async(request, runtime)

    def delete_key_pairs_with_options(
        self,
        request: ecs_20140526_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteKeyPairsResponse().from_map(
            self.do_rpcrequest('DeleteKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_key_pairs_with_options_async(
        self,
        request: ecs_20140526_models.DeleteKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteKeyPairsResponse().from_map(
            await self.do_rpcrequest_async('DeleteKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_key_pairs(
        self,
        request: ecs_20140526_models.DeleteKeyPairsRequest,
    ) -> ecs_20140526_models.DeleteKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    async def delete_key_pairs_async(
        self,
        request: ecs_20140526_models.DeleteKeyPairsRequest,
    ) -> ecs_20140526_models.DeleteKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_key_pairs_with_options_async(request, runtime)

    def delete_launch_template_with_options(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteLaunchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteLaunchTemplateResponse().from_map(
            self.do_rpcrequest('DeleteLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_launch_template_with_options_async(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteLaunchTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteLaunchTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteLaunchTemplate', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_launch_template(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateRequest,
    ) -> ecs_20140526_models.DeleteLaunchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_with_options(request, runtime)

    async def delete_launch_template_async(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateRequest,
    ) -> ecs_20140526_models.DeleteLaunchTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_launch_template_with_options_async(request, runtime)

    def delete_launch_template_version_with_options(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteLaunchTemplateVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteLaunchTemplateVersionResponse().from_map(
            self.do_rpcrequest('DeleteLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_launch_template_version_with_options_async(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteLaunchTemplateVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteLaunchTemplateVersionResponse().from_map(
            await self.do_rpcrequest_async('DeleteLaunchTemplateVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_launch_template_version(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateVersionRequest,
    ) -> ecs_20140526_models.DeleteLaunchTemplateVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_launch_template_version_with_options(request, runtime)

    async def delete_launch_template_version_async(
        self,
        request: ecs_20140526_models.DeleteLaunchTemplateVersionRequest,
    ) -> ecs_20140526_models.DeleteLaunchTemplateVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_launch_template_version_with_options_async(request, runtime)

    def delete_nat_gateway_with_options(
        self,
        request: ecs_20140526_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNatGatewayResponse().from_map(
            self.do_rpcrequest('DeleteNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nat_gateway_with_options_async(
        self,
        request: ecs_20140526_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNatGatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteNatGateway', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nat_gateway(
        self,
        request: ecs_20140526_models.DeleteNatGatewayRequest,
    ) -> ecs_20140526_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_gateway_with_options(request, runtime)

    async def delete_nat_gateway_async(
        self,
        request: ecs_20140526_models.DeleteNatGatewayRequest,
    ) -> ecs_20140526_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_gateway_with_options_async(request, runtime)

    def delete_network_interface_with_options(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('DeleteNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_interface_with_options_async(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_interface(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DeleteNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_with_options(request, runtime)

    async def delete_network_interface_async(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DeleteNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_interface_with_options_async(request, runtime)

    def delete_network_interface_permission_with_options(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfacePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNetworkInterfacePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNetworkInterfacePermissionResponse().from_map(
            self.do_rpcrequest('DeleteNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_interface_permission_with_options_async(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfacePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteNetworkInterfacePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteNetworkInterfacePermissionResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkInterfacePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_interface_permission(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfacePermissionRequest,
    ) -> ecs_20140526_models.DeleteNetworkInterfacePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_interface_permission_with_options(request, runtime)

    async def delete_network_interface_permission_async(
        self,
        request: ecs_20140526_models.DeleteNetworkInterfacePermissionRequest,
    ) -> ecs_20140526_models.DeleteNetworkInterfacePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_interface_permission_with_options_async(request, runtime)

    def delete_physical_connection_with_options(
        self,
        request: ecs_20140526_models.DeletePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeletePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeletePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('DeletePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.DeletePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeletePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeletePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeletePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_physical_connection(
        self,
        request: ecs_20140526_models.DeletePhysicalConnectionRequest,
    ) -> ecs_20140526_models.DeletePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_connection_with_options(request, runtime)

    async def delete_physical_connection_async(
        self,
        request: ecs_20140526_models.DeletePhysicalConnectionRequest,
    ) -> ecs_20140526_models.DeletePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_physical_connection_with_options_async(request, runtime)

    def delete_route_entry_with_options(
        self,
        request: ecs_20140526_models.DeleteRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteRouteEntryResponse().from_map(
            self.do_rpcrequest('DeleteRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_route_entry_with_options_async(
        self,
        request: ecs_20140526_models.DeleteRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouteEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_entry(
        self,
        request: ecs_20140526_models.DeleteRouteEntryRequest,
    ) -> ecs_20140526_models.DeleteRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_entry_with_options(request, runtime)

    async def delete_route_entry_async(
        self,
        request: ecs_20140526_models.DeleteRouteEntryRequest,
    ) -> ecs_20140526_models.DeleteRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_entry_with_options_async(request, runtime)

    def delete_router_interface_with_options(
        self,
        request: ecs_20140526_models.DeleteRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteRouterInterfaceResponse().from_map(
            self.do_rpcrequest('DeleteRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_router_interface_with_options_async(
        self,
        request: ecs_20140526_models.DeleteRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouterInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_router_interface(
        self,
        request: ecs_20140526_models.DeleteRouterInterfaceRequest,
    ) -> ecs_20140526_models.DeleteRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_router_interface_with_options(request, runtime)

    async def delete_router_interface_async(
        self,
        request: ecs_20140526_models.DeleteRouterInterfaceRequest,
    ) -> ecs_20140526_models.DeleteRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_router_interface_with_options_async(request, runtime)

    def delete_security_group_with_options(
        self,
        request: ecs_20140526_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSecurityGroupResponse().from_map(
            self.do_rpcrequest('DeleteSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_security_group_with_options_async(
        self,
        request: ecs_20140526_models.DeleteSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_group(
        self,
        request: ecs_20140526_models.DeleteSecurityGroupRequest,
    ) -> ecs_20140526_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    async def delete_security_group_async(
        self,
        request: ecs_20140526_models.DeleteSecurityGroupRequest,
    ) -> ecs_20140526_models.DeleteSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_group_with_options_async(request, runtime)

    def delete_snapshot_with_options(
        self,
        request: ecs_20140526_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSnapshotResponse().from_map(
            self.do_rpcrequest('DeleteSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.DeleteSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSnapshotResponse().from_map(
            await self.do_rpcrequest_async('DeleteSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot(
        self,
        request: ecs_20140526_models.DeleteSnapshotRequest,
    ) -> ecs_20140526_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_with_options(request, runtime)

    async def delete_snapshot_async(
        self,
        request: ecs_20140526_models.DeleteSnapshotRequest,
    ) -> ecs_20140526_models.DeleteSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_with_options_async(request, runtime)

    def delete_snapshot_group_with_options(
        self,
        request: ecs_20140526_models.DeleteSnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSnapshotGroupResponse().from_map(
            self.do_rpcrequest('DeleteSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snapshot_group_with_options_async(
        self,
        request: ecs_20140526_models.DeleteSnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteSnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteSnapshotGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteSnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snapshot_group(
        self,
        request: ecs_20140526_models.DeleteSnapshotGroupRequest,
    ) -> ecs_20140526_models.DeleteSnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_group_with_options(request, runtime)

    async def delete_snapshot_group_async(
        self,
        request: ecs_20140526_models.DeleteSnapshotGroupRequest,
    ) -> ecs_20140526_models.DeleteSnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snapshot_group_with_options_async(request, runtime)

    def delete_storage_set_with_options(
        self,
        request: ecs_20140526_models.DeleteStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteStorageSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteStorageSetResponse().from_map(
            self.do_rpcrequest('DeleteStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_storage_set_with_options_async(
        self,
        request: ecs_20140526_models.DeleteStorageSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteStorageSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteStorageSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteStorageSet', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_storage_set(
        self,
        request: ecs_20140526_models.DeleteStorageSetRequest,
    ) -> ecs_20140526_models.DeleteStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_storage_set_with_options(request, runtime)

    async def delete_storage_set_async(
        self,
        request: ecs_20140526_models.DeleteStorageSetRequest,
    ) -> ecs_20140526_models.DeleteStorageSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_storage_set_with_options_async(request, runtime)

    def delete_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.DeleteVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('DeleteVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.DeleteVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('DeleteVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_border_router(
        self,
        request: ecs_20140526_models.DeleteVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.DeleteVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_border_router_with_options(request, runtime)

    async def delete_virtual_border_router_async(
        self,
        request: ecs_20140526_models.DeleteVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.DeleteVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_border_router_with_options_async(request, runtime)

    def delete_vpc_with_options(
        self,
        request: ecs_20140526_models.DeleteVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVpcResponse().from_map(
            self.do_rpcrequest('DeleteVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_with_options_async(
        self,
        request: ecs_20140526_models.DeleteVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVpcResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc(
        self,
        request: ecs_20140526_models.DeleteVpcRequest,
    ) -> ecs_20140526_models.DeleteVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_with_options(request, runtime)

    async def delete_vpc_async(
        self,
        request: ecs_20140526_models.DeleteVpcRequest,
    ) -> ecs_20140526_models.DeleteVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_with_options_async(request, runtime)

    def delete_vswitch_with_options(
        self,
        request: ecs_20140526_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVSwitchResponse().from_map(
            self.do_rpcrequest('DeleteVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vswitch_with_options_async(
        self,
        request: ecs_20140526_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeleteVSwitchResponse().from_map(
            await self.do_rpcrequest_async('DeleteVSwitch', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vswitch(
        self,
        request: ecs_20140526_models.DeleteVSwitchRequest,
    ) -> ecs_20140526_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    async def delete_vswitch_async(
        self,
        request: ecs_20140526_models.DeleteVSwitchRequest,
    ) -> ecs_20140526_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vswitch_with_options_async(request, runtime)

    def deregister_managed_instance_with_options(
        self,
        request: ecs_20140526_models.DeregisterManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeregisterManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeregisterManagedInstanceResponse().from_map(
            self.do_rpcrequest('DeregisterManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deregister_managed_instance_with_options_async(
        self,
        request: ecs_20140526_models.DeregisterManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DeregisterManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DeregisterManagedInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeregisterManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_managed_instance(
        self,
        request: ecs_20140526_models.DeregisterManagedInstanceRequest,
    ) -> ecs_20140526_models.DeregisterManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_managed_instance_with_options(request, runtime)

    async def deregister_managed_instance_async(
        self,
        request: ecs_20140526_models.DeregisterManagedInstanceRequest,
    ) -> ecs_20140526_models.DeregisterManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_managed_instance_with_options_async(request, runtime)

    def describe_access_points_with_options(
        self,
        request: ecs_20140526_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAccessPointsResponse().from_map(
            self.do_rpcrequest('DescribeAccessPoints', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_points_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAccessPointsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccessPoints', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_points(
        self,
        request: ecs_20140526_models.DescribeAccessPointsRequest,
    ) -> ecs_20140526_models.DescribeAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    async def describe_access_points_async(
        self,
        request: ecs_20140526_models.DescribeAccessPointsRequest,
    ) -> ecs_20140526_models.DescribeAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_points_with_options_async(request, runtime)

    def describe_account_attributes_with_options(
        self,
        request: ecs_20140526_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAccountAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAccountAttributesResponse().from_map(
            self.do_rpcrequest('DescribeAccountAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_account_attributes_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAccountAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAccountAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAccountAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccountAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_attributes(
        self,
        request: ecs_20140526_models.DescribeAccountAttributesRequest,
    ) -> ecs_20140526_models.DescribeAccountAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_attributes_with_options(request, runtime)

    async def describe_account_attributes_async(
        self,
        request: ecs_20140526_models.DescribeAccountAttributesRequest,
    ) -> ecs_20140526_models.DescribeAccountAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_attributes_with_options_async(request, runtime)

    def describe_activations_with_options(
        self,
        request: ecs_20140526_models.DescribeActivationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeActivationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeActivationsResponse().from_map(
            self.do_rpcrequest('DescribeActivations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_activations_with_options_async(
        self,
        request: ecs_20140526_models.DescribeActivationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeActivationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeActivationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeActivations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_activations(
        self,
        request: ecs_20140526_models.DescribeActivationsRequest,
    ) -> ecs_20140526_models.DescribeActivationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_activations_with_options(request, runtime)

    async def describe_activations_async(
        self,
        request: ecs_20140526_models.DescribeActivationsRequest,
    ) -> ecs_20140526_models.DescribeActivationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_activations_with_options_async(request, runtime)

    def describe_auto_provisioning_group_history_with_options(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse().from_map(
            self.do_rpcrequest('DescribeAutoProvisioningGroupHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_provisioning_group_history_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoProvisioningGroupHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_group_history(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupHistoryRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_history_with_options(request, runtime)

    async def describe_auto_provisioning_group_history_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupHistoryRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_provisioning_group_history_with_options_async(request, runtime)

    def describe_auto_provisioning_group_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse().from_map(
            self.do_rpcrequest('DescribeAutoProvisioningGroupInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_provisioning_group_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoProvisioningGroupInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_group_instances(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupInstancesRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_group_instances_with_options(request, runtime)

    async def describe_auto_provisioning_group_instances_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupInstancesRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_provisioning_group_instances_with_options_async(request, runtime)

    def describe_auto_provisioning_groups_with_options(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupsResponse().from_map(
            self.do_rpcrequest('DescribeAutoProvisioningGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_provisioning_groups_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoProvisioningGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoProvisioningGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_provisioning_groups(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupsRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_provisioning_groups_with_options(request, runtime)

    async def describe_auto_provisioning_groups_async(
        self,
        request: ecs_20140526_models.DescribeAutoProvisioningGroupsRequest,
    ) -> ecs_20140526_models.DescribeAutoProvisioningGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_provisioning_groups_with_options_async(request, runtime)

    def describe_auto_snapshot_policy_ex_with_options(
        self,
        request: ecs_20140526_models.DescribeAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse().from_map(
            self.do_rpcrequest('DescribeAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_auto_snapshot_policy_ex_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse().from_map(
            await self.do_rpcrequest_async('DescribeAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_auto_snapshot_policy_ex(
        self,
        request: ecs_20140526_models.DescribeAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_snapshot_policy_ex_with_options(request, runtime)

    async def describe_auto_snapshot_policy_ex_async(
        self,
        request: ecs_20140526_models.DescribeAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_auto_snapshot_policy_ex_with_options_async(request, runtime)

    def describe_available_resource_with_options(
        self,
        request: ecs_20140526_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAvailableResourceResponse().from_map(
            self.do_rpcrequest('DescribeAvailableResource', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_resource_with_options_async(
        self,
        request: ecs_20140526_models.DescribeAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeAvailableResource', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(
        self,
        request: ecs_20140526_models.DescribeAvailableResourceRequest,
    ) -> ecs_20140526_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    async def describe_available_resource_async(
        self,
        request: ecs_20140526_models.DescribeAvailableResourceRequest,
    ) -> ecs_20140526_models.DescribeAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_resource_with_options_async(request, runtime)

    def describe_bandwidth_limitation_with_options(
        self,
        request: ecs_20140526_models.DescribeBandwidthLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeBandwidthLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeBandwidthLimitationResponse().from_map(
            self.do_rpcrequest('DescribeBandwidthLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bandwidth_limitation_with_options_async(
        self,
        request: ecs_20140526_models.DescribeBandwidthLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeBandwidthLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeBandwidthLimitationResponse().from_map(
            await self.do_rpcrequest_async('DescribeBandwidthLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bandwidth_limitation(
        self,
        request: ecs_20140526_models.DescribeBandwidthLimitationRequest,
    ) -> ecs_20140526_models.DescribeBandwidthLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_limitation_with_options(request, runtime)

    async def describe_bandwidth_limitation_async(
        self,
        request: ecs_20140526_models.DescribeBandwidthLimitationRequest,
    ) -> ecs_20140526_models.DescribeBandwidthLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bandwidth_limitation_with_options_async(request, runtime)

    def describe_bandwidth_packages_with_options(
        self,
        request: ecs_20140526_models.DescribeBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeBandwidthPackagesResponse().from_map(
            self.do_rpcrequest('DescribeBandwidthPackages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bandwidth_packages_with_options_async(
        self,
        request: ecs_20140526_models.DescribeBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeBandwidthPackagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeBandwidthPackages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bandwidth_packages(
        self,
        request: ecs_20140526_models.DescribeBandwidthPackagesRequest,
    ) -> ecs_20140526_models.DescribeBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwidth_packages_with_options(request, runtime)

    async def describe_bandwidth_packages_async(
        self,
        request: ecs_20140526_models.DescribeBandwidthPackagesRequest,
    ) -> ecs_20140526_models.DescribeBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bandwidth_packages_with_options_async(request, runtime)

    def describe_capacity_reservation_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCapacityReservationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCapacityReservationInstancesResponse().from_map(
            self.do_rpcrequest('DescribeCapacityReservationInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_capacity_reservation_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCapacityReservationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCapacityReservationInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCapacityReservationInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_capacity_reservation_instances(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationInstancesRequest,
    ) -> ecs_20140526_models.DescribeCapacityReservationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservation_instances_with_options(request, runtime)

    async def describe_capacity_reservation_instances_async(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationInstancesRequest,
    ) -> ecs_20140526_models.DescribeCapacityReservationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_capacity_reservation_instances_with_options_async(request, runtime)

    def describe_capacity_reservations_with_options(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCapacityReservationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCapacityReservationsResponse().from_map(
            self.do_rpcrequest('DescribeCapacityReservations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_capacity_reservations_with_options_async(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCapacityReservationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCapacityReservationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCapacityReservations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_capacity_reservations(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationsRequest,
    ) -> ecs_20140526_models.DescribeCapacityReservationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_capacity_reservations_with_options(request, runtime)

    async def describe_capacity_reservations_async(
        self,
        request: ecs_20140526_models.DescribeCapacityReservationsRequest,
    ) -> ecs_20140526_models.DescribeCapacityReservationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_capacity_reservations_with_options_async(request, runtime)

    def describe_classic_link_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeClassicLinkInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeClassicLinkInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeClassicLinkInstancesResponse().from_map(
            self.do_rpcrequest('DescribeClassicLinkInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_classic_link_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeClassicLinkInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeClassicLinkInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeClassicLinkInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeClassicLinkInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_classic_link_instances(
        self,
        request: ecs_20140526_models.DescribeClassicLinkInstancesRequest,
    ) -> ecs_20140526_models.DescribeClassicLinkInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_classic_link_instances_with_options(request, runtime)

    async def describe_classic_link_instances_async(
        self,
        request: ecs_20140526_models.DescribeClassicLinkInstancesRequest,
    ) -> ecs_20140526_models.DescribeClassicLinkInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_classic_link_instances_with_options_async(request, runtime)

    def describe_cloud_assistant_status_with_options(
        self,
        request: ecs_20140526_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCloudAssistantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCloudAssistantStatusResponse().from_map(
            self.do_rpcrequest('DescribeCloudAssistantStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cloud_assistant_status_with_options_async(
        self,
        request: ecs_20140526_models.DescribeCloudAssistantStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCloudAssistantStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCloudAssistantStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeCloudAssistantStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cloud_assistant_status(
        self,
        request: ecs_20140526_models.DescribeCloudAssistantStatusRequest,
    ) -> ecs_20140526_models.DescribeCloudAssistantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    async def describe_cloud_assistant_status_async(
        self,
        request: ecs_20140526_models.DescribeCloudAssistantStatusRequest,
    ) -> ecs_20140526_models.DescribeCloudAssistantStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cloud_assistant_status_with_options_async(request, runtime)

    def describe_clusters_with_options(
        self,
        request: ecs_20140526_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeClustersResponse().from_map(
            self.do_rpcrequest('DescribeClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_clusters_with_options_async(
        self,
        request: ecs_20140526_models.DescribeClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_clusters(
        self,
        request: ecs_20140526_models.DescribeClustersRequest,
    ) -> ecs_20140526_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    async def describe_clusters_async(
        self,
        request: ecs_20140526_models.DescribeClustersRequest,
    ) -> ecs_20140526_models.DescribeClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_clusters_with_options_async(request, runtime)

    def describe_commands_with_options(
        self,
        request: ecs_20140526_models.DescribeCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCommandsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCommandsResponse().from_map(
            self.do_rpcrequest('DescribeCommands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_commands_with_options_async(
        self,
        request: ecs_20140526_models.DescribeCommandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeCommandsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeCommandsResponse().from_map(
            await self.do_rpcrequest_async('DescribeCommands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_commands(
        self,
        request: ecs_20140526_models.DescribeCommandsRequest,
    ) -> ecs_20140526_models.DescribeCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_commands_with_options(request, runtime)

    async def describe_commands_async(
        self,
        request: ecs_20140526_models.DescribeCommandsRequest,
    ) -> ecs_20140526_models.DescribeCommandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_commands_with_options_async(request, runtime)

    def describe_dedicated_host_auto_renew_with_options(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostAutoRenew', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_auto_renew_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostAutoRenewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostAutoRenew', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_auto_renew(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostAutoRenewRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_auto_renew_with_options(request, runtime)

    async def describe_dedicated_host_auto_renew_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostAutoRenewRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_auto_renew_with_options_async(request, runtime)

    def describe_dedicated_host_clusters_with_options(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostClustersResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_clusters_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_clusters(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostClustersRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_clusters_with_options(request, runtime)

    async def describe_dedicated_host_clusters_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostClustersRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_clusters_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostsResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostsRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostsRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_dedicated_host_types_with_options(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostTypesResponse().from_map(
            self.do_rpcrequest('DescribeDedicatedHostTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_types_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDedicatedHostTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDedicatedHostTypesResponse().from_map(
            await self.do_rpcrequest_async('DescribeDedicatedHostTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_types(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostTypesRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_types_with_options(request, runtime)

    async def describe_dedicated_host_types_async(
        self,
        request: ecs_20140526_models.DescribeDedicatedHostTypesRequest,
    ) -> ecs_20140526_models.DescribeDedicatedHostTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_types_with_options_async(request, runtime)

    def describe_demands_with_options(
        self,
        request: ecs_20140526_models.DescribeDemandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDemandsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDemandsResponse().from_map(
            self.do_rpcrequest('DescribeDemands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_demands_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDemandsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDemandsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDemandsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDemands', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_demands(
        self,
        request: ecs_20140526_models.DescribeDemandsRequest,
    ) -> ecs_20140526_models.DescribeDemandsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_demands_with_options(request, runtime)

    async def describe_demands_async(
        self,
        request: ecs_20140526_models.DescribeDemandsRequest,
    ) -> ecs_20140526_models.DescribeDemandsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_demands_with_options_async(request, runtime)

    def describe_deployment_sets_with_options(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDeploymentSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDeploymentSetsResponse().from_map(
            self.do_rpcrequest('DescribeDeploymentSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_deployment_sets_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDeploymentSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDeploymentSetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeploymentSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployment_sets(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetsRequest,
    ) -> ecs_20140526_models.DescribeDeploymentSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_sets_with_options(request, runtime)

    async def describe_deployment_sets_async(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetsRequest,
    ) -> ecs_20140526_models.DescribeDeploymentSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployment_sets_with_options_async(request, runtime)

    def describe_deployment_set_supported_instance_type_family_with_options(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse().from_map(
            self.do_rpcrequest('DescribeDeploymentSetSupportedInstanceTypeFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_deployment_set_supported_instance_type_family_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse().from_map(
            await self.do_rpcrequest_async('DescribeDeploymentSetSupportedInstanceTypeFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_deployment_set_supported_instance_type_family(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyRequest,
    ) -> ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deployment_set_supported_instance_type_family_with_options(request, runtime)

    async def describe_deployment_set_supported_instance_type_family_async(
        self,
        request: ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyRequest,
    ) -> ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deployment_set_supported_instance_type_family_with_options_async(request, runtime)

    def describe_disk_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDiskMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDiskMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeDiskMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_disk_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDiskMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDiskMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDiskMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeDiskMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disk_monitor_data(
        self,
        request: ecs_20140526_models.DescribeDiskMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeDiskMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disk_monitor_data_with_options(request, runtime)

    async def describe_disk_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeDiskMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeDiskMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disk_monitor_data_with_options_async(request, runtime)

    def describe_disks_with_options(
        self,
        request: ecs_20140526_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDisksResponse().from_map(
            self.do_rpcrequest('DescribeDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_disks_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDisksResponse().from_map(
            await self.do_rpcrequest_async('DescribeDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disks(
        self,
        request: ecs_20140526_models.DescribeDisksRequest,
    ) -> ecs_20140526_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_with_options(request, runtime)

    async def describe_disks_async(
        self,
        request: ecs_20140526_models.DescribeDisksRequest,
    ) -> ecs_20140526_models.DescribeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disks_with_options_async(request, runtime)

    def describe_disks_full_status_with_options(
        self,
        request: ecs_20140526_models.DescribeDisksFullStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDisksFullStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDisksFullStatusResponse().from_map(
            self.do_rpcrequest('DescribeDisksFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_disks_full_status_with_options_async(
        self,
        request: ecs_20140526_models.DescribeDisksFullStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeDisksFullStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeDisksFullStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeDisksFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_disks_full_status(
        self,
        request: ecs_20140526_models.DescribeDisksFullStatusRequest,
    ) -> ecs_20140526_models.DescribeDisksFullStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_disks_full_status_with_options(request, runtime)

    async def describe_disks_full_status_async(
        self,
        request: ecs_20140526_models.DescribeDisksFullStatusRequest,
    ) -> ecs_20140526_models.DescribeDisksFullStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_disks_full_status_with_options_async(request, runtime)

    def describe_eip_addresses_with_options(
        self,
        request: ecs_20140526_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEipAddressesResponse().from_map(
            self.do_rpcrequest('DescribeEipAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_addresses_with_options_async(
        self,
        request: ecs_20140526_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEipAddressesResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_addresses(
        self,
        request: ecs_20140526_models.DescribeEipAddressesRequest,
    ) -> ecs_20140526_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    async def describe_eip_addresses_async(
        self,
        request: ecs_20140526_models.DescribeEipAddressesRequest,
    ) -> ecs_20140526_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_addresses_with_options_async(request, runtime)

    def describe_eip_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEipMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEipMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_monitor_data(
        self,
        request: ecs_20140526_models.DescribeEipMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_monitor_data_with_options(request, runtime)

    async def describe_eip_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeEipMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_monitor_data_with_options_async(request, runtime)

    def describe_elasticity_assurance_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeElasticityAssuranceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse().from_map(
            self.do_rpcrequest('DescribeElasticityAssuranceInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_elasticity_assurance_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeElasticityAssuranceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeElasticityAssuranceInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elasticity_assurance_instances(
        self,
        request: ecs_20140526_models.DescribeElasticityAssuranceInstancesRequest,
    ) -> ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurance_instances_with_options(request, runtime)

    async def describe_elasticity_assurance_instances_async(
        self,
        request: ecs_20140526_models.DescribeElasticityAssuranceInstancesRequest,
    ) -> ecs_20140526_models.DescribeElasticityAssuranceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elasticity_assurance_instances_with_options_async(request, runtime)

    def describe_elasticity_assurances_with_options(
        self,
        request: ecs_20140526_models.DescribeElasticityAssurancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeElasticityAssurancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeElasticityAssurancesResponse().from_map(
            self.do_rpcrequest('DescribeElasticityAssurances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_elasticity_assurances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeElasticityAssurancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeElasticityAssurancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeElasticityAssurancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeElasticityAssurances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_elasticity_assurances(
        self,
        request: ecs_20140526_models.DescribeElasticityAssurancesRequest,
    ) -> ecs_20140526_models.DescribeElasticityAssurancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_elasticity_assurances_with_options(request, runtime)

    async def describe_elasticity_assurances_async(
        self,
        request: ecs_20140526_models.DescribeElasticityAssurancesRequest,
    ) -> ecs_20140526_models.DescribeElasticityAssurancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_elasticity_assurances_with_options_async(request, runtime)

    def describe_eni_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeEniMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEniMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEniMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeEniMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eni_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeEniMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeEniMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeEniMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeEniMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eni_monitor_data(
        self,
        request: ecs_20140526_models.DescribeEniMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeEniMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eni_monitor_data_with_options(request, runtime)

    async def describe_eni_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeEniMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeEniMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eni_monitor_data_with_options_async(request, runtime)

    def describe_forward_table_entries_with_options(
        self,
        request: ecs_20140526_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeForwardTableEntriesResponse().from_map(
            self.do_rpcrequest('DescribeForwardTableEntries', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_forward_table_entries_with_options_async(
        self,
        request: ecs_20140526_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeForwardTableEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeForwardTableEntries', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_forward_table_entries(
        self,
        request: ecs_20140526_models.DescribeForwardTableEntriesRequest,
    ) -> ecs_20140526_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_forward_table_entries_with_options(request, runtime)

    async def describe_forward_table_entries_async(
        self,
        request: ecs_20140526_models.DescribeForwardTableEntriesRequest,
    ) -> ecs_20140526_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_forward_table_entries_with_options_async(request, runtime)

    def describe_ha_vips_with_options(
        self,
        request: ecs_20140526_models.DescribeHaVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeHaVipsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeHaVipsResponse().from_map(
            self.do_rpcrequest('DescribeHaVips', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ha_vips_with_options_async(
        self,
        request: ecs_20140526_models.DescribeHaVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeHaVipsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeHaVipsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHaVips', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ha_vips(
        self,
        request: ecs_20140526_models.DescribeHaVipsRequest,
    ) -> ecs_20140526_models.DescribeHaVipsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ha_vips_with_options(request, runtime)

    async def describe_ha_vips_async(
        self,
        request: ecs_20140526_models.DescribeHaVipsRequest,
    ) -> ecs_20140526_models.DescribeHaVipsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ha_vips_with_options_async(request, runtime)

    def describe_hpc_clusters_with_options(
        self,
        request: ecs_20140526_models.DescribeHpcClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeHpcClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeHpcClustersResponse().from_map(
            self.do_rpcrequest('DescribeHpcClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hpc_clusters_with_options_async(
        self,
        request: ecs_20140526_models.DescribeHpcClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeHpcClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeHpcClustersResponse().from_map(
            await self.do_rpcrequest_async('DescribeHpcClusters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hpc_clusters(
        self,
        request: ecs_20140526_models.DescribeHpcClustersRequest,
    ) -> ecs_20140526_models.DescribeHpcClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hpc_clusters_with_options(request, runtime)

    async def describe_hpc_clusters_async(
        self,
        request: ecs_20140526_models.DescribeHpcClustersRequest,
    ) -> ecs_20140526_models.DescribeHpcClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hpc_clusters_with_options_async(request, runtime)

    def describe_image_components_with_options(
        self,
        request: ecs_20140526_models.DescribeImageComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageComponentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageComponentsResponse().from_map(
            self.do_rpcrequest('DescribeImageComponents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_components_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImageComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageComponentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageComponentsResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageComponents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_components(
        self,
        request: ecs_20140526_models.DescribeImageComponentsRequest,
    ) -> ecs_20140526_models.DescribeImageComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_components_with_options(request, runtime)

    async def describe_image_components_async(
        self,
        request: ecs_20140526_models.DescribeImageComponentsRequest,
    ) -> ecs_20140526_models.DescribeImageComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_components_with_options_async(request, runtime)

    def describe_image_from_family_with_options(
        self,
        request: ecs_20140526_models.DescribeImageFromFamilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageFromFamilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageFromFamilyResponse().from_map(
            self.do_rpcrequest('DescribeImageFromFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_from_family_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImageFromFamilyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageFromFamilyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageFromFamilyResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageFromFamily', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_from_family(
        self,
        request: ecs_20140526_models.DescribeImageFromFamilyRequest,
    ) -> ecs_20140526_models.DescribeImageFromFamilyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_from_family_with_options(request, runtime)

    async def describe_image_from_family_async(
        self,
        request: ecs_20140526_models.DescribeImageFromFamilyRequest,
    ) -> ecs_20140526_models.DescribeImageFromFamilyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_from_family_with_options_async(request, runtime)

    def describe_image_pipeline_executions_with_options(
        self,
        request: ecs_20140526_models.DescribeImagePipelineExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagePipelineExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagePipelineExecutionsResponse().from_map(
            self.do_rpcrequest('DescribeImagePipelineExecutions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_pipeline_executions_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImagePipelineExecutionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagePipelineExecutionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagePipelineExecutionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeImagePipelineExecutions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_pipeline_executions(
        self,
        request: ecs_20140526_models.DescribeImagePipelineExecutionsRequest,
    ) -> ecs_20140526_models.DescribeImagePipelineExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipeline_executions_with_options(request, runtime)

    async def describe_image_pipeline_executions_async(
        self,
        request: ecs_20140526_models.DescribeImagePipelineExecutionsRequest,
    ) -> ecs_20140526_models.DescribeImagePipelineExecutionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_pipeline_executions_with_options_async(request, runtime)

    def describe_image_pipelines_with_options(
        self,
        request: ecs_20140526_models.DescribeImagePipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagePipelinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagePipelinesResponse().from_map(
            self.do_rpcrequest('DescribeImagePipelines', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_pipelines_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImagePipelinesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagePipelinesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagePipelinesResponse().from_map(
            await self.do_rpcrequest_async('DescribeImagePipelines', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_pipelines(
        self,
        request: ecs_20140526_models.DescribeImagePipelinesRequest,
    ) -> ecs_20140526_models.DescribeImagePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_pipelines_with_options(request, runtime)

    async def describe_image_pipelines_async(
        self,
        request: ecs_20140526_models.DescribeImagePipelinesRequest,
    ) -> ecs_20140526_models.DescribeImagePipelinesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_pipelines_with_options_async(request, runtime)

    def describe_images_with_options(
        self,
        request: ecs_20140526_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagesResponse().from_map(
            self.do_rpcrequest('DescribeImages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_images_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeImages', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_images(
        self,
        request: ecs_20140526_models.DescribeImagesRequest,
    ) -> ecs_20140526_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    async def describe_images_async(
        self,
        request: ecs_20140526_models.DescribeImagesRequest,
    ) -> ecs_20140526_models.DescribeImagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_images_with_options_async(request, runtime)

    def describe_image_share_permission_with_options(
        self,
        request: ecs_20140526_models.DescribeImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageSharePermissionResponse().from_map(
            self.do_rpcrequest('DescribeImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_share_permission_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageSharePermissionResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_share_permission(
        self,
        request: ecs_20140526_models.DescribeImageSharePermissionRequest,
    ) -> ecs_20140526_models.DescribeImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_share_permission_with_options(request, runtime)

    async def describe_image_share_permission_async(
        self,
        request: ecs_20140526_models.DescribeImageSharePermissionRequest,
    ) -> ecs_20140526_models.DescribeImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_share_permission_with_options_async(request, runtime)

    def describe_image_support_instance_types_with_options(
        self,
        request: ecs_20140526_models.DescribeImageSupportInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageSupportInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageSupportInstanceTypesResponse().from_map(
            self.do_rpcrequest('DescribeImageSupportInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_image_support_instance_types_with_options_async(
        self,
        request: ecs_20140526_models.DescribeImageSupportInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeImageSupportInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeImageSupportInstanceTypesResponse().from_map(
            await self.do_rpcrequest_async('DescribeImageSupportInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_image_support_instance_types(
        self,
        request: ecs_20140526_models.DescribeImageSupportInstanceTypesRequest,
    ) -> ecs_20140526_models.DescribeImageSupportInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_image_support_instance_types_with_options(request, runtime)

    async def describe_image_support_instance_types_async(
        self,
        request: ecs_20140526_models.DescribeImageSupportInstanceTypesRequest,
    ) -> ecs_20140526_models.DescribeImageSupportInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_image_support_instance_types_with_options_async(request, runtime)

    def describe_instance_attachment_attributes_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attachment_attributes_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attachment_attributes(
        self,
        request: ecs_20140526_models.DescribeInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attachment_attributes_with_options(request, runtime)

    async def describe_instance_attachment_attributes_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.DescribeInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attachment_attributes_with_options_async(request, runtime)

    def describe_instance_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_attribute(
        self,
        request: ecs_20140526_models.DescribeInstanceAttributeRequest,
    ) -> ecs_20140526_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    async def describe_instance_attribute_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAttributeRequest,
    ) -> ecs_20140526_models.DescribeInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_attribute_with_options_async(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renew_attribute(
        self,
        request: ecs_20140526_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    async def describe_instance_auto_renew_attribute_async(
        self,
        request: ecs_20140526_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renew_attribute_with_options_async(request, runtime)

    def describe_instance_history_events_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceHistoryEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceHistoryEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceHistoryEventsResponse().from_map(
            self.do_rpcrequest('DescribeInstanceHistoryEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_history_events_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceHistoryEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceHistoryEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceHistoryEventsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceHistoryEvents', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_history_events(
        self,
        request: ecs_20140526_models.DescribeInstanceHistoryEventsRequest,
    ) -> ecs_20140526_models.DescribeInstanceHistoryEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_history_events_with_options(request, runtime)

    async def describe_instance_history_events_async(
        self,
        request: ecs_20140526_models.DescribeInstanceHistoryEventsRequest,
    ) -> ecs_20140526_models.DescribeInstanceHistoryEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_history_events_with_options_async(request, runtime)

    def describe_instance_maintenance_attributes_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_maintenance_attributes_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_maintenance_attributes(
        self,
        request: ecs_20140526_models.DescribeInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_maintenance_attributes_with_options(request, runtime)

    async def describe_instance_maintenance_attributes_async(
        self,
        request: ecs_20140526_models.DescribeInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_maintenance_attributes_with_options_async(request, runtime)

    def describe_instance_modification_price_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceModificationPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceModificationPriceResponse().from_map(
            self.do_rpcrequest('DescribeInstanceModificationPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_modification_price_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceModificationPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceModificationPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceModificationPriceResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceModificationPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_modification_price(
        self,
        request: ecs_20140526_models.DescribeInstanceModificationPriceRequest,
    ) -> ecs_20140526_models.DescribeInstanceModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_modification_price_with_options(request, runtime)

    async def describe_instance_modification_price_async(
        self,
        request: ecs_20140526_models.DescribeInstanceModificationPriceRequest,
    ) -> ecs_20140526_models.DescribeInstanceModificationPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_modification_price_with_options_async(request, runtime)

    def describe_instance_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeInstanceMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_monitor_data(
        self,
        request: ecs_20140526_models.DescribeInstanceMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeInstanceMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_monitor_data_with_options(request, runtime)

    async def describe_instance_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeInstanceMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeInstanceMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_monitor_data_with_options_async(request, runtime)

    def describe_instance_ram_role_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceRamRoleResponse().from_map(
            self.do_rpcrequest('DescribeInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_ram_role_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceRamRoleResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_ram_role(
        self,
        request: ecs_20140526_models.DescribeInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DescribeInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_ram_role_with_options(request, runtime)

    async def describe_instance_ram_role_async(
        self,
        request: ecs_20140526_models.DescribeInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DescribeInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_ram_role_with_options_async(request, runtime)

    def describe_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstancesResponse().from_map(
            self.do_rpcrequest('DescribeInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances(
        self,
        request: ecs_20140526_models.DescribeInstancesRequest,
    ) -> ecs_20140526_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    async def describe_instances_async(
        self,
        request: ecs_20140526_models.DescribeInstancesRequest,
    ) -> ecs_20140526_models.DescribeInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_with_options_async(request, runtime)

    def describe_instances_full_status_with_options(
        self,
        request: ecs_20140526_models.DescribeInstancesFullStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstancesFullStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstancesFullStatusResponse().from_map(
            self.do_rpcrequest('DescribeInstancesFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instances_full_status_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstancesFullStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstancesFullStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstancesFullStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstancesFullStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instances_full_status(
        self,
        request: ecs_20140526_models.DescribeInstancesFullStatusRequest,
    ) -> ecs_20140526_models.DescribeInstancesFullStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_full_status_with_options(request, runtime)

    async def describe_instances_full_status_async(
        self,
        request: ecs_20140526_models.DescribeInstancesFullStatusRequest,
    ) -> ecs_20140526_models.DescribeInstancesFullStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instances_full_status_with_options_async(request, runtime)

    def describe_instance_status_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceStatusResponse().from_map(
            self.do_rpcrequest('DescribeInstanceStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_status_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceStatusResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_status(
        self,
        request: ecs_20140526_models.DescribeInstanceStatusRequest,
    ) -> ecs_20140526_models.DescribeInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_status_with_options(request, runtime)

    async def describe_instance_status_async(
        self,
        request: ecs_20140526_models.DescribeInstanceStatusRequest,
    ) -> ecs_20140526_models.DescribeInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_status_with_options_async(request, runtime)

    def describe_instance_topology_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTopologyResponse().from_map(
            self.do_rpcrequest('DescribeInstanceTopology', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_topology_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTopologyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTopologyResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceTopology', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_topology(
        self,
        request: ecs_20140526_models.DescribeInstanceTopologyRequest,
    ) -> ecs_20140526_models.DescribeInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_topology_with_options(request, runtime)

    async def describe_instance_topology_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTopologyRequest,
    ) -> ecs_20140526_models.DescribeInstanceTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_topology_with_options_async(request, runtime)

    def describe_instance_type_families_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceTypeFamiliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTypeFamiliesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTypeFamiliesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceTypeFamilies', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_type_families_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTypeFamiliesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTypeFamiliesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTypeFamiliesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceTypeFamilies', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_type_families(
        self,
        request: ecs_20140526_models.DescribeInstanceTypeFamiliesRequest,
    ) -> ecs_20140526_models.DescribeInstanceTypeFamiliesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_type_families_with_options(request, runtime)

    async def describe_instance_type_families_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTypeFamiliesRequest,
    ) -> ecs_20140526_models.DescribeInstanceTypeFamiliesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_type_families_with_options_async(request, runtime)

    def describe_instance_types_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTypesResponse().from_map(
            self.do_rpcrequest('DescribeInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_types_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceTypesResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceTypes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_types(
        self,
        request: ecs_20140526_models.DescribeInstanceTypesRequest,
    ) -> ecs_20140526_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    async def describe_instance_types_async(
        self,
        request: ecs_20140526_models.DescribeInstanceTypesRequest,
    ) -> ecs_20140526_models.DescribeInstanceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_types_with_options_async(request, runtime)

    def describe_instance_vnc_passwd_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceVncPasswdResponse().from_map(
            self.do_rpcrequest('DescribeInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_vnc_passwd_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceVncPasswdResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_vnc_passwd(
        self,
        request: ecs_20140526_models.DescribeInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.DescribeInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_passwd_with_options(request, runtime)

    async def describe_instance_vnc_passwd_async(
        self,
        request: ecs_20140526_models.DescribeInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.DescribeInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_vnc_passwd_with_options_async(request, runtime)

    def describe_instance_vnc_url_with_options(
        self,
        request: ecs_20140526_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceVncUrlResponse().from_map(
            self.do_rpcrequest('DescribeInstanceVncUrl', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_vnc_url_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInstanceVncUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInstanceVncUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInstanceVncUrlResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceVncUrl', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_vnc_url(
        self,
        request: ecs_20140526_models.DescribeInstanceVncUrlRequest,
    ) -> ecs_20140526_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_vnc_url_with_options(request, runtime)

    async def describe_instance_vnc_url_async(
        self,
        request: ecs_20140526_models.DescribeInstanceVncUrlRequest,
    ) -> ecs_20140526_models.DescribeInstanceVncUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_vnc_url_with_options_async(request, runtime)

    def describe_invocation_results_with_options(
        self,
        request: ecs_20140526_models.DescribeInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInvocationResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInvocationResultsResponse().from_map(
            self.do_rpcrequest('DescribeInvocationResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_invocation_results_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInvocationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInvocationResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInvocationResultsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInvocationResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocation_results(
        self,
        request: ecs_20140526_models.DescribeInvocationResultsRequest,
    ) -> ecs_20140526_models.DescribeInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_results_with_options(request, runtime)

    async def describe_invocation_results_async(
        self,
        request: ecs_20140526_models.DescribeInvocationResultsRequest,
    ) -> ecs_20140526_models.DescribeInvocationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocation_results_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: ecs_20140526_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInvocationsResponse().from_map(
            self.do_rpcrequest('DescribeInvocations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: ecs_20140526_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeInvocationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeInvocationsResponse().from_map(
            await self.do_rpcrequest_async('DescribeInvocations', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocations(
        self,
        request: ecs_20140526_models.DescribeInvocationsRequest,
    ) -> ecs_20140526_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: ecs_20140526_models.DescribeInvocationsRequest,
    ) -> ecs_20140526_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_key_pairs_with_options(
        self,
        request: ecs_20140526_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeKeyPairsResponse().from_map(
            self.do_rpcrequest('DescribeKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_key_pairs_with_options_async(
        self,
        request: ecs_20140526_models.DescribeKeyPairsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeKeyPairsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeKeyPairsResponse().from_map(
            await self.do_rpcrequest_async('DescribeKeyPairs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_key_pairs(
        self,
        request: ecs_20140526_models.DescribeKeyPairsRequest,
    ) -> ecs_20140526_models.DescribeKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    async def describe_key_pairs_async(
        self,
        request: ecs_20140526_models.DescribeKeyPairsRequest,
    ) -> ecs_20140526_models.DescribeKeyPairsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_key_pairs_with_options_async(request, runtime)

    def describe_launch_templates_with_options(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLaunchTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLaunchTemplatesResponse().from_map(
            self.do_rpcrequest('DescribeLaunchTemplates', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_launch_templates_with_options_async(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLaunchTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLaunchTemplatesResponse().from_map(
            await self.do_rpcrequest_async('DescribeLaunchTemplates', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_launch_templates(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplatesRequest,
    ) -> ecs_20140526_models.DescribeLaunchTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_templates_with_options(request, runtime)

    async def describe_launch_templates_async(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplatesRequest,
    ) -> ecs_20140526_models.DescribeLaunchTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_launch_templates_with_options_async(request, runtime)

    def describe_launch_template_versions_with_options(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLaunchTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLaunchTemplateVersionsResponse().from_map(
            self.do_rpcrequest('DescribeLaunchTemplateVersions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_launch_template_versions_with_options_async(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLaunchTemplateVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLaunchTemplateVersionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeLaunchTemplateVersions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_launch_template_versions(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplateVersionsRequest,
    ) -> ecs_20140526_models.DescribeLaunchTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_launch_template_versions_with_options(request, runtime)

    async def describe_launch_template_versions_async(
        self,
        request: ecs_20140526_models.DescribeLaunchTemplateVersionsRequest,
    ) -> ecs_20140526_models.DescribeLaunchTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_launch_template_versions_with_options_async(request, runtime)

    def describe_limitation_with_options(
        self,
        request: ecs_20140526_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLimitationResponse().from_map(
            self.do_rpcrequest('DescribeLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_limitation_with_options_async(
        self,
        request: ecs_20140526_models.DescribeLimitationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeLimitationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeLimitationResponse().from_map(
            await self.do_rpcrequest_async('DescribeLimitation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_limitation(
        self,
        request: ecs_20140526_models.DescribeLimitationRequest,
    ) -> ecs_20140526_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_limitation_with_options(request, runtime)

    async def describe_limitation_async(
        self,
        request: ecs_20140526_models.DescribeLimitationRequest,
    ) -> ecs_20140526_models.DescribeLimitationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_limitation_with_options_async(request, runtime)

    def describe_managed_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeManagedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeManagedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeManagedInstancesResponse().from_map(
            self.do_rpcrequest('DescribeManagedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_managed_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeManagedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeManagedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeManagedInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeManagedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_managed_instances(
        self,
        request: ecs_20140526_models.DescribeManagedInstancesRequest,
    ) -> ecs_20140526_models.DescribeManagedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_managed_instances_with_options(request, runtime)

    async def describe_managed_instances_async(
        self,
        request: ecs_20140526_models.DescribeManagedInstancesRequest,
    ) -> ecs_20140526_models.DescribeManagedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_managed_instances_with_options_async(request, runtime)

    def describe_nat_gateways_with_options(
        self,
        request: ecs_20140526_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNatGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeNatGateways', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_nat_gateways_with_options_async(
        self,
        request: ecs_20140526_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNatGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeNatGateways', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_nat_gateways(
        self,
        request: ecs_20140526_models.DescribeNatGatewaysRequest,
    ) -> ecs_20140526_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_gateways_with_options(request, runtime)

    async def describe_nat_gateways_async(
        self,
        request: ecs_20140526_models.DescribeNatGatewaysRequest,
    ) -> ecs_20140526_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_gateways_with_options_async(request, runtime)

    def describe_network_interface_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_interface_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interface_attribute(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_attribute_with_options(request, runtime)

    async def describe_network_interface_attribute_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_interface_attribute_with_options_async(request, runtime)

    def describe_network_interface_permissions_with_options(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse().from_map(
            self.do_rpcrequest('DescribeNetworkInterfacePermissions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_interface_permissions_with_options_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacePermissionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkInterfacePermissions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interface_permissions(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacePermissionsRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interface_permissions_with_options(request, runtime)

    async def describe_network_interface_permissions_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacePermissionsRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_interface_permissions_with_options_async(request, runtime)

    def describe_network_interfaces_with_options(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfacesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_interfaces_with_options_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNetworkInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNetworkInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_interfaces(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacesRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interfaces_with_options(request, runtime)

    async def describe_network_interfaces_async(
        self,
        request: ecs_20140526_models.DescribeNetworkInterfacesRequest,
    ) -> ecs_20140526_models.DescribeNetworkInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_interfaces_with_options_async(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeNewProjectEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeNewProjectEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_new_project_eip_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeNewProjectEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeNewProjectEipMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_new_project_eip_monitor_data(
        self,
        request: ecs_20140526_models.DescribeNewProjectEipMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    async def describe_new_project_eip_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeNewProjectEipMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_new_project_eip_monitor_data_with_options_async(request, runtime)

    def describe_physical_connections_with_options(
        self,
        request: ecs_20140526_models.DescribePhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribePhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribePhysicalConnectionsResponse().from_map(
            self.do_rpcrequest('DescribePhysicalConnections', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_physical_connections_with_options_async(
        self,
        request: ecs_20140526_models.DescribePhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribePhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribePhysicalConnectionsResponse().from_map(
            await self.do_rpcrequest_async('DescribePhysicalConnections', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_physical_connections(
        self,
        request: ecs_20140526_models.DescribePhysicalConnectionsRequest,
    ) -> ecs_20140526_models.DescribePhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_physical_connections_with_options(request, runtime)

    async def describe_physical_connections_async(
        self,
        request: ecs_20140526_models.DescribePhysicalConnectionsRequest,
    ) -> ecs_20140526_models.DescribePhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_physical_connections_with_options_async(request, runtime)

    def describe_price_with_options(
        self,
        request: ecs_20140526_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribePriceResponse().from_map(
            self.do_rpcrequest('DescribePrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_price_with_options_async(
        self,
        request: ecs_20140526_models.DescribePriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribePriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribePriceResponse().from_map(
            await self.do_rpcrequest_async('DescribePrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_price(
        self,
        request: ecs_20140526_models.DescribePriceRequest,
    ) -> ecs_20140526_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    async def describe_price_async(
        self,
        request: ecs_20140526_models.DescribePriceRequest,
    ) -> ecs_20140526_models.DescribePriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_price_with_options_async(request, runtime)

    def describe_recommend_instance_type_with_options(
        self,
        request: ecs_20140526_models.DescribeRecommendInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRecommendInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRecommendInstanceTypeResponse().from_map(
            self.do_rpcrequest('DescribeRecommendInstanceType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_recommend_instance_type_with_options_async(
        self,
        request: ecs_20140526_models.DescribeRecommendInstanceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRecommendInstanceTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRecommendInstanceTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeRecommendInstanceType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recommend_instance_type(
        self,
        request: ecs_20140526_models.DescribeRecommendInstanceTypeRequest,
    ) -> ecs_20140526_models.DescribeRecommendInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recommend_instance_type_with_options(request, runtime)

    async def describe_recommend_instance_type_async(
        self,
        request: ecs_20140526_models.DescribeRecommendInstanceTypeRequest,
    ) -> ecs_20140526_models.DescribeRecommendInstanceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recommend_instance_type_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ecs_20140526_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ecs_20140526_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ecs_20140526_models.DescribeRegionsRequest,
    ) -> ecs_20140526_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ecs_20140526_models.DescribeRegionsRequest,
    ) -> ecs_20140526_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_renewal_price_with_options(
        self,
        request: ecs_20140526_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRenewalPriceResponse().from_map(
            self.do_rpcrequest('DescribeRenewalPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_renewal_price_with_options_async(
        self,
        request: ecs_20140526_models.DescribeRenewalPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRenewalPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRenewalPriceResponse().from_map(
            await self.do_rpcrequest_async('DescribeRenewalPrice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_renewal_price(
        self,
        request: ecs_20140526_models.DescribeRenewalPriceRequest,
    ) -> ecs_20140526_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    async def describe_renewal_price_async(
        self,
        request: ecs_20140526_models.DescribeRenewalPriceRequest,
    ) -> ecs_20140526_models.DescribeRenewalPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_renewal_price_with_options_async(request, runtime)

    def describe_reserved_instances_with_options(
        self,
        request: ecs_20140526_models.DescribeReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeReservedInstancesResponse().from_map(
            self.do_rpcrequest('DescribeReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_reserved_instances_with_options_async(
        self,
        request: ecs_20140526_models.DescribeReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeReservedInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_reserved_instances(
        self,
        request: ecs_20140526_models.DescribeReservedInstancesRequest,
    ) -> ecs_20140526_models.DescribeReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_instances_with_options(request, runtime)

    async def describe_reserved_instances_async(
        self,
        request: ecs_20140526_models.DescribeReservedInstancesRequest,
    ) -> ecs_20140526_models.DescribeReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_reserved_instances_with_options_async(request, runtime)

    def describe_resource_by_tags_with_options(
        self,
        request: ecs_20140526_models.DescribeResourceByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeResourceByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeResourceByTagsResponse().from_map(
            self.do_rpcrequest('DescribeResourceByTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resource_by_tags_with_options_async(
        self,
        request: ecs_20140526_models.DescribeResourceByTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeResourceByTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeResourceByTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeResourceByTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resource_by_tags(
        self,
        request: ecs_20140526_models.DescribeResourceByTagsRequest,
    ) -> ecs_20140526_models.DescribeResourceByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_by_tags_with_options(request, runtime)

    async def describe_resource_by_tags_async(
        self,
        request: ecs_20140526_models.DescribeResourceByTagsRequest,
    ) -> ecs_20140526_models.DescribeResourceByTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resource_by_tags_with_options_async(request, runtime)

    def describe_resources_modification_with_options(
        self,
        request: ecs_20140526_models.DescribeResourcesModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeResourcesModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeResourcesModificationResponse().from_map(
            self.do_rpcrequest('DescribeResourcesModification', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_resources_modification_with_options_async(
        self,
        request: ecs_20140526_models.DescribeResourcesModificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeResourcesModificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeResourcesModificationResponse().from_map(
            await self.do_rpcrequest_async('DescribeResourcesModification', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_resources_modification(
        self,
        request: ecs_20140526_models.DescribeResourcesModificationRequest,
    ) -> ecs_20140526_models.DescribeResourcesModificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_resources_modification_with_options(request, runtime)

    async def describe_resources_modification_async(
        self,
        request: ecs_20140526_models.DescribeResourcesModificationRequest,
    ) -> ecs_20140526_models.DescribeResourcesModificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_resources_modification_with_options_async(request, runtime)

    def describe_router_interfaces_with_options(
        self,
        request: ecs_20140526_models.DescribeRouterInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRouterInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRouterInterfacesResponse().from_map(
            self.do_rpcrequest('DescribeRouterInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_router_interfaces_with_options_async(
        self,
        request: ecs_20140526_models.DescribeRouterInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRouterInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRouterInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouterInterfaces', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_router_interfaces(
        self,
        request: ecs_20140526_models.DescribeRouterInterfacesRequest,
    ) -> ecs_20140526_models.DescribeRouterInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_router_interfaces_with_options(request, runtime)

    async def describe_router_interfaces_async(
        self,
        request: ecs_20140526_models.DescribeRouterInterfacesRequest,
    ) -> ecs_20140526_models.DescribeRouterInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_router_interfaces_with_options_async(request, runtime)

    def describe_route_tables_with_options(
        self,
        request: ecs_20140526_models.DescribeRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRouteTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRouteTablesResponse().from_map(
            self.do_rpcrequest('DescribeRouteTables', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_tables_with_options_async(
        self,
        request: ecs_20140526_models.DescribeRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeRouteTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeRouteTablesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouteTables', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_tables(
        self,
        request: ecs_20140526_models.DescribeRouteTablesRequest,
    ) -> ecs_20140526_models.DescribeRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_tables_with_options(request, runtime)

    async def describe_route_tables_async(
        self,
        request: ecs_20140526_models.DescribeRouteTablesRequest,
    ) -> ecs_20140526_models.DescribeRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_tables_with_options_async(request, runtime)

    def describe_security_group_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_attribute(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    async def describe_security_group_attribute_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_attribute_with_options_async(request, runtime)

    def describe_security_group_references_with_options(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupReferencesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupReferencesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupReferencesResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupReferences', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_references_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupReferencesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupReferencesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupReferencesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupReferences', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_references(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupReferencesRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupReferencesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_references_with_options(request, runtime)

    async def describe_security_group_references_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupReferencesRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupReferencesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_references_with_options_async(request, runtime)

    def describe_security_groups_with_options(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupsResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_groups_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSecurityGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSecurityGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_groups(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupsRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    async def describe_security_groups_async(
        self,
        request: ecs_20140526_models.DescribeSecurityGroupsRequest,
    ) -> ecs_20140526_models.DescribeSecurityGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_groups_with_options_async(request, runtime)

    def describe_send_file_results_with_options(
        self,
        request: ecs_20140526_models.DescribeSendFileResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSendFileResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSendFileResultsResponse().from_map(
            self.do_rpcrequest('DescribeSendFileResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_send_file_results_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSendFileResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSendFileResultsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSendFileResultsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSendFileResults', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_send_file_results(
        self,
        request: ecs_20140526_models.DescribeSendFileResultsRequest,
    ) -> ecs_20140526_models.DescribeSendFileResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    async def describe_send_file_results_async(
        self,
        request: ecs_20140526_models.DescribeSendFileResultsRequest,
    ) -> ecs_20140526_models.DescribeSendFileResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_send_file_results_with_options_async(request, runtime)

    def describe_snapshot_groups_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotGroupsResponse().from_map(
            self.do_rpcrequest('DescribeSnapshotGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshot_groups_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshotGroups', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_groups(
        self,
        request: ecs_20140526_models.DescribeSnapshotGroupsRequest,
    ) -> ecs_20140526_models.DescribeSnapshotGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_groups_with_options(request, runtime)

    async def describe_snapshot_groups_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotGroupsRequest,
    ) -> ecs_20140526_models.DescribeSnapshotGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshot_groups_with_options_async(request, runtime)

    def describe_snapshot_links_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotLinksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotLinksResponse().from_map(
            self.do_rpcrequest('DescribeSnapshotLinks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshot_links_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotLinksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotLinksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotLinksResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshotLinks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_links(
        self,
        request: ecs_20140526_models.DescribeSnapshotLinksRequest,
    ) -> ecs_20140526_models.DescribeSnapshotLinksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_links_with_options(request, runtime)

    async def describe_snapshot_links_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotLinksRequest,
    ) -> ecs_20140526_models.DescribeSnapshotLinksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshot_links_with_options_async(request, runtime)

    def describe_snapshot_monitor_data_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeSnapshotMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshot_monitor_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshotMonitorData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_monitor_data(
        self,
        request: ecs_20140526_models.DescribeSnapshotMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeSnapshotMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_monitor_data_with_options(request, runtime)

    async def describe_snapshot_monitor_data_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotMonitorDataRequest,
    ) -> ecs_20140526_models.DescribeSnapshotMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshot_monitor_data_with_options_async(request, runtime)

    def describe_snapshot_package_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotPackageResponse().from_map(
            self.do_rpcrequest('DescribeSnapshotPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshot_package_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotPackageResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshotPackage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshot_package(
        self,
        request: ecs_20140526_models.DescribeSnapshotPackageRequest,
    ) -> ecs_20140526_models.DescribeSnapshotPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshot_package_with_options(request, runtime)

    async def describe_snapshot_package_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotPackageRequest,
    ) -> ecs_20140526_models.DescribeSnapshotPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshot_package_with_options_async(request, runtime)

    def describe_snapshots_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotsResponse().from_map(
            self.do_rpcrequest('DescribeSnapshots', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshots_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshots', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots(
        self,
        request: ecs_20140526_models.DescribeSnapshotsRequest,
    ) -> ecs_20140526_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_with_options(request, runtime)

    async def describe_snapshots_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotsRequest,
    ) -> ecs_20140526_models.DescribeSnapshotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_with_options_async(request, runtime)

    def describe_snapshots_usage_with_options(
        self,
        request: ecs_20140526_models.DescribeSnapshotsUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotsUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotsUsageResponse().from_map(
            self.do_rpcrequest('DescribeSnapshotsUsage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snapshots_usage_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotsUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSnapshotsUsageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSnapshotsUsageResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnapshotsUsage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snapshots_usage(
        self,
        request: ecs_20140526_models.DescribeSnapshotsUsageRequest,
    ) -> ecs_20140526_models.DescribeSnapshotsUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snapshots_usage_with_options(request, runtime)

    async def describe_snapshots_usage_async(
        self,
        request: ecs_20140526_models.DescribeSnapshotsUsageRequest,
    ) -> ecs_20140526_models.DescribeSnapshotsUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snapshots_usage_with_options_async(request, runtime)

    def describe_spot_advice_with_options(
        self,
        request: ecs_20140526_models.DescribeSpotAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotAdviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotAdviceResponse().from_map(
            self.do_rpcrequest('DescribeSpotAdvice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_spot_advice_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSpotAdviceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotAdviceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotAdviceResponse().from_map(
            await self.do_rpcrequest_async('DescribeSpotAdvice', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_spot_advice(
        self,
        request: ecs_20140526_models.DescribeSpotAdviceRequest,
    ) -> ecs_20140526_models.DescribeSpotAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_advice_with_options(request, runtime)

    async def describe_spot_advice_async(
        self,
        request: ecs_20140526_models.DescribeSpotAdviceRequest,
    ) -> ecs_20140526_models.DescribeSpotAdviceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spot_advice_with_options_async(request, runtime)

    def describe_spot_price_history_with_options(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotPriceHistoryResponse().from_map(
            self.do_rpcrequest('DescribeSpotPriceHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_spot_price_history_with_options_async(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeSpotPriceHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeSpotPriceHistory', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_spot_price_history(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_spot_price_history_with_options(request, runtime)

    async def describe_spot_price_history_async(
        self,
        request: ecs_20140526_models.DescribeSpotPriceHistoryRequest,
    ) -> ecs_20140526_models.DescribeSpotPriceHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_spot_price_history_with_options_async(request, runtime)

    def describe_storage_capacity_units_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageCapacityUnitsResponse().from_map(
            self.do_rpcrequest('DescribeStorageCapacityUnits', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_capacity_units_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageCapacityUnitsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageCapacityUnits', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_capacity_units(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_capacity_units_with_options(request, runtime)

    async def describe_storage_capacity_units_async(
        self,
        request: ecs_20140526_models.DescribeStorageCapacityUnitsRequest,
    ) -> ecs_20140526_models.DescribeStorageCapacityUnitsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_capacity_units_with_options_async(request, runtime)

    def describe_storage_set_details_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetDetailsResponse().from_map(
            self.do_rpcrequest('DescribeStorageSetDetails', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_set_details_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetDetailsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageSetDetails', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_set_details(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_set_details_with_options(request, runtime)

    async def describe_storage_set_details_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetDetailsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetDetailsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_set_details_with_options_async(request, runtime)

    def describe_storage_sets_with_options(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetsResponse().from_map(
            self.do_rpcrequest('DescribeStorageSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_storage_sets_with_options_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeStorageSetsResponse().from_map(
            await self.do_rpcrequest_async('DescribeStorageSets', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_storage_sets(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_storage_sets_with_options(request, runtime)

    async def describe_storage_sets_async(
        self,
        request: ecs_20140526_models.DescribeStorageSetsRequest,
    ) -> ecs_20140526_models.DescribeStorageSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_storage_sets_with_options_async(request, runtime)

    def describe_tags_with_options(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTagsResponse().from_map(
            self.do_rpcrequest('DescribeTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tags_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTagsResponse().from_map(
            await self.do_rpcrequest_async('DescribeTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    async def describe_tags_async(
        self,
        request: ecs_20140526_models.DescribeTagsRequest,
    ) -> ecs_20140526_models.DescribeTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tags_with_options_async(request, runtime)

    def describe_task_attribute_with_options(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTaskAttributeResponse().from_map(
            self.do_rpcrequest('DescribeTaskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_task_attribute_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTaskAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeTaskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_task_attribute(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_task_attribute_with_options(request, runtime)

    async def describe_task_attribute_async(
        self,
        request: ecs_20140526_models.DescribeTaskAttributeRequest,
    ) -> ecs_20140526_models.DescribeTaskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_attribute_with_options_async(request, runtime)

    def describe_tasks_with_options(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTasksResponse().from_map(
            self.do_rpcrequest('DescribeTasks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tasks_with_options_async(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeTasksResponse().from_map(
            await self.do_rpcrequest_async('DescribeTasks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tasks(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    async def describe_tasks_async(
        self,
        request: ecs_20140526_models.DescribeTasksRequest,
    ) -> ecs_20140526_models.DescribeTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tasks_with_options_async(request, runtime)

    def describe_user_business_behavior_with_options(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserBusinessBehaviorResponse().from_map(
            self.do_rpcrequest('DescribeUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_business_behavior_with_options_async(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserBusinessBehaviorResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_business_behavior(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_business_behavior_with_options(request, runtime)

    async def describe_user_business_behavior_async(
        self,
        request: ecs_20140526_models.DescribeUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.DescribeUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_business_behavior_with_options_async(request, runtime)

    def describe_user_data_with_options(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserDataResponse().from_map(
            self.do_rpcrequest('DescribeUserData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_user_data_with_options_async(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeUserDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeUserData', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_user_data(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_user_data_with_options(request, runtime)

    async def describe_user_data_async(
        self,
        request: ecs_20140526_models.DescribeUserDataRequest,
    ) -> ecs_20140526_models.DescribeUserDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_user_data_with_options_async(request, runtime)

    def describe_virtual_border_routers_with_options(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_with_options(request, runtime)

    async def describe_virtual_border_routers_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_with_options_async(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRoutersForPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_for_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRoutersForPhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers_for_physical_connection(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    async def describe_virtual_border_routers_for_physical_connection_async(
        self,
        request: ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_for_physical_connection_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVpcsResponse().from_map(
            self.do_rpcrequest('DescribeVpcs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVpcsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcs', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: ecs_20140526_models.DescribeVpcsRequest,
    ) -> ecs_20140526_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_vrouters_with_options(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vrouters_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVRouters', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vrouters(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vrouters_with_options(request, runtime)

    async def describe_vrouters_async(
        self,
        request: ecs_20140526_models.DescribeVRoutersRequest,
    ) -> ecs_20140526_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vrouters_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVSwitchesResponse().from_map(
            self.do_rpcrequest('DescribeVSwitches', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeVSwitchesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVSwitches', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: ecs_20140526_models.DescribeVSwitchesRequest,
    ) -> ecs_20140526_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DescribeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeZones', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: ecs_20140526_models.DescribeZonesRequest,
    ) -> ecs_20140526_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_classic_link_vpc_with_options(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachClassicLinkVpcResponse().from_map(
            self.do_rpcrequest('DetachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_classic_link_vpc_with_options_async(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachClassicLinkVpcResponse().from_map(
            await self.do_rpcrequest_async('DetachClassicLinkVpc', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_classic_link_vpc(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_classic_link_vpc_with_options(request, runtime)

    async def detach_classic_link_vpc_async(
        self,
        request: ecs_20140526_models.DetachClassicLinkVpcRequest,
    ) -> ecs_20140526_models.DetachClassicLinkVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_classic_link_vpc_with_options_async(request, runtime)

    def detach_disk_with_options(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachDiskResponse().from_map(
            self.do_rpcrequest('DetachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_disk_with_options_async(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachDiskResponse().from_map(
            await self.do_rpcrequest_async('DetachDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_disk(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
    ) -> ecs_20140526_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_disk_with_options(request, runtime)

    async def detach_disk_async(
        self,
        request: ecs_20140526_models.DetachDiskRequest,
    ) -> ecs_20140526_models.DetachDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_disk_with_options_async(request, runtime)

    def detach_instance_ram_role_with_options(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachInstanceRamRoleResponse().from_map(
            self.do_rpcrequest('DetachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_instance_ram_role_with_options_async(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachInstanceRamRoleResponse().from_map(
            await self.do_rpcrequest_async('DetachInstanceRamRole', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_instance_ram_role(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_instance_ram_role_with_options(request, runtime)

    async def detach_instance_ram_role_async(
        self,
        request: ecs_20140526_models.DetachInstanceRamRoleRequest,
    ) -> ecs_20140526_models.DetachInstanceRamRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_instance_ram_role_with_options_async(request, runtime)

    def detach_key_pair_with_options(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachKeyPairResponse().from_map(
            self.do_rpcrequest('DetachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachKeyPairResponse().from_map(
            await self.do_rpcrequest_async('DetachKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_key_pair(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_key_pair_with_options(request, runtime)

    async def detach_key_pair_async(
        self,
        request: ecs_20140526_models.DetachKeyPairRequest,
    ) -> ecs_20140526_models.DetachKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_key_pair_with_options_async(request, runtime)

    def detach_network_interface_with_options(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachNetworkInterfaceResponse().from_map(
            self.do_rpcrequest('DetachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_network_interface_with_options_async(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DetachNetworkInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DetachNetworkInterface', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_network_interface(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_network_interface_with_options(request, runtime)

    async def detach_network_interface_async(
        self,
        request: ecs_20140526_models.DetachNetworkInterfaceRequest,
    ) -> ecs_20140526_models.DetachNetworkInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_network_interface_with_options_async(request, runtime)

    def disable_activation_with_options(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DisableActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DisableActivationResponse().from_map(
            self.do_rpcrequest('DisableActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_activation_with_options_async(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.DisableActivationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.DisableActivationResponse().from_map(
            await self.do_rpcrequest_async('DisableActivation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_activation(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
    ) -> ecs_20140526_models.DisableActivationResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_activation_with_options(request, runtime)

    async def disable_activation_async(
        self,
        request: ecs_20140526_models.DisableActivationRequest,
    ) -> ecs_20140526_models.DisableActivationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_activation_with_options_async(request, runtime)

    def eip_fill_params_with_options(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillParamsResponse().from_map(
            self.do_rpcrequest('EipFillParams', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_fill_params_with_options_async(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillParamsResponse().from_map(
            await self.do_rpcrequest_async('EipFillParams', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_params(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_params_with_options(request, runtime)

    async def eip_fill_params_async(
        self,
        request: ecs_20140526_models.EipFillParamsRequest,
    ) -> ecs_20140526_models.EipFillParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_fill_params_with_options_async(request, runtime)

    def eip_fill_product_with_options(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillProductResponse().from_map(
            self.do_rpcrequest('EipFillProduct', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_fill_product_with_options_async(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipFillProductResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipFillProductResponse().from_map(
            await self.do_rpcrequest_async('EipFillProduct', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_fill_product(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
    ) -> ecs_20140526_models.EipFillProductResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_fill_product_with_options(request, runtime)

    async def eip_fill_product_async(
        self,
        request: ecs_20140526_models.EipFillProductRequest,
    ) -> ecs_20140526_models.EipFillProductResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_fill_product_with_options_async(request, runtime)

    def eip_notify_paid_with_options(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipNotifyPaidResponse().from_map(
            self.do_rpcrequest('EipNotifyPaid', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def eip_notify_paid_with_options_async(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EipNotifyPaidResponse().from_map(
            await self.do_rpcrequest_async('EipNotifyPaid', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def eip_notify_paid(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        runtime = util_models.RuntimeOptions()
        return self.eip_notify_paid_with_options(request, runtime)

    async def eip_notify_paid_async(
        self,
        request: ecs_20140526_models.EipNotifyPaidRequest,
    ) -> ecs_20140526_models.EipNotifyPaidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.eip_notify_paid_with_options_async(request, runtime)

    def enable_physical_connection_with_options(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EnablePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('EnablePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.EnablePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('EnablePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_physical_connection(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_physical_connection_with_options(request, runtime)

    async def enable_physical_connection_async(
        self,
        request: ecs_20140526_models.EnablePhysicalConnectionRequest,
    ) -> ecs_20140526_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_physical_connection_with_options_async(request, runtime)

    def export_image_with_options(
        self,
        request: ecs_20140526_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportImageResponse().from_map(
            self.do_rpcrequest('ExportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_image_with_options_async(
        self,
        request: ecs_20140526_models.ExportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportImageResponse().from_map(
            await self.do_rpcrequest_async('ExportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_image(
        self,
        request: ecs_20140526_models.ExportImageRequest,
    ) -> ecs_20140526_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    async def export_image_async(
        self,
        request: ecs_20140526_models.ExportImageRequest,
    ) -> ecs_20140526_models.ExportImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_image_with_options_async(request, runtime)

    def export_snapshot_with_options(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportSnapshotResponse().from_map(
            self.do_rpcrequest('ExportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ExportSnapshotResponse().from_map(
            await self.do_rpcrequest_async('ExportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_snapshot(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_snapshot_with_options(request, runtime)

    async def export_snapshot_async(
        self,
        request: ecs_20140526_models.ExportSnapshotRequest,
    ) -> ecs_20140526_models.ExportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_snapshot_with_options_async(request, runtime)

    def get_instance_console_output_with_options(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceConsoleOutputResponse().from_map(
            self.do_rpcrequest('GetInstanceConsoleOutput', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_console_output_with_options_async(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceConsoleOutputResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceConsoleOutput', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_console_output(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_console_output_with_options(request, runtime)

    async def get_instance_console_output_async(
        self,
        request: ecs_20140526_models.GetInstanceConsoleOutputRequest,
    ) -> ecs_20140526_models.GetInstanceConsoleOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_console_output_with_options_async(request, runtime)

    def get_instance_screenshot_with_options(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceScreenshotResponse().from_map(
            self.do_rpcrequest('GetInstanceScreenshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_instance_screenshot_with_options_async(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.GetInstanceScreenshotResponse().from_map(
            await self.do_rpcrequest_async('GetInstanceScreenshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_screenshot(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_instance_screenshot_with_options(request, runtime)

    async def get_instance_screenshot_async(
        self,
        request: ecs_20140526_models.GetInstanceScreenshotRequest,
    ) -> ecs_20140526_models.GetInstanceScreenshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_instance_screenshot_with_options_async(request, runtime)

    def import_image_with_options(
        self,
        request: ecs_20140526_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportImageResponse().from_map(
            self.do_rpcrequest('ImportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_image_with_options_async(
        self,
        request: ecs_20140526_models.ImportImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportImageResponse().from_map(
            await self.do_rpcrequest_async('ImportImage', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_image(
        self,
        request: ecs_20140526_models.ImportImageRequest,
    ) -> ecs_20140526_models.ImportImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_image_with_options(request, runtime)

    async def import_image_async(
        self,
        request: ecs_20140526_models.ImportImageRequest,
    ) -> ecs_20140526_models.ImportImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_image_with_options_async(request, runtime)

    def import_key_pair_with_options(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportKeyPairResponse().from_map(
            self.do_rpcrequest('ImportKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_key_pair_with_options_async(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportKeyPairResponse().from_map(
            await self.do_rpcrequest_async('ImportKeyPair', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_key_pair(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    async def import_key_pair_async(
        self,
        request: ecs_20140526_models.ImportKeyPairRequest,
    ) -> ecs_20140526_models.ImportKeyPairResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_key_pair_with_options_async(request, runtime)

    def import_snapshot_with_options(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportSnapshotResponse().from_map(
            self.do_rpcrequest('ImportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_snapshot_with_options_async(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ImportSnapshotResponse().from_map(
            await self.do_rpcrequest_async('ImportSnapshot', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_snapshot(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_snapshot_with_options(request, runtime)

    async def import_snapshot_async(
        self,
        request: ecs_20140526_models.ImportSnapshotRequest,
    ) -> ecs_20140526_models.ImportSnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_snapshot_with_options_async(request, runtime)

    def install_cloud_assistant_with_options(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InstallCloudAssistantResponse().from_map(
            self.do_rpcrequest('InstallCloudAssistant', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_cloud_assistant_with_options_async(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InstallCloudAssistantResponse().from_map(
            await self.do_rpcrequest_async('InstallCloudAssistant', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_cloud_assistant(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cloud_assistant_with_options(request, runtime)

    async def install_cloud_assistant_async(
        self,
        request: ecs_20140526_models.InstallCloudAssistantRequest,
    ) -> ecs_20140526_models.InstallCloudAssistantResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cloud_assistant_with_options_async(request, runtime)

    def invoke_command_with_options(
        self,
        tmp_req: ecs_20140526_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InvokeCommandResponse().from_map(
            self.do_rpcrequest('InvokeCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_command_with_options_async(
        self,
        tmp_req: ecs_20140526_models.InvokeCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.InvokeCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.InvokeCommandResponse().from_map(
            await self.do_rpcrequest_async('InvokeCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_command(
        self,
        request: ecs_20140526_models.InvokeCommandRequest,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_command_with_options(request, runtime)

    async def invoke_command_async(
        self,
        request: ecs_20140526_models.InvokeCommandRequest,
    ) -> ecs_20140526_models.InvokeCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_command_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinResourceGroupResponse().from_map(
            self.do_rpcrequest('JoinResourceGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinResourceGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_resource_group(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: ecs_20140526_models.JoinResourceGroupRequest,
    ) -> ecs_20140526_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def join_security_group_with_options(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinSecurityGroupResponse().from_map(
            self.do_rpcrequest('JoinSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_security_group_with_options_async(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.JoinSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_security_group(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    async def join_security_group_async(
        self,
        request: ecs_20140526_models.JoinSecurityGroupRequest,
    ) -> ecs_20140526_models.JoinSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_security_group_with_options_async(request, runtime)

    def leave_security_group_with_options(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.LeaveSecurityGroupResponse().from_map(
            self.do_rpcrequest('LeaveSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def leave_security_group_with_options_async(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.LeaveSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('LeaveSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def leave_security_group(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    async def leave_security_group_async(
        self,
        request: ecs_20140526_models.LeaveSecurityGroupRequest,
    ) -> ecs_20140526_models.LeaveSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.leave_security_group_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ecs_20140526_models.ListTagResourcesRequest,
    ) -> ecs_20140526_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_auto_provisioning_group_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoProvisioningGroupResponse().from_map(
            self.do_rpcrequest('ModifyAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_provisioning_group_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoProvisioningGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoProvisioningGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_provisioning_group(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_provisioning_group_with_options(request, runtime)

    async def modify_auto_provisioning_group_async(
        self,
        request: ecs_20140526_models.ModifyAutoProvisioningGroupRequest,
    ) -> ecs_20140526_models.ModifyAutoProvisioningGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_provisioning_group_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyResponse().from_map(
            self.do_rpcrequest('ModifyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_snapshot_policy_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoSnapshotPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    async def modify_auto_snapshot_policy_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_with_options_async(request, runtime)

    def modify_auto_snapshot_policy_ex_with_options(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse().from_map(
            self.do_rpcrequest('ModifyAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_auto_snapshot_policy_ex_with_options_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse().from_map(
            await self.do_rpcrequest_async('ModifyAutoSnapshotPolicyEx', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_auto_snapshot_policy_ex(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_auto_snapshot_policy_ex_with_options(request, runtime)

    async def modify_auto_snapshot_policy_ex_async(
        self,
        request: ecs_20140526_models.ModifyAutoSnapshotPolicyExRequest,
    ) -> ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_auto_snapshot_policy_ex_with_options_async(request, runtime)

    def modify_bandwidth_package_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyBandwidthPackageSpecResponse().from_map(
            self.do_rpcrequest('ModifyBandwidthPackageSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_bandwidth_package_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyBandwidthPackageSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyBandwidthPackageSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bandwidth_package_spec(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    async def modify_bandwidth_package_spec_async(
        self,
        request: ecs_20140526_models.ModifyBandwidthPackageSpecRequest,
    ) -> ecs_20140526_models.ModifyBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_capacity_reservation_with_options(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCapacityReservationResponse().from_map(
            self.do_rpcrequest('ModifyCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_capacity_reservation_with_options_async(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCapacityReservationResponse().from_map(
            await self.do_rpcrequest_async('ModifyCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_capacity_reservation(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_capacity_reservation_with_options(request, runtime)

    async def modify_capacity_reservation_async(
        self,
        request: ecs_20140526_models.ModifyCapacityReservationRequest,
    ) -> ecs_20140526_models.ModifyCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_capacity_reservation_with_options_async(request, runtime)

    def modify_command_with_options(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCommandResponse().from_map(
            self.do_rpcrequest('ModifyCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_command_with_options_async(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyCommandResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_command(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_command_with_options(request, runtime)

    async def modify_command_async(
        self,
        request: ecs_20140526_models.ModifyCommandRequest,
    ) -> ecs_20140526_models.ModifyCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_command_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_auto_release_time_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_release_time(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    async def modify_dedicated_host_auto_release_time_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_release_time_with_options_async(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_auto_renew_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    async def modify_dedicated_host_auto_renew_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_auto_renew_attribute_with_options_async(request, runtime)

    def modify_dedicated_host_cluster_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_cluster_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_cluster_attribute(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    async def modify_dedicated_host_cluster_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_cluster_attribute_with_options_async(request, runtime)

    def modify_dedicated_hosts_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyDedicatedHostsChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_hosts_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDedicatedHostsChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_hosts_charge_type(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_hosts_charge_type_with_options(request, runtime)

    async def modify_dedicated_hosts_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyDedicatedHostsChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_hosts_charge_type_with_options_async(request, runtime)

    def modify_demand_with_options(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDemandResponse().from_map(
            self.do_rpcrequest('ModifyDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_demand_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDemandResponse().from_map(
            await self.do_rpcrequest_async('ModifyDemand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_demand(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_demand_with_options(request, runtime)

    async def modify_demand_async(
        self,
        request: ecs_20140526_models.ModifyDemandRequest,
    ) -> ecs_20140526_models.ModifyDemandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_demand_with_options_async(request, runtime)

    def modify_deployment_set_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDeploymentSetAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDeploymentSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_deployment_set_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDeploymentSetAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDeploymentSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_deployment_set_attribute(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_deployment_set_attribute_with_options(request, runtime)

    async def modify_deployment_set_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDeploymentSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyDeploymentSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_deployment_set_attribute_with_options_async(request, runtime)

    def modify_disk_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskAttributeResponse().from_map(
            self.do_rpcrequest('ModifyDiskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_attribute(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_attribute_with_options(request, runtime)

    async def modify_disk_attribute_async(
        self,
        request: ecs_20140526_models.ModifyDiskAttributeRequest,
    ) -> ecs_20140526_models.ModifyDiskAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_attribute_with_options_async(request, runtime)

    def modify_disk_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyDiskChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_charge_type(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_charge_type_with_options(request, runtime)

    async def modify_disk_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyDiskChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyDiskChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_charge_type_with_options_async(request, runtime)

    def modify_disk_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskSpecResponse().from_map(
            self.do_rpcrequest('ModifyDiskSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_disk_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyDiskSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyDiskSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_disk_spec(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_disk_spec_with_options(request, runtime)

    async def modify_disk_spec_async(
        self,
        request: ecs_20140526_models.ModifyDiskSpecRequest,
    ) -> ecs_20140526_models.ModifyDiskSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_disk_spec_with_options_async(request, runtime)

    def modify_eip_address_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyEipAddressAttributeResponse().from_map(
            self.do_rpcrequest('ModifyEipAddressAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_eip_address_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyEipAddressAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyEipAddressAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_eip_address_attribute(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_eip_address_attribute_with_options(request, runtime)

    async def modify_eip_address_attribute_async(
        self,
        request: ecs_20140526_models.ModifyEipAddressAttributeRequest,
    ) -> ecs_20140526_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_eip_address_attribute_with_options_async(request, runtime)

    def modify_elasticity_assurance_with_options(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyElasticityAssuranceResponse().from_map(
            self.do_rpcrequest('ModifyElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_elasticity_assurance_with_options_async(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyElasticityAssuranceResponse().from_map(
            await self.do_rpcrequest_async('ModifyElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_elasticity_assurance(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_elasticity_assurance_with_options(request, runtime)

    async def modify_elasticity_assurance_async(
        self,
        request: ecs_20140526_models.ModifyElasticityAssuranceRequest,
    ) -> ecs_20140526_models.ModifyElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_elasticity_assurance_with_options_async(request, runtime)

    def modify_forward_entry_with_options(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyForwardEntryResponse().from_map(
            self.do_rpcrequest('ModifyForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_forward_entry_with_options_async(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyForwardEntry', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_forward_entry(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    async def modify_forward_entry_async(
        self,
        request: ecs_20140526_models.ModifyForwardEntryRequest,
    ) -> ecs_20140526_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_forward_entry_with_options_async(request, runtime)

    def modify_ha_vip_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHaVipAttributeResponse().from_map(
            self.do_rpcrequest('ModifyHaVipAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ha_vip_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHaVipAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHaVipAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ha_vip_attribute(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    async def modify_ha_vip_attribute_async(
        self,
        request: ecs_20140526_models.ModifyHaVipAttributeRequest,
    ) -> ecs_20140526_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ha_vip_attribute_with_options_async(request, runtime)

    def modify_hpc_cluster_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHpcClusterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyHpcClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_hpc_cluster_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyHpcClusterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHpcClusterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_hpc_cluster_attribute(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_hpc_cluster_attribute_with_options(request, runtime)

    async def modify_hpc_cluster_attribute_async(
        self,
        request: ecs_20140526_models.ModifyHpcClusterAttributeRequest,
    ) -> ecs_20140526_models.ModifyHpcClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_hpc_cluster_attribute_with_options_async(request, runtime)

    def modify_image_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageAttributeResponse().from_map(
            self.do_rpcrequest('ModifyImageAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_attribute(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    async def modify_image_attribute_async(
        self,
        request: ecs_20140526_models.ModifyImageAttributeRequest,
    ) -> ecs_20140526_models.ModifyImageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_attribute_with_options_async(request, runtime)

    def modify_image_share_group_permission_with_options(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageShareGroupPermissionResponse().from_map(
            self.do_rpcrequest('ModifyImageShareGroupPermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_group_permission_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageShareGroupPermissionResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageShareGroupPermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_group_permission(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_group_permission_with_options(request, runtime)

    async def modify_image_share_group_permission_async(
        self,
        request: ecs_20140526_models.ModifyImageShareGroupPermissionRequest,
    ) -> ecs_20140526_models.ModifyImageShareGroupPermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_group_permission_with_options_async(request, runtime)

    def modify_image_share_permission_with_options(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageSharePermissionResponse().from_map(
            self.do_rpcrequest('ModifyImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_image_share_permission_with_options_async(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyImageSharePermissionResponse().from_map(
            await self.do_rpcrequest_async('ModifyImageSharePermission', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_image_share_permission(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    async def modify_image_share_permission_async(
        self,
        request: ecs_20140526_models.ModifyImageSharePermissionRequest,
    ) -> ecs_20140526_models.ModifyImageSharePermissionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_image_share_permission_with_options_async(request, runtime)

    def modify_instance_attachment_attributes_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attachment_attributes_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttachmentAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attachment_attributes(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attachment_attributes_with_options(request, runtime)

    async def modify_instance_attachment_attributes_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttachmentAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttachmentAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attachment_attributes_with_options_async(request, runtime)

    def modify_instance_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    async def modify_instance_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_attribute_with_options_async(request, runtime)

    def modify_instance_auto_release_time_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_release_time_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoReleaseTime', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_release_time(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_release_time_with_options(request, runtime)

    async def modify_instance_auto_release_time_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoReleaseTimeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_release_time_with_options_async(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renew_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renew_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    async def modify_instance_auto_renew_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceAutoRenewAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renew_attribute_with_options_async(request, runtime)

    def modify_instance_charge_type_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_charge_type_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceChargeType', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_charge_type(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_charge_type_with_options(request, runtime)

    async def modify_instance_charge_type_async(
        self,
        request: ecs_20140526_models.ModifyInstanceChargeTypeRequest,
    ) -> ecs_20140526_models.ModifyInstanceChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_charge_type_with_options_async(request, runtime)

    def modify_instance_deployment_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceDeploymentResponse().from_map(
            self.do_rpcrequest('ModifyInstanceDeployment', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_deployment_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceDeploymentResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceDeployment', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_deployment(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_deployment_with_options(request, runtime)

    async def modify_instance_deployment_async(
        self,
        request: ecs_20140526_models.ModifyInstanceDeploymentRequest,
    ) -> ecs_20140526_models.ModifyInstanceDeploymentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_deployment_with_options_async(request, runtime)

    def modify_instance_maintenance_attributes_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_maintenance_attributes_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMaintenanceAttributes', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_maintenance_attributes(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    async def modify_instance_maintenance_attributes_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMaintenanceAttributesRequest,
    ) -> ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_maintenance_attributes_with_options_async(request, runtime)

    def modify_instance_metadata_options_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMetadataOptionsResponse().from_map(
            self.do_rpcrequest('ModifyInstanceMetadataOptions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_metadata_options_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceMetadataOptionsResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceMetadataOptions', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_metadata_options(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_metadata_options_with_options(request, runtime)

    async def modify_instance_metadata_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceMetadataOptionsRequest,
    ) -> ecs_20140526_models.ModifyInstanceMetadataOptionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_metadata_options_with_options_async(request, runtime)

    def modify_instance_network_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceNetworkSpecResponse().from_map(
            self.do_rpcrequest('ModifyInstanceNetworkSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_network_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceNetworkSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceNetworkSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_network_spec(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_network_spec_with_options(request, runtime)

    async def modify_instance_network_spec_async(
        self,
        request: ecs_20140526_models.ModifyInstanceNetworkSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceNetworkSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_network_spec_with_options_async(request, runtime)

    def modify_instance_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_spec(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_spec_with_options(request, runtime)

    async def modify_instance_spec_async(
        self,
        request: ecs_20140526_models.ModifyInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_spec_with_options_async(request, runtime)

    def modify_instance_vnc_passwd_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVncPasswdResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vnc_passwd_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVncPasswdResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceVncPasswd', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vnc_passwd(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vnc_passwd_with_options(request, runtime)

    async def modify_instance_vnc_passwd_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVncPasswdRequest,
    ) -> ecs_20140526_models.ModifyInstanceVncPasswdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vnc_passwd_with_options_async(request, runtime)

    def modify_instance_vpc_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVpcAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_vpc_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyInstanceVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_vpc_attribute(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    async def modify_instance_vpc_attribute_async(
        self,
        request: ecs_20140526_models.ModifyInstanceVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyInstanceVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_vpc_attribute_with_options_async(request, runtime)

    def modify_launch_template_default_version_with_options(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse().from_map(
            self.do_rpcrequest('ModifyLaunchTemplateDefaultVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_launch_template_default_version_with_options_async(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse().from_map(
            await self.do_rpcrequest_async('ModifyLaunchTemplateDefaultVersion', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_launch_template_default_version(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_launch_template_default_version_with_options(request, runtime)

    async def modify_launch_template_default_version_async(
        self,
        request: ecs_20140526_models.ModifyLaunchTemplateDefaultVersionRequest,
    ) -> ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_launch_template_default_version_with_options_async(request, runtime)

    def modify_managed_instance_with_options(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyManagedInstanceResponse().from_map(
            self.do_rpcrequest('ModifyManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_managed_instance_with_options_async(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyManagedInstanceResponse().from_map(
            await self.do_rpcrequest_async('ModifyManagedInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_managed_instance(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_managed_instance_with_options(request, runtime)

    async def modify_managed_instance_async(
        self,
        request: ecs_20140526_models.ModifyManagedInstanceRequest,
    ) -> ecs_20140526_models.ModifyManagedInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_managed_instance_with_options_async(request, runtime)

    def modify_network_interface_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_interface_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyNetworkInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_interface_attribute(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_interface_attribute_with_options(request, runtime)

    async def modify_network_interface_attribute_async(
        self,
        request: ecs_20140526_models.ModifyNetworkInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_interface_attribute_with_options_async(request, runtime)

    def modify_physical_connection_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse().from_map(
            self.do_rpcrequest('ModifyPhysicalConnectionAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_physical_connection_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyPhysicalConnectionAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_physical_connection_attribute(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    async def modify_physical_connection_attribute_async(
        self,
        request: ecs_20140526_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_physical_connection_attribute_with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPrepayInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyPrepayInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyPrepayInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyPrepayInstanceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: ecs_20140526_models.ModifyPrepayInstanceSpecRequest,
    ) -> ecs_20140526_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def modify_reserved_instance_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstanceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyReservedInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_reserved_instance_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstanceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyReservedInstanceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instance_attribute(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    async def modify_reserved_instance_attribute_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstanceAttributeRequest,
    ) -> ecs_20140526_models.ModifyReservedInstanceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instance_attribute_with_options_async(request, runtime)

    def modify_reserved_instances_with_options(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstancesResponse().from_map(
            self.do_rpcrequest('ModifyReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_reserved_instances_with_options_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyReservedInstancesResponse().from_map(
            await self.do_rpcrequest_async('ModifyReservedInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_reserved_instances(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_reserved_instances_with_options(request, runtime)

    async def modify_reserved_instances_async(
        self,
        request: ecs_20140526_models.ModifyReservedInstancesRequest,
    ) -> ecs_20140526_models.ModifyReservedInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_reserved_instances_with_options_async(request, runtime)

    def modify_router_interface_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_attribute(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_attribute_with_options(request, runtime)

    async def modify_router_interface_attribute_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceAttributeRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_attribute_with_options_async(request, runtime)

    def modify_router_interface_spec_with_options(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceSpecResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_spec_with_options_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyRouterInterfaceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceSpec', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_spec(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_spec_with_options(request, runtime)

    async def modify_router_interface_spec_async(
        self,
        request: ecs_20140526_models.ModifyRouterInterfaceSpecRequest,
    ) -> ecs_20140526_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_spec_with_options_async(request, runtime)

    def modify_security_group_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupAttributeResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_attribute(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_attribute_with_options(request, runtime)

    async def modify_security_group_attribute_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupAttributeRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_attribute_with_options_async(request, runtime)

    def modify_security_group_egress_rule_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupEgressRuleResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupEgressRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_egress_rule_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupEgressRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupEgressRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_egress_rule(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_egress_rule_with_options(request, runtime)

    async def modify_security_group_egress_rule_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupEgressRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupEgressRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_egress_rule_with_options_async(request, runtime)

    def modify_security_group_policy_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupPolicyResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_policy_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupPolicyResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupPolicy', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_policy(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_policy_with_options(request, runtime)

    async def modify_security_group_policy_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupPolicyRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_policy_with_options_async(request, runtime)

    def modify_security_group_rule_with_options(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupRuleResponse().from_map(
            self.do_rpcrequest('ModifySecurityGroupRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_security_group_rule_with_options_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySecurityGroupRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifySecurityGroupRule', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_security_group_rule(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_rule_with_options(request, runtime)

    async def modify_security_group_rule_async(
        self,
        request: ecs_20140526_models.ModifySecurityGroupRuleRequest,
    ) -> ecs_20140526_models.ModifySecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_group_rule_with_options_async(request, runtime)

    def modify_snapshot_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotAttributeResponse().from_map(
            self.do_rpcrequest('ModifySnapshotAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_snapshot_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifySnapshotAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_attribute(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_attribute_with_options(request, runtime)

    async def modify_snapshot_attribute_async(
        self,
        request: ecs_20140526_models.ModifySnapshotAttributeRequest,
    ) -> ecs_20140526_models.ModifySnapshotAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_attribute_with_options_async(request, runtime)

    def modify_snapshot_group_with_options(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotGroupResponse().from_map(
            self.do_rpcrequest('ModifySnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_snapshot_group_with_options_async(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifySnapshotGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifySnapshotGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snapshot_group(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snapshot_group_with_options(request, runtime)

    async def modify_snapshot_group_async(
        self,
        request: ecs_20140526_models.ModifySnapshotGroupRequest,
    ) -> ecs_20140526_models.ModifySnapshotGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snapshot_group_with_options_async(request, runtime)

    def modify_storage_capacity_unit_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse().from_map(
            self.do_rpcrequest('ModifyStorageCapacityUnitAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_storage_capacity_unit_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyStorageCapacityUnitAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_capacity_unit_attribute(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_capacity_unit_attribute_with_options(request, runtime)

    async def modify_storage_capacity_unit_attribute_async(
        self,
        request: ecs_20140526_models.ModifyStorageCapacityUnitAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_capacity_unit_attribute_with_options_async(request, runtime)

    def modify_storage_set_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageSetAttributeResponse().from_map(
            self.do_rpcrequest('ModifyStorageSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_storage_set_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyStorageSetAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyStorageSetAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_storage_set_attribute(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_set_attribute_with_options(request, runtime)

    async def modify_storage_set_attribute_async(
        self,
        request: ecs_20140526_models.ModifyStorageSetAttributeRequest,
    ) -> ecs_20140526_models.ModifyStorageSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_set_attribute_with_options_async(request, runtime)

    def modify_user_business_behavior_with_options(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyUserBusinessBehaviorResponse().from_map(
            self.do_rpcrequest('ModifyUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_user_business_behavior_with_options_async(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyUserBusinessBehaviorResponse().from_map(
            await self.do_rpcrequest_async('ModifyUserBusinessBehavior', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_user_business_behavior(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_user_business_behavior_with_options(request, runtime)

    async def modify_user_business_behavior_async(
        self,
        request: ecs_20140526_models.ModifyUserBusinessBehaviorRequest,
    ) -> ecs_20140526_models.ModifyUserBusinessBehaviorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_user_business_behavior_with_options_async(request, runtime)

    def modify_virtual_border_router_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVirtualBorderRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_virtual_border_router_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVirtualBorderRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_virtual_border_router_attribute(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    async def modify_virtual_border_router_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_border_router_attribute_with_options_async(request, runtime)

    def modify_vpc_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVpcAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpcAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_attribute(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_attribute_with_options(request, runtime)

    async def modify_vpc_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVpcAttributeRequest,
    ) -> ecs_20140526_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_attribute_with_options_async(request, runtime)

    def modify_vrouter_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vrouter_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVRouterAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vrouter_attribute(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vrouter_attribute_with_options(request, runtime)

    async def modify_vrouter_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVRouterAttributeRequest,
    ) -> ecs_20140526_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vrouter_attribute_with_options_async(request, runtime)

    def modify_vswitch_attribute_with_options(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVSwitchAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVSwitchAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vswitch_attribute_with_options_async(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ModifyVSwitchAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVSwitchAttribute', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vswitch_attribute(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    async def modify_vswitch_attribute_async(
        self,
        request: ecs_20140526_models.ModifyVSwitchAttributeRequest,
    ) -> ecs_20140526_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vswitch_attribute_with_options_async(request, runtime)

    def purchase_reserved_instances_offering_with_options(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseReservedInstancesOfferingResponse().from_map(
            self.do_rpcrequest('PurchaseReservedInstancesOffering', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purchase_reserved_instances_offering_with_options_async(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseReservedInstancesOfferingResponse().from_map(
            await self.do_rpcrequest_async('PurchaseReservedInstancesOffering', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_reserved_instances_offering(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    async def purchase_reserved_instances_offering_async(
        self,
        request: ecs_20140526_models.PurchaseReservedInstancesOfferingRequest,
    ) -> ecs_20140526_models.PurchaseReservedInstancesOfferingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_reserved_instances_offering_with_options_async(request, runtime)

    def purchase_storage_capacity_unit_with_options(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseStorageCapacityUnitResponse().from_map(
            self.do_rpcrequest('PurchaseStorageCapacityUnit', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def purchase_storage_capacity_unit_with_options_async(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.PurchaseStorageCapacityUnitResponse().from_map(
            await self.do_rpcrequest_async('PurchaseStorageCapacityUnit', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def purchase_storage_capacity_unit(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    async def purchase_storage_capacity_unit_async(
        self,
        request: ecs_20140526_models.PurchaseStorageCapacityUnitRequest,
    ) -> ecs_20140526_models.PurchaseStorageCapacityUnitResponse:
        runtime = util_models.RuntimeOptions()
        return await self.purchase_storage_capacity_unit_with_options_async(request, runtime)

    def re_activate_instances_with_options(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReActivateInstancesResponse().from_map(
            self.do_rpcrequest('ReActivateInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_activate_instances_with_options_async(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReActivateInstancesResponse().from_map(
            await self.do_rpcrequest_async('ReActivateInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_activate_instances(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_activate_instances_with_options(request, runtime)

    async def re_activate_instances_async(
        self,
        request: ecs_20140526_models.ReActivateInstancesRequest,
    ) -> ecs_20140526_models.ReActivateInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_activate_instances_with_options_async(request, runtime)

    def reboot_instance_with_options(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstanceResponse().from_map(
            self.do_rpcrequest('RebootInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instance_with_options_async(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstanceResponse().from_map(
            await self.do_rpcrequest_async('RebootInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instance(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    async def reboot_instance_async(
        self,
        request: ecs_20140526_models.RebootInstanceRequest,
    ) -> ecs_20140526_models.RebootInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instance_with_options_async(request, runtime)

    def reboot_instances_with_options(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstancesResponse().from_map(
            self.do_rpcrequest('RebootInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reboot_instances_with_options_async(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RebootInstancesResponse().from_map(
            await self.do_rpcrequest_async('RebootInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reboot_instances(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.reboot_instances_with_options(request, runtime)

    async def reboot_instances_async(
        self,
        request: ecs_20140526_models.RebootInstancesRequest,
    ) -> ecs_20140526_models.RebootInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_instances_with_options_async(request, runtime)

    def recover_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RecoverVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('RecoverVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recover_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RecoverVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('RecoverVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recover_virtual_border_router(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_virtual_border_router_with_options(request, runtime)

    async def recover_virtual_border_router_async(
        self,
        request: ecs_20140526_models.RecoverVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_virtual_border_router_with_options_async(request, runtime)

    def redeploy_dedicated_host_with_options(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployDedicatedHostResponse().from_map(
            self.do_rpcrequest('RedeployDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def redeploy_dedicated_host_with_options_async(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('RedeployDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_dedicated_host(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.redeploy_dedicated_host_with_options(request, runtime)

    async def redeploy_dedicated_host_async(
        self,
        request: ecs_20140526_models.RedeployDedicatedHostRequest,
    ) -> ecs_20140526_models.RedeployDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.redeploy_dedicated_host_with_options_async(request, runtime)

    def redeploy_instance_with_options(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployInstanceResponse().from_map(
            self.do_rpcrequest('RedeployInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def redeploy_instance_with_options_async(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RedeployInstanceResponse().from_map(
            await self.do_rpcrequest_async('RedeployInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def redeploy_instance(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.redeploy_instance_with_options(request, runtime)

    async def redeploy_instance_async(
        self,
        request: ecs_20140526_models.RedeployInstanceRequest,
    ) -> ecs_20140526_models.RedeployInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.redeploy_instance_with_options_async(request, runtime)

    def re_init_disk_with_options(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReInitDiskResponse().from_map(
            self.do_rpcrequest('ReInitDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def re_init_disk_with_options_async(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReInitDiskResponse().from_map(
            await self.do_rpcrequest_async('ReInitDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def re_init_disk(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    async def re_init_disk_async(
        self,
        request: ecs_20140526_models.ReInitDiskRequest,
    ) -> ecs_20140526_models.ReInitDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.re_init_disk_with_options_async(request, runtime)

    def release_capacity_reservation_with_options(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseCapacityReservationResponse().from_map(
            self.do_rpcrequest('ReleaseCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_capacity_reservation_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseCapacityReservationResponse().from_map(
            await self.do_rpcrequest_async('ReleaseCapacityReservation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_capacity_reservation(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_capacity_reservation_with_options(request, runtime)

    async def release_capacity_reservation_async(
        self,
        request: ecs_20140526_models.ReleaseCapacityReservationRequest,
    ) -> ecs_20140526_models.ReleaseCapacityReservationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_capacity_reservation_with_options_async(request, runtime)

    def release_dedicated_host_with_options(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseDedicatedHostResponse().from_map(
            self.do_rpcrequest('ReleaseDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_dedicated_host_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseDedicatedHostResponse().from_map(
            await self.do_rpcrequest_async('ReleaseDedicatedHost', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_dedicated_host(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_dedicated_host_with_options(request, runtime)

    async def release_dedicated_host_async(
        self,
        request: ecs_20140526_models.ReleaseDedicatedHostRequest,
    ) -> ecs_20140526_models.ReleaseDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_dedicated_host_with_options_async(request, runtime)

    def release_eip_address_with_options(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseEipAddressResponse().from_map(
            self.do_rpcrequest('ReleaseEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleaseEipAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_address(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    async def release_eip_address_async(
        self,
        request: ecs_20140526_models.ReleaseEipAddressRequest,
    ) -> ecs_20140526_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_eip_address_with_options_async(request, runtime)

    def release_public_ip_address_with_options(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleasePublicIpAddressResponse().from_map(
            self.do_rpcrequest('ReleasePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_public_ip_address_with_options_async(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReleasePublicIpAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleasePublicIpAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_public_ip_address(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_public_ip_address_with_options(request, runtime)

    async def release_public_ip_address_async(
        self,
        request: ecs_20140526_models.ReleasePublicIpAddressRequest,
    ) -> ecs_20140526_models.ReleasePublicIpAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_public_ip_address_with_options_async(request, runtime)

    def remove_bandwidth_package_ips_with_options(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveBandwidthPackageIpsResponse().from_map(
            self.do_rpcrequest('RemoveBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_bandwidth_package_ips_with_options_async(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveBandwidthPackageIpsResponse().from_map(
            await self.do_rpcrequest_async('RemoveBandwidthPackageIps', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_bandwidth_package_ips(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    async def remove_bandwidth_package_ips_async(
        self,
        request: ecs_20140526_models.RemoveBandwidthPackageIpsRequest,
    ) -> ecs_20140526_models.RemoveBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_bandwidth_package_ips_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveTagsResponse().from_map(
            self.do_rpcrequest('RemoveTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RemoveTagsResponse().from_map(
            await self.do_rpcrequest_async('RemoveTags', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: ecs_20140526_models.RemoveTagsRequest,
    ) -> ecs_20140526_models.RemoveTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def renew_dedicated_hosts_with_options(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewDedicatedHostsResponse().from_map(
            self.do_rpcrequest('RenewDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_dedicated_hosts_with_options_async(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewDedicatedHostsResponse().from_map(
            await self.do_rpcrequest_async('RenewDedicatedHosts', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_dedicated_hosts(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_dedicated_hosts_with_options(request, runtime)

    async def renew_dedicated_hosts_async(
        self,
        request: ecs_20140526_models.RenewDedicatedHostsRequest,
    ) -> ecs_20140526_models.RenewDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_dedicated_hosts_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: ecs_20140526_models.RenewInstanceRequest,
    ) -> ecs_20140526_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_system_disk_with_options(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReplaceSystemDiskResponse().from_map(
            self.do_rpcrequest('ReplaceSystemDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_system_disk_with_options_async(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReplaceSystemDiskResponse().from_map(
            await self.do_rpcrequest_async('ReplaceSystemDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_system_disk(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_system_disk_with_options(request, runtime)

    async def replace_system_disk_async(
        self,
        request: ecs_20140526_models.ReplaceSystemDiskRequest,
    ) -> ecs_20140526_models.ReplaceSystemDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_system_disk_with_options_async(request, runtime)

    def report_instances_status_with_options(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReportInstancesStatusResponse().from_map(
            self.do_rpcrequest('ReportInstancesStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def report_instances_status_with_options_async(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ReportInstancesStatusResponse().from_map(
            await self.do_rpcrequest_async('ReportInstancesStatus', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def report_instances_status(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.report_instances_status_with_options(request, runtime)

    async def report_instances_status_async(
        self,
        request: ecs_20140526_models.ReportInstancesStatusRequest,
    ) -> ecs_20140526_models.ReportInstancesStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.report_instances_status_with_options_async(request, runtime)

    def reset_disk_with_options(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDiskResponse().from_map(
            self.do_rpcrequest('ResetDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_disk_with_options_async(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDiskResponse().from_map(
            await self.do_rpcrequest_async('ResetDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disk(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
    ) -> ecs_20140526_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_disk_with_options(request, runtime)

    async def reset_disk_async(
        self,
        request: ecs_20140526_models.ResetDiskRequest,
    ) -> ecs_20140526_models.ResetDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_disk_with_options_async(request, runtime)

    def reset_disks_with_options(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDisksResponse().from_map(
            self.do_rpcrequest('ResetDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_disks_with_options_async(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResetDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResetDisksResponse().from_map(
            await self.do_rpcrequest_async('ResetDisks', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_disks(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
    ) -> ecs_20140526_models.ResetDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_disks_with_options(request, runtime)

    async def reset_disks_async(
        self,
        request: ecs_20140526_models.ResetDisksRequest,
    ) -> ecs_20140526_models.ResetDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_disks_with_options_async(request, runtime)

    def resize_disk_with_options(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResizeDiskResponse().from_map(
            self.do_rpcrequest('ResizeDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_disk_with_options_async(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.ResizeDiskResponse().from_map(
            await self.do_rpcrequest_async('ResizeDisk', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_disk(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_disk_with_options(request, runtime)

    async def resize_disk_async(
        self,
        request: ecs_20140526_models.ResizeDiskRequest,
    ) -> ecs_20140526_models.ResizeDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_disk_with_options_async(request, runtime)

    def revoke_security_group_with_options(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_with_options_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroup', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    async def revoke_security_group_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_with_options_async(request, runtime)

    def revoke_security_group_egress_with_options(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupEgressResponse().from_map(
            self.do_rpcrequest('RevokeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_security_group_egress_with_options_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RevokeSecurityGroupEgressResponse().from_map(
            await self.do_rpcrequest_async('RevokeSecurityGroupEgress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_security_group_egress(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    async def revoke_security_group_egress_async(
        self,
        request: ecs_20140526_models.RevokeSecurityGroupEgressRequest,
    ) -> ecs_20140526_models.RevokeSecurityGroupEgressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_security_group_egress_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: ecs_20140526_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunCommandResponse().from_map(
            self.do_rpcrequest('RunCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: ecs_20140526_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunCommandResponse:
        UtilClient.validate_model(tmp_req)
        request = ecs_20140526_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunCommandResponse().from_map(
            await self.do_rpcrequest_async('RunCommand', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_command(
        self,
        request: ecs_20140526_models.RunCommandRequest,
    ) -> ecs_20140526_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: ecs_20140526_models.RunCommandRequest,
    ) -> ecs_20140526_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def run_instances_with_options(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunInstancesResponse().from_map(
            self.do_rpcrequest('RunInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_instances_with_options_async(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.RunInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.RunInstancesResponse().from_map(
            await self.do_rpcrequest_async('RunInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_instances(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
    ) -> ecs_20140526_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_instances_with_options(request, runtime)

    async def run_instances_async(
        self,
        request: ecs_20140526_models.RunInstancesRequest,
    ) -> ecs_20140526_models.RunInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_instances_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        request: ecs_20140526_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.SendFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.SendFileResponse().from_map(
            self.do_rpcrequest('SendFile', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_file_with_options_async(
        self,
        request: ecs_20140526_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.SendFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.SendFileResponse().from_map(
            await self.do_rpcrequest_async('SendFile', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_file(
        self,
        request: ecs_20140526_models.SendFileRequest,
    ) -> ecs_20140526_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: ecs_20140526_models.SendFileRequest,
    ) -> ecs_20140526_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def start_elasticity_assurance_with_options(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartElasticityAssuranceResponse().from_map(
            self.do_rpcrequest('StartElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_elasticity_assurance_with_options_async(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartElasticityAssuranceResponse().from_map(
            await self.do_rpcrequest_async('StartElasticityAssurance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_elasticity_assurance(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_elasticity_assurance_with_options(request, runtime)

    async def start_elasticity_assurance_async(
        self,
        request: ecs_20140526_models.StartElasticityAssuranceRequest,
    ) -> ecs_20140526_models.StartElasticityAssuranceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_elasticity_assurance_with_options_async(request, runtime)

    def start_image_pipeline_execution_with_options(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartImagePipelineExecutionResponse().from_map(
            self.do_rpcrequest('StartImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_image_pipeline_execution_with_options_async(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartImagePipelineExecutionResponse().from_map(
            await self.do_rpcrequest_async('StartImagePipelineExecution', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_image_pipeline_execution(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_image_pipeline_execution_with_options(request, runtime)

    async def start_image_pipeline_execution_async(
        self,
        request: ecs_20140526_models.StartImagePipelineExecutionRequest,
    ) -> ecs_20140526_models.StartImagePipelineExecutionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_image_pipeline_execution_with_options_async(request, runtime)

    def start_instance_with_options(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instance_with_options_async(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstanceResponse().from_map(
            await self.do_rpcrequest_async('StartInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
    ) -> ecs_20140526_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    async def start_instance_async(
        self,
        request: ecs_20140526_models.StartInstanceRequest,
    ) -> ecs_20140526_models.StartInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instance_with_options_async(request, runtime)

    def start_instances_with_options(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstancesResponse().from_map(
            self.do_rpcrequest('StartInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_instances_with_options_async(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StartInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StartInstancesResponse().from_map(
            await self.do_rpcrequest_async('StartInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instances(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
    ) -> ecs_20140526_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_instances_with_options(request, runtime)

    async def start_instances_async(
        self,
        request: ecs_20140526_models.StartInstancesRequest,
    ) -> ecs_20140526_models.StartInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_instances_with_options_async(request, runtime)

    def stop_instance_with_options(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstanceResponse().from_map(
            self.do_rpcrequest('StopInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instance_with_options_async(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstanceResponse().from_map(
            await self.do_rpcrequest_async('StopInstance', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instance(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
    ) -> ecs_20140526_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    async def stop_instance_async(
        self,
        request: ecs_20140526_models.StopInstanceRequest,
    ) -> ecs_20140526_models.StopInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instance_with_options_async(request, runtime)

    def stop_instances_with_options(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstancesResponse().from_map(
            self.do_rpcrequest('StopInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_instances_with_options_async(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInstancesResponse().from_map(
            await self.do_rpcrequest_async('StopInstances', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_instances(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
    ) -> ecs_20140526_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_instances_with_options(request, runtime)

    async def stop_instances_async(
        self,
        request: ecs_20140526_models.StopInstancesRequest,
    ) -> ecs_20140526_models.StopInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_instances_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInvocationResponse().from_map(
            self.do_rpcrequest('StopInvocation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.StopInvocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.StopInvocationResponse().from_map(
            await self.do_rpcrequest_async('StopInvocation', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_invocation(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
    ) -> ecs_20140526_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: ecs_20140526_models.StopInvocationRequest,
    ) -> ecs_20140526_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
    ) -> ecs_20140526_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ecs_20140526_models.TagResourcesRequest,
    ) -> ecs_20140526_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def terminate_physical_connection_with_options(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminatePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('TerminatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_physical_connection_with_options_async(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminatePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('TerminatePhysicalConnection', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_physical_connection(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_physical_connection_with_options(request, runtime)

    async def terminate_physical_connection_async(
        self,
        request: ecs_20140526_models.TerminatePhysicalConnectionRequest,
    ) -> ecs_20140526_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_physical_connection_with_options_async(request, runtime)

    def terminate_virtual_border_router_with_options(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminateVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('TerminateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_virtual_border_router_with_options_async(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.TerminateVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('TerminateVirtualBorderRouter', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_virtual_border_router(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_virtual_border_router_with_options(request, runtime)

    async def terminate_virtual_border_router_async(
        self,
        request: ecs_20140526_models.TerminateVirtualBorderRouterRequest,
    ) -> ecs_20140526_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_virtual_border_router_with_options_async(request, runtime)

    def unassign_ipv_6addresses_with_options(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignIpv6AddressesResponse().from_map(
            self.do_rpcrequest('UnassignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassign_ipv_6addresses_with_options_async(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignIpv6AddressesResponse().from_map(
            await self.do_rpcrequest_async('UnassignIpv6Addresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_ipv_6addresses(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_ipv_6addresses_with_options(request, runtime)

    async def unassign_ipv_6addresses_async(
        self,
        request: ecs_20140526_models.UnassignIpv6AddressesRequest,
    ) -> ecs_20140526_models.UnassignIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_ipv_6addresses_with_options_async(request, runtime)

    def unassign_private_ip_addresses_with_options(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignPrivateIpAddressesResponse().from_map(
            self.do_rpcrequest('UnassignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassign_private_ip_addresses_with_options_async(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassignPrivateIpAddressesResponse().from_map(
            await self.do_rpcrequest_async('UnassignPrivateIpAddresses', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassign_private_ip_addresses(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    async def unassign_private_ip_addresses_async(
        self,
        request: ecs_20140526_models.UnassignPrivateIpAddressesRequest,
    ) -> ecs_20140526_models.UnassignPrivateIpAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassign_private_ip_addresses_with_options_async(request, runtime)

    def unassociate_eip_address_with_options(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateEipAddressResponse().from_map(
            self.do_rpcrequest('UnassociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_eip_address_with_options_async(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('UnassociateEipAddress', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_eip_address(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    async def unassociate_eip_address_async(
        self,
        request: ecs_20140526_models.UnassociateEipAddressRequest,
    ) -> ecs_20140526_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_eip_address_with_options_async(request, runtime)

    def unassociate_ha_vip_with_options(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateHaVipResponse().from_map(
            self.do_rpcrequest('UnassociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_ha_vip_with_options_async(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UnassociateHaVipResponse().from_map(
            await self.do_rpcrequest_async('UnassociateHaVip', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_ha_vip(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_ha_vip_with_options(request, runtime)

    async def unassociate_ha_vip_async(
        self,
        request: ecs_20140526_models.UnassociateHaVipRequest,
    ) -> ecs_20140526_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_ha_vip_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return ecs_20140526_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2014-05-26', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ecs_20140526_models.UntagResourcesRequest,
    ) -> ecs_20140526_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
