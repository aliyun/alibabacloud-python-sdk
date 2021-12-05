# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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
            'us-east-1': 'vpc.aliyuncs.com',
            'us-west-1': 'vpc.aliyuncs.com',
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
            'cn-huhehaote-nebula-1': 'vpc-nebula.cn-qingdao-nebula.aliyuncs.com',
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
            'cn-zhangbei': 'vpc.aliyuncs.com',
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
        return TeaCore.from_map(
            vpc_20160428_models.ActivateRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ActivateRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ActiveFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ActiveFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddBgpNetworkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddBgpNetworkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddCommonBandwidthPackageIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddCommonBandwidthPackageIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddCommonBandwidthPackageIpsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddCommonBandwidthPackageIpsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse(),
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

    def add_sources_to_traffic_mirror_session_with_options(
        self,
        request: vpc_20160428_models.AddSourcesToTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse(),
            self.do_rpcrequest('AddSourcesToTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_sources_to_traffic_mirror_session_with_options_async(
        self,
        request: vpc_20160428_models.AddSourcesToTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse(),
            await self.do_rpcrequest_async('AddSourcesToTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sources_to_traffic_mirror_session(
        self,
        request: vpc_20160428_models.AddSourcesToTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_sources_to_traffic_mirror_session_with_options(request, runtime)

    async def add_sources_to_traffic_mirror_session_async(
        self,
        request: vpc_20160428_models.AddSourcesToTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.AddSourcesToTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_sources_to_traffic_mirror_session_with_options_async(request, runtime)

    def allocate_eip_address_with_options(
        self,
        request: vpc_20160428_models.AllocateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AllocateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipAddressProResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipAddressProResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipSegmentAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateEipSegmentAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateIpv6InternetBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AllocateIpv6InternetBandwidthResponse(),
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

    def apply_physical_connection_loawith_options(
        self,
        request: vpc_20160428_models.ApplyPhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ApplyPhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ApplyPhysicalConnectionLOAResponse(),
            self.do_rpcrequest('ApplyPhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_physical_connection_loawith_options_async(
        self,
        request: vpc_20160428_models.ApplyPhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ApplyPhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ApplyPhysicalConnectionLOAResponse(),
            await self.do_rpcrequest_async('ApplyPhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_physical_connection_loa(
        self,
        request: vpc_20160428_models.ApplyPhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.ApplyPhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_physical_connection_loawith_options(request, runtime)

    async def apply_physical_connection_loa_async(
        self,
        request: vpc_20160428_models.ApplyPhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.ApplyPhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_physical_connection_loawith_options_async(request, runtime)

    def associate_eip_address_with_options(
        self,
        request: vpc_20160428_models.AssociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTableResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTableResponse(),
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

    def associate_route_table_with_gateway_with_options(
        self,
        request: vpc_20160428_models.AssociateRouteTableWithGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTableWithGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTableWithGatewayResponse(),
            self.do_rpcrequest('AssociateRouteTableWithGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_route_table_with_gateway_with_options_async(
        self,
        request: vpc_20160428_models.AssociateRouteTableWithGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTableWithGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTableWithGatewayResponse(),
            await self.do_rpcrequest_async('AssociateRouteTableWithGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_route_table_with_gateway(
        self,
        request: vpc_20160428_models.AssociateRouteTableWithGatewayRequest,
    ) -> vpc_20160428_models.AssociateRouteTableWithGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_route_table_with_gateway_with_options(request, runtime)

    async def associate_route_table_with_gateway_async(
        self,
        request: vpc_20160428_models.AssociateRouteTableWithGatewayRequest,
    ) -> vpc_20160428_models.AssociateRouteTableWithGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_route_table_with_gateway_with_options_async(request, runtime)

    def associate_route_tables_with_vpc_gateway_endpoint_with_options(
        self,
        request: vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse(),
            self.do_rpcrequest('AssociateRouteTablesWithVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def associate_route_tables_with_vpc_gateway_endpoint_with_options_async(
        self,
        request: vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse(),
            await self.do_rpcrequest_async('AssociateRouteTablesWithVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate_route_tables_with_vpc_gateway_endpoint(
        self,
        request: vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.associate_route_tables_with_vpc_gateway_endpoint_with_options(request, runtime)

    async def associate_route_tables_with_vpc_gateway_endpoint_async(
        self,
        request: vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.AssociateRouteTablesWithVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.associate_route_tables_with_vpc_gateway_endpoint_with_options_async(request, runtime)

    def associate_vpc_cidr_block_with_options(
        self,
        request: vpc_20160428_models.AssociateVpcCidrBlockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AssociateVpcCidrBlockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AssociateVpcCidrBlockResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateVpcCidrBlockResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AssociateVpnGatewayWithCertificateResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse(),
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

    def attach_vbr_to_vpconn_with_options(
        self,
        request: vpc_20160428_models.AttachVbrToVpconnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AttachVbrToVpconnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AttachVbrToVpconnResponse(),
            self.do_rpcrequest('AttachVbrToVpconn', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_vbr_to_vpconn_with_options_async(
        self,
        request: vpc_20160428_models.AttachVbrToVpconnRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.AttachVbrToVpconnResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.AttachVbrToVpconnResponse(),
            await self.do_rpcrequest_async('AttachVbrToVpconn', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_vbr_to_vpconn(
        self,
        request: vpc_20160428_models.AttachVbrToVpconnRequest,
    ) -> vpc_20160428_models.AttachVbrToVpconnResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_vbr_to_vpconn_with_options(request, runtime)

    async def attach_vbr_to_vpconn_async(
        self,
        request: vpc_20160428_models.AttachVbrToVpconnRequest,
    ) -> vpc_20160428_models.AttachVbrToVpconnResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_vbr_to_vpconn_with_options_async(request, runtime)

    def cancel_common_bandwidth_package_ip_bandwidth_with_options(
        self,
        request: vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CancelExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CancelExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CancelPhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CancelPhysicalConnectionResponse(),
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

    def complete_physical_connection_loawith_options(
        self,
        request: vpc_20160428_models.CompletePhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CompletePhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CompletePhysicalConnectionLOAResponse(),
            self.do_rpcrequest('CompletePhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def complete_physical_connection_loawith_options_async(
        self,
        request: vpc_20160428_models.CompletePhysicalConnectionLOARequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CompletePhysicalConnectionLOAResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CompletePhysicalConnectionLOAResponse(),
            await self.do_rpcrequest_async('CompletePhysicalConnectionLOA', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_physical_connection_loa(
        self,
        request: vpc_20160428_models.CompletePhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.CompletePhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return self.complete_physical_connection_loawith_options(request, runtime)

    async def complete_physical_connection_loa_async(
        self,
        request: vpc_20160428_models.CompletePhysicalConnectionLOARequest,
    ) -> vpc_20160428_models.CompletePhysicalConnectionLOAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.complete_physical_connection_loawith_options_async(request, runtime)

    def confirm_physical_connection_with_options(
        self,
        request: vpc_20160428_models.ConfirmPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ConfirmPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ConfirmPhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ConfirmPhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ConnectRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ConnectRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ConvertBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ConvertBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CopyNetworkAclEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CopyNetworkAclEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateBgpGroupResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateBgpGroupResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateBgpPeerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateBgpPeerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateCommonBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateCommonBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateForwardEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateForwardEntryResponse(),
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

    def create_full_nat_entry_with_options(
        self,
        request: vpc_20160428_models.CreateFullNatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateFullNatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateFullNatEntryResponse(),
            self.do_rpcrequest('CreateFullNatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_full_nat_entry_with_options_async(
        self,
        request: vpc_20160428_models.CreateFullNatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateFullNatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateFullNatEntryResponse(),
            await self.do_rpcrequest_async('CreateFullNatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_full_nat_entry(
        self,
        request: vpc_20160428_models.CreateFullNatEntryRequest,
    ) -> vpc_20160428_models.CreateFullNatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_full_nat_entry_with_options(request, runtime)

    async def create_full_nat_entry_async(
        self,
        request: vpc_20160428_models.CreateFullNatEntryRequest,
    ) -> vpc_20160428_models.CreateFullNatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_full_nat_entry_with_options_async(request, runtime)

    def create_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.CreateGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateHaVipResponse(),
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

    def create_ipv_6translator_with_options(
        self,
        request: vpc_20160428_models.CreateIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorAclListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorAclListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIPv6TranslatorEntryResponse(),
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

    def create_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.CreateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpsecServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpsecServerResponse(),
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

    def create_ipv_4gateway_with_options(
        self,
        request: vpc_20160428_models.CreateIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv4GatewayResponse(),
            self.do_rpcrequest('CreateIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_ipv_4gateway_with_options_async(
        self,
        request: vpc_20160428_models.CreateIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv4GatewayResponse(),
            await self.do_rpcrequest_async('CreateIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_ipv_4gateway(
        self,
        request: vpc_20160428_models.CreateIpv4GatewayRequest,
    ) -> vpc_20160428_models.CreateIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_ipv_4gateway_with_options(request, runtime)

    async def create_ipv_4gateway_async(
        self,
        request: vpc_20160428_models.CreateIpv4GatewayRequest,
    ) -> vpc_20160428_models.CreateIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_ipv_4gateway_with_options_async(request, runtime)

    def create_ipv_6egress_only_rule_with_options(
        self,
        request: vpc_20160428_models.CreateIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv6GatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateIpv6GatewayResponse(),
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

    def create_nat_gateway_with_options(
        self,
        request: vpc_20160428_models.CreateNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatGatewayResponse(),
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

    def create_nat_ip_with_options(
        self,
        request: vpc_20160428_models.CreateNatIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatIpResponse(),
            self.do_rpcrequest('CreateNatIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nat_ip_with_options_async(
        self,
        request: vpc_20160428_models.CreateNatIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatIpResponse(),
            await self.do_rpcrequest_async('CreateNatIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nat_ip(
        self,
        request: vpc_20160428_models.CreateNatIpRequest,
    ) -> vpc_20160428_models.CreateNatIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nat_ip_with_options(request, runtime)

    async def create_nat_ip_async(
        self,
        request: vpc_20160428_models.CreateNatIpRequest,
    ) -> vpc_20160428_models.CreateNatIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_ip_with_options_async(request, runtime)

    def create_nat_ip_cidr_with_options(
        self,
        request: vpc_20160428_models.CreateNatIpCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatIpCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatIpCidrResponse(),
            self.do_rpcrequest('CreateNatIpCidr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nat_ip_cidr_with_options_async(
        self,
        request: vpc_20160428_models.CreateNatIpCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNatIpCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNatIpCidrResponse(),
            await self.do_rpcrequest_async('CreateNatIpCidr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nat_ip_cidr(
        self,
        request: vpc_20160428_models.CreateNatIpCidrRequest,
    ) -> vpc_20160428_models.CreateNatIpCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nat_ip_cidr_with_options(request, runtime)

    async def create_nat_ip_cidr_async(
        self,
        request: vpc_20160428_models.CreateNatIpCidrRequest,
    ) -> vpc_20160428_models.CreateNatIpCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nat_ip_cidr_with_options_async(request, runtime)

    def create_network_acl_with_options(
        self,
        request: vpc_20160428_models.CreateNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateNetworkAclResponse(),
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

    def create_physical_connection_with_options(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionResponse(),
            self.do_rpcrequest('CreatePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionResponse(),
            await self.do_rpcrequest_async('CreatePhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_connection(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_with_options(request, runtime)

    async def create_physical_connection_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_connection_with_options_async(request, runtime)

    def create_physical_connection_occupancy_order_with_options(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse(),
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

    def create_physical_connection_setup_order_with_options(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionSetupOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse(),
            self.do_rpcrequest('CreatePhysicalConnectionSetupOrder', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_physical_connection_setup_order_with_options_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionSetupOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse(),
            await self.do_rpcrequest_async('CreatePhysicalConnectionSetupOrder', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_physical_connection_setup_order(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionSetupOrderRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_physical_connection_setup_order_with_options(request, runtime)

    async def create_physical_connection_setup_order_async(
        self,
        request: vpc_20160428_models.CreatePhysicalConnectionSetupOrderRequest,
    ) -> vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_physical_connection_setup_order_with_options_async(request, runtime)

    def create_route_entry_with_options(
        self,
        request: vpc_20160428_models.CreateRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouteTableResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouteTableResponse(),
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

    def create_router_interface_with_options(
        self,
        request: vpc_20160428_models.CreateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouterInterfaceResponse(),
            self.do_rpcrequest('CreateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_router_interface_with_options_async(
        self,
        request: vpc_20160428_models.CreateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateRouterInterfaceResponse(),
            await self.do_rpcrequest_async('CreateRouterInterface', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_router_interface(
        self,
        request: vpc_20160428_models.CreateRouterInterfaceRequest,
    ) -> vpc_20160428_models.CreateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_router_interface_with_options(request, runtime)

    async def create_router_interface_async(
        self,
        request: vpc_20160428_models.CreateRouterInterfaceRequest,
    ) -> vpc_20160428_models.CreateRouterInterfaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_router_interface_with_options_async(request, runtime)

    def create_snat_entry_with_options(
        self,
        request: vpc_20160428_models.CreateSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateSnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateSnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateSslVpnServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateSslVpnServerResponse(),
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

    def create_traffic_mirror_filter_with_options(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorFilterResponse(),
            self.do_rpcrequest('CreateTrafficMirrorFilter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_traffic_mirror_filter_with_options_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorFilterResponse(),
            await self.do_rpcrequest_async('CreateTrafficMirrorFilter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_traffic_mirror_filter(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_mirror_filter_with_options(request, runtime)

    async def create_traffic_mirror_filter_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_mirror_filter_with_options_async(request, runtime)

    def create_traffic_mirror_filter_rules_with_options(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse(),
            self.do_rpcrequest('CreateTrafficMirrorFilterRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_traffic_mirror_filter_rules_with_options_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse(),
            await self.do_rpcrequest_async('CreateTrafficMirrorFilterRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_traffic_mirror_filter_rules(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRulesRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_mirror_filter_rules_with_options(request, runtime)

    async def create_traffic_mirror_filter_rules_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorFilterRulesRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorFilterRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_mirror_filter_rules_with_options_async(request, runtime)

    def create_traffic_mirror_session_with_options(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorSessionResponse(),
            self.do_rpcrequest('CreateTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_traffic_mirror_session_with_options_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateTrafficMirrorSessionResponse(),
            await self.do_rpcrequest_async('CreateTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_traffic_mirror_session(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_traffic_mirror_session_with_options(request, runtime)

    async def create_traffic_mirror_session_async(
        self,
        request: vpc_20160428_models.CreateTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.CreateTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_traffic_mirror_session_with_options_async(request, runtime)

    def create_vswitch_with_options(
        self,
        request: vpc_20160428_models.CreateVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVSwitchResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVSwitchResponse(),
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

    def create_vbr_ha_with_options(
        self,
        request: vpc_20160428_models.CreateVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVbrHaResponse(),
            self.do_rpcrequest('CreateVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vbr_ha_with_options_async(
        self,
        request: vpc_20160428_models.CreateVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVbrHaResponse(),
            await self.do_rpcrequest_async('CreateVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vbr_ha(
        self,
        request: vpc_20160428_models.CreateVbrHaRequest,
    ) -> vpc_20160428_models.CreateVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vbr_ha_with_options(request, runtime)

    async def create_vbr_ha_async(
        self,
        request: vpc_20160428_models.CreateVbrHaRequest,
    ) -> vpc_20160428_models.CreateVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vbr_ha_with_options_async(request, runtime)

    def create_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.CreateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVirtualBorderRouterResponse(),
            self.do_rpcrequest('CreateVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_border_router_with_options_async(
        self,
        request: vpc_20160428_models.CreateVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVirtualBorderRouterResponse(),
            await self.do_rpcrequest_async('CreateVirtualBorderRouter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_border_router(
        self,
        request: vpc_20160428_models.CreateVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.CreateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_border_router_with_options(request, runtime)

    async def create_virtual_border_router_async(
        self,
        request: vpc_20160428_models.CreateVirtualBorderRouterRequest,
    ) -> vpc_20160428_models.CreateVirtualBorderRouterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_border_router_with_options_async(request, runtime)

    def create_virtual_physical_connection_with_options(
        self,
        request: vpc_20160428_models.CreateVirtualPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVirtualPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVirtualPhysicalConnectionResponse(),
            self.do_rpcrequest('CreateVirtualPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_virtual_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.CreateVirtualPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVirtualPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVirtualPhysicalConnectionResponse(),
            await self.do_rpcrequest_async('CreateVirtualPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_virtual_physical_connection(
        self,
        request: vpc_20160428_models.CreateVirtualPhysicalConnectionRequest,
    ) -> vpc_20160428_models.CreateVirtualPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_virtual_physical_connection_with_options(request, runtime)

    async def create_virtual_physical_connection_async(
        self,
        request: vpc_20160428_models.CreateVirtualPhysicalConnectionRequest,
    ) -> vpc_20160428_models.CreateVirtualPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_virtual_physical_connection_with_options_async(request, runtime)

    def create_vpc_with_options(
        self,
        request: vpc_20160428_models.CreateVpcRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpcResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpcResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpcResponse(),
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

    def create_vpc_gateway_endpoint_with_options(
        self,
        request: vpc_20160428_models.CreateVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpcGatewayEndpointResponse(),
            self.do_rpcrequest('CreateVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpc_gateway_endpoint_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpcGatewayEndpointResponse(),
            await self.do_rpcrequest_async('CreateVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpc_gateway_endpoint(
        self,
        request: vpc_20160428_models.CreateVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.CreateVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpc_gateway_endpoint_with_options(request, runtime)

    async def create_vpc_gateway_endpoint_async(
        self,
        request: vpc_20160428_models.CreateVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.CreateVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpc_gateway_endpoint_with_options_async(request, runtime)

    def create_vpconn_from_vbr_with_options(
        self,
        request: vpc_20160428_models.CreateVpconnFromVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpconnFromVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpconnFromVbrResponse(),
            self.do_rpcrequest('CreateVpconnFromVbr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_vpconn_from_vbr_with_options_async(
        self,
        request: vpc_20160428_models.CreateVpconnFromVbrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpconnFromVbrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpconnFromVbrResponse(),
            await self.do_rpcrequest_async('CreateVpconnFromVbr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vpconn_from_vbr(
        self,
        request: vpc_20160428_models.CreateVpconnFromVbrRequest,
    ) -> vpc_20160428_models.CreateVpconnFromVbrResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_vpconn_from_vbr_with_options(request, runtime)

    async def create_vpconn_from_vbr_async(
        self,
        request: vpc_20160428_models.CreateVpconnFromVbrRequest,
    ) -> vpc_20160428_models.CreateVpconnFromVbrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_vpconn_from_vbr_with_options_async(request, runtime)

    def create_vpn_connection_with_options(
        self,
        request: vpc_20160428_models.CreateVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.CreateVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnPbrRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnPbrRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.CreateVpnRouteEntryResponse(),
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

    def deactivate_router_interface_with_options(
        self,
        request: vpc_20160428_models.DeactivateRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeactivateRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeactivateRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeactivateRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeactiveFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeactiveFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpGroupResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpGroupResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpNetworkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpNetworkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpPeerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteBgpPeerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteCommonBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteCommonBandwidthPackageResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteExpressCloudConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteExpressConnectResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteExpressConnectResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteFlowLogResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteForwardEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteForwardEntryResponse(),
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

    def delete_full_nat_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteFullNatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteFullNatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteFullNatEntryResponse(),
            self.do_rpcrequest('DeleteFullNatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_full_nat_entry_with_options_async(
        self,
        request: vpc_20160428_models.DeleteFullNatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteFullNatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteFullNatEntryResponse(),
            await self.do_rpcrequest_async('DeleteFullNatEntry', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_full_nat_entry(
        self,
        request: vpc_20160428_models.DeleteFullNatEntryRequest,
    ) -> vpc_20160428_models.DeleteFullNatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_full_nat_entry_with_options(request, runtime)

    async def delete_full_nat_entry_async(
        self,
        request: vpc_20160428_models.DeleteFullNatEntryRequest,
    ) -> vpc_20160428_models.DeleteFullNatEntryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_full_nat_entry_with_options_async(request, runtime)

    def delete_global_acceleration_instance_with_options(
        self,
        request: vpc_20160428_models.DeleteGlobalAccelerationInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteHaVipResponse(),
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

    def delete_ipv_6translator_with_options(
        self,
        request: vpc_20160428_models.DeleteIPv6TranslatorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIPv6TranslatorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorAclListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorAclListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIPv6TranslatorEntryResponse(),
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

    def delete_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.DeleteIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpsecServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpsecServerResponse(),
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

    def delete_ipv_4gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv4GatewayResponse(),
            self.do_rpcrequest('DeleteIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_ipv_4gateway_with_options_async(
        self,
        request: vpc_20160428_models.DeleteIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv4GatewayResponse(),
            await self.do_rpcrequest_async('DeleteIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_ipv_4gateway(
        self,
        request: vpc_20160428_models.DeleteIpv4GatewayRequest,
    ) -> vpc_20160428_models.DeleteIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_ipv_4gateway_with_options(request, runtime)

    async def delete_ipv_4gateway_async(
        self,
        request: vpc_20160428_models.DeleteIpv4GatewayRequest,
    ) -> vpc_20160428_models.DeleteIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_ipv_4gateway_with_options_async(request, runtime)

    def delete_ipv_6egress_only_rule_with_options(
        self,
        request: vpc_20160428_models.DeleteIpv6EgressOnlyRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6GatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6GatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6InternetBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteIpv6InternetBandwidthResponse(),
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

    def delete_nat_gateway_with_options(
        self,
        request: vpc_20160428_models.DeleteNatGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatGatewayResponse(),
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

    def delete_nat_ip_with_options(
        self,
        request: vpc_20160428_models.DeleteNatIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatIpResponse(),
            self.do_rpcrequest('DeleteNatIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nat_ip_with_options_async(
        self,
        request: vpc_20160428_models.DeleteNatIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatIpResponse(),
            await self.do_rpcrequest_async('DeleteNatIp', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nat_ip(
        self,
        request: vpc_20160428_models.DeleteNatIpRequest,
    ) -> vpc_20160428_models.DeleteNatIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_ip_with_options(request, runtime)

    async def delete_nat_ip_async(
        self,
        request: vpc_20160428_models.DeleteNatIpRequest,
    ) -> vpc_20160428_models.DeleteNatIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_ip_with_options_async(request, runtime)

    def delete_nat_ip_cidr_with_options(
        self,
        request: vpc_20160428_models.DeleteNatIpCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatIpCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatIpCidrResponse(),
            self.do_rpcrequest('DeleteNatIpCidr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nat_ip_cidr_with_options_async(
        self,
        request: vpc_20160428_models.DeleteNatIpCidrRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNatIpCidrResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNatIpCidrResponse(),
            await self.do_rpcrequest_async('DeleteNatIpCidr', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nat_ip_cidr(
        self,
        request: vpc_20160428_models.DeleteNatIpCidrRequest,
    ) -> vpc_20160428_models.DeleteNatIpCidrResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nat_ip_cidr_with_options(request, runtime)

    async def delete_nat_ip_cidr_async(
        self,
        request: vpc_20160428_models.DeleteNatIpCidrRequest,
    ) -> vpc_20160428_models.DeleteNatIpCidrResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nat_ip_cidr_with_options_async(request, runtime)

    def delete_network_acl_with_options(
        self,
        request: vpc_20160428_models.DeleteNetworkAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteNetworkAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeletePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeletePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouteEntryResponse(),
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

    def delete_route_table_with_options(
        self,
        request: vpc_20160428_models.DeleteRouteTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouteTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouteTableResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouteTableResponse(),
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

    def delete_router_interface_with_options(
        self,
        request: vpc_20160428_models.DeleteRouterInterfaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteRouterInterfaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouterInterfaceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteRouterInterfaceResponse(),
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

    def delete_snat_entry_with_options(
        self,
        request: vpc_20160428_models.DeleteSnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteSnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSslVpnServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteSslVpnServerResponse(),
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

    def delete_traffic_mirror_filter_with_options(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorFilterResponse(),
            self.do_rpcrequest('DeleteTrafficMirrorFilter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_traffic_mirror_filter_with_options_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorFilterResponse(),
            await self.do_rpcrequest_async('DeleteTrafficMirrorFilter', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_traffic_mirror_filter(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_mirror_filter_with_options(request, runtime)

    async def delete_traffic_mirror_filter_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_mirror_filter_with_options_async(request, runtime)

    def delete_traffic_mirror_filter_rules_with_options(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse(),
            self.do_rpcrequest('DeleteTrafficMirrorFilterRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_traffic_mirror_filter_rules_with_options_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse(),
            await self.do_rpcrequest_async('DeleteTrafficMirrorFilterRules', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_traffic_mirror_filter_rules(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRulesRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_mirror_filter_rules_with_options(request, runtime)

    async def delete_traffic_mirror_filter_rules_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorFilterRulesRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorFilterRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_mirror_filter_rules_with_options_async(request, runtime)

    def delete_traffic_mirror_session_with_options(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorSessionResponse(),
            self.do_rpcrequest('DeleteTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_traffic_mirror_session_with_options_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteTrafficMirrorSessionResponse(),
            await self.do_rpcrequest_async('DeleteTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_traffic_mirror_session(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_traffic_mirror_session_with_options(request, runtime)

    async def delete_traffic_mirror_session_async(
        self,
        request: vpc_20160428_models.DeleteTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.DeleteTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_traffic_mirror_session_with_options_async(request, runtime)

    def delete_vswitch_with_options(
        self,
        request: vpc_20160428_models.DeleteVSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVSwitchResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVSwitchResponse(),
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

    def delete_vbr_ha_with_options(
        self,
        request: vpc_20160428_models.DeleteVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVbrHaResponse(),
            self.do_rpcrequest('DeleteVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vbr_ha_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVbrHaResponse(),
            await self.do_rpcrequest_async('DeleteVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vbr_ha(
        self,
        request: vpc_20160428_models.DeleteVbrHaRequest,
    ) -> vpc_20160428_models.DeleteVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vbr_ha_with_options(request, runtime)

    async def delete_vbr_ha_async(
        self,
        request: vpc_20160428_models.DeleteVbrHaRequest,
    ) -> vpc_20160428_models.DeleteVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vbr_ha_with_options_async(request, runtime)

    def delete_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.DeleteVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpcResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpcResponse(),
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

    def delete_vpc_gateway_endpoint_with_options(
        self,
        request: vpc_20160428_models.DeleteVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpcGatewayEndpointResponse(),
            self.do_rpcrequest('DeleteVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_vpc_gateway_endpoint_with_options_async(
        self,
        request: vpc_20160428_models.DeleteVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpcGatewayEndpointResponse(),
            await self.do_rpcrequest_async('DeleteVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vpc_gateway_endpoint(
        self,
        request: vpc_20160428_models.DeleteVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.DeleteVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_vpc_gateway_endpoint_with_options(request, runtime)

    async def delete_vpc_gateway_endpoint_async(
        self,
        request: vpc_20160428_models.DeleteVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.DeleteVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_vpc_gateway_endpoint_with_options_async(request, runtime)

    def delete_vpn_connection_with_options(
        self,
        request: vpc_20160428_models.DeleteVpnConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeleteVpnConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnPbrRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnPbrRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeleteVpnRouteEntryResponse(),
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

    def deletion_protection_with_options(
        self,
        request: vpc_20160428_models.DeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DeletionProtectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DeletionProtectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DeletionProtectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeAccessPointsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeAccessPointsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpGroupsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpGroupsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpNetworksResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpNetworksResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpPeersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeBgpPeersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCommonBandwidthPackagesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCommonBandwidthPackagesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCustomerGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCustomerGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeCustomerGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipAddressesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipAddressesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipGatewayInfoResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipGatewayInfoResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipMonitorDataResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipMonitorDataResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipSegmentResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeEipSegmentResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeExpressCloudConnectionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeExpressCloudConnectionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeFlowLogsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeFlowLogsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeForwardTableEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeForwardTableEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeGrantRulesToCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeGrantRulesToCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeHaVipsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeHaVipsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse(),
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

    def describe_ipv_6translator_acl_list_attributes_with_options(
        self,
        request: vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIPv6TranslatorsResponse(),
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

    def describe_instance_auto_renew_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeInstanceAutoRenewAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6AddressesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6AddressesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6GatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6GatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6GatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeIpv6GatewaysResponse(),
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

    def describe_nat_gateways_with_options(
        self,
        request: vpc_20160428_models.DescribeNatGatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeNatGatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNatGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNatGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNetworkAclAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNetworkAclAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNetworkAclsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNetworkAclsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribePhysicalConnectionLOAResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribePhysicalConnectionLOAResponse(),
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

    def describe_physical_connections_with_options(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribePhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribePhysicalConnectionsResponse(),
            self.do_rpcrequest('DescribePhysicalConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_physical_connections_with_options_async(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribePhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribePhysicalConnectionsResponse(),
            await self.do_rpcrequest_async('DescribePhysicalConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_physical_connections(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionsRequest,
    ) -> vpc_20160428_models.DescribePhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_physical_connections_with_options(request, runtime)

    async def describe_physical_connections_async(
        self,
        request: vpc_20160428_models.DescribePhysicalConnectionsRequest,
    ) -> vpc_20160428_models.DescribePhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_physical_connections_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: vpc_20160428_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRegionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRegionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteEntryListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteEntryListResponse(),
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

    def describe_route_table_list_with_options(
        self,
        request: vpc_20160428_models.DescribeRouteTableListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouteTableListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteTableListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteTableListResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteTablesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouteTablesResponse(),
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

    def describe_router_interface_attribute_with_options(
        self,
        request: vpc_20160428_models.DescribeRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouterInterfaceAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouterInterfaceAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouterInterfacesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeRouterInterfacesResponse(),
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

    def describe_server_related_global_acceleration_instances_with_options(
        self,
        request: vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSnatTableEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSnatTableEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnClientCertsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnClientCertsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnServersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeSslVpnServersResponse(),
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

    def describe_vrouters_with_options(
        self,
        request: vpc_20160428_models.DescribeVRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVRoutersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVRoutersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVSwitchAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVSwitchAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVSwitchesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVSwitchesResponse(),
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

    def describe_vbr_ha_with_options(
        self,
        request: vpc_20160428_models.DescribeVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVbrHaResponse(),
            self.do_rpcrequest('DescribeVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_vbr_ha_with_options_async(
        self,
        request: vpc_20160428_models.DescribeVbrHaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVbrHaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVbrHaResponse(),
            await self.do_rpcrequest_async('DescribeVbrHa', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vbr_ha(
        self,
        request: vpc_20160428_models.DescribeVbrHaRequest,
    ) -> vpc_20160428_models.DescribeVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_vbr_ha_with_options(request, runtime)

    async def describe_vbr_ha_async(
        self,
        request: vpc_20160428_models.DescribeVbrHaRequest,
    ) -> vpc_20160428_models.DescribeVbrHaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_vbr_ha_with_options_async(request, runtime)

    def describe_virtual_border_routers_with_options(
        self,
        request: vpc_20160428_models.DescribeVirtualBorderRoutersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeVirtualBorderRoutersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVirtualBorderRoutersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVirtualBorderRoutersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpcAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpcAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpcsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpcsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnConnectionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnConnectionsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnGatewayResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnGatewaysResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnRouteEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnRouteEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnSslServerLogsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeVpnSslServerLogsResponse(),
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

    def describe_zones_with_options(
        self,
        request: vpc_20160428_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DescribeZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DescribeZonesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DescribeZonesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DisableNatGatewayEcsMetricResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DisableNatGatewayEcsMetricResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DisableVpcClassicLinkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DisableVpcClassicLinkResponse(),
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

    def dissociate_route_table_from_gateway_with_options(
        self,
        request: vpc_20160428_models.DissociateRouteTableFromGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateRouteTableFromGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DissociateRouteTableFromGatewayResponse(),
            self.do_rpcrequest('DissociateRouteTableFromGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_route_table_from_gateway_with_options_async(
        self,
        request: vpc_20160428_models.DissociateRouteTableFromGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateRouteTableFromGatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DissociateRouteTableFromGatewayResponse(),
            await self.do_rpcrequest_async('DissociateRouteTableFromGateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_route_table_from_gateway(
        self,
        request: vpc_20160428_models.DissociateRouteTableFromGatewayRequest,
    ) -> vpc_20160428_models.DissociateRouteTableFromGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_route_table_from_gateway_with_options(request, runtime)

    async def dissociate_route_table_from_gateway_async(
        self,
        request: vpc_20160428_models.DissociateRouteTableFromGatewayRequest,
    ) -> vpc_20160428_models.DissociateRouteTableFromGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_route_table_from_gateway_with_options_async(request, runtime)

    def dissociate_route_tables_from_vpc_gateway_endpoint_with_options(
        self,
        request: vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse(),
            self.do_rpcrequest('DissociateRouteTablesFromVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dissociate_route_tables_from_vpc_gateway_endpoint_with_options_async(
        self,
        request: vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse(),
            await self.do_rpcrequest_async('DissociateRouteTablesFromVpcGatewayEndpoint', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dissociate_route_tables_from_vpc_gateway_endpoint(
        self,
        request: vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.dissociate_route_tables_from_vpc_gateway_endpoint_with_options(request, runtime)

    async def dissociate_route_tables_from_vpc_gateway_endpoint_async(
        self,
        request: vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointRequest,
    ) -> vpc_20160428_models.DissociateRouteTablesFromVpcGatewayEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dissociate_route_tables_from_vpc_gateway_endpoint_with_options_async(request, runtime)

    def dissociate_vpn_gateway_with_certificate_with_options(
        self,
        request: vpc_20160428_models.DissociateVpnGatewayWithCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DissociateVpnGatewayWithCertificateResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DownloadVpnConnectionConfigResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.DownloadVpnConnectionConfigResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnableNatGatewayEcsMetricResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnableNatGatewayEcsMetricResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnablePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnablePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnableVpcClassicLinkResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.EnableVpcClassicLinkResponse(),
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

    def enable_vpc_ipv_4gateway_with_options(
        self,
        request: vpc_20160428_models.EnableVpcIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableVpcIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.EnableVpcIpv4GatewayResponse(),
            self.do_rpcrequest('EnableVpcIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_vpc_ipv_4gateway_with_options_async(
        self,
        request: vpc_20160428_models.EnableVpcIpv4GatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.EnableVpcIpv4GatewayResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.EnableVpcIpv4GatewayResponse(),
            await self.do_rpcrequest_async('EnableVpcIpv4Gateway', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_vpc_ipv_4gateway(
        self,
        request: vpc_20160428_models.EnableVpcIpv4GatewayRequest,
    ) -> vpc_20160428_models.EnableVpcIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_vpc_ipv_4gateway_with_options(request, runtime)

    async def enable_vpc_ipv_4gateway_async(
        self,
        request: vpc_20160428_models.EnableVpcIpv4GatewayRequest,
    ) -> vpc_20160428_models.EnableVpcIpv4GatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_vpc_ipv_4gateway_with_options_async(request, runtime)

    def get_dhcp_options_set_with_options(
        self,
        request: vpc_20160428_models.GetDhcpOptionsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetDhcpOptionsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.GetDhcpOptionsSetResponse(),
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

    def get_ipv_4gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.GetIpv4GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetIpv4GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetIpv4GatewayAttributeResponse(),
            self.do_rpcrequest('GetIpv4GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_ipv_4gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.GetIpv4GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetIpv4GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetIpv4GatewayAttributeResponse(),
            await self.do_rpcrequest_async('GetIpv4GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ipv_4gateway_attribute(
        self,
        request: vpc_20160428_models.GetIpv4GatewayAttributeRequest,
    ) -> vpc_20160428_models.GetIpv4GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_ipv_4gateway_attribute_with_options(request, runtime)

    async def get_ipv_4gateway_attribute_async(
        self,
        request: vpc_20160428_models.GetIpv4GatewayAttributeRequest,
    ) -> vpc_20160428_models.GetIpv4GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_ipv_4gateway_attribute_with_options_async(request, runtime)

    def get_nat_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.GetNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetNatGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.GetNatGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.GetNatGatewayConvertStatusResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.GetNatGatewayConvertStatusResponse(),
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

    def get_physical_connection_service_status_with_options(
        self,
        request: vpc_20160428_models.GetPhysicalConnectionServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse(),
            self.do_rpcrequest('GetPhysicalConnectionServiceStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_physical_connection_service_status_with_options_async(
        self,
        request: vpc_20160428_models.GetPhysicalConnectionServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse(),
            await self.do_rpcrequest_async('GetPhysicalConnectionServiceStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_physical_connection_service_status(
        self,
        request: vpc_20160428_models.GetPhysicalConnectionServiceStatusRequest,
    ) -> vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_physical_connection_service_status_with_options(request, runtime)

    async def get_physical_connection_service_status_async(
        self,
        request: vpc_20160428_models.GetPhysicalConnectionServiceStatusRequest,
    ) -> vpc_20160428_models.GetPhysicalConnectionServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_physical_connection_service_status_with_options_async(request, runtime)

    def get_traffic_mirror_service_status_with_options(
        self,
        request: vpc_20160428_models.GetTrafficMirrorServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetTrafficMirrorServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetTrafficMirrorServiceStatusResponse(),
            self.do_rpcrequest('GetTrafficMirrorServiceStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_traffic_mirror_service_status_with_options_async(
        self,
        request: vpc_20160428_models.GetTrafficMirrorServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetTrafficMirrorServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetTrafficMirrorServiceStatusResponse(),
            await self.do_rpcrequest_async('GetTrafficMirrorServiceStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_traffic_mirror_service_status(
        self,
        request: vpc_20160428_models.GetTrafficMirrorServiceStatusRequest,
    ) -> vpc_20160428_models.GetTrafficMirrorServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_traffic_mirror_service_status_with_options(request, runtime)

    async def get_traffic_mirror_service_status_async(
        self,
        request: vpc_20160428_models.GetTrafficMirrorServiceStatusRequest,
    ) -> vpc_20160428_models.GetTrafficMirrorServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_traffic_mirror_service_status_with_options_async(request, runtime)

    def get_vpc_gateway_endpoint_attribute_with_options(
        self,
        request: vpc_20160428_models.GetVpcGatewayEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse(),
            self.do_rpcrequest('GetVpcGatewayEndpointAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_vpc_gateway_endpoint_attribute_with_options_async(
        self,
        request: vpc_20160428_models.GetVpcGatewayEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse(),
            await self.do_rpcrequest_async('GetVpcGatewayEndpointAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_vpc_gateway_endpoint_attribute(
        self,
        request: vpc_20160428_models.GetVpcGatewayEndpointAttributeRequest,
    ) -> vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_vpc_gateway_endpoint_attribute_with_options(request, runtime)

    async def get_vpc_gateway_endpoint_attribute_async(
        self,
        request: vpc_20160428_models.GetVpcGatewayEndpointAttributeRequest,
    ) -> vpc_20160428_models.GetVpcGatewayEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_vpc_gateway_endpoint_attribute_with_options_async(request, runtime)

    def grant_instance_to_cen_with_options(
        self,
        request: vpc_20160428_models.GrantInstanceToCenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.GrantInstanceToCenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.GrantInstanceToCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.GrantInstanceToCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListDhcpOptionsSetsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListDhcpOptionsSetsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListEnhanhcedNatGatewayAvailableZonesResponse(),
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

    def list_full_nat_entries_with_options(
        self,
        request: vpc_20160428_models.ListFullNatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListFullNatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListFullNatEntriesResponse(),
            self.do_rpcrequest('ListFullNatEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_full_nat_entries_with_options_async(
        self,
        request: vpc_20160428_models.ListFullNatEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListFullNatEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListFullNatEntriesResponse(),
            await self.do_rpcrequest_async('ListFullNatEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_full_nat_entries(
        self,
        request: vpc_20160428_models.ListFullNatEntriesRequest,
    ) -> vpc_20160428_models.ListFullNatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_full_nat_entries_with_options(request, runtime)

    async def list_full_nat_entries_async(
        self,
        request: vpc_20160428_models.ListFullNatEntriesRequest,
    ) -> vpc_20160428_models.ListFullNatEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_full_nat_entries_with_options_async(request, runtime)

    def list_gateway_route_table_entries_with_options(
        self,
        request: vpc_20160428_models.ListGatewayRouteTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListGatewayRouteTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListGatewayRouteTableEntriesResponse(),
            self.do_rpcrequest('ListGatewayRouteTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_gateway_route_table_entries_with_options_async(
        self,
        request: vpc_20160428_models.ListGatewayRouteTableEntriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListGatewayRouteTableEntriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListGatewayRouteTableEntriesResponse(),
            await self.do_rpcrequest_async('ListGatewayRouteTableEntries', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_gateway_route_table_entries(
        self,
        request: vpc_20160428_models.ListGatewayRouteTableEntriesRequest,
    ) -> vpc_20160428_models.ListGatewayRouteTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_route_table_entries_with_options(request, runtime)

    async def list_gateway_route_table_entries_async(
        self,
        request: vpc_20160428_models.ListGatewayRouteTableEntriesRequest,
    ) -> vpc_20160428_models.ListGatewayRouteTableEntriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_gateway_route_table_entries_with_options_async(request, runtime)

    def list_ipsec_servers_with_options(
        self,
        request: vpc_20160428_models.ListIpsecServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListIpsecServersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListIpsecServersResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListIpsecServersResponse(),
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

    def list_ipv_4gateways_with_options(
        self,
        request: vpc_20160428_models.ListIpv4GatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListIpv4GatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListIpv4GatewaysResponse(),
            self.do_rpcrequest('ListIpv4Gateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ipv_4gateways_with_options_async(
        self,
        request: vpc_20160428_models.ListIpv4GatewaysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListIpv4GatewaysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListIpv4GatewaysResponse(),
            await self.do_rpcrequest_async('ListIpv4Gateways', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ipv_4gateways(
        self,
        request: vpc_20160428_models.ListIpv4GatewaysRequest,
    ) -> vpc_20160428_models.ListIpv4GatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ipv_4gateways_with_options(request, runtime)

    async def list_ipv_4gateways_async(
        self,
        request: vpc_20160428_models.ListIpv4GatewaysRequest,
    ) -> vpc_20160428_models.ListIpv4GatewaysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ipv_4gateways_with_options_async(request, runtime)

    def list_nat_gateway_ecs_metric_with_options(
        self,
        request: vpc_20160428_models.ListNatGatewayEcsMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatGatewayEcsMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListNatGatewayEcsMetricResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListNatGatewayEcsMetricResponse(),
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

    def list_nat_ip_cidrs_with_options(
        self,
        request: vpc_20160428_models.ListNatIpCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatIpCidrsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListNatIpCidrsResponse(),
            self.do_rpcrequest('ListNatIpCidrs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nat_ip_cidrs_with_options_async(
        self,
        request: vpc_20160428_models.ListNatIpCidrsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatIpCidrsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListNatIpCidrsResponse(),
            await self.do_rpcrequest_async('ListNatIpCidrs', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nat_ip_cidrs(
        self,
        request: vpc_20160428_models.ListNatIpCidrsRequest,
    ) -> vpc_20160428_models.ListNatIpCidrsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nat_ip_cidrs_with_options(request, runtime)

    async def list_nat_ip_cidrs_async(
        self,
        request: vpc_20160428_models.ListNatIpCidrsRequest,
    ) -> vpc_20160428_models.ListNatIpCidrsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nat_ip_cidrs_with_options_async(request, runtime)

    def list_nat_ips_with_options(
        self,
        request: vpc_20160428_models.ListNatIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListNatIpsResponse(),
            self.do_rpcrequest('ListNatIps', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nat_ips_with_options_async(
        self,
        request: vpc_20160428_models.ListNatIpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListNatIpsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListNatIpsResponse(),
            await self.do_rpcrequest_async('ListNatIps', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nat_ips(
        self,
        request: vpc_20160428_models.ListNatIpsRequest,
    ) -> vpc_20160428_models.ListNatIpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nat_ips_with_options(request, runtime)

    async def list_nat_ips_async(
        self,
        request: vpc_20160428_models.ListNatIpsRequest,
    ) -> vpc_20160428_models.ListNatIpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nat_ips_with_options_async(request, runtime)

    def list_physical_connection_features_with_options(
        self,
        request: vpc_20160428_models.ListPhysicalConnectionFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListPhysicalConnectionFeaturesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListPhysicalConnectionFeaturesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListPhysicalConnectionFeaturesResponse(),
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

    def list_prefix_lists_with_options(
        self,
        request: vpc_20160428_models.ListPrefixListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListPrefixListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListPrefixListsResponse(),
            self.do_rpcrequest('ListPrefixLists', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_prefix_lists_with_options_async(
        self,
        request: vpc_20160428_models.ListPrefixListsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListPrefixListsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListPrefixListsResponse(),
            await self.do_rpcrequest_async('ListPrefixLists', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_prefix_lists(
        self,
        request: vpc_20160428_models.ListPrefixListsRequest,
    ) -> vpc_20160428_models.ListPrefixListsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prefix_lists_with_options(request, runtime)

    async def list_prefix_lists_async(
        self,
        request: vpc_20160428_models.ListPrefixListsRequest,
    ) -> vpc_20160428_models.ListPrefixListsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prefix_lists_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: vpc_20160428_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListTagResourcesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListTagResourcesResponse(),
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

    def list_traffic_mirror_filters_with_options(
        self,
        request: vpc_20160428_models.ListTrafficMirrorFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTrafficMirrorFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListTrafficMirrorFiltersResponse(),
            self.do_rpcrequest('ListTrafficMirrorFilters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_traffic_mirror_filters_with_options_async(
        self,
        request: vpc_20160428_models.ListTrafficMirrorFiltersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTrafficMirrorFiltersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListTrafficMirrorFiltersResponse(),
            await self.do_rpcrequest_async('ListTrafficMirrorFilters', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_traffic_mirror_filters(
        self,
        request: vpc_20160428_models.ListTrafficMirrorFiltersRequest,
    ) -> vpc_20160428_models.ListTrafficMirrorFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_mirror_filters_with_options(request, runtime)

    async def list_traffic_mirror_filters_async(
        self,
        request: vpc_20160428_models.ListTrafficMirrorFiltersRequest,
    ) -> vpc_20160428_models.ListTrafficMirrorFiltersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_traffic_mirror_filters_with_options_async(request, runtime)

    def list_traffic_mirror_sessions_with_options(
        self,
        request: vpc_20160428_models.ListTrafficMirrorSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTrafficMirrorSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListTrafficMirrorSessionsResponse(),
            self.do_rpcrequest('ListTrafficMirrorSessions', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_traffic_mirror_sessions_with_options_async(
        self,
        request: vpc_20160428_models.ListTrafficMirrorSessionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListTrafficMirrorSessionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListTrafficMirrorSessionsResponse(),
            await self.do_rpcrequest_async('ListTrafficMirrorSessions', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_traffic_mirror_sessions(
        self,
        request: vpc_20160428_models.ListTrafficMirrorSessionsRequest,
    ) -> vpc_20160428_models.ListTrafficMirrorSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_traffic_mirror_sessions_with_options(request, runtime)

    async def list_traffic_mirror_sessions_async(
        self,
        request: vpc_20160428_models.ListTrafficMirrorSessionsRequest,
    ) -> vpc_20160428_models.ListTrafficMirrorSessionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_traffic_mirror_sessions_with_options_async(request, runtime)

    def list_virtual_physical_connections_with_options(
        self,
        request: vpc_20160428_models.ListVirtualPhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVirtualPhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVirtualPhysicalConnectionsResponse(),
            self.do_rpcrequest('ListVirtualPhysicalConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_virtual_physical_connections_with_options_async(
        self,
        request: vpc_20160428_models.ListVirtualPhysicalConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVirtualPhysicalConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVirtualPhysicalConnectionsResponse(),
            await self.do_rpcrequest_async('ListVirtualPhysicalConnections', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_virtual_physical_connections(
        self,
        request: vpc_20160428_models.ListVirtualPhysicalConnectionsRequest,
    ) -> vpc_20160428_models.ListVirtualPhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_virtual_physical_connections_with_options(request, runtime)

    async def list_virtual_physical_connections_async(
        self,
        request: vpc_20160428_models.ListVirtualPhysicalConnectionsRequest,
    ) -> vpc_20160428_models.ListVirtualPhysicalConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_virtual_physical_connections_with_options_async(request, runtime)

    def list_vpc_endpoint_services_by_end_user_with_options(
        self,
        request: vpc_20160428_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse(),
            self.do_rpcrequest('ListVpcEndpointServicesByEndUser', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vpc_endpoint_services_by_end_user_with_options_async(
        self,
        request: vpc_20160428_models.ListVpcEndpointServicesByEndUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse(),
            await self.do_rpcrequest_async('ListVpcEndpointServicesByEndUser', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vpc_endpoint_services_by_end_user(
        self,
        request: vpc_20160428_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_endpoint_services_by_end_user_with_options(request, runtime)

    async def list_vpc_endpoint_services_by_end_user_async(
        self,
        request: vpc_20160428_models.ListVpcEndpointServicesByEndUserRequest,
    ) -> vpc_20160428_models.ListVpcEndpointServicesByEndUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_endpoint_services_by_end_user_with_options_async(request, runtime)

    def list_vpc_gateway_endpoints_with_options(
        self,
        request: vpc_20160428_models.ListVpcGatewayEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpcGatewayEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVpcGatewayEndpointsResponse(),
            self.do_rpcrequest('ListVpcGatewayEndpoints', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vpc_gateway_endpoints_with_options_async(
        self,
        request: vpc_20160428_models.ListVpcGatewayEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpcGatewayEndpointsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVpcGatewayEndpointsResponse(),
            await self.do_rpcrequest_async('ListVpcGatewayEndpoints', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vpc_gateway_endpoints(
        self,
        request: vpc_20160428_models.ListVpcGatewayEndpointsRequest,
    ) -> vpc_20160428_models.ListVpcGatewayEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vpc_gateway_endpoints_with_options(request, runtime)

    async def list_vpc_gateway_endpoints_async(
        self,
        request: vpc_20160428_models.ListVpcGatewayEndpointsRequest,
    ) -> vpc_20160428_models.ListVpcGatewayEndpointsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vpc_gateway_endpoints_with_options_async(request, runtime)

    def list_vpn_certificate_associations_with_options(
        self,
        request: vpc_20160428_models.ListVpnCertificateAssociationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ListVpnCertificateAssociationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ListVpnCertificateAssociationsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ListVpnCertificateAssociationsResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyBgpGroupAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyBgpGroupAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyBgpPeerAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyBgpPeerAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageInternetChargeTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCustomerGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyCustomerGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyEipAddressAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyEipAddressAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyFlowLogAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyFlowLogAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyForwardEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyForwardEntryResponse(),
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

    def modify_full_nat_entry_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyFullNatEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyFullNatEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyFullNatEntryAttributeResponse(),
            self.do_rpcrequest('ModifyFullNatEntryAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_full_nat_entry_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyFullNatEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyFullNatEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyFullNatEntryAttributeResponse(),
            await self.do_rpcrequest_async('ModifyFullNatEntryAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_full_nat_entry_attribute(
        self,
        request: vpc_20160428_models.ModifyFullNatEntryAttributeRequest,
    ) -> vpc_20160428_models.ModifyFullNatEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_full_nat_entry_attribute_with_options(request, runtime)

    async def modify_full_nat_entry_attribute_async(
        self,
        request: vpc_20160428_models.ModifyFullNatEntryAttributeRequest,
    ) -> vpc_20160428_models.ModifyFullNatEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_full_nat_entry_attribute_with_options_async(request, runtime)

    def modify_global_acceleration_instance_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyHaVipAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyHaVipAttributeResponse(),
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

    def modify_ipv_6translator_acl_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyIPv6TranslatorAclAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIPv6TranslatorEntryResponse(),
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

    def modify_instance_auto_renewal_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyInstanceAutoRenewalAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6AddressAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6AddressAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6GatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6GatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6GatewaySpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6GatewaySpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6InternetBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyIpv6InternetBandwidthResponse(),
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

    def modify_nat_gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyNatGatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatGatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatGatewaySpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatGatewaySpecResponse(),
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

    def modify_nat_ip_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyNatIpAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatIpAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatIpAttributeResponse(),
            self.do_rpcrequest('ModifyNatIpAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_nat_ip_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyNatIpAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatIpAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatIpAttributeResponse(),
            await self.do_rpcrequest_async('ModifyNatIpAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nat_ip_attribute(
        self,
        request: vpc_20160428_models.ModifyNatIpAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatIpAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_ip_attribute_with_options(request, runtime)

    async def modify_nat_ip_attribute_async(
        self,
        request: vpc_20160428_models.ModifyNatIpAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatIpAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_ip_attribute_with_options_async(request, runtime)

    def modify_nat_ip_cidr_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyNatIpCidrAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatIpCidrAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatIpCidrAttributeResponse(),
            self.do_rpcrequest('ModifyNatIpCidrAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_nat_ip_cidr_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyNatIpCidrAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNatIpCidrAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNatIpCidrAttributeResponse(),
            await self.do_rpcrequest_async('ModifyNatIpCidrAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_nat_ip_cidr_attribute(
        self,
        request: vpc_20160428_models.ModifyNatIpCidrAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatIpCidrAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_nat_ip_cidr_attribute_with_options(request, runtime)

    async def modify_nat_ip_cidr_attribute_async(
        self,
        request: vpc_20160428_models.ModifyNatIpCidrAttributeRequest,
    ) -> vpc_20160428_models.ModifyNatIpCidrAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_nat_ip_cidr_attribute_with_options_async(request, runtime)

    def modify_network_acl_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyNetworkAclAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyNetworkAclAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNetworkAclAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyNetworkAclAttributesResponse(),
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

    def modify_physical_connection_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse(),
            self.do_rpcrequest('ModifyPhysicalConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_physical_connection_attribute_with_options_async(
        self,
        request: vpc_20160428_models.ModifyPhysicalConnectionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse(),
            await self.do_rpcrequest_async('ModifyPhysicalConnectionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_physical_connection_attribute(
        self,
        request: vpc_20160428_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    async def modify_physical_connection_attribute_async(
        self,
        request: vpc_20160428_models.ModifyPhysicalConnectionAttributeRequest,
    ) -> vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_physical_connection_attribute_with_options_async(request, runtime)

    def modify_route_entry_with_options(
        self,
        request: vpc_20160428_models.ModifyRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouteEntryResponse(),
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

    def modify_route_table_attributes_with_options(
        self,
        request: vpc_20160428_models.ModifyRouteTableAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouteTableAttributesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouteTableAttributesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouteTableAttributesResponse(),
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

    def modify_router_interface_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyRouterInterfaceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyRouterInterfaceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouterInterfaceAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouterInterfaceAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouterInterfaceSpecResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyRouterInterfaceSpecResponse(),
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

    def modify_snat_entry_with_options(
        self,
        request: vpc_20160428_models.ModifySnatEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifySnatEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifySnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifySnatEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifySslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifySslVpnClientCertResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifySslVpnServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifySslVpnServerResponse(),
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

    def modify_vrouter_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVRouterAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVRouterAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVSwitchAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVSwitchAttributeResponse(),
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

    def modify_virtual_border_router_attribute_with_options(
        self,
        request: vpc_20160428_models.ModifyVirtualBorderRouterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpcAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpcAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnConnectionAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnConnectionAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnGatewayAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnRouteEntryWeightResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ModifyVpnRouteEntryWeightResponse(),
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

    def move_resource_group_with_options(
        self,
        request: vpc_20160428_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.MoveResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.MoveResourceGroupResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.MoveResourceGroupResponse(),
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

    def open_physical_connection_service_with_options(
        self,
        request: vpc_20160428_models.OpenPhysicalConnectionServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.OpenPhysicalConnectionServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.OpenPhysicalConnectionServiceResponse(),
            self.do_rpcrequest('OpenPhysicalConnectionService', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_physical_connection_service_with_options_async(
        self,
        request: vpc_20160428_models.OpenPhysicalConnectionServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.OpenPhysicalConnectionServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.OpenPhysicalConnectionServiceResponse(),
            await self.do_rpcrequest_async('OpenPhysicalConnectionService', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_physical_connection_service(
        self,
        request: vpc_20160428_models.OpenPhysicalConnectionServiceRequest,
    ) -> vpc_20160428_models.OpenPhysicalConnectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_physical_connection_service_with_options(request, runtime)

    async def open_physical_connection_service_async(
        self,
        request: vpc_20160428_models.OpenPhysicalConnectionServiceRequest,
    ) -> vpc_20160428_models.OpenPhysicalConnectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_physical_connection_service_with_options_async(request, runtime)

    def open_traffic_mirror_service_with_options(
        self,
        request: vpc_20160428_models.OpenTrafficMirrorServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.OpenTrafficMirrorServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.OpenTrafficMirrorServiceResponse(),
            self.do_rpcrequest('OpenTrafficMirrorService', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_traffic_mirror_service_with_options_async(
        self,
        request: vpc_20160428_models.OpenTrafficMirrorServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.OpenTrafficMirrorServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.OpenTrafficMirrorServiceResponse(),
            await self.do_rpcrequest_async('OpenTrafficMirrorService', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_traffic_mirror_service(
        self,
        request: vpc_20160428_models.OpenTrafficMirrorServiceRequest,
    ) -> vpc_20160428_models.OpenTrafficMirrorServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_traffic_mirror_service_with_options(request, runtime)

    async def open_traffic_mirror_service_async(
        self,
        request: vpc_20160428_models.OpenTrafficMirrorServiceRequest,
    ) -> vpc_20160428_models.OpenTrafficMirrorServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_traffic_mirror_service_with_options_async(request, runtime)

    def publish_vpn_route_entry_with_options(
        self,
        request: vpc_20160428_models.PublishVpnRouteEntryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.PublishVpnRouteEntryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.PublishVpnRouteEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.PublishVpnRouteEntryResponse(),
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

    def recover_physical_connection_with_options(
        self,
        request: vpc_20160428_models.RecoverPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RecoverPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RecoverPhysicalConnectionResponse(),
            self.do_rpcrequest('RecoverPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def recover_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.RecoverPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RecoverPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RecoverPhysicalConnectionResponse(),
            await self.do_rpcrequest_async('RecoverPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def recover_physical_connection(
        self,
        request: vpc_20160428_models.RecoverPhysicalConnectionRequest,
    ) -> vpc_20160428_models.RecoverPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.recover_physical_connection_with_options(request, runtime)

    async def recover_physical_connection_async(
        self,
        request: vpc_20160428_models.RecoverPhysicalConnectionRequest,
    ) -> vpc_20160428_models.RecoverPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.recover_physical_connection_with_options_async(request, runtime)

    def recover_virtual_border_router_with_options(
        self,
        request: vpc_20160428_models.RecoverVirtualBorderRouterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RecoverVirtualBorderRouterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RecoverVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RecoverVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReleaseEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReleaseEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReleaseEipSegmentAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReleaseEipSegmentAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse(),
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

    def remove_sources_from_traffic_mirror_session_with_options(
        self,
        request: vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse(),
            self.do_rpcrequest('RemoveSourcesFromTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_sources_from_traffic_mirror_session_with_options_async(
        self,
        request: vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse(),
            await self.do_rpcrequest_async('RemoveSourcesFromTrafficMirrorSession', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_sources_from_traffic_mirror_session(
        self,
        request: vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_sources_from_traffic_mirror_session_with_options(request, runtime)

    async def remove_sources_from_traffic_mirror_session_async(
        self,
        request: vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionRequest,
    ) -> vpc_20160428_models.RemoveSourcesFromTrafficMirrorSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_sources_from_traffic_mirror_session_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: vpc_20160428_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.RenewInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RenewInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RevokeInstanceFromCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.RevokeInstanceFromCenResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TagResourcesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TagResourcesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TerminatePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TerminatePhysicalConnectionResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TerminateVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.TerminateVirtualBorderRouterResponse(),
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

    def un_tag_resources_with_options(
        self,
        request: vpc_20160428_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UnTagResourcesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnTagResourcesResponse(),
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

    def unassociate_eip_address_with_options(
        self,
        request: vpc_20160428_models.UnassociateEipAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UnassociateEipAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateEipAddressResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateHaVipResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateNetworkAclResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateRouteTableResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateRouteTableResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateVpcCidrBlockResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UnassociateVpcCidrBlockResponse(),
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

    def update_cross_boarder_status_with_options(
        self,
        request: vpc_20160428_models.UpdateCrossBoarderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateCrossBoarderStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateCrossBoarderStatusResponse(),
            self.do_rpcrequest('UpdateCrossBoarderStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cross_boarder_status_with_options_async(
        self,
        request: vpc_20160428_models.UpdateCrossBoarderStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateCrossBoarderStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateCrossBoarderStatusResponse(),
            await self.do_rpcrequest_async('UpdateCrossBoarderStatus', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cross_boarder_status(
        self,
        request: vpc_20160428_models.UpdateCrossBoarderStatusRequest,
    ) -> vpc_20160428_models.UpdateCrossBoarderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cross_boarder_status_with_options(request, runtime)

    async def update_cross_boarder_status_async(
        self,
        request: vpc_20160428_models.UpdateCrossBoarderStatusRequest,
    ) -> vpc_20160428_models.UpdateCrossBoarderStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cross_boarder_status_with_options_async(request, runtime)

    def update_dhcp_options_set_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateDhcpOptionsSetAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse(),
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

    def update_gateway_route_table_entry_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse(),
            self.do_rpcrequest('UpdateGatewayRouteTableEntryAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gateway_route_table_entry_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse(),
            await self.do_rpcrequest_async('UpdateGatewayRouteTableEntryAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_gateway_route_table_entry_attribute(
        self,
        request: vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeRequest,
    ) -> vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_table_entry_attribute_with_options(request, runtime)

    async def update_gateway_route_table_entry_attribute_async(
        self,
        request: vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeRequest,
    ) -> vpc_20160428_models.UpdateGatewayRouteTableEntryAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_route_table_entry_attribute_with_options_async(request, runtime)

    def update_ipsec_server_with_options(
        self,
        request: vpc_20160428_models.UpdateIpsecServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateIpsecServerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateIpsecServerResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateIpsecServerResponse(),
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

    def update_ipv_4gateway_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateIpv4GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateIpv4GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateIpv4GatewayAttributeResponse(),
            self.do_rpcrequest('UpdateIpv4GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_ipv_4gateway_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateIpv4GatewayAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateIpv4GatewayAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateIpv4GatewayAttributeResponse(),
            await self.do_rpcrequest_async('UpdateIpv4GatewayAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_ipv_4gateway_attribute(
        self,
        request: vpc_20160428_models.UpdateIpv4GatewayAttributeRequest,
    ) -> vpc_20160428_models.UpdateIpv4GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ipv_4gateway_attribute_with_options(request, runtime)

    async def update_ipv_4gateway_attribute_async(
        self,
        request: vpc_20160428_models.UpdateIpv4GatewayAttributeRequest,
    ) -> vpc_20160428_models.UpdateIpv4GatewayAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ipv_4gateway_attribute_with_options_async(request, runtime)

    def update_nat_gateway_nat_type_with_options(
        self,
        request: vpc_20160428_models.UpdateNatGatewayNatTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateNatGatewayNatTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateNatGatewayNatTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateNatGatewayNatTypeResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateNetworkAclEntriesResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateNetworkAclEntriesResponse(),
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

    def update_traffic_mirror_filter_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse(),
            self.do_rpcrequest('UpdateTrafficMirrorFilterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_traffic_mirror_filter_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse(),
            await self.do_rpcrequest_async('UpdateTrafficMirrorFilterAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_traffic_mirror_filter_attribute(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_traffic_mirror_filter_attribute_with_options(request, runtime)

    async def update_traffic_mirror_filter_attribute_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_traffic_mirror_filter_attribute_with_options_async(request, runtime)

    def update_traffic_mirror_filter_rule_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse(),
            self.do_rpcrequest('UpdateTrafficMirrorFilterRuleAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_traffic_mirror_filter_rule_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse(),
            await self.do_rpcrequest_async('UpdateTrafficMirrorFilterRuleAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_traffic_mirror_filter_rule_attribute(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_traffic_mirror_filter_rule_attribute_with_options(request, runtime)

    async def update_traffic_mirror_filter_rule_attribute_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorFilterRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_traffic_mirror_filter_rule_attribute_with_options_async(request, runtime)

    def update_traffic_mirror_session_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorSessionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse(),
            self.do_rpcrequest('UpdateTrafficMirrorSessionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_traffic_mirror_session_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorSessionAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse(),
            await self.do_rpcrequest_async('UpdateTrafficMirrorSessionAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_traffic_mirror_session_attribute(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorSessionAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_traffic_mirror_session_attribute_with_options(request, runtime)

    async def update_traffic_mirror_session_attribute_async(
        self,
        request: vpc_20160428_models.UpdateTrafficMirrorSessionAttributeRequest,
    ) -> vpc_20160428_models.UpdateTrafficMirrorSessionAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_traffic_mirror_session_attribute_with_options_async(request, runtime)

    def update_virtual_border_bandwidth_with_options(
        self,
        request: vpc_20160428_models.UpdateVirtualBorderBandwidthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVirtualBorderBandwidthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVirtualBorderBandwidthResponse(),
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
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVirtualBorderBandwidthResponse(),
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

    def update_virtual_physical_connection_with_options(
        self,
        request: vpc_20160428_models.UpdateVirtualPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse(),
            self.do_rpcrequest('UpdateVirtualPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_virtual_physical_connection_with_options_async(
        self,
        request: vpc_20160428_models.UpdateVirtualPhysicalConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse(),
            await self.do_rpcrequest_async('UpdateVirtualPhysicalConnection', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_virtual_physical_connection(
        self,
        request: vpc_20160428_models.UpdateVirtualPhysicalConnectionRequest,
    ) -> vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_virtual_physical_connection_with_options(request, runtime)

    async def update_virtual_physical_connection_async(
        self,
        request: vpc_20160428_models.UpdateVirtualPhysicalConnectionRequest,
    ) -> vpc_20160428_models.UpdateVirtualPhysicalConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_virtual_physical_connection_with_options_async(request, runtime)

    def update_vpc_gateway_endpoint_attribute_with_options(
        self,
        request: vpc_20160428_models.UpdateVpcGatewayEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse(),
            self.do_rpcrequest('UpdateVpcGatewayEndpointAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_vpc_gateway_endpoint_attribute_with_options_async(
        self,
        request: vpc_20160428_models.UpdateVpcGatewayEndpointAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse(),
            await self.do_rpcrequest_async('UpdateVpcGatewayEndpointAttribute', '2016-04-28', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vpc_gateway_endpoint_attribute(
        self,
        request: vpc_20160428_models.UpdateVpcGatewayEndpointAttributeRequest,
    ) -> vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_vpc_gateway_endpoint_attribute_with_options(request, runtime)

    async def update_vpc_gateway_endpoint_attribute_async(
        self,
        request: vpc_20160428_models.UpdateVpcGatewayEndpointAttributeRequest,
    ) -> vpc_20160428_models.UpdateVpcGatewayEndpointAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_vpc_gateway_endpoint_attribute_with_options_async(request, runtime)
