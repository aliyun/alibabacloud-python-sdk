# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ecd20200930 import models as ecd_20200930_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self.check_config(config)
        self._endpoint = self.get_endpoint("ecd", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def modify_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyPolicyGroupResponse().from_map(self.do_request("ModifyPolicyGroup", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def modify_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_policy_group_with_options(request, runtime)

    def pay_order_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.PayOrderCallbackResponse().from_map(self.do_request("PayOrderCallback", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def pay_order_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pay_order_callback_with_options(request, runtime)

    def describe_desktop_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopTypesResponse().from_map(self.do_request("DescribeDesktopTypes", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_desktop_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_types_with_options(request, runtime)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDirectoriesResponse().from_map(self.do_request("DescribeDirectories", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def delete_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDirectoriesResponse().from_map(self.do_request("DeleteDirectories", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def delete_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directories_with_options(request, runtime)

    def list_directory_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ListDirectoryUsersResponse().from_map(self.do_request("ListDirectoryUsers", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def list_directory_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_directory_users_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateImageResponse().from_map(self.do_request("CreateImage", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def create_ramdirectory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateRAMDirectoryResponse().from_map(self.do_request("CreateRAMDirectory", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_ramdirectory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ramdirectory_with_options(request, runtime)

    def delete_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeletePolicyGroupsResponse().from_map(self.do_request("DeletePolicyGroups", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def delete_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_groups_with_options(request, runtime)

    def describe_policy_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribePolicyGroupsResponse().from_map(self.do_request("DescribePolicyGroups", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_policy_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_policy_groups_with_options(request, runtime)

    def delete_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteDesktopsResponse().from_map(self.do_request("DeleteDesktops", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def delete_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_desktops_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyImageAttributeResponse().from_map(self.do_request("ModifyImageAttribute", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def do_logical_delete_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DoLogicalDeleteResourceResponse().from_map(self.do_request("DoLogicalDeleteResource", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def do_logical_delete_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_logical_delete_resource_with_options(request, runtime)

    def modify_entitlement_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyEntitlementResponse().from_map(self.do_request("ModifyEntitlement", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def modify_entitlement(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_entitlement_with_options(request, runtime)

    def delete_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteBundlesResponse().from_map(self.do_request("DeleteBundles", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def delete_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bundles_with_options(request, runtime)

    def describe_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopsResponse().from_map(self.do_request("DescribeDesktops", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktops_with_options(request, runtime)

    def reboot_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.RebootDesktopsResponse().from_map(self.do_request("RebootDesktops", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def reboot_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_desktops_with_options(request, runtime)

    def create_bundle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateBundleResponse().from_map(self.do_request("CreateBundle", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_bundle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bundle_with_options(request, runtime)

    def modify_desktops_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopsPolicyGroupResponse().from_map(self.do_request("ModifyDesktopsPolicyGroup", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def modify_desktops_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktops_policy_group_with_options(request, runtime)

    def create_policy_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreatePolicyGroupResponse().from_map(self.do_request("CreatePolicyGroup", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_policy_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_group_with_options(request, runtime)

    def do_physical_delete_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DoPhysicalDeleteResourceResponse().from_map(self.do_request("DoPhysicalDeleteResource", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def do_physical_delete_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_physical_delete_resource_with_options(request, runtime)

    def create_adconnector_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateADConnectorDirectoryResponse().from_map(self.do_request("CreateADConnectorDirectory", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_adconnector_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_adconnector_directory_with_options(request, runtime)

    def get_connection_ticket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.GetConnectionTicketResponse().from_map(self.do_request("GetConnectionTicket", "HTTP", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def get_connection_ticket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_connection_ticket_with_options(request, runtime)

    def modify_desktop_policys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.ModifyDesktopPolicysResponse().from_map(self.do_request("ModifyDesktopPolicys", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def modify_desktop_policys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_desktop_policys_with_options(request, runtime)

    def describe_bundles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeBundlesResponse().from_map(self.do_request("DescribeBundles", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_bundles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bundles_with_options(request, runtime)

    def delete_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DeleteImagesResponse().from_map(self.do_request("DeleteImages", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def delete_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_images_with_options(request, runtime)

    def do_check_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DoCheckResourceResponse().from_map(self.do_request("DoCheckResource", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def do_check_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.do_check_resource_with_options(request, runtime)

    def describe_desktop_policys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeDesktopPolicysResponse().from_map(self.do_request("DescribeDesktopPolicys", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_desktop_policys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_desktop_policys_with_options(request, runtime)

    def create_desktops_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.CreateDesktopsResponse().from_map(self.do_request("CreateDesktops", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def create_desktops(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_desktops_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecd_20200930_models.DescribeImagesResponse().from_map(self.do_request("DescribeImages", "HTTPS", "POST", "2020-09-30", "AK", None, request.to_map(), runtime))

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
