# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-qingdao": "vpc.aliyuncs.com",
            "cn-beijing": "vpc.aliyuncs.com",
            "cn-hangzhou": "vpc.aliyuncs.com",
            "cn-shanghai": "vpc.aliyuncs.com",
            "cn-shenzhen": "vpc.aliyuncs.com",
            "cn-hongkong": "vpc.aliyuncs.com",
            "ap-southeast-1": "vpc.aliyuncs.com",
            "us-west-1": "vpc.aliyuncs.com",
            "us-east-1": "vpc.aliyuncs.com",
            "cn-shanghai-finance-1": "vpc.aliyuncs.com",
            "cn-shenzhen-finance-1": "vpc.aliyuncs.com",
            "cn-north-2-gov-1": "vpc.aliyuncs.com",
            "ap-northeast-2-pop": "vpc.aliyuncs.com",
            "cn-beijing-finance-1": "vpc.aliyuncs.com",
            "cn-beijing-finance-pop": "vpc.aliyuncs.com",
            "cn-beijing-gov-1": "vpc.aliyuncs.com",
            "cn-beijing-nu16-b01": "vpc.aliyuncs.com",
            "cn-edge-1": "vpc-nebula.cn-qingdao-nebula.aliyuncs.com",
            "cn-fujian": "vpc.aliyuncs.com",
            "cn-haidian-cm12-c01": "vpc.aliyuncs.com",
            "cn-hangzhou-bj-b01": "vpc.aliyuncs.com",
            "cn-hangzhou-finance": "vpc.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "vpc.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "vpc.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "vpc.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "vpc.aliyuncs.com",
            "cn-hangzhou-test-306": "vpc.aliyuncs.com",
            "cn-hongkong-finance-pop": "vpc.aliyuncs.com",
            "cn-qingdao-nebula": "vpc-nebula.cn-qingdao-nebula.aliyuncs.com",
            "cn-shanghai-et15-b01": "vpc.aliyuncs.com",
            "cn-shanghai-et2-b01": "vpc.aliyuncs.com",
            "cn-shanghai-inner": "vpc.aliyuncs.com",
            "cn-shanghai-internal-test-1": "vpc.aliyuncs.com",
            "cn-shenzhen-inner": "vpc.aliyuncs.com",
            "cn-shenzhen-st4-d01": "vpc.aliyuncs.com",
            "cn-shenzhen-su18-b01": "vpc.aliyuncs.com",
            "cn-wuhan": "vpc.aliyuncs.com",
            "cn-yushanfang": "vpc.aliyuncs.com",
            "cn-zhangbei-na61-b01": "vpc.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "vpc.cn-zhangjiakou.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "vpc-nebula.cn-qingdao-nebula.aliyuncs.com",
            "eu-west-1-oxs": "vpc-nebula.cn-shenzhen-cloudstone.aliyuncs.com",
            "rus-west-1-pop": "vpc.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("vpc", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def list_physical_connection_features_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ListPhysicalConnectionFeaturesResponse().from_map(self.do_request("ListPhysicalConnectionFeatures", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def list_physical_connection_features(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_physical_connection_features_with_options(request, runtime)

    def list_nat_gateway_ecs_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ListNatGatewayEcsMetricResponse().from_map(self.do_request("ListNatGatewayEcsMetric", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def list_nat_gateway_ecs_metric(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_nat_gateway_ecs_metric_with_options(request, runtime)

    def disable_nat_gateway_ecs_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DisableNatGatewayEcsMetricResponse().from_map(self.do_request("DisableNatGatewayEcsMetric", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def disable_nat_gateway_ecs_metric(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.disable_nat_gateway_ecs_metric_with_options(request, runtime)

    def enable_nat_gateway_ecs_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.EnableNatGatewayEcsMetricResponse().from_map(self.do_request("EnableNatGatewayEcsMetric", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def enable_nat_gateway_ecs_metric(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_nat_gateway_ecs_metric_with_options(request, runtime)

    def create_dhcp_options_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateDhcpOptionsSetResponse().from_map(self.do_request("CreateDhcpOptionsSet", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_dhcp_options_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_dhcp_options_set_with_options(request, runtime)

    def replace_vpc_dhcp_options_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ReplaceVpcDhcpOptionsSetResponse().from_map(self.do_request("ReplaceVpcDhcpOptionsSet", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def replace_vpc_dhcp_options_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.replace_vpc_dhcp_options_set_with_options(request, runtime)

    def update_dhcp_options_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UpdateDhcpOptionsSetAttributeResponse().from_map(self.do_request("UpdateDhcpOptionsSetAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def update_dhcp_options_set_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.update_dhcp_options_set_attribute_with_options(request, runtime)

    def get_dhcp_options_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.GetDhcpOptionsSetResponse().from_map(self.do_request("GetDhcpOptionsSet", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def get_dhcp_options_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_dhcp_options_set_with_options(request, runtime)

    def list_dhcp_options_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ListDhcpOptionsSetsResponse().from_map(self.do_request("ListDhcpOptionsSets", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def list_dhcp_options_sets(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_dhcp_options_sets_with_options(request, runtime)

    def detach_dhcp_options_set_from_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DetachDhcpOptionsSetFromVpcResponse().from_map(self.do_request("DetachDhcpOptionsSetFromVpc", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def detach_dhcp_options_set_from_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_dhcp_options_set_from_vpc_with_options(request, runtime)

    def attach_dhcp_options_set_to_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AttachDhcpOptionsSetToVpcResponse().from_map(self.do_request("AttachDhcpOptionsSetToVpc", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def attach_dhcp_options_set_to_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_dhcp_options_set_to_vpc_with_options(request, runtime)

    def delete_dhcp_options_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteDhcpOptionsSetResponse().from_map(self.do_request("DeleteDhcpOptionsSet", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_dhcp_options_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_dhcp_options_set_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RenewInstanceResponse().from_map(self.do_request("RenewInstance", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.renew_instance_with_options(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeInstanceAutoRenewAttributeResponse().from_map(self.do_request("DescribeInstanceAutoRenewAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(self.do_request("ModifyInstanceAutoRenewalAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def release_eip_segment_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ReleaseEipSegmentAddressResponse().from_map(self.do_request("ReleaseEipSegmentAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def release_eip_segment_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.release_eip_segment_address_with_options(request, runtime)

    def describe_eip_segment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeEipSegmentResponse().from_map(self.do_request("DescribeEipSegment", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_eip_segment(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_segment_with_options(request, runtime)

    def allocate_eip_segment_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AllocateEipSegmentAddressResponse().from_map(self.do_request("AllocateEipSegmentAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def allocate_eip_segment_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_eip_segment_address_with_options(request, runtime)

    def unassociate_vpc_cidr_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateVpcCidrBlockResponse().from_map(self.do_request("UnassociateVpcCidrBlock", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_vpc_cidr_block(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_vpc_cidr_block_with_options(request, runtime)

    def associate_vpc_cidr_block_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateVpcCidrBlockResponse().from_map(self.do_request("AssociateVpcCidrBlock", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_vpc_cidr_block(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_vpc_cidr_block_with_options(request, runtime)

    def describe_router_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRouterInterfaceAttributeResponse().from_map(self.do_request("DescribeRouterInterfaceAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_router_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_router_interface_attribute_with_options(request, runtime)

    def delete_express_cloud_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteExpressCloudConnectionResponse().from_map(self.do_request("DeleteExpressCloudConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_express_cloud_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_express_cloud_connection_with_options(request, runtime)

    def cancel_express_cloud_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CancelExpressCloudConnectionResponse().from_map(self.do_request("CancelExpressCloudConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def cancel_express_cloud_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_express_cloud_connection_with_options(request, runtime)

    def deletion_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeletionProtectionResponse().from_map(self.do_request("DeletionProtection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def deletion_protection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.deletion_protection_with_options(request, runtime)

    def describe_eip_gateway_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeEipGatewayInfoResponse().from_map(self.do_request("DescribeEipGatewayInfo", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_eip_gateway_info(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_gateway_info_with_options(request, runtime)

    def modify_bgp_peer_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyBgpPeerAttributeResponse().from_map(self.do_request("ModifyBgpPeerAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_bgp_peer_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_bgp_peer_attribute_with_options(request, runtime)

    def describe_vpn_ssl_server_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnSslServerLogsResponse().from_map(self.do_request("DescribeVpnSslServerLogs", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_ssl_server_logs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_ssl_server_logs_with_options(request, runtime)

    def modify_express_cloud_connection_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyExpressCloudConnectionBandwidthResponse().from_map(self.do_request("ModifyExpressCloudConnectionBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_express_cloud_connection_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_express_cloud_connection_bandwidth_with_options(request, runtime)

    def modify_express_cloud_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyExpressCloudConnectionAttributeResponse().from_map(self.do_request("ModifyExpressCloudConnectionAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_express_cloud_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_express_cloud_connection_attribute_with_options(request, runtime)

    def describe_express_cloud_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeExpressCloudConnectionsResponse().from_map(self.do_request("DescribeExpressCloudConnections", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_express_cloud_connections(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_express_cloud_connections_with_options(request, runtime)

    def create_express_cloud_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateExpressCloudConnectionResponse().from_map(self.do_request("CreateExpressCloudConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_express_cloud_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_express_cloud_connection_with_options(request, runtime)

    def update_network_acl_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UpdateNetworkAclEntriesResponse().from_map(self.do_request("UpdateNetworkAclEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def update_network_acl_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.update_network_acl_entries_with_options(request, runtime)

    def unassociate_network_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateNetworkAclResponse().from_map(self.do_request("UnassociateNetworkAcl", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_network_acl(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_network_acl_with_options(request, runtime)

    def modify_network_acl_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyNetworkAclAttributesResponse().from_map(self.do_request("ModifyNetworkAclAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_network_acl_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_network_acl_attributes_with_options(request, runtime)

    def describe_network_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeNetworkAclsResponse().from_map(self.do_request("DescribeNetworkAcls", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_network_acls(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_network_acls_with_options(request, runtime)

    def describe_network_acl_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeNetworkAclAttributesResponse().from_map(self.do_request("DescribeNetworkAclAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_network_acl_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_network_acl_attributes_with_options(request, runtime)

    def delete_network_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteNetworkAclResponse().from_map(self.do_request("DeleteNetworkAcl", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_network_acl(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_network_acl_with_options(request, runtime)

    def create_network_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateNetworkAclResponse().from_map(self.do_request("CreateNetworkAcl", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_network_acl(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_network_acl_with_options(request, runtime)

    def copy_network_acl_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CopyNetworkAclEntriesResponse().from_map(self.do_request("CopyNetworkAclEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def copy_network_acl_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.copy_network_acl_entries_with_options(request, runtime)

    def associate_network_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateNetworkAclResponse().from_map(self.do_request("AssociateNetworkAcl", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_network_acl(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_network_acl_with_options(request, runtime)

    def modify_common_bandwidth_package_ip_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyCommonBandwidthPackageIpBandwidthResponse().from_map(self.do_request("ModifyCommonBandwidthPackageIpBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_common_bandwidth_package_ip_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_common_bandwidth_package_ip_bandwidth_with_options(request, runtime)

    def cancel_common_bandwidth_package_ip_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CancelCommonBandwidthPackageIpBandwidthResponse().from_map(self.do_request("CancelCommonBandwidthPackageIpBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def cancel_common_bandwidth_package_ip_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_common_bandwidth_package_ip_bandwidth_with_options(request, runtime)

    def create_vpn_pbr_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVpnPbrRouteEntryResponse().from_map(self.do_request("CreateVpnPbrRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vpn_pbr_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpn_pbr_route_entry_with_options(request, runtime)

    def create_vpn_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVpnRouteEntryResponse().from_map(self.do_request("CreateVpnRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vpn_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpn_route_entry_with_options(request, runtime)

    def delete_vpn_pbr_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVpnPbrRouteEntryResponse().from_map(self.do_request("DeleteVpnPbrRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vpn_pbr_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpn_pbr_route_entry_with_options(request, runtime)

    def delete_vpn_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVpnRouteEntryResponse().from_map(self.do_request("DeleteVpnRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vpn_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpn_route_entry_with_options(request, runtime)

    def describe_vpn_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnRouteEntriesResponse().from_map(self.do_request("DescribeVpnRouteEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_route_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_route_entries_with_options(request, runtime)

    def describe_vpn_pbr_route_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnPbrRouteEntriesResponse().from_map(self.do_request("DescribeVpnPbrRouteEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_pbr_route_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_pbr_route_entries_with_options(request, runtime)

    def publish_vpn_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.PublishVpnRouteEntryResponse().from_map(self.do_request("PublishVpnRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def publish_vpn_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.publish_vpn_route_entry_with_options(request, runtime)

    def modify_vpn_route_entry_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVpnRouteEntryWeightResponse().from_map(self.do_request("ModifyVpnRouteEntryWeight", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vpn_route_entry_weight(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpn_route_entry_weight_with_options(request, runtime)

    def modify_vpn_pbr_route_entry_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVpnPbrRouteEntryWeightResponse().from_map(self.do_request("ModifyVpnPbrRouteEntryWeight", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vpn_pbr_route_entry_weight(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpn_pbr_route_entry_weight_with_options(request, runtime)

    def describe_physical_connection_loawith_options(self, request, runtime):
        """
        DescribePhysicalConnectionLOA Query LOA information about the physical connection.
        request demo:   * http(s)://[Endpoint]/?InstanceId=pc-bp1ca4wca27exxxxxxxx
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribePhysicalConnectionLOAResponse().from_map(self.do_request("DescribePhysicalConnectionLOA", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_physical_connection_loa(self, request):
        """
        DescribePhysicalConnectionLOA Query LOA information about the physical connection.
        request demo:   * http(s)://[Endpoint]/?InstanceId=pc-bp1ca4wca27exxxxxxxx
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_physical_connection_loawith_options(request, runtime)

    def create_physical_connection_setup_order_with_options(self, request, runtime):
        """
        CreatePhysicalConnectionSetupOrder Create an order for the resource fee.
        request demo:   * http(s)://[Endpoint]/?AccessPointId=ap-cn-beijing-ft-A
        &LineOperator=CT
        &RegionId=cn-shanghai
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreatePhysicalConnectionSetupOrderResponse().from_map(self.do_request("CreatePhysicalConnectionSetupOrder", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_physical_connection_setup_order(self, request):
        """
        CreatePhysicalConnectionSetupOrder Create an order for the resource fee.
        request demo:   * http(s)://[Endpoint]/?AccessPointId=ap-cn-beijing-ft-A
        &LineOperator=CT
        &RegionId=cn-shanghai
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.create_physical_connection_setup_order_with_options(request, runtime)

    def create_physical_connection_occupancy_order_with_options(self, request, runtime):
        """
        CreatePhysicalConnectionOccupancyOrder Create an order for the initial installation fee.
        request demo:   * http(s)://[Endpoint]/?PhysicalConnectionId=pc-bp1hp0wr072f6ambni141
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreatePhysicalConnectionOccupancyOrderResponse().from_map(self.do_request("CreatePhysicalConnectionOccupancyOrder", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_physical_connection_occupancy_order(self, request):
        """
        CreatePhysicalConnectionOccupancyOrder Create an order for the initial installation fee.
        request demo:   * http(s)://[Endpoint]/?PhysicalConnectionId=pc-bp1hp0wr072f6ambni141
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.create_physical_connection_occupancy_order_with_options(request, runtime)

    def complete_physical_connection_loawith_options(self, request, runtime):
        """
        CompletePhysicalConnectionLOA Report information about the completed installation of the leased line.
        request demo:   * http(s)://[Endpoint]/?InstanceId=pc-bp10tvlhnwkwxxxxxxxxxx
        &LineCode=aaa111
        &LineLabel=bbb222
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.CompletePhysicalConnectionLOAResponse().from_map(self.do_request("CompletePhysicalConnectionLOA", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def complete_physical_connection_loa(self, request):
        """
        CompletePhysicalConnectionLOA Report information about the completed installation of the leased line.
        request demo:   * http(s)://[Endpoint]/?InstanceId=pc-bp10tvlhnwkwxxxxxxxxxx
        &LineCode=aaa111
        &LineLabel=bbb222
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.complete_physical_connection_loawith_options(request, runtime)

    def apply_physical_connection_loawith_options(self, request, runtime):
        """
        ApplyPhysicalConnectionLOA Apply for the LOA.
        request demo:   * http(s)://[Endpoint]/?CompanyName=company
        &ConstructionTime=2019-02-28T16:00:00.000Z
        &InstanceId=pc-bp1qrb3044eqixxxxxxxx
        &LineType=SDH
        &PeerLocation=Hangzhou
        &RegionId=cn-hangzhou
        &Si=Alibaba Cloud
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.ApplyPhysicalConnectionLOAResponse().from_map(self.do_request("ApplyPhysicalConnectionLOA", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def apply_physical_connection_loa(self, request):
        """
        ApplyPhysicalConnectionLOA Apply for the LOA.
        request demo:   * http(s)://[Endpoint]/?CompanyName=company
        &ConstructionTime=2019-02-28T16:00:00.000Z
        &InstanceId=pc-bp1qrb3044eqixxxxxxxx
        &LineType=SDH
        &PeerLocation=Hangzhou
        &RegionId=cn-hangzhou
        &Si=Alibaba Cloud
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.apply_physical_connection_loawith_options(request, runtime)

    def convert_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ConvertBandwidthPackageResponse().from_map(self.do_request("ConvertBandwidthPackage", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def convert_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.convert_bandwidth_package_with_options(request, runtime)

    def modify_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyRouteEntryResponse().from_map(self.do_request("ModifyRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_route_entry_with_options(request, runtime)

    def describe_route_entry_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRouteEntryListResponse().from_map(self.do_request("DescribeRouteEntryList", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_route_entry_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_route_entry_list_with_options(request, runtime)

    def create_ipv_6translator_acl_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateIPv6TranslatorAclListResponse().from_map(self.do_request("CreateIPv6TranslatorAclList", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ipv_6translator_acl_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ipv_6translator_acl_list_with_options(request, runtime)

    def delete_ipv_6translator_acl_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIPv6TranslatorAclListResponse().from_map(self.do_request("DeleteIPv6TranslatorAclList", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6translator_acl_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6translator_acl_list_with_options(request, runtime)

    def add_ipv_6translator_acl_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AddIPv6TranslatorAclListEntryResponse().from_map(self.do_request("AddIPv6TranslatorAclListEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def add_ipv_6translator_acl_list_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_ipv_6translator_acl_list_entry_with_options(request, runtime)

    def describe_ipv_6translator_acl_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIPv6TranslatorAclListsResponse().from_map(self.do_request("DescribeIPv6TranslatorAclLists", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6translator_acl_lists(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6translator_acl_lists_with_options(request, runtime)

    def modify_ipv_6translator_acl_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIPv6TranslatorAclAttributeResponse().from_map(self.do_request("ModifyIPv6TranslatorAclAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6translator_acl_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6translator_acl_attribute_with_options(request, runtime)

    def remove_ipv_6translator_acl_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RemoveIPv6TranslatorAclListEntryResponse().from_map(self.do_request("RemoveIPv6TranslatorAclListEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def remove_ipv_6translator_acl_list_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_ipv_6translator_acl_list_entry_with_options(request, runtime)

    def describe_ipv_6translator_acl_list_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIPv6TranslatorAclListAttributesResponse().from_map(self.do_request("DescribeIPv6TranslatorAclListAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6translator_acl_list_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6translator_acl_list_attributes_with_options(request, runtime)

    def modify_ipv_6translator_acl_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIPv6TranslatorAclListEntryResponse().from_map(self.do_request("ModifyIPv6TranslatorAclListEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6translator_acl_list_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6translator_acl_list_entry_with_options(request, runtime)

    def un_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnTagResourcesResponse().from_map(self.do_request("UnTagResources", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def un_tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.un_tag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.TagResourcesResponse().from_map(self.do_request("TagResources", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.tag_resources_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ListTagResourcesResponse().from_map(self.do_request("ListTagResources", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_tag_resources_with_options(request, runtime)

    def modify_ipv_6internet_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIpv6InternetBandwidthResponse().from_map(self.do_request("ModifyIpv6InternetBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6internet_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6internet_bandwidth_with_options(request, runtime)

    def modify_ipv_6gateway_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIpv6GatewaySpecResponse().from_map(self.do_request("ModifyIpv6GatewaySpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6gateway_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6gateway_spec_with_options(request, runtime)

    def modify_ipv_6gateway_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIpv6GatewayAttributeResponse().from_map(self.do_request("ModifyIpv6GatewayAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6gateway_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6gateway_attribute_with_options(request, runtime)

    def modify_ipv_6address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIpv6AddressAttributeResponse().from_map(self.do_request("ModifyIpv6AddressAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6address_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6address_attribute_with_options(request, runtime)

    def describe_ipv_6gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIpv6GatewaysResponse().from_map(self.do_request("DescribeIpv6Gateways", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6gateways(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6gateways_with_options(request, runtime)

    def describe_ipv_6gateway_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIpv6GatewayAttributeResponse().from_map(self.do_request("DescribeIpv6GatewayAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6gateway_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6gateway_attribute_with_options(request, runtime)

    def describe_ipv_6egress_only_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIpv6EgressOnlyRulesResponse().from_map(self.do_request("DescribeIpv6EgressOnlyRules", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6egress_only_rules(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6egress_only_rules_with_options(request, runtime)

    def describe_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIpv6AddressesResponse().from_map(self.do_request("DescribeIpv6Addresses", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6addresses_with_options(request, runtime)

    def delete_ipv_6internet_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIpv6InternetBandwidthResponse().from_map(self.do_request("DeleteIpv6InternetBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6internet_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6internet_bandwidth_with_options(request, runtime)

    def delete_ipv_6gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIpv6GatewayResponse().from_map(self.do_request("DeleteIpv6Gateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6gateway_with_options(request, runtime)

    def delete_ipv_6egress_only_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIpv6EgressOnlyRuleResponse().from_map(self.do_request("DeleteIpv6EgressOnlyRule", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6egress_only_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6egress_only_rule_with_options(request, runtime)

    def create_ipv_6gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateIpv6GatewayResponse().from_map(self.do_request("CreateIpv6Gateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ipv_6gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ipv_6gateway_with_options(request, runtime)

    def create_ipv_6egress_only_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateIpv6EgressOnlyRuleResponse().from_map(self.do_request("CreateIpv6EgressOnlyRule", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ipv_6egress_only_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ipv_6egress_only_rule_with_options(request, runtime)

    def allocate_ipv_6internet_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AllocateIpv6InternetBandwidthResponse().from_map(self.do_request("AllocateIpv6InternetBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def allocate_ipv_6internet_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_ipv_6internet_bandwidth_with_options(request, runtime)

    def delete_express_connect_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteExpressConnectResponse().from_map(self.do_request("DeleteExpressConnect", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_express_connect(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_express_connect_with_options(request, runtime)

    def create_ipv_6translator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateIPv6TranslatorResponse().from_map(self.do_request("CreateIPv6Translator", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ipv_6translator(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ipv_6translator_with_options(request, runtime)

    def describe_ipv_6translators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIPv6TranslatorsResponse().from_map(self.do_request("DescribeIPv6Translators", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6translators(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6translators_with_options(request, runtime)

    def modify_ipv_6translator_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIPv6TranslatorAttributeResponse().from_map(self.do_request("ModifyIPv6TranslatorAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6translator_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6translator_attribute_with_options(request, runtime)

    def modify_ipv_6translator_bandwidth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIPv6TranslatorBandwidthResponse().from_map(self.do_request("ModifyIPv6TranslatorBandwidth", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6translator_bandwidth(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6translator_bandwidth_with_options(request, runtime)

    def create_ipv_6translator_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateIPv6TranslatorEntryResponse().from_map(self.do_request("CreateIPv6TranslatorEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ipv_6translator_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ipv_6translator_entry_with_options(request, runtime)

    def delete_ipv_6translator_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIPv6TranslatorEntryResponse().from_map(self.do_request("DeleteIPv6TranslatorEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6translator_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6translator_entry_with_options(request, runtime)

    def modify_ipv_6translator_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyIPv6TranslatorEntryResponse().from_map(self.do_request("ModifyIPv6TranslatorEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ipv_6translator_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ipv_6translator_entry_with_options(request, runtime)

    def describe_ipv_6translator_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeIPv6TranslatorEntriesResponse().from_map(self.do_request("DescribeIPv6TranslatorEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ipv_6translator_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ipv_6translator_entries_with_options(request, runtime)

    def delete_ipv_6translator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteIPv6TranslatorResponse().from_map(self.do_request("DeleteIPv6Translator", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ipv_6translator(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ipv_6translator_with_options(request, runtime)

    def allocate_eip_address_pro_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AllocateEipAddressProResponse().from_map(self.do_request("AllocateEipAddressPro", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def allocate_eip_address_pro(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_eip_address_pro_with_options(request, runtime)

    def describe_high_definition_monitor_log_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeHighDefinitionMonitorLogAttributeResponse().from_map(self.do_request("DescribeHighDefinitionMonitorLogAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_high_definition_monitor_log_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_high_definition_monitor_log_attribute_with_options(request, runtime)

    def modify_flow_log_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyFlowLogAttributeResponse().from_map(self.do_request("ModifyFlowLogAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_flow_log_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_flow_log_attribute_with_options(request, runtime)

    def describe_flow_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeFlowLogsResponse().from_map(self.do_request("DescribeFlowLogs", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_flow_logs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_flow_logs_with_options(request, runtime)

    def delete_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteFlowLogResponse().from_map(self.do_request("DeleteFlowLog", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_flow_log(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_flow_log_with_options(request, runtime)

    def deactive_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeactiveFlowLogResponse().from_map(self.do_request("DeactiveFlowLog", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def deactive_flow_log(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.deactive_flow_log_with_options(request, runtime)

    def create_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateFlowLogResponse().from_map(self.do_request("CreateFlowLog", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_flow_log(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_flow_log_with_options(request, runtime)

    def active_flow_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ActiveFlowLogResponse().from_map(self.do_request("ActiveFlowLog", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def active_flow_log(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.active_flow_log_with_options(request, runtime)

    def unassociate_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateRouteTableResponse().from_map(self.do_request("UnassociateRouteTable", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_route_table(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_route_table_with_options(request, runtime)

    def delete_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteRouteTableResponse().from_map(self.do_request("DeleteRouteTable", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_route_table(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_route_table_with_options(request, runtime)

    def create_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateRouteTableResponse().from_map(self.do_request("CreateRouteTable", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_route_table(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_route_table_with_options(request, runtime)

    def associate_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateRouteTableResponse().from_map(self.do_request("AssociateRouteTable", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_route_table(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_route_table_with_options(request, runtime)

    def create_vpn_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVpnGatewayResponse().from_map(self.do_request("CreateVpnGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vpn_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpn_gateway_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.MoveResourceGroupResponse().from_map(self.do_request("MoveResourceGroup", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.move_resource_group_with_options(request, runtime)

    def revoke_instance_from_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RevokeInstanceFromCenResponse().from_map(self.do_request("RevokeInstanceFromCen", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def revoke_instance_from_cen(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.revoke_instance_from_cen_with_options(request, runtime)

    def grant_instance_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.GrantInstanceToCenResponse().from_map(self.do_request("GrantInstanceToCen", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def grant_instance_to_cen(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.grant_instance_to_cen_with_options(request, runtime)

    def describe_grant_rules_to_cen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeGrantRulesToCenResponse().from_map(self.do_request("DescribeGrantRulesToCen", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_grant_rules_to_cen(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_grant_rules_to_cen_with_options(request, runtime)

    def modify_ssl_vpn_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifySslVpnServerResponse().from_map(self.do_request("ModifySslVpnServer", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ssl_vpn_server(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ssl_vpn_server_with_options(request, runtime)

    def modify_ssl_vpn_client_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifySslVpnClientCertResponse().from_map(self.do_request("ModifySslVpnClientCert", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ssl_vpn_client_cert(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ssl_vpn_client_cert_with_options(request, runtime)

    def describe_ssl_vpn_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeSslVpnServersResponse().from_map(self.do_request("DescribeSslVpnServers", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ssl_vpn_servers(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ssl_vpn_servers_with_options(request, runtime)

    def describe_ssl_vpn_client_certs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeSslVpnClientCertsResponse().from_map(self.do_request("DescribeSslVpnClientCerts", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ssl_vpn_client_certs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ssl_vpn_client_certs_with_options(request, runtime)

    def describe_ssl_vpn_client_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeSslVpnClientCertResponse().from_map(self.do_request("DescribeSslVpnClientCert", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ssl_vpn_client_cert(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ssl_vpn_client_cert_with_options(request, runtime)

    def delete_ssl_vpn_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteSslVpnServerResponse().from_map(self.do_request("DeleteSslVpnServer", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ssl_vpn_server(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ssl_vpn_server_with_options(request, runtime)

    def delete_ssl_vpn_client_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteSslVpnClientCertResponse().from_map(self.do_request("DeleteSslVpnClientCert", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ssl_vpn_client_cert(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ssl_vpn_client_cert_with_options(request, runtime)

    def create_ssl_vpn_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateSslVpnServerResponse().from_map(self.do_request("CreateSslVpnServer", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ssl_vpn_server(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ssl_vpn_server_with_options(request, runtime)

    def create_ssl_vpn_client_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateSslVpnClientCertResponse().from_map(self.do_request("CreateSslVpnClientCert", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ssl_vpn_client_cert(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ssl_vpn_client_cert_with_options(request, runtime)

    def remove_global_acceleration_instance_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RemoveGlobalAccelerationInstanceIpResponse().from_map(self.do_request("RemoveGlobalAccelerationInstanceIp", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def remove_global_acceleration_instance_ip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_global_acceleration_instance_ip_with_options(request, runtime)

    def add_global_acceleration_instance_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AddGlobalAccelerationInstanceIpResponse().from_map(self.do_request("AddGlobalAccelerationInstanceIp", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def add_global_acceleration_instance_ip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_global_acceleration_instance_ip_with_options(request, runtime)

    def describe_route_table_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRouteTableListResponse().from_map(self.do_request("DescribeRouteTableList", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_route_table_list(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_route_table_list_with_options(request, runtime)

    def modify_route_table_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyRouteTableAttributesResponse().from_map(self.do_request("ModifyRouteTableAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_route_table_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_route_table_attributes_with_options(request, runtime)

    def describe_bgp_networks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeBgpNetworksResponse().from_map(self.do_request("DescribeBgpNetworks", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_bgp_networks(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bgp_networks_with_options(request, runtime)

    def modify_common_bandwidth_package_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyCommonBandwidthPackagePayTypeResponse().from_map(self.do_request("ModifyCommonBandwidthPackagePayType", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_common_bandwidth_package_pay_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_common_bandwidth_package_pay_type_with_options(request, runtime)

    def unassociate_global_acceleration_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateGlobalAccelerationInstanceResponse().from_map(self.do_request("UnassociateGlobalAccelerationInstance", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_global_acceleration_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_global_acceleration_instance_with_options(request, runtime)

    def modify_global_acceleration_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceSpecResponse().from_map(self.do_request("ModifyGlobalAccelerationInstanceSpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_global_acceleration_instance_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_global_acceleration_instance_spec_with_options(request, runtime)

    def modify_global_acceleration_instance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyGlobalAccelerationInstanceAttributesResponse().from_map(self.do_request("ModifyGlobalAccelerationInstanceAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_global_acceleration_instance_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_global_acceleration_instance_attributes_with_options(request, runtime)

    def describe_server_related_global_acceleration_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeServerRelatedGlobalAccelerationInstancesResponse().from_map(self.do_request("DescribeServerRelatedGlobalAccelerationInstances", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_server_related_global_acceleration_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_server_related_global_acceleration_instances_with_options(request, runtime)

    def describe_global_acceleration_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeGlobalAccelerationInstancesResponse().from_map(self.do_request("DescribeGlobalAccelerationInstances", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_global_acceleration_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_global_acceleration_instances_with_options(request, runtime)

    def delete_global_acceleration_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteGlobalAccelerationInstanceResponse().from_map(self.do_request("DeleteGlobalAccelerationInstance", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_global_acceleration_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_global_acceleration_instance_with_options(request, runtime)

    def create_global_acceleration_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateGlobalAccelerationInstanceResponse().from_map(self.do_request("CreateGlobalAccelerationInstance", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_global_acceleration_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_global_acceleration_instance_with_options(request, runtime)

    def associate_global_acceleration_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateGlobalAccelerationInstanceResponse().from_map(self.do_request("AssociateGlobalAccelerationInstance", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_global_acceleration_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_global_acceleration_instance_with_options(request, runtime)

    def describe_vswitch_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVSwitchAttributesResponse().from_map(self.do_request("DescribeVSwitchAttributes", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vswitch_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vswitch_attributes_with_options(request, runtime)

    def remove_common_bandwidth_package_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RemoveCommonBandwidthPackageIpResponse().from_map(self.do_request("RemoveCommonBandwidthPackageIp", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def remove_common_bandwidth_package_ip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_common_bandwidth_package_ip_with_options(request, runtime)

    def modify_common_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyCommonBandwidthPackageSpecResponse().from_map(self.do_request("ModifyCommonBandwidthPackageSpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_common_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_common_bandwidth_package_spec_with_options(request, runtime)

    def modify_common_bandwidth_package_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyCommonBandwidthPackageAttributeResponse().from_map(self.do_request("ModifyCommonBandwidthPackageAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_common_bandwidth_package_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_common_bandwidth_package_attribute_with_options(request, runtime)

    def describe_common_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeCommonBandwidthPackagesResponse().from_map(self.do_request("DescribeCommonBandwidthPackages", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_common_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_common_bandwidth_packages_with_options(request, runtime)

    def delete_common_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteCommonBandwidthPackageResponse().from_map(self.do_request("DeleteCommonBandwidthPackage", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_common_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_common_bandwidth_package_with_options(request, runtime)

    def create_common_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateCommonBandwidthPackageResponse().from_map(self.do_request("CreateCommonBandwidthPackage", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_common_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_common_bandwidth_package_with_options(request, runtime)

    def add_common_bandwidth_package_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AddCommonBandwidthPackageIpResponse().from_map(self.do_request("AddCommonBandwidthPackageIp", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def add_common_bandwidth_package_ip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_common_bandwidth_package_ip_with_options(request, runtime)

    def modify_vpn_gateway_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVpnGatewayAttributeResponse().from_map(self.do_request("ModifyVpnGatewayAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vpn_gateway_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpn_gateway_attribute_with_options(request, runtime)

    def modify_vpn_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVpnConnectionAttributeResponse().from_map(self.do_request("ModifyVpnConnectionAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vpn_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpn_connection_attribute_with_options(request, runtime)

    def modify_customer_gateway_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyCustomerGatewayAttributeResponse().from_map(self.do_request("ModifyCustomerGatewayAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_customer_gateway_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_customer_gateway_attribute_with_options(request, runtime)

    def download_vpn_connection_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DownloadVpnConnectionConfigResponse().from_map(self.do_request("DownloadVpnConnectionConfig", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def download_vpn_connection_config(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.download_vpn_connection_config_with_options(request, runtime)

    def describe_vpn_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnGatewaysResponse().from_map(self.do_request("DescribeVpnGateways", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_gateways(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_gateways_with_options(request, runtime)

    def describe_vpn_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnGatewayResponse().from_map(self.do_request("DescribeVpnGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_gateway_with_options(request, runtime)

    def describe_vpn_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnConnectionsResponse().from_map(self.do_request("DescribeVpnConnections", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_connections(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_connections_with_options(request, runtime)

    def describe_vpn_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpnConnectionResponse().from_map(self.do_request("DescribeVpnConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpn_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpn_connection_with_options(request, runtime)

    def describe_customer_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeCustomerGatewaysResponse().from_map(self.do_request("DescribeCustomerGateways", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_customer_gateways(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_customer_gateways_with_options(request, runtime)

    def describe_customer_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeCustomerGatewayResponse().from_map(self.do_request("DescribeCustomerGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_customer_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_customer_gateway_with_options(request, runtime)

    def delete_vpn_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVpnGatewayResponse().from_map(self.do_request("DeleteVpnGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vpn_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpn_gateway_with_options(request, runtime)

    def delete_vpn_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVpnConnectionResponse().from_map(self.do_request("DeleteVpnConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vpn_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpn_connection_with_options(request, runtime)

    def delete_customer_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteCustomerGatewayResponse().from_map(self.do_request("DeleteCustomerGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_customer_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_customer_gateway_with_options(request, runtime)

    def create_vpn_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVpnConnectionResponse().from_map(self.do_request("CreateVpnConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vpn_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpn_connection_with_options(request, runtime)

    def create_customer_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateCustomerGatewayResponse().from_map(self.do_request("CreateCustomerGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_customer_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_customer_gateway_with_options(request, runtime)

    def modify_bgp_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyBgpGroupAttributeResponse().from_map(self.do_request("ModifyBgpGroupAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_bgp_group_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_bgp_group_attribute_with_options(request, runtime)

    def describe_bgp_peers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeBgpPeersResponse().from_map(self.do_request("DescribeBgpPeers", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_bgp_peers(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bgp_peers_with_options(request, runtime)

    def describe_bgp_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeBgpGroupsResponse().from_map(self.do_request("DescribeBgpGroups", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_bgp_groups(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bgp_groups_with_options(request, runtime)

    def delete_bgp_peer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteBgpPeerResponse().from_map(self.do_request("DeleteBgpPeer", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_bgp_peer(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_bgp_peer_with_options(request, runtime)

    def delete_bgp_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteBgpNetworkResponse().from_map(self.do_request("DeleteBgpNetwork", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_bgp_network(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_bgp_network_with_options(request, runtime)

    def delete_bgp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteBgpGroupResponse().from_map(self.do_request("DeleteBgpGroup", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_bgp_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_bgp_group_with_options(request, runtime)

    def create_bgp_peer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateBgpPeerResponse().from_map(self.do_request("CreateBgpPeer", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_bgp_peer(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_bgp_peer_with_options(request, runtime)

    def create_bgp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateBgpGroupResponse().from_map(self.do_request("CreateBgpGroup", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_bgp_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_bgp_group_with_options(request, runtime)

    def add_bgp_network_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AddBgpNetworkResponse().from_map(self.do_request("AddBgpNetwork", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def add_bgp_network(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_bgp_network_with_options(request, runtime)

    def enable_vpc_classic_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.EnableVpcClassicLinkResponse().from_map(self.do_request("EnableVpcClassicLink", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def enable_vpc_classic_link(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_vpc_classic_link_with_options(request, runtime)

    def disable_vpc_classic_link_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DisableVpcClassicLinkResponse().from_map(self.do_request("DisableVpcClassicLink", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def disable_vpc_classic_link(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.disable_vpc_classic_link_with_options(request, runtime)

    def describe_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpcAttributeResponse().from_map(self.do_request("DescribeVpcAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpc_attribute_with_options(request, runtime)

    def unassociate_physical_connection_from_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociatePhysicalConnectionFromVirtualBorderRouterResponse().from_map(self.do_request("UnassociatePhysicalConnectionFromVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_physical_connection_from_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_physical_connection_from_virtual_border_router_with_options(request, runtime)

    def associate_physical_connection_to_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociatePhysicalConnectionToVirtualBorderRouterResponse().from_map(self.do_request("AssociatePhysicalConnectionToVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_physical_connection_to_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_physical_connection_to_virtual_border_router_with_options(request, runtime)

    def modify_snat_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifySnatEntryResponse().from_map(self.do_request("ModifySnatEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_snat_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_snat_entry_with_options(request, runtime)

    def modify_nat_gateway_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyNatGatewaySpecResponse().from_map(self.do_request("ModifyNatGatewaySpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_nat_gateway_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_nat_gateway_spec_with_options(request, runtime)

    def modify_nat_gateway_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyNatGatewayAttributeResponse().from_map(self.do_request("ModifyNatGatewayAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_nat_gateway_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_nat_gateway_attribute_with_options(request, runtime)

    def modify_bandwidth_package_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyBandwidthPackageAttributeResponse().from_map(self.do_request("ModifyBandwidthPackageAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_bandwidth_package_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_bandwidth_package_attribute_with_options(request, runtime)

    def describe_snat_table_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeSnatTableEntriesResponse().from_map(self.do_request("DescribeSnatTableEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_snat_table_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snat_table_entries_with_options(request, runtime)

    def delete_snat_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteSnatEntryResponse().from_map(self.do_request("DeleteSnatEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_snat_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_snat_entry_with_options(request, runtime)

    def create_snat_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateSnatEntryResponse().from_map(self.do_request("CreateSnatEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_snat_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_snat_entry_with_options(request, runtime)

    def create_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateBandwidthPackageResponse().from_map(self.do_request("CreateBandwidthPackage", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_bandwidth_package_with_options(request, runtime)

    def unassociate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateHaVipResponse().from_map(self.do_request("UnassociateHaVip", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_ha_vip_with_options(request, runtime)

    def unassociate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.UnassociateEipAddressResponse().from_map(self.do_request("UnassociateEipAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def unassociate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_eip_address_with_options(request, runtime)

    def terminate_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.TerminateVirtualBorderRouterResponse().from_map(self.do_request("TerminateVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def terminate_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.terminate_virtual_border_router_with_options(request, runtime)

    def terminate_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.TerminatePhysicalConnectionResponse().from_map(self.do_request("TerminatePhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def terminate_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.terminate_physical_connection_with_options(request, runtime)

    def remove_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RemoveBandwidthPackageIpsResponse().from_map(self.do_request("RemoveBandwidthPackageIps", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def remove_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    def release_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ReleaseEipAddressResponse().from_map(self.do_request("ReleaseEipAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def release_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.release_eip_address_with_options(request, runtime)

    def recover_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.RecoverVirtualBorderRouterResponse().from_map(self.do_request("RecoverVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def recover_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.recover_virtual_border_router_with_options(request, runtime)

    def modify_vswitch_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVSwitchAttributeResponse().from_map(self.do_request("ModifyVSwitchAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vswitch_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vswitch_attribute_with_options(request, runtime)

    def modify_vrouter_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVRouterAttributeResponse().from_map(self.do_request("ModifyVRouterAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vrouter_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vrouter_attribute_with_options(request, runtime)

    def modify_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVpcAttributeResponse().from_map(self.do_request("ModifyVpcAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpc_attribute_with_options(request, runtime)

    def modify_virtual_border_router_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyVirtualBorderRouterAttributeResponse().from_map(self.do_request("ModifyVirtualBorderRouterAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_virtual_border_router_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    def modify_router_interface_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyRouterInterfaceSpecResponse().from_map(self.do_request("ModifyRouterInterfaceSpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_router_interface_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_router_interface_spec_with_options(request, runtime)

    def modify_router_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyRouterInterfaceAttributeResponse().from_map(self.do_request("ModifyRouterInterfaceAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_router_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_router_interface_attribute_with_options(request, runtime)

    def modify_physical_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyPhysicalConnectionAttributeResponse().from_map(self.do_request("ModifyPhysicalConnectionAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_physical_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    def modify_ha_vip_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyHaVipAttributeResponse().from_map(self.do_request("ModifyHaVipAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_ha_vip_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    def modify_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyForwardEntryResponse().from_map(self.do_request("ModifyForwardEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_forward_entry_with_options(request, runtime)

    def modify_eip_address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyEipAddressAttributeResponse().from_map(self.do_request("ModifyEipAddressAttribute", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_eip_address_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_eip_address_attribute_with_options(request, runtime)

    def modify_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ModifyBandwidthPackageSpecResponse().from_map(self.do_request("ModifyBandwidthPackageSpec", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def modify_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    def enable_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.EnablePhysicalConnectionResponse().from_map(self.do_request("EnablePhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def enable_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_physical_connection_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeZonesResponse().from_map(self.do_request("DescribeZones", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_zones_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVSwitchesResponse().from_map(self.do_request("DescribeVSwitches", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vswitches_with_options(request, runtime)

    def describe_vrouters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVRoutersResponse().from_map(self.do_request("DescribeVRouters", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vrouters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vrouters_with_options(request, runtime)

    def describe_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVpcsResponse().from_map(self.do_request("DescribeVpcs", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_vpcs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpcs_with_options(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(self.do_request("DescribeVirtualBorderRoutersForPhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_virtual_border_routers_for_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    def describe_virtual_border_routers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeVirtualBorderRoutersResponse().from_map(self.do_request("DescribeVirtualBorderRouters", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_virtual_border_routers(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_virtual_border_routers_with_options(request, runtime)

    def describe_route_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRouteTablesResponse().from_map(self.do_request("DescribeRouteTables", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_route_tables(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_route_tables_with_options(request, runtime)

    def describe_router_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRouterInterfacesResponse().from_map(self.do_request("DescribeRouterInterfaces", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_router_interfaces(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_router_interfaces_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeRegionsResponse().from_map(self.do_request("DescribeRegions", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_regions_with_options(request, runtime)

    def describe_physical_connections_with_options(self, request, runtime):
        """
        DescribePhysicalConnections Query physical connections in a region.
        request demo:   * https://vpc.aliyuncs.com/?Action=DescribePhysicalConnections
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribePhysicalConnectionsResponse().from_map(self.do_request("DescribePhysicalConnections", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_physical_connections(self, request):
        """
        DescribePhysicalConnections Query physical connections in a region.
        request demo:   * https://vpc.aliyuncs.com/?Action=DescribePhysicalConnections
        &RegionId=cn-hangzhou
        &<CommonParameters>
        description:
        """
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_physical_connections_with_options(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeNewProjectEipMonitorDataResponse().from_map(self.do_request("DescribeNewProjectEipMonitorData", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_new_project_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    def describe_nat_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeNatGatewaysResponse().from_map(self.do_request("DescribeNatGateways", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_nat_gateways(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_nat_gateways_with_options(request, runtime)

    def describe_ha_vips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeHaVipsResponse().from_map(self.do_request("DescribeHaVips", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_ha_vips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ha_vips_with_options(request, runtime)

    def describe_forward_table_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeForwardTableEntriesResponse().from_map(self.do_request("DescribeForwardTableEntries", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_forward_table_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_forward_table_entries_with_options(request, runtime)

    def describe_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeEipMonitorDataResponse().from_map(self.do_request("DescribeEipMonitorData", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_monitor_data_with_options(request, runtime)

    def describe_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeEipAddressesResponse().from_map(self.do_request("DescribeEipAddresses", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_addresses_with_options(request, runtime)

    def describe_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeBandwidthPackagesResponse().from_map(self.do_request("DescribeBandwidthPackages", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bandwidth_packages_with_options(request, runtime)

    def describe_access_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DescribeAccessPointsResponse().from_map(self.do_request("DescribeAccessPoints", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def describe_access_points(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_access_points_with_options(request, runtime)

    def delete_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVSwitchResponse().from_map(self.do_request("DeleteVSwitch", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vswitch(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vswitch_with_options(request, runtime)

    def delete_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVpcResponse().from_map(self.do_request("DeleteVpc", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpc_with_options(request, runtime)

    def delete_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteVirtualBorderRouterResponse().from_map(self.do_request("DeleteVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_virtual_border_router_with_options(request, runtime)

    def delete_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteRouterInterfaceResponse().from_map(self.do_request("DeleteRouterInterface", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_router_interface_with_options(request, runtime)

    def delete_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteRouteEntryResponse().from_map(self.do_request("DeleteRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_route_entry_with_options(request, runtime)

    def delete_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeletePhysicalConnectionResponse().from_map(self.do_request("DeletePhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_physical_connection_with_options(request, runtime)

    def delete_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteNatGatewayResponse().from_map(self.do_request("DeleteNatGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_nat_gateway_with_options(request, runtime)

    def delete_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteHaVipResponse().from_map(self.do_request("DeleteHaVip", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ha_vip_with_options(request, runtime)

    def delete_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteForwardEntryResponse().from_map(self.do_request("DeleteForwardEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_forward_entry_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeleteBandwidthPackageResponse().from_map(self.do_request("DeleteBandwidthPackage", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_bandwidth_package_with_options(request, runtime)

    def deactivate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.DeactivateRouterInterfaceResponse().from_map(self.do_request("DeactivateRouterInterface", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def deactivate_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.deactivate_router_interface_with_options(request, runtime)

    def create_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVSwitchResponse().from_map(self.do_request("CreateVSwitch", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vswitch(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vswitch_with_options(request, runtime)

    def create_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVpcResponse().from_map(self.do_request("CreateVpc", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpc_with_options(request, runtime)

    def create_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateVirtualBorderRouterResponse().from_map(self.do_request("CreateVirtualBorderRouter", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_virtual_border_router_with_options(request, runtime)

    def create_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateRouterInterfaceResponse().from_map(self.do_request("CreateRouterInterface", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_router_interface_with_options(request, runtime)

    def create_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateRouteEntryResponse().from_map(self.do_request("CreateRouteEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_route_entry_with_options(request, runtime)

    def create_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreatePhysicalConnectionResponse().from_map(self.do_request("CreatePhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_physical_connection_with_options(request, runtime)

    def create_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateNatGatewayResponse().from_map(self.do_request("CreateNatGateway", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_nat_gateway_with_options(request, runtime)

    def create_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateHaVipResponse().from_map(self.do_request("CreateHaVip", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ha_vip_with_options(request, runtime)

    def create_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CreateForwardEntryResponse().from_map(self.do_request("CreateForwardEntry", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def create_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_forward_entry_with_options(request, runtime)

    def connect_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ConnectRouterInterfaceResponse().from_map(self.do_request("ConnectRouterInterface", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def connect_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.connect_router_interface_with_options(request, runtime)

    def cancel_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.CancelPhysicalConnectionResponse().from_map(self.do_request("CancelPhysicalConnection", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def cancel_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_physical_connection_with_options(request, runtime)

    def associate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateHaVipResponse().from_map(self.do_request("AssociateHaVip", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_ha_vip_with_options(request, runtime)

    def associate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AssociateEipAddressResponse().from_map(self.do_request("AssociateEipAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def associate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_eip_address_with_options(request, runtime)

    def allocate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AllocateEipAddressResponse().from_map(self.do_request("AllocateEipAddress", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def allocate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_eip_address_with_options(request, runtime)

    def add_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.AddBandwidthPackageIpsResponse().from_map(self.do_request("AddBandwidthPackageIps", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def add_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    def activate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return vpc_20160428_models.ActivateRouterInterfaceResponse().from_map(self.do_request("ActivateRouterInterface", "HTTPS", "POST", "2016-04-28", "AK", None, request.to_map(), runtime))

    def activate_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.activate_router_interface_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
