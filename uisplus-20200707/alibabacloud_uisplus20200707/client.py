# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_uisplus20200707 import models as uisplus_20200707_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("uisplus", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_uis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeUisResponse().from_map(self.do_request("DescribeUis", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_uis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uis_with_options(request, runtime)

    def modify_vnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.ModifyVnetResponse().from_map(self.do_request("ModifyVnet", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def modify_vnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vnet_with_options(request, runtime)

    def describe_gre_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeGreConnectionsResponse().from_map(self.do_request("DescribeGreConnections", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_gre_connections(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gre_connections_with_options(request, runtime)

    def describe_uiss_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeUissResponse().from_map(self.do_request("DescribeUiss", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_uiss(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_uiss_with_options(request, runtime)

    def describe_vnet_route_entry_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeVnetRouteEntryListResponse().from_map(self.do_request("DescribeVnetRouteEntryList", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_vnet_route_entry_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vnet_route_entry_list_with_options(request, runtime)

    def create_vnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.CreateVnetResponse().from_map(self.do_request("CreateVnet", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def create_vnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vnet_with_options(request, runtime)

    def delete_vnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DeleteVnetResponse().from_map(self.do_request("DeleteVnet", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def delete_vnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vnet_with_options(request, runtime)

    def describe_vnets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeVnetsResponse().from_map(self.do_request("DescribeVnets", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_vnets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vnets_with_options(request, runtime)

    def delete_vnet_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DeleteVnetRouteEntryResponse().from_map(self.do_request("DeleteVnetRouteEntry", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def delete_vnet_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vnet_route_entry_with_options(request, runtime)

    def associate_eip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.AssociateEipResponse().from_map(self.do_request("AssociateEip", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def associate_eip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_with_options(request, runtime)

    def modify_gre_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.ModifyGreConnectionResponse().from_map(self.do_request("ModifyGreConnection", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def modify_gre_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_gre_connection_with_options(request, runtime)

    def describe_vnet_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeVnetResponse().from_map(self.do_request("DescribeVnet", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_vnet(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vnet_with_options(request, runtime)

    def un_associate_eip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.UnAssociateEipResponse().from_map(self.do_request("UnAssociateEip", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def un_associate_eip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_associate_eip_with_options(request, runtime)

    def delete_gre_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DeleteGreConnectionResponse().from_map(self.do_request("DeleteGreConnection", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def delete_gre_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gre_connection_with_options(request, runtime)

    def create_gre_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.CreateGreConnectionResponse().from_map(self.do_request("CreateGreConnection", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def create_gre_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gre_connection_with_options(request, runtime)

    def create_uis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.CreateUisResponse().from_map(self.do_request("CreateUis", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def create_uis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_uis_with_options(request, runtime)

    def create_vnet_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.CreateVnetRouteEntryResponse().from_map(self.do_request("CreateVnetRouteEntry", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def create_vnet_route_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vnet_route_entry_with_options(request, runtime)

    def delete_uis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DeleteUisResponse().from_map(self.do_request("DeleteUis", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def delete_uis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_uis_with_options(request, runtime)

    def describe_gre_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return uisplus_20200707_models.DescribeGreConnectionResponse().from_map(self.do_request("DescribeGreConnection", "HTTPS", "GET", "2020-07-07", "AK", request.to_map(), None, runtime))

    def describe_gre_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_gre_connection_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
