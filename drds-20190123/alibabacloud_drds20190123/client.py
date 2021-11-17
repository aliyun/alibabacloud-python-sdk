# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_drds20190123 import models as drds_20190123_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
            'ap-northeast-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'drds.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'drds.ap-southeast-1.aliyuncs.com',
            'cn-beijing-finance-1': 'drds.aliyuncs.com',
            'cn-beijing-finance-pop': 'drds.aliyuncs.com',
            'cn-beijing-gov-1': 'drds.aliyuncs.com',
            'cn-beijing-nu16-b01': 'drds.aliyuncs.com',
            'cn-chengdu': 'drds.aliyuncs.com',
            'cn-edge-1': 'drds.aliyuncs.com',
            'cn-fujian': 'drds.aliyuncs.com',
            'cn-haidian-cm12-c01': 'drds.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'drds.aliyuncs.com',
            'cn-hangzhou-finance': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'drds.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'drds.aliyuncs.com',
            'cn-hangzhou-test-306': 'drds.aliyuncs.com',
            'cn-hongkong-finance-pop': 'drds.aliyuncs.com',
            'cn-qingdao-nebula': 'drds.aliyuncs.com',
            'cn-shanghai-et15-b01': 'drds.aliyuncs.com',
            'cn-shanghai-et2-b01': 'drds.aliyuncs.com',
            'cn-shanghai-inner': 'drds.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'drds.aliyuncs.com',
            'cn-shenzhen-inner': 'drds.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'drds.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'drds.aliyuncs.com',
            'cn-wuhan': 'drds.aliyuncs.com',
            'cn-yushanfang': 'drds.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'drds.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'drds.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'drds.aliyuncs.com',
            'eu-central-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'drds.ap-southeast-1.aliyuncs.com',
            'eu-west-1-oxs': 'drds.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'drds.ap-southeast-1.aliyuncs.com',
            'rus-west-1-pop': 'drds.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'drds.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('drds', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_account_password_with_options(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            self.do_rpcrequest('ChangeAccountPassword', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_account_password_with_options_async(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeAccountPasswordResponse(),
            await self.do_rpcrequest_async('ChangeAccountPassword', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_account_password(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_account_password_with_options(request, runtime)

    async def change_account_password_async(
        self,
        request: drds_20190123_models.ChangeAccountPasswordRequest,
    ) -> drds_20190123_models.ChangeAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_account_password_with_options_async(request, runtime)

    def change_instance_azone_with_options(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            self.do_rpcrequest('ChangeInstanceAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_instance_azone_with_options_async(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceAzoneResponse(),
            await self.do_rpcrequest_async('ChangeInstanceAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_instance_azone(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_instance_azone_with_options(request, runtime)

    async def change_instance_azone_async(
        self,
        request: drds_20190123_models.ChangeInstanceAzoneRequest,
    ) -> drds_20190123_models.ChangeInstanceAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_instance_azone_with_options_async(request, runtime)

    def change_instance_network_with_options(
        self,
        request: drds_20190123_models.ChangeInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceNetworkResponse(),
            self.do_rpcrequest('ChangeInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def change_instance_network_with_options_async(
        self,
        request: drds_20190123_models.ChangeInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ChangeInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ChangeInstanceNetworkResponse(),
            await self.do_rpcrequest_async('ChangeInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def change_instance_network(
        self,
        request: drds_20190123_models.ChangeInstanceNetworkRequest,
    ) -> drds_20190123_models.ChangeInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_instance_network_with_options(request, runtime)

    async def change_instance_network_async(
        self,
        request: drds_20190123_models.ChangeInstanceNetworkRequest,
    ) -> drds_20190123_models.ChangeInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_instance_network_with_options_async(request, runtime)

    def check_connectivity_with_options(
        self,
        tmp_req: drds_20190123_models.CheckConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckConnectivityResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CheckConnectivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_info):
            request.db_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_info, 'DbInfo', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckConnectivityResponse(),
            self.do_rpcrequest('CheckConnectivity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_connectivity_with_options_async(
        self,
        tmp_req: drds_20190123_models.CheckConnectivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckConnectivityResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CheckConnectivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_info):
            request.db_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_info, 'DbInfo', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckConnectivityResponse(),
            await self.do_rpcrequest_async('CheckConnectivity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_connectivity(
        self,
        request: drds_20190123_models.CheckConnectivityRequest,
    ) -> drds_20190123_models.CheckConnectivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_connectivity_with_options(request, runtime)

    async def check_connectivity_async(
        self,
        request: drds_20190123_models.CheckConnectivityRequest,
    ) -> drds_20190123_models.CheckConnectivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_connectivity_with_options_async(request, runtime)

    def check_drds_db_name_with_options(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            self.do_rpcrequest('CheckDrdsDbName', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_drds_db_name_with_options_async(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckDrdsDbNameResponse(),
            await self.do_rpcrequest_async('CheckDrdsDbName', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_drds_db_name(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_drds_db_name_with_options(request, runtime)

    async def check_drds_db_name_async(
        self,
        request: drds_20190123_models.CheckDrdsDbNameRequest,
    ) -> drds_20190123_models.CheckDrdsDbNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_drds_db_name_with_options_async(request, runtime)

    def check_expand_status_with_options(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            self.do_rpcrequest('CheckExpandStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_expand_status_with_options_async(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckExpandStatusResponse(),
            await self.do_rpcrequest_async('CheckExpandStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_expand_status(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_expand_status_with_options(request, runtime)

    async def check_expand_status_async(
        self,
        request: drds_20190123_models.CheckExpandStatusRequest,
    ) -> drds_20190123_models.CheckExpandStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_expand_status_with_options_async(request, runtime)

    def check_new_table_name_valid_with_options(
        self,
        request: drds_20190123_models.CheckNewTableNameValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckNewTableNameValidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckNewTableNameValidResponse(),
            self.do_rpcrequest('CheckNewTableNameValid', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_new_table_name_valid_with_options_async(
        self,
        request: drds_20190123_models.CheckNewTableNameValidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckNewTableNameValidResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckNewTableNameValidResponse(),
            await self.do_rpcrequest_async('CheckNewTableNameValid', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_new_table_name_valid(
        self,
        request: drds_20190123_models.CheckNewTableNameValidRequest,
    ) -> drds_20190123_models.CheckNewTableNameValidResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_new_table_name_valid_with_options(request, runtime)

    async def check_new_table_name_valid_async(
        self,
        request: drds_20190123_models.CheckNewTableNameValidRequest,
    ) -> drds_20190123_models.CheckNewTableNameValidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_new_table_name_valid_with_options_async(request, runtime)

    def check_rds_super_account_with_options(
        self,
        request: drds_20190123_models.CheckRdsSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckRdsSuperAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckRdsSuperAccountResponse(),
            self.do_rpcrequest('CheckRdsSuperAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_rds_super_account_with_options_async(
        self,
        request: drds_20190123_models.CheckRdsSuperAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckRdsSuperAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckRdsSuperAccountResponse(),
            await self.do_rpcrequest_async('CheckRdsSuperAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_rds_super_account(
        self,
        request: drds_20190123_models.CheckRdsSuperAccountRequest,
    ) -> drds_20190123_models.CheckRdsSuperAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_rds_super_account_with_options(request, runtime)

    async def check_rds_super_account_async(
        self,
        request: drds_20190123_models.CheckRdsSuperAccountRequest,
    ) -> drds_20190123_models.CheckRdsSuperAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_rds_super_account_with_options_async(request, runtime)

    def check_sql_audit_enable_status_with_options(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            self.do_rpcrequest('CheckSqlAuditEnableStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_sql_audit_enable_status_with_options_async(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CheckSqlAuditEnableStatusResponse(),
            await self.do_rpcrequest_async('CheckSqlAuditEnableStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_sql_audit_enable_status(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_sql_audit_enable_status_with_options(request, runtime)

    async def check_sql_audit_enable_status_async(
        self,
        request: drds_20190123_models.CheckSqlAuditEnableStatusRequest,
    ) -> drds_20190123_models.CheckSqlAuditEnableStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_sql_audit_enable_status_with_options_async(request, runtime)

    def configure_drds_db_instances_with_options(
        self,
        request: drds_20190123_models.ConfigureDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ConfigureDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ConfigureDrdsDbInstancesResponse(),
            self.do_rpcrequest('ConfigureDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def configure_drds_db_instances_with_options_async(
        self,
        request: drds_20190123_models.ConfigureDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ConfigureDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ConfigureDrdsDbInstancesResponse(),
            await self.do_rpcrequest_async('ConfigureDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def configure_drds_db_instances(
        self,
        request: drds_20190123_models.ConfigureDrdsDbInstancesRequest,
    ) -> drds_20190123_models.ConfigureDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_drds_db_instances_with_options(request, runtime)

    async def configure_drds_db_instances_async(
        self,
        request: drds_20190123_models.ConfigureDrdsDbInstancesRequest,
    ) -> drds_20190123_models.ConfigureDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_drds_db_instances_with_options_async(request, runtime)

    def create_custom_data_export_pre_check_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataExportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateCustomDataExportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_custom_data_export_pre_check_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataExportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse(),
            await self.do_rpcrequest_async('CreateCustomDataExportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_export_pre_check_task(
        self,
        request: drds_20190123_models.CreateCustomDataExportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_export_pre_check_task_with_options(request, runtime)

    async def create_custom_data_export_pre_check_task_async(
        self,
        request: drds_20190123_models.CreateCustomDataExportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataExportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_data_export_pre_check_task_with_options_async(request, runtime)

    def create_custom_data_export_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataExportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportTaskResponse(),
            self.do_rpcrequest('CreateCustomDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_custom_data_export_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataExportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataExportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataExportTaskResponse(),
            await self.do_rpcrequest_async('CreateCustomDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_export_task(
        self,
        request: drds_20190123_models.CreateCustomDataExportTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_export_task_with_options(request, runtime)

    async def create_custom_data_export_task_async(
        self,
        request: drds_20190123_models.CreateCustomDataExportTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_data_export_task_with_options_async(request, runtime)

    def create_custom_data_import_pre_check_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataImportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateCustomDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_custom_data_import_pre_check_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataImportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse(),
            await self.do_rpcrequest_async('CreateCustomDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_import_pre_check_task(
        self,
        request: drds_20190123_models.CreateCustomDataImportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_import_pre_check_task_with_options(request, runtime)

    async def create_custom_data_import_pre_check_task_async(
        self,
        request: drds_20190123_models.CreateCustomDataImportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataImportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_data_import_pre_check_task_with_options_async(request, runtime)

    def create_custom_data_import_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataImportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportTaskResponse(),
            self.do_rpcrequest('CreateCustomDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_custom_data_import_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateCustomDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateCustomDataImportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateCustomDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateCustomDataImportTaskResponse(),
            await self.do_rpcrequest_async('CreateCustomDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_custom_data_import_task(
        self,
        request: drds_20190123_models.CreateCustomDataImportTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_custom_data_import_task_with_options(request, runtime)

    async def create_custom_data_import_task_async(
        self,
        request: drds_20190123_models.CreateCustomDataImportTaskRequest,
    ) -> drds_20190123_models.CreateCustomDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_custom_data_import_task_with_options_async(request, runtime)

    def create_drds_dbwith_options(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            self.do_rpcrequest('CreateDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_drds_dbwith_options_async(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBResponse(),
            await self.do_rpcrequest_async('CreateDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_db(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbwith_options(request, runtime)

    async def create_drds_db_async(
        self,
        request: drds_20190123_models.CreateDrdsDBRequest,
    ) -> drds_20190123_models.CreateDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_dbwith_options_async(request, runtime)

    def create_drds_dbpre_check_with_options(
        self,
        request: drds_20190123_models.CreateDrdsDBPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBPreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreCheckResponse(),
            self.do_rpcrequest('CreateDrdsDBPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_drds_dbpre_check_with_options_async(
        self,
        request: drds_20190123_models.CreateDrdsDBPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBPreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreCheckResponse(),
            await self.do_rpcrequest_async('CreateDrdsDBPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_dbpre_check(
        self,
        request: drds_20190123_models.CreateDrdsDBPreCheckRequest,
    ) -> drds_20190123_models.CreateDrdsDBPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpre_check_with_options(request, runtime)

    async def create_drds_dbpre_check_async(
        self,
        request: drds_20190123_models.CreateDrdsDBPreCheckRequest,
    ) -> drds_20190123_models.CreateDrdsDBPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_dbpre_check_with_options_async(request, runtime)

    def create_drds_dbpreview_with_options(
        self,
        request: drds_20190123_models.CreateDrdsDBPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBPreviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreviewResponse(),
            self.do_rpcrequest('CreateDrdsDBPreview', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_drds_dbpreview_with_options_async(
        self,
        request: drds_20190123_models.CreateDrdsDBPreviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsDBPreviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsDBPreviewResponse(),
            await self.do_rpcrequest_async('CreateDrdsDBPreview', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_dbpreview(
        self,
        request: drds_20190123_models.CreateDrdsDBPreviewRequest,
    ) -> drds_20190123_models.CreateDrdsDBPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_dbpreview_with_options(request, runtime)

    async def create_drds_dbpreview_async(
        self,
        request: drds_20190123_models.CreateDrdsDBPreviewRequest,
    ) -> drds_20190123_models.CreateDrdsDBPreviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_dbpreview_with_options_async(request, runtime)

    def create_drds_instance_with_options(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            self.do_rpcrequest('CreateDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateDrdsInstanceResponse(),
            await self.do_rpcrequest_async('CreateDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_drds_instance(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_drds_instance_with_options(request, runtime)

    async def create_drds_instance_async(
        self,
        request: drds_20190123_models.CreateDrdsInstanceRequest,
    ) -> drds_20190123_models.CreateDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_drds_instance_with_options_async(request, runtime)

    def create_evaluate_data_import_pre_check_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateEvaluateDataImportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse(),
            self.do_rpcrequest('CreateEvaluateDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_evaluate_data_import_pre_check_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateEvaluateDataImportPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportPreCheckTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse(),
            await self.do_rpcrequest_async('CreateEvaluateDataImportPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_data_import_pre_check_task(
        self,
        request: drds_20190123_models.CreateEvaluateDataImportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_data_import_pre_check_task_with_options(request, runtime)

    async def create_evaluate_data_import_pre_check_task_async(
        self,
        request: drds_20190123_models.CreateEvaluateDataImportPreCheckTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateDataImportPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_evaluate_data_import_pre_check_task_with_options_async(request, runtime)

    def create_evaluate_data_import_task_with_options(
        self,
        tmp_req: drds_20190123_models.CreateEvaluateDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateDataImportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportTaskResponse(),
            self.do_rpcrequest('CreateEvaluateDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_evaluate_data_import_task_with_options_async(
        self,
        tmp_req: drds_20190123_models.CreateEvaluateDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateDataImportTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.CreateEvaluateDataImportTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateDataImportTaskResponse(),
            await self.do_rpcrequest_async('CreateEvaluateDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_data_import_task(
        self,
        request: drds_20190123_models.CreateEvaluateDataImportTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_data_import_task_with_options(request, runtime)

    async def create_evaluate_data_import_task_async(
        self,
        request: drds_20190123_models.CreateEvaluateDataImportTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_evaluate_data_import_task_with_options_async(request, runtime)

    def create_evaluate_pre_check_task_with_options(
        self,
        request: drds_20190123_models.CreateEvaluatePreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluatePreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluatePreCheckTaskResponse(),
            self.do_rpcrequest('CreateEvaluatePreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_evaluate_pre_check_task_with_options_async(
        self,
        request: drds_20190123_models.CreateEvaluatePreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluatePreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluatePreCheckTaskResponse(),
            await self.do_rpcrequest_async('CreateEvaluatePreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_pre_check_task(
        self,
        request: drds_20190123_models.CreateEvaluatePreCheckTaskRequest,
    ) -> drds_20190123_models.CreateEvaluatePreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_pre_check_task_with_options(request, runtime)

    async def create_evaluate_pre_check_task_async(
        self,
        request: drds_20190123_models.CreateEvaluatePreCheckTaskRequest,
    ) -> drds_20190123_models.CreateEvaluatePreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_evaluate_pre_check_task_with_options_async(request, runtime)

    def create_evaluate_task_with_options(
        self,
        request: drds_20190123_models.CreateEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateTaskResponse(),
            self.do_rpcrequest('CreateEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_evaluate_task_with_options_async(
        self,
        request: drds_20190123_models.CreateEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateEvaluateTaskResponse(),
            await self.do_rpcrequest_async('CreateEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_evaluate_task(
        self,
        request: drds_20190123_models.CreateEvaluateTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_evaluate_task_with_options(request, runtime)

    async def create_evaluate_task_async(
        self,
        request: drds_20190123_models.CreateEvaluateTaskRequest,
    ) -> drds_20190123_models.CreateEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_evaluate_task_with_options_async(request, runtime)

    def create_instance_account_with_options(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            self.do_rpcrequest('CreateInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_account_with_options_async(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceAccountResponse(),
            await self.do_rpcrequest_async('CreateInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_account(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_account_with_options(request, runtime)

    async def create_instance_account_async(
        self,
        request: drds_20190123_models.CreateInstanceAccountRequest,
    ) -> drds_20190123_models.CreateInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_account_with_options_async(request, runtime)

    def create_instance_internet_address_with_options(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            self.do_rpcrequest('CreateInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_instance_internet_address_with_options_async(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateInstanceInternetAddressResponse(),
            await self.do_rpcrequest_async('CreateInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_instance_internet_address(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_instance_internet_address_with_options(request, runtime)

    async def create_instance_internet_address_async(
        self,
        request: drds_20190123_models.CreateInstanceInternetAddressRequest,
    ) -> drds_20190123_models.CreateInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_instance_internet_address_with_options_async(request, runtime)

    def create_my_cat_evaluate_with_options(
        self,
        request: drds_20190123_models.CreateMyCatEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateMyCatEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateMyCatEvaluateResponse(),
            self.do_rpcrequest('CreateMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_my_cat_evaluate_with_options_async(
        self,
        request: drds_20190123_models.CreateMyCatEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateMyCatEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateMyCatEvaluateResponse(),
            await self.do_rpcrequest_async('CreateMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_my_cat_evaluate(
        self,
        request: drds_20190123_models.CreateMyCatEvaluateRequest,
    ) -> drds_20190123_models.CreateMyCatEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_my_cat_evaluate_with_options(request, runtime)

    async def create_my_cat_evaluate_async(
        self,
        request: drds_20190123_models.CreateMyCatEvaluateRequest,
    ) -> drds_20190123_models.CreateMyCatEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_my_cat_evaluate_with_options_async(request, runtime)

    def create_order_for_rds_with_options(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            self.do_rpcrequest('CreateOrderForRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_order_for_rds_with_options_async(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateOrderForRdsResponse(),
            await self.do_rpcrequest_async('CreateOrderForRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_order_for_rds(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_order_for_rds_with_options(request, runtime)

    async def create_order_for_rds_async(
        self,
        request: drds_20190123_models.CreateOrderForRdsRequest,
    ) -> drds_20190123_models.CreateOrderForRdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_order_for_rds_with_options_async(request, runtime)

    def create_shard_task_with_options(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            self.do_rpcrequest('CreateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_shard_task_with_options_async(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.CreateShardTaskResponse(),
            await self.do_rpcrequest_async('CreateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_shard_task(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_shard_task_with_options(request, runtime)

    async def create_shard_task_async(
        self,
        request: drds_20190123_models.CreateShardTaskRequest,
    ) -> drds_20190123_models.CreateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_shard_task_with_options_async(request, runtime)

    def describe_back_menu_with_options(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            self.do_rpcrequest('DescribeBackMenu', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_back_menu_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackMenuResponse(),
            await self.do_rpcrequest_async('DescribeBackMenu', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_back_menu(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_back_menu_with_options(request, runtime)

    async def describe_back_menu_async(
        self,
        request: drds_20190123_models.DescribeBackMenuRequest,
    ) -> drds_20190123_models.DescribeBackMenuResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_back_menu_with_options_async(request, runtime)

    def describe_backup_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            self.do_rpcrequest('DescribeBackupDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupDbsResponse(),
            await self.do_rpcrequest_async('DescribeBackupDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_dbs(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_dbs_with_options(request, runtime)

    async def describe_backup_dbs_async(
        self,
        request: drds_20190123_models.DescribeBackupDbsRequest,
    ) -> drds_20190123_models.DescribeBackupDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_dbs_with_options_async(request, runtime)

    def describe_backup_local_with_options(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            self.do_rpcrequest('DescribeBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_local_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupLocalResponse(),
            await self.do_rpcrequest_async('DescribeBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_local(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_local_with_options(request, runtime)

    async def describe_backup_local_async(
        self,
        request: drds_20190123_models.DescribeBackupLocalRequest,
    ) -> drds_20190123_models.DescribeBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_local_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            self.do_rpcrequest('DescribeBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupPolicyResponse(),
            await self.do_rpcrequest_async('DescribeBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_policy(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: drds_20190123_models.DescribeBackupPolicyRequest,
    ) -> drds_20190123_models.DescribeBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backup_sets_with_options(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            self.do_rpcrequest('DescribeBackupSets', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_sets_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupSetsResponse(),
            await self.do_rpcrequest_async('DescribeBackupSets', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_sets(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_sets_with_options(request, runtime)

    async def describe_backup_sets_async(
        self,
        request: drds_20190123_models.DescribeBackupSetsRequest,
    ) -> drds_20190123_models.DescribeBackupSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_sets_with_options_async(request, runtime)

    def describe_backup_times_with_options(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            self.do_rpcrequest('DescribeBackupTimes', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_backup_times_with_options_async(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBackupTimesResponse(),
            await self.do_rpcrequest_async('DescribeBackupTimes', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_backup_times(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_times_with_options(request, runtime)

    async def describe_backup_times_async(
        self,
        request: drds_20190123_models.DescribeBackupTimesRequest,
    ) -> drds_20190123_models.DescribeBackupTimesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_times_with_options_async(request, runtime)

    def describe_batch_evaluate_task_report_with_options(
        self,
        request: drds_20190123_models.DescribeBatchEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBatchEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBatchEvaluateTaskReportResponse(),
            self.do_rpcrequest('DescribeBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_batch_evaluate_task_report_with_options_async(
        self,
        request: drds_20190123_models.DescribeBatchEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBatchEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBatchEvaluateTaskReportResponse(),
            await self.do_rpcrequest_async('DescribeBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_batch_evaluate_task_report(
        self,
        request: drds_20190123_models.DescribeBatchEvaluateTaskReportRequest,
    ) -> drds_20190123_models.DescribeBatchEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_batch_evaluate_task_report_with_options(request, runtime)

    async def describe_batch_evaluate_task_report_async(
        self,
        request: drds_20190123_models.DescribeBatchEvaluateTaskReportRequest,
    ) -> drds_20190123_models.DescribeBatchEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_batch_evaluate_task_report_with_options_async(request, runtime)

    def describe_broadcast_tables_with_options(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            self.do_rpcrequest('DescribeBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_broadcast_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeBroadcastTablesResponse(),
            await self.do_rpcrequest_async('DescribeBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_broadcast_tables(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_broadcast_tables_with_options(request, runtime)

    async def describe_broadcast_tables_async(
        self,
        request: drds_20190123_models.DescribeBroadcastTablesRequest,
    ) -> drds_20190123_models.DescribeBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_broadcast_tables_with_options_async(request, runtime)

    def describe_can_expand_instance_detail_list_with_options(
        self,
        request: drds_20190123_models.DescribeCanExpandInstanceDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCanExpandInstanceDetailListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCanExpandInstanceDetailListResponse(),
            self.do_rpcrequest('DescribeCanExpandInstanceDetailList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_can_expand_instance_detail_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeCanExpandInstanceDetailListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCanExpandInstanceDetailListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCanExpandInstanceDetailListResponse(),
            await self.do_rpcrequest_async('DescribeCanExpandInstanceDetailList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_can_expand_instance_detail_list(
        self,
        request: drds_20190123_models.DescribeCanExpandInstanceDetailListRequest,
    ) -> drds_20190123_models.DescribeCanExpandInstanceDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_can_expand_instance_detail_list_with_options(request, runtime)

    async def describe_can_expand_instance_detail_list_async(
        self,
        request: drds_20190123_models.DescribeCanExpandInstanceDetailListRequest,
    ) -> drds_20190123_models.DescribeCanExpandInstanceDetailListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_can_expand_instance_detail_list_with_options_async(request, runtime)

    def describe_custom_data_export_src_dst_tables_with_options(
        self,
        tmp_req: drds_20190123_models.DescribeCustomDataExportSrcDstTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataExportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse(),
            self.do_rpcrequest('DescribeCustomDataExportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_data_export_src_dst_tables_with_options_async(
        self,
        tmp_req: drds_20190123_models.DescribeCustomDataExportSrcDstTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataExportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.export_param):
            request.export_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.export_param, 'ExportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse(),
            await self.do_rpcrequest_async('DescribeCustomDataExportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_data_export_src_dst_tables(
        self,
        request: drds_20190123_models.DescribeCustomDataExportSrcDstTablesRequest,
    ) -> drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_data_export_src_dst_tables_with_options(request, runtime)

    async def describe_custom_data_export_src_dst_tables_async(
        self,
        request: drds_20190123_models.DescribeCustomDataExportSrcDstTablesRequest,
    ) -> drds_20190123_models.DescribeCustomDataExportSrcDstTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_data_export_src_dst_tables_with_options_async(request, runtime)

    def describe_custom_data_import_src_dst_tables_with_options(
        self,
        tmp_req: drds_20190123_models.DescribeCustomDataImportSrcDstTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataImportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse(),
            self.do_rpcrequest('DescribeCustomDataImportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_data_import_src_dst_tables_with_options_async(
        self,
        tmp_req: drds_20190123_models.DescribeCustomDataImportSrcDstTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeCustomDataImportSrcDstTablesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse(),
            await self.do_rpcrequest_async('DescribeCustomDataImportSrcDstTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_data_import_src_dst_tables(
        self,
        request: drds_20190123_models.DescribeCustomDataImportSrcDstTablesRequest,
    ) -> drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_data_import_src_dst_tables_with_options(request, runtime)

    async def describe_custom_data_import_src_dst_tables_async(
        self,
        request: drds_20190123_models.DescribeCustomDataImportSrcDstTablesRequest,
    ) -> drds_20190123_models.DescribeCustomDataImportSrcDstTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_data_import_src_dst_tables_with_options_async(request, runtime)

    def describe_data_export_pre_check_result_with_options(
        self,
        request: drds_20190123_models.DescribeDataExportPreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportPreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportPreCheckResultResponse(),
            self.do_rpcrequest('DescribeDataExportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_export_pre_check_result_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataExportPreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportPreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportPreCheckResultResponse(),
            await self.do_rpcrequest_async('DescribeDataExportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_pre_check_result(
        self,
        request: drds_20190123_models.DescribeDataExportPreCheckResultRequest,
    ) -> drds_20190123_models.DescribeDataExportPreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_pre_check_result_with_options(request, runtime)

    async def describe_data_export_pre_check_result_async(
        self,
        request: drds_20190123_models.DescribeDataExportPreCheckResultRequest,
    ) -> drds_20190123_models.DescribeDataExportPreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_export_pre_check_result_with_options_async(request, runtime)

    def describe_data_export_task_report_with_options(
        self,
        request: drds_20190123_models.DescribeDataExportTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTaskReportResponse(),
            self.do_rpcrequest('DescribeDataExportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_export_task_report_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataExportTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTaskReportResponse(),
            await self.do_rpcrequest_async('DescribeDataExportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_task_report(
        self,
        request: drds_20190123_models.DescribeDataExportTaskReportRequest,
    ) -> drds_20190123_models.DescribeDataExportTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_task_report_with_options(request, runtime)

    async def describe_data_export_task_report_async(
        self,
        request: drds_20190123_models.DescribeDataExportTaskReportRequest,
    ) -> drds_20190123_models.DescribeDataExportTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_export_task_report_with_options_async(request, runtime)

    def describe_data_export_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDataExportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTasksResponse(),
            self.do_rpcrequest('DescribeDataExportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_export_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataExportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataExportTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataExportTasksResponse(),
            await self.do_rpcrequest_async('DescribeDataExportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_export_tasks(
        self,
        request: drds_20190123_models.DescribeDataExportTasksRequest,
    ) -> drds_20190123_models.DescribeDataExportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_export_tasks_with_options(request, runtime)

    async def describe_data_export_tasks_async(
        self,
        request: drds_20190123_models.DescribeDataExportTasksRequest,
    ) -> drds_20190123_models.DescribeDataExportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_export_tasks_with_options_async(request, runtime)

    def describe_data_import_pre_check_result_with_options(
        self,
        request: drds_20190123_models.DescribeDataImportPreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportPreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportPreCheckResultResponse(),
            self.do_rpcrequest('DescribeDataImportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_import_pre_check_result_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataImportPreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportPreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportPreCheckResultResponse(),
            await self.do_rpcrequest_async('DescribeDataImportPreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_pre_check_result(
        self,
        request: drds_20190123_models.DescribeDataImportPreCheckResultRequest,
    ) -> drds_20190123_models.DescribeDataImportPreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_pre_check_result_with_options(request, runtime)

    async def describe_data_import_pre_check_result_async(
        self,
        request: drds_20190123_models.DescribeDataImportPreCheckResultRequest,
    ) -> drds_20190123_models.DescribeDataImportPreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_import_pre_check_result_with_options_async(request, runtime)

    def describe_data_import_task_report_with_options(
        self,
        request: drds_20190123_models.DescribeDataImportTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTaskReportResponse(),
            self.do_rpcrequest('DescribeDataImportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_import_task_report_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataImportTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTaskReportResponse(),
            await self.do_rpcrequest_async('DescribeDataImportTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_task_report(
        self,
        request: drds_20190123_models.DescribeDataImportTaskReportRequest,
    ) -> drds_20190123_models.DescribeDataImportTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_task_report_with_options(request, runtime)

    async def describe_data_import_task_report_async(
        self,
        request: drds_20190123_models.DescribeDataImportTaskReportRequest,
    ) -> drds_20190123_models.DescribeDataImportTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_import_task_report_with_options_async(request, runtime)

    def describe_data_import_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDataImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTasksResponse(),
            self.do_rpcrequest('DescribeDataImportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_import_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDataImportTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDataImportTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDataImportTasksResponse(),
            await self.do_rpcrequest_async('DescribeDataImportTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_import_tasks(
        self,
        request: drds_20190123_models.DescribeDataImportTasksRequest,
    ) -> drds_20190123_models.DescribeDataImportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_import_tasks_with_options(request, runtime)

    async def describe_data_import_tasks_async(
        self,
        request: drds_20190123_models.DescribeDataImportTasksRequest,
    ) -> drds_20190123_models.DescribeDataImportTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_import_tasks_with_options_async(request, runtime)

    def describe_db_instance_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            self.do_rpcrequest('DescribeDbInstanceDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_db_instance_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstanceDbsResponse(),
            await self.do_rpcrequest_async('DescribeDbInstanceDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_instance_dbs(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instance_dbs_with_options(request, runtime)

    async def describe_db_instance_dbs_async(
        self,
        request: drds_20190123_models.DescribeDbInstanceDbsRequest,
    ) -> drds_20190123_models.DescribeDbInstanceDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_instance_dbs_with_options_async(request, runtime)

    def describe_db_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            self.do_rpcrequest('DescribeDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_db_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDbInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_db_instances(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_db_instances_with_options(request, runtime)

    async def describe_db_instances_async(
        self,
        request: drds_20190123_models.DescribeDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_db_instances_with_options_async(request, runtime)

    def describe_drds_dbwith_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            self.do_rpcrequest('DescribeDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_dbwith_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbwith_options(request, runtime)

    async def describe_drds_db_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBRequest,
    ) -> drds_20190123_models.DescribeDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbwith_options_async(request, runtime)

    def describe_drds_dbcluster_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            self.do_rpcrequest('DescribeDrdsDBCluster', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_dbcluster_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBClusterResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDBCluster', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbcluster(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbcluster_with_options(request, runtime)

    async def describe_drds_dbcluster_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBClusterRequest,
    ) -> drds_20190123_models.DescribeDrdsDBClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbcluster_with_options_async(request, runtime)

    def describe_drds_dbip_white_list_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            self.do_rpcrequest('DescribeDrdsDBIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_dbip_white_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBIpWhiteListResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDBIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbip_white_list(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbip_white_list_with_options(request, runtime)

    async def describe_drds_dbip_white_list_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBIpWhiteListRequest,
    ) -> drds_20190123_models.DescribeDrdsDBIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbip_white_list_with_options_async(request, runtime)

    def describe_drds_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            self.do_rpcrequest('DescribeDrdsDBs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDBsResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDBs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_dbs(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_dbs_with_options(request, runtime)

    async def describe_drds_dbs_async(
        self,
        request: drds_20190123_models.DescribeDrdsDBsRequest,
    ) -> drds_20190123_models.DescribeDrdsDBsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_dbs_with_options_async(request, runtime)

    def describe_drds_db_instance_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            self.do_rpcrequest('DescribeDrdsDbInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_db_instance_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstanceResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDbInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_instance(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instance_with_options(request, runtime)

    async def describe_drds_db_instance_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_instance_with_options_async(request, runtime)

    def describe_drds_db_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_db_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDbInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_instances(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_instances_with_options(request, runtime)

    async def describe_drds_db_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsDbInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_instances_with_options_async(request, runtime)

    def describe_drds_db_rds_name_list_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            self.do_rpcrequest('DescribeDrdsDbRdsNameList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_db_rds_name_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbRdsNameListResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDbRdsNameList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_rds_name_list(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_rds_name_list_with_options(request, runtime)

    async def describe_drds_db_rds_name_list_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbRdsNameListRequest,
    ) -> drds_20190123_models.DescribeDrdsDbRdsNameListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_rds_name_list_with_options_async(request, runtime)

    def describe_drds_db_spec_and_price_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbSpecAndPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse(),
            self.do_rpcrequest('DescribeDrdsDbSpecAndPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_db_spec_and_price_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbSpecAndPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDbSpecAndPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_spec_and_price(
        self,
        request: drds_20190123_models.DescribeDrdsDbSpecAndPriceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_spec_and_price_with_options(request, runtime)

    async def describe_drds_db_spec_and_price_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbSpecAndPriceRequest,
    ) -> drds_20190123_models.DescribeDrdsDbSpecAndPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_spec_and_price_with_options_async(request, runtime)

    def describe_drds_db_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            self.do_rpcrequest('DescribeDrdsDbTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_db_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsDbTasksResponse(),
            await self.do_rpcrequest_async('DescribeDrdsDbTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_db_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_db_tasks_with_options(request, runtime)

    async def describe_drds_db_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsDbTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsDbTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_db_tasks_with_options_async(request, runtime)

    def describe_drds_instance_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            self.do_rpcrequest('DescribeDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_with_options(request, runtime)

    async def describe_drds_instance_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_with_options_async(request, runtime)

    def describe_drds_instance_db_monitor_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceDbMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instance_db_monitor_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstanceDbMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_db_monitor(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_db_monitor_with_options(request, runtime)

    async def describe_drds_instance_db_monitor_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceDbMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceDbMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_db_monitor_with_options_async(request, runtime)

    def describe_drds_instance_level_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceLevelTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instance_level_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstanceLevelTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_level_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_level_tasks_with_options(request, runtime)

    async def describe_drds_instance_level_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceLevelTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceLevelTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_level_tasks_with_options_async(request, runtime)

    def describe_drds_instance_monitor_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instance_monitor_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceMonitorResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstanceMonitor', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_monitor(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_monitor_with_options(request, runtime)

    async def describe_drds_instance_monitor_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceMonitorRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_monitor_with_options_async(request, runtime)

    def describe_drds_instance_version_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            self.do_rpcrequest('DescribeDrdsInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instance_version_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstanceVersionResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instance_version(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instance_version_with_options(request, runtime)

    async def describe_drds_instance_version_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstanceVersionRequest,
    ) -> drds_20190123_models.DescribeDrdsInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instance_version_with_options_async(request, runtime)

    def describe_drds_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDrdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_instances(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_instances_with_options(request, runtime)

    async def describe_drds_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_instances_with_options_async(request, runtime)

    def describe_drds_params_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            self.do_rpcrequest('DescribeDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_params_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsParamsResponse(),
            await self.do_rpcrequest_async('DescribeDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_params(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_params_with_options(request, runtime)

    async def describe_drds_params_async(
        self,
        request: drds_20190123_models.DescribeDrdsParamsRequest,
    ) -> drds_20190123_models.DescribeDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_params_with_options_async(request, runtime)

    def describe_drds_rds_instances_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            self.do_rpcrequest('DescribeDrdsRdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_rds_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsRdsInstancesResponse(),
            await self.do_rpcrequest_async('DescribeDrdsRdsInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_rds_instances(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_rds_instances_with_options(request, runtime)

    async def describe_drds_rds_instances_async(
        self,
        request: drds_20190123_models.DescribeDrdsRdsInstancesRequest,
    ) -> drds_20190123_models.DescribeDrdsRdsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_rds_instances_with_options_async(request, runtime)

    def describe_drds_sharding_dbs_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            self.do_rpcrequest('DescribeDrdsShardingDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_sharding_dbs_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsShardingDbsResponse(),
            await self.do_rpcrequest_async('DescribeDrdsShardingDbs', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_sharding_dbs(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sharding_dbs_with_options(request, runtime)

    async def describe_drds_sharding_dbs_async(
        self,
        request: drds_20190123_models.DescribeDrdsShardingDbsRequest,
    ) -> drds_20190123_models.DescribeDrdsShardingDbsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_sharding_dbs_with_options_async(request, runtime)

    def describe_drds_slow_sqls_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            self.do_rpcrequest('DescribeDrdsSlowSqls', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_slow_sqls_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSlowSqlsResponse(),
            await self.do_rpcrequest_async('DescribeDrdsSlowSqls', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_slow_sqls(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_slow_sqls_with_options(request, runtime)

    async def describe_drds_slow_sqls_async(
        self,
        request: drds_20190123_models.DescribeDrdsSlowSqlsRequest,
    ) -> drds_20190123_models.DescribeDrdsSlowSqlsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_slow_sqls_with_options_async(request, runtime)

    def describe_drds_sql_audit_status_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            self.do_rpcrequest('DescribeDrdsSqlAuditStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_sql_audit_status_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsSqlAuditStatusResponse(),
            await self.do_rpcrequest_async('DescribeDrdsSqlAuditStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_sql_audit_status(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_sql_audit_status_with_options(request, runtime)

    async def describe_drds_sql_audit_status_async(
        self,
        request: drds_20190123_models.DescribeDrdsSqlAuditStatusRequest,
    ) -> drds_20190123_models.DescribeDrdsSqlAuditStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_sql_audit_status_with_options_async(request, runtime)

    def describe_drds_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            self.do_rpcrequest('DescribeDrdsTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_drds_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeDrdsTasksResponse(),
            await self.do_rpcrequest_async('DescribeDrdsTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_drds_tasks(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_drds_tasks_with_options(request, runtime)

    async def describe_drds_tasks_async(
        self,
        request: drds_20190123_models.DescribeDrdsTasksRequest,
    ) -> drds_20190123_models.DescribeDrdsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_drds_tasks_with_options_async(request, runtime)

    def describe_evaluate_data_import_db_topologys_with_options(
        self,
        tmp_req: drds_20190123_models.DescribeEvaluateDataImportDbTopologysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeEvaluateDataImportDbTopologysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse(),
            self.do_rpcrequest('DescribeEvaluateDataImportDbTopologys', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_data_import_db_topologys_with_options_async(
        self,
        tmp_req: drds_20190123_models.DescribeEvaluateDataImportDbTopologysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.DescribeEvaluateDataImportDbTopologysShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.import_param):
            request.import_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.import_param, 'ImportParam', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse(),
            await self.do_rpcrequest_async('DescribeEvaluateDataImportDbTopologys', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_data_import_db_topologys(
        self,
        request: drds_20190123_models.DescribeEvaluateDataImportDbTopologysRequest,
    ) -> drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_data_import_db_topologys_with_options(request, runtime)

    async def describe_evaluate_data_import_db_topologys_async(
        self,
        request: drds_20190123_models.DescribeEvaluateDataImportDbTopologysRequest,
    ) -> drds_20190123_models.DescribeEvaluateDataImportDbTopologysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_data_import_db_topologys_with_options_async(request, runtime)

    def describe_evaluate_pre_check_result_with_options(
        self,
        request: drds_20190123_models.DescribeEvaluatePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluatePreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluatePreCheckResultResponse(),
            self.do_rpcrequest('DescribeEvaluatePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_pre_check_result_with_options_async(
        self,
        request: drds_20190123_models.DescribeEvaluatePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluatePreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluatePreCheckResultResponse(),
            await self.do_rpcrequest_async('DescribeEvaluatePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_pre_check_result(
        self,
        request: drds_20190123_models.DescribeEvaluatePreCheckResultRequest,
    ) -> drds_20190123_models.DescribeEvaluatePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_pre_check_result_with_options(request, runtime)

    async def describe_evaluate_pre_check_result_async(
        self,
        request: drds_20190123_models.DescribeEvaluatePreCheckResultRequest,
    ) -> drds_20190123_models.DescribeEvaluatePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_pre_check_result_with_options_async(request, runtime)

    def describe_evaluate_task_report_with_options(
        self,
        request: drds_20190123_models.DescribeEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTaskReportResponse(),
            self.do_rpcrequest('DescribeEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_task_report_with_options_async(
        self,
        request: drds_20190123_models.DescribeEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTaskReportResponse(),
            await self.do_rpcrequest_async('DescribeEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_task_report(
        self,
        request: drds_20190123_models.DescribeEvaluateTaskReportRequest,
    ) -> drds_20190123_models.DescribeEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_task_report_with_options(request, runtime)

    async def describe_evaluate_task_report_async(
        self,
        request: drds_20190123_models.DescribeEvaluateTaskReportRequest,
    ) -> drds_20190123_models.DescribeEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_task_report_with_options_async(request, runtime)

    def describe_evaluate_tasks_with_options(
        self,
        request: drds_20190123_models.DescribeEvaluateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTasksResponse(),
            self.do_rpcrequest('DescribeEvaluateTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_evaluate_tasks_with_options_async(
        self,
        request: drds_20190123_models.DescribeEvaluateTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeEvaluateTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeEvaluateTasksResponse(),
            await self.do_rpcrequest_async('DescribeEvaluateTasks', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_evaluate_tasks(
        self,
        request: drds_20190123_models.DescribeEvaluateTasksRequest,
    ) -> drds_20190123_models.DescribeEvaluateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluate_tasks_with_options(request, runtime)

    async def describe_evaluate_tasks_async(
        self,
        request: drds_20190123_models.DescribeEvaluateTasksRequest,
    ) -> drds_20190123_models.DescribeEvaluateTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluate_tasks_with_options_async(request, runtime)

    def describe_expand_logic_table_info_list_with_options(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            self.do_rpcrequest('DescribeExpandLogicTableInfoList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_expand_logic_table_info_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeExpandLogicTableInfoListResponse(),
            await self.do_rpcrequest_async('DescribeExpandLogicTableInfoList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_expand_logic_table_info_list(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_expand_logic_table_info_list_with_options(request, runtime)

    async def describe_expand_logic_table_info_list_async(
        self,
        request: drds_20190123_models.DescribeExpandLogicTableInfoListRequest,
    ) -> drds_20190123_models.DescribeExpandLogicTableInfoListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_expand_logic_table_info_list_with_options_async(request, runtime)

    def describe_hi_store_instance_info_with_options(
        self,
        request: drds_20190123_models.DescribeHiStoreInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHiStoreInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHiStoreInstanceInfoResponse(),
            self.do_rpcrequest('DescribeHiStoreInstanceInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hi_store_instance_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeHiStoreInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHiStoreInstanceInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHiStoreInstanceInfoResponse(),
            await self.do_rpcrequest_async('DescribeHiStoreInstanceInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hi_store_instance_info(
        self,
        request: drds_20190123_models.DescribeHiStoreInstanceInfoRequest,
    ) -> drds_20190123_models.DescribeHiStoreInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hi_store_instance_info_with_options(request, runtime)

    async def describe_hi_store_instance_info_async(
        self,
        request: drds_20190123_models.DescribeHiStoreInstanceInfoRequest,
    ) -> drds_20190123_models.DescribeHiStoreInstanceInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hi_store_instance_info_with_options_async(request, runtime)

    def describe_hot_db_list_with_options(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            self.do_rpcrequest('DescribeHotDbList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_hot_db_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeHotDbListResponse(),
            await self.do_rpcrequest_async('DescribeHotDbList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_hot_db_list(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_hot_db_list_with_options(request, runtime)

    async def describe_hot_db_list_async(
        self,
        request: drds_20190123_models.DescribeHotDbListRequest,
    ) -> drds_20190123_models.DescribeHotDbListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_hot_db_list_with_options_async(request, runtime)

    def describe_inst_db_log_info_with_options(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            self.do_rpcrequest('DescribeInstDbLogInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_inst_db_log_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbLogInfoResponse(),
            await self.do_rpcrequest_async('DescribeInstDbLogInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_inst_db_log_info(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_log_info_with_options(request, runtime)

    async def describe_inst_db_log_info_async(
        self,
        request: drds_20190123_models.DescribeInstDbLogInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbLogInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inst_db_log_info_with_options_async(request, runtime)

    def describe_inst_db_sls_info_with_options(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            self.do_rpcrequest('DescribeInstDbSlsInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_inst_db_sls_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstDbSlsInfoResponse(),
            await self.do_rpcrequest_async('DescribeInstDbSlsInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_inst_db_sls_info(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_inst_db_sls_info_with_options(request, runtime)

    async def describe_inst_db_sls_info_async(
        self,
        request: drds_20190123_models.DescribeInstDbSlsInfoRequest,
    ) -> drds_20190123_models.DescribeInstDbSlsInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_inst_db_sls_info_with_options_async(request, runtime)

    def describe_instance_accounts_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            self.do_rpcrequest('DescribeInstanceAccounts', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_accounts_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceAccountsResponse(),
            await self.do_rpcrequest_async('DescribeInstanceAccounts', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_accounts(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_accounts_with_options(request, runtime)

    async def describe_instance_accounts_async(
        self,
        request: drds_20190123_models.DescribeInstanceAccountsRequest,
    ) -> drds_20190123_models.DescribeInstanceAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_accounts_with_options_async(request, runtime)

    def describe_instance_menu_switch_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceMenuSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceMenuSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceMenuSwitchResponse(),
            self.do_rpcrequest('DescribeInstanceMenuSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_menu_switch_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceMenuSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceMenuSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceMenuSwitchResponse(),
            await self.do_rpcrequest_async('DescribeInstanceMenuSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_menu_switch(
        self,
        request: drds_20190123_models.DescribeInstanceMenuSwitchRequest,
    ) -> drds_20190123_models.DescribeInstanceMenuSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_menu_switch_with_options(request, runtime)

    async def describe_instance_menu_switch_async(
        self,
        request: drds_20190123_models.DescribeInstanceMenuSwitchRequest,
    ) -> drds_20190123_models.DescribeInstanceMenuSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_menu_switch_with_options_async(request, runtime)

    def describe_instance_switch_azone_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            self.do_rpcrequest('DescribeInstanceSwitchAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_switch_azone_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchAzoneResponse(),
            await self.do_rpcrequest_async('DescribeInstanceSwitchAzone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_switch_azone(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_azone_with_options(request, runtime)

    async def describe_instance_switch_azone_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchAzoneRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchAzoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_switch_azone_with_options_async(request, runtime)

    def describe_instance_switch_network_with_options(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            self.do_rpcrequest('DescribeInstanceSwitchNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_instance_switch_network_with_options_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeInstanceSwitchNetworkResponse(),
            await self.do_rpcrequest_async('DescribeInstanceSwitchNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_instance_switch_network(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_switch_network_with_options(request, runtime)

    async def describe_instance_switch_network_async(
        self,
        request: drds_20190123_models.DescribeInstanceSwitchNetworkRequest,
    ) -> drds_20190123_models.DescribeInstanceSwitchNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_switch_network_with_options_async(request, runtime)

    def describe_pre_check_result_with_options(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            self.do_rpcrequest('DescribePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_pre_check_result_with_options_async(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribePreCheckResultResponse(),
            await self.do_rpcrequest_async('DescribePreCheckResult', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_pre_check_result(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_result_with_options(request, runtime)

    async def describe_pre_check_result_async(
        self,
        request: drds_20190123_models.DescribePreCheckResultRequest,
    ) -> drds_20190123_models.DescribePreCheckResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_result_with_options_async(request, runtime)

    def describe_rdsperformance_with_options(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            self.do_rpcrequest('DescribeRDSPerformance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rdsperformance_with_options_async(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRDSPerformanceResponse(),
            await self.do_rpcrequest_async('DescribeRDSPerformance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rdsperformance(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rdsperformance_with_options(request, runtime)

    async def describe_rdsperformance_async(
        self,
        request: drds_20190123_models.DescribeRDSPerformanceRequest,
    ) -> drds_20190123_models.DescribeRDSPerformanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rdsperformance_with_options_async(request, runtime)

    def describe_rds_commodity_with_options(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            self.do_rpcrequest('DescribeRdsCommodity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_commodity_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsCommodityResponse(),
            await self.do_rpcrequest_async('DescribeRdsCommodity', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_commodity(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_commodity_with_options(request, runtime)

    async def describe_rds_commodity_async(
        self,
        request: drds_20190123_models.DescribeRdsCommodityRequest,
    ) -> drds_20190123_models.DescribeRdsCommodityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_commodity_with_options_async(request, runtime)

    def describe_rds_drds_dbwith_options(
        self,
        request: drds_20190123_models.DescribeRdsDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsDrdsDBResponse(),
            self.do_rpcrequest('DescribeRdsDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_drds_dbwith_options_async(
        self,
        request: drds_20190123_models.DescribeRdsDrdsDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsDrdsDBResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsDrdsDBResponse(),
            await self.do_rpcrequest_async('DescribeRdsDrdsDB', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_drds_db(
        self,
        request: drds_20190123_models.DescribeRdsDrdsDBRequest,
    ) -> drds_20190123_models.DescribeRdsDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_drds_dbwith_options(request, runtime)

    async def describe_rds_drds_db_async(
        self,
        request: drds_20190123_models.DescribeRdsDrdsDBRequest,
    ) -> drds_20190123_models.DescribeRdsDrdsDBResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_drds_dbwith_options_async(request, runtime)

    def describe_rds_performance_summary_with_options(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            self.do_rpcrequest('DescribeRdsPerformanceSummary', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_performance_summary_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPerformanceSummaryResponse(),
            await self.do_rpcrequest_async('DescribeRdsPerformanceSummary', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_performance_summary(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_performance_summary_with_options(request, runtime)

    async def describe_rds_performance_summary_async(
        self,
        request: drds_20190123_models.DescribeRdsPerformanceSummaryRequest,
    ) -> drds_20190123_models.DescribeRdsPerformanceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_performance_summary_with_options_async(request, runtime)

    def describe_rds_price_with_options(
        self,
        request: drds_20190123_models.DescribeRdsPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPriceResponse(),
            self.do_rpcrequest('DescribeRdsPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_price_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsPriceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsPriceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsPriceResponse(),
            await self.do_rpcrequest_async('DescribeRdsPrice', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_price(
        self,
        request: drds_20190123_models.DescribeRdsPriceRequest,
    ) -> drds_20190123_models.DescribeRdsPriceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_price_with_options(request, runtime)

    async def describe_rds_price_async(
        self,
        request: drds_20190123_models.DescribeRdsPriceRequest,
    ) -> drds_20190123_models.DescribeRdsPriceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_price_with_options_async(request, runtime)

    def describe_rds_read_only_with_options(
        self,
        request: drds_20190123_models.DescribeRdsReadOnlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsReadOnlyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsReadOnlyResponse(),
            self.do_rpcrequest('DescribeRdsReadOnly', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_read_only_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsReadOnlyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsReadOnlyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsReadOnlyResponse(),
            await self.do_rpcrequest_async('DescribeRdsReadOnly', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_read_only(
        self,
        request: drds_20190123_models.DescribeRdsReadOnlyRequest,
    ) -> drds_20190123_models.DescribeRdsReadOnlyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_read_only_with_options(request, runtime)

    async def describe_rds_read_only_async(
        self,
        request: drds_20190123_models.DescribeRdsReadOnlyRequest,
    ) -> drds_20190123_models.DescribeRdsReadOnlyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_read_only_with_options_async(request, runtime)

    def describe_rds_super_account_instances_with_options(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            self.do_rpcrequest('DescribeRdsSuperAccountInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_super_account_instances_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsSuperAccountInstancesResponse(),
            await self.do_rpcrequest_async('DescribeRdsSuperAccountInstances', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_super_account_instances(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_super_account_instances_with_options(request, runtime)

    async def describe_rds_super_account_instances_async(
        self,
        request: drds_20190123_models.DescribeRdsSuperAccountInstancesRequest,
    ) -> drds_20190123_models.DescribeRdsSuperAccountInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_super_account_instances_with_options_async(request, runtime)

    def describe_rds_vpc_for_zone_with_options(
        self,
        request: drds_20190123_models.DescribeRdsVpcForZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsVpcForZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsVpcForZoneResponse(),
            self.do_rpcrequest('DescribeRdsVpcForZone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_vpc_for_zone_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsVpcForZoneRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsVpcForZoneResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsVpcForZoneResponse(),
            await self.do_rpcrequest_async('DescribeRdsVpcForZone', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_vpc_for_zone(
        self,
        request: drds_20190123_models.DescribeRdsVpcForZoneRequest,
    ) -> drds_20190123_models.DescribeRdsVpcForZoneResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_vpc_for_zone_with_options(request, runtime)

    async def describe_rds_vpc_for_zone_async(
        self,
        request: drds_20190123_models.DescribeRdsVpcForZoneRequest,
    ) -> drds_20190123_models.DescribeRdsVpcForZoneResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_vpc_for_zone_with_options_async(request, runtime)

    def describe_recycle_bin_status_with_options(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            self.do_rpcrequest('DescribeRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_recycle_bin_status_with_options_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinStatusResponse(),
            await self.do_rpcrequest_async('DescribeRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recycle_bin_status(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_status_with_options(request, runtime)

    async def describe_recycle_bin_status_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinStatusRequest,
    ) -> drds_20190123_models.DescribeRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recycle_bin_status_with_options_async(request, runtime)

    def describe_recycle_bin_tables_with_options(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            self.do_rpcrequest('DescribeRecycleBinTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_recycle_bin_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRecycleBinTablesResponse(),
            await self.do_rpcrequest_async('DescribeRecycleBinTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_recycle_bin_tables(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_recycle_bin_tables_with_options(request, runtime)

    async def describe_recycle_bin_tables_async(
        self,
        request: drds_20190123_models.DescribeRecycleBinTablesRequest,
    ) -> drds_20190123_models.DescribeRecycleBinTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_recycle_bin_tables_with_options_async(request, runtime)

    def describe_restore_order_with_options(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            self.do_rpcrequest('DescribeRestoreOrder', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_restore_order_with_options_async(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRestoreOrderResponse(),
            await self.do_rpcrequest_async('DescribeRestoreOrder', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_restore_order(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_order_with_options(request, runtime)

    async def describe_restore_order_async(
        self,
        request: drds_20190123_models.DescribeRestoreOrderRequest,
    ) -> drds_20190123_models.DescribeRestoreOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_order_with_options_async(request, runtime)

    def describe_shard_task_info_with_options(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            self.do_rpcrequest('DescribeShardTaskInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_shard_task_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskInfoResponse(),
            await self.do_rpcrequest_async('DescribeShardTaskInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shard_task_info(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_info_with_options(request, runtime)

    async def describe_shard_task_info_async(
        self,
        request: drds_20190123_models.DescribeShardTaskInfoRequest,
    ) -> drds_20190123_models.DescribeShardTaskInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_task_info_with_options_async(request, runtime)

    def describe_shard_task_list_with_options(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            self.do_rpcrequest('DescribeShardTaskList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_shard_task_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeShardTaskListResponse(),
            await self.do_rpcrequest_async('DescribeShardTaskList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shard_task_list(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_shard_task_list_with_options(request, runtime)

    async def describe_shard_task_list_async(
        self,
        request: drds_20190123_models.DescribeShardTaskListRequest,
    ) -> drds_20190123_models.DescribeShardTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_shard_task_list_with_options_async(request, runtime)

    def describe_sql_flashbak_task_with_options(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            self.do_rpcrequest('DescribeSqlFlashbakTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_sql_flashbak_task_with_options_async(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSqlFlashbakTaskResponse(),
            await self.do_rpcrequest_async('DescribeSqlFlashbakTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sql_flashbak_task(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_sql_flashbak_task_with_options(request, runtime)

    async def describe_sql_flashbak_task_async(
        self,
        request: drds_20190123_models.DescribeSqlFlashbakTaskRequest,
    ) -> drds_20190123_models.DescribeSqlFlashbakTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_sql_flashbak_task_with_options_async(request, runtime)

    def describe_src_rds_list_with_options(
        self,
        request: drds_20190123_models.DescribeSrcRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSrcRdsListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSrcRdsListResponse(),
            self.do_rpcrequest('DescribeSrcRdsList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_src_rds_list_with_options_async(
        self,
        request: drds_20190123_models.DescribeSrcRdsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeSrcRdsListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeSrcRdsListResponse(),
            await self.do_rpcrequest_async('DescribeSrcRdsList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_src_rds_list(
        self,
        request: drds_20190123_models.DescribeSrcRdsListRequest,
    ) -> drds_20190123_models.DescribeSrcRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_src_rds_list_with_options(request, runtime)

    async def describe_src_rds_list_async(
        self,
        request: drds_20190123_models.DescribeSrcRdsListRequest,
    ) -> drds_20190123_models.DescribeSrcRdsListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_src_rds_list_with_options_async(request, runtime)

    def describe_table_with_options(
        self,
        request: drds_20190123_models.DescribeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            self.do_rpcrequest('DescribeTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_table_with_options_async(
        self,
        request: drds_20190123_models.DescribeTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableResponse(),
            await self.do_rpcrequest_async('DescribeTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table(
        self,
        request: drds_20190123_models.DescribeTableRequest,
    ) -> drds_20190123_models.DescribeTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_with_options(request, runtime)

    async def describe_table_async(
        self,
        request: drds_20190123_models.DescribeTableRequest,
    ) -> drds_20190123_models.DescribeTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_with_options_async(request, runtime)

    def describe_table_list_by_type_with_options(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            self.do_rpcrequest('DescribeTableListByType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_table_list_by_type_with_options_async(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableListByTypeResponse(),
            await self.do_rpcrequest_async('DescribeTableListByType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_list_by_type(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_list_by_type_with_options(request, runtime)

    async def describe_table_list_by_type_async(
        self,
        request: drds_20190123_models.DescribeTableListByTypeRequest,
    ) -> drds_20190123_models.DescribeTableListByTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_list_by_type_with_options_async(request, runtime)

    def describe_table_sharding_info_with_options(
        self,
        request: drds_20190123_models.DescribeTableShardingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableShardingInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableShardingInfoResponse(),
            self.do_rpcrequest('DescribeTableShardingInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_table_sharding_info_with_options_async(
        self,
        request: drds_20190123_models.DescribeTableShardingInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTableShardingInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTableShardingInfoResponse(),
            await self.do_rpcrequest_async('DescribeTableShardingInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_table_sharding_info(
        self,
        request: drds_20190123_models.DescribeTableShardingInfoRequest,
    ) -> drds_20190123_models.DescribeTableShardingInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_table_sharding_info_with_options(request, runtime)

    async def describe_table_sharding_info_async(
        self,
        request: drds_20190123_models.DescribeTableShardingInfoRequest,
    ) -> drds_20190123_models.DescribeTableShardingInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_table_sharding_info_with_options_async(request, runtime)

    def describe_tables_with_options(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            self.do_rpcrequest('DescribeTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tables_with_options_async(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeTablesResponse(),
            await self.do_rpcrequest_async('DescribeTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tables(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
    ) -> drds_20190123_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tables_with_options(request, runtime)

    async def describe_tables_async(
        self,
        request: drds_20190123_models.DescribeTablesRequest,
    ) -> drds_20190123_models.DescribeTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tables_with_options_async(request, runtime)

    def disable_sql_audit_with_options(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            self.do_rpcrequest('DisableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_sql_audit_with_options_async(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DisableSqlAuditResponse(),
            await self.do_rpcrequest_async('DisableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_sql_audit(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_sql_audit_with_options(request, runtime)

    async def disable_sql_audit_async(
        self,
        request: drds_20190123_models.DisableSqlAuditRequest,
    ) -> drds_20190123_models.DisableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_sql_audit_with_options_async(request, runtime)

    def enable_instance_ipv_6address_with_options(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            self.do_rpcrequest('EnableInstanceIpv6Address', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_instance_ipv_6address_with_options_async(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableInstanceIpv6AddressResponse(),
            await self.do_rpcrequest_async('EnableInstanceIpv6Address', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_instance_ipv_6address(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_ipv_6address_with_options(request, runtime)

    async def enable_instance_ipv_6address_async(
        self,
        request: drds_20190123_models.EnableInstanceIpv6AddressRequest,
    ) -> drds_20190123_models.EnableInstanceIpv6AddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_instance_ipv_6address_with_options_async(request, runtime)

    def enable_sql_audit_with_options(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            self.do_rpcrequest('EnableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_sql_audit_with_options_async(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlAuditResponse(),
            await self.do_rpcrequest_async('EnableSqlAudit', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_audit(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_audit_with_options(request, runtime)

    async def enable_sql_audit_async(
        self,
        request: drds_20190123_models.EnableSqlAuditRequest,
    ) -> drds_20190123_models.EnableSqlAuditResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_audit_with_options_async(request, runtime)

    def enable_sql_flashback_match_switch_with_options(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            self.do_rpcrequest('EnableSqlFlashbackMatchSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_sql_flashback_match_switch_with_options_async(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse(),
            await self.do_rpcrequest_async('EnableSqlFlashbackMatchSwitch', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_sql_flashback_match_switch(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_sql_flashback_match_switch_with_options(request, runtime)

    async def enable_sql_flashback_match_switch_async(
        self,
        request: drds_20190123_models.EnableSqlFlashbackMatchSwitchRequest,
    ) -> drds_20190123_models.EnableSqlFlashbackMatchSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_sql_flashback_match_switch_with_options_async(request, runtime)

    def flashback_recycle_bin_table_with_options(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            self.do_rpcrequest('FlashbackRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def flashback_recycle_bin_table_with_options_async(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.FlashbackRecycleBinTableResponse(),
            await self.do_rpcrequest_async('FlashbackRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def flashback_recycle_bin_table(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.flashback_recycle_bin_table_with_options(request, runtime)

    async def flashback_recycle_bin_table_async(
        self,
        request: drds_20190123_models.FlashbackRecycleBinTableRequest,
    ) -> drds_20190123_models.FlashbackRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.flashback_recycle_bin_table_with_options_async(request, runtime)

    def get_batch_evaluate_task_report_with_options(
        self,
        request: drds_20190123_models.GetBatchEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetBatchEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetBatchEvaluateTaskReportResponse(),
            self.do_rpcrequest('GetBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_batch_evaluate_task_report_with_options_async(
        self,
        request: drds_20190123_models.GetBatchEvaluateTaskReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetBatchEvaluateTaskReportResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetBatchEvaluateTaskReportResponse(),
            await self.do_rpcrequest_async('GetBatchEvaluateTaskReport', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_batch_evaluate_task_report(
        self,
        request: drds_20190123_models.GetBatchEvaluateTaskReportRequest,
    ) -> drds_20190123_models.GetBatchEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_batch_evaluate_task_report_with_options(request, runtime)

    async def get_batch_evaluate_task_report_async(
        self,
        request: drds_20190123_models.GetBatchEvaluateTaskReportRequest,
    ) -> drds_20190123_models.GetBatchEvaluateTaskReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_batch_evaluate_task_report_with_options_async(request, runtime)

    def get_drds_db_rds_relation_info_with_options(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            self.do_rpcrequest('GetDrdsDbRdsRelationInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_drds_db_rds_relation_info_with_options_async(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.GetDrdsDbRdsRelationInfoResponse(),
            await self.do_rpcrequest_async('GetDrdsDbRdsRelationInfo', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_drds_db_rds_relation_info(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_drds_db_rds_relation_info_with_options(request, runtime)

    async def get_drds_db_rds_relation_info_async(
        self,
        request: drds_20190123_models.GetDrdsDbRdsRelationInfoRequest,
    ) -> drds_20190123_models.GetDrdsDbRdsRelationInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_drds_db_rds_relation_info_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: drds_20190123_models.ListTagResourcesRequest,
    ) -> drds_20190123_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_reports_with_options(
        self,
        request: drds_20190123_models.ListUserReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListUserReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListUserReportsResponse(),
            self.do_rpcrequest('ListUserReports', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_user_reports_with_options_async(
        self,
        request: drds_20190123_models.ListUserReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListUserReportsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListUserReportsResponse(),
            await self.do_rpcrequest_async('ListUserReports', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_user_reports(
        self,
        request: drds_20190123_models.ListUserReportsRequest,
    ) -> drds_20190123_models.ListUserReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_user_reports_with_options(request, runtime)

    async def list_user_reports_async(
        self,
        request: drds_20190123_models.ListUserReportsRequest,
    ) -> drds_20190123_models.ListUserReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_user_reports_with_options_async(request, runtime)

    def list_versions_with_options(
        self,
        request: drds_20190123_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListVersionsResponse(),
            self.do_rpcrequest('ListVersions', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_versions_with_options_async(
        self,
        request: drds_20190123_models.ListVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ListVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ListVersionsResponse(),
            await self.do_rpcrequest_async('ListVersions', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_versions(
        self,
        request: drds_20190123_models.ListVersionsRequest,
    ) -> drds_20190123_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_versions_with_options(request, runtime)

    async def list_versions_async(
        self,
        request: drds_20190123_models.ListVersionsRequest,
    ) -> drds_20190123_models.ListVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_versions_with_options_async(request, runtime)

    def manage_private_rds_with_options(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            self.do_rpcrequest('ManagePrivateRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def manage_private_rds_with_options_async(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ManagePrivateRdsResponse(),
            await self.do_rpcrequest_async('ManagePrivateRds', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def manage_private_rds(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.manage_private_rds_with_options(request, runtime)

    async def manage_private_rds_async(
        self,
        request: drds_20190123_models.ManagePrivateRdsRequest,
    ) -> drds_20190123_models.ManagePrivateRdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.manage_private_rds_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            self.do_rpcrequest('ModifyAccountDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyAccountDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_description(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: drds_20190123_models.ModifyAccountDescriptionRequest,
    ) -> drds_20190123_models.ModifyAccountDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_account_privilege_with_options(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            self.do_rpcrequest('ModifyAccountPrivilege', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_account_privilege_with_options_async(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyAccountPrivilegeResponse(),
            await self.do_rpcrequest_async('ModifyAccountPrivilege', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_account_privilege(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_account_privilege_with_options(request, runtime)

    async def modify_account_privilege_async(
        self,
        request: drds_20190123_models.ModifyAccountPrivilegeRequest,
    ) -> drds_20190123_models.ModifyAccountPrivilegeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_privilege_with_options_async(request, runtime)

    def modify_drds_instance_description_with_options(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            self.do_rpcrequest('ModifyDrdsInstanceDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_drds_instance_description_with_options_async(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsInstanceDescriptionResponse(),
            await self.do_rpcrequest_async('ModifyDrdsInstanceDescription', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_drds_instance_description(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_instance_description_with_options(request, runtime)

    async def modify_drds_instance_description_async(
        self,
        request: drds_20190123_models.ModifyDrdsInstanceDescriptionRequest,
    ) -> drds_20190123_models.ModifyDrdsInstanceDescriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_instance_description_with_options_async(request, runtime)

    def modify_drds_ip_white_list_with_options(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            self.do_rpcrequest('ModifyDrdsIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_drds_ip_white_list_with_options_async(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyDrdsIpWhiteListResponse(),
            await self.do_rpcrequest_async('ModifyDrdsIpWhiteList', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_drds_ip_white_list(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_drds_ip_white_list_with_options(request, runtime)

    async def modify_drds_ip_white_list_async(
        self,
        request: drds_20190123_models.ModifyDrdsIpWhiteListRequest,
    ) -> drds_20190123_models.ModifyDrdsIpWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_drds_ip_white_list_with_options_async(request, runtime)

    def modify_event_task_status_with_options(
        self,
        request: drds_20190123_models.ModifyEventTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyEventTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyEventTaskStatusResponse(),
            self.do_rpcrequest('ModifyEventTaskStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_event_task_status_with_options_async(
        self,
        request: drds_20190123_models.ModifyEventTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyEventTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyEventTaskStatusResponse(),
            await self.do_rpcrequest_async('ModifyEventTaskStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_event_task_status(
        self,
        request: drds_20190123_models.ModifyEventTaskStatusRequest,
    ) -> drds_20190123_models.ModifyEventTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_event_task_status_with_options(request, runtime)

    async def modify_event_task_status_async(
        self,
        request: drds_20190123_models.ModifyEventTaskStatusRequest,
    ) -> drds_20190123_models.ModifyEventTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_event_task_status_with_options_async(request, runtime)

    def modify_polar_db_read_weight_with_options(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            self.do_rpcrequest('ModifyPolarDbReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_polar_db_read_weight_with_options_async(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyPolarDbReadWeightResponse(),
            await self.do_rpcrequest_async('ModifyPolarDbReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_polar_db_read_weight(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_polar_db_read_weight_with_options(request, runtime)

    async def modify_polar_db_read_weight_async(
        self,
        request: drds_20190123_models.ModifyPolarDbReadWeightRequest,
    ) -> drds_20190123_models.ModifyPolarDbReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_polar_db_read_weight_with_options_async(request, runtime)

    def modify_rds_read_weight_with_options(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            self.do_rpcrequest('ModifyRdsReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_rds_read_weight_with_options_async(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ModifyRdsReadWeightResponse(),
            await self.do_rpcrequest_async('ModifyRdsReadWeight', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_rds_read_weight(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_rds_read_weight_with_options(request, runtime)

    async def modify_rds_read_weight_async(
        self,
        request: drds_20190123_models.ModifyRdsReadWeightRequest,
    ) -> drds_20190123_models.ModifyRdsReadWeightResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_rds_read_weight_with_options_async(request, runtime)

    def my_cat_connect_test_with_options(
        self,
        request: drds_20190123_models.MyCatConnectTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.MyCatConnectTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatConnectTestResponse(),
            self.do_rpcrequest('MyCatConnectTest', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def my_cat_connect_test_with_options_async(
        self,
        request: drds_20190123_models.MyCatConnectTestRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.MyCatConnectTestResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatConnectTestResponse(),
            await self.do_rpcrequest_async('MyCatConnectTest', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def my_cat_connect_test(
        self,
        request: drds_20190123_models.MyCatConnectTestRequest,
    ) -> drds_20190123_models.MyCatConnectTestResponse:
        runtime = util_models.RuntimeOptions()
        return self.my_cat_connect_test_with_options(request, runtime)

    async def my_cat_connect_test_async(
        self,
        request: drds_20190123_models.MyCatConnectTestRequest,
    ) -> drds_20190123_models.MyCatConnectTestResponse:
        runtime = util_models.RuntimeOptions()
        return await self.my_cat_connect_test_with_options_async(request, runtime)

    def my_cat_custom_import_pre_check_with_options(
        self,
        tmp_req: drds_20190123_models.MyCatCustomImportPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.MyCatCustomImportPreCheckResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.MyCatCustomImportPreCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_map):
            request.table_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_map, 'TableMap', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatCustomImportPreCheckResponse(),
            self.do_rpcrequest('MyCatCustomImportPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def my_cat_custom_import_pre_check_with_options_async(
        self,
        tmp_req: drds_20190123_models.MyCatCustomImportPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.MyCatCustomImportPreCheckResponse:
        UtilClient.validate_model(tmp_req)
        request = drds_20190123_models.MyCatCustomImportPreCheckShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.table_map):
            request.table_map_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.table_map, 'TableMap', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.MyCatCustomImportPreCheckResponse(),
            await self.do_rpcrequest_async('MyCatCustomImportPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def my_cat_custom_import_pre_check(
        self,
        request: drds_20190123_models.MyCatCustomImportPreCheckRequest,
    ) -> drds_20190123_models.MyCatCustomImportPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.my_cat_custom_import_pre_check_with_options(request, runtime)

    async def my_cat_custom_import_pre_check_async(
        self,
        request: drds_20190123_models.MyCatCustomImportPreCheckRequest,
    ) -> drds_20190123_models.MyCatCustomImportPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.my_cat_custom_import_pre_check_with_options_async(request, runtime)

    def pre_check_modify_table_sharding_key_param_with_options(
        self,
        request: drds_20190123_models.PreCheckModifyTableShardingKeyParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse(),
            self.do_rpcrequest('PreCheckModifyTableShardingKeyParam', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pre_check_modify_table_sharding_key_param_with_options_async(
        self,
        request: drds_20190123_models.PreCheckModifyTableShardingKeyParamRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse(),
            await self.do_rpcrequest_async('PreCheckModifyTableShardingKeyParam', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pre_check_modify_table_sharding_key_param(
        self,
        request: drds_20190123_models.PreCheckModifyTableShardingKeyParamRequest,
    ) -> drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse:
        runtime = util_models.RuntimeOptions()
        return self.pre_check_modify_table_sharding_key_param_with_options(request, runtime)

    async def pre_check_modify_table_sharding_key_param_async(
        self,
        request: drds_20190123_models.PreCheckModifyTableShardingKeyParamRequest,
    ) -> drds_20190123_models.PreCheckModifyTableShardingKeyParamResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pre_check_modify_table_sharding_key_param_with_options_async(request, runtime)

    def pre_check_sql_flashback_task_with_options(
        self,
        request: drds_20190123_models.PreCheckSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PreCheckSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckSqlFlashbackTaskResponse(),
            self.do_rpcrequest('PreCheckSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def pre_check_sql_flashback_task_with_options_async(
        self,
        request: drds_20190123_models.PreCheckSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PreCheckSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PreCheckSqlFlashbackTaskResponse(),
            await self.do_rpcrequest_async('PreCheckSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def pre_check_sql_flashback_task(
        self,
        request: drds_20190123_models.PreCheckSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.PreCheckSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.pre_check_sql_flashback_task_with_options(request, runtime)

    async def pre_check_sql_flashback_task_async(
        self,
        request: drds_20190123_models.PreCheckSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.PreCheckSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.pre_check_sql_flashback_task_with_options_async(request, runtime)

    def precheck_my_cat_evaluate_with_options(
        self,
        request: drds_20190123_models.PrecheckMyCatEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PrecheckMyCatEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PrecheckMyCatEvaluateResponse(),
            self.do_rpcrequest('PrecheckMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def precheck_my_cat_evaluate_with_options_async(
        self,
        request: drds_20190123_models.PrecheckMyCatEvaluateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PrecheckMyCatEvaluateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PrecheckMyCatEvaluateResponse(),
            await self.do_rpcrequest_async('PrecheckMyCatEvaluate', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def precheck_my_cat_evaluate(
        self,
        request: drds_20190123_models.PrecheckMyCatEvaluateRequest,
    ) -> drds_20190123_models.PrecheckMyCatEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return self.precheck_my_cat_evaluate_with_options(request, runtime)

    async def precheck_my_cat_evaluate_async(
        self,
        request: drds_20190123_models.PrecheckMyCatEvaluateRequest,
    ) -> drds_20190123_models.PrecheckMyCatEvaluateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.precheck_my_cat_evaluate_with_options_async(request, runtime)

    def put_restore_pre_check_with_options(
        self,
        request: drds_20190123_models.PutRestorePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutRestorePreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutRestorePreCheckResponse(),
            self.do_rpcrequest('PutRestorePreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_restore_pre_check_with_options_async(
        self,
        request: drds_20190123_models.PutRestorePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutRestorePreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutRestorePreCheckResponse(),
            await self.do_rpcrequest_async('PutRestorePreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_restore_pre_check(
        self,
        request: drds_20190123_models.PutRestorePreCheckRequest,
    ) -> drds_20190123_models.PutRestorePreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_restore_pre_check_with_options(request, runtime)

    async def put_restore_pre_check_async(
        self,
        request: drds_20190123_models.PutRestorePreCheckRequest,
    ) -> drds_20190123_models.PutRestorePreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_restore_pre_check_with_options_async(request, runtime)

    def put_start_backup_with_options(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutStartBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            self.do_rpcrequest('PutStartBackup', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_start_backup_with_options_async(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.PutStartBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.PutStartBackupResponse(),
            await self.do_rpcrequest_async('PutStartBackup', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_start_backup(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
    ) -> drds_20190123_models.PutStartBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_start_backup_with_options(request, runtime)

    async def put_start_backup_async(
        self,
        request: drds_20190123_models.PutStartBackupRequest,
    ) -> drds_20190123_models.PutStartBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_start_backup_with_options_async(request, runtime)

    def rearrange_db_to_instance_with_options(
        self,
        request: drds_20190123_models.RearrangeDbToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RearrangeDbToInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RearrangeDbToInstanceResponse(),
            self.do_rpcrequest('RearrangeDbToInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rearrange_db_to_instance_with_options_async(
        self,
        request: drds_20190123_models.RearrangeDbToInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RearrangeDbToInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RearrangeDbToInstanceResponse(),
            await self.do_rpcrequest_async('RearrangeDbToInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rearrange_db_to_instance(
        self,
        request: drds_20190123_models.RearrangeDbToInstanceRequest,
    ) -> drds_20190123_models.RearrangeDbToInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rearrange_db_to_instance_with_options(request, runtime)

    async def rearrange_db_to_instance_async(
        self,
        request: drds_20190123_models.RearrangeDbToInstanceRequest,
    ) -> drds_20190123_models.RearrangeDbToInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rearrange_db_to_instance_with_options_async(request, runtime)

    def refresh_drds_atom_url_with_options(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            self.do_rpcrequest('RefreshDrdsAtomUrl', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_drds_atom_url_with_options_async(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RefreshDrdsAtomUrlResponse(),
            await self.do_rpcrequest_async('RefreshDrdsAtomUrl', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_drds_atom_url(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_drds_atom_url_with_options(request, runtime)

    async def refresh_drds_atom_url_async(
        self,
        request: drds_20190123_models.RefreshDrdsAtomUrlRequest,
    ) -> drds_20190123_models.RefreshDrdsAtomUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_drds_atom_url_with_options_async(request, runtime)

    def release_instance_internet_address_with_options(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            self.do_rpcrequest('ReleaseInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_instance_internet_address_with_options_async(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ReleaseInstanceInternetAddressResponse(),
            await self.do_rpcrequest_async('ReleaseInstanceInternetAddress', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance_internet_address(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_instance_internet_address_with_options(request, runtime)

    async def release_instance_internet_address_async(
        self,
        request: drds_20190123_models.ReleaseInstanceInternetAddressRequest,
    ) -> drds_20190123_models.ReleaseInstanceInternetAddressResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_instance_internet_address_with_options_async(request, runtime)

    def remove_backups_set_with_options(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            self.do_rpcrequest('RemoveBackupsSet', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_backups_set_with_options_async(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveBackupsSetResponse(),
            await self.do_rpcrequest_async('RemoveBackupsSet', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_backups_set(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_backups_set_with_options(request, runtime)

    async def remove_backups_set_async(
        self,
        request: drds_20190123_models.RemoveBackupsSetRequest,
    ) -> drds_20190123_models.RemoveBackupsSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_backups_set_with_options_async(request, runtime)

    def remove_data_export_task_with_options(
        self,
        request: drds_20190123_models.RemoveDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataExportTaskResponse(),
            self.do_rpcrequest('RemoveDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_data_export_task_with_options_async(
        self,
        request: drds_20190123_models.RemoveDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataExportTaskResponse(),
            await self.do_rpcrequest_async('RemoveDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_data_export_task(
        self,
        request: drds_20190123_models.RemoveDataExportTaskRequest,
    ) -> drds_20190123_models.RemoveDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_data_export_task_with_options(request, runtime)

    async def remove_data_export_task_async(
        self,
        request: drds_20190123_models.RemoveDataExportTaskRequest,
    ) -> drds_20190123_models.RemoveDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_data_export_task_with_options_async(request, runtime)

    def remove_data_import_task_with_options(
        self,
        request: drds_20190123_models.RemoveDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDataImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataImportTaskResponse(),
            self.do_rpcrequest('RemoveDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_data_import_task_with_options_async(
        self,
        request: drds_20190123_models.RemoveDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDataImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDataImportTaskResponse(),
            await self.do_rpcrequest_async('RemoveDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_data_import_task(
        self,
        request: drds_20190123_models.RemoveDataImportTaskRequest,
    ) -> drds_20190123_models.RemoveDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_data_import_task_with_options(request, runtime)

    async def remove_data_import_task_async(
        self,
        request: drds_20190123_models.RemoveDataImportTaskRequest,
    ) -> drds_20190123_models.RemoveDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_data_import_task_with_options_async(request, runtime)

    def remove_drds_db_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            self.do_rpcrequest('RemoveDrdsDb', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_drds_db_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbResponse(),
            await self.do_rpcrequest_async('RemoveDrdsDb', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_db(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_with_options(request, runtime)

    async def remove_drds_db_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbRequest,
    ) -> drds_20190123_models.RemoveDrdsDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_db_with_options_async(request, runtime)

    def remove_drds_db_failed_record_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            self.do_rpcrequest('RemoveDrdsDbFailedRecord', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_drds_db_failed_record_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsDbFailedRecordResponse(),
            await self.do_rpcrequest_async('RemoveDrdsDbFailedRecord', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_db_failed_record(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_db_failed_record_with_options(request, runtime)

    async def remove_drds_db_failed_record_async(
        self,
        request: drds_20190123_models.RemoveDrdsDbFailedRecordRequest,
    ) -> drds_20190123_models.RemoveDrdsDbFailedRecordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_db_failed_record_with_options_async(request, runtime)

    def remove_drds_instance_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            self.do_rpcrequest('RemoveDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsInstanceResponse(),
            await self.do_rpcrequest_async('RemoveDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_instance(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_instance_with_options(request, runtime)

    async def remove_drds_instance_async(
        self,
        request: drds_20190123_models.RemoveDrdsInstanceRequest,
    ) -> drds_20190123_models.RemoveDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_instance_with_options_async(request, runtime)

    def remove_drds_mysql_with_options(
        self,
        request: drds_20190123_models.RemoveDrdsMysqlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsMysqlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsMysqlResponse(),
            self.do_rpcrequest('RemoveDrdsMysql', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_drds_mysql_with_options_async(
        self,
        request: drds_20190123_models.RemoveDrdsMysqlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveDrdsMysqlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveDrdsMysqlResponse(),
            await self.do_rpcrequest_async('RemoveDrdsMysql', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_drds_mysql(
        self,
        request: drds_20190123_models.RemoveDrdsMysqlRequest,
    ) -> drds_20190123_models.RemoveDrdsMysqlResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_drds_mysql_with_options(request, runtime)

    async def remove_drds_mysql_async(
        self,
        request: drds_20190123_models.RemoveDrdsMysqlRequest,
    ) -> drds_20190123_models.RemoveDrdsMysqlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_drds_mysql_with_options_async(request, runtime)

    def remove_evaluate_task_with_options(
        self,
        request: drds_20190123_models.RemoveEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveEvaluateTaskResponse(),
            self.do_rpcrequest('RemoveEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_evaluate_task_with_options_async(
        self,
        request: drds_20190123_models.RemoveEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveEvaluateTaskResponse(),
            await self.do_rpcrequest_async('RemoveEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_evaluate_task(
        self,
        request: drds_20190123_models.RemoveEvaluateTaskRequest,
    ) -> drds_20190123_models.RemoveEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_evaluate_task_with_options(request, runtime)

    async def remove_evaluate_task_async(
        self,
        request: drds_20190123_models.RemoveEvaluateTaskRequest,
    ) -> drds_20190123_models.RemoveEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_evaluate_task_with_options_async(request, runtime)

    def remove_instance_account_with_options(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            self.do_rpcrequest('RemoveInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_instance_account_with_options_async(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveInstanceAccountResponse(),
            await self.do_rpcrequest_async('RemoveInstanceAccount', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_instance_account(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_instance_account_with_options(request, runtime)

    async def remove_instance_account_async(
        self,
        request: drds_20190123_models.RemoveInstanceAccountRequest,
    ) -> drds_20190123_models.RemoveInstanceAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_instance_account_with_options_async(request, runtime)

    def remove_recycle_bin_table_with_options(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            self.do_rpcrequest('RemoveRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_recycle_bin_table_with_options_async(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RemoveRecycleBinTableResponse(),
            await self.do_rpcrequest_async('RemoveRecycleBinTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_recycle_bin_table(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_recycle_bin_table_with_options(request, runtime)

    async def remove_recycle_bin_table_async(
        self,
        request: drds_20190123_models.RemoveRecycleBinTableRequest,
    ) -> drds_20190123_models.RemoveRecycleBinTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_recycle_bin_table_with_options_async(request, runtime)

    def restart_drds_instance_with_options(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            self.do_rpcrequest('RestartDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_drds_instance_with_options_async(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RestartDrdsInstanceResponse(),
            await self.do_rpcrequest_async('RestartDrdsInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_drds_instance(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_drds_instance_with_options(request, runtime)

    async def restart_drds_instance_async(
        self,
        request: drds_20190123_models.RestartDrdsInstanceRequest,
    ) -> drds_20190123_models.RestartDrdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_drds_instance_with_options_async(request, runtime)

    def rollback_instance_version_with_options(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            self.do_rpcrequest('RollbackInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rollback_instance_version_with_options_async(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.RollbackInstanceVersionResponse(),
            await self.do_rpcrequest_async('RollbackInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rollback_instance_version(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_instance_version_with_options(request, runtime)

    async def rollback_instance_version_async(
        self,
        request: drds_20190123_models.RollbackInstanceVersionRequest,
    ) -> drds_20190123_models.RollbackInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_instance_version_with_options_async(request, runtime)

    def set_backup_local_with_options(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            self.do_rpcrequest('SetBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_backup_local_with_options_async(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupLocalResponse(),
            await self.do_rpcrequest_async('SetBackupLocal', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backup_local(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_backup_local_with_options(request, runtime)

    async def set_backup_local_async(
        self,
        request: drds_20190123_models.SetBackupLocalRequest,
    ) -> drds_20190123_models.SetBackupLocalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_backup_local_with_options_async(request, runtime)

    def set_backup_policy_with_options(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            self.do_rpcrequest('SetBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_backup_policy_with_options_async(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetBackupPolicyResponse(),
            await self.do_rpcrequest_async('SetBackupPolicy', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backup_policy(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_backup_policy_with_options(request, runtime)

    async def set_backup_policy_async(
        self,
        request: drds_20190123_models.SetBackupPolicyRequest,
    ) -> drds_20190123_models.SetBackupPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_backup_policy_with_options_async(request, runtime)

    def setup_broadcast_tables_with_options(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            self.do_rpcrequest('SetupBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_broadcast_tables_with_options_async(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupBroadcastTablesResponse(),
            await self.do_rpcrequest_async('SetupBroadcastTables', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_broadcast_tables(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_broadcast_tables_with_options(request, runtime)

    async def setup_broadcast_tables_async(
        self,
        request: drds_20190123_models.SetupBroadcastTablesRequest,
    ) -> drds_20190123_models.SetupBroadcastTablesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_broadcast_tables_with_options_async(request, runtime)

    def setup_drds_params_with_options(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            self.do_rpcrequest('SetupDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_drds_params_with_options_async(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupDrdsParamsResponse(),
            await self.do_rpcrequest_async('SetupDrdsParams', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_drds_params(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_drds_params_with_options(request, runtime)

    async def setup_drds_params_async(
        self,
        request: drds_20190123_models.SetupDrdsParamsRequest,
    ) -> drds_20190123_models.SetupDrdsParamsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_drds_params_with_options_async(request, runtime)

    def setup_recycle_bin_status_with_options(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            self.do_rpcrequest('SetupRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_recycle_bin_status_with_options_async(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupRecycleBinStatusResponse(),
            await self.do_rpcrequest_async('SetupRecycleBinStatus', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_recycle_bin_status(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_recycle_bin_status_with_options(request, runtime)

    async def setup_recycle_bin_status_async(
        self,
        request: drds_20190123_models.SetupRecycleBinStatusRequest,
    ) -> drds_20190123_models.SetupRecycleBinStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_recycle_bin_status_with_options_async(request, runtime)

    def setup_table_with_options(
        self,
        request: drds_20190123_models.SetupTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            self.do_rpcrequest('SetupTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_table_with_options_async(
        self,
        request: drds_20190123_models.SetupTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableResponse(),
            await self.do_rpcrequest_async('SetupTable', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_table(
        self,
        request: drds_20190123_models.SetupTableRequest,
    ) -> drds_20190123_models.SetupTableResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_table_with_options(request, runtime)

    async def setup_table_async(
        self,
        request: drds_20190123_models.SetupTableRequest,
    ) -> drds_20190123_models.SetupTableResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_table_with_options_async(request, runtime)

    def setup_table_async_with_options(
        self,
        request: drds_20190123_models.SetupTableAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableAsyncResponse(),
            self.do_rpcrequest('SetupTableAsync', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def setup_table_async_with_options_async(
        self,
        request: drds_20190123_models.SetupTableAsyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SetupTableAsyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SetupTableAsyncResponse(),
            await self.do_rpcrequest_async('SetupTableAsync', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def setup_table_async(
        self,
        request: drds_20190123_models.SetupTableAsyncRequest,
    ) -> drds_20190123_models.SetupTableAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return self.setup_table_async_with_options(request, runtime)

    async def setup_table_async_async(
        self,
        request: drds_20190123_models.SetupTableAsyncRequest,
    ) -> drds_20190123_models.SetupTableAsyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.setup_table_async_with_options_async(request, runtime)

    def sql_compatibility_cancel_with_options(
        self,
        request: drds_20190123_models.SqlCompatibilityCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SqlCompatibilityCancelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityCancelResponse(),
            self.do_rpcrequest('SqlCompatibilityCancel', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sql_compatibility_cancel_with_options_async(
        self,
        request: drds_20190123_models.SqlCompatibilityCancelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SqlCompatibilityCancelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityCancelResponse(),
            await self.do_rpcrequest_async('SqlCompatibilityCancel', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sql_compatibility_cancel(
        self,
        request: drds_20190123_models.SqlCompatibilityCancelRequest,
    ) -> drds_20190123_models.SqlCompatibilityCancelResponse:
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_cancel_with_options(request, runtime)

    async def sql_compatibility_cancel_async(
        self,
        request: drds_20190123_models.SqlCompatibilityCancelRequest,
    ) -> drds_20190123_models.SqlCompatibilityCancelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sql_compatibility_cancel_with_options_async(request, runtime)

    def sql_compatibility_start_with_options(
        self,
        request: drds_20190123_models.SqlCompatibilityStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SqlCompatibilityStartResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityStartResponse(),
            self.do_rpcrequest('SqlCompatibilityStart', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sql_compatibility_start_with_options_async(
        self,
        request: drds_20190123_models.SqlCompatibilityStartRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SqlCompatibilityStartResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SqlCompatibilityStartResponse(),
            await self.do_rpcrequest_async('SqlCompatibilityStart', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sql_compatibility_start(
        self,
        request: drds_20190123_models.SqlCompatibilityStartRequest,
    ) -> drds_20190123_models.SqlCompatibilityStartResponse:
        runtime = util_models.RuntimeOptions()
        return self.sql_compatibility_start_with_options(request, runtime)

    async def sql_compatibility_start_async(
        self,
        request: drds_20190123_models.SqlCompatibilityStartRequest,
    ) -> drds_20190123_models.SqlCompatibilityStartResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sql_compatibility_start_with_options_async(request, runtime)

    def start_evaluate_task_with_options(
        self,
        request: drds_20190123_models.StartEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartEvaluateTaskResponse(),
            self.do_rpcrequest('StartEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_evaluate_task_with_options_async(
        self,
        request: drds_20190123_models.StartEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartEvaluateTaskResponse(),
            await self.do_rpcrequest_async('StartEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_evaluate_task(
        self,
        request: drds_20190123_models.StartEvaluateTaskRequest,
    ) -> drds_20190123_models.StartEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_evaluate_task_with_options(request, runtime)

    async def start_evaluate_task_async(
        self,
        request: drds_20190123_models.StartEvaluateTaskRequest,
    ) -> drds_20190123_models.StartEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_evaluate_task_with_options_async(request, runtime)

    def start_restore_with_options(
        self,
        request: drds_20190123_models.StartRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartRestoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            self.do_rpcrequest('StartRestore', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_restore_with_options_async(
        self,
        request: drds_20190123_models.StartRestoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StartRestoreResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StartRestoreResponse(),
            await self.do_rpcrequest_async('StartRestore', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_restore(
        self,
        request: drds_20190123_models.StartRestoreRequest,
    ) -> drds_20190123_models.StartRestoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_restore_with_options(request, runtime)

    async def start_restore_async(
        self,
        request: drds_20190123_models.StartRestoreRequest,
    ) -> drds_20190123_models.StartRestoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_restore_with_options_async(request, runtime)

    def stop_data_export_task_with_options(
        self,
        request: drds_20190123_models.StopDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataExportTaskResponse(),
            self.do_rpcrequest('StopDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_data_export_task_with_options_async(
        self,
        request: drds_20190123_models.StopDataExportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopDataExportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataExportTaskResponse(),
            await self.do_rpcrequest_async('StopDataExportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_data_export_task(
        self,
        request: drds_20190123_models.StopDataExportTaskRequest,
    ) -> drds_20190123_models.StopDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_data_export_task_with_options(request, runtime)

    async def stop_data_export_task_async(
        self,
        request: drds_20190123_models.StopDataExportTaskRequest,
    ) -> drds_20190123_models.StopDataExportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_data_export_task_with_options_async(request, runtime)

    def stop_data_import_task_with_options(
        self,
        request: drds_20190123_models.StopDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopDataImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataImportTaskResponse(),
            self.do_rpcrequest('StopDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_data_import_task_with_options_async(
        self,
        request: drds_20190123_models.StopDataImportTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopDataImportTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopDataImportTaskResponse(),
            await self.do_rpcrequest_async('StopDataImportTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_data_import_task(
        self,
        request: drds_20190123_models.StopDataImportTaskRequest,
    ) -> drds_20190123_models.StopDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_data_import_task_with_options(request, runtime)

    async def stop_data_import_task_async(
        self,
        request: drds_20190123_models.StopDataImportTaskRequest,
    ) -> drds_20190123_models.StopDataImportTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_data_import_task_with_options_async(request, runtime)

    def stop_evaluate_task_with_options(
        self,
        request: drds_20190123_models.StopEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopEvaluateTaskResponse(),
            self.do_rpcrequest('StopEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_evaluate_task_with_options_async(
        self,
        request: drds_20190123_models.StopEvaluateTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.StopEvaluateTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.StopEvaluateTaskResponse(),
            await self.do_rpcrequest_async('StopEvaluateTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_evaluate_task(
        self,
        request: drds_20190123_models.StopEvaluateTaskRequest,
    ) -> drds_20190123_models.StopEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_evaluate_task_with_options(request, runtime)

    async def stop_evaluate_task_async(
        self,
        request: drds_20190123_models.StopEvaluateTaskRequest,
    ) -> drds_20190123_models.StopEvaluateTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_evaluate_task_with_options_async(request, runtime)

    def submit_clean_table_sharding_key_modify_with_options(
        self,
        request: drds_20190123_models.SubmitCleanTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitCleanTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_clean_table_sharding_key_modify_with_options_async(
        self,
        request: drds_20190123_models.SubmitCleanTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse(),
            await self.do_rpcrequest_async('SubmitCleanTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_clean_table_sharding_key_modify(
        self,
        request: drds_20190123_models.SubmitCleanTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_table_sharding_key_modify_with_options(request, runtime)

    async def submit_clean_table_sharding_key_modify_async(
        self,
        request: drds_20190123_models.SubmitCleanTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitCleanTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_clean_table_sharding_key_modify_with_options_async(request, runtime)

    def submit_clean_task_with_options(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            self.do_rpcrequest('SubmitCleanTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_clean_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitCleanTaskResponse(),
            await self.do_rpcrequest_async('SubmitCleanTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_clean_task(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_clean_task_with_options(request, runtime)

    async def submit_clean_task_async(
        self,
        request: drds_20190123_models.SubmitCleanTaskRequest,
    ) -> drds_20190123_models.SubmitCleanTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_clean_task_with_options_async(request, runtime)

    def submit_hot_expand_pre_check_task_with_options(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            self.do_rpcrequest('SubmitHotExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_hot_expand_pre_check_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandPreCheckTaskResponse(),
            await self.do_rpcrequest_async('SubmitHotExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_hot_expand_pre_check_task(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_pre_check_task_with_options(request, runtime)

    async def submit_hot_expand_pre_check_task_async(
        self,
        request: drds_20190123_models.SubmitHotExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_hot_expand_pre_check_task_with_options_async(request, runtime)

    def submit_hot_expand_task_with_options(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            self.do_rpcrequest('SubmitHotExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_hot_expand_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitHotExpandTaskResponse(),
            await self.do_rpcrequest_async('SubmitHotExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_hot_expand_task(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_hot_expand_task_with_options(request, runtime)

    async def submit_hot_expand_task_async(
        self,
        request: drds_20190123_models.SubmitHotExpandTaskRequest,
    ) -> drds_20190123_models.SubmitHotExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_hot_expand_task_with_options_async(request, runtime)

    def submit_rollback_sharding_key_modify_with_options(
        self,
        request: drds_20190123_models.SubmitRollbackShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitRollbackShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitRollbackShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitRollbackShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_rollback_sharding_key_modify_with_options_async(
        self,
        request: drds_20190123_models.SubmitRollbackShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitRollbackShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitRollbackShardingKeyModifyResponse(),
            await self.do_rpcrequest_async('SubmitRollbackShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_rollback_sharding_key_modify(
        self,
        request: drds_20190123_models.SubmitRollbackShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitRollbackShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_rollback_sharding_key_modify_with_options(request, runtime)

    async def submit_rollback_sharding_key_modify_async(
        self,
        request: drds_20190123_models.SubmitRollbackShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitRollbackShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_rollback_sharding_key_modify_with_options_async(request, runtime)

    def submit_smooth_expand_pre_check_with_options(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            self.do_rpcrequest('SubmitSmoothExpandPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_smooth_expand_pre_check_with_options_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckResponse(),
            await self.do_rpcrequest_async('SubmitSmoothExpandPreCheck', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_pre_check(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_with_options(request, runtime)

    async def submit_smooth_expand_pre_check_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smooth_expand_pre_check_with_options_async(request, runtime)

    def submit_smooth_expand_pre_check_task_with_options(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            self.do_rpcrequest('SubmitSmoothExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_smooth_expand_pre_check_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse(),
            await self.do_rpcrequest_async('SubmitSmoothExpandPreCheckTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_pre_check_task(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_pre_check_task_with_options(request, runtime)

    async def submit_smooth_expand_pre_check_task_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandPreCheckTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandPreCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smooth_expand_pre_check_task_with_options_async(request, runtime)

    def submit_smooth_expand_task_with_options(
        self,
        request: drds_20190123_models.SubmitSmoothExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandTaskResponse(),
            self.do_rpcrequest('SubmitSmoothExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_smooth_expand_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSmoothExpandTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSmoothExpandTaskResponse(),
            await self.do_rpcrequest_async('SubmitSmoothExpandTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_smooth_expand_task(
        self,
        request: drds_20190123_models.SubmitSmoothExpandTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_smooth_expand_task_with_options(request, runtime)

    async def submit_smooth_expand_task_async(
        self,
        request: drds_20190123_models.SubmitSmoothExpandTaskRequest,
    ) -> drds_20190123_models.SubmitSmoothExpandTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_smooth_expand_task_with_options_async(request, runtime)

    def submit_sql_flashback_task_with_options(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            self.do_rpcrequest('SubmitSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_sql_flashback_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSqlFlashbackTaskResponse(),
            await self.do_rpcrequest_async('SubmitSqlFlashbackTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_sql_flashback_task(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_sql_flashback_task_with_options(request, runtime)

    async def submit_sql_flashback_task_async(
        self,
        request: drds_20190123_models.SubmitSqlFlashbackTaskRequest,
    ) -> drds_20190123_models.SubmitSqlFlashbackTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_sql_flashback_task_with_options_async(request, runtime)

    def submit_switch_table_sharding_key_modify_with_options(
        self,
        request: drds_20190123_models.SubmitSwitchTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitSwitchTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_switch_table_sharding_key_modify_with_options_async(
        self,
        request: drds_20190123_models.SubmitSwitchTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse(),
            await self.do_rpcrequest_async('SubmitSwitchTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_switch_table_sharding_key_modify(
        self,
        request: drds_20190123_models.SubmitSwitchTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_switch_table_sharding_key_modify_with_options(request, runtime)

    async def submit_switch_table_sharding_key_modify_async(
        self,
        request: drds_20190123_models.SubmitSwitchTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitSwitchTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_switch_table_sharding_key_modify_with_options_async(request, runtime)

    def submit_switch_task_with_options(
        self,
        request: drds_20190123_models.SubmitSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTaskResponse(),
            self.do_rpcrequest('SubmitSwitchTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_switch_task_with_options_async(
        self,
        request: drds_20190123_models.SubmitSwitchTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitSwitchTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitSwitchTaskResponse(),
            await self.do_rpcrequest_async('SubmitSwitchTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_switch_task(
        self,
        request: drds_20190123_models.SubmitSwitchTaskRequest,
    ) -> drds_20190123_models.SubmitSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_switch_task_with_options(request, runtime)

    async def submit_switch_task_async(
        self,
        request: drds_20190123_models.SubmitSwitchTaskRequest,
    ) -> drds_20190123_models.SubmitSwitchTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_switch_task_with_options_async(request, runtime)

    def submit_table_sharding_key_modify_with_options(
        self,
        request: drds_20190123_models.SubmitTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitTableShardingKeyModifyResponse(),
            self.do_rpcrequest('SubmitTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_table_sharding_key_modify_with_options_async(
        self,
        request: drds_20190123_models.SubmitTableShardingKeyModifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SubmitTableShardingKeyModifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SubmitTableShardingKeyModifyResponse(),
            await self.do_rpcrequest_async('SubmitTableShardingKeyModify', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_table_sharding_key_modify(
        self,
        request: drds_20190123_models.SubmitTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_table_sharding_key_modify_with_options(request, runtime)

    async def submit_table_sharding_key_modify_async(
        self,
        request: drds_20190123_models.SubmitTableShardingKeyModifyRequest,
    ) -> drds_20190123_models.SubmitTableShardingKeyModifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_table_sharding_key_modify_with_options_async(request, runtime)

    def switch_global_broadcast_type_with_options(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            self.do_rpcrequest('SwitchGlobalBroadcastType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def switch_global_broadcast_type_with_options_async(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.SwitchGlobalBroadcastTypeResponse(),
            await self.do_rpcrequest_async('SwitchGlobalBroadcastType', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def switch_global_broadcast_type(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_global_broadcast_type_with_options(request, runtime)

    async def switch_global_broadcast_type_async(
        self,
        request: drds_20190123_models.SwitchGlobalBroadcastTypeRequest,
    ) -> drds_20190123_models.SwitchGlobalBroadcastTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_global_broadcast_type_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: drds_20190123_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: drds_20190123_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: drds_20190123_models.TagResourcesRequest,
    ) -> drds_20190123_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: drds_20190123_models.TagResourcesRequest,
    ) -> drds_20190123_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
    ) -> drds_20190123_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: drds_20190123_models.UntagResourcesRequest,
    ) -> drds_20190123_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_instance_network_with_options(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            self.do_rpcrequest('UpdateInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_instance_network_with_options_async(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateInstanceNetworkResponse(),
            await self.do_rpcrequest_async('UpdateInstanceNetwork', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_network(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_instance_network_with_options(request, runtime)

    async def update_instance_network_async(
        self,
        request: drds_20190123_models.UpdateInstanceNetworkRequest,
    ) -> drds_20190123_models.UpdateInstanceNetworkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_instance_network_with_options_async(request, runtime)

    def update_private_rds_class_with_options(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            self.do_rpcrequest('UpdatePrivateRdsClass', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_private_rds_class_with_options_async(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdatePrivateRdsClassResponse(),
            await self.do_rpcrequest_async('UpdatePrivateRdsClass', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_private_rds_class(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_private_rds_class_with_options(request, runtime)

    async def update_private_rds_class_async(
        self,
        request: drds_20190123_models.UpdatePrivateRdsClassRequest,
    ) -> drds_20190123_models.UpdatePrivateRdsClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_private_rds_class_with_options_async(request, runtime)

    def update_resource_group_attribute_with_options(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            self.do_rpcrequest('UpdateResourceGroupAttribute', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_resource_group_attribute_with_options_async(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpdateResourceGroupAttributeResponse(),
            await self.do_rpcrequest_async('UpdateResourceGroupAttribute', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_resource_group_attribute(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_attribute_with_options(request, runtime)

    async def update_resource_group_attribute_async(
        self,
        request: drds_20190123_models.UpdateResourceGroupAttributeRequest,
    ) -> drds_20190123_models.UpdateResourceGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_resource_group_attribute_with_options_async(request, runtime)

    def upgrade_hi_store_instance_with_options(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            self.do_rpcrequest('UpgradeHiStoreInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_hi_store_instance_with_options_async(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeHiStoreInstanceResponse(),
            await self.do_rpcrequest_async('UpgradeHiStoreInstance', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_hi_store_instance(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_hi_store_instance_with_options(request, runtime)

    async def upgrade_hi_store_instance_async(
        self,
        request: drds_20190123_models.UpgradeHiStoreInstanceRequest,
    ) -> drds_20190123_models.UpgradeHiStoreInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_hi_store_instance_with_options_async(request, runtime)

    def upgrade_instance_version_with_options(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            self.do_rpcrequest('UpgradeInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_instance_version_with_options_async(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.UpgradeInstanceVersionResponse(),
            await self.do_rpcrequest_async('UpgradeInstanceVersion', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    async def upgrade_instance_version_async(
        self,
        request: drds_20190123_models.UpgradeInstanceVersionRequest,
    ) -> drds_20190123_models.UpgradeInstanceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_instance_version_with_options_async(request, runtime)

    def validate_shard_task_with_options(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            self.do_rpcrequest('ValidateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def validate_shard_task_with_options_async(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.ValidateShardTaskResponse(),
            await self.do_rpcrequest_async('ValidateShardTask', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def validate_shard_task(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.validate_shard_task_with_options(request, runtime)

    async def validate_shard_task_async(
        self,
        request: drds_20190123_models.ValidateShardTaskRequest,
    ) -> drds_20190123_models.ValidateShardTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.validate_shard_task_with_options_async(request, runtime)

    def describe_rds_inst_infos_with_options(
        self,
        request: drds_20190123_models.DescribeRdsInstInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsInstInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsInstInfosResponse(),
            self.do_rpcrequest('describeRdsInstInfos', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_rds_inst_infos_with_options_async(
        self,
        request: drds_20190123_models.DescribeRdsInstInfosRequest,
        runtime: util_models.RuntimeOptions,
    ) -> drds_20190123_models.DescribeRdsInstInfosResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            drds_20190123_models.DescribeRdsInstInfosResponse(),
            await self.do_rpcrequest_async('describeRdsInstInfos', '2019-01-23', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rds_inst_infos(
        self,
        request: drds_20190123_models.DescribeRdsInstInfosRequest,
    ) -> drds_20190123_models.DescribeRdsInstInfosResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_inst_infos_with_options(request, runtime)

    async def describe_rds_inst_infos_async(
        self,
        request: drds_20190123_models.DescribeRdsInstInfosRequest,
    ) -> drds_20190123_models.DescribeRdsInstInfosResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_inst_infos_with_options_async(request, runtime)
