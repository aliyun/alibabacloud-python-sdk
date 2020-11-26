# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_rds20140815 import models as rds_20140815_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "regional"
        self._endpoint_map = {
            "cn-qingdao": "rds.aliyuncs.com",
            "cn-beijing": "rds.aliyuncs.com",
            "cn-hangzhou": "rds.aliyuncs.com",
            "cn-shanghai": "rds.aliyuncs.com",
            "cn-shenzhen": "rds.aliyuncs.com",
            "cn-hongkong": "rds.aliyuncs.com",
            "ap-southeast-1": "rds.aliyuncs.com",
            "us-west-1": "rds.aliyuncs.com",
            "us-east-1": "rds.aliyuncs.com",
            "cn-shanghai-finance-1": "rds.aliyuncs.com",
            "cn-shenzhen-finance-1": "rds.aliyuncs.com",
            "cn-north-2-gov-1": "rds.aliyuncs.com",
            "ap-northeast-2-pop": "rds.ap-northeast-1.aliyuncs.com",
            "cn-beijing-finance-1": "rds.aliyuncs.com",
            "cn-beijing-finance-pop": "rds.aliyuncs.com",
            "cn-beijing-gov-1": "rds.aliyuncs.com",
            "cn-beijing-nu16-b01": "rds.aliyuncs.com",
            "cn-edge-1": "rds.aliyuncs.com",
            "cn-fujian": "rds.aliyuncs.com",
            "cn-haidian-cm12-c01": "rds.aliyuncs.com",
            "cn-hangzhou-bj-b01": "rds.aliyuncs.com",
            "cn-hangzhou-finance": "rds.aliyuncs.com",
            "cn-hangzhou-internal-prod-1": "rds.aliyuncs.com",
            "cn-hangzhou-internal-test-1": "rds.aliyuncs.com",
            "cn-hangzhou-internal-test-2": "rds.aliyuncs.com",
            "cn-hangzhou-internal-test-3": "rds.aliyuncs.com",
            "cn-hangzhou-test-306": "rds.aliyuncs.com",
            "cn-hongkong-finance-pop": "rds.aliyuncs.com",
            "cn-qingdao-nebula": "rds.aliyuncs.com",
            "cn-shanghai-et15-b01": "rds.aliyuncs.com",
            "cn-shanghai-et2-b01": "rds.aliyuncs.com",
            "cn-shanghai-inner": "rds.aliyuncs.com",
            "cn-shanghai-internal-test-1": "rds.aliyuncs.com",
            "cn-shenzhen-inner": "rds.aliyuncs.com",
            "cn-shenzhen-st4-d01": "rds.aliyuncs.com",
            "cn-shenzhen-su18-b01": "rds.aliyuncs.com",
            "cn-wuhan": "rds.aliyuncs.com",
            "cn-yushanfang": "rds.aliyuncs.com",
            "cn-zhangbei-na61-b01": "rds.aliyuncs.com",
            "cn-zhangjiakou-na62-a01": "rds.aliyuncs.com",
            "cn-zhengzhou-nebula-1": "rds.aliyuncs.com",
            "eu-west-1-oxs": "rds.ap-northeast-1.aliyuncs.com",
            "rus-west-1-pop": "rds.ap-northeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("rds", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.GetDbProxyInstanceSslResponse().from_map(self.do_request("GetDbProxyInstanceSsl", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def get_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_db_proxy_instance_ssl_with_options(request, runtime)

    def modify_db_proxy_instance_ssl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDbProxyInstanceSslResponse().from_map(self.do_request("ModifyDbProxyInstanceSsl", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_db_proxy_instance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_db_proxy_instance_ssl_with_options(request, runtime)

    def migrate_connection_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.MigrateConnectionToOtherZoneResponse().from_map(self.do_request("MigrateConnectionToOtherZone", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def migrate_connection_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_connection_to_other_zone_with_options(request, runtime)

    def get_dbinstance_topology_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.GetDBInstanceTopologyResponse().from_map(self.do_request("GetDBInstanceTopology", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def get_dbinstance_topology(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_dbinstance_topology_with_options(request, runtime)

    def check_region_support_backup_encryption_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckRegionSupportBackupEncryptionResponse().from_map(self.do_request("CheckRegionSupportBackupEncryption", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_region_support_backup_encryption(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_region_support_backup_encryption_with_options(request, runtime)

    def describe_dbinstance_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceDetailResponse().from_map(self.do_request("DescribeDBInstanceDetail", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_detail_with_options(request, runtime)

    def modify_license_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyLicenseInfoResponse().from_map(self.do_request("ModifyLicenseInfo", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_license_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_license_info_with_options(request, runtime)

    def delete_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteDBProxyEndpointAddressResponse().from_map(self.do_request("DeleteDBProxyEndpointAddress", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbproxy_endpoint_address_with_options(request, runtime)

    def create_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDBProxyEndpointAddressResponse().from_map(self.do_request("CreateDBProxyEndpointAddress", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dbproxy_endpoint_address_with_options(request, runtime)

    def describe_das_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDasInstanceConfigResponse().from_map(self.do_request("DescribeDasInstanceConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_das_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_das_instance_config_with_options(request, runtime)

    def modify_das_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDasInstanceConfigResponse().from_map(self.do_request("ModifyDasInstanceConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_das_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_das_instance_config_with_options(request, runtime)

    def describe_rds_resource_settings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeRdsResourceSettingsResponse().from_map(self.do_request("DescribeRdsResourceSettings", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_rds_resource_settings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_resource_settings_with_options(request, runtime)

    def delete_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteHostAccountResponse().from_map(self.do_request("DeleteHostAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    def describe_host_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeHostAccountsResponse().from_map(self.do_request("DescribeHostAccounts", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_host_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_host_accounts_with_options(request, runtime)

    def reset_host_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ResetHostAccountPasswordResponse().from_map(self.do_request("ResetHostAccountPassword", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def reset_host_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_host_account_password_with_options(request, runtime)

    def create_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateHostAccountResponse().from_map(self.do_request("CreateHostAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    def describe_dedicated_host_image_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDedicatedHostImageCategoriesResponse().from_map(self.do_request("DescribeDedicatedHostImageCategories", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_image_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_image_categories_with_options(request, runtime)

    def describe_cross_backup_meta_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCrossBackupMetaListResponse().from_map(self.do_request("DescribeCrossBackupMetaList", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_cross_backup_meta_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_backup_meta_list_with_options(request, runtime)

    def restore_ddr_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RestoreDdrTableResponse().from_map(self.do_request("RestoreDdrTable", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def restore_ddr_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_ddr_table_with_options(request, runtime)

    def modify_dbproxy_endpoint_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBProxyEndpointAddressResponse().from_map(self.do_request("ModifyDBProxyEndpointAddress", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbproxy_endpoint_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_address_with_options(request, runtime)

    def terminate_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.TerminateMigrateTaskResponse().from_map(self.do_request("TerminateMigrateTask", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def terminate_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.terminate_migrate_task_with_options(request, runtime)

    def describe_local_available_recovery_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeLocalAvailableRecoveryTimeResponse().from_map(self.do_request("DescribeLocalAvailableRecoveryTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_local_available_recovery_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_local_available_recovery_time_with_options(request, runtime)

    def describe_available_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableZonesResponse().from_map(self.do_request("DescribeAvailableZones", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_zones_with_options(request, runtime)

    def describe_available_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableClassesResponse().from_map(self.do_request("DescribeAvailableClasses", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_classes_with_options(request, runtime)

    def create_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDedicatedHostAccountResponse().from_map(self.do_request("CreateDedicatedHostAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    def delete_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteDedicatedHostAccountResponse().from_map(self.do_request("DeleteDedicatedHostAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    def modify_dedicated_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDedicatedHostAccountResponse().from_map(self.do_request("ModifyDedicatedHostAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    def transform_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.TransformDBInstancePayTypeResponse().from_map(self.do_request("TransformDBInstancePayType", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def transform_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_dbinstance_pay_type_with_options(request, runtime)

    def create_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDedicatedHostUserResponse().from_map(self.do_request("CreateDedicatedHostUser", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_user_with_options(request, runtime)

    def modify_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDedicatedHostUserResponse().from_map(self.do_request("ModifyDedicatedHostUser", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_user_with_options(request, runtime)

    def drop_dedicated_host_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DropDedicatedHostUserResponse().from_map(self.do_request("DropDedicatedHostUser", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def drop_dedicated_host_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    def upgrade_dbproxy_instance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.UpgradeDBProxyInstanceKernelVersionResponse().from_map(self.do_request("UpgradeDBProxyInstanceKernelVersion", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def upgrade_dbproxy_instance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbproxy_instance_kernel_version_with_options(request, runtime)

    def stop_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.StopDBInstanceResponse().from_map(self.do_request("StopDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def stop_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    def start_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.StartDBInstanceResponse().from_map(self.do_request("StartDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def start_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    def describe_signed_event_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSignedEventActionsResponse().from_map(self.do_request("DescribeSignedEventActions", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_signed_event_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_signed_event_actions_with_options(request, runtime)

    def sign_event_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.SignEventActionResponse().from_map(self.do_request("SignEventAction", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def sign_event_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sign_event_action_with_options(request, runtime)

    def describe_next_event_for_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeNextEventForSignResponse().from_map(self.do_request("DescribeNextEventForSign", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_next_event_for_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_next_event_for_sign_with_options(request, runtime)

    def modify_action_event_verify_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyActionEventVerifyPolicyResponse().from_map(self.do_request("ModifyActionEventVerifyPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_action_event_verify_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_verify_policy_with_options(request, runtime)

    def describe_dbinstances_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesOverviewResponse().from_map(self.do_request("DescribeDBInstancesOverview", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_overview_with_options(request, runtime)

    def describe_migrate_task_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeMigrateTaskByIdResponse().from_map(self.do_request("DescribeMigrateTaskById", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_migrate_task_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_task_by_id_with_options(request, runtime)

    def delete_backup_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteBackupFileResponse().from_map(self.do_request("DeleteBackupFile", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_backup_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_file_with_options(request, runtime)

    def describe_detached_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDetachedBackupsResponse().from_map(self.do_request("DescribeDetachedBackups", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_detached_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_detached_backups_with_options(request, runtime)

    def evaluate_dedicated_host_instance_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.EvaluateDedicatedHostInstanceResourceResponse().from_map(self.do_request("EvaluateDedicatedHostInstanceResource", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def evaluate_dedicated_host_instance_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.evaluate_dedicated_host_instance_resource_with_options(request, runtime)

    def describe_available_dedicated_host_classes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableDedicatedHostClassesResponse().from_map(self.do_request("DescribeAvailableDedicatedHostClasses", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_dedicated_host_classes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    def describe_available_dedicated_host_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableDedicatedHostZonesResponse().from_map(self.do_request("DescribeAvailableDedicatedHostZones", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_dedicated_host_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    def release_instance_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ReleaseInstanceConnectionResponse().from_map(self.do_request("ReleaseInstanceConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def release_instance_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_connection_with_options(request, runtime)

    def unlock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.UnlockAccountResponse().from_map(self.do_request("UnlockAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def unlock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_account_with_options(request, runtime)

    def lock_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.LockAccountResponse().from_map(self.do_request("LockAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def lock_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_account_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ListTagResourcesResponse().from_map(self.do_request("ListTagResources", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.TagResourcesResponse().from_map(self.do_request("TagResources", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.UntagResourcesResponse().from_map(self.do_request("UntagResources", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def describe_dedicated_host_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDedicatedHostGroupsResponse().from_map(self.do_request("DescribeDedicatedHostGroups", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    def create_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDedicatedHostGroupResponse().from_map(self.do_request("CreateDedicatedHostGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    def delete_dedicated_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteDedicatedHostGroupResponse().from_map(self.do_request("DeleteDedicatedHostGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_dedicated_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDedicatedHostGroupAttributeResponse().from_map(self.do_request("ModifyDedicatedHostGroupAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    def restart_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RestartDedicatedHostResponse().from_map(self.do_request("RestartDedicatedHost", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def restart_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    def replace_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ReplaceDedicatedHostResponse().from_map(self.do_request("ReplaceDedicatedHost", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def replace_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    def describe_dedicated_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDedicatedHostsResponse().from_map(self.do_request("DescribeDedicatedHosts", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dedicated_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    def describe_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDedicatedHostAttributeResponse().from_map(self.do_request("DescribeDedicatedHostAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    def clear_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ClearDedicatedHostResponse().from_map(self.do_request("ClearDedicatedHost", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def clear_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    def modify_dedicated_host_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDedicatedHostAttributeResponse().from_map(self.do_request("ModifyDedicatedHostAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dedicated_host_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    def migrate_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.MigrateDBInstanceResponse().from_map(self.do_request("MigrateDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def migrate_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_dbinstance_with_options(request, runtime)

    def create_dedicated_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDedicatedHostResponse().from_map(self.do_request("CreateDedicatedHost", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dedicated_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    def rebuild_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RebuildDBInstanceResponse().from_map(self.do_request("RebuildDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def rebuild_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebuild_dbinstance_with_options(request, runtime)

    def describe_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBProxyEndpointResponse().from_map(self.do_request("DescribeDBProxyEndpoint", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_endpoint_with_options(request, runtime)

    def describe_dbproxy_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBProxyPerformanceResponse().from_map(self.do_request("DescribeDBProxyPerformance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbproxy_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_performance_with_options(request, runtime)

    def describe_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBProxyResponse().from_map(self.do_request("DescribeDBProxy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbproxy_with_options(request, runtime)

    def modify_dbproxy_endpoint_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBProxyEndpointResponse().from_map(self.do_request("ModifyDBProxyEndpoint", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbproxy_endpoint(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_endpoint_with_options(request, runtime)

    def modify_dbproxy_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBProxyInstanceResponse().from_map(self.do_request("ModifyDBProxyInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbproxy_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_instance_with_options(request, runtime)

    def modify_dbproxy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBProxyResponse().from_map(self.do_request("ModifyDBProxy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbproxy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbproxy_with_options(request, runtime)

    def modify_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyHASwitchConfigResponse().from_map(self.do_request("ModifyHASwitchConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_haswitch_config_with_options(request, runtime)

    def describe_haswitch_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeHASwitchConfigResponse().from_map(self.do_request("DescribeHASwitchConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_haswitch_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_haswitch_config_with_options(request, runtime)

    def modify_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyActionEventPolicyResponse().from_map(self.do_request("ModifyActionEventPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_action_event_policy_with_options(request, runtime)

    def describe_action_event_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeActionEventPolicyResponse().from_map(self.do_request("DescribeActionEventPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_action_event_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_action_event_policy_with_options(request, runtime)

    def describe_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeEventsResponse().from_map(self.do_request("DescribeEvents", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_events_with_options(request, runtime)

    def describe_dbinstances_for_clone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesForCloneResponse().from_map(self.do_request("DescribeDBInstancesForClone", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances_for_clone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_for_clone_with_options(request, runtime)

    def describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        """
        DescribeDTCSecurityIpHostsForSQLServer 调用DescribeDTCSecurityIpHostsForSQLServer接口查询RDS实例的分布式事务白名单信息。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeDTCSecurityIpHostsForSQLServer
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 关于分布式事务白名单请参见[设置分布式事务白名单](~~124321~~)。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDTCSecurityIpHostsForSQLServerResponse().from_map(self.do_request("DescribeDTCSecurityIpHostsForSQLServer", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        """
        DescribeDTCSecurityIpHostsForSQLServer 调用DescribeDTCSecurityIpHostsForSQLServer接口查询RDS实例的分布式事务白名单信息。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeDTCSecurityIpHostsForSQLServer
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 关于分布式事务白名单请参见[设置分布式事务白名单](~~124321~~)。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(self, request, runtime):
        """
        ModifyDTCSecurityIpHostsForSQLServer 调用ModifyDTCSecurityIpHostsForSQLServer接口设置分布式事务白名单。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=ModifyDTCSecurityIpHostsForSQLServer
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &SecurityIpHosts=192.168.1.100,k3ecstest
        &WhiteListGroupName=test1
        &<公共请求参数>
        ```
        description:   * 分布式事务白名单可以让ECS实例和RDS实例之间支持分布式事务。详情请参见[设置分布式事务白名单](~~124321~~)。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDTCSecurityIpHostsForSQLServerResponse().from_map(self.do_request("ModifyDTCSecurityIpHostsForSQLServer", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dtcsecurity_ip_hosts_for_sqlserver(self, request):
        """
        ModifyDTCSecurityIpHostsForSQLServer 调用ModifyDTCSecurityIpHostsForSQLServer接口设置分布式事务白名单。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=ModifyDTCSecurityIpHostsForSQLServer
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &SecurityIpHosts=192.168.1.100,k3ecstest
        &WhiteListGroupName=test1
        &<公共请求参数>
        ```
        description:   * 分布式事务白名单可以让ECS实例和RDS实例之间支持分布式事务。详情请参见[设置分布式事务白名单](~~124321~~)。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dtcsecurity_ip_hosts_for_sqlserver_with_options(request, runtime)

    def describe_dbinstance_ip_hostname_with_options(self, request, runtime):
        """
        DescribeDBInstanceIpHostname 调用DescribeDBInstanceIpHostname接口查询RDS实例的底层ECS实例的hostname。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeDBInstanceIpHostname
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * RDS实例是基于ECS实例搭建的，本接口用于[设置分布式事务白名单](~~124321~~)时查询RDS实例的底层ECS实例的hostname。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceIpHostnameResponse().from_map(self.do_request("DescribeDBInstanceIpHostname", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_ip_hostname(self, request):
        """
        DescribeDBInstanceIpHostname 调用DescribeDBInstanceIpHostname接口查询RDS实例的底层ECS实例的hostname。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeDBInstanceIpHostname
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * RDS实例是基于ECS实例搭建的，本接口用于[设置分布式事务白名单](~~124321~~)时查询RDS实例的底层ECS实例的hostname。
        仅适用于如下版本实例：
        * SQL Server 2012/2016企业版高可用版
        * SQL Server 2012/2016标准版
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_ip_hostname_with_options(request, runtime)

    def modify_dbinstance_auto_upgrade_minor_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceAutoUpgradeMinorVersionResponse().from_map(self.do_request("ModifyDBInstanceAutoUpgradeMinorVersion", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_auto_upgrade_minor_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_auto_upgrade_minor_version_with_options(request, runtime)

    def describe_available_cross_region_with_options(self, request, runtime):
        """
        DescribeAvailableCrossRegion 调用DescribeAvailableCrossRegion接口查询所选地域当前可以进行跨地域备份的目的地域。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeAvailableCrossRegion
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableCrossRegionResponse().from_map(self.do_request("DescribeAvailableCrossRegion", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_cross_region(self, request):
        """
        DescribeAvailableCrossRegion 调用DescribeAvailableCrossRegion接口查询所选地域当前可以进行跨地域备份的目的地域。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeAvailableCrossRegion
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_cross_region_with_options(request, runtime)

    def check_create_ddr_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckCreateDdrDBInstanceResponse().from_map(self.do_request("CheckCreateDdrDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_create_ddr_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_create_ddr_dbinstance_with_options(request, runtime)

    def describe_available_recovery_time_with_options(self, request, runtime):
        """
        DescribeAvailableRecoveryTime 调用DescribeAvailableRecoveryTime接口查询某跨地域备份文件可恢复哪个时间段的数据。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeAvailableRecoveryTime
        &CrossBackupId=14377
        &<公共请求参数>
        ```
        description:   * 查看普通备份文件可恢复哪个时间段的数据请参见[DescribeBackups](~~26273~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableRecoveryTimeResponse().from_map(self.do_request("DescribeAvailableRecoveryTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_recovery_time(self, request):
        """
        DescribeAvailableRecoveryTime 调用DescribeAvailableRecoveryTime接口查询某跨地域备份文件可恢复哪个时间段的数据。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeAvailableRecoveryTime
        &CrossBackupId=14377
        &<公共请求参数>
        ```
        description:   * 查看普通备份文件可恢复哪个时间段的数据请参见[DescribeBackups](~~26273~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_recovery_time_with_options(request, runtime)

    def describe_cross_region_log_backup_files_with_options(self, request, runtime):
        """
        DescribeCrossRegionLogBackupFiles 调用DescribeCrossRegionLogBackupFiles接口查看跨地域日志备份文件列表。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeCrossRegionLogBackupFiles
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &StartTime=2019-05-30T12:10Z
        &EndTime=2019-06-15T12:10Z
        &<公共请求参数>
        ```
        description:   * 查看数据备份文件请参见[DescribeCrossRegionBackups](~~121733~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCrossRegionLogBackupFilesResponse().from_map(self.do_request("DescribeCrossRegionLogBackupFiles", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_cross_region_log_backup_files(self, request):
        """
        DescribeCrossRegionLogBackupFiles 调用DescribeCrossRegionLogBackupFiles接口查看跨地域日志备份文件列表。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeCrossRegionLogBackupFiles
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &StartTime=2019-05-30T12:10Z
        &EndTime=2019-06-15T12:10Z
        &<公共请求参数>
        ```
        description:   * 查看数据备份文件请参见[DescribeCrossRegionBackups](~~121733~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_log_backup_files_with_options(request, runtime)

    def modify_instance_cross_backup_policy_with_options(self, request, runtime):
        """
        ModifyInstanceCrossBackupPolicy 调用ModifyInstanceCrossBackupPolicy接口修改RDS跨地域备份设置。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=ModifyInstanceCrossBackupPolicy
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyInstanceCrossBackupPolicyResponse().from_map(self.do_request("ModifyInstanceCrossBackupPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_instance_cross_backup_policy(self, request):
        """
        ModifyInstanceCrossBackupPolicy 调用ModifyInstanceCrossBackupPolicy接口修改RDS跨地域备份设置。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=ModifyInstanceCrossBackupPolicy
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_cross_backup_policy_with_options(request, runtime)

    def create_ddr_instance_with_options(self, request, runtime):
        """
        CreateDdrInstance 调用CreateDdrInstance接口跨地域恢复数据到新实例。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action==CreateDdrInstance
        &RegionId=cn-hangzhou
        &Engine=MySQL
        &EngineVersion=5.6
        &DBInstanceClass=rds.mysql.s1.small
        &DBInstanceStorage=20
        &DBInstanceNetType=Intranet
        &PayType=Prepaid
        &RestoreType=0
        &SecurityIPList=127.0.0.1
        &BackupSetId=14358
        &<公共请求参数>
        ```
        description:   * 恢复前可以调用[CheckCreateDdrDBInstance](~~121721~~)接口预检查某RDS实例是否可以用跨地域备份集进行跨地域恢复。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDdrInstanceResponse().from_map(self.do_request("CreateDdrInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_ddr_instance(self, request):
        """
        CreateDdrInstance 调用CreateDdrInstance接口跨地域恢复数据到新实例。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action==CreateDdrInstance
        &RegionId=cn-hangzhou
        &Engine=MySQL
        &EngineVersion=5.6
        &DBInstanceClass=rds.mysql.s1.small
        &DBInstanceStorage=20
        &DBInstanceNetType=Intranet
        &PayType=Prepaid
        &RestoreType=0
        &SecurityIPList=127.0.0.1
        &BackupSetId=14358
        &<公共请求参数>
        ```
        description:   * 恢复前可以调用[CheckCreateDdrDBInstance](~~121721~~)接口预检查某RDS实例是否可以用跨地域备份集进行跨地域恢复。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.create_ddr_instance_with_options(request, runtime)

    def describe_cross_region_backup_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCrossRegionBackupDBInstanceResponse().from_map(self.do_request("DescribeCrossRegionBackupDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_cross_region_backup_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backup_dbinstance_with_options(request, runtime)

    def describe_instance_cross_backup_policy_with_options(self, request, runtime):
        """
        DescribeInstanceCrossBackupPolicy 调用DescribeInstanceCrossBackupPolicy接口查询跨地域备份设置。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeInstanceCrossBackupPolicy
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &<公共请求参数>
        ```
        description:   * 仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeInstanceCrossBackupPolicyResponse().from_map(self.do_request("DescribeInstanceCrossBackupPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_instance_cross_backup_policy(self, request):
        """
        DescribeInstanceCrossBackupPolicy 调用DescribeInstanceCrossBackupPolicy接口查询跨地域备份设置。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeInstanceCrossBackupPolicy
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &<公共请求参数>
        ```
        description:   * 仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_cross_backup_policy_with_options(request, runtime)

    def describe_cross_region_backups_with_options(self, request, runtime):
        """
        DescribeCrossRegionBackups 调用DescribeCrossRegionBackups接口查看某RDS实例跨地域数据备份文件列表。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeCrossRegionBackups
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &CrossBackupId=14562
        &<公共请求参数>
        ```
        description:   * 查看日志备份文件请参见[DescribeCrossRegionLogBackupFiles](~~121734~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCrossRegionBackupsResponse().from_map(self.do_request("DescribeCrossRegionBackups", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_cross_region_backups(self, request):
        """
        DescribeCrossRegionBackups 调用DescribeCrossRegionBackups接口查看某RDS实例跨地域数据备份文件列表。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeCrossRegionBackups
        &DBInstanceId=rm-uf6wjk5xxxxxxxxxx
        &CrossBackupId=14562
        &<公共请求参数>
        ```
        description:   * 查看日志备份文件请参见[DescribeCrossRegionLogBackupFiles](~~121734~~)。
        仅适用于如下实例：
        * MySQL 5.7高可用本地SSD盘版
        * MySQL 5.6
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_region_backups_with_options(request, runtime)

    def check_cloud_resource_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckCloudResourceAuthorizedResponse().from_map(self.do_request("CheckCloudResourceAuthorized", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_cloud_resource_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_cloud_resource_authorized_with_options(request, runtime)

    def describe_read_dbinstance_delay_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeReadDBInstanceDelayResponse().from_map(self.do_request("DescribeReadDBInstanceDelay", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_read_dbinstance_delay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_read_dbinstance_delay_with_options(request, runtime)

    def restore_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RestoreTableResponse().from_map(self.do_request("RestoreTable", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def restore_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restore_table_with_options(request, runtime)

    def create_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateParameterGroupResponse().from_map(self.do_request("CreateParameterGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parameter_group_with_options(request, runtime)

    def describe_parameter_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeParameterGroupsResponse().from_map(self.do_request("DescribeParameterGroups", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_parameter_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_groups_with_options(request, runtime)

    def clone_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CloneParameterGroupResponse().from_map(self.do_request("CloneParameterGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def clone_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_parameter_group_with_options(request, runtime)

    def describe_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeParameterGroupResponse().from_map(self.do_request("DescribeParameterGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_group_with_options(request, runtime)

    def modify_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyParameterGroupResponse().from_map(self.do_request("ModifyParameterGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_group_with_options(request, runtime)

    def delete_parameter_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteParameterGroupResponse().from_map(self.do_request("DeleteParameterGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_parameter_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parameter_group_with_options(request, runtime)

    def modify_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifySQLCollectorRetentionResponse().from_map(self.do_request("ModifySQLCollectorRetention", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_retention_with_options(request, runtime)

    def describe_sqlcollector_retention_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLCollectorRetentionResponse().from_map(self.do_request("DescribeSQLCollectorRetention", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqlcollector_retention(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_retention_with_options(request, runtime)

    def check_instance_exist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckInstanceExistResponse().from_map(self.do_request("CheckInstanceExist", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_instance_exist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_instance_exist_with_options(request, runtime)

    def describe_log_backup_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeLogBackupFilesResponse().from_map(self.do_request("DescribeLogBackupFiles", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_log_backup_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_log_backup_files_with_options(request, runtime)

    def migrate_security_ipmode_with_options(self, request, runtime):
        """
        MigrateSecurityIPMode You can call this operation to switch a whitelist from normal mode to safe mode.
        request demo:   * http(s)://rds.aliyuncs.com/? Action=MigrateSecurityIPMode
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &<Common request parameters>
        description:   * * In normal mode, IP addresses in the whitelist apply to both classic networks and VPCs. In case of security risks, we recommend that you switch to safe mode.
        * In safe mode, IP addresses in the whitelist are divided into VPC IP addresses and the IP addresses of classic networks and public networks.
        >
        * Safe mode cannot be switched to normal mode.
        * This operation is not applicable to SQL Server and MariaDB instances.
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.MigrateSecurityIPModeResponse().from_map(self.do_request("MigrateSecurityIPMode", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def migrate_security_ipmode(self, request):
        """
        MigrateSecurityIPMode You can call this operation to switch a whitelist from normal mode to safe mode.
        request demo:   * http(s)://rds.aliyuncs.com/? Action=MigrateSecurityIPMode
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &<Common request parameters>
        description:   * * In normal mode, IP addresses in the whitelist apply to both classic networks and VPCs. In case of security risks, we recommend that you switch to safe mode.
        * In safe mode, IP addresses in the whitelist are divided into VPC IP addresses and the IP addresses of classic networks and public networks.
        >
        * Safe mode cannot be switched to normal mode.
        * This operation is not applicable to SQL Server and MariaDB instances.
        """
        runtime = util_models.RuntimeOptions()
        return self.migrate_security_ipmode_with_options(request, runtime)

    def switch_dbinstance_vpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.SwitchDBInstanceVpcResponse().from_map(self.do_request("SwitchDBInstanceVpc", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def switch_dbinstance_vpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_vpc_with_options(request, runtime)

    def describe_collation_time_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCollationTimeZonesResponse().from_map(self.do_request("DescribeCollationTimeZones", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_collation_time_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_collation_time_zones_with_options(request, runtime)

    def describe_instance_keywords_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeInstanceKeywordsResponse().from_map(self.do_request("DescribeInstanceKeywords", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_instance_keywords(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_keywords_with_options(request, runtime)

    def modify_collation_time_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyCollationTimeZoneResponse().from_map(self.do_request("ModifyCollationTimeZone", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_collation_time_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_collation_time_zone_with_options(request, runtime)

    def describe_backup_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeBackupDatabaseResponse().from_map(self.do_request("DescribeBackupDatabase", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_backup_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_database_with_options(request, runtime)

    def copy_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CopyDatabaseBetweenInstancesResponse().from_map(self.do_request("CopyDatabaseBetweenInstances", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def copy_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_between_instances_with_options(request, runtime)

    def recovery_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RecoveryDBInstanceResponse().from_map(self.do_request("RecoveryDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def recovery_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recovery_dbinstance_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAvailableResourceResponse().from_map(self.do_request("DescribeAvailableResource", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def destroy_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DestroyDBInstanceResponse().from_map(self.do_request("DestroyDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def destroy_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.destroy_dbinstance_with_options(request, runtime)

    def modify_readonly_instance_delay_replication_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyReadonlyInstanceDelayReplicationTimeResponse().from_map(self.do_request("ModifyReadonlyInstanceDelayReplicationTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_readonly_instance_delay_replication_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_readonly_instance_delay_replication_time_with_options(request, runtime)

    def describe_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceProxyConfigurationResponse().from_map(self.do_request("DescribeDBInstanceProxyConfiguration", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_proxy_configuration_with_options(request, runtime)

    def create_online_database_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateOnlineDatabaseTaskResponse().from_map(self.do_request("CreateOnlineDatabaseTask", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_online_database_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_online_database_task_with_options(request, runtime)

    def upgrade_dbinstance_kernel_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.UpgradeDBInstanceKernelVersionResponse().from_map(self.do_request("UpgradeDBInstanceKernelVersion", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def upgrade_dbinstance_kernel_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_kernel_version_with_options(request, runtime)

    def modify_dbinstance_proxy_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceProxyConfigurationResponse().from_map(self.do_request("ModifyDBInstanceProxyConfiguration", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_proxy_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_proxy_configuration_with_options(request, runtime)

    def describe_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSecurityGroupConfigurationResponse().from_map(self.do_request("DescribeSecurityGroupConfiguration", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_configuration_with_options(request, runtime)

    def modify_security_group_configuration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifySecurityGroupConfigurationResponse().from_map(self.do_request("ModifySecurityGroupConfiguration", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_security_group_configuration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_group_configuration_with_options(request, runtime)

    def describe_oss_downloads_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeOssDownloadsForSQLServerResponse().from_map(self.do_request("DescribeOssDownloadsForSQLServer", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_oss_downloads_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_for_sqlserver_with_options(request, runtime)

    def describe_migrate_tasks_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeMigrateTasksForSQLServerResponse().from_map(self.do_request("DescribeMigrateTasksForSQLServer", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_migrate_tasks_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_for_sqlserver_with_options(request, runtime)

    def create_migrate_task_for_sqlserver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateMigrateTaskForSQLServerResponse().from_map(self.do_request("CreateMigrateTaskForSQLServer", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_migrate_task_for_sqlserver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_for_sqlserver_with_options(request, runtime)

    def create_migrate_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateMigrateTaskResponse().from_map(self.do_request("CreateMigrateTask", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_migrate_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_migrate_task_with_options(request, runtime)

    def describe_oss_downloads_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeOssDownloadsResponse().from_map(self.do_request("DescribeOssDownloads", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_oss_downloads(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_oss_downloads_with_options(request, runtime)

    def describe_migrate_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeMigrateTasksResponse().from_map(self.do_request("DescribeMigrateTasks", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_migrate_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_migrate_tasks_with_options(request, runtime)

    def copy_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CopyDatabaseResponse().from_map(self.do_request("CopyDatabase", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def copy_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_database_with_options(request, runtime)

    def reset_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ResetAccountResponse().from_map(self.do_request("ResetAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def reset_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_with_options(request, runtime)

    def describe_dbinstances_as_csv_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesAsCsvResponse().from_map(self.do_request("DescribeDBInstancesAsCsv", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances_as_csv(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_as_csv_with_options(request, runtime)

    def modify_dbinstance_network_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceNetworkExpireTimeResponse().from_map(self.do_request("ModifyDBInstanceNetworkExpireTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_network_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_expire_time_with_options(request, runtime)

    def modify_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyResourceGroupResponse().from_map(self.do_request("ModifyResourceGroup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_group_with_options(request, runtime)

    def describe_renewal_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeRenewalPriceResponse().from_map(self.do_request("DescribeRenewalPrice", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_renewal_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_renewal_price_with_options(request, runtime)

    def describe_price_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribePriceResponse().from_map(self.do_request("DescribePrice", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_price(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_price_with_options(request, runtime)

    def renew_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RenewInstanceResponse().from_map(self.do_request("RenewInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def renew_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    def check_recovery_conditions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckRecoveryConditionsResponse().from_map(self.do_request("CheckRecoveryConditions", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_recovery_conditions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_recovery_conditions_with_options(request, runtime)

    def modify_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyInstanceAutoRenewalAttributeResponse().from_map(self.do_request("ModifyInstanceAutoRenewalAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_auto_renewal_attribute_with_options(request, runtime)

    def describe_instance_auto_renewal_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeInstanceAutoRenewalAttributeResponse().from_map(self.do_request("DescribeInstanceAutoRenewalAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_instance_auto_renewal_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_auto_renewal_attribute_with_options(request, runtime)

    def release_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ReleaseReadWriteSplittingConnectionResponse().from_map(self.do_request("ReleaseReadWriteSplittingConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def release_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_read_write_splitting_connection_with_options(request, runtime)

    def modify_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyReadWriteSplittingConnectionResponse().from_map(self.do_request("ModifyReadWriteSplittingConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_read_write_splitting_connection_with_options(request, runtime)

    def calculate_dbinstance_weight_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CalculateDBInstanceWeightResponse().from_map(self.do_request("CalculateDBInstanceWeight", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def calculate_dbinstance_weight(self, request):
        runtime = util_models.RuntimeOptions()
        return self.calculate_dbinstance_weight_with_options(request, runtime)

    def allocate_read_write_splitting_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.AllocateReadWriteSplittingConnectionResponse().from_map(self.do_request("AllocateReadWriteSplittingConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def allocate_read_write_splitting_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_read_write_splitting_connection_with_options(request, runtime)

    def modify_dbinstance_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstancePayTypeResponse().from_map(self.do_request("ModifyDBInstancePayType", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_pay_type_with_options(request, runtime)

    def describe_character_set_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeCharacterSetNameResponse().from_map(self.do_request("DescribeCharacterSetName", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_character_set_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_character_set_name_with_options(request, runtime)

    def delete_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteBackupResponse().from_map(self.do_request("DeleteBackup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    def describe_diagnostic_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDiagnosticReportListResponse().from_map(self.do_request("DescribeDiagnosticReportList", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_diagnostic_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_report_list_with_options(request, runtime)

    def create_diagnostic_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDiagnosticReportResponse().from_map(self.do_request("CreateDiagnosticReport", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_diagnostic_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_report_with_options(request, runtime)

    def clone_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CloneDBInstanceResponse().from_map(self.do_request("CloneDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def clone_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_dbinstance_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        """
        DescribeTags 调用DescribeTags接口查询RDS实例的标签。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeTags
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 调用本接口时限制条件如下：
        * 如果传入指定实例ID，则查询该实例下所有标签，其他过滤条件失效；
        * 若查询标签时仅传入标签键（TagKey），未传入标签值（TagValue），则返回所有符合标签键条件的结果。若同时传入标签键和标签值，则返回两个条件都符合的结果。
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeTagsResponse().from_map(self.do_request("DescribeTags", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_tags(self, request):
        """
        DescribeTags 调用DescribeTags接口查询RDS实例的标签。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=DescribeTags
        &RegionId=cn-hangzhou
        &<公共请求参数>
        ```
        description:   * 调用本接口时限制条件如下：
        * 如果传入指定实例ID，则查询该实例下所有标签，其他过滤条件失效；
        * 若查询标签时仅传入标签键（TagKey），未传入标签值（TagValue），则返回所有符合标签键条件的结果。若同时传入标签键和标签值，则返回两个条件都符合的结果。
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_dbinstance_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceByTagsResponse().from_map(self.do_request("DescribeDBInstanceByTags", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_by_tags_with_options(request, runtime)

    def revoke_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RevokeOperatorPermissionResponse().from_map(self.do_request("RevokeOperatorPermission", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def revoke_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_operator_permission_with_options(request, runtime)

    def modify_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceTDEResponse().from_map(self.do_request("ModifyDBInstanceTDE", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_tdewith_options(request, runtime)

    def modify_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceSSLResponse().from_map(self.do_request("ModifyDBInstanceSSL", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_sslwith_options(request, runtime)

    def grant_operator_permission_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.GrantOperatorPermissionResponse().from_map(self.do_request("GrantOperatorPermission", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def grant_operator_permission(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_operator_permission_with_options(request, runtime)

    def describe_dbinstance_tdewith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceTDEResponse().from_map(self.do_request("DescribeDBInstanceTDE", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_tde(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_tdewith_options(request, runtime)

    def describe_dbinstance_sslwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceSSLResponse().from_map(self.do_request("DescribeDBInstanceSSL", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_ssl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_sslwith_options(request, runtime)

    def describe_sqllog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLLogFilesResponse().from_map(self.do_request("DescribeSQLLogFiles", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqllog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_files_with_options(request, runtime)

    def modify_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceMonitorResponse().from_map(self.do_request("ModifyDBInstanceMonitor", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_monitor_with_options(request, runtime)

    def switch_dbinstance_hawith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.SwitchDBInstanceHAResponse().from_map(self.do_request("SwitchDBInstanceHA", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def switch_dbinstance_ha(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_hawith_options(request, runtime)

    def describe_dbinstance_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceMonitorResponse().from_map(self.do_request("DescribeDBInstanceMonitor", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_monitor_with_options(request, runtime)

    def describe_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLCollectorPolicyResponse().from_map(self.do_request("DescribeSQLCollectorPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlcollector_policy_with_options(request, runtime)

    def modify_sqlcollector_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifySQLCollectorPolicyResponse().from_map(self.do_request("ModifySQLCollectorPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_sqlcollector_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sqlcollector_policy_with_options(request, runtime)

    def modify_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceHAConfigResponse().from_map(self.do_request("ModifyDBInstanceHAConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_haconfig_with_options(request, runtime)

    def describe_dbinstance_haconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceHAConfigResponse().from_map(self.do_request("DescribeDBInstanceHAConfig", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_haconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_haconfig_with_options(request, runtime)

    def describe_sqlreports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLReportsResponse().from_map(self.do_request("DescribeSQLReports", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqlreports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqlreports_with_options(request, runtime)

    def describe_dbinstance_iparray_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceIPArrayListResponse().from_map(self.do_request("DescribeDBInstanceIPArrayList", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_iparray_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_iparray_list_with_options(request, runtime)

    def describe_sqllog_report_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLLogReportListResponse().from_map(self.do_request("DescribeSQLLogReportList", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqllog_report_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_report_list_with_options(request, runtime)

    def reset_account_for_pgwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ResetAccountForPGResponse().from_map(self.do_request("ResetAccountForPG", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def reset_account_for_pg(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_for_pgwith_options(request, runtime)

    def upgrade_dbinstance_engine_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.UpgradeDBInstanceEngineVersionResponse().from_map(self.do_request("UpgradeDBInstanceEngineVersion", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def upgrade_dbinstance_engine_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_dbinstance_engine_version_with_options(request, runtime)

    def revoke_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RevokeAccountPrivilegeResponse().from_map(self.do_request("RevokeAccountPrivilege", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def revoke_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_account_privilege_with_options(request, runtime)

    def restart_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.RestartDBInstanceResponse().from_map(self.do_request("RestartDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def restart_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ResetAccountPasswordResponse().from_map(self.do_request("ResetAccountPassword", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def remove_tags_from_resource_with_options(self, request, runtime):
        """
        RemoveTagsFromResource 调用RemoveTagsFromResource接口解绑标签。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=RemoveTagsFromResource
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &Tag.1.key=test
        &<公共请求参数>
        ```
        description:   * 限制条件如下：
        * 单次最多支持解绑10个标签；
        * 若一个标签所绑定的实例全都解绑，则该标签自动删除；
        * 若解绑标签时仅传入标签键（TagKey），未传入标签值（TagValue），则解绑所有符合标签键条件的标签。
        * 必须传入至少一组标签或者单独的一个标签键。
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.RemoveTagsFromResourceResponse().from_map(self.do_request("RemoveTagsFromResource", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def remove_tags_from_resource(self, request):
        """
        RemoveTagsFromResource 调用RemoveTagsFromResource接口解绑标签。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=RemoveTagsFromResource
        &DBInstanceId=rm-uf6wjk5xxxxxxx
        &RegionId=cn-hangzhou
        &Tag.1.key=test
        &<公共请求参数>
        ```
        description:   * 限制条件如下：
        * 单次最多支持解绑10个标签；
        * 若一个标签所绑定的实例全都解绑，则该标签自动删除；
        * 若解绑标签时仅传入标签键（TagKey），未传入标签值（TagValue），则解绑所有符合标签键条件的标签。
        * 必须传入至少一组标签或者单独的一个标签键。
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_from_resource_with_options(request, runtime)

    def purge_dbinstance_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.PurgeDBInstanceLogResponse().from_map(self.do_request("PurgeDBInstanceLog", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def purge_dbinstance_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.purge_dbinstance_log_with_options(request, runtime)

    def modify_security_ips_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifySecurityIpsResponse().from_map(self.do_request("ModifySecurityIps", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_security_ips(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_security_ips_with_options(request, runtime)

    def modify_parameter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyParameterResponse().from_map(self.do_request("ModifyParameter", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_parameter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parameter_with_options(request, runtime)

    def modify_dbinstance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceSpecResponse().from_map(self.do_request("ModifyDBInstanceSpec", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_spec_with_options(request, runtime)

    def modify_dbinstance_maintain_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceMaintainTimeResponse().from_map(self.do_request("ModifyDBInstanceMaintainTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_maintain_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_maintain_time_with_options(request, runtime)

    def modify_dbinstance_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceDescriptionResponse().from_map(self.do_request("ModifyDBInstanceDescription", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_description_with_options(request, runtime)

    def modify_dbdescription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBDescriptionResponse().from_map(self.do_request("ModifyDBDescription", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbdescription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbdescription_with_options(request, runtime)

    def modify_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyBackupPolicyResponse().from_map(self.do_request("ModifyBackupPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    def modify_account_description_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyAccountDescriptionResponse().from_map(self.do_request("ModifyAccountDescription", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_account_description(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    def migrate_to_other_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.MigrateToOtherZoneResponse().from_map(self.do_request("MigrateToOtherZone", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def migrate_to_other_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.migrate_to_other_zone_with_options(request, runtime)

    def import_database_between_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ImportDatabaseBetweenInstancesResponse().from_map(self.do_request("ImportDatabaseBetweenInstances", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def import_database_between_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_database_between_instances_with_options(request, runtime)

    def grant_account_privilege_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.GrantAccountPrivilegeResponse().from_map(self.do_request("GrantAccountPrivilege", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def grant_account_privilege(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_account_privilege_with_options(request, runtime)

    def describe_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeTasksResponse().from_map(self.do_request("DescribeTasks", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tasks_with_options(request, runtime)

    def describe_sqllog_reports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLLogReportsResponse().from_map(self.do_request("DescribeSQLLogReports", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqllog_reports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_reports_with_options(request, runtime)

    def describe_sqllog_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSQLLogRecordsResponse().from_map(self.do_request("DescribeSQLLogRecords", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_sqllog_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sqllog_records_with_options(request, runtime)

    def describe_slow_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSlowLogsResponse().from_map(self.do_request("DescribeSlowLogs", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_slow_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_logs_with_options(request, runtime)

    def describe_slow_log_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeSlowLogRecordsResponse().from_map(self.do_request("DescribeSlowLogRecords", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_slow_log_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    def describe_resource_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeResourceUsageResponse().from_map(self.do_request("DescribeResourceUsage", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_resource_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_resource_usage_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeRegionsResponse().from_map(self.do_request("DescribeRegions", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_parameter_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeParameterTemplatesResponse().from_map(self.do_request("DescribeParameterTemplates", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_parameter_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameter_templates_with_options(request, runtime)

    def describe_parameters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeParametersResponse().from_map(self.do_request("DescribeParameters", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_parameters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parameters_with_options(request, runtime)

    def describe_modify_parameter_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeModifyParameterLogResponse().from_map(self.do_request("DescribeModifyParameterLog", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_modify_parameter_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_modify_parameter_log_with_options(request, runtime)

    def describe_error_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeErrorLogsResponse().from_map(self.do_request("DescribeErrorLogs", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_error_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_error_logs_with_options(request, runtime)

    def describe_dbinstance_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancePerformanceResponse().from_map(self.do_request("DescribeDBInstancePerformance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_performance_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDatabasesResponse().from_map(self.do_request("DescribeDatabases", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_binlog_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeBinlogFilesResponse().from_map(self.do_request("DescribeBinlogFiles", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_binlog_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_binlog_files_with_options(request, runtime)

    def describe_backup_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeBackupTasksResponse().from_map(self.do_request("DescribeBackupTasks", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_backup_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_tasks_with_options(request, runtime)

    def describe_backups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeBackupsResponse().from_map(self.do_request("DescribeBackups", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_backups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    def describe_backup_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeBackupPolicyResponse().from_map(self.do_request("DescribeBackupPolicy", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_backup_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    def describe_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeAccountsResponse().from_map(self.do_request("DescribeAccounts", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    def descibe_imports_from_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescibeImportsFromDatabaseResponse().from_map(self.do_request("DescibeImportsFromDatabase", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def descibe_imports_from_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.descibe_imports_from_database_with_options(request, runtime)

    def delete_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteDBInstanceResponse().from_map(self.do_request("DeleteDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    def delete_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteDatabaseResponse().from_map(self.do_request("DeleteDatabase", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    def delete_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DeleteAccountResponse().from_map(self.do_request("DeleteAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def create_temp_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateTempDBInstanceResponse().from_map(self.do_request("CreateTempDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_temp_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_temp_dbinstance_with_options(request, runtime)

    def create_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDatabaseResponse().from_map(self.do_request("CreateDatabase", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_database_with_options(request, runtime)

    def create_backup_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateBackupResponse().from_map(self.do_request("CreateBackup", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_backup(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateAccountResponse().from_map(self.do_request("CreateAccount", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def check_dbname_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckDBNameAvailableResponse().from_map(self.do_request("CheckDBNameAvailable", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_dbname_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_dbname_available_with_options(request, runtime)

    def check_account_name_available_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CheckAccountNameAvailableResponse().from_map(self.do_request("CheckAccountNameAvailable", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def check_account_name_available(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_account_name_available_with_options(request, runtime)

    def cancel_import_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CancelImportResponse().from_map(self.do_request("CancelImport", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def cancel_import(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_import_with_options(request, runtime)

    def add_tags_to_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.AddTagsToResourceResponse().from_map(self.do_request("AddTagsToResource", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def add_tags_to_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_to_resource_with_options(request, runtime)

    def switch_dbinstance_net_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.SwitchDBInstanceNetTypeResponse().from_map(self.do_request("SwitchDBInstanceNetType", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def switch_dbinstance_net_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_dbinstance_net_type_with_options(request, runtime)

    def release_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ReleaseInstancePublicConnectionResponse().from_map(self.do_request("ReleaseInstancePublicConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def release_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_public_connection_with_options(request, runtime)

    def modify_dbinstance_network_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceNetworkTypeResponse().from_map(self.do_request("ModifyDBInstanceNetworkType", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_network_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_network_type_with_options(request, runtime)

    def modify_dbinstance_connection_string_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceConnectionStringResponse().from_map(self.do_request("ModifyDBInstanceConnectionString", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_connection_string(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    def modify_dbinstance_connection_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.ModifyDBInstanceConnectionModeResponse().from_map(self.do_request("ModifyDBInstanceConnectionMode", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def modify_dbinstance_connection_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_mode_with_options(request, runtime)

    def describe_dbinstance_net_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceNetInfoResponse().from_map(self.do_request("DescribeDBInstanceNetInfo", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_net_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_net_info_with_options(request, runtime)

    def create_read_only_dbinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateReadOnlyDBInstanceResponse().from_map(self.do_request("CreateReadOnlyDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_read_only_dbinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_read_only_dbinstance_with_options(request, runtime)

    def create_dbinstance_with_options(self, request, runtime):
        """
        CreateDBInstance 调用CreateDBInstance接口创建一个RDS实例。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=CreateDBInstance
        &RegionId=cn-hangzhou
        &Engine=MySQL
        &EngineVersion=5.6
        &DBInstanceClass=rds.mysql.s1.small
        &DBInstanceStorage=20
        &DBInstanceNetType=Internet
        &PayType=Postpaid
        &SecurityIPList=10.23.12.27/24
        &<公共请求参数>
        ```
        description:   * **请确保在使用该接口前，已充分了解RDS产品的收费方式和<xref href="https://www.alibabacloud.com/product/apsaradb-for-rds#pricing" format="html" scope="external" props="intl">价格</xref><xref href="https://www.aliyun.com/price/product#/rds/detail" format="html" scope="external" props="china">价格</xref>。**\
        关于RDS实例的规格，请参见[实例规格表](~~26312~~)。
        """
        UtilClient.validate_model(request)
        return rds_20140815_models.CreateDBInstanceResponse().from_map(self.do_request("CreateDBInstance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def create_dbinstance(self, request):
        """
        CreateDBInstance 调用CreateDBInstance接口创建一个RDS实例。
        request demo:   * ```
        http(s)://rds.aliyuncs.com/?Action=CreateDBInstance
        &RegionId=cn-hangzhou
        &Engine=MySQL
        &EngineVersion=5.6
        &DBInstanceClass=rds.mysql.s1.small
        &DBInstanceStorage=20
        &DBInstanceNetType=Internet
        &PayType=Postpaid
        &SecurityIPList=10.23.12.27/24
        &<公共请求参数>
        ```
        description:   * **请确保在使用该接口前，已充分了解RDS产品的收费方式和<xref href="https://www.alibabacloud.com/product/apsaradb-for-rds#pricing" format="html" scope="external" props="intl">价格</xref><xref href="https://www.aliyun.com/price/product#/rds/detail" format="html" scope="external" props="china">价格</xref>。**\
        关于RDS实例的规格，请参见[实例规格表](~~26312~~)。
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    def allocate_instance_public_connection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.AllocateInstancePublicConnectionResponse().from_map(self.do_request("AllocateInstancePublicConnection", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def allocate_instance_public_connection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_instance_public_connection_with_options(request, runtime)

    def describe_dbinstances_by_performance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesByPerformanceResponse().from_map(self.do_request("DescribeDBInstancesByPerformance", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances_by_performance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_performance_with_options(request, runtime)

    def describe_dbinstances_by_expire_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesByExpireTimeResponse().from_map(self.do_request("DescribeDBInstancesByExpireTime", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances_by_expire_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_by_expire_time_with_options(request, runtime)

    def describe_dbinstances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstancesResponse().from_map(self.do_request("DescribeDBInstances", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    def describe_dbinstance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return rds_20140815_models.DescribeDBInstanceAttributeResponse().from_map(self.do_request("DescribeDBInstanceAttribute", "HTTPS", "POST", "2014-08-15", "AK", None, request.to_map(), runtime))

    def describe_dbinstance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
