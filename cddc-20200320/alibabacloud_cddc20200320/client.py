# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cddc20200320 import models as cddc_20200320_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cddc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def modify_dbinstance_switch_weight_with_options(
        self,
        request: cddc_20200320_models.ModifyDBInstanceSwitchWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse(),
            self.do_rpcrequest('ModifyDBInstanceSwitchWeight', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dbinstance_switch_weight_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDBInstanceSwitchWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse(),
            await self.do_rpcrequest_async('ModifyDBInstanceSwitchWeight', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dbinstance_switch_weight(
        self,
        request: cddc_20200320_models.ModifyDBInstanceSwitchWeightRequest,
    ) -> cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_switch_weight_with_options(request, runtime)

    async def modify_dbinstance_switch_weight_async(
        self,
        request: cddc_20200320_models.ModifyDBInstanceSwitchWeightRequest,
    ) -> cddc_20200320_models.ModifyDBInstanceSwitchWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_switch_weight_with_options_async(request, runtime)

    def describe_available_dedicated_host_zones_with_options(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostZones', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_dedicated_host_zones_with_options_async(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse(),
            await self.do_rpcrequest_async('DescribeAvailableDedicatedHostZones', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_zones(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_zones_with_options(request, runtime)

    async def describe_available_dedicated_host_zones_async(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostZonesRequest,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_zones_with_options_async(request, runtime)

    def describe_dedicated_host_groups_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostGroupsResponse(),
            self.do_rpcrequest('DescribeDedicatedHostGroups', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_groups_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostGroupsResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostGroups', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_groups(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_groups_with_options(request, runtime)

    async def describe_dedicated_host_groups_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostGroupsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_groups_with_options_async(request, runtime)

    def describe_my_base_host_over_view_with_options(
        self,
        request: cddc_20200320_models.DescribeMyBaseHostOverViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeMyBaseHostOverViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseHostOverViewResponse(),
            self.do_rpcrequest('DescribeMyBaseHostOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_my_base_host_over_view_with_options_async(
        self,
        request: cddc_20200320_models.DescribeMyBaseHostOverViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeMyBaseHostOverViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseHostOverViewResponse(),
            await self.do_rpcrequest_async('DescribeMyBaseHostOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_my_base_host_over_view(
        self,
        request: cddc_20200320_models.DescribeMyBaseHostOverViewRequest,
    ) -> cddc_20200320_models.DescribeMyBaseHostOverViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_base_host_over_view_with_options(request, runtime)

    async def describe_my_base_host_over_view_async(
        self,
        request: cddc_20200320_models.DescribeMyBaseHostOverViewRequest,
    ) -> cddc_20200320_models.DescribeMyBaseHostOverViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_base_host_over_view_with_options_async(request, runtime)

    def describe_brief_dedicated_hosts_with_options(
        self,
        request: cddc_20200320_models.DescribeBriefDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeBriefDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeBriefDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeBriefDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_brief_dedicated_hosts_with_options_async(
        self,
        request: cddc_20200320_models.DescribeBriefDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeBriefDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeBriefDedicatedHostsResponse(),
            await self.do_rpcrequest_async('DescribeBriefDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_brief_dedicated_hosts(
        self,
        request: cddc_20200320_models.DescribeBriefDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeBriefDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_brief_dedicated_hosts_with_options(request, runtime)

    async def describe_brief_dedicated_hosts_async(
        self,
        request: cddc_20200320_models.DescribeBriefDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeBriefDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_brief_dedicated_hosts_with_options_async(request, runtime)

    def describe_dedicated_resource_advisor_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedResourceAdvisorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse(),
            self.do_rpcrequest('DescribeDedicatedResourceAdvisor', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_resource_advisor_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedResourceAdvisorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedResourceAdvisor', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_resource_advisor(
        self,
        request: cddc_20200320_models.DescribeDedicatedResourceAdvisorRequest,
    ) -> cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_resource_advisor_with_options(request, runtime)

    async def describe_dedicated_resource_advisor_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedResourceAdvisorRequest,
    ) -> cddc_20200320_models.DescribeDedicatedResourceAdvisorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_resource_advisor_with_options_async(request, runtime)

    def describe_list_user_backup_file_record_with_options(
        self,
        request: cddc_20200320_models.DescribeListUserBackupFileRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeListUserBackupFileRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeListUserBackupFileRecordResponse(),
            self.do_rpcrequest('DescribeListUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_list_user_backup_file_record_with_options_async(
        self,
        request: cddc_20200320_models.DescribeListUserBackupFileRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeListUserBackupFileRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeListUserBackupFileRecordResponse(),
            await self.do_rpcrequest_async('DescribeListUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_list_user_backup_file_record(
        self,
        request: cddc_20200320_models.DescribeListUserBackupFileRecordRequest,
    ) -> cddc_20200320_models.DescribeListUserBackupFileRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_list_user_backup_file_record_with_options(request, runtime)

    async def describe_list_user_backup_file_record_async(
        self,
        request: cddc_20200320_models.DescribeListUserBackupFileRecordRequest,
    ) -> cddc_20200320_models.DescribeListUserBackupFileRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_list_user_backup_file_record_with_options_async(request, runtime)

    def create_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostAccountResponse(),
            self.do_rpcrequest('CreateDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostAccountResponse(),
            await self.do_rpcrequest_async('CreateDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_account(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_account_with_options(request, runtime)

    async def create_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostAccountResponse(),
            self.do_rpcrequest('DeleteDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostAccountResponse(),
            await self.do_rpcrequest_async('DeleteDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_account(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_account_with_options(request, runtime)

    async def delete_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_account_with_options_async(request, runtime)

    def delete_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostGroupResponse(),
            self.do_rpcrequest('DeleteDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dedicated_host_group_with_options_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteDedicatedHostGroupResponse(),
            await self.do_rpcrequest_async('DeleteDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dedicated_host_group(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dedicated_host_group_with_options(request, runtime)

    async def delete_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.DeleteDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.DeleteDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dedicated_host_group_with_options_async(request, runtime)

    def check_user_if_authorise_my_base_system_role_with_options(
        self,
        request: cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse(),
            self.do_rpcrequest('CheckUserIfAuthoriseMyBaseSystemRole', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_user_if_authorise_my_base_system_role_with_options_async(
        self,
        request: cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse(),
            await self.do_rpcrequest_async('CheckUserIfAuthoriseMyBaseSystemRole', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_user_if_authorise_my_base_system_role(
        self,
        request: cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleRequest,
    ) -> cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_user_if_authorise_my_base_system_role_with_options(request, runtime)

    async def check_user_if_authorise_my_base_system_role_async(
        self,
        request: cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleRequest,
    ) -> cddc_20200320_models.CheckUserIfAuthoriseMyBaseSystemRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_user_if_authorise_my_base_system_role_with_options_async(request, runtime)

    def describe_schedule_instance_with_options(
        self,
        request: cddc_20200320_models.DescribeScheduleInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleInstanceResponse(),
            self.do_rpcrequest('DescribeScheduleInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_schedule_instance_with_options_async(
        self,
        request: cddc_20200320_models.DescribeScheduleInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleInstanceResponse(),
            await self.do_rpcrequest_async('DescribeScheduleInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_instance(
        self,
        request: cddc_20200320_models.DescribeScheduleInstanceRequest,
    ) -> cddc_20200320_models.DescribeScheduleInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_instance_with_options(request, runtime)

    async def describe_schedule_instance_async(
        self,
        request: cddc_20200320_models.DescribeScheduleInstanceRequest,
    ) -> cddc_20200320_models.DescribeScheduleInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_instance_with_options_async(request, runtime)

    def excute_schedule_with_options(
        self,
        request: cddc_20200320_models.ExcuteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ExcuteScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ExcuteScheduleResponse(),
            self.do_rpcrequest('ExcuteSchedule', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def excute_schedule_with_options_async(
        self,
        request: cddc_20200320_models.ExcuteScheduleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ExcuteScheduleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ExcuteScheduleResponse(),
            await self.do_rpcrequest_async('ExcuteSchedule', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def excute_schedule(
        self,
        request: cddc_20200320_models.ExcuteScheduleRequest,
    ) -> cddc_20200320_models.ExcuteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return self.excute_schedule_with_options(request, runtime)

    async def excute_schedule_async(
        self,
        request: cddc_20200320_models.ExcuteScheduleRequest,
    ) -> cddc_20200320_models.ExcuteScheduleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.excute_schedule_with_options_async(request, runtime)

    def replace_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ReplaceDedicatedHostResponse(),
            self.do_rpcrequest('ReplaceDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def replace_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ReplaceDedicatedHostResponse(),
            await self.do_rpcrequest_async('ReplaceDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def replace_dedicated_host(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.replace_dedicated_host_with_options(request, runtime)

    async def replace_dedicated_host_async(
        self,
        request: cddc_20200320_models.ReplaceDedicatedHostRequest,
    ) -> cddc_20200320_models.ReplaceDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.replace_dedicated_host_with_options_async(request, runtime)

    def modify_dedicated_host_account_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAccountResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_account_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAccountResponse(),
            await self.do_rpcrequest_async('ModifyDedicatedHostAccount', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_account(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_account_with_options(request, runtime)

    async def modify_dedicated_host_account_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAccountRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_account_with_options_async(request, runtime)

    def describe_host_ecs_level_info_with_options(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostEcsLevelInfoResponse(),
            self.do_rpcrequest('DescribeHostEcsLevelInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_ecs_level_info_with_options_async(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostEcsLevelInfoResponse(),
            await self.do_rpcrequest_async('DescribeHostEcsLevelInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_ecs_level_info(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_ecs_level_info_with_options(request, runtime)

    async def describe_host_ecs_level_info_async(
        self,
        request: cddc_20200320_models.DescribeHostEcsLevelInfoRequest,
    ) -> cddc_20200320_models.DescribeHostEcsLevelInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_ecs_level_info_with_options_async(request, runtime)

    def allocate_host_instance_cross_vpc_vip_with_options(
        self,
        request: cddc_20200320_models.AllocateHostInstanceCrossVpcVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse(),
            self.do_rpcrequest('AllocateHostInstanceCrossVpcVip', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def allocate_host_instance_cross_vpc_vip_with_options_async(
        self,
        request: cddc_20200320_models.AllocateHostInstanceCrossVpcVipRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse(),
            await self.do_rpcrequest_async('AllocateHostInstanceCrossVpcVip', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def allocate_host_instance_cross_vpc_vip(
        self,
        request: cddc_20200320_models.AllocateHostInstanceCrossVpcVipRequest,
    ) -> cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_host_instance_cross_vpc_vip_with_options(request, runtime)

    async def allocate_host_instance_cross_vpc_vip_async(
        self,
        request: cddc_20200320_models.AllocateHostInstanceCrossVpcVipRequest,
    ) -> cddc_20200320_models.AllocateHostInstanceCrossVpcVipResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_host_instance_cross_vpc_vip_with_options_async(request, runtime)

    def describe_dedicated_hosts_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_hosts_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_with_options(request, runtime)

    async def describe_dedicated_hosts_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_with_options_async(request, runtime)

    def describe_dedicated_host_disks_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostDisksResponse(),
            self.do_rpcrequest('DescribeDedicatedHostDisks', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_disks_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostDisksResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostDisks', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_disks(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_disks_with_options(request, runtime)

    async def describe_dedicated_host_disks_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostDisksRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_disks_with_options_async(request, runtime)

    def describe_my_base_instance_over_view_with_options(
        self,
        request: cddc_20200320_models.DescribeMyBaseInstanceOverViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse(),
            self.do_rpcrequest('DescribeMyBaseInstanceOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_my_base_instance_over_view_with_options_async(
        self,
        request: cddc_20200320_models.DescribeMyBaseInstanceOverViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse(),
            await self.do_rpcrequest_async('DescribeMyBaseInstanceOverView', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_my_base_instance_over_view(
        self,
        request: cddc_20200320_models.DescribeMyBaseInstanceOverViewRequest,
    ) -> cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_my_base_instance_over_view_with_options(request, runtime)

    async def describe_my_base_instance_over_view_async(
        self,
        request: cddc_20200320_models.DescribeMyBaseInstanceOverViewRequest,
    ) -> cddc_20200320_models.DescribeMyBaseInstanceOverViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_my_base_instance_over_view_with_options_async(request, runtime)

    def modify_schedule_method_with_options(
        self,
        request: cddc_20200320_models.ModifyScheduleMethodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyScheduleMethodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyScheduleMethodResponse(),
            self.do_rpcrequest('ModifyScheduleMethod', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_schedule_method_with_options_async(
        self,
        request: cddc_20200320_models.ModifyScheduleMethodRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyScheduleMethodResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyScheduleMethodResponse(),
            await self.do_rpcrequest_async('ModifyScheduleMethod', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_schedule_method(
        self,
        request: cddc_20200320_models.ModifyScheduleMethodRequest,
    ) -> cddc_20200320_models.ModifyScheduleMethodResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_schedule_method_with_options(request, runtime)

    async def modify_schedule_method_async(
        self,
        request: cddc_20200320_models.ModifyScheduleMethodRequest,
    ) -> cddc_20200320_models.ModifyScheduleMethodResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_schedule_method_with_options_async(request, runtime)

    def describe_available_dedicated_host_classes_with_options(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse(),
            self.do_rpcrequest('DescribeAvailableDedicatedHostClasses', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_available_dedicated_host_classes_with_options_async(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostClassesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse(),
            await self.do_rpcrequest_async('DescribeAvailableDedicatedHostClasses', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_dedicated_host_classes(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_available_dedicated_host_classes_with_options(request, runtime)

    async def describe_available_dedicated_host_classes_async(
        self,
        request: cddc_20200320_models.DescribeAvailableDedicatedHostClassesRequest,
    ) -> cddc_20200320_models.DescribeAvailableDedicatedHostClassesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_available_dedicated_host_classes_with_options_async(request, runtime)

    def describe_check_user_backup_file_with_options(
        self,
        request: cddc_20200320_models.DescribeCheckUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeCheckUserBackupFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCheckUserBackupFileResponse(),
            self.do_rpcrequest('DescribeCheckUserBackupFile', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_check_user_backup_file_with_options_async(
        self,
        request: cddc_20200320_models.DescribeCheckUserBackupFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeCheckUserBackupFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCheckUserBackupFileResponse(),
            await self.do_rpcrequest_async('DescribeCheckUserBackupFile', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_check_user_backup_file(
        self,
        request: cddc_20200320_models.DescribeCheckUserBackupFileRequest,
    ) -> cddc_20200320_models.DescribeCheckUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_check_user_backup_file_with_options(request, runtime)

    async def describe_check_user_backup_file_async(
        self,
        request: cddc_20200320_models.DescribeCheckUserBackupFileRequest,
    ) -> cddc_20200320_models.DescribeCheckUserBackupFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_check_user_backup_file_with_options_async(request, runtime)

    def modify_dedicated_host_password_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostPasswordResponse(),
            self.do_rpcrequest('ModifyDedicatedHostPassword', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_password_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostPasswordResponse(),
            await self.do_rpcrequest_async('ModifyDedicatedHostPassword', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_password(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_password_with_options(request, runtime)

    async def modify_dedicated_host_password_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostPasswordRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_password_with_options_async(request, runtime)

    def describe_schedule_methods_with_options(
        self,
        request: cddc_20200320_models.DescribeScheduleMethodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleMethodsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleMethodsResponse(),
            self.do_rpcrequest('DescribeScheduleMethods', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_schedule_methods_with_options_async(
        self,
        request: cddc_20200320_models.DescribeScheduleMethodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleMethodsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleMethodsResponse(),
            await self.do_rpcrequest_async('DescribeScheduleMethods', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_methods(
        self,
        request: cddc_20200320_models.DescribeScheduleMethodsRequest,
    ) -> cddc_20200320_models.DescribeScheduleMethodsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_methods_with_options(request, runtime)

    async def describe_schedule_methods_async(
        self,
        request: cddc_20200320_models.DescribeScheduleMethodsRequest,
    ) -> cddc_20200320_models.DescribeScheduleMethodsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_methods_with_options_async(request, runtime)

    def clear_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ClearDedicatedHostResponse(),
            self.do_rpcrequest('ClearDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clear_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.ClearDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ClearDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ClearDedicatedHostResponse(),
            await self.do_rpcrequest_async('ClearDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clear_dedicated_host(
        self,
        request: cddc_20200320_models.ClearDedicatedHostRequest,
    ) -> cddc_20200320_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.clear_dedicated_host_with_options(request, runtime)

    async def clear_dedicated_host_async(
        self,
        request: cddc_20200320_models.ClearDedicatedHostRequest,
    ) -> cddc_20200320_models.ClearDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clear_dedicated_host_with_options_async(request, runtime)

    def delete_user_backup_file_record_with_options(
        self,
        request: cddc_20200320_models.DeleteUserBackupFileRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteUserBackupFileRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteUserBackupFileRecordResponse(),
            self.do_rpcrequest('DeleteUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_backup_file_record_with_options_async(
        self,
        request: cddc_20200320_models.DeleteUserBackupFileRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DeleteUserBackupFileRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DeleteUserBackupFileRecordResponse(),
            await self.do_rpcrequest_async('DeleteUserBackupFileRecord', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user_backup_file_record(
        self,
        request: cddc_20200320_models.DeleteUserBackupFileRecordRequest,
    ) -> cddc_20200320_models.DeleteUserBackupFileRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_backup_file_record_with_options(request, runtime)

    async def delete_user_backup_file_record_async(
        self,
        request: cddc_20200320_models.DeleteUserBackupFileRecordRequest,
    ) -> cddc_20200320_models.DeleteUserBackupFileRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_backup_file_record_with_options_async(request, runtime)

    def describe_evaluate_dedicated_hosts_with_options(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse(),
            self.do_rpcrequest('DescribeEvaluateDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_dedicated_hosts_with_options_async(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse(),
            await self.do_rpcrequest_async('DescribeEvaluateDedicatedHosts', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_dedicated_hosts(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_dedicated_hosts_with_options(request, runtime)

    async def describe_evaluate_dedicated_hosts_async(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsRequest,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_dedicated_hosts_with_options_async(request, runtime)

    def describe_host_instance_monitor_info_with_options(
        self,
        request: cddc_20200320_models.DescribeHostInstanceMonitorInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse(),
            self.do_rpcrequest('DescribeHostInstanceMonitorInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_instance_monitor_info_with_options_async(
        self,
        request: cddc_20200320_models.DescribeHostInstanceMonitorInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse(),
            await self.do_rpcrequest_async('DescribeHostInstanceMonitorInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_instance_monitor_info(
        self,
        request: cddc_20200320_models.DescribeHostInstanceMonitorInfoRequest,
    ) -> cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_instance_monitor_info_with_options(request, runtime)

    async def describe_host_instance_monitor_info_async(
        self,
        request: cddc_20200320_models.DescribeHostInstanceMonitorInfoRequest,
    ) -> cddc_20200320_models.DescribeHostInstanceMonitorInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_instance_monitor_info_with_options_async(request, runtime)

    def describe_dedicated_host_metric_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostMetricResponse(),
            self.do_rpcrequest('DescribeDedicatedHostMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_metric_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostMetricResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_metric(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostMetricRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_metric_with_options(request, runtime)

    async def describe_dedicated_host_metric_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostMetricRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_metric_with_options_async(request, runtime)

    def create_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostResponse(),
            self.do_rpcrequest('CreateDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostResponse(),
            await self.do_rpcrequest_async('CreateDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_with_options(request, runtime)

    async def create_dedicated_host_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_with_options_async(request, runtime)

    def describe_dedicated_instance_metric_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceMetricResponse(),
            self.do_rpcrequest('DescribeDedicatedInstanceMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_instance_metric_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceMetricResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedInstanceMetric', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_instance_metric(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceMetricRequest,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_instance_metric_with_options(request, runtime)

    async def describe_dedicated_instance_metric_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceMetricRequest,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_instance_metric_with_options_async(request, runtime)

    def describe_cross_vpc_instance_with_options(
        self,
        request: cddc_20200320_models.DescribeCrossVpcInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeCrossVpcInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCrossVpcInstanceResponse(),
            self.do_rpcrequest('DescribeCrossVpcInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cross_vpc_instance_with_options_async(
        self,
        request: cddc_20200320_models.DescribeCrossVpcInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeCrossVpcInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeCrossVpcInstanceResponse(),
            await self.do_rpcrequest_async('DescribeCrossVpcInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cross_vpc_instance(
        self,
        request: cddc_20200320_models.DescribeCrossVpcInstanceRequest,
    ) -> cddc_20200320_models.DescribeCrossVpcInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cross_vpc_instance_with_options(request, runtime)

    async def describe_cross_vpc_instance_async(
        self,
        request: cddc_20200320_models.DescribeCrossVpcInstanceRequest,
    ) -> cddc_20200320_models.DescribeCrossVpcInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cross_vpc_instance_with_options_async(request, runtime)

    def modify_dedicated_host_class_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostClassResponse(),
            self.do_rpcrequest('ModifyDedicatedHostClass', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_class_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostClassResponse(),
            await self.do_rpcrequest_async('ModifyDedicatedHostClass', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_class(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_class_with_options(request, runtime)

    async def modify_dedicated_host_class_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostClassRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_class_with_options_async(request, runtime)

    def describe_dedicated_hosts_check_in_bastion_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsCheckInBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse(),
            self.do_rpcrequest('DescribeDedicatedHostsCheckInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_hosts_check_in_bastion_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsCheckInBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostsCheckInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts_check_in_bastion(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsCheckInBastionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_check_in_bastion_with_options(request, runtime)

    async def describe_dedicated_hosts_check_in_bastion_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsCheckInBastionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsCheckInBastionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_check_in_bastion_with_options_async(request, runtime)

    def drop_dedicated_host_user_with_options(
        self,
        request: cddc_20200320_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DropDedicatedHostUserResponse(),
            self.do_rpcrequest('DropDedicatedHostUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def drop_dedicated_host_user_with_options_async(
        self,
        request: cddc_20200320_models.DropDedicatedHostUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DropDedicatedHostUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DropDedicatedHostUserResponse(),
            await self.do_rpcrequest_async('DropDedicatedHostUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def drop_dedicated_host_user(
        self,
        request: cddc_20200320_models.DropDedicatedHostUserRequest,
    ) -> cddc_20200320_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.drop_dedicated_host_user_with_options(request, runtime)

    async def drop_dedicated_host_user_async(
        self,
        request: cddc_20200320_models.DropDedicatedHostUserRequest,
    ) -> cddc_20200320_models.DropDedicatedHostUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.drop_dedicated_host_user_with_options_async(request, runtime)

    def describe_dedicated_hosts_in_bastion_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsInBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsInBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsInBastionResponse(),
            self.do_rpcrequest('DescribeDedicatedHostsInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_hosts_in_bastion_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsInBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostsInBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostsInBastionResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostsInBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_hosts_in_bastion(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsInBastionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsInBastionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_hosts_in_bastion_with_options(request, runtime)

    async def describe_dedicated_hosts_in_bastion_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostsInBastionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostsInBastionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_hosts_in_bastion_with_options_async(request, runtime)

    def modify_dedicated_host_group_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostGroupAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_group_attribute_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse(),
            await self.do_rpcrequest_async('ModifyDedicatedHostGroupAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_group_attribute(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_group_attribute_with_options(request, runtime)

    async def modify_dedicated_host_group_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostGroupAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_group_attribute_with_options_async(request, runtime)

    def query_host_instance_console_info_with_options(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostInstanceConsoleInfoResponse(),
            self.do_rpcrequest('QueryHostInstanceConsoleInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_host_instance_console_info_with_options_async(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostInstanceConsoleInfoResponse(),
            await self.do_rpcrequest_async('QueryHostInstanceConsoleInfo', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_host_instance_console_info(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_host_instance_console_info_with_options(request, runtime)

    async def query_host_instance_console_info_async(
        self,
        request: cddc_20200320_models.QueryHostInstanceConsoleInfoRequest,
    ) -> cddc_20200320_models.QueryHostInstanceConsoleInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_host_instance_console_info_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: cddc_20200320_models.DescribeRegionsRequest,
    ) -> cddc_20200320_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def query_host_base_info_by_instance_with_options(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostBaseInfoByInstanceResponse(),
            self.do_rpcrequest('QueryHostBaseInfoByInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_host_base_info_by_instance_with_options_async(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.QueryHostBaseInfoByInstanceResponse(),
            await self.do_rpcrequest_async('QueryHostBaseInfoByInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_host_base_info_by_instance(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_host_base_info_by_instance_with_options(request, runtime)

    async def query_host_base_info_by_instance_async(
        self,
        request: cddc_20200320_models.QueryHostBaseInfoByInstanceRequest,
    ) -> cddc_20200320_models.QueryHostBaseInfoByInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_host_base_info_by_instance_with_options_async(request, runtime)

    def describe_dedicated_instance_distribution_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse(),
            self.do_rpcrequest('DescribeDedicatedInstanceDistribution', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_instance_distribution_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceDistributionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedInstanceDistribution', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_instance_distribution(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceDistributionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_instance_distribution_with_options(request, runtime)

    async def describe_dedicated_instance_distribution_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedInstanceDistributionRequest,
    ) -> cddc_20200320_models.DescribeDedicatedInstanceDistributionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_instance_distribution_with_options_async(request, runtime)

    def describe_schedule_host_with_options(
        self,
        request: cddc_20200320_models.DescribeScheduleHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleHostResponse(),
            self.do_rpcrequest('DescribeScheduleHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_schedule_host_with_options_async(
        self,
        request: cddc_20200320_models.DescribeScheduleHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeScheduleHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeScheduleHostResponse(),
            await self.do_rpcrequest_async('DescribeScheduleHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_schedule_host(
        self,
        request: cddc_20200320_models.DescribeScheduleHostRequest,
    ) -> cddc_20200320_models.DescribeScheduleHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_schedule_host_with_options(request, runtime)

    async def describe_schedule_host_async(
        self,
        request: cddc_20200320_models.DescribeScheduleHostRequest,
    ) -> cddc_20200320_models.DescribeScheduleHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_schedule_host_with_options_async(request, runtime)

    def modify_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAttributeResponse(),
            self.do_rpcrequest('ModifyDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_dedicated_host_attribute_with_options_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.ModifyDedicatedHostAttributeResponse(),
            await self.do_rpcrequest_async('ModifyDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_dedicated_host_attribute(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dedicated_host_attribute_with_options(request, runtime)

    async def modify_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.ModifyDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.ModifyDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dedicated_host_attribute_with_options_async(request, runtime)

    def create_dedicated_host_group_with_options(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostGroupResponse(),
            self.do_rpcrequest('CreateDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dedicated_host_group_with_options_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.CreateDedicatedHostGroupResponse(),
            await self.do_rpcrequest_async('CreateDedicatedHostGroup', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dedicated_host_group(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dedicated_host_group_with_options(request, runtime)

    async def create_dedicated_host_group_async(
        self,
        request: cddc_20200320_models.CreateDedicatedHostGroupRequest,
    ) -> cddc_20200320_models.CreateDedicatedHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dedicated_host_group_with_options_async(request, runtime)

    def add_hosts_to_bastion_with_options(
        self,
        request: cddc_20200320_models.AddHostsToBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AddHostsToBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AddHostsToBastionResponse(),
            self.do_rpcrequest('AddHostsToBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_hosts_to_bastion_with_options_async(
        self,
        request: cddc_20200320_models.AddHostsToBastionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AddHostsToBastionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AddHostsToBastionResponse(),
            await self.do_rpcrequest_async('AddHostsToBastion', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_hosts_to_bastion(
        self,
        request: cddc_20200320_models.AddHostsToBastionRequest,
    ) -> cddc_20200320_models.AddHostsToBastionResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_hosts_to_bastion_with_options(request, runtime)

    async def add_hosts_to_bastion_async(
        self,
        request: cddc_20200320_models.AddHostsToBastionRequest,
    ) -> cddc_20200320_models.AddHostsToBastionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_hosts_to_bastion_with_options_async(request, runtime)

    def attach_hosts_to_bastion_user_with_options(
        self,
        request: cddc_20200320_models.AttachHostsToBastionUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AttachHostsToBastionUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AttachHostsToBastionUserResponse(),
            self.do_rpcrequest('AttachHostsToBastionUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def attach_hosts_to_bastion_user_with_options_async(
        self,
        request: cddc_20200320_models.AttachHostsToBastionUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.AttachHostsToBastionUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.AttachHostsToBastionUserResponse(),
            await self.do_rpcrequest_async('AttachHostsToBastionUser', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_hosts_to_bastion_user(
        self,
        request: cddc_20200320_models.AttachHostsToBastionUserRequest,
    ) -> cddc_20200320_models.AttachHostsToBastionUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.attach_hosts_to_bastion_user_with_options(request, runtime)

    async def attach_hosts_to_bastion_user_async(
        self,
        request: cddc_20200320_models.AttachHostsToBastionUserRequest,
    ) -> cddc_20200320_models.AttachHostsToBastionUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.attach_hosts_to_bastion_user_with_options_async(request, runtime)

    def describe_evaluate_dedicated_hosts_for_instance_with_options(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse(),
            self.do_rpcrequest('DescribeEvaluateDedicatedHostsForInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_dedicated_hosts_for_instance_with_options_async(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse(),
            await self.do_rpcrequest_async('DescribeEvaluateDedicatedHostsForInstance', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_dedicated_hosts_for_instance(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceRequest,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_dedicated_hosts_for_instance_with_options(request, runtime)

    async def describe_evaluate_dedicated_hosts_for_instance_async(
        self,
        request: cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceRequest,
    ) -> cddc_20200320_models.DescribeEvaluateDedicatedHostsForInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_dedicated_hosts_for_instance_with_options_async(request, runtime)

    def restart_dedicated_host_with_options(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.RestartDedicatedHostResponse(),
            self.do_rpcrequest('RestartDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_dedicated_host_with_options_async(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.RestartDedicatedHostResponse(),
            await self.do_rpcrequest_async('RestartDedicatedHost', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_dedicated_host(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_dedicated_host_with_options(request, runtime)

    async def restart_dedicated_host_async(
        self,
        request: cddc_20200320_models.RestartDedicatedHostRequest,
    ) -> cddc_20200320_models.RestartDedicatedHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_dedicated_host_with_options_async(request, runtime)

    def describe_dedicated_host_health_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostHealthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostHealthResponse(),
            self.do_rpcrequest('DescribeDedicatedHostHealth', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_health_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostHealthResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostHealthResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostHealth', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_health(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostHealthRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostHealthResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_health_with_options(request, runtime)

    async def describe_dedicated_host_health_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostHealthRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostHealthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_health_with_options_async(request, runtime)

    def describe_host_web_shell_with_options(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostWebShellResponse(),
            self.do_rpcrequest('DescribeHostWebShell', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_web_shell_with_options_async(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeHostWebShellResponse(),
            await self.do_rpcrequest_async('DescribeHostWebShell', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_web_shell(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_web_shell_with_options(request, runtime)

    async def describe_host_web_shell_async(
        self,
        request: cddc_20200320_models.DescribeHostWebShellRequest,
    ) -> cddc_20200320_models.DescribeHostWebShellResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_web_shell_with_options_async(request, runtime)

    def describe_dedicated_host_attribute_with_options(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostAttributeResponse(),
            self.do_rpcrequest('DescribeDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dedicated_host_attribute_with_options_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cddc_20200320_models.DescribeDedicatedHostAttributeResponse(),
            await self.do_rpcrequest_async('DescribeDedicatedHostAttribute', '2020-03-20', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dedicated_host_attribute(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dedicated_host_attribute_with_options(request, runtime)

    async def describe_dedicated_host_attribute_async(
        self,
        request: cddc_20200320_models.DescribeDedicatedHostAttributeRequest,
    ) -> cddc_20200320_models.DescribeDedicatedHostAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dedicated_host_attribute_with_options_async(request, runtime)
