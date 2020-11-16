# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ecd20201001 import models as ecd_20201001_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("ecd", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20201001_models.DescribeDirectoriesResponse().from_map(self.do_request("DescribeDirectories", "HTTPS", "POST", "2020-10-01", "AK", None, request.to_map(), runtime))

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def delete_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20201001_models.DeleteDirectoriesResponse().from_map(self.do_request("DeleteDirectories", "HTTPS", "POST", "2020-10-01", "AK", None, request.to_map(), runtime))

    def delete_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    def describe_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20201001_models.DescribeDesktopsResponse().from_map(self.do_request("DescribeDesktops", "HTTPS", "POST", "2020-10-01", "AK", None, request.to_map(), runtime))

    def describe_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    def reboot_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20201001_models.RebootDesktopsResponse().from_map(self.do_request("RebootDesktops", "HTTPS", "POST", "2020-10-01", "AK", None, request.to_map(), runtime))

    def reboot_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def get_connection_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20201001_models.GetConnectionTicketResponse().from_map(self.do_request("GetConnectionTicket", "HTTPS", "POST", "2020-10-01", "AK", None, request.to_map(), runtime))

    def get_connection_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
