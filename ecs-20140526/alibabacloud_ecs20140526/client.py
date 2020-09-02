# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-qingdao": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-beijing": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shanghai": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shenzhen": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hongkong": "ecs-cn-hangzhou.aliyuncs.com",
            "ap-southeast-1": "ecs-cn-hangzhou.aliyuncs.com",
            "us-west-1": "ecs-cn-hangzhou.aliyuncs.com",
            "us-east-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shanghai-finance-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shenzhen-finance-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-north-2-gov-1": "ecs.aliyuncs.com",
            "ap-northeast-2-pop": "ecs.ap-northeast-1.aliyuncs.com",
            "cn-beijing-finance-1": "ecs.aliyuncs.com",
            "cn-beijing-finance-pop": "ecs.aliyuncs.com",
            "cn-beijing-gov-1": "ecs.aliyuncs.com",
            "cn-beijing-nu16-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-edge-1": "ecs.cn-qingdao-nebula.aliyuncs.com",
            "cn-fujian": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-haidian-cm12-c01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-bj-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-finance": "ecs.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hangzhou-test-306": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-hongkong-finance-pop": "ecs.aliyuncs.com",
            "cn-shanghai-et15-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shanghai-et2-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shanghai-inner": "ecs.aliyuncs.com",
            "cn-shanghai-internal-test-1": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shenzhen-inner": "ecs.aliyuncs.com",
            "cn-shenzhen-st4-d01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-shenzhen-su18-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-wuhan": "ecs.aliyuncs.com",
            "cn-yushanfang": "ecs.aliyuncs.com",
            "cn-zhangbei-na61-b01": "ecs-cn-hangzhou.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "ecs.cn-zhangjiakou.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "ecs.cn-qingdao-nebula.aliyuncs.com",
            "eu-west-1-oxs": "ecs.cn-shenzhen-cloudstone.aliyuncs.com",
            "rus-west-1-pop": "ecs.ap-northeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("ecs", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def modify_dedicated_host_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDedicatedHostClusterAttributeResponse().from_map(self.do_request("ModifyDedicatedHostClusterAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_dedicated_host_cluster_attribute_with_options(request, runtime)

    def describe_dedicated_host_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDedicatedHostClustersResponse().from_map(self.do_request("DescribeDedicatedHostClusters", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_clusters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_dedicated_host_clusters_with_options(request, runtime)

    def delete_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteDedicatedHostClusterResponse().from_map(self.do_request("DeleteDedicatedHostCluster", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_dedicated_host_cluster_with_options(request, runtime)

    def create_dedicated_host_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateDedicatedHostClusterResponse().from_map(self.do_request("CreateDedicatedHostCluster", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_dedicated_host_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_dedicated_host_cluster_with_options(request, runtime)

    def describe_deployment_set_supported_instance_type_family_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDeploymentSetSupportedInstanceTypeFamilyResponse().from_map(self.do_request("DescribeDeploymentSetSupportedInstanceTypeFamily", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_deployment_set_supported_instance_type_family(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_deployment_set_supported_instance_type_family_with_options(request, runtime)

    def describe_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeNetworkInterfaceAttributeResponse().from_map(self.do_request("DescribeNetworkInterfaceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_network_interface_attribute_with_options(request, runtime)

    def copy_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CopySnapshotResponse().from_map(self.do_request("CopySnapshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def copy_snapshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.copy_snapshot_with_options(request, runtime)

    def modify_dedicated_hosts_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDedicatedHostsChargeTypeResponse().from_map(self.do_request("ModifyDedicatedHostsChargeType", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_dedicated_hosts_charge_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_dedicated_hosts_charge_type_with_options(request, runtime)

    def modify_instance_metadata_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceMetadataOptionsResponse().from_map(self.do_request("ModifyInstanceMetadataOptions", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_metadata_options(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_metadata_options_with_options(request, runtime)

    def describe_image_from_family_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeImageFromFamilyResponse().from_map(self.do_request("DescribeImageFromFamily", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_image_from_family(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_image_from_family_with_options(request, runtime)

    def stop_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.StopInstancesResponse().from_map(self.do_request("StopInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def stop_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.stop_instances_with_options(request, runtime)

    def start_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.StartInstancesResponse().from_map(self.do_request("StartInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def start_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.start_instances_with_options(request, runtime)

    def reboot_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RebootInstancesResponse().from_map(self.do_request("RebootInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def reboot_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.reboot_instances_with_options(request, runtime)

    def redeploy_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RedeployDedicatedHostResponse().from_map(self.do_request("RedeployDedicatedHost", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def redeploy_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.redeploy_dedicated_host_with_options(request, runtime)

    def modify_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceMaintenanceAttributesResponse().from_map(self.do_request("ModifyInstanceMaintenanceAttributes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_maintenance_attributes_with_options(request, runtime)

    def describe_instance_maintenance_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceMaintenanceAttributesResponse().from_map(self.do_request("DescribeInstanceMaintenanceAttributes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_maintenance_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_maintenance_attributes_with_options(request, runtime)

    def modify_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDemandResponse().from_map(self.do_request("ModifyDemand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_demand(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_demand_with_options(request, runtime)

    def delete_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteDemandResponse().from_map(self.do_request("DeleteDemand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_demand(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_demand_with_options(request, runtime)

    def create_demand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateDemandResponse().from_map(self.do_request("CreateDemand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_demand(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_demand_with_options(request, runtime)

    def purchase_storage_capacity_unit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.PurchaseStorageCapacityUnitResponse().from_map(self.do_request("PurchaseStorageCapacityUnit", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def purchase_storage_capacity_unit(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.purchase_storage_capacity_unit_with_options(request, runtime)

    def modify_storage_capacity_unit_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyStorageCapacityUnitAttributeResponse().from_map(self.do_request("ModifyStorageCapacityUnitAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_storage_capacity_unit_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_storage_capacity_unit_attribute_with_options(request, runtime)

    def describe_storage_capacity_units_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeStorageCapacityUnitsResponse().from_map(self.do_request("DescribeStorageCapacityUnits", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_storage_capacity_units(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_storage_capacity_units_with_options(request, runtime)

    def run_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RunCommandResponse().from_map(self.do_request("RunCommand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def run_command(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.run_command_with_options(request, runtime)

    def delete_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteInstancesResponse().from_map(self.do_request("DeleteInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_instances_with_options(request, runtime)

    def modify_storage_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyStorageSetAttributeResponse().from_map(self.do_request("ModifyStorageSetAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_storage_set_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_storage_set_attribute_with_options(request, runtime)

    def describe_storage_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeStorageSetsResponse().from_map(self.do_request("DescribeStorageSets", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_storage_sets(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_storage_sets_with_options(request, runtime)

    def describe_storage_set_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeStorageSetDetailsResponse().from_map(self.do_request("DescribeStorageSetDetails", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_storage_set_details(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_storage_set_details_with_options(request, runtime)

    def delete_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteStorageSetResponse().from_map(self.do_request("DeleteStorageSet", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_storage_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_storage_set_with_options(request, runtime)

    def create_storage_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateStorageSetResponse().from_map(self.do_request("CreateStorageSet", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_storage_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_storage_set_with_options(request, runtime)

    def modify_disk_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDiskSpecResponse().from_map(self.do_request("ModifyDiskSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_disk_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_disk_spec_with_options(request, runtime)

    def modify_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyAutoProvisioningGroupResponse().from_map(self.do_request("ModifyAutoProvisioningGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_auto_provisioning_group_with_options(request, runtime)

    def describe_auto_provisioning_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAutoProvisioningGroupsResponse().from_map(self.do_request("DescribeAutoProvisioningGroups", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_auto_provisioning_groups(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_auto_provisioning_groups_with_options(request, runtime)

    def describe_auto_provisioning_group_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAutoProvisioningGroupInstancesResponse().from_map(self.do_request("DescribeAutoProvisioningGroupInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_auto_provisioning_group_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_auto_provisioning_group_instances_with_options(request, runtime)

    def delete_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteAutoProvisioningGroupResponse().from_map(self.do_request("DeleteAutoProvisioningGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_auto_provisioning_group_with_options(request, runtime)

    def create_auto_provisioning_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateAutoProvisioningGroupResponse().from_map(self.do_request("CreateAutoProvisioningGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_auto_provisioning_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_auto_provisioning_group_with_options(request, runtime)

    def describe_auto_provisioning_group_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAutoProvisioningGroupHistoryResponse().from_map(self.do_request("DescribeAutoProvisioningGroupHistory", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_auto_provisioning_group_history(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_auto_provisioning_group_history_with_options(request, runtime)

    def report_instances_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReportInstancesStatusResponse().from_map(self.do_request("ReportInstancesStatus", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def report_instances_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.report_instances_status_with_options(request, runtime)

    def modify_reserved_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyReservedInstanceAttributeResponse().from_map(self.do_request("ModifyReservedInstanceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_reserved_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_reserved_instance_attribute_with_options(request, runtime)

    def purchase_reserved_instances_offering_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.PurchaseReservedInstancesOfferingResponse().from_map(self.do_request("PurchaseReservedInstancesOffering", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def purchase_reserved_instances_offering(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.purchase_reserved_instances_offering_with_options(request, runtime)

    def modify_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyReservedInstancesResponse().from_map(self.do_request("ModifyReservedInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_reserved_instances_with_options(request, runtime)

    def describe_reserved_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeReservedInstancesResponse().from_map(self.do_request("DescribeReservedInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_reserved_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_reserved_instances_with_options(request, runtime)

    def describe_demands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDemandsResponse().from_map(self.do_request("DescribeDemands", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_demands(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_demands_with_options(request, runtime)

    def import_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ImportSnapshotResponse().from_map(self.do_request("ImportSnapshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def import_snapshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.import_snapshot_with_options(request, runtime)

    def export_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ExportSnapshotResponse().from_map(self.do_request("ExportSnapshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def export_snapshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.export_snapshot_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.UntagResourcesResponse().from_map(self.do_request("UntagResources", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.untag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.TagResourcesResponse().from_map(self.do_request("TagResources", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.tag_resources_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ListTagResourcesResponse().from_map(self.do_request("ListTagResources", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.list_tag_resources_with_options(request, runtime)

    def accept_inquired_system_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AcceptInquiredSystemEventResponse().from_map(self.do_request("AcceptInquiredSystemEvent", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def accept_inquired_system_event(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.accept_inquired_system_event_with_options(request, runtime)

    def redeploy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RedeployInstanceResponse().from_map(self.do_request("RedeployInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def redeploy_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.redeploy_instance_with_options(request, runtime)

    def unassign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.UnassignIpv6AddressesResponse().from_map(self.do_request("UnassignIpv6Addresses", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def unassign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassign_ipv_6addresses_with_options(request, runtime)

    def assign_ipv_6addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AssignIpv6AddressesResponse().from_map(self.do_request("AssignIpv6Addresses", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def assign_ipv_6addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.assign_ipv_6addresses_with_options(request, runtime)

    def describe_instance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceTopologyResponse().from_map(self.do_request("DescribeInstanceTopology", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_topology(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_topology_with_options(request, runtime)

    def renew_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RenewDedicatedHostsResponse().from_map(self.do_request("RenewDedicatedHosts", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def renew_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.renew_dedicated_hosts_with_options(request, runtime)

    def release_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReleaseDedicatedHostResponse().from_map(self.do_request("ReleaseDedicatedHost", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def release_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.release_dedicated_host_with_options(request, runtime)

    def modify_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceDeploymentResponse().from_map(self.do_request("ModifyInstanceDeployment", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_deployment_with_options(request, runtime)

    def modify_dedicated_host_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDedicatedHostAutoRenewAttributeResponse().from_map(self.do_request("ModifyDedicatedHostAutoRenewAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_dedicated_host_auto_renew_attribute_with_options(request, runtime)

    def modify_dedicated_host_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDedicatedHostAutoReleaseTimeResponse().from_map(self.do_request("ModifyDedicatedHostAutoReleaseTime", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_dedicated_host_auto_release_time_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDedicatedHostAttributeResponse().from_map(self.do_request("ModifyDedicatedHostAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDedicatedHostsResponse().from_map(self.do_request("DescribeDedicatedHosts", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_dedicated_host_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDedicatedHostTypesResponse().from_map(self.do_request("DescribeDedicatedHostTypes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_types(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_dedicated_host_types_with_options(request, runtime)

    def describe_dedicated_host_auto_renew_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDedicatedHostAutoRenewResponse().from_map(self.do_request("DescribeDedicatedHostAutoRenew", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_auto_renew(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_dedicated_host_auto_renew_with_options(request, runtime)

    def allocate_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AllocateDedicatedHostsResponse().from_map(self.do_request("AllocateDedicatedHosts", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def allocate_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_dedicated_hosts_with_options(request, runtime)

    def create_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateSimulatedSystemEventsResponse().from_map(self.do_request("CreateSimulatedSystemEvents", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_simulated_system_events_with_options(request, runtime)

    def cancel_simulated_system_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CancelSimulatedSystemEventsResponse().from_map(self.do_request("CancelSimulatedSystemEvents", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def cancel_simulated_system_events(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_simulated_system_events_with_options(request, runtime)

    def describe_eni_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeEniMonitorDataResponse().from_map(self.do_request("DescribeEniMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_eni_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eni_monitor_data_with_options(request, runtime)

    def describe_account_attributes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAccountAttributesResponse().from_map(self.do_request("DescribeAccountAttributes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_account_attributes(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_account_attributes_with_options(request, runtime)

    def modify_launch_template_default_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyLaunchTemplateDefaultVersionResponse().from_map(self.do_request("ModifyLaunchTemplateDefaultVersion", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_launch_template_default_version(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_launch_template_default_version_with_options(request, runtime)

    def describe_launch_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeLaunchTemplatesResponse().from_map(self.do_request("DescribeLaunchTemplates", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_launch_templates(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_launch_templates_with_options(request, runtime)

    def describe_launch_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeLaunchTemplateVersionsResponse().from_map(self.do_request("DescribeLaunchTemplateVersions", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_launch_template_versions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_launch_template_versions_with_options(request, runtime)

    def delete_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteLaunchTemplateVersionResponse().from_map(self.do_request("DeleteLaunchTemplateVersion", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_launch_template_version_with_options(request, runtime)

    def delete_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteLaunchTemplateResponse().from_map(self.do_request("DeleteLaunchTemplate", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_launch_template(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_launch_template_with_options(request, runtime)

    def create_launch_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateLaunchTemplateVersionResponse().from_map(self.do_request("CreateLaunchTemplateVersion", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_launch_template_version(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_launch_template_version_with_options(request, runtime)

    def create_launch_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateLaunchTemplateResponse().from_map(self.do_request("CreateLaunchTemplate", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_launch_template(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_launch_template_with_options(request, runtime)

    def install_cloud_assistant_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.InstallCloudAssistantResponse().from_map(self.do_request("InstallCloudAssistant", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def install_cloud_assistant(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.install_cloud_assistant_with_options(request, runtime)

    def describe_cloud_assistant_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeCloudAssistantStatusResponse().from_map(self.do_request("DescribeCloudAssistantStatus", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_cloud_assistant_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_cloud_assistant_status_with_options(request, runtime)

    def unassign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.UnassignPrivateIpAddressesResponse().from_map(self.do_request("UnassignPrivateIpAddresses", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def unassign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassign_private_ip_addresses_with_options(request, runtime)

    def assign_private_ip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AssignPrivateIpAddressesResponse().from_map(self.do_request("AssignPrivateIpAddresses", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def assign_private_ip_addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.assign_private_ip_addresses_with_options(request, runtime)

    def describe_network_interface_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeNetworkInterfacePermissionsResponse().from_map(self.do_request("DescribeNetworkInterfacePermissions", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_network_interface_permissions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_network_interface_permissions_with_options(request, runtime)

    def delete_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteNetworkInterfacePermissionResponse().from_map(self.do_request("DeleteNetworkInterfacePermission", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_network_interface_permission_with_options(request, runtime)

    def create_network_interface_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateNetworkInterfacePermissionResponse().from_map(self.do_request("CreateNetworkInterfacePermission", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_network_interface_permission(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_network_interface_permission_with_options(request, runtime)

    def get_instance_screenshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.GetInstanceScreenshotResponse().from_map(self.do_request("GetInstanceScreenshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def get_instance_screenshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_instance_screenshot_with_options(request, runtime)

    def get_instance_console_output_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.GetInstanceConsoleOutputResponse().from_map(self.do_request("GetInstanceConsoleOutput", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def get_instance_console_output(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.get_instance_console_output_with_options(request, runtime)

    def describe_resources_modification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeResourcesModificationResponse().from_map(self.do_request("DescribeResourcesModification", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_resources_modification(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_resources_modification_with_options(request, runtime)

    def describe_bandwidth_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeBandwidthLimitationResponse().from_map(self.do_request("DescribeBandwidthLimitation", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_bandwidth_limitation(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bandwidth_limitation_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAvailableResourceResponse().from_map(self.do_request("DescribeAvailableResource", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_available_resource_with_options(request, runtime)

    def re_activate_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReActivateInstancesResponse().from_map(self.do_request("ReActivateInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def re_activate_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.re_activate_instances_with_options(request, runtime)

    def describe_instances_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstancesFullStatusResponse().from_map(self.do_request("DescribeInstancesFullStatus", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instances_full_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instances_full_status_with_options(request, runtime)

    def describe_instance_history_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceHistoryEventsResponse().from_map(self.do_request("DescribeInstanceHistoryEvents", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_history_events(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_history_events_with_options(request, runtime)

    def describe_disks_full_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDisksFullStatusResponse().from_map(self.do_request("DescribeDisksFullStatus", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_disks_full_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_disks_full_status_with_options(request, runtime)

    def modify_user_business_behavior_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyUserBusinessBehaviorResponse().from_map(self.do_request("ModifyUserBusinessBehavior", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_user_business_behavior_with_options(request, runtime)

    def describe_user_business_behavior_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeUserBusinessBehaviorResponse().from_map(self.do_request("DescribeUserBusinessBehavior", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_user_business_behavior(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_user_business_behavior_with_options(request, runtime)

    def run_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RunInstancesResponse().from_map(self.do_request("RunInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def run_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.run_instances_with_options(request, runtime)

    def convert_nat_public_ip_to_eip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ConvertNatPublicIpToEipResponse().from_map(self.do_request("ConvertNatPublicIpToEip", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def convert_nat_public_ip_to_eip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.convert_nat_public_ip_to_eip_with_options(request, runtime)

    def modify_hpc_cluster_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyHpcClusterAttributeResponse().from_map(self.do_request("ModifyHpcClusterAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_hpc_cluster_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_hpc_cluster_attribute_with_options(request, runtime)

    def describe_hpc_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeHpcClustersResponse().from_map(self.do_request("DescribeHpcClusters", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_hpc_clusters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_hpc_clusters_with_options(request, runtime)

    def delete_hpc_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteHpcClusterResponse().from_map(self.do_request("DeleteHpcCluster", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_hpc_cluster_with_options(request, runtime)

    def create_hpc_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateHpcClusterResponse().from_map(self.do_request("CreateHpcCluster", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_hpc_cluster(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_hpc_cluster_with_options(request, runtime)

    def describe_snapshots_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSnapshotsUsageResponse().from_map(self.do_request("DescribeSnapshotsUsage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_snapshots_usage(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snapshots_usage_with_options(request, runtime)

    def describe_spot_price_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSpotPriceHistoryResponse().from_map(self.do_request("DescribeSpotPriceHistory", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_spot_price_history(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_spot_price_history_with_options(request, runtime)

    def stop_invocation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.StopInvocationResponse().from_map(self.do_request("StopInvocation", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def stop_invocation(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.stop_invocation_with_options(request, runtime)

    def modify_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyCommandResponse().from_map(self.do_request("ModifyCommand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_command(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_command_with_options(request, runtime)

    def invoke_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.InvokeCommandResponse().from_map(self.do_request("InvokeCommand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def invoke_command(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.invoke_command_with_options(request, runtime)

    def describe_invocations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInvocationsResponse().from_map(self.do_request("DescribeInvocations", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_invocations(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_invocations_with_options(request, runtime)

    def describe_invocation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInvocationResultsResponse().from_map(self.do_request("DescribeInvocationResults", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_invocation_results(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_invocation_results_with_options(request, runtime)

    def describe_commands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeCommandsResponse().from_map(self.do_request("DescribeCommands", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_commands(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_commands_with_options(request, runtime)

    def delete_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteCommandResponse().from_map(self.do_request("DeleteCommand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_command(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_command_with_options(request, runtime)

    def create_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateCommandResponse().from_map(self.do_request("CreateCommand", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_command(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_command_with_options(request, runtime)

    def modify_security_group_egress_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifySecurityGroupEgressRuleResponse().from_map(self.do_request("ModifySecurityGroupEgressRule", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_security_group_egress_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_security_group_egress_rule_with_options(request, runtime)

    def modify_disk_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDiskChargeTypeResponse().from_map(self.do_request("ModifyDiskChargeType", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_disk_charge_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_disk_charge_type_with_options(request, runtime)

    def modify_network_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyNetworkInterfaceAttributeResponse().from_map(self.do_request("ModifyNetworkInterfaceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_network_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_network_interface_attribute_with_options(request, runtime)

    def detach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DetachNetworkInterfaceResponse().from_map(self.do_request("DetachNetworkInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def detach_network_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_network_interface_with_options(request, runtime)

    def describe_network_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeNetworkInterfacesResponse().from_map(self.do_request("DescribeNetworkInterfaces", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_network_interfaces(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_network_interfaces_with_options(request, runtime)

    def delete_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteNetworkInterfaceResponse().from_map(self.do_request("DeleteNetworkInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_network_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_network_interface_with_options(request, runtime)

    def create_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateNetworkInterfaceResponse().from_map(self.do_request("CreateNetworkInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_network_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_network_interface_with_options(request, runtime)

    def attach_network_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AttachNetworkInterfaceResponse().from_map(self.do_request("AttachNetworkInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def attach_network_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_network_interface_with_options(request, runtime)

    def describe_recommend_instance_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeRecommendInstanceTypeResponse().from_map(self.do_request("DescribeRecommendInstanceType", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_recommend_instance_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_recommend_instance_type_with_options(request, runtime)

    def modify_prepay_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyPrepayInstanceSpecResponse().from_map(self.do_request("ModifyPrepayInstanceSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_prepay_instance_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    def modify_instance_charge_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceChargeTypeResponse().from_map(self.do_request("ModifyInstanceChargeType", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_charge_type(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_charge_type_with_options(request, runtime)

    def join_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.JoinResourceGroupResponse().from_map(self.do_request("JoinResourceGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def join_resource_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.join_resource_group_with_options(request, runtime)

    def modify_security_group_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifySecurityGroupPolicyResponse().from_map(self.do_request("ModifySecurityGroupPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_security_group_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_security_group_policy_with_options(request, runtime)

    def describe_security_group_references_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSecurityGroupReferencesResponse().from_map(self.do_request("DescribeSecurityGroupReferences", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_security_group_references(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_security_group_references_with_options(request, runtime)

    def detach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DetachClassicLinkVpcResponse().from_map(self.do_request("DetachClassicLinkVpc", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def detach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_classic_link_vpc_with_options(request, runtime)

    def describe_classic_link_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeClassicLinkInstancesResponse().from_map(self.do_request("DescribeClassicLinkInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_classic_link_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_classic_link_instances_with_options(request, runtime)

    def attach_classic_link_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AttachClassicLinkVpcResponse().from_map(self.do_request("AttachClassicLinkVpc", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def attach_classic_link_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_classic_link_vpc_with_options(request, runtime)

    def detach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DetachInstanceRamRoleResponse().from_map(self.do_request("DetachInstanceRamRole", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def detach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_instance_ram_role_with_options(request, runtime)

    def describe_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceRamRoleResponse().from_map(self.do_request("DescribeInstanceRamRole", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_ram_role_with_options(request, runtime)

    def attach_instance_ram_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AttachInstanceRamRoleResponse().from_map(self.do_request("AttachInstanceRamRole", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def attach_instance_ram_role(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_instance_ram_role_with_options(request, runtime)

    def describe_snapshot_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSnapshotPackageResponse().from_map(self.do_request("DescribeSnapshotPackage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_snapshot_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snapshot_package_with_options(request, runtime)

    def modify_security_group_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifySecurityGroupRuleResponse().from_map(self.do_request("ModifySecurityGroupRule", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_security_group_rule(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_security_group_rule_with_options(request, runtime)

    def describe_snapshot_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSnapshotMonitorDataResponse().from_map(self.do_request("DescribeSnapshotMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_snapshot_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snapshot_monitor_data_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeRenewalPriceResponse().from_map(self.do_request("DescribeRenewalPrice", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribePriceResponse().from_map(self.do_request("DescribePrice", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_price_with_options(request, runtime)

    def modify_deployment_set_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDeploymentSetAttributeResponse().from_map(self.do_request("ModifyDeploymentSetAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_deployment_set_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_deployment_set_attribute_with_options(request, runtime)

    def describe_deployment_sets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDeploymentSetsResponse().from_map(self.do_request("DescribeDeploymentSets", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_deployment_sets(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_deployment_sets_with_options(request, runtime)

    def delete_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteDeploymentSetResponse().from_map(self.do_request("DeleteDeploymentSet", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_deployment_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_deployment_set_with_options(request, runtime)

    def create_deployment_set_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateDeploymentSetResponse().from_map(self.do_request("CreateDeploymentSet", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_deployment_set(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_deployment_set_with_options(request, runtime)

    def import_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ImportKeyPairResponse().from_map(self.do_request("ImportKeyPair", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def import_key_pair(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.import_key_pair_with_options(request, runtime)

    def detach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DetachKeyPairResponse().from_map(self.do_request("DetachKeyPair", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def detach_key_pair(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_key_pair_with_options(request, runtime)

    def describe_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeKeyPairsResponse().from_map(self.do_request("DescribeKeyPairs", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_key_pairs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_key_pairs_with_options(request, runtime)

    def delete_key_pairs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteKeyPairsResponse().from_map(self.do_request("DeleteKeyPairs", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_key_pairs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_key_pairs_with_options(request, runtime)

    def create_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateKeyPairResponse().from_map(self.do_request("CreateKeyPair", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_key_pair(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_key_pair_with_options(request, runtime)

    def attach_key_pair_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AttachKeyPairResponse().from_map(self.do_request("AttachKeyPair", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def attach_key_pair(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_key_pair_with_options(request, runtime)

    def modify_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceAutoRenewAttributeResponse().from_map(self.do_request("ModifyInstanceAutoRenewAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_auto_renew_attribute_with_options(request, runtime)

    def describe_instance_auto_renew_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceAutoRenewAttributeResponse().from_map(self.do_request("DescribeInstanceAutoRenewAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_auto_renew_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_auto_renew_attribute_with_options(request, runtime)

    def describe_snapshot_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSnapshotLinksResponse().from_map(self.do_request("DescribeSnapshotLinks", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_snapshot_links(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snapshot_links_with_options(request, runtime)

    def modify_instance_auto_release_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceAutoReleaseTimeResponse().from_map(self.do_request("ModifyInstanceAutoReleaseTime", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_auto_release_time(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_auto_release_time_with_options(request, runtime)

    def describe_new_project_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeNewProjectEipMonitorDataResponse().from_map(self.do_request("DescribeNewProjectEipMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_new_project_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_new_project_eip_monitor_data_with_options(request, runtime)

    def describe_user_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeUserDataResponse().from_map(self.do_request("DescribeUserData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_user_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_user_data_with_options(request, runtime)

    def remove_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RemoveBandwidthPackageIpsResponse().from_map(self.do_request("RemoveBandwidthPackageIps", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def remove_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_bandwidth_package_ips_with_options(request, runtime)

    def modify_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyForwardEntryResponse().from_map(self.do_request("ModifyForwardEntry", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_forward_entry_with_options(request, runtime)

    def modify_bandwidth_package_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyBandwidthPackageSpecResponse().from_map(self.do_request("ModifyBandwidthPackageSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_bandwidth_package_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_bandwidth_package_spec_with_options(request, runtime)

    def describe_nat_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeNatGatewaysResponse().from_map(self.do_request("DescribeNatGateways", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_nat_gateways(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_nat_gateways_with_options(request, runtime)

    def describe_forward_table_entries_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeForwardTableEntriesResponse().from_map(self.do_request("DescribeForwardTableEntries", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_forward_table_entries(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_forward_table_entries_with_options(request, runtime)

    def describe_bandwidth_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeBandwidthPackagesResponse().from_map(self.do_request("DescribeBandwidthPackages", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_bandwidth_packages(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_bandwidth_packages_with_options(request, runtime)

    def delete_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteNatGatewayResponse().from_map(self.do_request("DeleteNatGateway", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_nat_gateway_with_options(request, runtime)

    def delete_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteForwardEntryResponse().from_map(self.do_request("DeleteForwardEntry", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_forward_entry_with_options(request, runtime)

    def delete_bandwidth_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteBandwidthPackageResponse().from_map(self.do_request("DeleteBandwidthPackage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_bandwidth_package(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_bandwidth_package_with_options(request, runtime)

    def create_nat_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateNatGatewayResponse().from_map(self.do_request("CreateNatGateway", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_nat_gateway(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_nat_gateway_with_options(request, runtime)

    def create_forward_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateForwardEntryResponse().from_map(self.do_request("CreateForwardEntry", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_forward_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_forward_entry_with_options(request, runtime)

    def add_bandwidth_package_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AddBandwidthPackageIpsResponse().from_map(self.do_request("AddBandwidthPackageIps", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def add_bandwidth_package_ips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_bandwidth_package_ips_with_options(request, runtime)

    def eip_fill_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.EipFillProductResponse().from_map(self.do_request("EipFillProduct", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def eip_fill_product(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.eip_fill_product_with_options(request, runtime)

    def eip_notify_paid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.EipNotifyPaidResponse().from_map(self.do_request("EipNotifyPaid", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def eip_notify_paid(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.eip_notify_paid_with_options(request, runtime)

    def eip_fill_params_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.EipFillParamsResponse().from_map(self.do_request("EipFillParams", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def eip_fill_params(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.eip_fill_params_with_options(request, runtime)

    def modify_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyAutoSnapshotPolicyExResponse().from_map(self.do_request("ModifyAutoSnapshotPolicyEx", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_auto_snapshot_policy_ex_with_options(request, runtime)

    def describe_auto_snapshot_policy_ex_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAutoSnapshotPolicyExResponse().from_map(self.do_request("DescribeAutoSnapshotPolicyEx", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_auto_snapshot_policy_ex(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_auto_snapshot_policy_ex_with_options(request, runtime)

    def delete_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteAutoSnapshotPolicyResponse().from_map(self.do_request("DeleteAutoSnapshotPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_auto_snapshot_policy_with_options(request, runtime)

    def create_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateAutoSnapshotPolicyResponse().from_map(self.do_request("CreateAutoSnapshotPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_auto_snapshot_policy_with_options(request, runtime)

    def cancel_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CancelAutoSnapshotPolicyResponse().from_map(self.do_request("CancelAutoSnapshotPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def cancel_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_auto_snapshot_policy_with_options(request, runtime)

    def apply_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ApplyAutoSnapshotPolicyResponse().from_map(self.do_request("ApplyAutoSnapshotPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def apply_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.apply_auto_snapshot_policy_with_options(request, runtime)

    def describe_image_support_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeImageSupportInstanceTypesResponse().from_map(self.do_request("DescribeImageSupportInstanceTypes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_image_support_instance_types(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_image_support_instance_types_with_options(request, runtime)

    def terminate_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.TerminateVirtualBorderRouterResponse().from_map(self.do_request("TerminateVirtualBorderRouter", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def terminate_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.terminate_virtual_border_router_with_options(request, runtime)

    def terminate_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.TerminatePhysicalConnectionResponse().from_map(self.do_request("TerminatePhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def terminate_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.terminate_physical_connection_with_options(request, runtime)

    def recover_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RecoverVirtualBorderRouterResponse().from_map(self.do_request("RecoverVirtualBorderRouter", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def recover_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.recover_virtual_border_router_with_options(request, runtime)

    def modify_virtual_border_router_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyVirtualBorderRouterAttributeResponse().from_map(self.do_request("ModifyVirtualBorderRouterAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_virtual_border_router_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_virtual_border_router_attribute_with_options(request, runtime)

    def modify_physical_connection_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyPhysicalConnectionAttributeResponse().from_map(self.do_request("ModifyPhysicalConnectionAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_physical_connection_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_physical_connection_attribute_with_options(request, runtime)

    def enable_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.EnablePhysicalConnectionResponse().from_map(self.do_request("EnablePhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def enable_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.enable_physical_connection_with_options(request, runtime)

    def describe_virtual_border_routers_for_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeVirtualBorderRoutersForPhysicalConnectionResponse().from_map(self.do_request("DescribeVirtualBorderRoutersForPhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_virtual_border_routers_for_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_virtual_border_routers_for_physical_connection_with_options(request, runtime)

    def describe_virtual_border_routers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeVirtualBorderRoutersResponse().from_map(self.do_request("DescribeVirtualBorderRouters", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_virtual_border_routers(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_virtual_border_routers_with_options(request, runtime)

    def describe_physical_connections_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribePhysicalConnectionsResponse().from_map(self.do_request("DescribePhysicalConnections", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_physical_connections(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_physical_connections_with_options(request, runtime)

    def describe_access_points_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeAccessPointsResponse().from_map(self.do_request("DescribeAccessPoints", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_access_points(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_access_points_with_options(request, runtime)

    def delete_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteVirtualBorderRouterResponse().from_map(self.do_request("DeleteVirtualBorderRouter", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_virtual_border_router_with_options(request, runtime)

    def delete_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeletePhysicalConnectionResponse().from_map(self.do_request("DeletePhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_physical_connection_with_options(request, runtime)

    def create_virtual_border_router_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateVirtualBorderRouterResponse().from_map(self.do_request("CreateVirtualBorderRouter", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_virtual_border_router(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_virtual_border_router_with_options(request, runtime)

    def create_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreatePhysicalConnectionResponse().from_map(self.do_request("CreatePhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_physical_connection_with_options(request, runtime)

    def cancel_physical_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CancelPhysicalConnectionResponse().from_map(self.do_request("CancelPhysicalConnection", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def cancel_physical_connection(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_physical_connection_with_options(request, runtime)

    def import_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ImportImageResponse().from_map(self.do_request("ImportImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def import_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.import_image_with_options(request, runtime)

    def export_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ExportImageResponse().from_map(self.do_request("ExportImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def export_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.export_image_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeTasksResponse().from_map(self.do_request("DescribeTasks", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_tasks_with_options(request, runtime)

    def describe_task_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeTaskAttributeResponse().from_map(self.do_request("DescribeTaskAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_task_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_task_attribute_with_options(request, runtime)

    def cancel_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CancelTaskResponse().from_map(self.do_request("CancelTask", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def cancel_task(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_task_with_options(request, runtime)

    def describe_instance_type_families_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceTypeFamiliesResponse().from_map(self.do_request("DescribeInstanceTypeFamilies", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_type_families(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_type_families_with_options(request, runtime)

    def modify_router_interface_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyRouterInterfaceSpecResponse().from_map(self.do_request("ModifyRouterInterfaceSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_router_interface_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_router_interface_spec_with_options(request, runtime)

    def modify_router_interface_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyRouterInterfaceAttributeResponse().from_map(self.do_request("ModifyRouterInterfaceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_router_interface_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_router_interface_attribute_with_options(request, runtime)

    def describe_router_interfaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeRouterInterfacesResponse().from_map(self.do_request("DescribeRouterInterfaces", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_router_interfaces(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_router_interfaces_with_options(request, runtime)

    def delete_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteRouterInterfaceResponse().from_map(self.do_request("DeleteRouterInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_router_interface_with_options(request, runtime)

    def deactivate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeactivateRouterInterfaceResponse().from_map(self.do_request("DeactivateRouterInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def deactivate_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.deactivate_router_interface_with_options(request, runtime)

    def create_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateRouterInterfaceResponse().from_map(self.do_request("CreateRouterInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_router_interface_with_options(request, runtime)

    def connect_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ConnectRouterInterfaceResponse().from_map(self.do_request("ConnectRouterInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def connect_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.connect_router_interface_with_options(request, runtime)

    def activate_router_interface_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ActivateRouterInterfaceResponse().from_map(self.do_request("ActivateRouterInterface", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def activate_router_interface(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.activate_router_interface_with_options(request, runtime)

    def unassociate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.UnassociateHaVipResponse().from_map(self.do_request("UnassociateHaVip", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def unassociate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_ha_vip_with_options(request, runtime)

    def modify_ha_vip_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyHaVipAttributeResponse().from_map(self.do_request("ModifyHaVipAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_ha_vip_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_ha_vip_attribute_with_options(request, runtime)

    def describe_ha_vips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeHaVipsResponse().from_map(self.do_request("DescribeHaVips", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_ha_vips(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_ha_vips_with_options(request, runtime)

    def delete_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteHaVipResponse().from_map(self.do_request("DeleteHaVip", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_ha_vip_with_options(request, runtime)

    def create_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateHaVipResponse().from_map(self.do_request("CreateHaVip", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_ha_vip_with_options(request, runtime)

    def associate_ha_vip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AssociateHaVipResponse().from_map(self.do_request("AssociateHaVip", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def associate_ha_vip(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_ha_vip_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RenewInstanceResponse().from_map(self.do_request("RenewInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.renew_instance_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RemoveTagsResponse().from_map(self.do_request("RemoveTags", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.remove_tags_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeTagsResponse().from_map(self.do_request("DescribeTags", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_tags_with_options(request, runtime)

    def describe_resource_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeResourceByTagsResponse().from_map(self.do_request("DescribeResourceByTags", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_resource_by_tags(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_resource_by_tags_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AddTagsResponse().from_map(self.do_request("AddTags", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def add_tags(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.add_tags_with_options(request, runtime)

    def unassociate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.UnassociateEipAddressResponse().from_map(self.do_request("UnassociateEipAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def unassociate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.unassociate_eip_address_with_options(request, runtime)

    def stop_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.StopInstanceResponse().from_map(self.do_request("StopInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def stop_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.stop_instance_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.StartInstanceResponse().from_map(self.do_request("StartInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.start_instance_with_options(request, runtime)

    def revoke_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RevokeSecurityGroupEgressResponse().from_map(self.do_request("RevokeSecurityGroupEgress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def revoke_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.revoke_security_group_egress_with_options(request, runtime)

    def revoke_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RevokeSecurityGroupResponse().from_map(self.do_request("RevokeSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def revoke_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.revoke_security_group_with_options(request, runtime)

    def resize_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ResizeDiskResponse().from_map(self.do_request("ResizeDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def resize_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.resize_disk_with_options(request, runtime)

    def reset_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ResetDiskResponse().from_map(self.do_request("ResetDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def reset_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.reset_disk_with_options(request, runtime)

    def replace_system_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReplaceSystemDiskResponse().from_map(self.do_request("ReplaceSystemDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def replace_system_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.replace_system_disk_with_options(request, runtime)

    def release_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReleasePublicIpAddressResponse().from_map(self.do_request("ReleasePublicIpAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def release_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.release_public_ip_address_with_options(request, runtime)

    def release_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReleaseEipAddressResponse().from_map(self.do_request("ReleaseEipAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def release_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.release_eip_address_with_options(request, runtime)

    def re_init_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ReInitDiskResponse().from_map(self.do_request("ReInitDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def re_init_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.re_init_disk_with_options(request, runtime)

    def reboot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.RebootInstanceResponse().from_map(self.do_request("RebootInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def reboot_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.reboot_instance_with_options(request, runtime)

    def modify_vswitch_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyVSwitchAttributeResponse().from_map(self.do_request("ModifyVSwitchAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_vswitch_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vswitch_attribute_with_options(request, runtime)

    def modify_vrouter_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyVRouterAttributeResponse().from_map(self.do_request("ModifyVRouterAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_vrouter_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vrouter_attribute_with_options(request, runtime)

    def modify_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyVpcAttributeResponse().from_map(self.do_request("ModifyVpcAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_vpc_attribute_with_options(request, runtime)

    def modify_snapshot_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifySnapshotAttributeResponse().from_map(self.do_request("ModifySnapshotAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_snapshot_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_snapshot_attribute_with_options(request, runtime)

    def modify_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifySecurityGroupAttributeResponse().from_map(self.do_request("ModifySecurityGroupAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_security_group_attribute_with_options(request, runtime)

    def modify_instance_vpc_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceVpcAttributeResponse().from_map(self.do_request("ModifyInstanceVpcAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_vpc_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_vpc_attribute_with_options(request, runtime)

    def modify_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceVncPasswdResponse().from_map(self.do_request("ModifyInstanceVncPasswd", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_vnc_passwd_with_options(request, runtime)

    def modify_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceSpecResponse().from_map(self.do_request("ModifyInstanceSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_spec_with_options(request, runtime)

    def modify_instance_network_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceNetworkSpecResponse().from_map(self.do_request("ModifyInstanceNetworkSpec", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_network_spec(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_network_spec_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyInstanceAttributeResponse().from_map(self.do_request("ModifyInstanceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyImageSharePermissionResponse().from_map(self.do_request("ModifyImageSharePermission", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_image_share_permission_with_options(request, runtime)

    def modify_image_share_group_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyImageShareGroupPermissionResponse().from_map(self.do_request("ModifyImageShareGroupPermission", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_image_share_group_permission(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_image_share_group_permission_with_options(request, runtime)

    def modify_image_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyImageAttributeResponse().from_map(self.do_request("ModifyImageAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_image_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_image_attribute_with_options(request, runtime)

    def modify_eip_address_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyEipAddressAttributeResponse().from_map(self.do_request("ModifyEipAddressAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_eip_address_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_eip_address_attribute_with_options(request, runtime)

    def modify_disk_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyDiskAttributeResponse().from_map(self.do_request("ModifyDiskAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_disk_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_disk_attribute_with_options(request, runtime)

    def modify_auto_snapshot_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.ModifyAutoSnapshotPolicyResponse().from_map(self.do_request("ModifyAutoSnapshotPolicy", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def modify_auto_snapshot_policy(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.modify_auto_snapshot_policy_with_options(request, runtime)

    def leave_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.LeaveSecurityGroupResponse().from_map(self.do_request("LeaveSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def leave_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.leave_security_group_with_options(request, runtime)

    def join_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.JoinSecurityGroupResponse().from_map(self.do_request("JoinSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def join_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.join_security_group_with_options(request, runtime)

    def detach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DetachDiskResponse().from_map(self.do_request("DetachDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def detach_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.detach_disk_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeZonesResponse().from_map(self.do_request("DescribeZones", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_zones_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeVSwitchesResponse().from_map(self.do_request("DescribeVSwitches", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vswitches_with_options(request, runtime)

    def describe_vrouters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeVRoutersResponse().from_map(self.do_request("DescribeVRouters", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_vrouters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vrouters_with_options(request, runtime)

    def describe_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeVpcsResponse().from_map(self.do_request("DescribeVpcs", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_vpcs(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_vpcs_with_options(request, runtime)

    def describe_snapshots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSnapshotsResponse().from_map(self.do_request("DescribeSnapshots", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_snapshots(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_snapshots_with_options(request, runtime)

    def describe_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSecurityGroupsResponse().from_map(self.do_request("DescribeSecurityGroups", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_security_groups(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_security_groups_with_options(request, runtime)

    def describe_security_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeSecurityGroupAttributeResponse().from_map(self.do_request("DescribeSecurityGroupAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_security_group_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_security_group_attribute_with_options(request, runtime)

    def describe_route_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeRouteTablesResponse().from_map(self.do_request("DescribeRouteTables", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_route_tables(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_route_tables_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeRegionsResponse().from_map(self.do_request("DescribeRegions", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_regions_with_options(request, runtime)

    def describe_limitation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeLimitationResponse().from_map(self.do_request("DescribeLimitation", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_limitation(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_limitation_with_options(request, runtime)

    def describe_instance_vnc_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceVncUrlResponse().from_map(self.do_request("DescribeInstanceVncUrl", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_vnc_url(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_vnc_url_with_options(request, runtime)

    def describe_instance_vnc_passwd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceVncPasswdResponse().from_map(self.do_request("DescribeInstanceVncPasswd", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_vnc_passwd(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_vnc_passwd_with_options(request, runtime)

    def describe_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceTypesResponse().from_map(self.do_request("DescribeInstanceTypes", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_types(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_types_with_options(request, runtime)

    def describe_instance_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceStatusResponse().from_map(self.do_request("DescribeInstanceStatus", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_status(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_status_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstancesResponse().from_map(self.do_request("DescribeInstances", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instances_with_options(request, runtime)

    def describe_instance_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceMonitorDataResponse().from_map(self.do_request("DescribeInstanceMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_monitor_data_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeInstanceAttributeResponse().from_map(self.do_request("DescribeInstanceAttribute", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_image_share_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeImageSharePermissionResponse().from_map(self.do_request("DescribeImageSharePermission", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_image_share_permission(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_image_share_permission_with_options(request, runtime)

    def describe_images_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeImagesResponse().from_map(self.do_request("DescribeImages", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_images(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_images_with_options(request, runtime)

    def describe_eip_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeEipMonitorDataResponse().from_map(self.do_request("DescribeEipMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_eip_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_monitor_data_with_options(request, runtime)

    def describe_eip_addresses_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeEipAddressesResponse().from_map(self.do_request("DescribeEipAddresses", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_eip_addresses(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_eip_addresses_with_options(request, runtime)

    def describe_disks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDisksResponse().from_map(self.do_request("DescribeDisks", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_disks(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_disks_with_options(request, runtime)

    def describe_disk_monitor_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeDiskMonitorDataResponse().from_map(self.do_request("DescribeDiskMonitorData", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_disk_monitor_data(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_disk_monitor_data_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DescribeClustersResponse().from_map(self.do_request("DescribeClusters", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.describe_clusters_with_options(request, runtime)

    def delete_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteVSwitchResponse().from_map(self.do_request("DeleteVSwitch", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_vswitch(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vswitch_with_options(request, runtime)

    def delete_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteVpcResponse().from_map(self.do_request("DeleteVpc", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_vpc_with_options(request, runtime)

    def delete_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteSnapshotResponse().from_map(self.do_request("DeleteSnapshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_snapshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_snapshot_with_options(request, runtime)

    def delete_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteSecurityGroupResponse().from_map(self.do_request("DeleteSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_security_group_with_options(request, runtime)

    def delete_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteRouteEntryResponse().from_map(self.do_request("DeleteRouteEntry", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_route_entry_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteInstanceResponse().from_map(self.do_request("DeleteInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_instance_with_options(request, runtime)

    def delete_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteImageResponse().from_map(self.do_request("DeleteImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_image_with_options(request, runtime)

    def delete_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.DeleteDiskResponse().from_map(self.do_request("DeleteDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def delete_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.delete_disk_with_options(request, runtime)

    def create_vswitch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateVSwitchResponse().from_map(self.do_request("CreateVSwitch", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_vswitch(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vswitch_with_options(request, runtime)

    def create_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateVpcResponse().from_map(self.do_request("CreateVpc", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_vpc(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_vpc_with_options(request, runtime)

    def create_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateSnapshotResponse().from_map(self.do_request("CreateSnapshot", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_snapshot(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_snapshot_with_options(request, runtime)

    def create_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateSecurityGroupResponse().from_map(self.do_request("CreateSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_security_group_with_options(request, runtime)

    def create_route_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateRouteEntryResponse().from_map(self.do_request("CreateRouteEntry", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_route_entry(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_route_entry_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateInstanceResponse().from_map(self.do_request("CreateInstance", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_instance_with_options(request, runtime)

    def create_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateImageResponse().from_map(self.do_request("CreateImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_image_with_options(request, runtime)

    def create_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CreateDiskResponse().from_map(self.do_request("CreateDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def create_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.create_disk_with_options(request, runtime)

    def copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CopyImageResponse().from_map(self.do_request("CopyImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def copy_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.copy_image_with_options(request, runtime)

    def cancel_copy_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.CancelCopyImageResponse().from_map(self.do_request("CancelCopyImage", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def cancel_copy_image(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.cancel_copy_image_with_options(request, runtime)

    def authorize_security_group_egress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AuthorizeSecurityGroupEgressResponse().from_map(self.do_request("AuthorizeSecurityGroupEgress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def authorize_security_group_egress(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.authorize_security_group_egress_with_options(request, runtime)

    def authorize_security_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AuthorizeSecurityGroupResponse().from_map(self.do_request("AuthorizeSecurityGroup", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def authorize_security_group(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.authorize_security_group_with_options(request, runtime)

    def attach_disk_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AttachDiskResponse().from_map(self.do_request("AttachDisk", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def attach_disk(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.attach_disk_with_options(request, runtime)

    def associate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AssociateEipAddressResponse().from_map(self.do_request("AssociateEipAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def associate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.associate_eip_address_with_options(request, runtime)

    def allocate_public_ip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AllocatePublicIpAddressResponse().from_map(self.do_request("AllocatePublicIpAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def allocate_public_ip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_public_ip_address_with_options(request, runtime)

    def allocate_eip_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return ecs_20140526_models.AllocateEipAddressResponse().from_map(self.do_request("AllocateEipAddress", "HTTPS", "POST", "2014-05-26", "AK", None, request.to_map(), runtime))

    def allocate_eip_address(self, request):
        runtime = util_models.RuntimeOptions(

        )
        return self.allocate_eip_address_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
