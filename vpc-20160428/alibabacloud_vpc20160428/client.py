# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vpc20160428 import models as vpc_20160428_models
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
            'cn-qingdao': 'vpc.aliyuncs.com',
            'cn-beijing': 'vpc.aliyuncs.com',
            'cn-hangzhou': 'vpc.aliyuncs.com',
            'cn-shanghai': 'vpc.aliyuncs.com',
            'cn-shenzhen': 'vpc.aliyuncs.com',
            'cn-hongkong': 'vpc.aliyuncs.com',
            'ap-southeast-1': 'vpc.aliyuncs.com',
            'us-west-1': 'vpc.aliyuncs.com',
            'us-east-1': 'vpc.aliyuncs.com',
            'cn-shanghai-finance-1': 'vpc.aliyuncs.com',
            'cn-shenzhen-finance-1': 'vpc.aliyuncs.com',
            'cn-north-2-gov-1': 'vpc.aliyuncs.com',
            'ap-northeast-2-pop': 'vpc.aliyuncs.com',
            'cn-beijing-finance-1': 'vpc.aliyuncs.com',
            'cn-beijing-finance-pop': 'vpc.aliyuncs.com',
            'cn-beijing-gov-1': 'vpc.aliyuncs.com',
            'cn-beijing-nu16-b01': 'vpc.aliyuncs.com',
            'cn-edge-1': 'vpc-nebula.cn-qingdao-nebula.aliyuncs.com',
            'cn-fujian': 'vpc.aliyuncs.com',
            'cn-haidian-cm12-c01': 'vpc.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'vpc.aliyuncs.com',
            'cn-hangzhou-finance': 'vpc.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'vpc.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'vpc.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'vpc.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'vpc.aliyuncs.com',
            'cn-hangzhou-test-306': 'vpc.aliyuncs.com',
            'cn-hongkong-finance-pop': 'vpc.aliyuncs.com',
            'cn-qingdao-nebula': 'vpc-nebula.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'vpc.aliyuncs.com',
            'cn-shanghai-et2-b01': 'vpc.aliyuncs.com',
            'cn-shanghai-inner': 'vpc.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'vpc.aliyuncs.com',
            'cn-shenzhen-inner': 'vpc.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'vpc.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'vpc.aliyuncs.com',
            'cn-wuhan': 'vpc.aliyuncs.com',
            'cn-yushanfang': 'vpc.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'vpc.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'vpc.cn-zhangjiakou.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'vpc-nebula.cn-qingdao-nebula.aliyuncs.com',
            'eu-west-1-oxs': 'vpc-nebula.cn-shenzhen-cloudstone.aliyuncs.com',
            'rus-west-1-pop': 'vpc.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('vpc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_router_interface_with_options(
        self,
        request: vpc_20160428_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ActivateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('ActivateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def activate_router_interface_with_options_async(
        self,
        request: vpc_20160428_models.ActivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ActivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ActivateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ActivateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_router_interface(
        self,
        request: vpc_20160428_models.ActivateRouterInterfaceRequest,
    ) -> vpc_20160428_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.activate_router_interface_with_options(request, runtime)

    async def activate_router_interface_async(
        self,
        request: vpc_20160428_models.ActivateRouterInterfaceRequest,
    ) -> vpc_20160428_models.ActivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.activate_router_interface_with_options_async(request, runtime)

    def active_flow_log_with_options(
        self,
        request: vpc_20160428_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ActiveFlowLogResponse().from_map(
            self.do_rpcrequest('ActiveFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def active_flow_log_with_options_async(
        self,
        request: vpc_20160428_models.ActiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ActiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ActiveFlowLogResponse().from_map(
            await self.do_rpcrequest_async('ActiveFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def active_flow_log(
        self,
        request: vpc_20160428_models.ActiveFlowLogRequest,
    ) -> vpc_20160428_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_flow_log_with_options(request, runtime)

    async def active_flow_log_async(
        self,
        request: vpc_20160428_models.ActiveFlowLogRequest,
    ) -> vpc_20160428_models.ActiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_flow_log_with_options_async(request, runtime)

    def add_bgp_network_with_options(
        self,
        request: vpc_20160428_models.AddBgpNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddBgpNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddBgpNetworkResponse().from_map(
            self.do_rpcrequest('AddBgpNetwork', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_bgp_network_with_options_async(
        self,
        request: vpc_20160428_models.AddBgpNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddBgpNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddBgpNetworkResponse().from_map(
            await self.do_rpcrequest_async('AddBgpNetwork', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_bgp_network(
        self,
        request: vpc_20160428_models.AddBgpNetworkRequest,
    ) -> vpc_20160428_models.AddBgpNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_bgp_network_with_options(request, runtime)

    async def add_bgp_network_async(
        self,
        request: vpc_20160428_models.AddBgpNetworkRequest,
    ) -> vpc_20160428_models.AddBgpNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_bgp_network_with_options_async(request, runtime)

    def add_common_bandwidth_package_ip_with_options(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddCommonBandwidthPackageIpResponse().from_map(
            self.do_rpcrequest('AddCommonBandwidthPackageIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_common_bandwidth_package_ip_with_options_async(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddCommonBandwidthPackageIpResponse().from_map(
            await self.do_rpcrequest_async('AddCommonBandwidthPackageIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_common_bandwidth_package_ip(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpRequest,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_common_bandwidth_package_ip_with_options(request, runtime)

    async def add_common_bandwidth_package_ip_async(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpRequest,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_common_bandwidth_package_ip_with_options_async(request, runtime)

    def add_common_bandwidth_package_ips_with_options(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddCommonBandwidthPackageIpsResponse().from_map(
            self.do_rpcrequest('AddCommonBandwidthPackageIps', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_common_bandwidth_package_ips_with_options_async(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddCommonBandwidthPackageIpsResponse().from_map(
            await self.do_rpcrequest_async('AddCommonBandwidthPackageIps', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_common_bandwidth_package_ips(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpsRequest,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_common_bandwidth_package_ips_with_options(request, runtime)

    async def add_common_bandwidth_package_ips_async(
        self,
        request: vpc_20160428_models.AddCommonBandwidthPackageIpsRequest,
    ) -> vpc_20160428_models.AddCommonBandwidthPackageIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_common_bandwidth_package_ips_with_options_async(request, runtime)

    def add_global_acceleration_instance_ip_with_options(
        self,
        request: vpc_20160428_models.AddGlobalAccelerationInstanceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse().from_map(
            self.do_rpcrequest('AddGlobalAccelerationInstanceIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_global_acceleration_instance_ip_with_options_async(
        self,
        request: vpc_20160428_models.AddGlobalAccelerationInstanceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse().from_map(
            await self.do_rpcrequest_async('AddGlobalAccelerationInstanceIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_global_acceleration_instance_ip(
        self,
        request: vpc_20160428_models.AddGlobalAccelerationInstanceIpRequest,
    ) -> vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_global_acceleration_instance_ip_with_options(request, runtime)

    async def add_global_acceleration_instance_ip_async(
        self,
        request: vpc_20160428_models.AddGlobalAccelerationInstanceIpRequest,
    ) -> vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_global_acceleration_instance_ip_with_options_async(request, runtime)

    def add_ipv_6translator_acl_list_entry_with_options(
        self,
        request: vpc_20160428_models.AddIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse().from_map(
            self.do_rpcrequest('AddIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_ipv_6translator_acl_list_entry_with_options_async(
        self,
        request: vpc_20160428_models.AddIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse().from_map(
            await self.do_rpcrequest_async('AddIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_ipv_6translator_acl_list_entry(
        self,
        request: vpc_20160428_models.AddIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ipv_6translator_acl_list_entry_with_options(request, runtime)

    async def add_ipv_6translator_acl_list_entry_async(
        self,
        request: vpc_20160428_models.AddIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ipv_6translator_acl_list_entry_with_options_async(request, runtime)

    def allocate_eip_address_with_options(
        self,
        request: vpc_20160428_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipAddressResponse().from_map(
            self.do_rpcrequest('AllocateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_eip_address_with_options_async(
        self,
        request: vpc_20160428_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_address(
        self,
        request: vpc_20160428_models.AllocateEipAddressRequest,
    ) -> vpc_20160428_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    async def allocate_eip_address_async(
        self,
        request: vpc_20160428_models.AllocateEipAddressRequest,
    ) -> vpc_20160428_models.AllocateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_eip_address_with_options_async(request, runtime)

    def allocate_eip_address_pro_with_options(
        self,
        request: vpc_20160428_models.AllocateEipAddressProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipAddressProResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipAddressProResponse().from_map(
            self.do_rpcrequest('AllocateEipAddressPro', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_eip_address_pro_with_options_async(
        self,
        request: vpc_20160428_models.AllocateEipAddressProRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipAddressProResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipAddressProResponse().from_map(
            await self.do_rpcrequest_async('AllocateEipAddressPro', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_address_pro(
        self,
        request: vpc_20160428_models.AllocateEipAddressProRequest,
    ) -> vpc_20160428_models.AllocateEipAddressProResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_pro_with_options(request, runtime)

    async def allocate_eip_address_pro_async(
        self,
        request: vpc_20160428_models.AllocateEipAddressProRequest,
    ) -> vpc_20160428_models.AllocateEipAddressProResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_eip_address_pro_with_options_async(request, runtime)

    def allocate_eip_segment_address_with_options(
        self,
        request: vpc_20160428_models.AllocateEipSegmentAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipSegmentAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipSegmentAddressResponse().from_map(
            self.do_rpcrequest('AllocateEipSegmentAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_eip_segment_address_with_options_async(
        self,
        request: vpc_20160428_models.AllocateEipSegmentAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipSegmentAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateEipSegmentAddressResponse().from_map(
            await self.do_rpcrequest_async('AllocateEipSegmentAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_eip_segment_address(
        self,
        request: vpc_20160428_models.AllocateEipSegmentAddressRequest,
    ) -> vpc_20160428_models.AllocateEipSegmentAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_segment_address_with_options(request, runtime)

    async def allocate_eip_segment_address_async(
        self,
        request: vpc_20160428_models.AllocateEipSegmentAddressRequest,
    ) -> vpc_20160428_models.AllocateEipSegmentAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_eip_segment_address_with_options_async(request, runtime)

    def allocate_ipv_6internet_bandwidth_with_options(
        self,
        request: vpc_20160428_models.AllocateIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateIpv6InternetBandwidthResponse().from_map(
            self.do_rpcrequest('AllocateIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_ipv_6internet_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.AllocateIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AllocateIpv6InternetBandwidthResponse().from_map(
            await self.do_rpcrequest_async('AllocateIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_ipv_6internet_bandwidth(
        self,
        request: vpc_20160428_models.AllocateIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.AllocateIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_ipv_6internet_bandwidth_with_options(request, runtime)

    async def allocate_ipv_6internet_bandwidth_async(
        self,
        request: vpc_20160428_models.AllocateIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.AllocateIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_ipv_6internet_bandwidth_with_options_async(request, runtime)

    def associate_eip_address_with_options(
        self,
        request: vpc_20160428_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateEipAddressResponse().from_map(
            self.do_rpcrequest('AssociateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_eip_address_with_options_async(
        self,
        request: vpc_20160428_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('AssociateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_eip_address(
        self,
        request: vpc_20160428_models.AssociateEipAddressRequest,
    ) -> vpc_20160428_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    async def associate_eip_address_async(
        self,
        request: vpc_20160428_models.AssociateEipAddressRequest,
    ) -> vpc_20160428_models.AssociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_eip_address_with_options_async(request, runtime)

    def associate_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.AssociateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse().from_map(
            self.do_rpcrequest('AssociateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_global_acceleration_instance_with_options_async(
        self,
        request: vpc_20160428_models.AssociateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse().from_map(
            await self.do_rpcrequest_async('AssociateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_global_acceleration_instance(
        self,
        request: vpc_20160428_models.AssociateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_global_acceleration_instance_with_options(request, runtime)

    async def associate_global_acceleration_instance_async(
        self,
        request: vpc_20160428_models.AssociateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_global_acceleration_instance_with_options_async(request, runtime)

    def associate_ha_vip_with_options(
        self,
        request: vpc_20160428_models.AssociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateHaVipResponse().from_map(
            self.do_rpcrequest('AssociateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_ha_vip_with_options_async(
        self,
        request: vpc_20160428_models.AssociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateHaVipResponse().from_map(
            await self.do_rpcrequest_async('AssociateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_ha_vip(
        self,
        request: vpc_20160428_models.AssociateHaVipRequest,
    ) -> vpc_20160428_models.AssociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_ha_vip_with_options(request, runtime)

    async def associate_ha_vip_async(
        self,
        request: vpc_20160428_models.AssociateHaVipRequest,
    ) -> vpc_20160428_models.AssociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_ha_vip_with_options_async(request, runtime)

    def associate_network_acl_with_options(
        self,
        request: vpc_20160428_models.AssociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateNetworkAclResponse().from_map(
            self.do_rpcrequest('AssociateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_network_acl_with_options_async(
        self,
        request: vpc_20160428_models.AssociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateNetworkAclResponse().from_map(
            await self.do_rpcrequest_async('AssociateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_network_acl(
        self,
        request: vpc_20160428_models.AssociateNetworkAclRequest,
    ) -> vpc_20160428_models.AssociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_network_acl_with_options(request, runtime)

    async def associate_network_acl_async(
        self,
        request: vpc_20160428_models.AssociateNetworkAclRequest,
    ) -> vpc_20160428_models.AssociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_network_acl_with_options_async(request, runtime)

    def associate_physical_connection_to_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('AssociatePhysicalConnectionToVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_physical_connection_to_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('AssociatePhysicalConnectionToVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_physical_connection_to_virtual_border_router(
        self,
        request: vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_physical_connection_to_virtual_border_router_with_options(request, runtime)

    async def associate_physical_connection_to_virtual_border_router_async(
        self,
        request: vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_physical_connection_to_virtual_border_router_with_options_async(request, runtime)

    def associate_route_table_with_options(
        self,
        request: vpc_20160428_models.AssociateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateRouteTableResponse().from_map(
            self.do_rpcrequest('AssociateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_route_table_with_options_async(
        self,
        request: vpc_20160428_models.AssociateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateRouteTableResponse().from_map(
            await self.do_rpcrequest_async('AssociateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_route_table(
        self,
        request: vpc_20160428_models.AssociateRouteTableRequest,
    ) -> vpc_20160428_models.AssociateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_route_table_with_options(request, runtime)

    async def associate_route_table_async(
        self,
        request: vpc_20160428_models.AssociateRouteTableRequest,
    ) -> vpc_20160428_models.AssociateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_route_table_with_options_async(request, runtime)

    def associate_vpc_cidr_block_with_options(
        self,
        request: vpc_20160428_models.AssociateVpcCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateVpcCidrBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateVpcCidrBlockResponse().from_map(
            self.do_rpcrequest('AssociateVpcCidrBlock', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_vpc_cidr_block_with_options_async(
        self,
        request: vpc_20160428_models.AssociateVpcCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateVpcCidrBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateVpcCidrBlockResponse().from_map(
            await self.do_rpcrequest_async('AssociateVpcCidrBlock', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_vpc_cidr_block(
        self,
        request: vpc_20160428_models.AssociateVpcCidrBlockRequest,
    ) -> vpc_20160428_models.AssociateVpcCidrBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_vpc_cidr_block_with_options(request, runtime)

    async def associate_vpc_cidr_block_async(
        self,
        request: vpc_20160428_models.AssociateVpcCidrBlockRequest,
    ) -> vpc_20160428_models.AssociateVpcCidrBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_vpc_cidr_block_with_options_async(request, runtime)

    def associate_vpn_gateway_with_certificate_with_options(
        self,
        request: vpc_20160428_models.AssociateVpnGatewayWithCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse().from_map(
            self.do_rpcrequest('AssociateVpnGatewayWithCertificate', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_vpn_gateway_with_certificate_with_options_async(
        self,
        request: vpc_20160428_models.AssociateVpnGatewayWithCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse().from_map(
            await self.do_rpcrequest_async('AssociateVpnGatewayWithCertificate', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_vpn_gateway_with_certificate(
        self,
        request: vpc_20160428_models.AssociateVpnGatewayWithCertificateRequest,
    ) -> vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_vpn_gateway_with_certificate_with_options(request, runtime)

    async def associate_vpn_gateway_with_certificate_async(
        self,
        request: vpc_20160428_models.AssociateVpnGatewayWithCertificateRequest,
    ) -> vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_vpn_gateway_with_certificate_with_options_async(request, runtime)

    def attach_dhcp_options_set_to_vpc_with_options(
        self,
        request: vpc_20160428_models.AttachDhcpOptionsSetToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse().from_map(
            self.do_rpcrequest('AttachDhcpOptionsSetToVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_dhcp_options_set_to_vpc_with_options_async(
        self,
        request: vpc_20160428_models.AttachDhcpOptionsSetToVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse().from_map(
            await self.do_rpcrequest_async('AttachDhcpOptionsSetToVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_dhcp_options_set_to_vpc(
        self,
        request: vpc_20160428_models.AttachDhcpOptionsSetToVpcRequest,
    ) -> vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_dhcp_options_set_to_vpc_with_options(request, runtime)

    async def attach_dhcp_options_set_to_vpc_async(
        self,
        request: vpc_20160428_models.AttachDhcpOptionsSetToVpcRequest,
    ) -> vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_dhcp_options_set_to_vpc_with_options_async(request, runtime)

    def cancel_common_bandwidth_package_ip_bandwidth_with_options(
        self,
        request: vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse().from_map(
            self.do_rpcrequest('CancelCommonBandwidthPackageIpBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_common_bandwidth_package_ip_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse().from_map(
            await self.do_rpcrequest_async('CancelCommonBandwidthPackageIpBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_common_bandwidth_package_ip_bandwidth(
        self,
        request: vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthRequest,
    ) -> vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_common_bandwidth_package_ip_bandwidth_with_options(request, runtime)

    async def cancel_common_bandwidth_package_ip_bandwidth_async(
        self,
        request: vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthRequest,
    ) -> vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_common_bandwidth_package_ip_bandwidth_with_options_async(request, runtime)

    def cancel_express_cloud_connection_with_options(
        self,
        request: vpc_20160428_models.CancelExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelExpressCloudConnectionResponse().from_map(
            self.do_rpcrequest('CancelExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_express_cloud_connection_with_options_async(
        self,
        request: vpc_20160428_models.CancelExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelExpressCloudConnectionResponse().from_map(
            await self.do_rpcrequest_async('CancelExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_express_cloud_connection(
        self,
        request: vpc_20160428_models.CancelExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.CancelExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_express_cloud_connection_with_options(request, runtime)

    async def cancel_express_cloud_connection_async(
        self,
        request: vpc_20160428_models.CancelExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.CancelExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_express_cloud_connection_with_options_async(request, runtime)

    def cancel_physical_connection_with_options(
        self,
        request: vpc_20160428_models.CancelPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('CancelPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.CancelPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CancelPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('CancelPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_physical_connection(
        self,
        request: vpc_20160428_models.CancelPhysicalConnectionRequest,
    ) -> vpc_20160428_models.CancelPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_physical_connection_with_options(request, runtime)

    async def cancel_physical_connection_async(
        self,
        request: vpc_20160428_models.CancelPhysicalConnectionRequest,
    ) -> vpc_20160428_models.CancelPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_physical_connection_with_options_async(request, runtime)

    def confirm_physical_connection_with_options(
        self,
        request: vpc_20160428_models.ConfirmPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConfirmPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConfirmPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('ConfirmPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def confirm_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.ConfirmPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConfirmPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConfirmPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('ConfirmPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def confirm_physical_connection(
        self,
        request: vpc_20160428_models.ConfirmPhysicalConnectionRequest,
    ) -> vpc_20160428_models.ConfirmPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.confirm_physical_connection_with_options(request, runtime)

    async def confirm_physical_connection_async(
        self,
        request: vpc_20160428_models.ConfirmPhysicalConnectionRequest,
    ) -> vpc_20160428_models.ConfirmPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.confirm_physical_connection_with_options_async(request, runtime)

    def connect_router_interface_with_options(
        self,
        request: vpc_20160428_models.ConnectRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConnectRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConnectRouterInterfaceResponse().from_map(
            self.do_rpcrequest('ConnectRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def connect_router_interface_with_options_async(
        self,
        request: vpc_20160428_models.ConnectRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConnectRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConnectRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('ConnectRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def connect_router_interface(
        self,
        request: vpc_20160428_models.ConnectRouterInterfaceRequest,
    ) -> vpc_20160428_models.ConnectRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.connect_router_interface_with_options(request, runtime)

    async def connect_router_interface_async(
        self,
        request: vpc_20160428_models.ConnectRouterInterfaceRequest,
    ) -> vpc_20160428_models.ConnectRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.connect_router_interface_with_options_async(request, runtime)

    def convert_bandwidth_package_with_options(
        self,
        request: vpc_20160428_models.ConvertBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConvertBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConvertBandwidthPackageResponse().from_map(
            self.do_rpcrequest('ConvertBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def convert_bandwidth_package_with_options_async(
        self,
        request: vpc_20160428_models.ConvertBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConvertBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ConvertBandwidthPackageResponse().from_map(
            await self.do_rpcrequest_async('ConvertBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_bandwidth_package(
        self,
        request: vpc_20160428_models.ConvertBandwidthPackageRequest,
    ) -> vpc_20160428_models.ConvertBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.convert_bandwidth_package_with_options(request, runtime)

    async def convert_bandwidth_package_async(
        self,
        request: vpc_20160428_models.ConvertBandwidthPackageRequest,
    ) -> vpc_20160428_models.ConvertBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.convert_bandwidth_package_with_options_async(request, runtime)

    def copy_network_acl_entries_with_options(
        self,
        request: vpc_20160428_models.CopyNetworkAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CopyNetworkAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CopyNetworkAclEntriesResponse().from_map(
            self.do_rpcrequest('CopyNetworkAclEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def copy_network_acl_entries_with_options_async(
        self,
        request: vpc_20160428_models.CopyNetworkAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CopyNetworkAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CopyNetworkAclEntriesResponse().from_map(
            await self.do_rpcrequest_async('CopyNetworkAclEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def copy_network_acl_entries(
        self,
        request: vpc_20160428_models.CopyNetworkAclEntriesRequest,
    ) -> vpc_20160428_models.CopyNetworkAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.copy_network_acl_entries_with_options(request, runtime)

    async def copy_network_acl_entries_async(
        self,
        request: vpc_20160428_models.CopyNetworkAclEntriesRequest,
    ) -> vpc_20160428_models.CopyNetworkAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.copy_network_acl_entries_with_options_async(request, runtime)

    def create_bgp_group_with_options(
        self,
        request: vpc_20160428_models.CreateBgpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateBgpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateBgpGroupResponse().from_map(
            self.do_rpcrequest('CreateBgpGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_bgp_group_with_options_async(
        self,
        request: vpc_20160428_models.CreateBgpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateBgpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateBgpGroupResponse().from_map(
            await self.do_rpcrequest_async('CreateBgpGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bgp_group(
        self,
        request: vpc_20160428_models.CreateBgpGroupRequest,
    ) -> vpc_20160428_models.CreateBgpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bgp_group_with_options(request, runtime)

    async def create_bgp_group_async(
        self,
        request: vpc_20160428_models.CreateBgpGroupRequest,
    ) -> vpc_20160428_models.CreateBgpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bgp_group_with_options_async(request, runtime)

    def create_bgp_peer_with_options(
        self,
        request: vpc_20160428_models.CreateBgpPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateBgpPeerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateBgpPeerResponse().from_map(
            self.do_rpcrequest('CreateBgpPeer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_bgp_peer_with_options_async(
        self,
        request: vpc_20160428_models.CreateBgpPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateBgpPeerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateBgpPeerResponse().from_map(
            await self.do_rpcrequest_async('CreateBgpPeer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bgp_peer(
        self,
        request: vpc_20160428_models.CreateBgpPeerRequest,
    ) -> vpc_20160428_models.CreateBgpPeerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_bgp_peer_with_options(request, runtime)

    async def create_bgp_peer_async(
        self,
        request: vpc_20160428_models.CreateBgpPeerRequest,
    ) -> vpc_20160428_models.CreateBgpPeerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_bgp_peer_with_options_async(request, runtime)

    def create_common_bandwidth_package_with_options(
        self,
        request: vpc_20160428_models.CreateCommonBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateCommonBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateCommonBandwidthPackageResponse().from_map(
            self.do_rpcrequest('CreateCommonBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_common_bandwidth_package_with_options_async(
        self,
        request: vpc_20160428_models.CreateCommonBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateCommonBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateCommonBandwidthPackageResponse().from_map(
            await self.do_rpcrequest_async('CreateCommonBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_common_bandwidth_package(
        self,
        request: vpc_20160428_models.CreateCommonBandwidthPackageRequest,
    ) -> vpc_20160428_models.CreateCommonBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_common_bandwidth_package_with_options(request, runtime)

    async def create_common_bandwidth_package_async(
        self,
        request: vpc_20160428_models.CreateCommonBandwidthPackageRequest,
    ) -> vpc_20160428_models.CreateCommonBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_common_bandwidth_package_with_options_async(request, runtime)

    def create_customer_gateway_with_options(
        self,
        request: vpc_20160428_models.CreateCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateCustomerGatewayResponse().from_map(
            self.do_rpcrequest('CreateCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_customer_gateway_with_options_async(
        self,
        request: vpc_20160428_models.CreateCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateCustomerGatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customer_gateway(
        self,
        request: vpc_20160428_models.CreateCustomerGatewayRequest,
    ) -> vpc_20160428_models.CreateCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_customer_gateway_with_options(request, runtime)

    async def create_customer_gateway_async(
        self,
        request: vpc_20160428_models.CreateCustomerGatewayRequest,
    ) -> vpc_20160428_models.CreateCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_customer_gateway_with_options_async(request, runtime)

    def create_dhcp_options_set_with_options(
        self,
        request: vpc_20160428_models.CreateDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateDhcpOptionsSetResponse().from_map(
            self.do_rpcrequest('CreateDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dhcp_options_set_with_options_async(
        self,
        request: vpc_20160428_models.CreateDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateDhcpOptionsSetResponse().from_map(
            await self.do_rpcrequest_async('CreateDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dhcp_options_set(
        self,
        request: vpc_20160428_models.CreateDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.CreateDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dhcp_options_set_with_options(request, runtime)

    async def create_dhcp_options_set_async(
        self,
        request: vpc_20160428_models.CreateDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.CreateDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dhcp_options_set_with_options_async(request, runtime)

    def create_express_cloud_connection_with_options(
        self,
        request: vpc_20160428_models.CreateExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateExpressCloudConnectionResponse().from_map(
            self.do_rpcrequest('CreateExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_express_cloud_connection_with_options_async(
        self,
        request: vpc_20160428_models.CreateExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateExpressCloudConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreateExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_express_cloud_connection(
        self,
        request: vpc_20160428_models.CreateExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.CreateExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_express_cloud_connection_with_options(request, runtime)

    async def create_express_cloud_connection_async(
        self,
        request: vpc_20160428_models.CreateExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.CreateExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_express_cloud_connection_with_options_async(request, runtime)

    def create_flow_log_with_options(
        self,
        request: vpc_20160428_models.CreateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateFlowLogResponse().from_map(
            self.do_rpcrequest('CreateFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_log_with_options_async(
        self,
        request: vpc_20160428_models.CreateFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateFlowLogResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_log(
        self,
        request: vpc_20160428_models.CreateFlowLogRequest,
    ) -> vpc_20160428_models.CreateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_log_with_options(request, runtime)

    async def create_flow_log_async(
        self,
        request: vpc_20160428_models.CreateFlowLogRequest,
    ) -> vpc_20160428_models.CreateFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_log_with_options_async(request, runtime)

    def create_forward_entry_with_options(
        self,
        request: vpc_20160428_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateForwardEntryResponse().from_map(
            self.do_rpcrequest('CreateForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_forward_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_forward_entry(
        self,
        request: vpc_20160428_models.CreateForwardEntryRequest,
    ) -> vpc_20160428_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_forward_entry_with_options(request, runtime)

    async def create_forward_entry_async(
        self,
        request: vpc_20160428_models.CreateForwardEntryRequest,
    ) -> vpc_20160428_models.CreateForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_forward_entry_with_options_async(request, runtime)

    def create_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.CreateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateGlobalAccelerationInstanceResponse().from_map(
            self.do_rpcrequest('CreateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_global_acceleration_instance_with_options_async(
        self,
        request: vpc_20160428_models.CreateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateGlobalAccelerationInstanceResponse().from_map(
            await self.do_rpcrequest_async('CreateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_global_acceleration_instance(
        self,
        request: vpc_20160428_models.CreateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.CreateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_global_acceleration_instance_with_options(request, runtime)

    async def create_global_acceleration_instance_async(
        self,
        request: vpc_20160428_models.CreateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.CreateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_global_acceleration_instance_with_options_async(request, runtime)

    def create_ha_vip_with_options(
        self,
        request: vpc_20160428_models.CreateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateHaVipResponse().from_map(
            self.do_rpcrequest('CreateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ha_vip_with_options_async(
        self,
        request: vpc_20160428_models.CreateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateHaVipResponse().from_map(
            await self.do_rpcrequest_async('CreateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ha_vip(
        self,
        request: vpc_20160428_models.CreateHaVipRequest,
    ) -> vpc_20160428_models.CreateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ha_vip_with_options(request, runtime)

    async def create_ha_vip_async(
        self,
        request: vpc_20160428_models.CreateHaVipRequest,
    ) -> vpc_20160428_models.CreateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ha_vip_with_options_async(request, runtime)

    def create_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.CreateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpsecServerResponse().from_map(
            self.do_rpcrequest('CreateIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipsec_server_with_options_async(
        self,
        request: vpc_20160428_models.CreateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpsecServerResponse().from_map(
            await self.do_rpcrequest_async('CreateIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipsec_server(
        self,
        request: vpc_20160428_models.CreateIpsecServerRequest,
    ) -> vpc_20160428_models.CreateIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipsec_server_with_options(request, runtime)

    async def create_ipsec_server_async(
        self,
        request: vpc_20160428_models.CreateIpsecServerRequest,
    ) -> vpc_20160428_models.CreateIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipsec_server_with_options_async(request, runtime)

    def create_ipv_6egress_only_rule_with_options(
        self,
        request: vpc_20160428_models.CreateIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse().from_map(
            self.do_rpcrequest('CreateIpv6EgressOnlyRule', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_6egress_only_rule_with_options_async(
        self,
        request: vpc_20160428_models.CreateIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateIpv6EgressOnlyRule', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_6egress_only_rule(
        self,
        request: vpc_20160428_models.CreateIpv6EgressOnlyRuleRequest,
    ) -> vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_6egress_only_rule_with_options(request, runtime)

    async def create_ipv_6egress_only_rule_async(
        self,
        request: vpc_20160428_models.CreateIpv6EgressOnlyRuleRequest,
    ) -> vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_6egress_only_rule_with_options_async(request, runtime)

    def create_ipv_6gateway_with_options(
        self,
        request: vpc_20160428_models.CreateIpv6GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv6GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpv6GatewayResponse().from_map(
            self.do_rpcrequest('CreateIpv6Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_6gateway_with_options_async(
        self,
        request: vpc_20160428_models.CreateIpv6GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv6GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIpv6GatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateIpv6Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_6gateway(
        self,
        request: vpc_20160428_models.CreateIpv6GatewayRequest,
    ) -> vpc_20160428_models.CreateIpv6GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_6gateway_with_options(request, runtime)

    async def create_ipv_6gateway_async(
        self,
        request: vpc_20160428_models.CreateIpv6GatewayRequest,
    ) -> vpc_20160428_models.CreateIpv6GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_6gateway_with_options_async(request, runtime)

    def create_ipv_6translator_with_options(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorResponse().from_map(
            self.do_rpcrequest('CreateIPv6Translator', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_6translator_with_options_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorResponse().from_map(
            await self.do_rpcrequest_async('CreateIPv6Translator', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_6translator(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_6translator_with_options(request, runtime)

    async def create_ipv_6translator_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_6translator_with_options_async(request, runtime)

    def create_ipv_6translator_acl_list_with_options(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorAclListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorAclListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorAclListResponse().from_map(
            self.do_rpcrequest('CreateIPv6TranslatorAclList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_6translator_acl_list_with_options_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorAclListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorAclListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorAclListResponse().from_map(
            await self.do_rpcrequest_async('CreateIPv6TranslatorAclList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_6translator_acl_list(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorAclListRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorAclListResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_6translator_acl_list_with_options(request, runtime)

    async def create_ipv_6translator_acl_list_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorAclListRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorAclListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_6translator_acl_list_with_options_async(request, runtime)

    def create_ipv_6translator_entry_with_options(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorEntryResponse().from_map(
            self.do_rpcrequest('CreateIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_6translator_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateIPv6TranslatorEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_6translator_entry(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_6translator_entry_with_options(request, runtime)

    async def create_ipv_6translator_entry_async(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.CreateIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_6translator_entry_with_options_async(request, runtime)

    def create_nat_gateway_with_options(
        self,
        request: vpc_20160428_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateNatGatewayResponse().from_map(
            self.do_rpcrequest('CreateNatGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nat_gateway_with_options_async(
        self,
        request: vpc_20160428_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateNatGatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateNatGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nat_gateway(
        self,
        request: vpc_20160428_models.CreateNatGatewayRequest,
    ) -> vpc_20160428_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nat_gateway_with_options(request, runtime)

    async def create_nat_gateway_async(
        self,
        request: vpc_20160428_models.CreateNatGatewayRequest,
    ) -> vpc_20160428_models.CreateNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_gateway_with_options_async(request, runtime)

    def create_network_acl_with_options(
        self,
        request: vpc_20160428_models.CreateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateNetworkAclResponse().from_map(
            self.do_rpcrequest('CreateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_network_acl_with_options_async(
        self,
        request: vpc_20160428_models.CreateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateNetworkAclResponse().from_map(
            await self.do_rpcrequest_async('CreateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_network_acl(
        self,
        request: vpc_20160428_models.CreateNetworkAclRequest,
    ) -> vpc_20160428_models.CreateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_network_acl_with_options(request, runtime)

    async def create_network_acl_async(
        self,
        request: vpc_20160428_models.CreateNetworkAclRequest,
    ) -> vpc_20160428_models.CreateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_network_acl_with_options_async(request, runtime)

    def create_physical_connection_occupancy_order_with_options(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse().from_map(
            self.do_rpcrequest('CreatePhysicalConnectionOccupancyOrder', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_physical_connection_occupancy_order_with_options_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse().from_map(
            await self.do_rpcrequest_async('CreatePhysicalConnectionOccupancyOrder', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_connection_occupancy_order(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_occupancy_order_with_options(request, runtime)

    async def create_physical_connection_occupancy_order_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_connection_occupancy_order_with_options_async(request, runtime)

    def create_route_entry_with_options(
        self,
        request: vpc_20160428_models.CreateRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateRouteEntryResponse().from_map(
            self.do_rpcrequest('CreateRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_route_entry(
        self,
        request: vpc_20160428_models.CreateRouteEntryRequest,
    ) -> vpc_20160428_models.CreateRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_route_entry_with_options(request, runtime)

    async def create_route_entry_async(
        self,
        request: vpc_20160428_models.CreateRouteEntryRequest,
    ) -> vpc_20160428_models.CreateRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_route_entry_with_options_async(request, runtime)

    def create_route_table_with_options(
        self,
        request: vpc_20160428_models.CreateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateRouteTableResponse().from_map(
            self.do_rpcrequest('CreateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_route_table_with_options_async(
        self,
        request: vpc_20160428_models.CreateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateRouteTableResponse().from_map(
            await self.do_rpcrequest_async('CreateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_route_table(
        self,
        request: vpc_20160428_models.CreateRouteTableRequest,
    ) -> vpc_20160428_models.CreateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_route_table_with_options(request, runtime)

    async def create_route_table_async(
        self,
        request: vpc_20160428_models.CreateRouteTableRequest,
    ) -> vpc_20160428_models.CreateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_route_table_with_options_async(request, runtime)

    def create_snat_entry_with_options(
        self,
        request: vpc_20160428_models.CreateSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSnatEntryResponse().from_map(
            self.do_rpcrequest('CreateSnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_snat_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSnatEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateSnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_snat_entry(
        self,
        request: vpc_20160428_models.CreateSnatEntryRequest,
    ) -> vpc_20160428_models.CreateSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_snat_entry_with_options(request, runtime)

    async def create_snat_entry_async(
        self,
        request: vpc_20160428_models.CreateSnatEntryRequest,
    ) -> vpc_20160428_models.CreateSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_snat_entry_with_options_async(request, runtime)

    def create_ssl_vpn_client_cert_with_options(
        self,
        request: vpc_20160428_models.CreateSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSslVpnClientCertResponse().from_map(
            self.do_rpcrequest('CreateSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ssl_vpn_client_cert_with_options_async(
        self,
        request: vpc_20160428_models.CreateSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSslVpnClientCertResponse().from_map(
            await self.do_rpcrequest_async('CreateSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ssl_vpn_client_cert(
        self,
        request: vpc_20160428_models.CreateSslVpnClientCertRequest,
    ) -> vpc_20160428_models.CreateSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ssl_vpn_client_cert_with_options(request, runtime)

    async def create_ssl_vpn_client_cert_async(
        self,
        request: vpc_20160428_models.CreateSslVpnClientCertRequest,
    ) -> vpc_20160428_models.CreateSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ssl_vpn_client_cert_with_options_async(request, runtime)

    def create_ssl_vpn_server_with_options(
        self,
        request: vpc_20160428_models.CreateSslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSslVpnServerResponse().from_map(
            self.do_rpcrequest('CreateSslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ssl_vpn_server_with_options_async(
        self,
        request: vpc_20160428_models.CreateSslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateSslVpnServerResponse().from_map(
            await self.do_rpcrequest_async('CreateSslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ssl_vpn_server(
        self,
        request: vpc_20160428_models.CreateSslVpnServerRequest,
    ) -> vpc_20160428_models.CreateSslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ssl_vpn_server_with_options(request, runtime)

    async def create_ssl_vpn_server_async(
        self,
        request: vpc_20160428_models.CreateSslVpnServerRequest,
    ) -> vpc_20160428_models.CreateSslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ssl_vpn_server_with_options_async(request, runtime)

    def create_vpc_with_options(
        self,
        request: vpc_20160428_models.CreateVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpcResponse().from_map(
            self.do_rpcrequest('CreateVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpc_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpcResponse().from_map(
            await self.do_rpcrequest_async('CreateVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc(
        self,
        request: vpc_20160428_models.CreateVpcRequest,
    ) -> vpc_20160428_models.CreateVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_with_options(request, runtime)

    async def create_vpc_async(
        self,
        request: vpc_20160428_models.CreateVpcRequest,
    ) -> vpc_20160428_models.CreateVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_with_options_async(request, runtime)

    def create_vpn_connection_with_options(
        self,
        request: vpc_20160428_models.CreateVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnConnectionResponse().from_map(
            self.do_rpcrequest('CreateVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpn_connection_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnConnectionResponse().from_map(
            await self.do_rpcrequest_async('CreateVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpn_connection(
        self,
        request: vpc_20160428_models.CreateVpnConnectionRequest,
    ) -> vpc_20160428_models.CreateVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpn_connection_with_options(request, runtime)

    async def create_vpn_connection_async(
        self,
        request: vpc_20160428_models.CreateVpnConnectionRequest,
    ) -> vpc_20160428_models.CreateVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpn_connection_with_options_async(request, runtime)

    def create_vpn_gateway_with_options(
        self,
        request: vpc_20160428_models.CreateVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnGatewayResponse().from_map(
            self.do_rpcrequest('CreateVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpn_gateway_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnGatewayResponse().from_map(
            await self.do_rpcrequest_async('CreateVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpn_gateway(
        self,
        request: vpc_20160428_models.CreateVpnGatewayRequest,
    ) -> vpc_20160428_models.CreateVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpn_gateway_with_options(request, runtime)

    async def create_vpn_gateway_async(
        self,
        request: vpc_20160428_models.CreateVpnGatewayRequest,
    ) -> vpc_20160428_models.CreateVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpn_gateway_with_options_async(request, runtime)

    def create_vpn_pbr_route_entry_with_options(
        self,
        request: vpc_20160428_models.CreateVpnPbrRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnPbrRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnPbrRouteEntryResponse().from_map(
            self.do_rpcrequest('CreateVpnPbrRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpn_pbr_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpnPbrRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnPbrRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnPbrRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateVpnPbrRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpn_pbr_route_entry(
        self,
        request: vpc_20160428_models.CreateVpnPbrRouteEntryRequest,
    ) -> vpc_20160428_models.CreateVpnPbrRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpn_pbr_route_entry_with_options(request, runtime)

    async def create_vpn_pbr_route_entry_async(
        self,
        request: vpc_20160428_models.CreateVpnPbrRouteEntryRequest,
    ) -> vpc_20160428_models.CreateVpnPbrRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpn_pbr_route_entry_with_options_async(request, runtime)

    def create_vpn_route_entry_with_options(
        self,
        request: vpc_20160428_models.CreateVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnRouteEntryResponse().from_map(
            self.do_rpcrequest('CreateVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpn_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVpnRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('CreateVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpn_route_entry(
        self,
        request: vpc_20160428_models.CreateVpnRouteEntryRequest,
    ) -> vpc_20160428_models.CreateVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpn_route_entry_with_options(request, runtime)

    async def create_vpn_route_entry_async(
        self,
        request: vpc_20160428_models.CreateVpnRouteEntryRequest,
    ) -> vpc_20160428_models.CreateVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpn_route_entry_with_options_async(request, runtime)

    def create_vswitch_with_options(
        self,
        request: vpc_20160428_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVSwitchResponse().from_map(
            self.do_rpcrequest('CreateVSwitch', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vswitch_with_options_async(
        self,
        request: vpc_20160428_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.CreateVSwitchResponse().from_map(
            await self.do_rpcrequest_async('CreateVSwitch', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vswitch(
        self,
        request: vpc_20160428_models.CreateVSwitchRequest,
    ) -> vpc_20160428_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    async def create_vswitch_async(
        self,
        request: vpc_20160428_models.CreateVSwitchRequest,
    ) -> vpc_20160428_models.CreateVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vswitch_with_options_async(request, runtime)

    def deactivate_router_interface_with_options(
        self,
        request: vpc_20160428_models.DeactivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeactivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeactivateRouterInterfaceResponse().from_map(
            self.do_rpcrequest('DeactivateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactivate_router_interface_with_options_async(
        self,
        request: vpc_20160428_models.DeactivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeactivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeactivateRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeactivateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactivate_router_interface(
        self,
        request: vpc_20160428_models.DeactivateRouterInterfaceRequest,
    ) -> vpc_20160428_models.DeactivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactivate_router_interface_with_options(request, runtime)

    async def deactivate_router_interface_async(
        self,
        request: vpc_20160428_models.DeactivateRouterInterfaceRequest,
    ) -> vpc_20160428_models.DeactivateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactivate_router_interface_with_options_async(request, runtime)

    def deactive_flow_log_with_options(
        self,
        request: vpc_20160428_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeactiveFlowLogResponse().from_map(
            self.do_rpcrequest('DeactiveFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deactive_flow_log_with_options_async(
        self,
        request: vpc_20160428_models.DeactiveFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeactiveFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeactiveFlowLogResponse().from_map(
            await self.do_rpcrequest_async('DeactiveFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deactive_flow_log(
        self,
        request: vpc_20160428_models.DeactiveFlowLogRequest,
    ) -> vpc_20160428_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.deactive_flow_log_with_options(request, runtime)

    async def deactive_flow_log_async(
        self,
        request: vpc_20160428_models.DeactiveFlowLogRequest,
    ) -> vpc_20160428_models.DeactiveFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deactive_flow_log_with_options_async(request, runtime)

    def delete_bgp_group_with_options(
        self,
        request: vpc_20160428_models.DeleteBgpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpGroupResponse().from_map(
            self.do_rpcrequest('DeleteBgpGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bgp_group_with_options_async(
        self,
        request: vpc_20160428_models.DeleteBgpGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpGroupResponse().from_map(
            await self.do_rpcrequest_async('DeleteBgpGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bgp_group(
        self,
        request: vpc_20160428_models.DeleteBgpGroupRequest,
    ) -> vpc_20160428_models.DeleteBgpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bgp_group_with_options(request, runtime)

    async def delete_bgp_group_async(
        self,
        request: vpc_20160428_models.DeleteBgpGroupRequest,
    ) -> vpc_20160428_models.DeleteBgpGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bgp_group_with_options_async(request, runtime)

    def delete_bgp_network_with_options(
        self,
        request: vpc_20160428_models.DeleteBgpNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpNetworkResponse().from_map(
            self.do_rpcrequest('DeleteBgpNetwork', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bgp_network_with_options_async(
        self,
        request: vpc_20160428_models.DeleteBgpNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpNetworkResponse().from_map(
            await self.do_rpcrequest_async('DeleteBgpNetwork', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bgp_network(
        self,
        request: vpc_20160428_models.DeleteBgpNetworkRequest,
    ) -> vpc_20160428_models.DeleteBgpNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bgp_network_with_options(request, runtime)

    async def delete_bgp_network_async(
        self,
        request: vpc_20160428_models.DeleteBgpNetworkRequest,
    ) -> vpc_20160428_models.DeleteBgpNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bgp_network_with_options_async(request, runtime)

    def delete_bgp_peer_with_options(
        self,
        request: vpc_20160428_models.DeleteBgpPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpPeerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpPeerResponse().from_map(
            self.do_rpcrequest('DeleteBgpPeer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_bgp_peer_with_options_async(
        self,
        request: vpc_20160428_models.DeleteBgpPeerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteBgpPeerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteBgpPeerResponse().from_map(
            await self.do_rpcrequest_async('DeleteBgpPeer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bgp_peer(
        self,
        request: vpc_20160428_models.DeleteBgpPeerRequest,
    ) -> vpc_20160428_models.DeleteBgpPeerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_bgp_peer_with_options(request, runtime)

    async def delete_bgp_peer_async(
        self,
        request: vpc_20160428_models.DeleteBgpPeerRequest,
    ) -> vpc_20160428_models.DeleteBgpPeerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_bgp_peer_with_options_async(request, runtime)

    def delete_common_bandwidth_package_with_options(
        self,
        request: vpc_20160428_models.DeleteCommonBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteCommonBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteCommonBandwidthPackageResponse().from_map(
            self.do_rpcrequest('DeleteCommonBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_common_bandwidth_package_with_options_async(
        self,
        request: vpc_20160428_models.DeleteCommonBandwidthPackageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteCommonBandwidthPackageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteCommonBandwidthPackageResponse().from_map(
            await self.do_rpcrequest_async('DeleteCommonBandwidthPackage', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_common_bandwidth_package(
        self,
        request: vpc_20160428_models.DeleteCommonBandwidthPackageRequest,
    ) -> vpc_20160428_models.DeleteCommonBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_common_bandwidth_package_with_options(request, runtime)

    async def delete_common_bandwidth_package_async(
        self,
        request: vpc_20160428_models.DeleteCommonBandwidthPackageRequest,
    ) -> vpc_20160428_models.DeleteCommonBandwidthPackageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_common_bandwidth_package_with_options_async(request, runtime)

    def delete_customer_gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteCustomerGatewayResponse().from_map(
            self.do_rpcrequest('DeleteCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_customer_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DeleteCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteCustomerGatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customer_gateway(
        self,
        request: vpc_20160428_models.DeleteCustomerGatewayRequest,
    ) -> vpc_20160428_models.DeleteCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_customer_gateway_with_options(request, runtime)

    async def delete_customer_gateway_async(
        self,
        request: vpc_20160428_models.DeleteCustomerGatewayRequest,
    ) -> vpc_20160428_models.DeleteCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_customer_gateway_with_options_async(request, runtime)

    def delete_dhcp_options_set_with_options(
        self,
        request: vpc_20160428_models.DeleteDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteDhcpOptionsSetResponse().from_map(
            self.do_rpcrequest('DeleteDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dhcp_options_set_with_options_async(
        self,
        request: vpc_20160428_models.DeleteDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteDhcpOptionsSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dhcp_options_set(
        self,
        request: vpc_20160428_models.DeleteDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.DeleteDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dhcp_options_set_with_options(request, runtime)

    async def delete_dhcp_options_set_async(
        self,
        request: vpc_20160428_models.DeleteDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.DeleteDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dhcp_options_set_with_options_async(request, runtime)

    def delete_express_cloud_connection_with_options(
        self,
        request: vpc_20160428_models.DeleteExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteExpressCloudConnectionResponse().from_map(
            self.do_rpcrequest('DeleteExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_express_cloud_connection_with_options_async(
        self,
        request: vpc_20160428_models.DeleteExpressCloudConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteExpressCloudConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteExpressCloudConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeleteExpressCloudConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_express_cloud_connection(
        self,
        request: vpc_20160428_models.DeleteExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.DeleteExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_express_cloud_connection_with_options(request, runtime)

    async def delete_express_cloud_connection_async(
        self,
        request: vpc_20160428_models.DeleteExpressCloudConnectionRequest,
    ) -> vpc_20160428_models.DeleteExpressCloudConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_express_cloud_connection_with_options_async(request, runtime)

    def delete_express_connect_with_options(
        self,
        request: vpc_20160428_models.DeleteExpressConnectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteExpressConnectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteExpressConnectResponse().from_map(
            self.do_rpcrequest('DeleteExpressConnect', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_express_connect_with_options_async(
        self,
        request: vpc_20160428_models.DeleteExpressConnectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteExpressConnectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteExpressConnectResponse().from_map(
            await self.do_rpcrequest_async('DeleteExpressConnect', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_express_connect(
        self,
        request: vpc_20160428_models.DeleteExpressConnectRequest,
    ) -> vpc_20160428_models.DeleteExpressConnectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_express_connect_with_options(request, runtime)

    async def delete_express_connect_async(
        self,
        request: vpc_20160428_models.DeleteExpressConnectRequest,
    ) -> vpc_20160428_models.DeleteExpressConnectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_express_connect_with_options_async(request, runtime)

    def delete_flow_log_with_options(
        self,
        request: vpc_20160428_models.DeleteFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteFlowLogResponse().from_map(
            self.do_rpcrequest('DeleteFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_log_with_options_async(
        self,
        request: vpc_20160428_models.DeleteFlowLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteFlowLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteFlowLogResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowLog', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_log(
        self,
        request: vpc_20160428_models.DeleteFlowLogRequest,
    ) -> vpc_20160428_models.DeleteFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_log_with_options(request, runtime)

    async def delete_flow_log_async(
        self,
        request: vpc_20160428_models.DeleteFlowLogRequest,
    ) -> vpc_20160428_models.DeleteFlowLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_log_with_options_async(request, runtime)

    def delete_forward_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteForwardEntryResponse().from_map(
            self.do_rpcrequest('DeleteForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_forward_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_forward_entry(
        self,
        request: vpc_20160428_models.DeleteForwardEntryRequest,
    ) -> vpc_20160428_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_forward_entry_with_options(request, runtime)

    async def delete_forward_entry_async(
        self,
        request: vpc_20160428_models.DeleteForwardEntryRequest,
    ) -> vpc_20160428_models.DeleteForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_forward_entry_with_options_async(request, runtime)

    def delete_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.DeleteGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse().from_map(
            self.do_rpcrequest('DeleteGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_global_acceleration_instance_with_options_async(
        self,
        request: vpc_20160428_models.DeleteGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse().from_map(
            await self.do_rpcrequest_async('DeleteGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_global_acceleration_instance(
        self,
        request: vpc_20160428_models.DeleteGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_global_acceleration_instance_with_options(request, runtime)

    async def delete_global_acceleration_instance_async(
        self,
        request: vpc_20160428_models.DeleteGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_global_acceleration_instance_with_options_async(request, runtime)

    def delete_ha_vip_with_options(
        self,
        request: vpc_20160428_models.DeleteHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteHaVipResponse().from_map(
            self.do_rpcrequest('DeleteHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ha_vip_with_options_async(
        self,
        request: vpc_20160428_models.DeleteHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteHaVipResponse().from_map(
            await self.do_rpcrequest_async('DeleteHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ha_vip(
        self,
        request: vpc_20160428_models.DeleteHaVipRequest,
    ) -> vpc_20160428_models.DeleteHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ha_vip_with_options(request, runtime)

    async def delete_ha_vip_async(
        self,
        request: vpc_20160428_models.DeleteHaVipRequest,
    ) -> vpc_20160428_models.DeleteHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ha_vip_with_options_async(request, runtime)

    def delete_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.DeleteIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpsecServerResponse().from_map(
            self.do_rpcrequest('DeleteIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipsec_server_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpsecServerResponse().from_map(
            await self.do_rpcrequest_async('DeleteIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipsec_server(
        self,
        request: vpc_20160428_models.DeleteIpsecServerRequest,
    ) -> vpc_20160428_models.DeleteIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipsec_server_with_options(request, runtime)

    async def delete_ipsec_server_async(
        self,
        request: vpc_20160428_models.DeleteIpsecServerRequest,
    ) -> vpc_20160428_models.DeleteIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipsec_server_with_options_async(request, runtime)

    def delete_ipv_6egress_only_rule_with_options(
        self,
        request: vpc_20160428_models.DeleteIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse().from_map(
            self.do_rpcrequest('DeleteIpv6EgressOnlyRule', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6egress_only_rule_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteIpv6EgressOnlyRule', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6egress_only_rule(
        self,
        request: vpc_20160428_models.DeleteIpv6EgressOnlyRuleRequest,
    ) -> vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6egress_only_rule_with_options(request, runtime)

    async def delete_ipv_6egress_only_rule_async(
        self,
        request: vpc_20160428_models.DeleteIpv6EgressOnlyRuleRequest,
    ) -> vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6egress_only_rule_with_options_async(request, runtime)

    def delete_ipv_6gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteIpv6GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6GatewayResponse().from_map(
            self.do_rpcrequest('DeleteIpv6Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6gateway_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIpv6GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6GatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteIpv6Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6gateway(
        self,
        request: vpc_20160428_models.DeleteIpv6GatewayRequest,
    ) -> vpc_20160428_models.DeleteIpv6GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6gateway_with_options(request, runtime)

    async def delete_ipv_6gateway_async(
        self,
        request: vpc_20160428_models.DeleteIpv6GatewayRequest,
    ) -> vpc_20160428_models.DeleteIpv6GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6gateway_with_options_async(request, runtime)

    def delete_ipv_6internet_bandwidth_with_options(
        self,
        request: vpc_20160428_models.DeleteIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6InternetBandwidthResponse().from_map(
            self.do_rpcrequest('DeleteIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6internet_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIpv6InternetBandwidthResponse().from_map(
            await self.do_rpcrequest_async('DeleteIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6internet_bandwidth(
        self,
        request: vpc_20160428_models.DeleteIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.DeleteIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6internet_bandwidth_with_options(request, runtime)

    async def delete_ipv_6internet_bandwidth_async(
        self,
        request: vpc_20160428_models.DeleteIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.DeleteIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6internet_bandwidth_with_options_async(request, runtime)

    def delete_ipv_6translator_with_options(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorResponse().from_map(
            self.do_rpcrequest('DeleteIPv6Translator', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6translator_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorResponse().from_map(
            await self.do_rpcrequest_async('DeleteIPv6Translator', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6translator(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6translator_with_options(request, runtime)

    async def delete_ipv_6translator_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6translator_with_options_async(request, runtime)

    def delete_ipv_6translator_acl_list_with_options(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorAclListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorAclListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorAclListResponse().from_map(
            self.do_rpcrequest('DeleteIPv6TranslatorAclList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6translator_acl_list_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorAclListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorAclListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorAclListResponse().from_map(
            await self.do_rpcrequest_async('DeleteIPv6TranslatorAclList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6translator_acl_list(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorAclListRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorAclListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6translator_acl_list_with_options(request, runtime)

    async def delete_ipv_6translator_acl_list_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorAclListRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorAclListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6translator_acl_list_with_options_async(request, runtime)

    def delete_ipv_6translator_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorEntryResponse().from_map(
            self.do_rpcrequest('DeleteIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_6translator_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteIPv6TranslatorEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_6translator_entry(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_6translator_entry_with_options(request, runtime)

    async def delete_ipv_6translator_entry_async(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_6translator_entry_with_options_async(request, runtime)

    def delete_nat_gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteNatGatewayResponse().from_map(
            self.do_rpcrequest('DeleteNatGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nat_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteNatGatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteNatGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nat_gateway(
        self,
        request: vpc_20160428_models.DeleteNatGatewayRequest,
    ) -> vpc_20160428_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_gateway_with_options(request, runtime)

    async def delete_nat_gateway_async(
        self,
        request: vpc_20160428_models.DeleteNatGatewayRequest,
    ) -> vpc_20160428_models.DeleteNatGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_gateway_with_options_async(request, runtime)

    def delete_network_acl_with_options(
        self,
        request: vpc_20160428_models.DeleteNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteNetworkAclResponse().from_map(
            self.do_rpcrequest('DeleteNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_network_acl_with_options_async(
        self,
        request: vpc_20160428_models.DeleteNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteNetworkAclResponse().from_map(
            await self.do_rpcrequest_async('DeleteNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_network_acl(
        self,
        request: vpc_20160428_models.DeleteNetworkAclRequest,
    ) -> vpc_20160428_models.DeleteNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_network_acl_with_options(request, runtime)

    async def delete_network_acl_async(
        self,
        request: vpc_20160428_models.DeleteNetworkAclRequest,
    ) -> vpc_20160428_models.DeleteNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_network_acl_with_options_async(request, runtime)

    def delete_physical_connection_with_options(
        self,
        request: vpc_20160428_models.DeletePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeletePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeletePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('DeletePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.DeletePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeletePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeletePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeletePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_physical_connection(
        self,
        request: vpc_20160428_models.DeletePhysicalConnectionRequest,
    ) -> vpc_20160428_models.DeletePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_physical_connection_with_options(request, runtime)

    async def delete_physical_connection_async(
        self,
        request: vpc_20160428_models.DeletePhysicalConnectionRequest,
    ) -> vpc_20160428_models.DeletePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_physical_connection_with_options_async(request, runtime)

    def delete_route_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouteEntryResponse().from_map(
            self.do_rpcrequest('DeleteRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_entry(
        self,
        request: vpc_20160428_models.DeleteRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_entry_with_options(request, runtime)

    async def delete_route_entry_async(
        self,
        request: vpc_20160428_models.DeleteRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_entry_with_options_async(request, runtime)

    def delete_router_interface_with_options(
        self,
        request: vpc_20160428_models.DeleteRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouterInterfaceResponse().from_map(
            self.do_rpcrequest('DeleteRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_router_interface_with_options_async(
        self,
        request: vpc_20160428_models.DeleteRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouterInterfaceResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_router_interface(
        self,
        request: vpc_20160428_models.DeleteRouterInterfaceRequest,
    ) -> vpc_20160428_models.DeleteRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_router_interface_with_options(request, runtime)

    async def delete_router_interface_async(
        self,
        request: vpc_20160428_models.DeleteRouterInterfaceRequest,
    ) -> vpc_20160428_models.DeleteRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_router_interface_with_options_async(request, runtime)

    def delete_route_table_with_options(
        self,
        request: vpc_20160428_models.DeleteRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouteTableResponse().from_map(
            self.do_rpcrequest('DeleteRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_route_table_with_options_async(
        self,
        request: vpc_20160428_models.DeleteRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteRouteTableResponse().from_map(
            await self.do_rpcrequest_async('DeleteRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_route_table(
        self,
        request: vpc_20160428_models.DeleteRouteTableRequest,
    ) -> vpc_20160428_models.DeleteRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_route_table_with_options(request, runtime)

    async def delete_route_table_async(
        self,
        request: vpc_20160428_models.DeleteRouteTableRequest,
    ) -> vpc_20160428_models.DeleteRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_route_table_with_options_async(request, runtime)

    def delete_snat_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSnatEntryResponse().from_map(
            self.do_rpcrequest('DeleteSnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_snat_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSnatEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteSnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_snat_entry(
        self,
        request: vpc_20160428_models.DeleteSnatEntryRequest,
    ) -> vpc_20160428_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_snat_entry_with_options(request, runtime)

    async def delete_snat_entry_async(
        self,
        request: vpc_20160428_models.DeleteSnatEntryRequest,
    ) -> vpc_20160428_models.DeleteSnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_snat_entry_with_options_async(request, runtime)

    def delete_ssl_vpn_client_cert_with_options(
        self,
        request: vpc_20160428_models.DeleteSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSslVpnClientCertResponse().from_map(
            self.do_rpcrequest('DeleteSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ssl_vpn_client_cert_with_options_async(
        self,
        request: vpc_20160428_models.DeleteSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSslVpnClientCertResponse().from_map(
            await self.do_rpcrequest_async('DeleteSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ssl_vpn_client_cert(
        self,
        request: vpc_20160428_models.DeleteSslVpnClientCertRequest,
    ) -> vpc_20160428_models.DeleteSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ssl_vpn_client_cert_with_options(request, runtime)

    async def delete_ssl_vpn_client_cert_async(
        self,
        request: vpc_20160428_models.DeleteSslVpnClientCertRequest,
    ) -> vpc_20160428_models.DeleteSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ssl_vpn_client_cert_with_options_async(request, runtime)

    def delete_ssl_vpn_server_with_options(
        self,
        request: vpc_20160428_models.DeleteSslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSslVpnServerResponse().from_map(
            self.do_rpcrequest('DeleteSslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ssl_vpn_server_with_options_async(
        self,
        request: vpc_20160428_models.DeleteSslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteSslVpnServerResponse().from_map(
            await self.do_rpcrequest_async('DeleteSslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ssl_vpn_server(
        self,
        request: vpc_20160428_models.DeleteSslVpnServerRequest,
    ) -> vpc_20160428_models.DeleteSslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ssl_vpn_server_with_options(request, runtime)

    async def delete_ssl_vpn_server_async(
        self,
        request: vpc_20160428_models.DeleteSslVpnServerRequest,
    ) -> vpc_20160428_models.DeleteSslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ssl_vpn_server_with_options_async(request, runtime)

    def delete_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.DeleteVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('DeleteVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('DeleteVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_virtual_border_router(
        self,
        request: vpc_20160428_models.DeleteVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.DeleteVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_virtual_border_router_with_options(request, runtime)

    async def delete_virtual_border_router_async(
        self,
        request: vpc_20160428_models.DeleteVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.DeleteVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_virtual_border_router_with_options_async(request, runtime)

    def delete_vpc_with_options(
        self,
        request: vpc_20160428_models.DeleteVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpcResponse().from_map(
            self.do_rpcrequest('DeleteVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpcResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc(
        self,
        request: vpc_20160428_models.DeleteVpcRequest,
    ) -> vpc_20160428_models.DeleteVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_with_options(request, runtime)

    async def delete_vpc_async(
        self,
        request: vpc_20160428_models.DeleteVpcRequest,
    ) -> vpc_20160428_models.DeleteVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_with_options_async(request, runtime)

    def delete_vpn_connection_with_options(
        self,
        request: vpc_20160428_models.DeleteVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnConnectionResponse().from_map(
            self.do_rpcrequest('DeleteVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpn_connection_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnConnectionResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpn_connection(
        self,
        request: vpc_20160428_models.DeleteVpnConnectionRequest,
    ) -> vpc_20160428_models.DeleteVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpn_connection_with_options(request, runtime)

    async def delete_vpn_connection_async(
        self,
        request: vpc_20160428_models.DeleteVpnConnectionRequest,
    ) -> vpc_20160428_models.DeleteVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpn_connection_with_options_async(request, runtime)

    def delete_vpn_gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnGatewayResponse().from_map(
            self.do_rpcrequest('DeleteVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpn_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnGatewayResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpn_gateway(
        self,
        request: vpc_20160428_models.DeleteVpnGatewayRequest,
    ) -> vpc_20160428_models.DeleteVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpn_gateway_with_options(request, runtime)

    async def delete_vpn_gateway_async(
        self,
        request: vpc_20160428_models.DeleteVpnGatewayRequest,
    ) -> vpc_20160428_models.DeleteVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpn_gateway_with_options_async(request, runtime)

    def delete_vpn_pbr_route_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteVpnPbrRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnPbrRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnPbrRouteEntryResponse().from_map(
            self.do_rpcrequest('DeleteVpnPbrRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpn_pbr_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpnPbrRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnPbrRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnPbrRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpnPbrRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpn_pbr_route_entry(
        self,
        request: vpc_20160428_models.DeleteVpnPbrRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteVpnPbrRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpn_pbr_route_entry_with_options(request, runtime)

    async def delete_vpn_pbr_route_entry_async(
        self,
        request: vpc_20160428_models.DeleteVpnPbrRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteVpnPbrRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpn_pbr_route_entry_with_options_async(request, runtime)

    def delete_vpn_route_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnRouteEntryResponse().from_map(
            self.do_rpcrequest('DeleteVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpn_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVpnRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('DeleteVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpn_route_entry(
        self,
        request: vpc_20160428_models.DeleteVpnRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpn_route_entry_with_options(request, runtime)

    async def delete_vpn_route_entry_async(
        self,
        request: vpc_20160428_models.DeleteVpnRouteEntryRequest,
    ) -> vpc_20160428_models.DeleteVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpn_route_entry_with_options_async(request, runtime)

    def delete_vswitch_with_options(
        self,
        request: vpc_20160428_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVSwitchResponse().from_map(
            self.do_rpcrequest('DeleteVSwitch', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vswitch_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeleteVSwitchResponse().from_map(
            await self.do_rpcrequest_async('DeleteVSwitch', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vswitch(
        self,
        request: vpc_20160428_models.DeleteVSwitchRequest,
    ) -> vpc_20160428_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    async def delete_vswitch_async(
        self,
        request: vpc_20160428_models.DeleteVSwitchRequest,
    ) -> vpc_20160428_models.DeleteVSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vswitch_with_options_async(request, runtime)

    def deletion_protection_with_options(
        self,
        request: vpc_20160428_models.DeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeletionProtectionResponse().from_map(
            self.do_rpcrequest('DeletionProtection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deletion_protection_with_options_async(
        self,
        request: vpc_20160428_models.DeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DeletionProtectionResponse().from_map(
            await self.do_rpcrequest_async('DeletionProtection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deletion_protection(
        self,
        request: vpc_20160428_models.DeletionProtectionRequest,
    ) -> vpc_20160428_models.DeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.deletion_protection_with_options(request, runtime)

    async def deletion_protection_async(
        self,
        request: vpc_20160428_models.DeletionProtectionRequest,
    ) -> vpc_20160428_models.DeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deletion_protection_with_options_async(request, runtime)

    def describe_access_points_with_options(
        self,
        request: vpc_20160428_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeAccessPointsResponse().from_map(
            self.do_rpcrequest('DescribeAccessPoints', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_access_points_with_options_async(
        self,
        request: vpc_20160428_models.DescribeAccessPointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeAccessPointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeAccessPointsResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccessPoints', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_points(
        self,
        request: vpc_20160428_models.DescribeAccessPointsRequest,
    ) -> vpc_20160428_models.DescribeAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_access_points_with_options(request, runtime)

    async def describe_access_points_async(
        self,
        request: vpc_20160428_models.DescribeAccessPointsRequest,
    ) -> vpc_20160428_models.DescribeAccessPointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_access_points_with_options_async(request, runtime)

    def describe_bgp_groups_with_options(
        self,
        request: vpc_20160428_models.DescribeBgpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpGroupsResponse().from_map(
            self.do_rpcrequest('DescribeBgpGroups', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_groups_with_options_async(
        self,
        request: vpc_20160428_models.DescribeBgpGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpGroupsResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpGroups', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_groups(
        self,
        request: vpc_20160428_models.DescribeBgpGroupsRequest,
    ) -> vpc_20160428_models.DescribeBgpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_groups_with_options(request, runtime)

    async def describe_bgp_groups_async(
        self,
        request: vpc_20160428_models.DescribeBgpGroupsRequest,
    ) -> vpc_20160428_models.DescribeBgpGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_groups_with_options_async(request, runtime)

    def describe_bgp_networks_with_options(
        self,
        request: vpc_20160428_models.DescribeBgpNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpNetworksResponse().from_map(
            self.do_rpcrequest('DescribeBgpNetworks', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_networks_with_options_async(
        self,
        request: vpc_20160428_models.DescribeBgpNetworksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpNetworksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpNetworksResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpNetworks', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_networks(
        self,
        request: vpc_20160428_models.DescribeBgpNetworksRequest,
    ) -> vpc_20160428_models.DescribeBgpNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_networks_with_options(request, runtime)

    async def describe_bgp_networks_async(
        self,
        request: vpc_20160428_models.DescribeBgpNetworksRequest,
    ) -> vpc_20160428_models.DescribeBgpNetworksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_networks_with_options_async(request, runtime)

    def describe_bgp_peers_with_options(
        self,
        request: vpc_20160428_models.DescribeBgpPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpPeersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpPeersResponse().from_map(
            self.do_rpcrequest('DescribeBgpPeers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_bgp_peers_with_options_async(
        self,
        request: vpc_20160428_models.DescribeBgpPeersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeBgpPeersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeBgpPeersResponse().from_map(
            await self.do_rpcrequest_async('DescribeBgpPeers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bgp_peers(
        self,
        request: vpc_20160428_models.DescribeBgpPeersRequest,
    ) -> vpc_20160428_models.DescribeBgpPeersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_bgp_peers_with_options(request, runtime)

    async def describe_bgp_peers_async(
        self,
        request: vpc_20160428_models.DescribeBgpPeersRequest,
    ) -> vpc_20160428_models.DescribeBgpPeersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_bgp_peers_with_options_async(request, runtime)

    def describe_common_bandwidth_packages_with_options(
        self,
        request: vpc_20160428_models.DescribeCommonBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCommonBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCommonBandwidthPackagesResponse().from_map(
            self.do_rpcrequest('DescribeCommonBandwidthPackages', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_common_bandwidth_packages_with_options_async(
        self,
        request: vpc_20160428_models.DescribeCommonBandwidthPackagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCommonBandwidthPackagesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCommonBandwidthPackagesResponse().from_map(
            await self.do_rpcrequest_async('DescribeCommonBandwidthPackages', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_common_bandwidth_packages(
        self,
        request: vpc_20160428_models.DescribeCommonBandwidthPackagesRequest,
    ) -> vpc_20160428_models.DescribeCommonBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_common_bandwidth_packages_with_options(request, runtime)

    async def describe_common_bandwidth_packages_async(
        self,
        request: vpc_20160428_models.DescribeCommonBandwidthPackagesRequest,
    ) -> vpc_20160428_models.DescribeCommonBandwidthPackagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_common_bandwidth_packages_with_options_async(request, runtime)

    def describe_customer_gateway_with_options(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCustomerGatewayResponse().from_map(
            self.do_rpcrequest('DescribeCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_customer_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCustomerGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCustomerGatewayResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomerGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_customer_gateway(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewayRequest,
    ) -> vpc_20160428_models.DescribeCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customer_gateway_with_options(request, runtime)

    async def describe_customer_gateway_async(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewayRequest,
    ) -> vpc_20160428_models.DescribeCustomerGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customer_gateway_with_options_async(request, runtime)

    def describe_customer_gateways_with_options(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCustomerGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCustomerGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeCustomerGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_customer_gateways_with_options_async(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeCustomerGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeCustomerGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeCustomerGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_customer_gateways(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewaysRequest,
    ) -> vpc_20160428_models.DescribeCustomerGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_customer_gateways_with_options(request, runtime)

    async def describe_customer_gateways_async(
        self,
        request: vpc_20160428_models.DescribeCustomerGatewaysRequest,
    ) -> vpc_20160428_models.DescribeCustomerGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_customer_gateways_with_options_async(request, runtime)

    def describe_eip_addresses_with_options(
        self,
        request: vpc_20160428_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipAddressesResponse().from_map(
            self.do_rpcrequest('DescribeEipAddresses', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_addresses_with_options_async(
        self,
        request: vpc_20160428_models.DescribeEipAddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipAddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipAddressesResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipAddresses', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_addresses(
        self,
        request: vpc_20160428_models.DescribeEipAddressesRequest,
    ) -> vpc_20160428_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    async def describe_eip_addresses_async(
        self,
        request: vpc_20160428_models.DescribeEipAddressesRequest,
    ) -> vpc_20160428_models.DescribeEipAddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_addresses_with_options_async(request, runtime)

    def describe_eip_gateway_info_with_options(
        self,
        request: vpc_20160428_models.DescribeEipGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipGatewayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipGatewayInfoResponse().from_map(
            self.do_rpcrequest('DescribeEipGatewayInfo', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_gateway_info_with_options_async(
        self,
        request: vpc_20160428_models.DescribeEipGatewayInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipGatewayInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipGatewayInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipGatewayInfo', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_gateway_info(
        self,
        request: vpc_20160428_models.DescribeEipGatewayInfoRequest,
    ) -> vpc_20160428_models.DescribeEipGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_gateway_info_with_options(request, runtime)

    async def describe_eip_gateway_info_async(
        self,
        request: vpc_20160428_models.DescribeEipGatewayInfoRequest,
    ) -> vpc_20160428_models.DescribeEipGatewayInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_gateway_info_with_options_async(request, runtime)

    def describe_eip_monitor_data_with_options(
        self,
        request: vpc_20160428_models.DescribeEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeEipMonitorData', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_monitor_data_with_options_async(
        self,
        request: vpc_20160428_models.DescribeEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipMonitorData', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_monitor_data(
        self,
        request: vpc_20160428_models.DescribeEipMonitorDataRequest,
    ) -> vpc_20160428_models.DescribeEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_monitor_data_with_options(request, runtime)

    async def describe_eip_monitor_data_async(
        self,
        request: vpc_20160428_models.DescribeEipMonitorDataRequest,
    ) -> vpc_20160428_models.DescribeEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_monitor_data_with_options_async(request, runtime)

    def describe_eip_segment_with_options(
        self,
        request: vpc_20160428_models.DescribeEipSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipSegmentResponse().from_map(
            self.do_rpcrequest('DescribeEipSegment', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_eip_segment_with_options_async(
        self,
        request: vpc_20160428_models.DescribeEipSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeEipSegmentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeEipSegmentResponse().from_map(
            await self.do_rpcrequest_async('DescribeEipSegment', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_eip_segment(
        self,
        request: vpc_20160428_models.DescribeEipSegmentRequest,
    ) -> vpc_20160428_models.DescribeEipSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_segment_with_options(request, runtime)

    async def describe_eip_segment_async(
        self,
        request: vpc_20160428_models.DescribeEipSegmentRequest,
    ) -> vpc_20160428_models.DescribeEipSegmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eip_segment_with_options_async(request, runtime)

    def describe_express_cloud_connections_with_options(
        self,
        request: vpc_20160428_models.DescribeExpressCloudConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeExpressCloudConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeExpressCloudConnectionsResponse().from_map(
            self.do_rpcrequest('DescribeExpressCloudConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_express_cloud_connections_with_options_async(
        self,
        request: vpc_20160428_models.DescribeExpressCloudConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeExpressCloudConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeExpressCloudConnectionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeExpressCloudConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_express_cloud_connections(
        self,
        request: vpc_20160428_models.DescribeExpressCloudConnectionsRequest,
    ) -> vpc_20160428_models.DescribeExpressCloudConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_express_cloud_connections_with_options(request, runtime)

    async def describe_express_cloud_connections_async(
        self,
        request: vpc_20160428_models.DescribeExpressCloudConnectionsRequest,
    ) -> vpc_20160428_models.DescribeExpressCloudConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_express_cloud_connections_with_options_async(request, runtime)

    def describe_flow_logs_with_options(
        self,
        request: vpc_20160428_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeFlowLogsResponse().from_map(
            self.do_rpcrequest('DescribeFlowLogs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_logs_with_options_async(
        self,
        request: vpc_20160428_models.DescribeFlowLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeFlowLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeFlowLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowLogs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_logs(
        self,
        request: vpc_20160428_models.DescribeFlowLogsRequest,
    ) -> vpc_20160428_models.DescribeFlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_logs_with_options(request, runtime)

    async def describe_flow_logs_async(
        self,
        request: vpc_20160428_models.DescribeFlowLogsRequest,
    ) -> vpc_20160428_models.DescribeFlowLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_logs_with_options_async(request, runtime)

    def describe_forward_table_entries_with_options(
        self,
        request: vpc_20160428_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeForwardTableEntriesResponse().from_map(
            self.do_rpcrequest('DescribeForwardTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_forward_table_entries_with_options_async(
        self,
        request: vpc_20160428_models.DescribeForwardTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeForwardTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeForwardTableEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeForwardTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_forward_table_entries(
        self,
        request: vpc_20160428_models.DescribeForwardTableEntriesRequest,
    ) -> vpc_20160428_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_forward_table_entries_with_options(request, runtime)

    async def describe_forward_table_entries_async(
        self,
        request: vpc_20160428_models.DescribeForwardTableEntriesRequest,
    ) -> vpc_20160428_models.DescribeForwardTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_forward_table_entries_with_options_async(request, runtime)

    def describe_global_acceleration_instances_with_options(
        self,
        request: vpc_20160428_models.DescribeGlobalAccelerationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse().from_map(
            self.do_rpcrequest('DescribeGlobalAccelerationInstances', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_global_acceleration_instances_with_options_async(
        self,
        request: vpc_20160428_models.DescribeGlobalAccelerationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeGlobalAccelerationInstances', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_global_acceleration_instances(
        self,
        request: vpc_20160428_models.DescribeGlobalAccelerationInstancesRequest,
    ) -> vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_global_acceleration_instances_with_options(request, runtime)

    async def describe_global_acceleration_instances_async(
        self,
        request: vpc_20160428_models.DescribeGlobalAccelerationInstancesRequest,
    ) -> vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_global_acceleration_instances_with_options_async(request, runtime)

    def describe_grant_rules_to_cen_with_options(
        self,
        request: vpc_20160428_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeGrantRulesToCenResponse().from_map(
            self.do_rpcrequest('DescribeGrantRulesToCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_grant_rules_to_cen_with_options_async(
        self,
        request: vpc_20160428_models.DescribeGrantRulesToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeGrantRulesToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeGrantRulesToCenResponse().from_map(
            await self.do_rpcrequest_async('DescribeGrantRulesToCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_grant_rules_to_cen(
        self,
        request: vpc_20160428_models.DescribeGrantRulesToCenRequest,
    ) -> vpc_20160428_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    async def describe_grant_rules_to_cen_async(
        self,
        request: vpc_20160428_models.DescribeGrantRulesToCenRequest,
    ) -> vpc_20160428_models.DescribeGrantRulesToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_grant_rules_to_cen_with_options_async(request, runtime)

    def describe_ha_vips_with_options(
        self,
        request: vpc_20160428_models.DescribeHaVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeHaVipsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeHaVipsResponse().from_map(
            self.do_rpcrequest('DescribeHaVips', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ha_vips_with_options_async(
        self,
        request: vpc_20160428_models.DescribeHaVipsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeHaVipsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeHaVipsResponse().from_map(
            await self.do_rpcrequest_async('DescribeHaVips', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ha_vips(
        self,
        request: vpc_20160428_models.DescribeHaVipsRequest,
    ) -> vpc_20160428_models.DescribeHaVipsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ha_vips_with_options(request, runtime)

    async def describe_ha_vips_async(
        self,
        request: vpc_20160428_models.DescribeHaVipsRequest,
    ) -> vpc_20160428_models.DescribeHaVipsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ha_vips_with_options_async(request, runtime)

    def describe_high_definition_monitor_log_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse().from_map(
            self.do_rpcrequest('DescribeHighDefinitionMonitorLogAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_high_definition_monitor_log_attribute_with_options_async(
        self,
        request: vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeHighDefinitionMonitorLogAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_high_definition_monitor_log_attribute(
        self,
        request: vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeRequest,
    ) -> vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_high_definition_monitor_log_attribute_with_options(request, runtime)

    async def describe_high_definition_monitor_log_attribute_async(
        self,
        request: vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeRequest,
    ) -> vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_high_definition_monitor_log_attribute_with_options_async(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            self.do_rpcrequest('DescribeInstanceAutoRenewAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_auto_renew_attribute_with_options_async(
        self,
        request: vpc_20160428_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeInstanceAutoRenewAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_auto_renew_attribute(
        self,
        request: vpc_20160428_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    async def describe_instance_auto_renew_attribute_async(
        self,
        request: vpc_20160428_models.DescribeInstanceAutoRenewAttributeRequest,
    ) -> vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_auto_renew_attribute_with_options_async(request, runtime)

    def describe_ipv_6addresses_with_options(
        self,
        request: vpc_20160428_models.DescribeIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6AddressesResponse().from_map(
            self.do_rpcrequest('DescribeIpv6Addresses', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6addresses_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIpv6AddressesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6AddressesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6AddressesResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpv6Addresses', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6addresses(
        self,
        request: vpc_20160428_models.DescribeIpv6AddressesRequest,
    ) -> vpc_20160428_models.DescribeIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6addresses_with_options(request, runtime)

    async def describe_ipv_6addresses_async(
        self,
        request: vpc_20160428_models.DescribeIpv6AddressesRequest,
    ) -> vpc_20160428_models.DescribeIpv6AddressesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6addresses_with_options_async(request, runtime)

    def describe_ipv_6egress_only_rules_with_options(
        self,
        request: vpc_20160428_models.DescribeIpv6EgressOnlyRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse().from_map(
            self.do_rpcrequest('DescribeIpv6EgressOnlyRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6egress_only_rules_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIpv6EgressOnlyRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpv6EgressOnlyRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6egress_only_rules(
        self,
        request: vpc_20160428_models.DescribeIpv6EgressOnlyRulesRequest,
    ) -> vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6egress_only_rules_with_options(request, runtime)

    async def describe_ipv_6egress_only_rules_async(
        self,
        request: vpc_20160428_models.DescribeIpv6EgressOnlyRulesRequest,
    ) -> vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6egress_only_rules_with_options_async(request, runtime)

    def describe_ipv_6gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6GatewayAttributeResponse().from_map(
            self.do_rpcrequest('DescribeIpv6GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6GatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpv6GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6gateway_attribute(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewayAttributeRequest,
    ) -> vpc_20160428_models.DescribeIpv6GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6gateway_attribute_with_options(request, runtime)

    async def describe_ipv_6gateway_attribute_async(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewayAttributeRequest,
    ) -> vpc_20160428_models.DescribeIpv6GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6gateway_attribute_with_options_async(request, runtime)

    def describe_ipv_6gateways_with_options(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6GatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6GatewaysResponse().from_map(
            self.do_rpcrequest('DescribeIpv6Gateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6gateways_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIpv6GatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIpv6GatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeIpv6Gateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6gateways(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewaysRequest,
    ) -> vpc_20160428_models.DescribeIpv6GatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6gateways_with_options(request, runtime)

    async def describe_ipv_6gateways_async(
        self,
        request: vpc_20160428_models.DescribeIpv6GatewaysRequest,
    ) -> vpc_20160428_models.DescribeIpv6GatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6gateways_with_options_async(request, runtime)

    def describe_ipv_6translator_acl_list_attributes_with_options(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse().from_map(
            self.do_rpcrequest('DescribeIPv6TranslatorAclListAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6translator_acl_list_attributes_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeIPv6TranslatorAclListAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6translator_acl_list_attributes(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6translator_acl_list_attributes_with_options(request, runtime)

    async def describe_ipv_6translator_acl_list_attributes_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6translator_acl_list_attributes_with_options_async(request, runtime)

    def describe_ipv_6translator_acl_lists_with_options(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse().from_map(
            self.do_rpcrequest('DescribeIPv6TranslatorAclLists', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6translator_acl_lists_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse().from_map(
            await self.do_rpcrequest_async('DescribeIPv6TranslatorAclLists', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6translator_acl_lists(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListsRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6translator_acl_lists_with_options(request, runtime)

    async def describe_ipv_6translator_acl_lists_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListsRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6translator_acl_lists_with_options_async(request, runtime)

    def describe_ipv_6translator_entries_with_options(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse().from_map(
            self.do_rpcrequest('DescribeIPv6TranslatorEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6translator_entries_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeIPv6TranslatorEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6translator_entries(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorEntriesRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6translator_entries_with_options(request, runtime)

    async def describe_ipv_6translator_entries_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorEntriesRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6translator_entries_with_options_async(request, runtime)

    def describe_ipv_6translators_with_options(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorsResponse().from_map(
            self.do_rpcrequest('DescribeIPv6Translators', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ipv_6translators_with_options_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeIPv6TranslatorsResponse().from_map(
            await self.do_rpcrequest_async('DescribeIPv6Translators', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ipv_6translators(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorsRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ipv_6translators_with_options(request, runtime)

    async def describe_ipv_6translators_async(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorsRequest,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ipv_6translators_with_options_async(request, runtime)

    def describe_nat_gateways_with_options(
        self,
        request: vpc_20160428_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNatGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeNatGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_nat_gateways_with_options_async(
        self,
        request: vpc_20160428_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNatGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeNatGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_nat_gateways(
        self,
        request: vpc_20160428_models.DescribeNatGatewaysRequest,
    ) -> vpc_20160428_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_nat_gateways_with_options(request, runtime)

    async def describe_nat_gateways_async(
        self,
        request: vpc_20160428_models.DescribeNatGatewaysRequest,
    ) -> vpc_20160428_models.DescribeNatGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_nat_gateways_with_options_async(request, runtime)

    def describe_network_acl_attributes_with_options(
        self,
        request: vpc_20160428_models.DescribeNetworkAclAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNetworkAclAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNetworkAclAttributesResponse().from_map(
            self.do_rpcrequest('DescribeNetworkAclAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_acl_attributes_with_options_async(
        self,
        request: vpc_20160428_models.DescribeNetworkAclAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNetworkAclAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNetworkAclAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkAclAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_acl_attributes(
        self,
        request: vpc_20160428_models.DescribeNetworkAclAttributesRequest,
    ) -> vpc_20160428_models.DescribeNetworkAclAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_acl_attributes_with_options(request, runtime)

    async def describe_network_acl_attributes_async(
        self,
        request: vpc_20160428_models.DescribeNetworkAclAttributesRequest,
    ) -> vpc_20160428_models.DescribeNetworkAclAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_acl_attributes_with_options_async(request, runtime)

    def describe_network_acls_with_options(
        self,
        request: vpc_20160428_models.DescribeNetworkAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNetworkAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNetworkAclsResponse().from_map(
            self.do_rpcrequest('DescribeNetworkAcls', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_network_acls_with_options_async(
        self,
        request: vpc_20160428_models.DescribeNetworkAclsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNetworkAclsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNetworkAclsResponse().from_map(
            await self.do_rpcrequest_async('DescribeNetworkAcls', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_network_acls(
        self,
        request: vpc_20160428_models.DescribeNetworkAclsRequest,
    ) -> vpc_20160428_models.DescribeNetworkAclsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_network_acls_with_options(request, runtime)

    async def describe_network_acls_async(
        self,
        request: vpc_20160428_models.DescribeNetworkAclsRequest,
    ) -> vpc_20160428_models.DescribeNetworkAclsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_network_acls_with_options_async(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(
        self,
        request: vpc_20160428_models.DescribeNewProjectEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse().from_map(
            self.do_rpcrequest('DescribeNewProjectEipMonitorData', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_new_project_eip_monitor_data_with_options_async(
        self,
        request: vpc_20160428_models.DescribeNewProjectEipMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse().from_map(
            await self.do_rpcrequest_async('DescribeNewProjectEipMonitorData', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_new_project_eip_monitor_data(
        self,
        request: vpc_20160428_models.DescribeNewProjectEipMonitorDataRequest,
    ) -> vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    async def describe_new_project_eip_monitor_data_async(
        self,
        request: vpc_20160428_models.DescribeNewProjectEipMonitorDataRequest,
    ) -> vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_new_project_eip_monitor_data_with_options_async(request, runtime)

    def describe_physical_connection_loawith_options(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribePhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribePhysicalConnectionLOAResponse().from_map(
            self.do_rpcrequest('DescribePhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_physical_connection_loawith_options_async(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribePhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribePhysicalConnectionLOAResponse().from_map(
            await self.do_rpcrequest_async('DescribePhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_physical_connection_loa(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.DescribePhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_physical_connection_loawith_options(request, runtime)

    async def describe_physical_connection_loa_async(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.DescribePhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_physical_connection_loawith_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: vpc_20160428_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRegionsResponse().from_map(
            self.do_rpcrequest('DescribeRegions', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRegionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeRegions', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: vpc_20160428_models.DescribeRegionsRequest,
    ) -> vpc_20160428_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: vpc_20160428_models.DescribeRegionsRequest,
    ) -> vpc_20160428_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_route_entry_list_with_options(
        self,
        request: vpc_20160428_models.DescribeRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteEntryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteEntryListResponse().from_map(
            self.do_rpcrequest('DescribeRouteEntryList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_entry_list_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRouteEntryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteEntryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteEntryListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouteEntryList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_entry_list(
        self,
        request: vpc_20160428_models.DescribeRouteEntryListRequest,
    ) -> vpc_20160428_models.DescribeRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_entry_list_with_options(request, runtime)

    async def describe_route_entry_list_async(
        self,
        request: vpc_20160428_models.DescribeRouteEntryListRequest,
    ) -> vpc_20160428_models.DescribeRouteEntryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_entry_list_with_options_async(request, runtime)

    def describe_router_interface_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouterInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('DescribeRouterInterfaceAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_router_interface_attribute_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouterInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouterInterfaceAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_router_interface_attribute(
        self,
        request: vpc_20160428_models.DescribeRouterInterfaceAttributeRequest,
    ) -> vpc_20160428_models.DescribeRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_router_interface_attribute_with_options(request, runtime)

    async def describe_router_interface_attribute_async(
        self,
        request: vpc_20160428_models.DescribeRouterInterfaceAttributeRequest,
    ) -> vpc_20160428_models.DescribeRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_router_interface_attribute_with_options_async(request, runtime)

    def describe_router_interfaces_with_options(
        self,
        request: vpc_20160428_models.DescribeRouterInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouterInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouterInterfacesResponse().from_map(
            self.do_rpcrequest('DescribeRouterInterfaces', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_router_interfaces_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRouterInterfacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouterInterfacesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouterInterfacesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouterInterfaces', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_router_interfaces(
        self,
        request: vpc_20160428_models.DescribeRouterInterfacesRequest,
    ) -> vpc_20160428_models.DescribeRouterInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_router_interfaces_with_options(request, runtime)

    async def describe_router_interfaces_async(
        self,
        request: vpc_20160428_models.DescribeRouterInterfacesRequest,
    ) -> vpc_20160428_models.DescribeRouterInterfacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_router_interfaces_with_options_async(request, runtime)

    def describe_route_table_list_with_options(
        self,
        request: vpc_20160428_models.DescribeRouteTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteTableListResponse().from_map(
            self.do_rpcrequest('DescribeRouteTableList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_table_list_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRouteTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteTableListResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouteTableList', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_table_list(
        self,
        request: vpc_20160428_models.DescribeRouteTableListRequest,
    ) -> vpc_20160428_models.DescribeRouteTableListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_table_list_with_options(request, runtime)

    async def describe_route_table_list_async(
        self,
        request: vpc_20160428_models.DescribeRouteTableListRequest,
    ) -> vpc_20160428_models.DescribeRouteTableListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_table_list_with_options_async(request, runtime)

    def describe_route_tables_with_options(
        self,
        request: vpc_20160428_models.DescribeRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteTablesResponse().from_map(
            self.do_rpcrequest('DescribeRouteTables', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_route_tables_with_options_async(
        self,
        request: vpc_20160428_models.DescribeRouteTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeRouteTablesResponse().from_map(
            await self.do_rpcrequest_async('DescribeRouteTables', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_route_tables(
        self,
        request: vpc_20160428_models.DescribeRouteTablesRequest,
    ) -> vpc_20160428_models.DescribeRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_route_tables_with_options(request, runtime)

    async def describe_route_tables_async(
        self,
        request: vpc_20160428_models.DescribeRouteTablesRequest,
    ) -> vpc_20160428_models.DescribeRouteTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_route_tables_with_options_async(request, runtime)

    def describe_server_related_global_acceleration_instances_with_options(
        self,
        request: vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse().from_map(
            self.do_rpcrequest('DescribeServerRelatedGlobalAccelerationInstances', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_server_related_global_acceleration_instances_with_options_async(
        self,
        request: vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse().from_map(
            await self.do_rpcrequest_async('DescribeServerRelatedGlobalAccelerationInstances', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_server_related_global_acceleration_instances(
        self,
        request: vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesRequest,
    ) -> vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_server_related_global_acceleration_instances_with_options(request, runtime)

    async def describe_server_related_global_acceleration_instances_async(
        self,
        request: vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesRequest,
    ) -> vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_server_related_global_acceleration_instances_with_options_async(request, runtime)

    def describe_snat_table_entries_with_options(
        self,
        request: vpc_20160428_models.DescribeSnatTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSnatTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSnatTableEntriesResponse().from_map(
            self.do_rpcrequest('DescribeSnatTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_snat_table_entries_with_options_async(
        self,
        request: vpc_20160428_models.DescribeSnatTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSnatTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSnatTableEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeSnatTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_snat_table_entries(
        self,
        request: vpc_20160428_models.DescribeSnatTableEntriesRequest,
    ) -> vpc_20160428_models.DescribeSnatTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_snat_table_entries_with_options(request, runtime)

    async def describe_snat_table_entries_async(
        self,
        request: vpc_20160428_models.DescribeSnatTableEntriesRequest,
    ) -> vpc_20160428_models.DescribeSnatTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_snat_table_entries_with_options_async(request, runtime)

    def describe_ssl_vpn_client_cert_with_options(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnClientCertResponse().from_map(
            self.do_rpcrequest('DescribeSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ssl_vpn_client_cert_with_options_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnClientCertResponse().from_map(
            await self.do_rpcrequest_async('DescribeSslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ssl_vpn_client_cert(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertRequest,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ssl_vpn_client_cert_with_options(request, runtime)

    async def describe_ssl_vpn_client_cert_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertRequest,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ssl_vpn_client_cert_with_options_async(request, runtime)

    def describe_ssl_vpn_client_certs_with_options(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnClientCertsResponse().from_map(
            self.do_rpcrequest('DescribeSslVpnClientCerts', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ssl_vpn_client_certs_with_options_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnClientCertsResponse().from_map(
            await self.do_rpcrequest_async('DescribeSslVpnClientCerts', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ssl_vpn_client_certs(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertsRequest,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ssl_vpn_client_certs_with_options(request, runtime)

    async def describe_ssl_vpn_client_certs_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnClientCertsRequest,
    ) -> vpc_20160428_models.DescribeSslVpnClientCertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ssl_vpn_client_certs_with_options_async(request, runtime)

    def describe_ssl_vpn_servers_with_options(
        self,
        request: vpc_20160428_models.DescribeSslVpnServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnServersResponse().from_map(
            self.do_rpcrequest('DescribeSslVpnServers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_ssl_vpn_servers_with_options_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeSslVpnServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeSslVpnServersResponse().from_map(
            await self.do_rpcrequest_async('DescribeSslVpnServers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_ssl_vpn_servers(
        self,
        request: vpc_20160428_models.DescribeSslVpnServersRequest,
    ) -> vpc_20160428_models.DescribeSslVpnServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_ssl_vpn_servers_with_options(request, runtime)

    async def describe_ssl_vpn_servers_async(
        self,
        request: vpc_20160428_models.DescribeSslVpnServersRequest,
    ) -> vpc_20160428_models.DescribeSslVpnServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_ssl_vpn_servers_with_options_async(request, runtime)

    def describe_virtual_border_routers_with_options(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVirtualBorderRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRouters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVirtualBorderRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRouters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersRequest,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_with_options(request, runtime)

    async def describe_virtual_border_routers_async(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersRequest,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_with_options_async(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            self.do_rpcrequest('DescribeVirtualBorderRoutersForPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_virtual_border_routers_for_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeVirtualBorderRoutersForPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_virtual_border_routers_for_physical_connection(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    async def describe_virtual_border_routers_for_physical_connection_async(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionRequest,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_virtual_border_routers_for_physical_connection_with_options_async(request, runtime)

    def describe_vpc_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpcAttributeResponse().from_map(
            self.do_rpcrequest('DescribeVpcAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpc_attribute_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpc_attribute(
        self,
        request: vpc_20160428_models.DescribeVpcAttributeRequest,
    ) -> vpc_20160428_models.DescribeVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpc_attribute_with_options(request, runtime)

    async def describe_vpc_attribute_async(
        self,
        request: vpc_20160428_models.DescribeVpcAttributeRequest,
    ) -> vpc_20160428_models.DescribeVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpc_attribute_with_options_async(request, runtime)

    def describe_vpcs_with_options(
        self,
        request: vpc_20160428_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpcsResponse().from_map(
            self.do_rpcrequest('DescribeVpcs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpcs_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpcsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpcsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpcsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpcs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(
        self,
        request: vpc_20160428_models.DescribeVpcsRequest,
    ) -> vpc_20160428_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    async def describe_vpcs_async(
        self,
        request: vpc_20160428_models.DescribeVpcsRequest,
    ) -> vpc_20160428_models.DescribeVpcsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpcs_with_options_async(request, runtime)

    def describe_vpn_connection_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnConnectionResponse().from_map(
            self.do_rpcrequest('DescribeVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_connection_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnConnectionResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_connection(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionRequest,
    ) -> vpc_20160428_models.DescribeVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_connection_with_options(request, runtime)

    async def describe_vpn_connection_async(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionRequest,
    ) -> vpc_20160428_models.DescribeVpnConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_connection_with_options_async(request, runtime)

    def describe_vpn_connections_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnConnectionsResponse().from_map(
            self.do_rpcrequest('DescribeVpnConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_connections_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnConnectionsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_connections(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionsRequest,
    ) -> vpc_20160428_models.DescribeVpnConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_connections_with_options(request, runtime)

    async def describe_vpn_connections_async(
        self,
        request: vpc_20160428_models.DescribeVpnConnectionsRequest,
    ) -> vpc_20160428_models.DescribeVpnConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_connections_with_options_async(request, runtime)

    def describe_vpn_gateway_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnGatewayResponse().from_map(
            self.do_rpcrequest('DescribeVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnGatewayResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_gateway(
        self,
        request: vpc_20160428_models.DescribeVpnGatewayRequest,
    ) -> vpc_20160428_models.DescribeVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_gateway_with_options(request, runtime)

    async def describe_vpn_gateway_async(
        self,
        request: vpc_20160428_models.DescribeVpnGatewayRequest,
    ) -> vpc_20160428_models.DescribeVpnGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_gateway_with_options_async(request, runtime)

    def describe_vpn_gateways_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnGatewaysResponse().from_map(
            self.do_rpcrequest('DescribeVpnGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_gateways_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnGatewaysResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnGateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_gateways(
        self,
        request: vpc_20160428_models.DescribeVpnGatewaysRequest,
    ) -> vpc_20160428_models.DescribeVpnGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_gateways_with_options(request, runtime)

    async def describe_vpn_gateways_async(
        self,
        request: vpc_20160428_models.DescribeVpnGatewaysRequest,
    ) -> vpc_20160428_models.DescribeVpnGatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_gateways_with_options_async(request, runtime)

    def describe_vpn_pbr_route_entries_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnPbrRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse().from_map(
            self.do_rpcrequest('DescribeVpnPbrRouteEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_pbr_route_entries_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnPbrRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnPbrRouteEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_pbr_route_entries(
        self,
        request: vpc_20160428_models.DescribeVpnPbrRouteEntriesRequest,
    ) -> vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_pbr_route_entries_with_options(request, runtime)

    async def describe_vpn_pbr_route_entries_async(
        self,
        request: vpc_20160428_models.DescribeVpnPbrRouteEntriesRequest,
    ) -> vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_pbr_route_entries_with_options_async(request, runtime)

    def describe_vpn_route_entries_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnRouteEntriesResponse().from_map(
            self.do_rpcrequest('DescribeVpnRouteEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_route_entries_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnRouteEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnRouteEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnRouteEntriesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnRouteEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_route_entries(
        self,
        request: vpc_20160428_models.DescribeVpnRouteEntriesRequest,
    ) -> vpc_20160428_models.DescribeVpnRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_route_entries_with_options(request, runtime)

    async def describe_vpn_route_entries_async(
        self,
        request: vpc_20160428_models.DescribeVpnRouteEntriesRequest,
    ) -> vpc_20160428_models.DescribeVpnRouteEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_route_entries_with_options_async(request, runtime)

    def describe_vpn_ssl_server_logs_with_options(
        self,
        request: vpc_20160428_models.DescribeVpnSslServerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnSslServerLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnSslServerLogsResponse().from_map(
            self.do_rpcrequest('DescribeVpnSslServerLogs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vpn_ssl_server_logs_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVpnSslServerLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVpnSslServerLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVpnSslServerLogsResponse().from_map(
            await self.do_rpcrequest_async('DescribeVpnSslServerLogs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpn_ssl_server_logs(
        self,
        request: vpc_20160428_models.DescribeVpnSslServerLogsRequest,
    ) -> vpc_20160428_models.DescribeVpnSslServerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vpn_ssl_server_logs_with_options(request, runtime)

    async def describe_vpn_ssl_server_logs_async(
        self,
        request: vpc_20160428_models.DescribeVpnSslServerLogsRequest,
    ) -> vpc_20160428_models.DescribeVpnSslServerLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vpn_ssl_server_logs_with_options_async(request, runtime)

    def describe_vrouters_with_options(
        self,
        request: vpc_20160428_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVRoutersResponse().from_map(
            self.do_rpcrequest('DescribeVRouters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vrouters_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVRoutersResponse().from_map(
            await self.do_rpcrequest_async('DescribeVRouters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vrouters(
        self,
        request: vpc_20160428_models.DescribeVRoutersRequest,
    ) -> vpc_20160428_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vrouters_with_options(request, runtime)

    async def describe_vrouters_async(
        self,
        request: vpc_20160428_models.DescribeVRoutersRequest,
    ) -> vpc_20160428_models.DescribeVRoutersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vrouters_with_options_async(request, runtime)

    def describe_vswitch_attributes_with_options(
        self,
        request: vpc_20160428_models.DescribeVSwitchAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVSwitchAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVSwitchAttributesResponse().from_map(
            self.do_rpcrequest('DescribeVSwitchAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitch_attributes_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVSwitchAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVSwitchAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVSwitchAttributesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVSwitchAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitch_attributes(
        self,
        request: vpc_20160428_models.DescribeVSwitchAttributesRequest,
    ) -> vpc_20160428_models.DescribeVSwitchAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitch_attributes_with_options(request, runtime)

    async def describe_vswitch_attributes_async(
        self,
        request: vpc_20160428_models.DescribeVSwitchAttributesRequest,
    ) -> vpc_20160428_models.DescribeVSwitchAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitch_attributes_with_options_async(request, runtime)

    def describe_vswitches_with_options(
        self,
        request: vpc_20160428_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVSwitchesResponse().from_map(
            self.do_rpcrequest('DescribeVSwitches', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vswitches_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVSwitchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVSwitchesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeVSwitchesResponse().from_map(
            await self.do_rpcrequest_async('DescribeVSwitches', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(
        self,
        request: vpc_20160428_models.DescribeVSwitchesRequest,
    ) -> vpc_20160428_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    async def describe_vswitches_async(
        self,
        request: vpc_20160428_models.DescribeVSwitchesRequest,
    ) -> vpc_20160428_models.DescribeVSwitchesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vswitches_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: vpc_20160428_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeZonesResponse().from_map(
            self.do_rpcrequest('DescribeZones', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: vpc_20160428_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DescribeZonesResponse().from_map(
            await self.do_rpcrequest_async('DescribeZones', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(
        self,
        request: vpc_20160428_models.DescribeZonesRequest,
    ) -> vpc_20160428_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: vpc_20160428_models.DescribeZonesRequest,
    ) -> vpc_20160428_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_dhcp_options_set_from_vpc_with_options(
        self,
        request: vpc_20160428_models.DetachDhcpOptionsSetFromVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse().from_map(
            self.do_rpcrequest('DetachDhcpOptionsSetFromVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_dhcp_options_set_from_vpc_with_options_async(
        self,
        request: vpc_20160428_models.DetachDhcpOptionsSetFromVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse().from_map(
            await self.do_rpcrequest_async('DetachDhcpOptionsSetFromVpc', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_dhcp_options_set_from_vpc(
        self,
        request: vpc_20160428_models.DetachDhcpOptionsSetFromVpcRequest,
    ) -> vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_dhcp_options_set_from_vpc_with_options(request, runtime)

    async def detach_dhcp_options_set_from_vpc_async(
        self,
        request: vpc_20160428_models.DetachDhcpOptionsSetFromVpcRequest,
    ) -> vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_dhcp_options_set_from_vpc_with_options_async(request, runtime)

    def disable_nat_gateway_ecs_metric_with_options(
        self,
        request: vpc_20160428_models.DisableNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DisableNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DisableNatGatewayEcsMetricResponse().from_map(
            self.do_rpcrequest('DisableNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_nat_gateway_ecs_metric_with_options_async(
        self,
        request: vpc_20160428_models.DisableNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DisableNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DisableNatGatewayEcsMetricResponse().from_map(
            await self.do_rpcrequest_async('DisableNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_nat_gateway_ecs_metric(
        self,
        request: vpc_20160428_models.DisableNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.DisableNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_nat_gateway_ecs_metric_with_options(request, runtime)

    async def disable_nat_gateway_ecs_metric_async(
        self,
        request: vpc_20160428_models.DisableNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.DisableNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_nat_gateway_ecs_metric_with_options_async(request, runtime)

    def disable_vpc_classic_link_with_options(
        self,
        request: vpc_20160428_models.DisableVpcClassicLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DisableVpcClassicLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DisableVpcClassicLinkResponse().from_map(
            self.do_rpcrequest('DisableVpcClassicLink', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_vpc_classic_link_with_options_async(
        self,
        request: vpc_20160428_models.DisableVpcClassicLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DisableVpcClassicLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DisableVpcClassicLinkResponse().from_map(
            await self.do_rpcrequest_async('DisableVpcClassicLink', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_vpc_classic_link(
        self,
        request: vpc_20160428_models.DisableVpcClassicLinkRequest,
    ) -> vpc_20160428_models.DisableVpcClassicLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_vpc_classic_link_with_options(request, runtime)

    async def disable_vpc_classic_link_async(
        self,
        request: vpc_20160428_models.DisableVpcClassicLinkRequest,
    ) -> vpc_20160428_models.DisableVpcClassicLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_vpc_classic_link_with_options_async(request, runtime)

    def dissociate_vpn_gateway_with_certificate_with_options(
        self,
        request: vpc_20160428_models.DissociateVpnGatewayWithCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse().from_map(
            self.do_rpcrequest('DissociateVpnGatewayWithCertificate', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_vpn_gateway_with_certificate_with_options_async(
        self,
        request: vpc_20160428_models.DissociateVpnGatewayWithCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse().from_map(
            await self.do_rpcrequest_async('DissociateVpnGatewayWithCertificate', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_vpn_gateway_with_certificate(
        self,
        request: vpc_20160428_models.DissociateVpnGatewayWithCertificateRequest,
    ) -> vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_vpn_gateway_with_certificate_with_options(request, runtime)

    async def dissociate_vpn_gateway_with_certificate_async(
        self,
        request: vpc_20160428_models.DissociateVpnGatewayWithCertificateRequest,
    ) -> vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_vpn_gateway_with_certificate_with_options_async(request, runtime)

    def download_vpn_connection_config_with_options(
        self,
        request: vpc_20160428_models.DownloadVpnConnectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DownloadVpnConnectionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DownloadVpnConnectionConfigResponse().from_map(
            self.do_rpcrequest('DownloadVpnConnectionConfig', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def download_vpn_connection_config_with_options_async(
        self,
        request: vpc_20160428_models.DownloadVpnConnectionConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DownloadVpnConnectionConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.DownloadVpnConnectionConfigResponse().from_map(
            await self.do_rpcrequest_async('DownloadVpnConnectionConfig', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def download_vpn_connection_config(
        self,
        request: vpc_20160428_models.DownloadVpnConnectionConfigRequest,
    ) -> vpc_20160428_models.DownloadVpnConnectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_vpn_connection_config_with_options(request, runtime)

    async def download_vpn_connection_config_async(
        self,
        request: vpc_20160428_models.DownloadVpnConnectionConfigRequest,
    ) -> vpc_20160428_models.DownloadVpnConnectionConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_vpn_connection_config_with_options_async(request, runtime)

    def enable_nat_gateway_ecs_metric_with_options(
        self,
        request: vpc_20160428_models.EnableNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnableNatGatewayEcsMetricResponse().from_map(
            self.do_rpcrequest('EnableNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_nat_gateway_ecs_metric_with_options_async(
        self,
        request: vpc_20160428_models.EnableNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnableNatGatewayEcsMetricResponse().from_map(
            await self.do_rpcrequest_async('EnableNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_nat_gateway_ecs_metric(
        self,
        request: vpc_20160428_models.EnableNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.EnableNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_nat_gateway_ecs_metric_with_options(request, runtime)

    async def enable_nat_gateway_ecs_metric_async(
        self,
        request: vpc_20160428_models.EnableNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.EnableNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_nat_gateway_ecs_metric_with_options_async(request, runtime)

    def enable_physical_connection_with_options(
        self,
        request: vpc_20160428_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnablePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('EnablePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.EnablePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnablePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnablePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('EnablePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_physical_connection(
        self,
        request: vpc_20160428_models.EnablePhysicalConnectionRequest,
    ) -> vpc_20160428_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_physical_connection_with_options(request, runtime)

    async def enable_physical_connection_async(
        self,
        request: vpc_20160428_models.EnablePhysicalConnectionRequest,
    ) -> vpc_20160428_models.EnablePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_physical_connection_with_options_async(request, runtime)

    def enable_vpc_classic_link_with_options(
        self,
        request: vpc_20160428_models.EnableVpcClassicLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableVpcClassicLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnableVpcClassicLinkResponse().from_map(
            self.do_rpcrequest('EnableVpcClassicLink', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_vpc_classic_link_with_options_async(
        self,
        request: vpc_20160428_models.EnableVpcClassicLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableVpcClassicLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.EnableVpcClassicLinkResponse().from_map(
            await self.do_rpcrequest_async('EnableVpcClassicLink', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_vpc_classic_link(
        self,
        request: vpc_20160428_models.EnableVpcClassicLinkRequest,
    ) -> vpc_20160428_models.EnableVpcClassicLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_vpc_classic_link_with_options(request, runtime)

    async def enable_vpc_classic_link_async(
        self,
        request: vpc_20160428_models.EnableVpcClassicLinkRequest,
    ) -> vpc_20160428_models.EnableVpcClassicLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_vpc_classic_link_with_options_async(request, runtime)

    def get_dhcp_options_set_with_options(
        self,
        request: vpc_20160428_models.GetDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetDhcpOptionsSetResponse().from_map(
            self.do_rpcrequest('GetDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_dhcp_options_set_with_options_async(
        self,
        request: vpc_20160428_models.GetDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetDhcpOptionsSetResponse().from_map(
            await self.do_rpcrequest_async('GetDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_dhcp_options_set(
        self,
        request: vpc_20160428_models.GetDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.GetDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_dhcp_options_set_with_options(request, runtime)

    async def get_dhcp_options_set_async(
        self,
        request: vpc_20160428_models.GetDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.GetDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_dhcp_options_set_with_options_async(request, runtime)

    def get_nat_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.GetNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetNatGatewayAttributeResponse().from_map(
            self.do_rpcrequest('GetNatGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_nat_gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.GetNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetNatGatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('GetNatGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_nat_gateway_attribute(
        self,
        request: vpc_20160428_models.GetNatGatewayAttributeRequest,
    ) -> vpc_20160428_models.GetNatGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_nat_gateway_attribute_with_options(request, runtime)

    async def get_nat_gateway_attribute_async(
        self,
        request: vpc_20160428_models.GetNatGatewayAttributeRequest,
    ) -> vpc_20160428_models.GetNatGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_nat_gateway_attribute_with_options_async(request, runtime)

    def get_nat_gateway_convert_status_with_options(
        self,
        request: vpc_20160428_models.GetNatGatewayConvertStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetNatGatewayConvertStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetNatGatewayConvertStatusResponse().from_map(
            self.do_rpcrequest('GetNatGatewayConvertStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_nat_gateway_convert_status_with_options_async(
        self,
        request: vpc_20160428_models.GetNatGatewayConvertStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetNatGatewayConvertStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GetNatGatewayConvertStatusResponse().from_map(
            await self.do_rpcrequest_async('GetNatGatewayConvertStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_nat_gateway_convert_status(
        self,
        request: vpc_20160428_models.GetNatGatewayConvertStatusRequest,
    ) -> vpc_20160428_models.GetNatGatewayConvertStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_nat_gateway_convert_status_with_options(request, runtime)

    async def get_nat_gateway_convert_status_async(
        self,
        request: vpc_20160428_models.GetNatGatewayConvertStatusRequest,
    ) -> vpc_20160428_models.GetNatGatewayConvertStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_nat_gateway_convert_status_with_options_async(request, runtime)

    def grant_instance_to_cen_with_options(
        self,
        request: vpc_20160428_models.GrantInstanceToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GrantInstanceToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GrantInstanceToCenResponse().from_map(
            self.do_rpcrequest('GrantInstanceToCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def grant_instance_to_cen_with_options_async(
        self,
        request: vpc_20160428_models.GrantInstanceToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GrantInstanceToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.GrantInstanceToCenResponse().from_map(
            await self.do_rpcrequest_async('GrantInstanceToCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def grant_instance_to_cen(
        self,
        request: vpc_20160428_models.GrantInstanceToCenRequest,
    ) -> vpc_20160428_models.GrantInstanceToCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_instance_to_cen_with_options(request, runtime)

    async def grant_instance_to_cen_async(
        self,
        request: vpc_20160428_models.GrantInstanceToCenRequest,
    ) -> vpc_20160428_models.GrantInstanceToCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_instance_to_cen_with_options_async(request, runtime)

    def list_dhcp_options_sets_with_options(
        self,
        request: vpc_20160428_models.ListDhcpOptionsSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListDhcpOptionsSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListDhcpOptionsSetsResponse().from_map(
            self.do_rpcrequest('ListDhcpOptionsSets', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dhcp_options_sets_with_options_async(
        self,
        request: vpc_20160428_models.ListDhcpOptionsSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListDhcpOptionsSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListDhcpOptionsSetsResponse().from_map(
            await self.do_rpcrequest_async('ListDhcpOptionsSets', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dhcp_options_sets(
        self,
        request: vpc_20160428_models.ListDhcpOptionsSetsRequest,
    ) -> vpc_20160428_models.ListDhcpOptionsSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dhcp_options_sets_with_options(request, runtime)

    async def list_dhcp_options_sets_async(
        self,
        request: vpc_20160428_models.ListDhcpOptionsSetsRequest,
    ) -> vpc_20160428_models.ListDhcpOptionsSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dhcp_options_sets_with_options_async(request, runtime)

    def list_enhanhced_nat_gateway_available_zones_with_options(
        self,
        request: vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse().from_map(
            self.do_rpcrequest('ListEnhanhcedNatGatewayAvailableZones', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_enhanhced_nat_gateway_available_zones_with_options_async(
        self,
        request: vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse().from_map(
            await self.do_rpcrequest_async('ListEnhanhcedNatGatewayAvailableZones', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_enhanhced_nat_gateway_available_zones(
        self,
        request: vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesRequest,
    ) -> vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_enhanhced_nat_gateway_available_zones_with_options(request, runtime)

    async def list_enhanhced_nat_gateway_available_zones_async(
        self,
        request: vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesRequest,
    ) -> vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_enhanhced_nat_gateway_available_zones_with_options_async(request, runtime)

    def list_ipsec_servers_with_options(
        self,
        request: vpc_20160428_models.ListIpsecServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListIpsecServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListIpsecServersResponse().from_map(
            self.do_rpcrequest('ListIpsecServers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ipsec_servers_with_options_async(
        self,
        request: vpc_20160428_models.ListIpsecServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListIpsecServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListIpsecServersResponse().from_map(
            await self.do_rpcrequest_async('ListIpsecServers', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ipsec_servers(
        self,
        request: vpc_20160428_models.ListIpsecServersRequest,
    ) -> vpc_20160428_models.ListIpsecServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ipsec_servers_with_options(request, runtime)

    async def list_ipsec_servers_async(
        self,
        request: vpc_20160428_models.ListIpsecServersRequest,
    ) -> vpc_20160428_models.ListIpsecServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ipsec_servers_with_options_async(request, runtime)

    def list_nat_gateway_ecs_metric_with_options(
        self,
        request: vpc_20160428_models.ListNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListNatGatewayEcsMetricResponse().from_map(
            self.do_rpcrequest('ListNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nat_gateway_ecs_metric_with_options_async(
        self,
        request: vpc_20160428_models.ListNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListNatGatewayEcsMetricResponse().from_map(
            await self.do_rpcrequest_async('ListNatGatewayEcsMetric', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nat_gateway_ecs_metric(
        self,
        request: vpc_20160428_models.ListNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.ListNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nat_gateway_ecs_metric_with_options(request, runtime)

    async def list_nat_gateway_ecs_metric_async(
        self,
        request: vpc_20160428_models.ListNatGatewayEcsMetricRequest,
    ) -> vpc_20160428_models.ListNatGatewayEcsMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nat_gateway_ecs_metric_with_options_async(request, runtime)

    def list_physical_connection_features_with_options(
        self,
        request: vpc_20160428_models.ListPhysicalConnectionFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListPhysicalConnectionFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListPhysicalConnectionFeaturesResponse().from_map(
            self.do_rpcrequest('ListPhysicalConnectionFeatures', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_physical_connection_features_with_options_async(
        self,
        request: vpc_20160428_models.ListPhysicalConnectionFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListPhysicalConnectionFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListPhysicalConnectionFeaturesResponse().from_map(
            await self.do_rpcrequest_async('ListPhysicalConnectionFeatures', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_physical_connection_features(
        self,
        request: vpc_20160428_models.ListPhysicalConnectionFeaturesRequest,
    ) -> vpc_20160428_models.ListPhysicalConnectionFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_physical_connection_features_with_options(request, runtime)

    async def list_physical_connection_features_async(
        self,
        request: vpc_20160428_models.ListPhysicalConnectionFeaturesRequest,
    ) -> vpc_20160428_models.ListPhysicalConnectionFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_physical_connection_features_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: vpc_20160428_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: vpc_20160428_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: vpc_20160428_models.ListTagResourcesRequest,
    ) -> vpc_20160428_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: vpc_20160428_models.ListTagResourcesRequest,
    ) -> vpc_20160428_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_vpn_certificate_associations_with_options(
        self,
        request: vpc_20160428_models.ListVpnCertificateAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpnCertificateAssociationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListVpnCertificateAssociationsResponse().from_map(
            self.do_rpcrequest('ListVpnCertificateAssociations', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vpn_certificate_associations_with_options_async(
        self,
        request: vpc_20160428_models.ListVpnCertificateAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpnCertificateAssociationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ListVpnCertificateAssociationsResponse().from_map(
            await self.do_rpcrequest_async('ListVpnCertificateAssociations', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vpn_certificate_associations(
        self,
        request: vpc_20160428_models.ListVpnCertificateAssociationsRequest,
    ) -> vpc_20160428_models.ListVpnCertificateAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpn_certificate_associations_with_options(request, runtime)

    async def list_vpn_certificate_associations_async(
        self,
        request: vpc_20160428_models.ListVpnCertificateAssociationsRequest,
    ) -> vpc_20160428_models.ListVpnCertificateAssociationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpn_certificate_associations_with_options_async(request, runtime)

    def modify_bgp_group_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyBgpGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyBgpGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyBgpGroupAttributeResponse().from_map(
            self.do_rpcrequest('ModifyBgpGroupAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_bgp_group_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyBgpGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyBgpGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyBgpGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyBgpGroupAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bgp_group_attribute(
        self,
        request: vpc_20160428_models.ModifyBgpGroupAttributeRequest,
    ) -> vpc_20160428_models.ModifyBgpGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bgp_group_attribute_with_options(request, runtime)

    async def modify_bgp_group_attribute_async(
        self,
        request: vpc_20160428_models.ModifyBgpGroupAttributeRequest,
    ) -> vpc_20160428_models.ModifyBgpGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bgp_group_attribute_with_options_async(request, runtime)

    def modify_bgp_peer_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyBgpPeerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyBgpPeerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyBgpPeerAttributeResponse().from_map(
            self.do_rpcrequest('ModifyBgpPeerAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_bgp_peer_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyBgpPeerAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyBgpPeerAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyBgpPeerAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyBgpPeerAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_bgp_peer_attribute(
        self,
        request: vpc_20160428_models.ModifyBgpPeerAttributeRequest,
    ) -> vpc_20160428_models.ModifyBgpPeerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_bgp_peer_attribute_with_options(request, runtime)

    async def modify_bgp_peer_attribute_async(
        self,
        request: vpc_20160428_models.ModifyBgpPeerAttributeRequest,
    ) -> vpc_20160428_models.ModifyBgpPeerAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_bgp_peer_attribute_with_options_async(request, runtime)

    def modify_common_bandwidth_package_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse().from_map(
            self.do_rpcrequest('ModifyCommonBandwidthPackageAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_common_bandwidth_package_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommonBandwidthPackageAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_common_bandwidth_package_attribute(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageAttributeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_common_bandwidth_package_attribute_with_options(request, runtime)

    async def modify_common_bandwidth_package_attribute_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageAttributeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_common_bandwidth_package_attribute_with_options_async(request, runtime)

    def modify_common_bandwidth_package_internet_charge_type_with_options(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse().from_map(
            self.do_rpcrequest('ModifyCommonBandwidthPackageInternetChargeType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_common_bandwidth_package_internet_charge_type_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommonBandwidthPackageInternetChargeType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_common_bandwidth_package_internet_charge_type(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_common_bandwidth_package_internet_charge_type_with_options(request, runtime)

    async def modify_common_bandwidth_package_internet_charge_type_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_common_bandwidth_package_internet_charge_type_with_options_async(request, runtime)

    def modify_common_bandwidth_package_ip_bandwidth_with_options(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse().from_map(
            self.do_rpcrequest('ModifyCommonBandwidthPackageIpBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_common_bandwidth_package_ip_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommonBandwidthPackageIpBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_common_bandwidth_package_ip_bandwidth(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_common_bandwidth_package_ip_bandwidth_with_options(request, runtime)

    async def modify_common_bandwidth_package_ip_bandwidth_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_common_bandwidth_package_ip_bandwidth_with_options_async(request, runtime)

    def modify_common_bandwidth_package_pay_type_with_options(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse().from_map(
            self.do_rpcrequest('ModifyCommonBandwidthPackagePayType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_common_bandwidth_package_pay_type_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommonBandwidthPackagePayType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_common_bandwidth_package_pay_type(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_common_bandwidth_package_pay_type_with_options(request, runtime)

    async def modify_common_bandwidth_package_pay_type_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_common_bandwidth_package_pay_type_with_options_async(request, runtime)

    def modify_common_bandwidth_package_spec_with_options(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse().from_map(
            self.do_rpcrequest('ModifyCommonBandwidthPackageSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_common_bandwidth_package_spec_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyCommonBandwidthPackageSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_common_bandwidth_package_spec(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageSpecRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_common_bandwidth_package_spec_with_options(request, runtime)

    async def modify_common_bandwidth_package_spec_async(
        self,
        request: vpc_20160428_models.ModifyCommonBandwidthPackageSpecRequest,
    ) -> vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_common_bandwidth_package_spec_with_options_async(request, runtime)

    def modify_customer_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyCustomerGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCustomerGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCustomerGatewayAttributeResponse().from_map(
            self.do_rpcrequest('ModifyCustomerGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_customer_gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyCustomerGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyCustomerGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyCustomerGatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyCustomerGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_customer_gateway_attribute(
        self,
        request: vpc_20160428_models.ModifyCustomerGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyCustomerGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_customer_gateway_attribute_with_options(request, runtime)

    async def modify_customer_gateway_attribute_async(
        self,
        request: vpc_20160428_models.ModifyCustomerGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyCustomerGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_customer_gateway_attribute_with_options_async(request, runtime)

    def modify_eip_address_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyEipAddressAttributeResponse().from_map(
            self.do_rpcrequest('ModifyEipAddressAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_eip_address_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyEipAddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyEipAddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyEipAddressAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyEipAddressAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_eip_address_attribute(
        self,
        request: vpc_20160428_models.ModifyEipAddressAttributeRequest,
    ) -> vpc_20160428_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_eip_address_attribute_with_options(request, runtime)

    async def modify_eip_address_attribute_async(
        self,
        request: vpc_20160428_models.ModifyEipAddressAttributeRequest,
    ) -> vpc_20160428_models.ModifyEipAddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_eip_address_attribute_with_options_async(request, runtime)

    def modify_express_cloud_connection_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse().from_map(
            self.do_rpcrequest('ModifyExpressCloudConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_express_cloud_connection_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyExpressCloudConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_express_cloud_connection_attribute(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_express_cloud_connection_attribute_with_options(request, runtime)

    async def modify_express_cloud_connection_attribute_async(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_express_cloud_connection_attribute_with_options_async(request, runtime)

    def modify_express_cloud_connection_bandwidth_with_options(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse().from_map(
            self.do_rpcrequest('ModifyExpressCloudConnectionBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_express_cloud_connection_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyExpressCloudConnectionBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_express_cloud_connection_bandwidth(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionBandwidthRequest,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_express_cloud_connection_bandwidth_with_options(request, runtime)

    async def modify_express_cloud_connection_bandwidth_async(
        self,
        request: vpc_20160428_models.ModifyExpressCloudConnectionBandwidthRequest,
    ) -> vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_express_cloud_connection_bandwidth_with_options_async(request, runtime)

    def modify_flow_log_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyFlowLogAttributeResponse().from_map(
            self.do_rpcrequest('ModifyFlowLogAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_log_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyFlowLogAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyFlowLogAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyFlowLogAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowLogAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_log_attribute(
        self,
        request: vpc_20160428_models.ModifyFlowLogAttributeRequest,
    ) -> vpc_20160428_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_log_attribute_with_options(request, runtime)

    async def modify_flow_log_attribute_async(
        self,
        request: vpc_20160428_models.ModifyFlowLogAttributeRequest,
    ) -> vpc_20160428_models.ModifyFlowLogAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_log_attribute_with_options_async(request, runtime)

    def modify_forward_entry_with_options(
        self,
        request: vpc_20160428_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyForwardEntryResponse().from_map(
            self.do_rpcrequest('ModifyForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_forward_entry_with_options_async(
        self,
        request: vpc_20160428_models.ModifyForwardEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyForwardEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyForwardEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyForwardEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_forward_entry(
        self,
        request: vpc_20160428_models.ModifyForwardEntryRequest,
    ) -> vpc_20160428_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_forward_entry_with_options(request, runtime)

    async def modify_forward_entry_async(
        self,
        request: vpc_20160428_models.ModifyForwardEntryRequest,
    ) -> vpc_20160428_models.ModifyForwardEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_forward_entry_with_options_async(request, runtime)

    def modify_global_acceleration_instance_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse().from_map(
            self.do_rpcrequest('ModifyGlobalAccelerationInstanceAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_global_acceleration_instance_attributes_with_options_async(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyGlobalAccelerationInstanceAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_global_acceleration_instance_attributes(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesRequest,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_global_acceleration_instance_attributes_with_options(request, runtime)

    async def modify_global_acceleration_instance_attributes_async(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesRequest,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_acceleration_instance_attributes_with_options_async(request, runtime)

    def modify_global_acceleration_instance_spec_with_options(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse().from_map(
            self.do_rpcrequest('ModifyGlobalAccelerationInstanceSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_global_acceleration_instance_spec_with_options_async(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyGlobalAccelerationInstanceSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_global_acceleration_instance_spec(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecRequest,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_global_acceleration_instance_spec_with_options(request, runtime)

    async def modify_global_acceleration_instance_spec_async(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecRequest,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_global_acceleration_instance_spec_with_options_async(request, runtime)

    def modify_ha_vip_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyHaVipAttributeResponse().from_map(
            self.do_rpcrequest('ModifyHaVipAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ha_vip_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyHaVipAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyHaVipAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyHaVipAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyHaVipAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ha_vip_attribute(
        self,
        request: vpc_20160428_models.ModifyHaVipAttributeRequest,
    ) -> vpc_20160428_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    async def modify_ha_vip_attribute_async(
        self,
        request: vpc_20160428_models.ModifyHaVipAttributeRequest,
    ) -> vpc_20160428_models.ModifyHaVipAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ha_vip_attribute_with_options_async(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            self.do_rpcrequest('ModifyInstanceAutoRenewalAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_instance_auto_renewal_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyInstanceAutoRenewalAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_auto_renewal_attribute(
        self,
        request: vpc_20160428_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    async def modify_instance_auto_renewal_attribute_async(
        self,
        request: vpc_20160428_models.ModifyInstanceAutoRenewalAttributeRequest,
    ) -> vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_instance_auto_renewal_attribute_with_options_async(request, runtime)

    def modify_ipv_6address_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyIpv6AddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6AddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6AddressAttributeResponse().from_map(
            self.do_rpcrequest('ModifyIpv6AddressAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6address_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIpv6AddressAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6AddressAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6AddressAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpv6AddressAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6address_attribute(
        self,
        request: vpc_20160428_models.ModifyIpv6AddressAttributeRequest,
    ) -> vpc_20160428_models.ModifyIpv6AddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6address_attribute_with_options(request, runtime)

    async def modify_ipv_6address_attribute_async(
        self,
        request: vpc_20160428_models.ModifyIpv6AddressAttributeRequest,
    ) -> vpc_20160428_models.ModifyIpv6AddressAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6address_attribute_with_options_async(request, runtime)

    def modify_ipv_6gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6GatewayAttributeResponse().from_map(
            self.do_rpcrequest('ModifyIpv6GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6GatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpv6GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6gateway_attribute(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyIpv6GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6gateway_attribute_with_options(request, runtime)

    async def modify_ipv_6gateway_attribute_async(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyIpv6GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6gateway_attribute_with_options_async(request, runtime)

    def modify_ipv_6gateway_spec_with_options(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewaySpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6GatewaySpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6GatewaySpecResponse().from_map(
            self.do_rpcrequest('ModifyIpv6GatewaySpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6gateway_spec_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewaySpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6GatewaySpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6GatewaySpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpv6GatewaySpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6gateway_spec(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewaySpecRequest,
    ) -> vpc_20160428_models.ModifyIpv6GatewaySpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6gateway_spec_with_options(request, runtime)

    async def modify_ipv_6gateway_spec_async(
        self,
        request: vpc_20160428_models.ModifyIpv6GatewaySpecRequest,
    ) -> vpc_20160428_models.ModifyIpv6GatewaySpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6gateway_spec_with_options_async(request, runtime)

    def modify_ipv_6internet_bandwidth_with_options(
        self,
        request: vpc_20160428_models.ModifyIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6InternetBandwidthResponse().from_map(
            self.do_rpcrequest('ModifyIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6internet_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIpv6InternetBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIpv6InternetBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIpv6InternetBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyIpv6InternetBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6internet_bandwidth(
        self,
        request: vpc_20160428_models.ModifyIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.ModifyIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6internet_bandwidth_with_options(request, runtime)

    async def modify_ipv_6internet_bandwidth_async(
        self,
        request: vpc_20160428_models.ModifyIpv6InternetBandwidthRequest,
    ) -> vpc_20160428_models.ModifyIpv6InternetBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6internet_bandwidth_with_options_async(request, runtime)

    def modify_ipv_6translator_acl_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse().from_map(
            self.do_rpcrequest('ModifyIPv6TranslatorAclAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6translator_acl_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyIPv6TranslatorAclAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6translator_acl_attribute(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclAttributeRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6translator_acl_attribute_with_options(request, runtime)

    async def modify_ipv_6translator_acl_attribute_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclAttributeRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6translator_acl_attribute_with_options_async(request, runtime)

    def modify_ipv_6translator_acl_list_entry_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse().from_map(
            self.do_rpcrequest('ModifyIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6translator_acl_list_entry_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6translator_acl_list_entry(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6translator_acl_list_entry_with_options(request, runtime)

    async def modify_ipv_6translator_acl_list_entry_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6translator_acl_list_entry_with_options_async(request, runtime)

    def modify_ipv_6translator_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse().from_map(
            self.do_rpcrequest('ModifyIPv6TranslatorAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6translator_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyIPv6TranslatorAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6translator_attribute(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAttributeRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6translator_attribute_with_options(request, runtime)

    async def modify_ipv_6translator_attribute_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAttributeRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6translator_attribute_with_options_async(request, runtime)

    def modify_ipv_6translator_bandwidth_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse().from_map(
            self.do_rpcrequest('ModifyIPv6TranslatorBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6translator_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse().from_map(
            await self.do_rpcrequest_async('ModifyIPv6TranslatorBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6translator_bandwidth(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorBandwidthRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6translator_bandwidth_with_options(request, runtime)

    async def modify_ipv_6translator_bandwidth_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorBandwidthRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6translator_bandwidth_with_options_async(request, runtime)

    def modify_ipv_6translator_entry_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorEntryResponse().from_map(
            self.do_rpcrequest('ModifyIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ipv_6translator_entry_with_options_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyIPv6TranslatorEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyIPv6TranslatorEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ipv_6translator_entry(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ipv_6translator_entry_with_options(request, runtime)

    async def modify_ipv_6translator_entry_async(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorEntryRequest,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ipv_6translator_entry_with_options_async(request, runtime)

    def modify_nat_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNatGatewayAttributeResponse().from_map(
            self.do_rpcrequest('ModifyNatGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_nat_gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNatGatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyNatGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nat_gateway_attribute(
        self,
        request: vpc_20160428_models.ModifyNatGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_gateway_attribute_with_options(request, runtime)

    async def modify_nat_gateway_attribute_async(
        self,
        request: vpc_20160428_models.ModifyNatGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_gateway_attribute_with_options_async(request, runtime)

    def modify_nat_gateway_spec_with_options(
        self,
        request: vpc_20160428_models.ModifyNatGatewaySpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatGatewaySpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNatGatewaySpecResponse().from_map(
            self.do_rpcrequest('ModifyNatGatewaySpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_nat_gateway_spec_with_options_async(
        self,
        request: vpc_20160428_models.ModifyNatGatewaySpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatGatewaySpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNatGatewaySpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyNatGatewaySpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nat_gateway_spec(
        self,
        request: vpc_20160428_models.ModifyNatGatewaySpecRequest,
    ) -> vpc_20160428_models.ModifyNatGatewaySpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_gateway_spec_with_options(request, runtime)

    async def modify_nat_gateway_spec_async(
        self,
        request: vpc_20160428_models.ModifyNatGatewaySpecRequest,
    ) -> vpc_20160428_models.ModifyNatGatewaySpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_gateway_spec_with_options_async(request, runtime)

    def modify_network_acl_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyNetworkAclAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNetworkAclAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNetworkAclAttributesResponse().from_map(
            self.do_rpcrequest('ModifyNetworkAclAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_network_acl_attributes_with_options_async(
        self,
        request: vpc_20160428_models.ModifyNetworkAclAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNetworkAclAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyNetworkAclAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyNetworkAclAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_network_acl_attributes(
        self,
        request: vpc_20160428_models.ModifyNetworkAclAttributesRequest,
    ) -> vpc_20160428_models.ModifyNetworkAclAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_network_acl_attributes_with_options(request, runtime)

    async def modify_network_acl_attributes_async(
        self,
        request: vpc_20160428_models.ModifyNetworkAclAttributesRequest,
    ) -> vpc_20160428_models.ModifyNetworkAclAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_network_acl_attributes_with_options_async(request, runtime)

    def modify_route_entry_with_options(
        self,
        request: vpc_20160428_models.ModifyRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouteEntryResponse().from_map(
            self.do_rpcrequest('ModifyRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.ModifyRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_route_entry(
        self,
        request: vpc_20160428_models.ModifyRouteEntryRequest,
    ) -> vpc_20160428_models.ModifyRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_route_entry_with_options(request, runtime)

    async def modify_route_entry_async(
        self,
        request: vpc_20160428_models.ModifyRouteEntryRequest,
    ) -> vpc_20160428_models.ModifyRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_route_entry_with_options_async(request, runtime)

    def modify_router_interface_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouterInterfaceAttributeResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouterInterfaceAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_attribute(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceAttributeRequest,
    ) -> vpc_20160428_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_attribute_with_options(request, runtime)

    async def modify_router_interface_attribute_async(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceAttributeRequest,
    ) -> vpc_20160428_models.ModifyRouterInterfaceAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_attribute_with_options_async(request, runtime)

    def modify_router_interface_spec_with_options(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouterInterfaceSpecResponse().from_map(
            self.do_rpcrequest('ModifyRouterInterfaceSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_router_interface_spec_with_options_async(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouterInterfaceSpecResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouterInterfaceSpecResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouterInterfaceSpec', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_router_interface_spec(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceSpecRequest,
    ) -> vpc_20160428_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_router_interface_spec_with_options(request, runtime)

    async def modify_router_interface_spec_async(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceSpecRequest,
    ) -> vpc_20160428_models.ModifyRouterInterfaceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_router_interface_spec_with_options_async(request, runtime)

    def modify_route_table_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyRouteTableAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteTableAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouteTableAttributesResponse().from_map(
            self.do_rpcrequest('ModifyRouteTableAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_route_table_attributes_with_options_async(
        self,
        request: vpc_20160428_models.ModifyRouteTableAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteTableAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyRouteTableAttributesResponse().from_map(
            await self.do_rpcrequest_async('ModifyRouteTableAttributes', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_route_table_attributes(
        self,
        request: vpc_20160428_models.ModifyRouteTableAttributesRequest,
    ) -> vpc_20160428_models.ModifyRouteTableAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_route_table_attributes_with_options(request, runtime)

    async def modify_route_table_attributes_async(
        self,
        request: vpc_20160428_models.ModifyRouteTableAttributesRequest,
    ) -> vpc_20160428_models.ModifyRouteTableAttributesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_route_table_attributes_with_options_async(request, runtime)

    def modify_snat_entry_with_options(
        self,
        request: vpc_20160428_models.ModifySnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySnatEntryResponse().from_map(
            self.do_rpcrequest('ModifySnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_snat_entry_with_options_async(
        self,
        request: vpc_20160428_models.ModifySnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySnatEntryResponse().from_map(
            await self.do_rpcrequest_async('ModifySnatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_snat_entry(
        self,
        request: vpc_20160428_models.ModifySnatEntryRequest,
    ) -> vpc_20160428_models.ModifySnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_snat_entry_with_options(request, runtime)

    async def modify_snat_entry_async(
        self,
        request: vpc_20160428_models.ModifySnatEntryRequest,
    ) -> vpc_20160428_models.ModifySnatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_snat_entry_with_options_async(request, runtime)

    def modify_ssl_vpn_client_cert_with_options(
        self,
        request: vpc_20160428_models.ModifySslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySslVpnClientCertResponse().from_map(
            self.do_rpcrequest('ModifySslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ssl_vpn_client_cert_with_options_async(
        self,
        request: vpc_20160428_models.ModifySslVpnClientCertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySslVpnClientCertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySslVpnClientCertResponse().from_map(
            await self.do_rpcrequest_async('ModifySslVpnClientCert', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ssl_vpn_client_cert(
        self,
        request: vpc_20160428_models.ModifySslVpnClientCertRequest,
    ) -> vpc_20160428_models.ModifySslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ssl_vpn_client_cert_with_options(request, runtime)

    async def modify_ssl_vpn_client_cert_async(
        self,
        request: vpc_20160428_models.ModifySslVpnClientCertRequest,
    ) -> vpc_20160428_models.ModifySslVpnClientCertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ssl_vpn_client_cert_with_options_async(request, runtime)

    def modify_ssl_vpn_server_with_options(
        self,
        request: vpc_20160428_models.ModifySslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySslVpnServerResponse().from_map(
            self.do_rpcrequest('ModifySslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_ssl_vpn_server_with_options_async(
        self,
        request: vpc_20160428_models.ModifySslVpnServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySslVpnServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifySslVpnServerResponse().from_map(
            await self.do_rpcrequest_async('ModifySslVpnServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_ssl_vpn_server(
        self,
        request: vpc_20160428_models.ModifySslVpnServerRequest,
    ) -> vpc_20160428_models.ModifySslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_ssl_vpn_server_with_options(request, runtime)

    async def modify_ssl_vpn_server_async(
        self,
        request: vpc_20160428_models.ModifySslVpnServerRequest,
    ) -> vpc_20160428_models.ModifySslVpnServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_ssl_vpn_server_with_options_async(request, runtime)

    def modify_virtual_border_router_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVirtualBorderRouterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_virtual_border_router_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVirtualBorderRouterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_virtual_border_router_attribute(
        self,
        request: vpc_20160428_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    async def modify_virtual_border_router_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVirtualBorderRouterAttributeRequest,
    ) -> vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_virtual_border_router_attribute_with_options_async(request, runtime)

    def modify_vpc_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpcAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVpcAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpc_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVpcAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpcAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpcAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpcAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpc_attribute(
        self,
        request: vpc_20160428_models.ModifyVpcAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpc_attribute_with_options(request, runtime)

    async def modify_vpc_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVpcAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpcAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpc_attribute_with_options_async(request, runtime)

    def modify_vpn_connection_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVpnConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnConnectionAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVpnConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpn_connection_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVpnConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnConnectionAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpnConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpn_connection_attribute(
        self,
        request: vpc_20160428_models.ModifyVpnConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpnConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpn_connection_attribute_with_options(request, runtime)

    async def modify_vpn_connection_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVpnConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpnConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpn_connection_attribute_with_options_async(request, runtime)

    def modify_vpn_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVpnGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnGatewayAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVpnGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpn_gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVpnGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnGatewayAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpnGatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpn_gateway_attribute(
        self,
        request: vpc_20160428_models.ModifyVpnGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpnGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpn_gateway_attribute_with_options(request, runtime)

    async def modify_vpn_gateway_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVpnGatewayAttributeRequest,
    ) -> vpc_20160428_models.ModifyVpnGatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpn_gateway_attribute_with_options_async(request, runtime)

    def modify_vpn_pbr_route_entry_weight_with_options(
        self,
        request: vpc_20160428_models.ModifyVpnPbrRouteEntryWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse().from_map(
            self.do_rpcrequest('ModifyVpnPbrRouteEntryWeight', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpn_pbr_route_entry_weight_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVpnPbrRouteEntryWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpnPbrRouteEntryWeight', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpn_pbr_route_entry_weight(
        self,
        request: vpc_20160428_models.ModifyVpnPbrRouteEntryWeightRequest,
    ) -> vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpn_pbr_route_entry_weight_with_options(request, runtime)

    async def modify_vpn_pbr_route_entry_weight_async(
        self,
        request: vpc_20160428_models.ModifyVpnPbrRouteEntryWeightRequest,
    ) -> vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpn_pbr_route_entry_weight_with_options_async(request, runtime)

    def modify_vpn_route_entry_weight_with_options(
        self,
        request: vpc_20160428_models.ModifyVpnRouteEntryWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnRouteEntryWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnRouteEntryWeightResponse().from_map(
            self.do_rpcrequest('ModifyVpnRouteEntryWeight', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vpn_route_entry_weight_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVpnRouteEntryWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVpnRouteEntryWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVpnRouteEntryWeightResponse().from_map(
            await self.do_rpcrequest_async('ModifyVpnRouteEntryWeight', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vpn_route_entry_weight(
        self,
        request: vpc_20160428_models.ModifyVpnRouteEntryWeightRequest,
    ) -> vpc_20160428_models.ModifyVpnRouteEntryWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vpn_route_entry_weight_with_options(request, runtime)

    async def modify_vpn_route_entry_weight_async(
        self,
        request: vpc_20160428_models.ModifyVpnRouteEntryWeightRequest,
    ) -> vpc_20160428_models.ModifyVpnRouteEntryWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vpn_route_entry_weight_with_options_async(request, runtime)

    def modify_vrouter_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVRouterAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVRouterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vrouter_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVRouterAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVRouterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vrouter_attribute(
        self,
        request: vpc_20160428_models.ModifyVRouterAttributeRequest,
    ) -> vpc_20160428_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vrouter_attribute_with_options(request, runtime)

    async def modify_vrouter_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVRouterAttributeRequest,
    ) -> vpc_20160428_models.ModifyVRouterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vrouter_attribute_with_options_async(request, runtime)

    def modify_vswitch_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVSwitchAttributeResponse().from_map(
            self.do_rpcrequest('ModifyVSwitchAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_vswitch_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyVSwitchAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVSwitchAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ModifyVSwitchAttributeResponse().from_map(
            await self.do_rpcrequest_async('ModifyVSwitchAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vswitch_attribute(
        self,
        request: vpc_20160428_models.ModifyVSwitchAttributeRequest,
    ) -> vpc_20160428_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_vswitch_attribute_with_options(request, runtime)

    async def modify_vswitch_attribute_async(
        self,
        request: vpc_20160428_models.ModifyVSwitchAttributeRequest,
    ) -> vpc_20160428_models.ModifyVSwitchAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_vswitch_attribute_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: vpc_20160428_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.MoveResourceGroupResponse().from_map(
            self.do_rpcrequest('MoveResourceGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: vpc_20160428_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.MoveResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('MoveResourceGroup', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_resource_group(
        self,
        request: vpc_20160428_models.MoveResourceGroupRequest,
    ) -> vpc_20160428_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: vpc_20160428_models.MoveResourceGroupRequest,
    ) -> vpc_20160428_models.MoveResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def publish_vpn_route_entry_with_options(
        self,
        request: vpc_20160428_models.PublishVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.PublishVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.PublishVpnRouteEntryResponse().from_map(
            self.do_rpcrequest('PublishVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def publish_vpn_route_entry_with_options_async(
        self,
        request: vpc_20160428_models.PublishVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.PublishVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.PublishVpnRouteEntryResponse().from_map(
            await self.do_rpcrequest_async('PublishVpnRouteEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_vpn_route_entry(
        self,
        request: vpc_20160428_models.PublishVpnRouteEntryRequest,
    ) -> vpc_20160428_models.PublishVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.publish_vpn_route_entry_with_options(request, runtime)

    async def publish_vpn_route_entry_async(
        self,
        request: vpc_20160428_models.PublishVpnRouteEntryRequest,
    ) -> vpc_20160428_models.PublishVpnRouteEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.publish_vpn_route_entry_with_options_async(request, runtime)

    def recover_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RecoverVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('RecoverVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recover_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RecoverVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('RecoverVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recover_virtual_border_router(
        self,
        request: vpc_20160428_models.RecoverVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_virtual_border_router_with_options(request, runtime)

    async def recover_virtual_border_router_async(
        self,
        request: vpc_20160428_models.RecoverVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.RecoverVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_virtual_border_router_with_options_async(request, runtime)

    def release_eip_address_with_options(
        self,
        request: vpc_20160428_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReleaseEipAddressResponse().from_map(
            self.do_rpcrequest('ReleaseEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_eip_address_with_options_async(
        self,
        request: vpc_20160428_models.ReleaseEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReleaseEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReleaseEipAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_address(
        self,
        request: vpc_20160428_models.ReleaseEipAddressRequest,
    ) -> vpc_20160428_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    async def release_eip_address_async(
        self,
        request: vpc_20160428_models.ReleaseEipAddressRequest,
    ) -> vpc_20160428_models.ReleaseEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_eip_address_with_options_async(request, runtime)

    def release_eip_segment_address_with_options(
        self,
        request: vpc_20160428_models.ReleaseEipSegmentAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReleaseEipSegmentAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReleaseEipSegmentAddressResponse().from_map(
            self.do_rpcrequest('ReleaseEipSegmentAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_eip_segment_address_with_options_async(
        self,
        request: vpc_20160428_models.ReleaseEipSegmentAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReleaseEipSegmentAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReleaseEipSegmentAddressResponse().from_map(
            await self.do_rpcrequest_async('ReleaseEipSegmentAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_eip_segment_address(
        self,
        request: vpc_20160428_models.ReleaseEipSegmentAddressRequest,
    ) -> vpc_20160428_models.ReleaseEipSegmentAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_eip_segment_address_with_options(request, runtime)

    async def release_eip_segment_address_async(
        self,
        request: vpc_20160428_models.ReleaseEipSegmentAddressRequest,
    ) -> vpc_20160428_models.ReleaseEipSegmentAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_eip_segment_address_with_options_async(request, runtime)

    def remove_common_bandwidth_package_ip_with_options(
        self,
        request: vpc_20160428_models.RemoveCommonBandwidthPackageIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse().from_map(
            self.do_rpcrequest('RemoveCommonBandwidthPackageIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_common_bandwidth_package_ip_with_options_async(
        self,
        request: vpc_20160428_models.RemoveCommonBandwidthPackageIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse().from_map(
            await self.do_rpcrequest_async('RemoveCommonBandwidthPackageIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_common_bandwidth_package_ip(
        self,
        request: vpc_20160428_models.RemoveCommonBandwidthPackageIpRequest,
    ) -> vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_common_bandwidth_package_ip_with_options(request, runtime)

    async def remove_common_bandwidth_package_ip_async(
        self,
        request: vpc_20160428_models.RemoveCommonBandwidthPackageIpRequest,
    ) -> vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_common_bandwidth_package_ip_with_options_async(request, runtime)

    def remove_global_acceleration_instance_ip_with_options(
        self,
        request: vpc_20160428_models.RemoveGlobalAccelerationInstanceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse().from_map(
            self.do_rpcrequest('RemoveGlobalAccelerationInstanceIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_global_acceleration_instance_ip_with_options_async(
        self,
        request: vpc_20160428_models.RemoveGlobalAccelerationInstanceIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse().from_map(
            await self.do_rpcrequest_async('RemoveGlobalAccelerationInstanceIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_global_acceleration_instance_ip(
        self,
        request: vpc_20160428_models.RemoveGlobalAccelerationInstanceIpRequest,
    ) -> vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_global_acceleration_instance_ip_with_options(request, runtime)

    async def remove_global_acceleration_instance_ip_async(
        self,
        request: vpc_20160428_models.RemoveGlobalAccelerationInstanceIpRequest,
    ) -> vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_global_acceleration_instance_ip_with_options_async(request, runtime)

    def remove_ipv_6translator_acl_list_entry_with_options(
        self,
        request: vpc_20160428_models.RemoveIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse().from_map(
            self.do_rpcrequest('RemoveIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_ipv_6translator_acl_list_entry_with_options_async(
        self,
        request: vpc_20160428_models.RemoveIPv6TranslatorAclListEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse().from_map(
            await self.do_rpcrequest_async('RemoveIPv6TranslatorAclListEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_ipv_6translator_acl_list_entry(
        self,
        request: vpc_20160428_models.RemoveIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ipv_6translator_acl_list_entry_with_options(request, runtime)

    async def remove_ipv_6translator_acl_list_entry_async(
        self,
        request: vpc_20160428_models.RemoveIPv6TranslatorAclListEntryRequest,
    ) -> vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ipv_6translator_acl_list_entry_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: vpc_20160428_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RenewInstanceResponse().from_map(
            self.do_rpcrequest('RenewInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: vpc_20160428_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RenewInstanceResponse().from_map(
            await self.do_rpcrequest_async('RenewInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def renew_instance(
        self,
        request: vpc_20160428_models.RenewInstanceRequest,
    ) -> vpc_20160428_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: vpc_20160428_models.RenewInstanceRequest,
    ) -> vpc_20160428_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def replace_vpc_dhcp_options_set_with_options(
        self,
        request: vpc_20160428_models.ReplaceVpcDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse().from_map(
            self.do_rpcrequest('ReplaceVpcDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_vpc_dhcp_options_set_with_options_async(
        self,
        request: vpc_20160428_models.ReplaceVpcDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse().from_map(
            await self.do_rpcrequest_async('ReplaceVpcDhcpOptionsSet', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_vpc_dhcp_options_set(
        self,
        request: vpc_20160428_models.ReplaceVpcDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_vpc_dhcp_options_set_with_options(request, runtime)

    async def replace_vpc_dhcp_options_set_async(
        self,
        request: vpc_20160428_models.ReplaceVpcDhcpOptionsSetRequest,
    ) -> vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_vpc_dhcp_options_set_with_options_async(request, runtime)

    def revoke_instance_from_cen_with_options(
        self,
        request: vpc_20160428_models.RevokeInstanceFromCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RevokeInstanceFromCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RevokeInstanceFromCenResponse().from_map(
            self.do_rpcrequest('RevokeInstanceFromCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def revoke_instance_from_cen_with_options_async(
        self,
        request: vpc_20160428_models.RevokeInstanceFromCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RevokeInstanceFromCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.RevokeInstanceFromCenResponse().from_map(
            await self.do_rpcrequest_async('RevokeInstanceFromCen', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def revoke_instance_from_cen(
        self,
        request: vpc_20160428_models.RevokeInstanceFromCenRequest,
    ) -> vpc_20160428_models.RevokeInstanceFromCenResponse:
        runtime = util_models.RuntimeOptions()
        return self.revoke_instance_from_cen_with_options(request, runtime)

    async def revoke_instance_from_cen_async(
        self,
        request: vpc_20160428_models.RevokeInstanceFromCenRequest,
    ) -> vpc_20160428_models.RevokeInstanceFromCenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revoke_instance_from_cen_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: vpc_20160428_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: vpc_20160428_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: vpc_20160428_models.TagResourcesRequest,
    ) -> vpc_20160428_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: vpc_20160428_models.TagResourcesRequest,
    ) -> vpc_20160428_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def terminate_physical_connection_with_options(
        self,
        request: vpc_20160428_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TerminatePhysicalConnectionResponse().from_map(
            self.do_rpcrequest('TerminatePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.TerminatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TerminatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TerminatePhysicalConnectionResponse().from_map(
            await self.do_rpcrequest_async('TerminatePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_physical_connection(
        self,
        request: vpc_20160428_models.TerminatePhysicalConnectionRequest,
    ) -> vpc_20160428_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_physical_connection_with_options(request, runtime)

    async def terminate_physical_connection_async(
        self,
        request: vpc_20160428_models.TerminatePhysicalConnectionRequest,
    ) -> vpc_20160428_models.TerminatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_physical_connection_with_options_async(request, runtime)

    def terminate_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TerminateVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('TerminateVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def terminate_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.TerminateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.TerminateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.TerminateVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('TerminateVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def terminate_virtual_border_router(
        self,
        request: vpc_20160428_models.TerminateVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_virtual_border_router_with_options(request, runtime)

    async def terminate_virtual_border_router_async(
        self,
        request: vpc_20160428_models.TerminateVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.TerminateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_virtual_border_router_with_options_async(request, runtime)

    def unassociate_eip_address_with_options(
        self,
        request: vpc_20160428_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateEipAddressResponse().from_map(
            self.do_rpcrequest('UnassociateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_eip_address_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateEipAddressResponse().from_map(
            await self.do_rpcrequest_async('UnassociateEipAddress', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_eip_address(
        self,
        request: vpc_20160428_models.UnassociateEipAddressRequest,
    ) -> vpc_20160428_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    async def unassociate_eip_address_async(
        self,
        request: vpc_20160428_models.UnassociateEipAddressRequest,
    ) -> vpc_20160428_models.UnassociateEipAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_eip_address_with_options_async(request, runtime)

    def unassociate_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.UnassociateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse().from_map(
            self.do_rpcrequest('UnassociateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_global_acceleration_instance_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse().from_map(
            await self.do_rpcrequest_async('UnassociateGlobalAccelerationInstance', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_global_acceleration_instance(
        self,
        request: vpc_20160428_models.UnassociateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_global_acceleration_instance_with_options(request, runtime)

    async def unassociate_global_acceleration_instance_async(
        self,
        request: vpc_20160428_models.UnassociateGlobalAccelerationInstanceRequest,
    ) -> vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_global_acceleration_instance_with_options_async(request, runtime)

    def unassociate_ha_vip_with_options(
        self,
        request: vpc_20160428_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateHaVipResponse().from_map(
            self.do_rpcrequest('UnassociateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_ha_vip_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateHaVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateHaVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateHaVipResponse().from_map(
            await self.do_rpcrequest_async('UnassociateHaVip', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_ha_vip(
        self,
        request: vpc_20160428_models.UnassociateHaVipRequest,
    ) -> vpc_20160428_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_ha_vip_with_options(request, runtime)

    async def unassociate_ha_vip_async(
        self,
        request: vpc_20160428_models.UnassociateHaVipRequest,
    ) -> vpc_20160428_models.UnassociateHaVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_ha_vip_with_options_async(request, runtime)

    def unassociate_network_acl_with_options(
        self,
        request: vpc_20160428_models.UnassociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateNetworkAclResponse().from_map(
            self.do_rpcrequest('UnassociateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_network_acl_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateNetworkAclResponse().from_map(
            await self.do_rpcrequest_async('UnassociateNetworkAcl', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_network_acl(
        self,
        request: vpc_20160428_models.UnassociateNetworkAclRequest,
    ) -> vpc_20160428_models.UnassociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_network_acl_with_options(request, runtime)

    async def unassociate_network_acl_async(
        self,
        request: vpc_20160428_models.UnassociateNetworkAclRequest,
    ) -> vpc_20160428_models.UnassociateNetworkAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_network_acl_with_options_async(request, runtime)

    def unassociate_physical_connection_from_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse().from_map(
            self.do_rpcrequest('UnassociatePhysicalConnectionFromVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_physical_connection_from_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse().from_map(
            await self.do_rpcrequest_async('UnassociatePhysicalConnectionFromVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_physical_connection_from_virtual_border_router(
        self,
        request: vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_physical_connection_from_virtual_border_router_with_options(request, runtime)

    async def unassociate_physical_connection_from_virtual_border_router_async(
        self,
        request: vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_physical_connection_from_virtual_border_router_with_options_async(request, runtime)

    def unassociate_route_table_with_options(
        self,
        request: vpc_20160428_models.UnassociateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateRouteTableResponse().from_map(
            self.do_rpcrequest('UnassociateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_route_table_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateRouteTableResponse().from_map(
            await self.do_rpcrequest_async('UnassociateRouteTable', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_route_table(
        self,
        request: vpc_20160428_models.UnassociateRouteTableRequest,
    ) -> vpc_20160428_models.UnassociateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_route_table_with_options(request, runtime)

    async def unassociate_route_table_async(
        self,
        request: vpc_20160428_models.UnassociateRouteTableRequest,
    ) -> vpc_20160428_models.UnassociateRouteTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_route_table_with_options_async(request, runtime)

    def unassociate_vpc_cidr_block_with_options(
        self,
        request: vpc_20160428_models.UnassociateVpcCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateVpcCidrBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateVpcCidrBlockResponse().from_map(
            self.do_rpcrequest('UnassociateVpcCidrBlock', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def unassociate_vpc_cidr_block_with_options_async(
        self,
        request: vpc_20160428_models.UnassociateVpcCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateVpcCidrBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnassociateVpcCidrBlockResponse().from_map(
            await self.do_rpcrequest_async('UnassociateVpcCidrBlock', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unassociate_vpc_cidr_block(
        self,
        request: vpc_20160428_models.UnassociateVpcCidrBlockRequest,
    ) -> vpc_20160428_models.UnassociateVpcCidrBlockResponse:
        runtime = util_models.RuntimeOptions()
        return self.unassociate_vpc_cidr_block_with_options(request, runtime)

    async def unassociate_vpc_cidr_block_async(
        self,
        request: vpc_20160428_models.UnassociateVpcCidrBlockRequest,
    ) -> vpc_20160428_models.UnassociateVpcCidrBlockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unassociate_vpc_cidr_block_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: vpc_20160428_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnTagResourcesResponse().from_map(
            self.do_rpcrequest('UnTagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: vpc_20160428_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UnTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UnTagResources', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def un_tag_resources(
        self,
        request: vpc_20160428_models.UnTagResourcesRequest,
    ) -> vpc_20160428_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: vpc_20160428_models.UnTagResourcesRequest,
    ) -> vpc_20160428_models.UnTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_dhcp_options_set_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateDhcpOptionsSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse().from_map(
            self.do_rpcrequest('UpdateDhcpOptionsSetAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dhcp_options_set_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateDhcpOptionsSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse().from_map(
            await self.do_rpcrequest_async('UpdateDhcpOptionsSetAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dhcp_options_set_attribute(
        self,
        request: vpc_20160428_models.UpdateDhcpOptionsSetAttributeRequest,
    ) -> vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dhcp_options_set_attribute_with_options(request, runtime)

    async def update_dhcp_options_set_attribute_async(
        self,
        request: vpc_20160428_models.UpdateDhcpOptionsSetAttributeRequest,
    ) -> vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dhcp_options_set_attribute_with_options_async(request, runtime)

    def update_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.UpdateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateIpsecServerResponse().from_map(
            self.do_rpcrequest('UpdateIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ipsec_server_with_options_async(
        self,
        request: vpc_20160428_models.UpdateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateIpsecServerResponse().from_map(
            await self.do_rpcrequest_async('UpdateIpsecServer', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ipsec_server(
        self,
        request: vpc_20160428_models.UpdateIpsecServerRequest,
    ) -> vpc_20160428_models.UpdateIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ipsec_server_with_options(request, runtime)

    async def update_ipsec_server_async(
        self,
        request: vpc_20160428_models.UpdateIpsecServerRequest,
    ) -> vpc_20160428_models.UpdateIpsecServerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ipsec_server_with_options_async(request, runtime)

    def update_nat_gateway_nat_type_with_options(
        self,
        request: vpc_20160428_models.UpdateNatGatewayNatTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateNatGatewayNatTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateNatGatewayNatTypeResponse().from_map(
            self.do_rpcrequest('UpdateNatGatewayNatType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_nat_gateway_nat_type_with_options_async(
        self,
        request: vpc_20160428_models.UpdateNatGatewayNatTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateNatGatewayNatTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateNatGatewayNatTypeResponse().from_map(
            await self.do_rpcrequest_async('UpdateNatGatewayNatType', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_nat_gateway_nat_type(
        self,
        request: vpc_20160428_models.UpdateNatGatewayNatTypeRequest,
    ) -> vpc_20160428_models.UpdateNatGatewayNatTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_nat_gateway_nat_type_with_options(request, runtime)

    async def update_nat_gateway_nat_type_async(
        self,
        request: vpc_20160428_models.UpdateNatGatewayNatTypeRequest,
    ) -> vpc_20160428_models.UpdateNatGatewayNatTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_nat_gateway_nat_type_with_options_async(request, runtime)

    def update_network_acl_entries_with_options(
        self,
        request: vpc_20160428_models.UpdateNetworkAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateNetworkAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateNetworkAclEntriesResponse().from_map(
            self.do_rpcrequest('UpdateNetworkAclEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_network_acl_entries_with_options_async(
        self,
        request: vpc_20160428_models.UpdateNetworkAclEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateNetworkAclEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateNetworkAclEntriesResponse().from_map(
            await self.do_rpcrequest_async('UpdateNetworkAclEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_network_acl_entries(
        self,
        request: vpc_20160428_models.UpdateNetworkAclEntriesRequest,
    ) -> vpc_20160428_models.UpdateNetworkAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_network_acl_entries_with_options(request, runtime)

    async def update_network_acl_entries_async(
        self,
        request: vpc_20160428_models.UpdateNetworkAclEntriesRequest,
    ) -> vpc_20160428_models.UpdateNetworkAclEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_network_acl_entries_with_options_async(request, runtime)

    def update_virtual_border_bandwidth_with_options(
        self,
        request: vpc_20160428_models.UpdateVirtualBorderBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVirtualBorderBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateVirtualBorderBandwidthResponse().from_map(
            self.do_rpcrequest('UpdateVirtualBorderBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_virtual_border_bandwidth_with_options_async(
        self,
        request: vpc_20160428_models.UpdateVirtualBorderBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVirtualBorderBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return vpc_20160428_models.UpdateVirtualBorderBandwidthResponse().from_map(
            await self.do_rpcrequest_async('UpdateVirtualBorderBandwidth', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_virtual_border_bandwidth(
        self,
        request: vpc_20160428_models.UpdateVirtualBorderBandwidthRequest,
    ) -> vpc_20160428_models.UpdateVirtualBorderBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_virtual_border_bandwidth_with_options(request, runtime)

    async def update_virtual_border_bandwidth_async(
        self,
        request: vpc_20160428_models.UpdateVirtualBorderBandwidthRequest,
    ) -> vpc_20160428_models.UpdateVirtualBorderBandwidthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_virtual_border_bandwidth_with_options_async(request, runtime)
