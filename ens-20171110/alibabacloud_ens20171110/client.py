# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ens20171110 import models as ens_20171110_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ""
        self.check_config(config)
        self._endpoint = self.get_endpoint("ens", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def describe_epn_bandwitdh_by_internet_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEpnBandwitdhByInternetChargeTypeResponse().from_map(self.do_request("DescribeEpnBandwitdhByInternetChargeType", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_epn_bandwitdh_by_internet_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_bandwitdh_by_internet_charge_type_with_options(request, runtime)

    def describe_epn_band_width_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEpnBandWidthDataResponse().from_map(self.do_request("DescribeEpnBandWidthData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_epn_band_width_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_band_width_data_with_options(request, runtime)

    def describe_epn_measurement_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEpnMeasurementDataResponse().from_map(self.do_request("DescribeEpnMeasurementData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_epn_measurement_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_measurement_data_with_options(request, runtime)

    def describe_network_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeNetworkInterfacesResponse().from_map(self.do_request("DescribeNetworkInterfaces", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_network_interfaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_network_interfaces_with_options(request, runtime)

    def create_epinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateEPInstanceResponse().from_map(self.do_request("CreateEPInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_epinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_epinstance_with_options(request, runtime)

    def modify_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ModifyImageSharePermissionResponse().from_map(self.do_request("ModifyImageSharePermission", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def modify_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_share_permission_with_options(request, runtime)

    def add_network_interface_to_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AddNetworkInterfaceToInstanceResponse().from_map(self.do_request("AddNetworkInterfaceToInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def add_network_interface_to_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_network_interface_to_instance_with_options(request, runtime)

    def describe_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeImageSharePermissionResponse().from_map(self.do_request("DescribeImageSharePermission", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_share_permission_with_options(request, runtime)

    def remove_vswitches_from_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RemoveVSwitchesFromEpnInstanceResponse().from_map(self.do_request("RemoveVSwitchesFromEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def remove_vswitches_from_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vswitches_from_epn_instance_with_options(request, runtime)

    def dist_application_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DistApplicationDataResponse().from_map(self.do_request("DistApplicationData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def dist_application_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dist_application_data_with_options(request, runtime)

    def join_vswitches_to_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.JoinVSwitchesToEpnInstanceResponse().from_map(self.do_request("JoinVSwitchesToEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def join_vswitches_to_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_vswitches_to_epn_instance_with_options(request, runtime)

    def describe_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeApplicationResponse().from_map(self.do_request("DescribeApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_application_with_options(request, runtime)

    def describe_data_push_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeDataPushResultResponse().from_map(self.do_request("DescribeDataPushResult", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_data_push_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_push_result_with_options(request, runtime)

    def push_application_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.PushApplicationDataResponse().from_map(self.do_request("PushApplicationData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def push_application_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_application_data_with_options(request, runtime)

    def upgrade_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.UpgradeApplicationResponse().from_map(self.do_request("UpgradeApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def upgrade_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_application_with_options(request, runtime)

    def rescale_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RescaleApplicationResponse().from_map(self.do_request("RescaleApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def rescale_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rescale_application_with_options(request, runtime)

    def delete_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DeleteEpnInstanceResponse().from_map(self.do_request("DeleteEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def delete_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_epn_instance_with_options(request, runtime)

    def list_applications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ListApplicationsResponse().from_map(self.do_request("ListApplications", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def list_applications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    def describe_servcie_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeServcieScheduleResponse().from_map(self.do_request("DescribeServcieSchedule", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_servcie_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_servcie_schedule_with_options(request, runtime)

    def delete_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DeleteApplicationResponse().from_map(self.do_request("DeleteApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def delete_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    def modify_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ModifyEpnInstanceResponse().from_map(self.do_request("ModifyEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def modify_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_epn_instance_with_options(request, runtime)

    def rollback_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RollbackApplicationResponse().from_map(self.do_request("RollbackApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def rollback_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_application_with_options(request, runtime)

    def describe_epn_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEpnInstanceAttributeResponse().from_map(self.do_request("DescribeEpnInstanceAttribute", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_epn_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_instance_attribute_with_options(request, runtime)

    def run_service_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RunServiceScheduleResponse().from_map(self.do_request("RunServiceSchedule", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def run_service_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_service_schedule_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateApplicationResponse().from_map(self.do_request("CreateApplication", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateEpnInstanceResponse().from_map(self.do_request("CreateEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_epn_instance_with_options(request, runtime)

    def stop_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.StopEpnInstanceResponse().from_map(self.do_request("StopEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def stop_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_epn_instance_with_options(request, runtime)

    def describe_data_dist_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeDataDistResultResponse().from_map(self.do_request("DescribeDataDistResult", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_data_dist_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_dist_result_with_options(request, runtime)

    def describe_epn_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEpnInstancesResponse().from_map(self.do_request("DescribeEpnInstances", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_epn_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_epn_instances_with_options(request, runtime)

    def remove_public_ips_from_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RemovePublicIpsFromEpnInstanceResponse().from_map(self.do_request("RemovePublicIpsFromEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def remove_public_ips_from_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_public_ips_from_epn_instance_with_options(request, runtime)

    def join_public_ips_to_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.JoinPublicIpsToEpnInstanceResponse().from_map(self.do_request("JoinPublicIpsToEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def join_public_ips_to_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_public_ips_to_epn_instance_with_options(request, runtime)

    def describe_application_resource_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeApplicationResourceSummaryResponse().from_map(self.do_request("DescribeApplicationResourceSummary", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_application_resource_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_application_resource_summary_with_options(request, runtime)

    def start_epn_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.StartEpnInstanceResponse().from_map(self.do_request("StartEpnInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def start_epn_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_epn_instance_with_options(request, runtime)

    def describe_export_image_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeExportImageInfoResponse().from_map(self.do_request("DescribeExportImageInfo", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_export_image_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_export_image_info_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeVSwitchesResponse().from_map(self.do_request("DescribeVSwitches", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    def delete_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DeleteVSwitchResponse().from_map(self.do_request("DeleteVSwitch", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def delete_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vswitch_with_options(request, runtime)

    def create_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateVSwitchResponse().from_map(self.do_request("CreateVSwitch", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_vswitch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vswitch_with_options(request, runtime)

    def describe_export_image_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeExportImageStatusResponse().from_map(self.do_request("DescribeExportImageStatus", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_export_image_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_export_image_status_with_options(request, runtime)

    def export_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ExportImageResponse().from_map(self.do_request("ExportImage", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def export_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_image_with_options(request, runtime)

    def import_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ImportKeyPairResponse().from_map(self.do_request("ImportKeyPair", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def import_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_key_pair_with_options(request, runtime)

    def describe_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeKeyPairsResponse().from_map(self.do_request("DescribeKeyPairs", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_key_pairs_with_options(request, runtime)

    def delete_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DeleteKeyPairsResponse().from_map(self.do_request("DeleteKeyPairs", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def delete_key_pairs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_key_pairs_with_options(request, runtime)

    def create_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateKeyPairResponse().from_map(self.do_request("CreateKeyPair", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_key_pair(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_key_pair_with_options(request, runtime)

    def export_bill_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ExportBillDetailDataResponse().from_map(self.do_request("ExportBillDetailData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def export_bill_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_bill_detail_data_with_options(request, runtime)

    def describe_ens_region_id_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsRegionIdResourceResponse().from_map(self.do_request("DescribeEnsRegionIdResource", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_region_id_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_region_id_resource_with_options(request, runtime)

    def describe_bandwitdh_by_internet_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeBandwitdhByInternetChargeTypeResponse().from_map(self.do_request("DescribeBandwitdhByInternetChargeType", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_bandwitdh_by_internet_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bandwitdh_by_internet_charge_type_with_options(request, runtime)

    def authorize_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AuthorizeSecurityGroupResponse().from_map(self.do_request("AuthorizeSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def authorize_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    def revoke_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RevokeSecurityGroupResponse().from_map(self.do_request("RevokeSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def revoke_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DeleteSecurityGroupResponse().from_map(self.do_request("DeleteSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_security_group_with_options(request, runtime)

    def describe_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeSecurityGroupAttributeResponse().from_map(self.do_request("DescribeSecurityGroupAttribute", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    def leave_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.LeaveSecurityGroupResponse().from_map(self.do_request("LeaveSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def leave_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.leave_security_group_with_options(request, runtime)

    def join_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.JoinSecurityGroupResponse().from_map(self.do_request("JoinSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def join_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_security_group_with_options(request, runtime)

    def authorize_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AuthorizeSecurityGroupEgressResponse().from_map(self.do_request("AuthorizeSecurityGroupEgress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def authorize_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_egress_with_options(request, runtime)

    def revoke_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RevokeSecurityGroupEgressResponse().from_map(self.do_request("RevokeSecurityGroupEgress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def revoke_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_security_group_egress_with_options(request, runtime)

    def describe_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeSecurityGroupsResponse().from_map(self.do_request("DescribeSecurityGroups", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_groups_with_options(request, runtime)

    def create_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateSecurityGroupResponse().from_map(self.do_request("CreateSecurityGroup", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_security_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_security_group_with_options(request, runtime)

    def describe_ens_region_id_ipv_6info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsRegionIdIpv6InfoResponse().from_map(self.do_request("DescribeEnsRegionIdIpv6Info", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_region_id_ipv_6info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_region_id_ipv_6info_with_options(request, runtime)

    def describe_create_pre_paid_instance_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeCreatePrePaidInstanceResultResponse().from_map(self.do_request("DescribeCreatePrePaidInstanceResult", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_create_pre_paid_instance_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_create_pre_paid_instance_result_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribePriceResponse().from_map(self.do_request("DescribePrice", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def export_measurement_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ExportMeasurementDataResponse().from_map(self.do_request("ExportMeasurementData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def export_measurement_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_measurement_data_with_options(request, runtime)

    def describe_measurement_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeMeasurementDataResponse().from_map(self.do_request("DescribeMeasurementData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_measurement_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_measurement_data_with_options(request, runtime)

    def describe_available_resource_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeAvailableResourceInfoResponse().from_map(self.do_request("DescribeAvailableResourceInfo", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_available_resource_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_info_with_options(request, runtime)

    def describe_pre_paid_instance_stock_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribePrePaidInstanceStockResponse().from_map(self.do_request("DescribePrePaidInstanceStock", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_pre_paid_instance_stock(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_paid_instance_stock_with_options(request, runtime)

    def unassociate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.UnassociateEipAddressResponse().from_map(self.do_request("UnassociateEipAddress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def unassociate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassociate_eip_address_with_options(request, runtime)

    def release_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ReleaseEipAddressResponse().from_map(self.do_request("ReleaseEipAddress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def release_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_eip_address_with_options(request, runtime)

    def describe_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEipAddressesResponse().from_map(self.do_request("DescribeEipAddresses", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eip_addresses_with_options(request, runtime)

    def associate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AssociateEipAddressResponse().from_map(self.do_request("AssociateEipAddress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def associate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_eip_address_with_options(request, runtime)

    def allocate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AllocateEipAddressResponse().from_map(self.do_request("AllocateEipAddress", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def allocate_eip_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_eip_address_with_options(request, runtime)

    def release_post_paid_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ReleasePostPaidInstanceResponse().from_map(self.do_request("ReleasePostPaidInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def release_post_paid_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_post_paid_instance_with_options(request, runtime)

    def release_pre_paid_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ReleasePrePaidInstanceResponse().from_map(self.do_request("ReleasePrePaidInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def release_pre_paid_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_pre_paid_instance_with_options(request, runtime)

    def attach_ens_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.AttachEnsInstancesResponse().from_map(self.do_request("AttachEnsInstances", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def attach_ens_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_ens_instances_with_options(request, runtime)

    def describe_reserved_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeReservedResourceResponse().from_map(self.do_request("DescribeReservedResource", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_reserved_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_reserved_resource_with_options(request, runtime)

    def describe_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeInstanceTypesResponse().from_map(self.do_request("DescribeInstanceTypes", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_types_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateImageResponse().from_map(self.do_request("CreateImage", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_image_with_options(request, runtime)

    def describe_ens_net_sale_district_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsNetSaleDistrictResponse().from_map(self.do_request("DescribeEnsNetSaleDistrict", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_net_sale_district(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_sale_district_with_options(request, runtime)

    def describe_ens_net_district_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsNetDistrictResponse().from_map(self.do_request("DescribeEnsNetDistrict", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_net_district(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_district_with_options(request, runtime)

    def pre_create_ens_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.PreCreateEnsServiceResponse().from_map(self.do_request("PreCreateEnsService", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def pre_create_ens_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pre_create_ens_service_with_options(request, runtime)

    def describe_band_withd_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeBandWithdChargeTypeResponse().from_map(self.do_request("DescribeBandWithdChargeType", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_band_withd_charge_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_band_withd_charge_type_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ModifyImageAttributeResponse().from_map(self.do_request("ModifyImageAttribute", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_image_attribute_with_options(request, runtime)

    def create_ens_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateEnsServiceResponse().from_map(self.do_request("CreateEnsService", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_ens_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_ens_service_with_options(request, runtime)

    def describe_ens_net_level_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsNetLevelResponse().from_map(self.do_request("DescribeEnsNetLevel", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_net_level(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_net_level_with_options(request, runtime)

    def describe_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeInstanceSpecResponse().from_map(self.do_request("DescribeInstanceSpec", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_with_options(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeInstanceAutoRenewAttributeResponse().from_map(self.do_request("DescribeInstanceAutoRenewAttribute", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeAvailableResourceResponse().from_map(self.do_request("DescribeAvailableResource", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.CreateInstanceResponse().from_map(self.do_request("CreateInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def re_init_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ReInitDiskResponse().from_map(self.do_request("ReInitDisk", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def re_init_disk(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_init_disk_with_options(request, runtime)

    def describe_image_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeImageInfosResponse().from_map(self.do_request("DescribeImageInfos", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_image_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_image_infos_with_options(request, runtime)

    def describe_user_band_width_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeUserBandWidthDataResponse().from_map(self.do_request("DescribeUserBandWidthData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_user_band_width_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_band_width_data_with_options(request, runtime)

    def reboot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.RebootInstanceResponse().from_map(self.do_request("RebootInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def reboot_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reboot_instance_with_options(request, runtime)

    def describe_ens_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeEnsRegionsResponse().from_map(self.do_request("DescribeEnsRegions", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_ens_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ens_regions_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.StartInstanceResponse().from_map(self.do_request("StartInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def describe_instance_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeInstanceMonitorDataResponse().from_map(self.do_request("DescribeInstanceMonitorData", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_instance_monitor_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_monitor_data_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeInstancesResponse().from_map(self.do_request("DescribeInstances", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.DescribeImagesResponse().from_map(self.do_request("DescribeImages", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_images_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.StopInstanceResponse().from_map(self.do_request("StopInstance", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_instance_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ens_20171110_models.ModifyInstanceAttributeResponse().from_map(self.do_request("ModifyInstanceAttribute", "HTTPS", "POST", "2017-11-10", "AK", None, request.to_map(), runtime))

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
